import sys
from pathlib import Path
import subprocess

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from video_pipeline import extract_frames, crop_minimap_dir


def create_sample_video(path: Path) -> None:
    cmd = [
        'ffmpeg',
        '-f', 'lavfi',
        '-i', 'color=c=black:s=32x32:d=1',
        '-vf', 'format=yuv420p',
        '-y', str(path),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def test_extract_frames(tmp_path: Path) -> None:
    video = tmp_path / 'sample.mp4'
    create_sample_video(video)
    out_dir = tmp_path / 'frames'
    count = extract_frames(video, out_dir, fps=1, width=32)
    assert count > 0
    assert any(out_dir.glob('*.jpg'))


def test_crop_minimap(tmp_path: Path) -> None:
    frame_dir = tmp_path / 'frames'
    frame_dir.mkdir()
    img_path = frame_dir / 'f.jpg'
    import numpy as np
    import cv2
    img = np.zeros((32, 32, 3), dtype=np.uint8)
    cv2.imwrite(str(img_path), img)

    cfg = {'roi': [[0,0],[31,0],[31,31],[0,31]], 'output_size': [16,16]}
    cfg_path = tmp_path / 'cfg.yaml'
    import yaml
    cfg_path.write_text(yaml.safe_dump(cfg))

    out_dir = tmp_path / 'mini'
    count = crop_minimap_dir(frame_dir, out_dir, cfg_path)
    assert count == 1
    assert (out_dir / 'f.jpg').is_file()
