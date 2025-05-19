#!/usr/bin/env python3
"""
segment_rounds.py – Automatically split mixed PUBG‑Mobile frames into round
folders using **match‑end template detection** + perceptual hashing fallback.

USAGE (examples)
----------------
# Peek mode – show detected boundaries only
python segment_rounds.py data/frames --template templates/end_template.png --peek

# Physically move frames into Round1…Round5 under the project root
python segment_rounds.py data/frames --template templates/end_template.png

OPTIONS
-------
positional:
  frames_dir            directory that contains extracted JPG frames; if omitted
                        the script looks for "data/frames" relative to project
                        root.

optional:
  -o, --out-root PATH   where to create RoundX folders (default: project root)
  -s, --segments N      number of rounds in the video (default: 5)
  -t, --template PATH   template image of the "試合終了 / MATCH FINISHED" text
                        cropped tightly (required for accurate split)
  --end-th FLOAT        template match threshold (default: 0.75)
  --phash-th INT        hamming distance threshold for pHash fallback (default: 10)
  --peek                do not move files, just print detected boundaries
  --dry-run             alias to --peek (kept for backward compatibility)

REQUIREMENTS
------------
* OpenCV‑Python ≥ 4.5
* tqdm
* numpy

The script is **location‑agnostic**: it determines the project root two levels
above this file, so running from src/ or root works the same.
"""
from __future__ import annotations

import argparse
import math
import os
import shutil
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def compute_phash(img: np.ndarray) -> int:
    """Return 64‑bit perceptual hash of the image (grayscale ndarray)."""
    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
    img = np.float32(img)
    dct = cv2.dct(img)
    dct_low = dct[:8, :8]
    med = np.median(dct_low[1:])  # skip DC term
    bits = (dct_low > med).flatten()
    hash_val = 0
    for b in bits:
        hash_val = (hash_val << 1) | int(b)
    return hash_val


def hamming(a: int, b: int) -> int:
    return (a ^ b).bit_count()


def read_gray(path: Path) -> np.ndarray:
    arr = np.fromfile(str(path), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Cannot decode {path}")
    return img


def detect_template(frame: np.ndarray, tmpl: np.ndarray, end_th: float) -> bool:
    res = cv2.matchTemplate(frame, tmpl, cv2.TM_CCOEFF_NORMED)
    max_val = float(res.max())
    return max_val >= end_th


# -----------------------------------------------------------------------------
# Core processing per frame (multithreaded)
# -----------------------------------------------------------------------------

def worker(args):
    path, tmpl_bytes, end_th = args
    try:
        frame = read_gray(path)
    except Exception:
        return None
    # Dark frame filter (too dim)
    if frame.mean() < 10:
        return (path.name, None, False)  # skip phash – treated as blank
    p_hash = compute_phash(frame)

    is_end = False
    if tmpl_bytes is not None:
        tmpl = cv2.imdecode(tmpl_bytes, cv2.IMREAD_GRAYSCALE)
        is_end = detect_template(frame, tmpl, end_th)
    return (path.name, p_hash, is_end)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Split frames into round folders")
    parser.add_argument("frames_dir", nargs="?", default=None,
                        help="directory containing JPG frames (default: data/frames)")
    parser.add_argument("-o", "--out-root", default=None,
                        help="output root to create RoundX folders (default: project root)")
    parser.add_argument("-s", "--segments", type=int, default=5,
                        help="number of rounds contained in the video (default: 5)")
    parser.add_argument("-t", "--template", required=True,
                        help="path to MATCH FINISHED template image")
    parser.add_argument("--end-th", type=float, default=0.75,
                        help="template match correlation threshold")
    parser.add_argument("--phash-th", type=int, default=10,
                        help="hamming threshold for pHash fallback peaks")
    parser.add_argument("--peek", action="store_true", help="preview only, no file move")
    parser.add_argument("--dry-run", action="store_true", help=argparse.SUPPRESS)

    args = parser.parse_args()
    if args.dry_run:
        args.peek = True

    # Resolve project root (two levels above script location)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent.parent

    # Resolve frames directory
    if args.frames_dir is None:
        frames_dir = project_root / "data" / "frames"
    else:
        frames_dir = Path(args.frames_dir)
        if not frames_dir.exists():
            frames_dir_alt = project_root / "data" / args.frames_dir
            if frames_dir_alt.exists():
                frames_dir = frames_dir_alt
    if not frames_dir.exists():
        sys.exit(f"No JPG frames found: {frames_dir}")

    # Resolve output root
    out_root = Path(args.out_root) if args.out_root else project_root

    # Template bytes pre‑read
    tmpl_path = Path(args.template)
    if not tmpl_path.exists():
        sys.exit("Template image not found: " + str(tmpl_path))
    tmpl_bytes = np.fromfile(str(tmpl_path), dtype=np.uint8)

    # Gather frame paths
    jpgs = sorted(frames_dir.glob("*.jpg"))
    if not jpgs:
        sys.exit(f"No JPG files in {frames_dir}")

    # Parallel processing
    tasks = [(p, tmpl_bytes, args.end_th) for p in jpgs]
    phashes = {}
    end_indices = []
    with ProcessPoolExecutor() as ex:
        for res in tqdm(ex.map(worker, tasks, chunksize=128), total=len(tasks)):
            if res is None:
                continue
            name, ph, is_end = res
            idx = int(name.split("_")[-1].split(".")[0])
            if ph is not None:
                phashes[idx] = ph
            if is_end:
                end_indices.append(idx)

    end_indices = sorted(end_indices)

    # If not enough ends found, supplement with pHash peaks
    if len(end_indices) < args.segments - 1:
        # Build distance list
        sorted_idx = sorted(phashes)
        dists = [hamming(phashes[i], phashes[j]) for i, j in zip(sorted_idx[:-1], sorted_idx[1:])]
        peaks = []
        for i, d in enumerate(dists):
            if d >= args.phash_th:
                peaks.append(sorted_idx[i + 1])
        # Merge with end_indices and take earliest N‑1 unique
        end_indices = sorted(set(end_indices + peaks))[: args.segments - 1]

    if len(end_indices) < args.segments - 1:
        print("Warning: boundary count < expected segments‑1; results may be off.")

    # Print summary / peek mode
    boundaries_str = ", ".join(map(str, end_indices))
    print(f"Detected boundaries: {boundaries_str}")
    if args.peek:
        return

    # ------------------------------------------------------------------
    # Move frames into RoundX
    # ------------------------------------------------------------------
    round_dirs = []
    for i in range(1, args.segments + 1):
        rd = out_root / f"Round{i}"
        rd.mkdir(parents=True, exist_ok=True)
        round_dirs.append(rd)

    boundary_ptrs = end_indices + [math.inf]
    cur_round = 0
    moved = 0
    for jp in jpgs:
        idx = int(jp.stem.split("_")[-1])
        if idx >= boundary_ptrs[cur_round]:
            cur_round += 1
        target_dir = round_dirs[min(cur_round, args.segments - 1)]
        shutil.move(str(jp), target_dir / jp.name)
        moved += 1

    print(f"Moved {moved} frames into {args.segments} round folders under {out_root}")


if __name__ == "__main__":
    main()
