#!/usr/bin/env python3

import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path
from typing import List

FRAME_RE = re.compile(r"frame[_-]?(\d+)\.(?:jpg|jpeg|png)$", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build empty positions index (64 players per frame) with progress"
    )
    parser.add_argument("minimap_dir", type=str, help="Path to minimap frames directory")
    parser.add_argument("match_id", type=str, help="Match ID, e.g., 2025-09-18_PMJL_Erangel1")
    parser.add_argument("map_name", type=str, help="Map name, e.g., erangel")
    parser.add_argument("map_round", type=str, help="Map round, e.g., Erangel1")
    parser.add_argument("roster_csv", type=str, help="Roster CSV path (must include 'player_uid' column)")
    parser.add_argument("output_jsonl", type=str, help="Output JSONL file path")
    parser.add_argument("--fps", type=float, default=2.0, help="Frames per second (default: 2.0)")
    parser.add_argument("--progress-interval", type=float, default=0.25, help="Progress refresh interval seconds")
    return parser.parse_args()


def read_roster(roster_csv: Path) -> List[str]:
    t0 = time.perf_counter()
    player_uids: List[str] = []
    with open(roster_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "player_uid" not in reader.fieldnames:
            raise ValueError("Roster CSV must contain 'player_uid' column")
        for row in reader:
            uid = row.get("player_uid")
            if uid:
                player_uids.append(uid)
    dt = time.perf_counter() - t0
    print(f"[DEBUG] read_roster: loaded {len(player_uids)} players in {dt:.3f}s", file=sys.stderr)
    return player_uids


def scan_frames(minimap_dir: Path) -> List[Path]:
    t0 = time.perf_counter()
    frames = [p for p in minimap_dir.iterdir() if p.is_file() and FRAME_RE.search(p.name)]
    frames.sort(key=lambda p: int(FRAME_RE.search(p.name).group(1)))
    dt = time.perf_counter() - t0
    print(f"[DEBUG] scan_frames: found {len(frames)} frames in {dt:.3f}s", file=sys.stderr)
    return frames


def frame_index_of(path: Path) -> int:
    m = FRAME_RE.search(path.name)
    if not m:
        raise ValueError(f"Unrecognized frame filename: {path}")
    return int(m.group(1))


def human(n: float) -> str:
    # Human-friendly big number formatter
    if n >= 1_000_000:
        return f"{n/1_000_000:.2f}M"
    if n >= 1_000:
        return f"{n/1_000:.2f}k"
    return f"{int(n)}"


def print_progress(done: int, total: int, start_time: float, prefix: str = "") -> None:
    # Single-line progress bar with ETA and throughput
    now = time.perf_counter()
    elapsed = max(1e-9, now - start_time)
    rate = done / elapsed
    pct = 0.0 if total == 0 else done / total
    eta = (total - done) / rate if rate > 0 else float("inf")
    bar_len = 24
    filled = int(bar_len * pct)
    bar = "#" * filled + "-" * (bar_len - filled)
    msg = (
        f"\r{prefix}[{bar}] {pct*100:6.2f}%  | {human(done)}/{human(total)} recs  "
        f"{rate:7.1f} rec/s  ETA {eta:6.1f}s"
    )
    sys.stderr.write(msg)
    sys.stderr.flush()


def main() -> None:
    args = parse_args()

    print("[INFO] Building empty positions index (skeleton mode, v1.1)...", file=sys.stderr)
    print(f"[INFO] minimap_dir={args.minimap_dir}", file=sys.stderr)
    print(f"[INFO] match_id={args.match_id}  map_name={args.map_name}  map_round={args.map_round}", file=sys.stderr)
    print(f"[INFO] fps={args.fps}", file=sys.stderr)

    t0 = time.perf_counter()
    players = read_roster(Path(args.roster_csv))
    frames = scan_frames(Path(args.minimap_dir))

    if not frames:
        raise SystemExit("No frames found. Check directory and filename pattern (frame_00001.jpg etc.)")
    if not players:
        raise SystemExit("No players in roster. 'player_uid' column required.")

    fps = float(args.fps)
    ms_per_frame = int(1000.0 / fps)

    out_path = Path(args.output_jsonl)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    expected_records = len(frames) * len(players)
    print(f"[INFO] frames={len(frames)} players={len(players)} => records≈{expected_records}", file=sys.stderr)

    n_records = 0
    last_refresh = 0.0

    with open(out_path, "w", encoding="utf-8") as out:
        for i, frame_path in enumerate(frames, 1):
            idx = frame_index_of(frame_path)
            ts_ms = (idx - 1) * ms_per_frame
            for uid in players:
                try:
                    team_id, player_slot = uid.split("-")
                except ValueError:
                    team_id, player_slot = uid, "P?"
                rec = {
                    "match_id": args.match_id,
                    "map_name": args.map_name,
                    "map_round": args.map_round,
                    "frame_index": idx,
                    "ts_ms": ts_ms,
                    "image_path": str(frame_path.as_posix()),
                    "team_id": team_id,
                    "player_slot": player_slot,
                    "player_uid": uid,
                    "status": "unknown",
                    "px_x": None,
                    "px_y": None,
                    "x_norm": None,
                    "y_norm": None,
                    "confidence": None,
                    "calib_id": None,
                    "notes": None,
                }
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_records += 1

            # progress refresh
            now = time.perf_counter()
            if now - last_refresh >= float(args.progress_interval):
                print_progress(n_records, expected_records, t0, prefix="[WRITE] ")
                last_refresh = now

    # final progress line
    print_progress(n_records, expected_records, t0, prefix="[WRITE] ")
    sys.stderr.write("\n")

    dt = time.perf_counter() - t0
    print(f"[INFO] Wrote {n_records} records to {out_path} in {dt:.2f}s", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
