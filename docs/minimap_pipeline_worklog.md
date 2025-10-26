# Minimap Pipeline Implementation Worklog

## Overview

This document summarises the implementation work carried out to deliver the
prototype minimap processing pipeline consisting of detection, tracking, and
position filling utilities.

## Phase A – Detection

- Added `tools/detect_minimap_positions.py` implementing two classical CV
  detection pipelines:
  - Template matching (OpenCV `matchTemplate`) with non-maximum suppression.
  - HSV colour thresholding with morphological denoising and contour centroid
    extraction.
- Outputs JSONL records with per-frame detections, logging progress and timing
  information for traceability.

## Phase B – ID Assignment

- Added `tools/assign_tracks_to_players.py` which ingests detection JSONL files
  and associates detections with roster entries using:
  - A greedy initial assignment on the first frame.
  - Constant-velocity prediction plus Hungarian matching for subsequent frames.
  - Missing detection handling with configurable grace periods and elimination
    thresholds.
- Emits frame-by-frame assignment JSONL files including status, confidence, and
  diagnostic notes.

## Phase C – Position Filling

- Added `tools/fill_positions_jsonl.py` to merge assignments into the skeleton
  positions JSONL:
  - Fills pixel and normalised coordinates using cached image dimension lookups.
  - Applies calibration identifiers, status management safeguards, and note
    propagation.
  - Logs processing throughput and summary statistics.

## Additional Notes

- All new CLI tools include robust argument parsing, structured logging, and
  defensive error handling.
- The pipeline supports flexible downstream experimentation thanks to JSONL
  interoperability between phases.

## Testing Workflow

- Execute `flake8 tools/detect_minimap_positions.py tools/assign_tracks_to_players.py tools/fill_positions_jsonl.py` to enforce repository style guidelines prior to functional checks.
- Run `pytest tests/` to validate the shared helper modules that support the three CLIs; ensure optional OpenCV dependencies are installed locally to avoid import errors.
- For CLI-level smoke tests, invoke each script with a reduced sample dataset:
  - `python tools/detect_minimap_positions.py --input data/minimaps/sample --output tmp/detections.jsonl`
  - `python tools/assign_tracks_to_players.py --detections tmp/detections.jsonl --output tmp/assignments.jsonl`
  - `python tools/fill_positions_jsonl.py --assignments tmp/assignments.jsonl --positions data/positions/index.jsonl --output tmp/positions_filled.jsonl`
- Review the generated JSONL files to verify that detections, assignments, and filled positions share consistent frame counts and roster coverage before running the full dataset.
