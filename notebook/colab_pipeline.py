"""Utilities for running the MapSight_AI pipeline on Google Colab.

The helper classes in this module mirror the workflow that previously lived in
``MapSight_AI_Colab.ipynb``.  Each component is intentionally small and can be
combined from scripts or interactive notebooks.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterator, List, Sequence

import cv2
import numpy as np
import yaml
from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
)
from tqdm import tqdm


def _phash64(image: np.ndarray, hash_size: int) -> int:
    """Compute a 64-bit perceptual hash from the given image."""

    resized = cv2.resize(
        image, (hash_size * 4, hash_size * 4), interpolation=cv2.INTER_AREA
    )
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dct = cv2.dct(gray)
    low_frequencies = dct[:hash_size, :hash_size]
    flattened = low_frequencies.flatten()[1:]
    median = float(np.median(flattened))
    bits = (flattened > median).astype(np.uint8)
    bits = np.pad(bits, (0, 64 - len(bits)), constant_values=0)
    hash_value = 0
    for bit in bits:
        hash_value = (hash_value << 1) | int(bit)
    return hash_value


def _hash_file_for_pool(args: tuple[Path, int]) -> tuple[Path, int]:
    """Compute a perceptual hash in a ProcessPool friendly function."""

    path, hash_size = args
    data = np.fromfile(path, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    if image is None:
        return path, -1
    return path, _phash64(image, hash_size)


@dataclass(frozen=True)
class NotebookPathConfig:
    """Container object that keeps track of the Colab directory layout."""

    base_path: Path
    data_path: Path
    frames_path: Path
    minimaps_path: Path
    templates_path: Path
    deleted_frames_path: Path

    @classmethod
    def from_base_path(cls, base_path: Path) -> "NotebookPathConfig":
        base_path = base_path.expanduser().resolve()
        data_path = base_path / "data"
        return cls(
            base_path=base_path,
            data_path=data_path,
            frames_path=data_path / "frames",
            minimaps_path=data_path / "minimaps",
            templates_path=data_path / "templates",
            deleted_frames_path=data_path / "deleted_frames",
        )

    def resolve(
        self, path_str: str | None, *, default_dir: Path | None = None
    ) -> Path:
        if path_str:
            candidate = Path(path_str)
            if candidate.is_absolute():
                return candidate
            return self.base_path / candidate
        if default_dir is None:
            raise ValueError(
                "A default directory must be provided when path_str is None"
            )
        return default_dir


class DirectoryManager:
    """Creates the directory hierarchy used inside Google Drive."""

    def __init__(self, config: NotebookPathConfig) -> None:
        self.config = config

    def ensure_directories(self) -> None:
        for directory in self._iter_directories():
            directory.mkdir(parents=True, exist_ok=True)

    def _iter_directories(self) -> Iterator[Path]:
        yield self.config.base_path
        yield self.config.data_path
        yield self.config.frames_path
        yield self.config.minimaps_path
        yield self.config.templates_path
        yield self.config.deleted_frames_path


class ConfigWriter:
    """Writes the default `config.yaml` used by minimap cropping."""

    DEFAULT_CONTENT: str = """# MapSight_AI Configuration for Google Colab
roi:
  - [722, 0]
  - [1800, 0]
  - [1800, 1077]
  - [722, 1077]
