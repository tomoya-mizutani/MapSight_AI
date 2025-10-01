"""Utilities for analyzing and visualizing player position time series."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd

REQUIRED_FIELDS = {
    "match_id",
    "map_name",
    "map_round",
    "frame_index",
    "ts_ms",
    "image_path",
    "team_id",
    "player_slot",
    "player_uid",
    "status",
    "px_x",
    "px_y",
    "x_norm",
    "y_norm",
}


def _canonicalize_identifier(identifier: str) -> str:
    lowered = identifier.lower()
    match = re.search(
        r"team\s*0*(?P<team>\d{1,2})[^0-9a-z]*(?:player|p)\s*0*(?P<slot>\d)",
        lowered,
    )
    if match:
        team_number = int(match.group("team"))
        slot_number = int(match.group("slot"))
        return f"team{team_number:02d}p{slot_number}"
    cleaned = re.sub(r"[^0-9a-z]", "", lowered)
    return cleaned


def load_player_positions(source: Path | str) -> pd.DataFrame:
    """Load player position records from a JSONL or Parquet file."""

    path = Path(source)
    if not path.exists():
        raise FileNotFoundError(f"Player positions file not found: {path}")

    if path.suffix.lower() == ".jsonl":
        dataframe = pd.read_json(path, lines=True)
    elif path.suffix.lower() in {".json", ".ndjson"}:
        dataframe = pd.read_json(path, lines=True)
    elif path.suffix.lower() == ".parquet":
        dataframe = pd.read_parquet(path)
    else:
        raise ValueError(
            f"Unsupported file extension '{path.suffix}'. Expected .jsonl or .parquet"
        )

    missing = REQUIRED_FIELDS.difference(dataframe.columns)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing required columns: {missing_list}")

    dataframe = dataframe.copy()
    dataframe["player_uid_canonical"] = dataframe["player_uid"].astype(str).map(
        _canonicalize_identifier
    )
    dataframe.sort_values(["ts_ms", "frame_index"], inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    return dataframe


@dataclass
class PlayerTrajectory:
    """Convenience wrapper around a player's time-ordered position records."""

    player_uid: str
    dataframe: pd.DataFrame

    def ensure_columns(self) -> None:
        missing = REQUIRED_FIELDS.difference(self.dataframe.columns)
        if missing:
            missing_list = ", ".join(sorted(missing))
            raise ValueError(f"Trajectory missing required columns: {missing_list}")

    def coordinate_series(self, use_normalized: bool = True) -> Tuple[pd.Series, pd.Series]:
        x_column, y_column = ("x_norm", "y_norm") if use_normalized else ("px_x", "px_y")
        return self.dataframe[x_column], self.dataframe[y_column]

    def filtered_coordinates(
        self,
        use_normalized: bool = True,
    ) -> Tuple[np.ndarray, np.ndarray, pd.Series]:
        x_values, y_values = self.coordinate_series(use_normalized=use_normalized)
        mask = x_values.notna() & y_values.notna()
        filtered_dataframe = self.dataframe.loc[mask]
        return (
            filtered_dataframe[x_values.name].to_numpy(dtype=float),
            filtered_dataframe[y_values.name].to_numpy(dtype=float),
            filtered_dataframe["ts_ms"],
        )


def get_player_trajectory(
    dataframe: pd.DataFrame,
    player_identifier: str,
    *,
    team_identifier: Optional[str] = None,
    player_slot: Optional[str] = None,
) -> PlayerTrajectory:
    """Extract a single player's trajectory from the full dataset."""

    if "player_uid_canonical" not in dataframe.columns:
        raise ValueError("Dataframe missing 'player_uid_canonical'. Use load_player_positions().")

    canonical_identifier = _canonicalize_identifier(player_identifier)
    mask = dataframe["player_uid_canonical"] == canonical_identifier

    if team_identifier is not None:
        mask &= dataframe["team_id"].astype(str).str.lower() == team_identifier.lower()

    if player_slot is not None:
        mask &= dataframe["player_slot"].astype(str).str.lower() == player_slot.lower()

    trajectory_frame = dataframe.loc[mask].copy()

    if trajectory_frame.empty:
        raise ValueError(
            "No records found for the requested player identifier."
        )

    trajectory_frame.sort_values(["ts_ms", "frame_index"], inplace=True)

    most_common_uid = (
        trajectory_frame["player_uid"].mode().iat[0]
        if not trajectory_frame["player_uid"].mode().empty
        else player_identifier
    )

    return PlayerTrajectory(player_uid=most_common_uid, dataframe=trajectory_frame.reset_index(drop=True))


