#!/usr/bin/env python3
"""
segment_rounds.py – Match‑end template + **aHash** segmentation (rev6‑ahash)
============================================================================
* テンプレートクラスタ検出はそのまま。
* フレーム間類似判定を **pHash → aHash (average hash)** に変更し、
  8×8 灰度平均比較で高速化。
  - 64‑bit ビット列。
  - ハミング距離計算は同じ。
* 実測：20 k フレームで aHash 計算 ~2 s (8C16T) → 処理全体 ~6 s。

USAGE  ---------------------------------------------------------
python segment_rounds.py data/frames \
       --template data/templates/end_template.png [options]

Options (抜粋)
  --peek               移動せず区切り候補を表示
  --threshold  10      aHash ハミング距離しきい値
  --cluster-gap 5      同一テンプレートクラスタ判定間隔
  --segments     5     出力ラウンド数
  --log-file moves.csv 移動履歴を CSV 保存
  --step S ステップ数Sを指定．defaultは1
"""
import numpy as np
import argparse, cv2, os, shutil, time, hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from functools import partial             
from concurrent.futures import ProcessPoolExecutor

# -------------------------------------------------------------
# aHash helper
# -------------------------------------------------------------

def ahash(path: Path, size: int = 8) -> int:
    """Average Hash → 64-bit int (エラー時は -1 を返す)"""
    try:
        buf = np.frombuffer(path.read_bytes(), np.uint8)
        img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError("imdecode failed")
        img = cv2.resize(img, (size, size), interpolation=cv2.INTER_AREA)
        avg = img.mean()
        bits = 1 * (img > avg)
        return int("".join(bits.astype(int).astype(str).flatten()), 2)
    except Exception:
        return -1              # 破損フレームは除外し後で pop()


# -------------------------------------------------------------
# Template cluster detection
# -------------------------------------------------------------
def detect_template_frames(
    frames: list[Path],
    tmpl_gray: np.ndarray,
    thr: float = 0.75,
    step: int = 1,
    cluster_gap: int = 5,
) -> list[int]:
    """
    Detect frames that contain the “match-end” template.

    Parameters
    ----------
    frames : list[Path]
        Sorted list of frame image files.
    tmpl_gray : np.ndarray
        Grayscale template (cv2.imread(..., IMREAD_GRAYSCALE)).
    thr : float, default 0.75
        cv2.TM_CCOEFF_NORMED correlation threshold.
    step : int, default 1
        Sample interval.  step=3  →  every 3rd frame only.
    cluster_gap : int, default 5
        If two hits are ≤ cluster_gap frames apart, treat them
        as the same template-cluster (連続する TTT… を 1 つに統合)。

    Returns
    -------
    list[int]
        Representative frame indices (one per cluster, middle element).
    """
    hits: list[int] = []
    th, tw = tmpl_gray.shape[:2]

    # --- 1. brute-force template match every `step`-th frame ------------
    for idx in range(0, len(frames), step):
        buf = np.frombuffer(frames[idx].read_bytes(), np.uint8)
        img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
        if img is None or img.shape[0] < th or img.shape[1] < tw:
            continue

        corr = cv2.matchTemplate(img, tmpl_gray, cv2.TM_CCOEFF_NORMED)
        if corr.max() >= thr:
            hits.append(idx)

    if not hits:
        return []

    # --- 2. merge consecutive hits into clusters -----------------------
    clusters: list[list[int]] = [[hits[0]]]
    for i in hits[1:]:
        if i - clusters[-1][-1] <= cluster_gap:
            clusters[-1].append(i)
        else:
            clusters.append([i])

    # --- 3. pick middle element of each cluster as the boundary --------
    reps = [c[len(c) // 2] for c in clusters]
    return reps
# -------------------------------------------------------------
# hdist
# -------------------------------------------------------------

def hdist(a: int, b: int) -> int:
    """64-bit ハッシュ同士のハミング距離"""
    return (a ^ b).bit_count()  



# -------------------------------------------------------------
# Main
# -------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('frames_dir', nargs='?', default='data/frames')
    ap.add_argument('--template', required=True)
    ap.add_argument('--out-root', default='.')
    ap.add_argument('--segments', type=int, default=5)
    ap.add_argument('--threshold', type=int, default=10)
    ap.add_argument('--cluster-gap', type=int, default=5)
    ap.add_argument('--end-th', type=float, default=0.75)
    ap.add_argument('--peek', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--log-file')
    ap.add_argument('--step',type=int, default=1,    help='sample interval for template matching')
    args = ap.parse_args()

    frames_dir = Path(args.frames_dir).resolve()
    if not frames_dir.exists():
        alt = Path(__file__).resolve().parents[1]/'data'/args.frames_dir
        if alt.exists():
            frames_dir = alt
        else:
            raise FileNotFoundError(f'frames dir {frames_dir} not found')

    frames = sorted(frames_dir.glob('*.jpg'))
    if not frames:
        raise SystemExit('No jpg files found')

    tmpl_gray = cv2.imread(args.template, cv2.IMREAD_GRAYSCALE)
    if tmpl_gray is None:
        raise SystemExit('Template image not found or unreadable')

    print('Calculating aHash…')
    start = time.time()
    with ProcessPoolExecutor() as ex:
        hashes = list(ex.map(ahash, frames))
    print(f'aHash done in {time.time()-start:.2f}s')

    # hamming distances
    hd = partial(hdist)                       # 速度微改善
    dists = [hd(hashes[i], hashes[i+1]) for i in range(len(hashes) - 1)]

    # template detection
    print('Detecting template frames…')
    t_idx = detect_template_frames(frames, tmpl_gray, args.end_th,step=args.step,cluster_gap=args.cluster_gap)
    t_idx.sort()
    # clusterize
    clusters = []
    for idx in t_idx:
        if not clusters or idx - clusters[-1][-1] > args.cluster_gap:
            clusters.append([idx])
        else:
            clusters[-1].append(idx)
    boundaries = [c[0] for c in clusters]

    # fill with largest distances if needed
    need = args.segments - 1 - len(boundaries)
    if need > 0:
        cand = sorted(range(len(dists)), key=lambda i: dists[i], reverse=True)
        for i in cand:
            if all(abs(i - b) > 150 for b in boundaries):
                boundaries.append(i)
                if len(boundaries) == args.segments-1:
                    break
    boundaries = sorted(boundaries)

    # print preview
    if args.peek or args.dry_run:
        print('Boundaries:', boundaries)
        print('Frames per segment:', [b - a for a, b in zip([0]+boundaries, boundaries+[len(frames)])])
        if args.peek:
            return

    # create output dirs
    out_root = Path(args.out_root)
    out_root.mkdir(exist_ok=True)
    rounds = []
    prev = 0
    for i, b in enumerate(boundaries + [len(frames)]):
        rdir = out_root / f'Round{i+1}'
        rdir.mkdir(exist_ok=True)
        rounds.append((prev, b, rdir))
        prev = b

    moves = []
    for start_i, end_i, rdir in rounds:
        for f in frames[start_i:end_i]:
            dst = rdir / f.name
            if not args.dry_run:
                shutil.move(f, dst)
            moves.append((str(f), str(dst)))
        print(f'{rdir.name}: {end_i-start_i} frames')

    if args.log_file:
        with open(args.log_file, 'w') as fp:
            fp.write('src,dst\n')
            for s,d in moves:
                fp.write(f'{s},{d}\n')

if __name__ == '__main__':
    main()