output_size: [512, 512]
"""

    def __init__(self, config_path: Path) -> None:
        self.config_path = config_path

    def write_default(self, *, overwrite: bool = True) -> Path:
        if self.config_path.exists() and not overwrite:
            return self.config_path
        self.config_path.write_text(self.DEFAULT_CONTENT, encoding="utf-8")
        return self.config_path


@dataclass
class FrameExtractionRequest:
    """User provided options for extracting frames from a video source."""

    video_source: str
    frames_per_second: float = 0.5
    quality: int = 2
    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d")
    )


class FrameExtractor:
    """Extracts frames from a YouTube URL or local video using ffmpeg."""

    def __init__(self, config: NotebookPathConfig) -> None:
        self.config = config

    def extract(self, request: FrameExtractionRequest) -> Path:
        output_dir = self._prepare_output_dir(request.timestamp)
        command = self._build_command(request, output_dir)
        self._run_command(command)
        self._ensure_frames_created(output_dir)
        return output_dir

    def _prepare_output_dir(self, timestamp: str) -> Path:
        target_dir = self.config.frames_path / timestamp
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir

    def _build_command(
        self, request: FrameExtractionRequest, output_dir: Path
    ) -> List[str]:
        if self._is_youtube_source(request.video_source):
            return self._build_youtube_command(request, output_dir)
        return self._build_local_command(request, output_dir)

    def _build_youtube_command(
        self, request: FrameExtractionRequest, output_dir: Path
    ) -> List[str]:
        destination = str(output_dir / "frame_%05d.jpg")
        exec_command = (
            'ffmpeg -i {{}} -vf "fps={fps}" -q:v {quality} "{destination}"'
        ).format(
            fps=request.frames_per_second,
            quality=request.quality,
            destination=destination,
        )
        return [
            "yt-dlp",
            "--no-warnings",
            "-f",
            "best[ext=mp4]",
            "--exec",
            exec_command,
            request.video_source,
        ]

    def _build_local_command(
        self, request: FrameExtractionRequest, output_dir: Path
    ) -> List[str]:
        destination = str(output_dir / "frame_%05d.jpg")
        return [
            "ffmpeg",
            "-i",
            request.video_source,
            "-vf",
            f"fps={request.frames_per_second}",
            "-q:v",
            str(request.quality),
            destination,
        ]

    def _is_youtube_source(self, video_source: str) -> bool:
        return "youtube.com" in video_source or "youtu.be" in video_source

    def _run_command(self, command: Sequence[str]) -> None:
        result = subprocess.run(
            command,
            cwd=self.config.base_path,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            message = f"Frame extraction failed:\n{result.stderr}"
            raise RuntimeError(message)

    def _ensure_frames_created(self, output_dir: Path) -> None:
        if not any(output_dir.glob("*.jpg")):
            raise RuntimeError("No frames were created during extraction.")


class MinimapCropper:
    """Crop minimap regions from extracted frames via perspective transform."""

    def __init__(self, paths: NotebookPathConfig, config_path: Path) -> None:
        self.paths = paths
        self.config_path = config_path

    def crop(
        self, frames_dir: Path, *, output_dir: Path | None = None
    ) -> Path:
        config = self._load_config()
        transform_matrix, output_size = self._prepare_transform(config)
        frames = self._collect_frames(frames_dir)
        target_dir = self._prepare_output_dir(frames_dir, output_dir)
        self._process_frames(frames, transform_matrix, output_size, target_dir)
        return target_dir

    def _load_config(self) -> dict:
        with self.config_path.open("r", encoding="utf-8") as fp:
            return yaml.safe_load(fp)

    def _prepare_transform(
        self, config: dict
    ) -> tuple[np.ndarray, tuple[int, int]]:
        roi_points = np.array(config["roi"], dtype="float32").reshape(
            (-1, 1, 2)
        )
        hull = cv2.convexHull(roi_points).reshape(-1, 2).astype("float32")
        width, height = config["output_size"]
        destination = np.array(
            [[0, 0], [width, 0], [width, height], [0, height]],
            dtype="float32",
        )
        matrix = cv2.getPerspectiveTransform(hull, destination)
        return matrix, (width, height)

    def _collect_frames(self, frames_dir: Path) -> List[Path]:
        frames = sorted(Path(frames_dir).glob("*.jpg"))
        if not frames:
            raise FileNotFoundError(f"No JPG frames found in {frames_dir}")
        return frames

    def _prepare_output_dir(
        self, frames_dir: Path, output_dir: Path | None
    ) -> Path:
        if output_dir is not None:
            target_dir = output_dir
        else:
            target_dir = self.paths.minimaps_path / Path(frames_dir).name
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir

    def _process_frames(
        self,
        frames: Sequence[Path],
        transform_matrix: np.ndarray,
        output_size: tuple[int, int],
        target_dir: Path,
    ) -> None:
        width, height = output_size
        for frame in tqdm(frames, desc="Cropping minimaps"):
            image = cv2.imread(str(frame))
            if image is None:
                continue
            cropped = cv2.warpPerspective(
                image,
                transform_matrix,
                (width, height),
            )
            cv2.imwrite(str(target_dir / frame.name), cropped)


class DuplicateFrameCleaner:
    """Remove frames similar to a reference image via perceptual hashing."""

    def __init__(self, deleted_frames_root: Path) -> None:
        self.deleted_frames_root = deleted_frames_root

    def clean(
        self,
        reference_path: Path,
        target_dir: Path,
        *,
        threshold: int = 10,
        hash_size: int = 8,
        dry_run: bool = False,
    ) -> int:
        self._validate_paths(reference_path, target_dir)
        reference_hash = self._compute_hash(reference_path, hash_size)
        candidates = self._collect_candidate_files(target_dir)
        duplicates = self._find_duplicates(
            reference_hash, candidates, hash_size, threshold
        )
        if not dry_run:
            self._move_duplicates(duplicates, target_dir)
        return len(duplicates)

    def _validate_paths(self, reference_path: Path, target_dir: Path) -> None:
        if not Path(reference_path).exists():
            raise FileNotFoundError(
                f"Reference image not found: {reference_path}"
            )
        if not Path(target_dir).is_dir():
            raise NotADirectoryError(
                f"Target directory not found: {target_dir}"
            )

    def _compute_hash(self, image_path: Path, hash_size: int) -> int:
        image = cv2.imread(str(image_path))
        if image is None:
            raise ValueError(f"Failed to read reference image: {image_path}")
        return _phash64(image, hash_size)

    def _collect_candidate_files(self, target_dir: Path) -> List[Path]:
        extensions = {".jpg", ".jpeg", ".png"}
        files = [
            path
            for path in Path(target_dir).iterdir()
            if path.suffix.lower() in extensions
        ]
        if not files:
            raise FileNotFoundError(
                f"No candidate images found in {target_dir}"
            )
        return files

    def _find_duplicates(
        self,
        reference_hash: int,
        candidates: Sequence[Path],
        hash_size: int,
        threshold: int,
    ) -> List[Path]:
        duplicates: List[Path] = []
        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(_hash_file_for_pool, (candidate, hash_size))
                for candidate in candidates
            ]
            for future in tqdm(
                as_completed(futures),
                total=len(candidates),
                desc="Computing hashes",
            ):
                candidate, hash_value = future.result()
                if hash_value == -1:
                    continue
                distance = self._hamming_distance(
                    reference_hash,
                    hash_value,
                )
                if distance <= threshold:
                    duplicates.append(candidate)
        return duplicates

    def _move_duplicates(
        self, duplicates: Sequence[Path], original_dir: Path
    ) -> None:
        destination = self.deleted_frames_root / Path(original_dir).name
        destination.mkdir(parents=True, exist_ok=True)
        for candidate in duplicates:
            shutil.move(str(candidate), destination / candidate.name)

    def _hamming_distance(self, first: int, second: int) -> int:
        return (first ^ second).bit_count()


class RoundSegmenter:
    """Split frames into rounds using template matching and aHash metrics."""

    def __init__(self, data_root: Path) -> None:
        self.data_root = data_root

    def segment(
        self,
        frames_dir: Path,
        template_path: Path,
        *,
        segments: int = 5,
        end_threshold: float = 0.5,
        step: int = 5,
        dry_run: bool = True,
    ) -> List[int]:
        frames = self._collect_frames(frames_dir)
        template = self._load_template(template_path)
        ahashes = self._compute_ahashes(frames)
        distances = self._compute_hamming_distances(ahashes)
        hits = self._detect_template_hits(
            frames,
            template,
            end_threshold,
            step,
        )
        boundaries = self._select_boundaries(distances, hits, segments)
        if not dry_run:
            self._write_segments(frames, boundaries, segments, frames_dir)
        return boundaries

    def _collect_frames(self, frames_dir: Path) -> List[Path]:
        frames = sorted(Path(frames_dir).glob("*.jpg"))
        if not frames:
            raise FileNotFoundError(f"No frames found in {frames_dir}")
        return frames

    def _load_template(self, template_path: Path) -> np.ndarray:
        template = cv2.imread(
            str(template_path),
            cv2.IMREAD_GRAYSCALE,
        )
        if template is None:
            raise FileNotFoundError(
                f"Template image not found: {template_path}"
            )
        return template

    def _compute_ahashes(self, frames: Sequence[Path]) -> List[int]:
        hashes: List[int] = []
        for frame in tqdm(frames, desc="Computing aHash"):
            hashes.append(self._ahash(frame))
        return hashes

    def _compute_hamming_distances(self, hashes: Sequence[int]) -> List[int]:
        return [
            self._hamming_distance(hashes[i], hashes[i + 1])
            for i in range(len(hashes) - 1)
        ]

    def _detect_template_hits(
        self,
        frames: Sequence[Path],
        template: np.ndarray,
        end_threshold: float,
        step: int,
    ) -> List[int]:
        hits: List[int] = []
        template_height, template_width = template.shape[:2]
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(
                    self._match_template,
                    index,
                    frames[index],
                    template,
                    end_threshold,
                    template_height,
                    template_width,
                )
                for index in range(0, len(frames), step)
            ]
            for future in tqdm(
                as_completed(futures),
                total=len(futures),
                desc="Template matching",
            ):
                result = future.result()
                if result is not None:
                    hits.append(result)
        return sorted(hits)

    def _select_boundaries(
        self,
        distances: Sequence[int],
        hits: Sequence[int],
        segments: int,
    ) -> List[int]:
        boundaries = list(hits[: max(segments - 1, 0)])
        additional_needed = max(segments - 1 - len(boundaries), 0)
        if additional_needed == 0:
            return boundaries
        candidates = sorted(
            range(len(distances)),
            key=distances.__getitem__,
            reverse=True,
        )
        for index in candidates:
            if self._is_far_from_existing(index, boundaries):
                boundaries.append(index)
                if len(boundaries) == segments - 1:
                    break
        boundaries.sort()
        return boundaries

    def _write_segments(
        self,
        frames: Sequence[Path],
        boundaries: Sequence[int],
        segments: int,
        frames_dir: Path,
    ) -> None:
        output_root = self.data_root / Path(frames_dir).name
        output_root.mkdir(parents=True, exist_ok=True)
        indexes = boundaries + [len(frames)]
        previous = 0
        for round_index, boundary in enumerate(indexes, start=1):
            round_dir = output_root / f"round{round_index}"
            round_dir.mkdir(exist_ok=True)
            self._copy_round_frames(frames[previous:boundary], round_dir)
            previous = boundary

    def _copy_round_frames(
        self, frames: Sequence[Path], destination: Path
    ) -> None:
        for position, frame in enumerate(frames, start=1):
            new_name = destination / f"Frames_{position:05d}.jpg"
            shutil.copy2(frame, new_name)

    def _match_template(
        self,
        index: int,
        frame_path: Path,
        template: np.ndarray,
        threshold: float,
        template_height: int,
        template_width: int,
    ) -> int | None:
        buffer = np.frombuffer(frame_path.read_bytes(), np.uint8)
        image = cv2.imdecode(buffer, cv2.IMREAD_GRAYSCALE)
        if (
            image is None
            or image.shape[0] < template_height
            or image.shape[1] < template_width
        ):
            return None
        correlation = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        if correlation.max() >= threshold:
            return index
        return None

    def _ahash(self, frame_path: Path, size: int = 8) -> int:
        buffer = np.frombuffer(frame_path.read_bytes(), np.uint8)
        image = cv2.imdecode(buffer, cv2.IMREAD_GRAYSCALE)
        if image is None:
            return -1
        resized = cv2.resize(image, (size, size), interpolation=cv2.INTER_AREA)
        average = resized.mean()
        bits = (resized > average).astype(np.uint8).flatten()
        hash_value = 0
        for bit in bits:
            hash_value = (hash_value << 1) | int(bit)
        return hash_value

    def _hamming_distance(self, first: int, second: int) -> int:
        return (first ^ second).bit_count()

    def _is_far_from_existing(
        self, index: int, existing: Sequence[int], minimum_gap: int = 50
    ) -> bool:
        return all(abs(index - value) > minimum_gap for value in existing)


class ColabStatusReporter:
    """Summarise the processing status of the Colab workspace."""

    def __init__(self, config: NotebookPathConfig) -> None:
        self.config = config

    def report(self) -> str:
        parts = [
            "=== MapSight_AI Colab Status ===",
            f"Base path: {self.config.base_path}",
            self._summarise_directory("frames", self.config.frames_path),
            self._summarise_directory("minimaps", self.config.minimaps_path),
            self._summarise_directory("templates", self.config.templates_path),
            self._summarise_directory(
                "deleted_frames", self.config.deleted_frames_path
            ),
        ]
        return "\n".join(parts)

    def _summarise_directory(self, name: str, directory: Path) -> str:
        if not directory.exists():
            return f"- {name}: (missing)"
        files = list(directory.rglob("*.jpg"))
        files.extend(directory.rglob("*.png"))
        return f"- {name}: {len(files)} image files"


def _build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run MapSight_AI utilities on Colab"
    )
    parser.add_argument(
        "--base-path",
        default="/content/drive/MyDrive/MapSight_AI",
        help="Base path inside Google Drive",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    setup_parser = subparsers.add_parser(
        "setup",
        help="Initialise directories and config file",
    )
    setup_parser.add_argument(
        "--no-overwrite",
        action="store_true",
        help="Do not overwrite config.yaml",
    )

    extract_parser = subparsers.add_parser(
        "extract",
        help="Extract frames from a video source",
    )
    extract_parser.add_argument(
        "video_source",
        help="YouTube URL or local video path",
    )
    extract_parser.add_argument(
        "--fps",
        type=float,
        default=0.5,
        help="Frames per second",
    )
    extract_parser.add_argument(
        "--quality",
        type=int,
        default=2,
        help="JPEG quality (2-31)",
    )
    extract_parser.add_argument(
        "--timestamp",
        help="Custom output timestamp directory name",
    )

    crop_parser = subparsers.add_parser(
        "crop",
        help="Crop minimaps from a directory of frames",
    )
    crop_parser.add_argument(
        "frames_dir",
        help="Directory containing frame JPG files",
    )
    crop_parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to config.yaml",
    )
    crop_parser.add_argument(
        "--output",
        help="Optional output directory for cropped images",
    )

    clean_parser = subparsers.add_parser(
        "clean",
        help="Remove frames similar to a reference image",
    )
    clean_parser.add_argument(
        "reference",
        help="Reference image path",
    )
    clean_parser.add_argument(
        "target",
        help="Directory to scan for duplicates",
    )
    clean_parser.add_argument(
        "--threshold",
        type=int,
        default=10,
        help="Hamming distance threshold",
    )
    clean_parser.add_argument(
        "--hash-size",
        type=int,
        default=8,
        help="Hash size for pHash",
    )
    clean_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only list duplicates",
    )

    segment_parser = subparsers.add_parser(
        "segment",
        help="Segment frames into rounds",
    )
    segment_parser.add_argument(
        "frames_dir",
        help="Directory with frame JPG files",
    )
    segment_parser.add_argument("template", help="Template image path")
    segment_parser.add_argument(
        "--segments",
        type=int,
        default=5,
        help="Number of segments to create",
    )
    segment_parser.add_argument(
        "--end-threshold",
        type=float,
        default=0.5,
        help="Template matching threshold",
    )
    segment_parser.add_argument(
        "--step",
        type=int,
        default=5,
        help="Sampling step for template matching",
    )
    segment_parser.add_argument(
        "--no-dry-run",
        action="store_true",
        help="Write segmented frames to disk",
    )

    subparsers.add_parser("status", help="Show workspace summary")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_argument_parser()
    args = parser.parse_args(argv)

    config = NotebookPathConfig.from_base_path(Path(args.base_path))
    directory_manager = DirectoryManager(config)

    if args.command == "setup":
        directory_manager.ensure_directories()
        writer = ConfigWriter(config.base_path / "config.yaml")
        writer.write_default(overwrite=not args.no_overwrite)
        print("Setup complete.")
        return 0

    if args.command == "extract":
        directory_manager.ensure_directories()
        request = FrameExtractionRequest(
            video_source=args.video_source,
            frames_per_second=args.fps,
            quality=args.quality,
            timestamp=args.timestamp or datetime.now().strftime("%Y-%m-%d"),
        )
        extractor = FrameExtractor(config)
        output_dir = extractor.extract(request)
        print(f"Frames extracted to: {output_dir}")
        return 0

    if args.command == "crop":
        directory_manager.ensure_directories()
        frames_dir = config.resolve(args.frames_dir)
        config_path = config.resolve(
            args.config, default_dir=config.base_path / "config.yaml"
        )
        output_dir = config.resolve(args.output) if args.output else None
        cropper = MinimapCropper(config, config_path)
        result = cropper.crop(frames_dir, output_dir=output_dir)
        print(f"Cropped minimaps stored in: {result}")
        return 0

    if args.command == "clean":
        directory_manager.ensure_directories()
        cleaner = DuplicateFrameCleaner(config.deleted_frames_path)
        duplicates = cleaner.clean(
            config.resolve(args.reference),
            config.resolve(args.target),
            threshold=args.threshold,
            hash_size=args.hash_size,
            dry_run=args.dry_run,
        )
        if args.dry_run:
            print(f"[DRY-RUN] {duplicates} duplicates detected.")
        else:
            print(f"Removed {duplicates} duplicate frames.")
        return 0

    if args.command == "segment":
        directory_manager.ensure_directories()
        segmenter = RoundSegmenter(config.data_path)
        boundaries = segmenter.segment(
            config.resolve(args.frames_dir),
            config.resolve(args.template),
            segments=args.segments,
            end_threshold=args.end_threshold,
            step=args.step,
            dry_run=not args.no_dry_run,
        )
        print(f"Detected boundaries: {boundaries}")
        if args.no_dry_run:
            print("Segmented frames written to disk.")
        return 0

    if args.command == "status":
        reporter = ColabStatusReporter(config)
        print(reporter.report())
        return 0

    parser.error("Unknown command")
    return 1


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
