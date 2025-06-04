#!/usr/bin/env python3
"""End-to-end video import pipeline.

This script downloads a video, extracts frames and crops the minimap
region based on ``config.yaml``. Output directories are created using
``data_dirs.py`` so Scrim/tournament data are organised automatically.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

import cv2
import numpy as np
import yaml
import yt_dlp

from data_dirs import create_scrim, create_tournament


def download_video(url: str, out_dir: Path) -> Path:
    """Download ``url`` into ``out_dir`` and return the file path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    if url.startswith("http"):
        ydl = yt_dlp.YoutubeDL({"outtmpl": str(out_dir / "%(_id)s.%(ext)s"), "format": "mp4"})
        info = ydl.extract_info(url, download=True)
        return Path(ydl.prepare_filename(info))
    else:
        src = Path(url.replace("file://", ""))
        dst = out_dir / src.name
        if src.resolve() != dst.resolve():
            shutil.copy2(src, dst)
        return dst


def extract_frames(video: Path, out_dir: Path, fps: float = 0.5, width: int = 1920) -> int:
    """Extract frames using ffmpeg and return frame count."""
    out_dir.mkdir(parents=True, exist_ok=True)
    pattern = out_dir / "frame_%05d.jpg"
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-stats",
        "-i",
        str(video),
        "-vf",
        f"fps={fps},scale={width}:-2",
        "-q:v",
        "2",
        str(pattern),
    ]
    subprocess.run(cmd, check=True)
    return len(list(out_dir.glob("*.jpg")))


def crop_minimap_dir(frames_dir: Path, out_dir: Path, cfg_path: Path = Path("config.yaml")) -> int:
    """Crop minimap region for all JPG images in ``frames_dir``."""
    cfg = yaml.safe_load(open(cfg_path, encoding="utf-8"))
    points = np.array(cfg["roi"], dtype="float32").reshape((-1, 1, 2))
    src_pts = cv2.convexHull(points).reshape(-1, 2).astype("float32")
    dst_w, dst_h = cfg["output_size"]
    dst_pts = np.array([[0, 0], [dst_w, 0], [dst_w, dst_h], [0, dst_h]], dtype="float32")
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for f in sorted(frames_dir.glob("*.jpg")):
        img = cv2.imread(str(f))
        if img is None:
            continue
        warp = cv2.warpPerspective(img, M, (dst_w, dst_h))
        cv2.imwrite(str(out_dir / f.name), warp)
        count += 1
    return count


def main() -> None:
    p = argparse.ArgumentParser(description="Download and preprocess match video")
    p.add_argument("--url", required=True, help="YouTube or direct video URL")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scrim", help="import scrim video")
    s.add_argument("date", help="YYYY/MM/DD format")
    s.add_argument("--rounds", type=int, default=2)

    t = sub.add_parser("tournament", help="import tournament video")
    t.add_argument("name", help="tournament name")

    p.add_argument("--fps", type=float, default=0.5, help="frames per second")
    p.add_argument("--width", type=int, default=1920, help="scaled frame width")
    p.add_argument("--root", default="data", help="root data directory")
    p.add_argument("--config", default="config.yaml", help="ROI config path")
    args = p.parse_args()

    if args.cmd == "scrim":
        base = create_scrim(args.date, rounds=args.rounds, root=args.root)
    else:
        base = create_tournament(args.name, root=args.root)

    raw_dir = base / "raw_videos"
    frames_dir = base / "frames"
    mini_dir = base / "minimaps"

    video = download_video(args.url, raw_dir)
    extract_frames(video, frames_dir, fps=args.fps, width=args.width)
    crop_minimap_dir(frames_dir, mini_dir, Path(args.config))
    print(mini_dir)


if __name__ == "__main__":
    main()
