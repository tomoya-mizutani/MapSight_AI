import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import cv2
import numpy as np
from segment_rounds import detect_template_frames


def test_detect_template_frames(tmp_path: Path) -> None:
    np.random.seed(0)
    tmpl = np.zeros((4, 4), dtype=np.uint8)
    tmpl[1:3, 1:3] = 255
    tmpl_path = tmp_path / 'template.png'
    cv2.imwrite(str(tmpl_path), tmpl)

    frames = []
    for i in range(5):
        img = np.random.randint(0, 256, (20, 20), dtype=np.uint8)
        if i in {1, 3}:
            img[8:12, 8:12] = tmpl
        path = tmp_path / f'frame_{i}.png'
        cv2.imwrite(str(path), img)
        frames.append(path)

    tmpl_gray = cv2.imread(str(tmpl_path), cv2.IMREAD_GRAYSCALE)
    hits = detect_template_frames(frames, tmpl_gray, thr=0.9, step=1, cluster_gap=0, max_workers=1)
    assert sorted(hits) == [1, 3]
