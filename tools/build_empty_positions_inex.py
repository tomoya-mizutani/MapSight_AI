#!/usr/bin/env python3

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from typing import List

FRAME_RE = re.compile(r"frame[_-]?(\d+)\.(?:jpg|jpeg|png)$", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build empty positions index (64 players per frame)"
    )
    parser.add_argument("minimap_dir", type=str, help="Path to minimap frames directory")
    parser.add_argument("match_id", type=str, help="Match ID, e.g., 2025-09-21_PMJL_R1")
    parser.add_argument("map_name", type=str, help="Map name, e.g., erangel")
    parser.add_argument("map_round", type=str, help="Map round, e.g., R1")
    parser.add_argument("roster_csv", type=str, help="Roster CSV path")
    parser.add_argument("output_jsonl", type=str, help="Output JSONL file path")
    parser.add_argument("--fps", type=float, default=2.0, help="Frames per second (default: 2.0)")
    return parser.parse_args()


def read_roster(roster_csv: Path) -> List[str]:
    start = time.perf_counter()
    players: List[str] = []
    with open(roster_csv, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(',')
        idx_uid = header.index("player_uid")
        for line in f:
            items = line.strip().split(',')
            if len(items) <= idx_uid:
                continue
            players.append(items[idx_uid])
    dur = time.perf_counter() - start
    print(f"[DEBUG] read_roster: loaded {len(players)} players in {dur:.3f}s", file=sys.stderr)
    return players


def scan_frames(minimap_dir: Path) -> List[Path]:
    start = time.perf_counter()
    frames = sorted(
        [p for p in minimap_dir.iterdir() if p.is_file() and FRAME_RE.search(p.name)],
        key=lambda p: int(FRAME_RE.search(p.name).group(1))
    )
    dur = time.perf_counter() - start
    print(f"[DEBUG] scan_frames: found {len(frames)} frames in {dur:.3f}s", file=sys.stderr)
    return frames


def frame_index_of(path: Path) -> int:
    m = FRAME_RE.search(path.name)
    if not m:
        raise ValueError(f"Unrecognized frame filename: {path}")
    return int(m.group(1))


def main() -> None:
    args = parse_args()

    t0 = time.perf_counter()
    print("[INFO] Building empty positions index (skeleton mode)...", file=sys.stderr)
    players = read_roster(Path(args.roster_csv))
    frames = scan_frames(Path(args.minimap_dir))

    n_records = 0
    fps = float(args.fps)
    ms_per_frame = int(1000.0 / fps)

    out_path = Path(args.output_jsonl)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as out:
        for i, frame_path in enumerate(frames, 1):
            idx = frame_index_of(frame_path)
            ts_ms = (idx - 1) * ms_per_frame
            if i % 50 == 1:
                print(f"[INFO] processing frame {i}/{len(frames)} (idx={idx}, ts_ms={ts_ms})", file=sys.stderr)
            for uid in players:
                rec = {
                    "match_id": args.match_id,
                    "map_name": args.map_name,
                    "map_round": args.map_round,
                    "frame_index": idx,
                    "ts_ms": ts_ms,
                    "image_path": str(frame_path.as_posix()),
                    # roster から復元（TEAMxx, Pn を uid から解析する運用でもOK）
                    "team_id": uid.split('-')[0],
                    "player_slot": uid.split('-')[1],
                    "player_uid": uid,
                    # 検出前の雛形
                    "status": "unknown",
                    "px_x": None,
                    "px_y": None,
                    "x_norm": None,
                    "y_norm": None,
                    "confidence": None,
                    "calib_id": None,
                    "notes": None
                }
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_records += 1

    sec = time.perf_counter() - t0
    print(f"[INFO] Wrote {n_records} records to {out_path} in {sec:.2f}s", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)