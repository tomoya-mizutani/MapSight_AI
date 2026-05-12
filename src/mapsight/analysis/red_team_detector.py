"""Detect red-team player positions based on red nameplates and circle markers."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple

import cv2
import numpy as np


@dataclass(frozen=True)
class RedTeamDetection:
    label_bbox: Tuple[int, int, int, int]
    circle_center: Tuple[int, int]


@dataclass(frozen=True)
class RedTeamDetectorConfig:
    min_rect_area: int = 300
    min_rect_aspect: float = 2.0
    max_rect_aspect: float = 8.0
    min_rect_fill_ratio: float = 0.6
    min_circle_area: int = 40
    max_circle_area: int = 1200
    min_circle_circularity: float = 0.6
    max_match_distance: float = 70.0
    red_hsv_lower_1: Tuple[int, int, int] = (0, 120, 70)
    red_hsv_upper_1: Tuple[int, int, int] = (10, 255, 255)
    red_hsv_lower_2: Tuple[int, int, int] = (170, 120, 70)
    red_hsv_upper_2: Tuple[int, int, int] = (180, 255, 255)


@dataclass(frozen=True)
class RedTeamAnnotationConfig:
    label_color_bgr: Tuple[int, int, int] = (0, 255, 255)
    circle_color_bgr: Tuple[int, int, int] = (0, 255, 255)
    crosshair_color_bgr: Tuple[int, int, int] = (0, 255, 255)
    line_thickness: int = 2
    crosshair_radius: int = 8


class RedTeamDetector:
    """Detect red team label/circle pairs and return circle centers."""

    def __init__(
        self,
        config: RedTeamDetectorConfig | None = None,
        annotation_config: RedTeamAnnotationConfig | None = None,
    ) -> None:
        self.config = config or RedTeamDetectorConfig()
        self.annotation_config = annotation_config or RedTeamAnnotationConfig()

    def detect(self, image_path: Path | str) -> List[RedTeamDetection]:
        image = self._load_image(image_path)
        mask = self._create_red_mask(image)
        contours = self._find_contours(mask)
        label_rects, circle_contours = self._split_contours(contours)
        circle_centers = self._circle_centers(circle_contours)
        return self._match_labels_to_circles(label_rects, circle_centers)

    def annotate(
        self,
        image_path: Path | str,
        detections: Iterable[RedTeamDetection],
        *,
        output_path: Path | str | None = None,
    ) -> np.ndarray:
        image = self._load_image(image_path)
        annotated = self._draw_detections(image, detections)
        if output_path is not None:
            self._write_image(output_path, annotated)
        return annotated

    def _load_image(self, image_path: Path | str) -> np.ndarray:
        path = Path(image_path)
        image = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(f"Image not found or unreadable: {path}")
        return image

    def _create_red_mask(self, image: np.ndarray) -> np.ndarray:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower1 = np.array(self.config.red_hsv_lower_1, dtype=np.uint8)
        upper1 = np.array(self.config.red_hsv_upper_1, dtype=np.uint8)
        lower2 = np.array(self.config.red_hsv_lower_2, dtype=np.uint8)
        upper2 = np.array(self.config.red_hsv_upper_2, dtype=np.uint8)
        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        mask = cv2.bitwise_or(mask1, mask2)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        return mask

    def _write_image(self, output_path: Path | str, image: np.ndarray) -> None:
        path = Path(output_path)
        if not cv2.imwrite(str(path), image):
            raise ValueError(f"Failed to write annotated image to: {path}")

    def _find_contours(self, mask: np.ndarray) -> List[np.ndarray]:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def _split_contours(
        self, contours: Iterable[np.ndarray]
    ) -> Tuple[List[Tuple[int, int, int, int]], List[np.ndarray]]:
        label_rects: List[Tuple[int, int, int, int]] = []
        circle_contours: List[np.ndarray] = []
        for contour in contours:
            if self._is_label_rect(contour):
                label_rects.append(cv2.boundingRect(contour))
            elif self._is_circle(contour):
                circle_contours.append(contour)
        return label_rects, circle_contours

    def _is_label_rect(self, contour: np.ndarray) -> bool:
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if area < self.config.min_rect_area or h == 0:
            return False
        aspect_ratio = w / float(h)
        if not (self.config.min_rect_aspect <= aspect_ratio <= self.config.max_rect_aspect):
            return False
        fill_ratio = area / float(w * h)
        return fill_ratio >= self.config.min_rect_fill_ratio

    def _is_circle(self, contour: np.ndarray) -> bool:
        area = cv2.contourArea(contour)
        if not (self.config.min_circle_area <= area <= self.config.max_circle_area):
            return False
        perimeter = cv2.arcLength(contour, True)
        if perimeter == 0:
            return False
        circularity = 4 * np.pi * area / (perimeter ** 2)
        return circularity >= self.config.min_circle_circularity

    def _circle_centers(self, contours: Iterable[np.ndarray]) -> List[Tuple[int, int]]:
        centers: List[Tuple[int, int]] = []
        for contour in contours:
            moments = cv2.moments(contour)
            if moments["m00"] == 0:
                continue
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])
            centers.append((center_x, center_y))
        return centers

    def _match_labels_to_circles(
        self,
        label_rects: Iterable[Tuple[int, int, int, int]],
        circle_centers: Iterable[Tuple[int, int]],
    ) -> List[RedTeamDetection]:
        detections: List[RedTeamDetection] = []
        for rect in label_rects:
            rect_center = self._rect_center(rect)
            matched_center = self._closest_circle(rect_center, circle_centers)
            if matched_center is None:
                continue
            detections.append(
                RedTeamDetection(label_bbox=rect, circle_center=matched_center)
            )
        return detections

    def _rect_center(self, rect: Tuple[int, int, int, int]) -> Tuple[int, int]:
        x, y, w, h = rect
        return (int(x + w / 2), int(y + h / 2))

    def _closest_circle(
        self, rect_center: Tuple[int, int], circle_centers: Iterable[Tuple[int, int]]
    ) -> Tuple[int, int] | None:
        best_center = None
        best_distance = self.config.max_match_distance
        for center in circle_centers:
            distance = float(np.hypot(center[0] - rect_center[0], center[1] - rect_center[1]))
            if distance <= best_distance:
                best_distance = distance
                best_center = center
        return best_center

    def _draw_detections(
        self, image: np.ndarray, detections: Iterable[RedTeamDetection]
    ) -> np.ndarray:
        annotated = image.copy()
        for detection in detections:
            self._draw_label_box(annotated, detection.label_bbox)
            self._draw_circle_marker(annotated, detection.circle_center)
            self._draw_crosshair(annotated, detection.circle_center)
        return annotated

    def _draw_label_box(self, image: np.ndarray, bbox: Tuple[int, int, int, int]) -> None:
        x, y, w, h = bbox
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            self.annotation_config.label_color_bgr,
            self.annotation_config.line_thickness,
        )

    def _draw_circle_marker(self, image: np.ndarray, center: Tuple[int, int]) -> None:
        cv2.circle(
            image,
            center,
            self.annotation_config.crosshair_radius,
            self.annotation_config.circle_color_bgr,
            self.annotation_config.line_thickness,
        )

    def _draw_crosshair(self, image: np.ndarray, center: Tuple[int, int]) -> None:
        radius = self.annotation_config.crosshair_radius
        cx, cy = center
        cv2.line(
            image,
            (cx - radius, cy),
            (cx + radius, cy),
            self.annotation_config.crosshair_color_bgr,
            self.annotation_config.line_thickness,
        )
        cv2.line(
            image,
            (cx, cy - radius),
            (cx, cy + radius),
            self.annotation_config.crosshair_color_bgr,
            self.annotation_config.line_thickness,
        )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Detect red-team circle centers paired with red nameplates."
    )
    parser.add_argument("image_path", type=Path, help="Path to the minimap image.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path to save an annotated image.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    detector = RedTeamDetector()
    detections = detector.detect(args.image_path)
    for detection in detections:
        print(f"{detection.circle_center[0]},{detection.circle_center[1]}")
    if args.output is not None:
        detector.annotate(args.image_path, detections, output_path=args.output)


if __name__ == "__main__":
    main()
