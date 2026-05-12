import json
from pathlib import Path

import matplotlib
import numpy as np
import pytest

from mapsight.analysis import (
    PlayerTrajectory,
    compute_player_summary,
    get_player_trajectory,
    load_player_positions,
    plot_player_trajectory,
)


@pytest.fixture()
def sample_positions_file(tmp_path: Path) -> Path:
    records = [
        {
            "match_id": "match-001",
            "map_name": "erangel",
            "map_round": "Erangel1",
            "frame_index": 1,
            "ts_ms": 0,
            "image_path": "frame_00001.jpg",
            "team_id": "TEAM01",
            "player_slot": "P1",
            "player_uid": "TEAM01-P1",
            "status": "alive",
            "px_x": 120.0,
            "px_y": 380.0,
            "x_norm": 0.12,
            "y_norm": 0.38,
            "confidence": 0.9,
            "calib_id": None,
            "notes": None,
        },
        {
            "match_id": "match-001",
            "map_name": "erangel",
            "map_round": "Erangel1",
            "frame_index": 2,
            "ts_ms": 1000,
            "image_path": "frame_00002.jpg",
            "team_id": "TEAM01",
            "player_slot": "P1",
            "player_uid": "TEAM01-P1",
            "status": "alive",
            "px_x": 240.0,
            "px_y": 250.0,
            "x_norm": 0.24,
            "y_norm": 0.25,
            "confidence": 0.92,
            "calib_id": None,
            "notes": None,
        },
        {
            "match_id": "match-001",
            "map_name": "erangel",
            "map_round": "Erangel1",
            "frame_index": 2,
            "ts_ms": 1000,
            "image_path": "frame_00002.jpg",
            "team_id": "TEAM01",
            "player_slot": "P2",
            "player_uid": "TEAM01-P2",
            "status": "alive",
            "px_x": 400.0,
            "px_y": 300.0,
            "x_norm": 0.40,
            "y_norm": 0.30,
            "confidence": 0.88,
            "calib_id": None,
            "notes": None,
        },
    ]
    output_path = tmp_path / "positions.jsonl"
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record))
            handle.write("\n")
    return output_path


def test_get_player_trajectory_with_flexible_identifier(sample_positions_file: Path) -> None:
    dataframe = load_player_positions(sample_positions_file)
    trajectory = get_player_trajectory(
        dataframe,
        "Team1player1",
        team_identifier="TEAM01",
        player_slot="P1",
    )
    assert isinstance(trajectory, PlayerTrajectory)
    assert len(trajectory.dataframe) == 2
    assert trajectory.player_uid == "TEAM01-P1"

    summary = compute_player_summary(trajectory)
    assert summary["frames"] == 2
    assert summary["duration_ms"] == 1000
    assert pytest.approx(summary["normalized_path_length"], rel=1e-3) == pytest.approx(
        np.sqrt((0.24 - 0.12) ** 2 + (0.25 - 0.38) ** 2),
        rel=1e-3,
    )
    assert pytest.approx(summary["pixel_path_length"], rel=1e-3) == pytest.approx(
        np.sqrt((240.0 - 120.0) ** 2 + (250.0 - 380.0) ** 2),
        rel=1e-3,
    )


def test_plot_player_trajectory_creates_file(sample_positions_file: Path, tmp_path: Path) -> None:
    matplotlib.use("Agg")
    dataframe = load_player_positions(sample_positions_file)
    trajectory = get_player_trajectory(dataframe, "TEAM01-P1")

    output_path = tmp_path / "trajectory.png"
    result_path = plot_player_trajectory(
        trajectory,
        output_path=output_path,
        use_normalized_coordinates=True,
        show_figure=False,
    )

    assert result_path == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
