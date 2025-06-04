import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import cv2
import numpy as np
from clean_same_frames import phash64, hamming_distance, compute_hash


def create_image(square: bool = False) -> np.ndarray:
    img = np.zeros((32, 32, 3), dtype=np.uint8)
    if square:
        cv2.rectangle(img, (8, 8), (24, 24), (255, 255, 255), -1)
    return img


def test_phash64_and_hamming(tmp_path: Path) -> None:
    img1 = create_image(False)
    img2 = create_image(False)
    img3 = create_image(True)
    h1 = phash64(img1)
    h2 = phash64(img2)
    h3 = phash64(img3)
    assert hamming_distance(h1, h2) == 0
    assert hamming_distance(h1, h3) > 0


def test_duplicate_detection(tmp_path: Path) -> None:
    img1 = create_image(False)
    img2 = create_image(False)
    img3 = create_image(True)
    p1 = tmp_path / 'a.jpg'
    p2 = tmp_path / 'b.jpg'
    p3 = tmp_path / 'c.jpg'
    cv2.imwrite(str(p1), img1)
    cv2.imwrite(str(p2), img2)
    cv2.imwrite(str(p3), img3)
    h1 = compute_hash(p1, 8)[1]
    h2 = compute_hash(p2, 8)[1]
    h3 = compute_hash(p3, 8)[1]
    thr = 5
    dup_paths = [p for p, h in [(p1, h1), (p2, h2), (p3, h3)] if h != -1 and hamming_distance(h1, h) <= thr and p != p1]
    assert dup_paths == [p2]
