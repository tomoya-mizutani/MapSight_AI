# Red Team Detector (Version 1 & 2)

This document describes the HSV/contour-based red team detector implemented in
`src/mapsight/analysis/red_team_detector.py`. The detector locates red
nameplates (e.g., `Faze_***`) and returns the center coordinates of the paired
red circle markers.

## Overview

The detection pipeline follows these stages:

1. **HSV thresholding**: isolate red regions using two hue ranges.
2. **Morphology cleanup**: open/close operations to reduce noise.
3. **Contour extraction**: find external contours from the red mask.
4. **Shape classification**:
   - wide, filled rectangles → nameplates
   - near-circular blobs → circle markers
5. **Pairing**: match each rectangle to the closest circle within a distance
   threshold.

## Quick Start (CLI)

```bash
python -m mapsight.analysis.red_team_detector /path/to/minimap.png
```

Output is one `x,y` coordinate per detected red team circle center.

### Annotated Output (Version 2)

To visually verify the detections, provide an output path to write an annotated
image. The detector highlights nameplates and circle centers using a fluorescent
yellow overlay by default.

```bash
python -m mapsight.analysis.red_team_detector /path/to/minimap.png \
  --output /path/to/annotated.png
```

## Python API

```python
from mapsight.analysis import RedTeamDetector

detector = RedTeamDetector()
detections = detector.detect("minimap.png")

for detection in detections:
    print(detection.circle_center)
```

Each `RedTeamDetection` contains:

- `label_bbox`: `(x, y, w, h)` bounding box of the red nameplate rectangle
- `circle_center`: `(x, y)` center of the matched circle marker

## Configuration

Use `RedTeamDetectorConfig` to tune thresholds:

```python
from mapsight.analysis import RedTeamDetector, RedTeamDetectorConfig

config = RedTeamDetectorConfig(
    min_rect_area=300,
    max_match_distance=80.0,
)
detector = RedTeamDetector(config)
```

Key parameters:

- `min_rect_area`, `min_rect_aspect`, `max_rect_aspect`, `min_rect_fill_ratio`
  control rectangle filtering.
- `min_circle_area`, `max_circle_area`, `min_circle_circularity` control circle
  filtering.
- `max_match_distance` controls the label-to-circle pairing range.
- `red_hsv_lower_*`, `red_hsv_upper_*` control the HSV red thresholding.

## Annotation Configuration (Version 2)

Use `RedTeamAnnotationConfig` to customize the overlay colors and line widths.

```python
from mapsight.analysis import RedTeamAnnotationConfig, RedTeamDetector

annotation = RedTeamAnnotationConfig(
    label_color_bgr=(0, 255, 255),
    circle_color_bgr=(0, 255, 255),
    crosshair_color_bgr=(0, 255, 255),
)
detector = RedTeamDetector(annotation_config=annotation)
```

Call `annotate()` to save the overlay:

```python
detector.annotate("minimap.png", detections, output_path="annotated.png")
```