def compute_player_summary(trajectory: PlayerTrajectory) -> Dict[str, object]:
    """Return high-level metrics describing the player's activity."""

    trajectory.ensure_columns()
    data = trajectory.dataframe

    start_timestamp = int(data["ts_ms"].min())
    end_timestamp = int(data["ts_ms"].max())
    duration_ms = end_timestamp - start_timestamp

    status_counts = data["status"].value_counts(dropna=False).to_dict()

    x_norm_values, y_norm_values, _ = trajectory.filtered_coordinates(use_normalized=True)
    normalized_distance = compute_path_length(x_norm_values, y_norm_values)

    x_pixel_values, y_pixel_values, _ = trajectory.filtered_coordinates(use_normalized=False)
    pixel_distance = compute_path_length(x_pixel_values, y_pixel_values)

    summary = {
        "player_uid": trajectory.player_uid,
        "match_id": data["match_id"].iloc[0],
        "map_round": data["map_round"].iloc[0],
        "team_id": data["team_id"].iloc[0],
        "frames": int(len(data)),
        "start_timestamp_ms": start_timestamp,
        "end_timestamp_ms": end_timestamp,
        "duration_ms": duration_ms,
        "status_counts": status_counts,
        "normalized_path_length": normalized_distance,
        "pixel_path_length": pixel_distance,
    }
    return summary


def compute_path_length(x_values: np.ndarray, y_values: np.ndarray) -> float:
    if len(x_values) < 2 or len(y_values) < 2:
        return 0.0
    deltas = np.sqrt(np.diff(x_values) ** 2 + np.diff(y_values) ** 2)
    length = float(np.sum(deltas))
    if math.isnan(length):
        return 0.0
    return length


def plot_player_trajectory(
    trajectory: PlayerTrajectory,
    *,
    use_normalized_coordinates: bool = True,
    map_image_path: Optional[Path | str] = None,
    output_path: Optional[Path | str] = None,
    show_figure: bool = False,
    title: Optional[str] = None,
) -> Path | None:
    """Create a line plot showing the player's movement path."""

    trajectory.ensure_columns()

    x_values, y_values, _ = trajectory.filtered_coordinates(
        use_normalized=use_normalized_coordinates
    )
    if len(x_values) == 0:
        raise ValueError("No coordinate data available for plotting.")

    try:
        import matplotlib.pyplot as plt
        from matplotlib.ticker import MultipleLocator
    except ImportError as exc:
        raise RuntimeError("matplotlib is required for plotting trajectories") from exc

    if map_image_path is not None:
        map_path = Path(map_image_path)
        if not map_path.exists():
            raise FileNotFoundError(f"Map image not found: {map_path}")
        image_data = plt.imread(map_path)
        height, width = image_data.shape[:2]
    else:
        image_data = None
        height, width = 1, 1

    x_label, y_label = ("Normalized X", "Normalized Y") if use_normalized_coordinates else ("Pixel X", "Pixel Y")

    figure, axis = plt.subplots(figsize=(7, 7))

    if image_data is not None:
        extent = (0, 1, 1, 0) if use_normalized_coordinates else (0, width, height, 0)
        axis.imshow(image_data, extent=extent, alpha=0.8)
    else:
        axis.set_facecolor("#1b1b1b")

    axis.plot(
        x_values,
        y_values,
        color="#03a9f4",
        linewidth=2.5,
        marker="o",
        markersize=3,
        label="Trajectory",
    )

    axis.scatter([x_values[0]], [y_values[0]], color="#4caf50", s=60, label="Start")
    axis.scatter([x_values[-1]], [y_values[-1]], color="#f44336", s=60, label="End")

    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)

    chart_title = title or f"Trajectory for {trajectory.player_uid}"
    axis.set_title(chart_title)
    axis.legend(loc="best")

    if use_normalized_coordinates:
        axis.set_xlim(0, 1)
        axis.set_ylim(1, 0)
        axis.xaxis.set_major_locator(MultipleLocator(0.1))
        axis.yaxis.set_major_locator(MultipleLocator(0.1))
    else:
        axis.invert_yaxis()

    axis.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    if output_path is not None:
        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(destination, dpi=200, bbox_inches="tight")
    else:
        destination = None

    if show_figure:
        plt.show()

    plt.close(figure)

    if destination is not None:
        return destination
    return None
