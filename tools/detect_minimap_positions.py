#!/usr/bin/env python3
"""CLI utilities for detecting player icons on minimap frames.

This script implements two classical computer vision approaches to detect
player icons on minimap frames:

* Template matching using OpenCV ``matchTemplate`` with non-maximum
  suppression.
* HSV colour thresholding with morphology and contour based centroids.

The detector outputs JSON lines per frame for downstream tracking and filling.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Sequence, Tuple

import cv2
import numpy as np

FRAME_SUFFIXES = (".jpg", ".jpeg", ".png")


def extract_frame_index(name: str) -> int:
    """Extract an integer frame index from the filename if possible."""

    digits = "".join(ch for ch in name if ch.isdigit())
    if not digits:
        return 0
    return int(digits)


@dataclass
class Detection:
    """Container for a single detection result."""

    x_px: float
    y_px: float
    score: float
    width: int
    height: int
    method: str

    def to_json(self) -> Dict[str, float | int | str]:
        """Convert the detection to a JSON serialisable dictionary."""

        return {
            "x_px": self.x_px,
            "y_px": self.y_px,
            "score": self.score,
            "width": self.width,
            "height": self.height,
            "method": self.method,
        }


@dataclass
class FrameRecord:
    """Detection results for a single frame."""

    frame_index: int
    image_path: Path
    detections: List[Detection]

    def to_json(self) -> Dict[str, object]:
        """Convert the frame record to a JSON serialisable dictionary."""

        return {
            "frame_index": self.frame_index,
            "image_path": self.image_path.as_posix(),
            "detections": [det.to_json() for det in self.detections],
        }


@dataclass
class TemplateConfig:
    """Configuration for template matching based detection."""

    template_path: Path
    threshold: float
    match_mode_name: str
    match_mode: int
    image: np.ndarray


@dataclass
class HSVConfig:
    """Configuration for HSV threshold based detection."""

    lower: Tuple[int, int, int]
    upper: Tuple[int, int, int]
    morph_kernel: int
    morph_iterations: int
    min_area: float
    max_area: float


@dataclass
class DetectorConfig:
    """Merged configuration for all detection strategies."""

    method: str
    template: Optional[TemplateConfig]
    hsv: Optional[HSVConfig]
    nms_threshold: float
    max_detections: Optional[int]


def parse_triplet(value: str) -> Tuple[int, int, int]:
    """Parse a HSV triplet encoded as ``h,s,v`` string."""

    parts = value.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError(
            f"Expected three comma separated integers, got: {value!r}"
        )
    try:
        h, s, v = (int(p) for p in parts)
    except ValueError as exc:  # pragma: no cover - defensive
        raise argparse.ArgumentTypeError(
            f"HSV triplet requires integers: {value!r}"
        ) from exc
    return h, s, v


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(
        description="Detect player icons on minimap frames (JSONL output)"
    )
    parser.add_argument(
        "frames_dir",
        type=Path,
        help="Directory that contains minimap frame images",
    )
    parser.add_argument(
        "output_jsonl",
        type=Path,
        help="Path to the output JSONL file",
    )
    parser.add_argument(
        "--method",
        choices=("template", "hsv"),
        default="template",
        help="Detection method to use (default: template)",
    )
    parser.add_argument(
        "--template",
        type=Path,
        help="Path to the template image (required for template method)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.75,
        help="Template matching threshold (for template method)",
    )
    parser.add_argument(
        "--match-mode",
        choices=[
            "TM_CCOEFF",
            "TM_CCOEFF_NORMED",
            "TM_CCORR",
            "TM_CCORR_NORMED",
            "TM_SQDIFF",
            "TM_SQDIFF_NORMED",
        ],
        default="TM_CCOEFF_NORMED",
        help="OpenCV template matching mode",
    )
    parser.add_argument(
        "--hsv-lower",
        type=parse_triplet,
        default=(0, 0, 200),
        help="Lower HSV bound as h,s,v (for hsv method)",
    )
    parser.add_argument(
        "--hsv-upper",
        type=parse_triplet,
        default=(180, 80, 255),
        help="Upper HSV bound as h,s,v (for hsv method)",
    )
    parser.add_argument(
        "--morph-kernel",
        type=int,
        default=3,
        help="Kernel size for morphology operations (for hsv method)",
    )
    parser.add_argument(
        "--morph-iterations",
        type=int,
        default=1,
        help="Number of morphology iterations (for hsv method)",
    )
    parser.add_argument(
        "--min-area",
        type=float,
        default=6.0,
        help="Minimum contour area to keep (for hsv method)",
    )
    parser.add_argument(
        "--max-area",
        type=float,
        default=400.0,
        help="Maximum contour area to keep (for hsv method)",
    )
    parser.add_argument(
        "--nms-threshold",
        type=float,
        default=0.3,
        help="IoU threshold for non-maximum suppression",
    )
    parser.add_argument(
        "--max-detections",
        type=int,
        default=None,
        help="Optional cap on the number of detections per frame after NMS",
    )
    return parser.parse_args()


def load_template(path: Path, match_mode: str) -> Tuple[np.ndarray, int]:
    """Load the template image and resolve the OpenCV matching mode."""

    if not path:
        raise ValueError("Template path must be provided for template matching")
    template = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if template is None:
        raise FileNotFoundError(f"Failed to load template image: {path}")
    mode = getattr(cv2, match_mode)
    return template, mode


def list_frame_paths(frames_dir: Path) -> List[Path]:
    """Return frame image paths sorted lexicographically."""

    if not frames_dir.is_dir():
        raise FileNotFoundError(f"Frames directory not found: {frames_dir}")
    paths = sorted(
        [p for p in frames_dir.iterdir() if p.suffix.lower() in FRAME_SUFFIXES],
        key=lambda p: extract_frame_index(p.name),
    )
    if not paths:
        message = (
            "No frame images with suffix " f"{FRAME_SUFFIXES} found in {frames_dir}"
        )
        raise FileNotFoundError(message)
    return paths


def compute_iou(
    box_a: Tuple[int, int, int, int], box_b: Tuple[int, int, int, int]
) -> float:
    """Compute intersection over union for two bounding boxes."""

    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b
    inter_x1 = max(ax1, bx1)
    inter_y1 = max(ay1, by1)
    inter_x2 = min(ax2, bx2)
    inter_y2 = min(ay2, by2)
    inter_w = max(0, inter_x2 - inter_x1)
    inter_h = max(0, inter_y2 - inter_y1)
    inter_area = inter_w * inter_h
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    union = area_a + area_b - inter_area
    if union <= 0:
        return 0.0
    return inter_area / union


def nms(
    boxes: Sequence[Tuple[int, int, int, int]],
    scores: Sequence[float],
    threshold: float,
    max_detections: Optional[int] = None,
) -> List[int]:
    """Perform non-maximum suppression and return kept indices."""

    if not boxes:
        return []
    indices = np.argsort(scores)[::-1]
    keep: List[int] = []
    while indices.size > 0:
        current = int(indices[0])
        keep.append(current)
        if max_detections is not None and len(keep) >= max_detections:
            break
        current_box = boxes[current]
        remaining = []
        for idx in indices[1:]:
            idx_int = int(idx)
            iou = compute_iou(current_box, boxes[idx_int])
            if iou <= threshold:
                remaining.append(idx_int)
        indices = np.array(remaining, dtype=int)
    return keep


def detections_from_template(
    image: np.ndarray,
    template: np.ndarray,
    threshold: float,
    method_name: str,
    match_mode: int,
    nms_threshold: float,
    max_detections: Optional[int],
) -> List[Detection]:
    """Run template matching and convert peaks to detections."""

    if template is None:
        raise ValueError("Template image must be provided for template detection")
    if match_mode is None:
        raise ValueError("Match mode must be provided for template detection")
    result = cv2.matchTemplate(image, template, match_mode)
    if match_mode in (cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED):
        loc = np.where(result <= threshold)
        scores = result[loc]
        boxes = []
        det_scores = []
        for (y, x), score in zip(zip(*loc), scores):
            boxes.append((x, y, x + template.shape[1], y + template.shape[0]))
            det_scores.append(1.0 - float(score))
    else:
        loc = np.where(result >= threshold)
        scores = result[loc]
        boxes = []
        det_scores = []
        for (y, x), score in zip(zip(*loc), scores):
            boxes.append((x, y, x + template.shape[1], y + template.shape[0]))
            det_scores.append(float(score))
    kept = nms(boxes, det_scores, nms_threshold, max_detections)
    detections: List[Detection] = []
    for idx in kept:
        x1, y1, x2, y2 = boxes[idx]
        score = det_scores[idx]
        detections.append(
            Detection(
                x_px=x1 + (x2 - x1) / 2.0,
                y_px=y1 + (y2 - y1) / 2.0,
                score=max(0.0, min(1.0, float(score))),
                width=x2 - x1,
                height=y2 - y1,
                method=f"template:{method_name}",
            )
        )
    return detections


def detections_from_hsv(
    image: np.ndarray,
    hsv_config: HSVConfig,
    nms_threshold: float,
    max_detections: Optional[int],
) -> List[Detection]:
    """Run HSV thresholding and contour analysis to produce detections."""

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array(hsv_config.lower, dtype=np.uint8)
    upper = np.array(hsv_config.upper, dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (hsv_config.morph_kernel, hsv_config.morph_kernel)
    )
    cleaned = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel, iterations=hsv_config.morph_iterations
    )
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes: List[Tuple[int, int, int, int]] = []
    scores: List[float] = []
    detections: List[Detection] = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < hsv_config.min_area or area > hsv_config.max_area:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        boxes.append((x, y, x + w, y + h))
        scores.append(float(area))
    kept = nms(boxes, scores, nms_threshold, max_detections)
    for idx in kept:
        x1, y1, x2, y2 = boxes[idx]
        w = x2 - x1
        h = y2 - y1
        detection = Detection(
            x_px=x1 + w / 2.0,
            y_px=y1 + h / 2.0,
            score=1.0,
            width=w,
            height=h,
            method="hsv",
        )
        detections.append(detection)
    return detections


def build_detector_config(args: argparse.Namespace) -> DetectorConfig:
    """Build the runtime detector configuration from command line arguments."""

    template_config: Optional[TemplateConfig] = None
    hsv_config: Optional[HSVConfig] = None
    if args.method == "template":
        if args.template is None:
            raise ValueError("--template is required when using method='template'")
        template_image, match_mode = load_template(args.template, args.match_mode)
        template_config = TemplateConfig(
            template_path=args.template,
            threshold=args.threshold,
            match_mode_name=args.match_mode,
            match_mode=match_mode,
            image=template_image,
        )
    else:
        hsv_config = HSVConfig(
            lower=args.hsv_lower,
            upper=args.hsv_upper,
            morph_kernel=args.morph_kernel,
            morph_iterations=args.morph_iterations,
            min_area=args.min_area,
            max_area=args.max_area,
        )
    return DetectorConfig(
        method=args.method,
        template=template_config,
        hsv=hsv_config,
        nms_threshold=args.nms_threshold,
        max_detections=args.max_detections,
    )


def iter_frames(paths: Sequence[Path]) -> Iterator[Tuple[int, Path, np.ndarray]]:
    """Yield ``(frame_index, path, image)`` triples for the given paths."""

    for path in sorted(paths, key=lambda p: extract_frame_index(p.name)):
        frame_index = extract_frame_index(path.name)
        image = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if image is None:
            print(f"[WARN] Failed to load image: {path}", file=sys.stderr)
            continue
        yield frame_index, path, image


def run_detection(config: DetectorConfig, frames_dir: Path) -> List[FrameRecord]:
    """Execute detection over all frames in the directory."""

    start = time.perf_counter()
    frame_paths = list_frame_paths(frames_dir)
    frame_records: List[FrameRecord] = []
    template_image: Optional[np.ndarray] = None
    match_mode: Optional[int] = None
    template_name: Optional[str] = None
    if config.method == "template":
        assert config.template is not None  # pragma: no cover - validated earlier
        template_name = config.template.match_mode_name
        template_image = config.template.image
        match_mode = config.template.match_mode
        template_h, template_w = template_image.shape[:2]
        template_message = (
            "[INFO] Template matching with template "
            f"{config.template.template_path} "
            f"size=({template_w}x{template_h}), "
            f"threshold={config.template.threshold}"
        )
        print(template_message, file=sys.stderr)
    else:
        assert config.hsv is not None  # pragma: no cover - validated earlier
        hsv_message = (
            "[INFO] HSV thresholding "
            f"lower={config.hsv.lower} "
            f"upper={config.hsv.upper} "
            f"area=({config.hsv.min_area}, {config.hsv.max_area})"
        )
        print(hsv_message, file=sys.stderr)
    for progress_index, (frame_index, path, image) in enumerate(
        iter_frames(frame_paths), start=1
    ):
        if progress_index % 50 == 1:
            progress_message = (
                f"[INFO] Processing frame {progress_index}/{len(frame_paths)} "
                f"(frame_index={frame_index}): {path.name}"
            )
            print(progress_message, file=sys.stderr)
        if config.method == "template":
            detections = detections_from_template(
                image=image,
                template=template_image,
                threshold=config.template.threshold,
                method_name=template_name or "template",
                match_mode=match_mode,
                nms_threshold=config.nms_threshold,
                max_detections=config.max_detections,
            )
        else:
            detections = detections_from_hsv(
                image=image,
                hsv_config=config.hsv,
                nms_threshold=config.nms_threshold,
                max_detections=config.max_detections,
            )
        frame_records.append(
            FrameRecord(frame_index=frame_index, image_path=path, detections=detections)
        )
    elapsed = time.perf_counter() - start
    total_detections = sum(len(record.detections) for record in frame_records)
    summary_message = (
        f"[INFO] Processed {len(frame_records)} frames "
        f"with {total_detections} detections "
        f"in {elapsed:.2f}s"
    )
    print(summary_message, file=sys.stderr)
    return frame_records


def save_results(records: Sequence[FrameRecord], output_path: Path) -> None:
    """Write detection results as JSON lines."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record.to_json(), ensure_ascii=False) + "\n")
    print(
        f"[INFO] Wrote detection results to {output_path} ({len(records)} frames)",
        file=sys.stderr,
    )


def main() -> None:
    """CLI entry point."""

    args = parse_args()
    config = build_detector_config(args)
    records = run_detection(config, args.frames_dir)
    save_results(records, args.output_jsonl)


if __name__ == "__main__":  # pragma: no cover - CLI entry
    try:
        main()
    except Exception as exc:  # pragma: no cover - CLI error handling
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)
