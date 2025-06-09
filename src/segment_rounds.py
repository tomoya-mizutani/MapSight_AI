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
python segment_rounds.py data/frames/<upload-date> \
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
import argparse
import cv2
import os
import shutil
import time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from threading import Lock, Thread
from functools import partial

# グローバル変数（進捗管理用）
processed = 0
last_print = 0
total_frames = 1
lock = Lock()

def ahash(path: Path, size: int = 8) -> int:
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
        return -1

def ahash_progress_global(path):
    global processed, last_print, total_frames
    res = ahash(path)
    with lock:
        processed += 1
        now = time.time()
        if now - last_print > 1:
            print(f"\raHash progress: {processed}/{total_frames} ({processed/total_frames*100:.1f}%)", end="", flush=True)
            last_print = now
    return res

def process_frame_cpu(idx, frame_path, tmpl_gray, thr, th, tw):
    buf = np.frombuffer(frame_path.read_bytes(), np.uint8)
    img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
    if img is None or img.shape[0] < th or img.shape[1] < tw:
        return None
    corr = cv2.matchTemplate(img, tmpl_gray, cv2.TM_CCOEFF_NORMED)
    if corr.max() >= thr:
        return idx
    return None

def detect_template_frames(
    frames: list[Path],
    tmpl_gray: np.ndarray,
    thr: float = 0.75,
    step: int = 1,
    cluster_gap: int = 5,
    max_workers: int = 8
) -> list[int]:
    hits = []
    th, tw = tmpl_gray.shape[:2]

    total = len(frames) // step + (1 if len(frames) % step else 0)
    processed_local = 0
    last_update_time = time.time()
    lock_local = Lock()
    stop_flag = False

    def progress_report():
        spinner = ['-', '\\', '|', '/']
        spin_idx = 0
        while not stop_flag:
            with lock_local:
                now = time.time()
                if now - last_update_time > 5:
                    msg = "\r⚠ 処理が5秒以上止まっている可能性があります...          "
                else:
                    pct = (processed_local / total) * 100 if total > 0 else 100
                    msg = f"\r処理中... {processed_local}/{total} ({pct:.1f}%) {spinner[spin_idx]}"
                    spin_idx = (spin_idx + 1) % len(spinner)
            print(msg, end="", flush=True)
            time.sleep(0.5)
        print("\r処理完了。                                           ")

    t = Thread(target=progress_report, daemon=True)
    t.start()

    def process_frame_wrapper(idx):
        nonlocal processed_local, last_update_time
        result = process_frame_cpu(idx, frames[idx], tmpl_gray, thr, th, tw)
        with lock_local:
            processed_local += 1
            last_update_time = time.time()
        return result

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_frame_wrapper, idx) for idx in range(0, len(frames), step)]
        for future in as_completed(futures):
            res = future.result()
            if res is not None:
                hits.append(res)

    stop_flag = True
    t.join()

    if not hits:
        return []

    clusters = [[hits[0]]]
    for i in sorted(hits)[1:]:
        if i - clusters[-1][-1] <= cluster_gap:
            clusters[-1].append(i)
        else:
            clusters.append([i])

    reps = [c[len(c) // 2] for c in clusters]
    return reps

def hdist(a: int, b: int) -> int:
    return (a ^ b).bit_count()

def main():
    global processed, last_print, total_frames
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
    ap.add_argument('--step', type=int, default=1, help='sample interval for template matching')
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

    processed = 0
    last_print = time.time()
    total_frames = len(frames)

    with ProcessPoolExecutor() as ex:
        hashes = list(ex.map(ahash_progress_global, frames))
    print(f"\naHash done in {time.time()-start:.2f}s")

    hd = partial(hdist)
    dists = [hd(hashes[i], hashes[i+1]) for i in range(len(hashes) - 1)]

    print('Detecting template frames…')
    start_detect = time.time()

    t_idx = detect_template_frames(
        frames, tmpl_gray, args.end_th,
        step=args.step,
        cluster_gap=args.cluster_gap,
        max_workers=os.cpu_count() or 8
    )
    print(f"Template detection done in {time.time() - start_detect:.2f}s")
    t_idx.sort()

    clusters = []
    for idx in t_idx:
        if not clusters or idx - clusters[-1][-1] > args.cluster_gap:
            clusters.append([idx])
        else:
            clusters[-1].append(idx)
    boundaries = [c[0] for c in clusters]

    need = args.segments - 1 - len(boundaries)
    if need > 0:
        cand = sorted(range(len(dists)), key=lambda i: dists[i], reverse=True)
        for i in cand:
            if all(abs(i - b) > 150 for b in boundaries):
                boundaries.append(i)
                if len(boundaries) == args.segments - 1:
                    break
    boundaries = sorted(boundaries)

    if args.peek or args.dry_run:
        print('Boundaries:', boundaries)
        print('Frames per segment:', [b - a for a, b in zip([0]+boundaries, boundaries+[len(frames)])])
        if args.peek:
            return

    # ここから保存先ディレクトリ構成の変更
    upload_date = frames_dir.name
    if upload_date == 'frames':
        raise SystemExit('frames_dir must be data/frames/<upload-date>')
    out_root = Path(args.out_root) / upload_date
    out_root.mkdir(parents=True, exist_ok=True)
    rounds = []
    prev = 0
    for i, b in enumerate(boundaries + [len(frames)]):
        rdir = out_root / f'round{i+1}'
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
        print(f'{rdir.name}: {end_i - start_i} frames')

    if args.log_file:
        with open(args.log_file, 'w') as fp:
            fp.write('src,dst\n')
            for s, d in moves:
                fp.write(f'{s},{d}\n')

default_main = main

if __name__ == '__main__':
    main()
