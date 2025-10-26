#!/usr/bin/env python3
"""Assign detections to player tracks using frame-to-frame association.

This tool reads detection results produced by ``detect_minimap_positions.py``
and associates them with players listed in a roster CSV file. The association
uses a constant-velocity prediction model combined with the Hungarian algorithm
for optimal assignment. Unmatched players are temporarily marked as
``unknown``; prolonged missing detections transition to ``eliminated`` status.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
from scipy.optimize import linear_sum_assignment


@dataclass
class DetectionObservation:
    """Representation of a detection in a frame."""

    x_px: float
    y_px: float
    score: float
    method: str


@dataclass
class FrameDetections:
    """Detections available for a particular frame."""

    frame_index: int
    image_path: Path
    detections: List[DetectionObservation]


@dataclass
class TrackState:
    """State of an individual player track."""

    player_uid: str
    last_frame_index: Optional[int] = None
    last_position: Optional[Tuple[float, float]] = None
    velocity: Tuple[float, float] = (0.0, 0.0)
    missing_frames: int = 0
    status: str = "unknown"
    eliminated: bool = False
    last_confidence: float = 0.0
    notes: str = ""

    def predict(self, frame_index: int) -> Tuple[float, float]:
        """Predict the next position using constant velocity."""

        if self.last_frame_index is None or self.last_position is None:
            return (0.0, 0.0)
        delta = max(1, frame_index - self.last_frame_index)
        return (
            self.last_position[0] + self.velocity[0] * delta,
            self.last_position[1] + self.velocity[1] * delta,
        )

    def update_with_detection(
        self,
        frame_index: int,
        detection: DetectionObservation,
        velocity_damping: float,
    ) -> None:
        """Update the track with a matched detection."""

        if self.last_position is not None and self.last_frame_index is not None:
            delta = max(1, frame_index - self.last_frame_index)
            new_velocity = (
                (detection.x_px - self.last_position[0]) / delta,
                (detection.y_px - self.last_position[1]) / delta,
            )
            self.velocity = (
                velocity_damping * self.velocity[0]
                + (1.0 - velocity_damping) * new_velocity[0],
                velocity_damping * self.velocity[1]
                + (1.0 - velocity_damping) * new_velocity[1],
            )
        self.last_position = (detection.x_px, detection.y_px)
        self.last_frame_index = frame_index
        self.missing_frames = 0
        self.status = "alive"
        self.eliminated = False
        self.last_confidence = max(0.0, min(1.0, detection.score))
        self.notes = f"assigned via Hungarian ({detection.method})"

    def mark_missing(self, eliminate_after: int) -> None:
        """Increase missing counter and update status accordingly."""

        self.missing_frames += 1
        if eliminate_after >= 0 and self.missing_frames > eliminate_after:
            self.status = "eliminated"
            self.eliminated = True
            self.last_confidence = 0.0
            self.notes = f"missing for {self.missing_frames} frames, marked eliminated"
        else:
            self.status = "unknown"
            if eliminate_after >= 0:
                denom = max(1, eliminate_after)
            else:
                denom = max(1, self.missing_frames)
            self.last_confidence = max(0.0, 1.0 - self.missing_frames / denom)
            self.notes = f"no detection for {self.missing_frames} frames"


@dataclass
class Assignment:
    """Assignment for a single player in a frame."""

    player_uid: str
    px_x: Optional[float]
    px_y: Optional[float]
    score: Optional[float]
    status: str
    confidence: float
    notes: str

    def to_json(self) -> Dict[str, object]:
        """Convert the assignment to JSON serialisable format."""

        return {
            "player_uid": self.player_uid,
            "px_x": self.px_x,
            "px_y": self.px_y,
            "score": self.score,
            "status": self.status,
            "confidence": self.confidence,
            "notes": self.notes,
        }


@dataclass
class FrameAssignments:
    """Assignments generated for a frame."""

    frame_index: int
    image_path: Path
    assignments: List[Assignment]

    def to_json(self) -> Dict[str, object]:
        """Convert to JSON serialisable structure."""

        assignments_data = [assignment.to_json() for assignment in self.assignments]
        return {
            "frame_index": self.frame_index,
            "image_path": self.image_path.as_posix(),
            "assignments": assignments_data,
        }


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(
        description="Assign minimap detections to players using Hungarian tracking",
    )
    parser.add_argument("detections_jsonl", type=Path, help="Detections JSONL path")
    parser.add_argument(
        "roster_csv", type=Path, help="Roster CSV with player_uid column"
    )
    parser.add_argument("output_jsonl", type=Path, help="Assignments JSONL output path")
    parser.add_argument(
        "--max-missed",
        type=int,
        default=5,
        help="Number of frames to keep a track alive without detections",
    )
    parser.add_argument(
        "--eliminate-after",
        type=int,
        default=12,
        help=(
            "Frames after which an unseen player is marked eliminated "
            "(negative to disable)"
        ),
    )
    parser.add_argument(
        "--distance-threshold",
        type=float,
        default=60.0,
        help="Maximum pixel distance for an assignment to be considered valid",
    )
    parser.add_argument(
        "--velocity-damping",
        type=float,
        default=0.5,
        help=("Damping factor for velocity updates (0=new velocity, " "1=keep old)"),
    )
    return parser.parse_args()


def read_roster(roster_csv: Path) -> List[str]:
    """Load player UIDs from the roster CSV file."""

    start = time.perf_counter()
    player_uids: List[str] = []
    with roster_csv.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if "player_uid" not in reader.fieldnames:
            raise ValueError("Roster CSV must contain a player_uid column")
        for row in reader:
            uid = row.get("player_uid")
            if uid:
                player_uids.append(uid)
    duration = time.perf_counter() - start
    message = (
        f"[INFO] Loaded {len(player_uids)} players from {roster_csv} "
        f"in {duration:.2f}s"
    )
    print(message, file=sys.stderr)
    if not player_uids:
        raise ValueError("Roster CSV did not contain any player_uid entries")
    return player_uids


def load_detections(detections_path: Path) -> List[FrameDetections]:
    """Load detections JSON lines into structured records."""

    records: List[FrameDetections] = []
    start = time.perf_counter()
    with detections_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            data = json.loads(line)
            frame_index = int(data["frame_index"])
            image_path = Path(data["image_path"])
            detections_json = data.get("detections", [])
            detections: List[DetectionObservation] = []
            for det in detections_json:
                detections.append(
                    DetectionObservation(
                        x_px=float(det["x_px"]),
                        y_px=float(det["y_px"]),
                        score=float(det.get("score", 0.0)),
                        method=str(det.get("method", "unknown")),
                    )
                )
            records.append(
                FrameDetections(
                    frame_index=frame_index,
                    image_path=image_path,
                    detections=detections,
                )
            )
    duration = time.perf_counter() - start
    message = (
        f"[INFO] Loaded detections for {len(records)} frames from "
        f"{detections_path} in {duration:.2f}s"
    )
    print(message, file=sys.stderr)
    return records


def initialise_tracks(player_uids: Sequence[str]) -> Dict[str, TrackState]:
    """Create TrackState objects for all players."""

    return {uid: TrackState(player_uid=uid) for uid in player_uids}


def greedy_initial_assignment(
    frame: FrameDetections, tracks: Dict[str, TrackState], player_uids: Sequence[str]
) -> FrameAssignments:
    """Assign the first frame using a deterministic greedy strategy."""

    sorted_pairs = sorted(enumerate(frame.detections), key=lambda pair: pair[1].x_px)
    assignments: List[Assignment] = []
    for idx, player_uid in enumerate(player_uids):
        track = tracks[player_uid]
        if idx < len(sorted_pairs):
            det_index, detection = sorted_pairs[idx]
            track.update_with_detection(
                frame.frame_index, detection, velocity_damping=0.0
            )
            assignments.append(
                Assignment(
                    player_uid=player_uid,
                    px_x=detection.x_px,
                    px_y=detection.y_px,
                    score=detection.score,
                    status=track.status,
                    confidence=track.last_confidence,
                    notes=f"initial assignment (detection #{det_index})",
                )
            )
        else:
            track.mark_missing(eliminate_after=-1)
            assignments.append(
                Assignment(
                    player_uid=player_uid,
                    px_x=None,
                    px_y=None,
                    score=None,
                    status=track.status,
                    confidence=track.last_confidence,
                    notes="no detection available in initial frame",
                )
            )
    return FrameAssignments(
        frame_index=frame.frame_index,
        image_path=frame.image_path,
        assignments=assignments,
    )


def build_cost_matrix(
    frame_index: int,
    detections: Sequence[DetectionObservation],
    tracks: Sequence[TrackState],
    distance_threshold: float,
) -> Tuple[np.ndarray, float]:
    """Construct the cost matrix for Hungarian assignment."""

    num_tracks = len(tracks)
    num_detections = len(detections)
    if num_tracks == 0 or num_detections == 0:
        return np.empty((num_tracks, num_detections)), distance_threshold * 10.0
    max_cost = distance_threshold * 10.0
    cost_matrix = np.full((num_tracks, num_detections), max_cost, dtype=float)
    for i, track in enumerate(tracks):
        predicted = track.predict(frame_index)
        for j, detection in enumerate(detections):
            distance = math.dist(predicted, (detection.x_px, detection.y_px))
            if distance <= distance_threshold:
                cost_matrix[i, j] = distance
    return cost_matrix, max_cost


def run_assignment(
    frames: Sequence[FrameDetections],
    player_uids: Sequence[str],
    max_missed: int,
    eliminate_after: int,
    distance_threshold: float,
    velocity_damping: float,
) -> List[FrameAssignments]:
    """Run the tracking loop and produce frame assignments."""

    if not frames:
        raise ValueError("No detection frames were provided")
    tracks = initialise_tracks(player_uids)
    results: List[FrameAssignments] = []
    first_frame = frames[0]
    init_message = (
        "[INFO] Performing greedy initial assignment for frame "
        f"{first_frame.frame_index}"
    )
    print(init_message, file=sys.stderr)
    results.append(greedy_initial_assignment(first_frame, tracks, player_uids))
    for frame in frames[1:]:
        detections = frame.detections
        track_list = [tracks[uid] for uid in player_uids]
        cost_matrix, max_cost = build_cost_matrix(
            frame.frame_index, detections, track_list, distance_threshold
        )
        assignments: Dict[str, Assignment] = {}
        if cost_matrix.size > 0:
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            for row, col in zip(row_ind, col_ind):
                if cost_matrix[row, col] >= max_cost:
                    continue
                track = track_list[row]
                detection = detections[col]
                track.update_with_detection(
                    frame.frame_index, detection, velocity_damping
                )
                distance_note = f"assigned with distance {cost_matrix[row, col]:.2f}"
                assignments[track.player_uid] = Assignment(
                    player_uid=track.player_uid,
                    px_x=detection.x_px,
                    px_y=detection.y_px,
                    score=detection.score,
                    status=track.status,
                    confidence=track.last_confidence,
                    notes=distance_note,
                )
        for player_uid, track in tracks.items():
            if player_uid in assignments:
                continue
            track.mark_missing(eliminate_after)
            if track.missing_frames <= max_missed or eliminate_after < 0:
                assignments[player_uid] = Assignment(
                    player_uid=player_uid,
                    px_x=track.last_position[0] if track.last_position else None,
                    px_y=track.last_position[1] if track.last_position else None,
                    score=None,
                    status=track.status,
                    confidence=track.last_confidence,
                    notes=track.notes,
                )
            else:
                assignments[player_uid] = Assignment(
                    player_uid=player_uid,
                    px_x=None,
                    px_y=None,
                    score=None,
                    status=track.status,
                    confidence=track.last_confidence,
                    notes=track.notes,
                )
        assigned_count = sum(
            1 for assignment in assignments.values() if assignment.status == "alive"
        )
        unknown_count = sum(
            1 for assignment in assignments.values() if assignment.status == "unknown"
        )
        eliminated_count = sum(
            1
            for assignment in assignments.values()
            if assignment.status == "eliminated"
        )
        summary = (
            f"[INFO] Frame {frame.frame_index}: detections={len(detections)} "
            f"assigned={assigned_count} unknown={unknown_count} "
            f"eliminated={eliminated_count}"
        )
        print(summary, file=sys.stderr)
        ordered_assignments = [assignments[uid] for uid in player_uids]
        results.append(
            FrameAssignments(
                frame_index=frame.frame_index,
                image_path=frame.image_path,
                assignments=ordered_assignments,
            )
        )
    return results


def save_assignments(records: Sequence[FrameAssignments], output_path: Path) -> None:
    """Write frame assignments as JSON lines."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record.to_json(), ensure_ascii=False) + "\n")
    message = f"[INFO] Wrote assignments for {len(records)} frames to {output_path}"
    print(message, file=sys.stderr)


def main() -> None:
    """Program entry point."""

    args = parse_args()
    player_uids = read_roster(args.roster_csv)
    frames = load_detections(args.detections_jsonl)
    records = run_assignment(
        frames=frames,
        player_uids=player_uids,
        max_missed=args.max_missed,
        eliminate_after=args.eliminate_after,
        distance_threshold=args.distance_threshold,
        velocity_damping=args.velocity_damping,
    )
    save_assignments(records, args.output_jsonl)


if __name__ == "__main__":  # pragma: no cover - CLI guard
    try:
        main()
    except Exception as exc:  # pragma: no cover - CLI error handling
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)
