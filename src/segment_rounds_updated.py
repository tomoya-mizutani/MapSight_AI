#!/usr/bin/env python3
"""
segment_rounds.py – PUBGラウンド境界検出スクリプト (rev6-ahash)
================================================================
PUBGの試合動画から抽出されたフレーム画像を自動的にラウンド単位でセグメント化する
Pythonスクリプトです。テンプレートマッチングとaHash（Average Hash）アルゴリズムを
組み合わせて、高速で正確なラウンド境界検出を実現します。

アルゴリズム:
* テンプレートマッチング: ラウンド終了画面のテンプレート画像との類似度計算
* aHash (Average Hash): 8×8グレースケール画像から64ビットハッシュを生成
* ハイブリッド検出: テンプレート検出で確実な境界を特定、不足分をaHashで補完

性能:
* 実測：20,000フレームで処理全体 ~6秒（8C16T環境）
* aHash計算: ~2秒、テンプレート検出: ~3秒
* グレースケール処理により1/3のメモリ効率化

USAGE ---------------------------------------------------------
python segment_rounds.py data/frames/<upload-date> \
       --template data/templates/Match_End_template.jpg [options]

出力先: data/<upload-date>/round1/, round2/, ...
ファイル操作: 元ファイルを保持してコピー（shutil.copy2使用）

引数:
  frames_dir           フレーム画像が格納されたディレクトリ
                      例: data/frames/2025-05-02

オプション:
  --template FILE      テンプレート画像ファイルパス（必須）
  --segments N         出力ラウンド数（デフォルト: 5）
  --threshold N        aHash ハミング距離しきい値（デフォルト: 10、現在未使用）
  --cluster-gap N      同一テンプレートクラスタ判定間隔（デフォルト: 5）
  --end-th FLOAT       テンプレートマッチング類似度しきい値（デフォルト: 0.5）
  --step N             テンプレートマッチングのステップ数（デフォルト: 1）
  --peek               移動せず区切り候補を表示のみ
  --dry-run            実際のファイル操作を行わず処理内容を表示
  --log-file FILE      移動履歴を CSV ファイルに保存
  --out-root DIR       出力ルートディレクトリ（後方互換性のため残存、現在未使用）
"""

import numpy as np
import argparse
import cv2
import os
import shutil
import time
import json
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from threading import Lock, Thread
import re
try:
    import easyocr
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    print("注意: EasyOCRライブラリが見つかりません。OCR機能は無効化されます。")
from functools import partial

# グローバル変数（進捗管理用）
processed = 0
last_print = 0
total_frames = 1
start_ahash = 0
lock = Lock()
ocr_reader = None  # EasyOCRリーダーのグローバルインスタンス

def init_ocr_reader():
    """EasyOCRリーダーを初期化
    
    Returns:
        easyocr.Reader: 初期化されたOCRリーダー、エラー時はNone
    """
    global ocr_reader
    if not OCR_AVAILABLE:
        return None
    
    if ocr_reader is None:
        try:
            print("OCRリーダーを初期化中...")
            # 日本語と英語をサポート
            ocr_reader = easyocr.Reader(['ja', 'en'], gpu=True)
            print("OCRリーダー初期化完了")
        except Exception as e:
            print(f"OCRリーダー初期化エラー: {e}")
            print("GPU使用を無効化して再試行...")
            try:
                ocr_reader = easyocr.Reader(['ja', 'en'], gpu=False)
                print("OCRリーダー初期化完了（CPU使用）")
            except Exception as e2:
                print(f"OCRリーダー初期化失敗: {e2}")
                return None
    return ocr_reader

def extract_text_from_image(image_path, confidence_threshold=0.5):
    """画像からテキストを抽出
    
    Args:
        image_path (str): 画像ファイルのパス
        confidence_threshold (float): 信頼度しきい値（0.0-1.0）
    
    Returns:
        list: 抽出されたテキストのリスト（信頼度付き）
    """
    reader = init_ocr_reader()
    if reader is None:
        return []
    
    try:
        # OCR実行
        results = reader.readtext(str(image_path))
        
        # 信頼度でフィルタリング
        filtered_results = []
        for result in results:
            try:
                # EasyOCRの結果構造: (bbox, text, confidence)
                if isinstance(result, (list, tuple)) and len(result) >= 3:
                    bbox = result[0]
                    text = result[1]
                    confidence = result[2]
                    
                    # 信頼度が数値であることを確認
                    if isinstance(confidence, (int, float)) and confidence >= confidence_threshold:
                        filtered_results.append({
                            'text': str(text).strip(),
                            'confidence': float(confidence),
                            'bbox': bbox
                        })
            except (IndexError, TypeError, ValueError) as e:
                # 結果の構造が予期しない場合はスキップ
                print(f"OCR結果解析エラー: {e}")
                continue
        
        return filtered_results
    except Exception as e:
        print(f"OCR処理エラー {image_path}: {e}")
        return []

def detect_round_text_patterns(text_results):
    """ラウンド関連のテキストパターンを検出
    
    Args:
        text_results (list): extract_text_from_imageの結果
    
    Returns:
        dict: 検出されたパターンの情報
    """
    patterns = {
        'round_number': [],      # ラウンド番号
        'game_over': [],         # ゲーム終了関連
        'winner': [],            # 勝者関連
        'kill_count': [],        # キル数
        'placement': []          # 順位
    }
    
    for result in text_results:
        text = result['text'].lower()
        confidence = result['confidence']
        
        # ラウンド番号の検出
        round_match = re.search(r'round\s*(\d+)|ラウンド\s*(\d+)|第\s*(\d+)\s*戦', text)
        if round_match:
            round_num = round_match.group(1) or round_match.group(2) or round_match.group(3)
            patterns['round_number'].append({
                'round': int(round_num),
                'confidence': confidence,
                'text': result['text']
            })
        
        # ゲーム終了の検出
        if any(keyword in text for keyword in ['game over', 'match over', 'ゲーム終了', '試合終了', 'winner', '勝者']):
            patterns['game_over'].append({
                'text': result['text'],
                'confidence': confidence
            })
        
        # 勝者の検出
        if any(keyword in text for keyword in ['winner', 'chicken dinner', '勝者', 'victory', '勝利']):
            patterns['winner'].append({
                'text': result['text'],
                'confidence': confidence
            })
        
        # キル数の検出
        kill_match = re.search(r'(\d+)\s*kills?|キル\s*(\d+)|倒した\s*(\d+)', text)
        if kill_match:
            kill_count = kill_match.group(1) or kill_match.group(2) or kill_match.group(3)
            patterns['kill_count'].append({
                'kills': int(kill_count),
                'confidence': confidence,
                'text': result['text']
            })
        
        # 順位の検出
        place_match = re.search(r'#(\d+)|(\d+)位|(\d+)th|(\d+)nd|(\d+)rd|(\d+)st', text)
        if place_match:
            place = (place_match.group(1) or place_match.group(2) or 
                    place_match.group(3) or place_match.group(4) or 
                    place_match.group(5) or place_match.group(6))
            patterns['placement'].append({
                'place': int(place),
                'confidence': confidence,
                'text': result['text']
            })
    
    return patterns

def analyze_frame_with_ocr(frame_path, confidence_threshold=0.6):
    """フレームをOCRで分析してゲーム状態を判定
    
    Args:
        frame_path (str): フレーム画像のパス
        confidence_threshold (float): OCR信頼度しきい値
    
    Returns:
        dict: 分析結果の辞書
    """
    if not OCR_AVAILABLE:
        return {'status': 'ocr_unavailable'}
    
    text_results = extract_text_from_image(frame_path, confidence_threshold)
    if not text_results:
        return {'status': 'no_text_detected'}
    
    patterns = detect_round_text_patterns(text_results)
    
    # 分析結果をまとめる
    analysis = {
        'status': 'text_detected',
        'text_count': len(text_results),
        'patterns': patterns,
        'all_text': [r['text'] for r in text_results],
        'high_confidence_text': [r['text'] for r in text_results if r['confidence'] > 0.8]
    }
    
    # ゲーム状態の判定
    if patterns['game_over'] or patterns['winner']:
        analysis['game_state'] = 'round_end'
    elif patterns['round_number']:
        analysis['game_state'] = 'round_start'
    elif patterns['kill_count'] or patterns['placement']:
        analysis['game_state'] = 'in_game'
    else:
        analysis['game_state'] = 'unknown'
    
    return analysis

def ahash(path: Path, size: int = 8) -> int:
    """
    aHash (Average Hash) アルゴリズムによる画像ハッシュ計算
    
    アルゴリズム:
    1. 画像を8×8グレースケールにリサイズ
    2. 平均輝度を計算
    3. 各ピクセルが平均以上かどうかで64ビットハッシュ生成
    
    Args:
        path: 画像ファイルのパス
        size: ハッシュサイズ（デフォルト: 8x8=64bit）
    
    Returns:
        64ビット整数ハッシュ値、エラー時は-1
    """
    try:
        buf = np.frombuffer(path.read_bytes(), np.uint8)
        img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError("imdecode failed")
        
        # 8x8にリサイズしてグレースケール化（メモリ効率化）
        img = cv2.resize(img, (size, size), interpolation=cv2.INTER_AREA)
        avg = img.mean()
        
        # 平均値以上のピクセルを1、未満を0とする二値化
        bits = 1 * (img > avg)
        return int("".join(bits.astype(int).astype(str).flatten()), 2)
    except Exception:
        return -1

def ahash_progress_global(path):
    """進捗表示付きaHash計算（並列処理用ラッパー）"""
    global processed, last_print, total_frames, start_ahash
    res = ahash(path)
    with lock:
        processed += 1
        now = time.time()
        if now - last_print > 0.5:  # 更新頻度を上げる
            pct = (processed / total_frames) * 100
            elapsed = now - start_ahash
            rate = processed / elapsed if elapsed > 0 else 0
            eta = (total_frames - processed) / rate if rate > 0 else 0
            eta_str = f"残り{eta:.0f}秒" if eta > 1 else "完了間近"
            print(f"\raHash計算: {processed}/{total_frames} ({pct:.1f}%) | {rate:.1f} fps | {eta_str}", end="", flush=True)
            last_print = now
    return res

def process_frame_cpu(idx, frame_path, tmpl_gray, thr, th, tw):
    """
    テンプレートマッチング処理（単一フレーム）
    
    Args:
        idx: フレームインデックス
        frame_path: フレーム画像のパス
        tmpl_gray: グレースケールテンプレート画像
        thr: 類似度しきい値
        th, tw: テンプレート画像の高さ、幅
    
    Returns:
        しきい値以上の場合はフレームインデックス、未満はNone
    """
    buf = np.frombuffer(frame_path.read_bytes(), np.uint8)
    img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
    if img is None or img.shape[0] < th or img.shape[1] < tw:
        return None
    
    # OpenCVのテンプレートマッチング（正規化相関係数法）
    corr = cv2.matchTemplate(img, tmpl_gray, cv2.TM_CCOEFF_NORMED)

    if corr.max() >= thr:
        return idx
    return None

def detect_template_frames(
    frames: list[Path],
    tmpl_gray: np.ndarray,
    thr: float = 0.5,
    step: int = 1,
    cluster_gap: int = 3,
    max_workers: int = 8
) -> list[int]:
    """
    テンプレートマッチングによる境界フレーム検出
    
    Args:
        frames: フレーム画像パスのリスト
        tmpl_gray: グレースケールテンプレート画像
        thr: 類似度しきい値（デフォルト: 0.5）
        step: 検査間隔（デフォルト: 1、全フレーム）
        cluster_gap: クラスタリング間隔
        max_workers: 並列処理数
    
    Returns:
        検出されたフレームインデックスのリスト
    """
    hits = []
    th, tw = tmpl_gray.shape[:2]

    total = len(frames) // step + (1 if len(frames) % step else 0)
    processed_local = 0
    detections_count = 0
    last_update_time = time.time()
    start_time = time.time()
    lock_local = Lock()
    stop_flag = False

    def progress_report():
        """テンプレートマッチング進捗表示スレッド"""
        spinner = ['-', '\\', '|', '/']
        spin_idx = 0
        while not stop_flag:
            with lock_local:
                now = time.time()
                elapsed = now - start_time
                if now - last_update_time > 10:
                    msg = "\r⚠ 処理が10秒以上止まっています... 処理を確認中          "
                else:
                    pct = (processed_local / total) * 100 if total > 0 else 100
                    if processed_local > 0:
                        avg_time = elapsed / processed_local
                        eta = avg_time * (total - processed_local)
                        eta_str = f"残り約{eta:.0f}秒" if eta > 0 else "完了間近"
                    else:
                        eta_str = "計算中..."
                    
                    msg = (f"\rテンプレートマッチング: {processed_local}/{total} "
                          f"({pct:.1f}%) | 検出数: {detections_count} | "
                          f"{eta_str} {spinner[spin_idx]}")
                    spin_idx = (spin_idx + 1) % len(spinner)
            print(msg, end="", flush=True)
            time.sleep(0.3)
        
        # 最終結果表示
        with lock_local:
            elapsed = time.time() - start_time
            rate = processed_local / elapsed if elapsed > 0 else 0
            print(f"\rテンプレートマッチング完了: {processed_local}/{total} フレーム処理, "
                  f"{detections_count}個検出, {elapsed:.1f}秒 ({rate:.1f} fps)        ")

    t = Thread(target=progress_report, daemon=True)
    t.start()

    def process_frame_wrapper(idx):
        nonlocal processed_local, last_update_time, detections_count
        result = process_frame_cpu(idx, frames[idx], tmpl_gray, thr, th, tw)
        with lock_local:
            processed_local += 1
            last_update_time = time.time()
            if result is not None:
                detections_count += 1
        return result

    # 並列テンプレートマッチング実行
    print(f"テンプレートマッチング開始: {total}フレームを{max_workers}並列で処理...")
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

    # クラスタリング処理：近接する検出フレームをグループ化
    clusters = [[hits[0]]]
    for i in sorted(hits)[1:]:
        if i - clusters[-1][-1] <= cluster_gap:
            clusters[-1].append(i)  # 既存クラスタに追加
        else:
            clusters.append([i])    # 新しいクラスタ作成

    # 各クラスタの代表値（中央値）を取得
    reps = [c[len(c) // 2] for c in clusters]
    return reps

def hdist(a: int, b: int) -> int:
    """ハミング距離計算：2つのハッシュ値間の異なるビット数"""
    return (a ^ b).bit_count()

def verify_boundary_frames(frames, boundaries, tmpl_gray, args):
    """境界フレームとテンプレート画像のマッチング結果を検証
    
    Args:
        frames: フレーム画像パスのリスト
        boundaries: 検出された境界フレームのインデックスリスト
        tmpl_gray: グレースケールテンプレート画像
        args: コマンドライン引数
    """
    print(f"\n=== 境界フレーム検証 ===")
    print(f"検出された境界フレーム: {boundaries}")
    print(f"テンプレートマッチングしきい値: {args.end_th}")
    
    verification_results = []
    
    for i, boundary_idx in enumerate(boundaries):
        print(f"\n--- 境界フレーム {i+1}: フレーム#{boundary_idx} ---")
        
        # 境界フレーム周辺（前後2フレーム）をチェック
        check_range = range(max(0, boundary_idx - 2), min(len(frames), boundary_idx + 3))
        
        for frame_idx in check_range:
            frame_path = frames[frame_idx]
            
            try:
                # 画像読み込み
                buf = np.frombuffer(frame_path.read_bytes(), np.uint8)
                img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    print(f"  フレーム#{frame_idx}: 画像読み込み失敗")
                    continue
                
                # テンプレートマッチング実行
                corr = cv2.matchTemplate(img, tmpl_gray, cv2.TM_CCOEFF_NORMED)
                max_val = corr.max()
                max_loc = cv2.minMaxLoc(corr)[3]  # 最大値の位置
                
                # 結果表示
                status = "✓ マッチ" if max_val >= args.end_th else "✗ 非マッチ"
                marker = " ★ " if frame_idx == boundary_idx else "   "
                print(f"{marker}フレーム#{frame_idx}: 類似度 {max_val:.4f} {status}")
                
                # 検証結果記録
                verification_results.append({
                    'boundary_index': i + 1,
                    'frame_index': frame_idx,
                    'is_boundary_frame': frame_idx == boundary_idx,
                    'similarity': max_val,
                    'matches_template': max_val >= args.end_th,
                    'match_location': max_loc
                })
                
            except Exception as e:
                print(f"  フレーム#{frame_idx}: エラー - {e}")
    
    # 検証結果サマリー
    print(f"\n=== 検証結果サマリー ===")
    boundary_matches = 0
    total_boundaries = len(boundaries)
    
    for result in verification_results:
        if result['is_boundary_frame']:
            if result['matches_template']:
                boundary_matches += 1
                print(f"境界フレーム {result['boundary_index']}: ✓ テンプレートとマッチ (類似度: {result['similarity']:.4f})")
            else:
                print(f"境界フレーム {result['boundary_index']}: ✗ テンプレートと非マッチ (類似度: {result['similarity']:.4f})")
    
    match_rate = (boundary_matches / total_boundaries * 100) if total_boundaries > 0 else 0
    print(f"\n境界フレームのマッチ率: {boundary_matches}/{total_boundaries} ({match_rate:.1f}%)")
    
    if match_rate < 80:
        print("⚠ 警告: マッチ率が低いです。以下を確認してください:")
        print("  - テンプレート画像が適切か")
        print("  - しきい値 (--end-th) が適切か")
        print("  - フレーム品質に問題がないか")
    elif match_rate == 100:
        print("✓ 全ての境界フレームがテンプレートとマッチしています")
    else:
        print("△ 一部の境界フレームがマッチしていません")
    
    return verification_results

def save_boundary_verification_report(verification_results, boundaries, args):
    """境界フレーム検証結果をJSONファイルに保存
    
    Args:
        verification_results: verify_boundary_framesの結果
        boundaries: 境界フレームのリスト
        args: コマンドライン引数
    """
    if not args.verify_report:
        return
    
    import json
    from datetime import datetime
    
    # レポートデータ作成
    report_data = {
        'verification_timestamp': datetime.now().isoformat(),
        'template_threshold': args.end_th,
        'total_boundaries': len(boundaries),
        'boundaries': boundaries,
        'verification_details': verification_results,
        'summary': {
            'boundary_matches': sum(1 for r in verification_results if r['is_boundary_frame'] and r['matches_template']),
            'total_boundaries': len(boundaries),
            'match_rate_percent': 0
        }
    }
    
    # マッチ率計算
    if len(boundaries) > 0:
        report_data['summary']['match_rate_percent'] = (
            report_data['summary']['boundary_matches'] / len(boundaries) * 100
        )
    
    # ファイル保存
    try:
        with open(args.verify_report, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        print(f"境界フレーム検証レポート保存: {args.verify_report}")
    except Exception as e:
        print(f"検証レポート保存エラー: {e}")

def main():
    """メイン処理"""
    global processed, last_print, total_frames
    
    # コマンドライン引数パーサー設定
    ap = argparse.ArgumentParser(
        description="PUBGラウンド境界検出スクリプト",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  基本実行:
    python segment_rounds.py data/frames/2025-05-02 --template data/templates/Match_End_template.jpg
  
  しきい値調整:
    python segment_rounds.py data/frames/2025-05-02 --template template.jpg --end-th 0.6 --segments 6
  
  処理内容確認（ドライラン）:
    python segment_rounds.py data/frames/2025-05-02 --template template.jpg --dry-run
  
  OCR機能を有効化:
    python segment_rounds.py data/frames/2025-05-02 --template template.jpg --enable-ocr
  
  OCR詳細分析（レポート付き）:
    python segment_rounds.py data/frames/2025-05-02 --template template.jpg --enable-ocr --ocr-confidence 0.7 --ocr-report ocr_analysis.json
        """
    )
    
    ap.add_argument('frames_dir', nargs='?', default='data/frames', 
                    help='フレーム画像が格納されたディレクトリ（例: data/frames/2025-05-02）')
    ap.add_argument('--template', required=True, 
                    help='テンプレート画像ファイルパス（必須）')
    ap.add_argument('--out-root', default='.', 
                    help='出力ルートディレクトリ（後方互換性のため残存、現在未使用）')
    ap.add_argument('--segments', type=int, default=5, 
                    help='出力ラウンド数（デフォルト: 5）')
    ap.add_argument('--threshold', type=int, default=10, 
                    help='aHash ハミング距離しきい値（デフォルト: 10、現在未使用）')
    ap.add_argument('--cluster-gap', type=int, default=5, 
                    help='同一テンプレートクラスタ判定間隔（デフォルト: 5）')
    ap.add_argument('--end-th', type=float, default=0.5, 
                    help='テンプレートマッチング類似度しきい値（デフォルト: 0.5）')
    ap.add_argument('--peek', action='store_true', 
                    help='移動せず区切り候補を表示のみ')
    ap.add_argument('--dry-run', action='store_true', 
                    help='実際のファイル操作を行わず処理内容を表示')
    ap.add_argument('--log-file', 
                    help='移動履歴を CSV ファイルに保存')
    ap.add_argument('--step', type=int, default=1, 
                    help='テンプレートマッチングのステップ数（デフォルト: 1）')
    ap.add_argument('--enable-ocr', action='store_true', 
                    help='OCR機能を有効化してテキスト情報を活用')
    ap.add_argument('--ocr-confidence', type=float, default=0.6, 
                    help='OCR信頼度しきい値（デフォルト: 0.6）')
    ap.add_argument('--ocr-sample-rate', type=int, default=10, 
                    help='OCR分析のサンプリング間隔（デフォルト: 10フレームに1回）')
    ap.add_argument('--ocr-report', 
                    help='OCR分析結果をJSONファイルに保存')
    ap.add_argument('--verify-report', 
                    help='境界フレーム検証結果をJSONファイルに保存')
    
    args = ap.parse_args()

    # フレームディレクトリの検証
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

    # テンプレート画像の読み込み（グレースケール）
    tmpl_gray = cv2.imread(args.template, cv2.IMREAD_GRAYSCALE)
    if tmpl_gray is None:
        raise SystemExit('Template image not found or unreadable')

    print('aHashアルゴリズムによる画像ハッシュ計算を開始...')
    start = time.time()

    # aHash計算（並列処理）
    global processed, last_print, total_frames, start_ahash
    processed = 0
    last_print = time.time()
    start_ahash = time.time()
    total_frames = len(frames)

    with ProcessPoolExecutor() as ex:
        hashes = list(ex.map(ahash_progress_global, frames))
    elapsed = time.time() - start
    rate = len(frames) / elapsed if elapsed > 0 else 0
    print(f"\naHash計算完了: {len(frames)}フレーム, {elapsed:.2f}秒 ({rate:.1f} fps)")

    # フレーム間ハミング距離計算
    print("フレーム間ハミング距離を計算中...")
    hd = partial(hdist)
    dists = [hd(hashes[i], hashes[i+1]) for i in range(len(hashes) - 1)]

    print(f'テンプレートマッチング開始（しきい値: {args.end_th}, ステップ: {args.step}）...')
    start_detect = time.time()

    # テンプレートマッチング実行
    t_idx = detect_template_frames(
        frames, tmpl_gray, args.end_th,
        step=args.step,
        cluster_gap=args.cluster_gap,
        max_workers=os.cpu_count() or 8
    )
    
    elapsed_detect = time.time() - start_detect
    print(f"テンプレートマッチング完了: {len(t_idx)}個の候補を検出, {elapsed_detect:.2f}秒")
    t_idx.sort()

    # 境界フレームのクラスタリング
    print("境界フレームをクラスタリング中...")
    clusters = []
    for idx in t_idx:
        if not clusters or idx - clusters[-1][-1] > args.cluster_gap:
            clusters.append([idx])
        else:
            clusters[-1].append(idx)
    boundaries = [c[0] for c in clusters]
    print(f"テンプレートマッチングで{len(boundaries)}個の境界を検出")

    # 不足分をaHashベースで補完
    need = args.segments - 1 - len(boundaries)
    if need > 0:
        print(f"aHashベースで{need}個の境界を追加検索中...")
        cand = sorted(range(len(dists)), key=lambda i: dists[i], reverse=True)
        for i in cand:
            if all(abs(i - b) > 150 for b in boundaries):
                boundaries.append(i)
                if len(boundaries) == args.segments - 1:
                    break
        print(f"aHashで{len(boundaries) - len([c[0] for c in clusters])}個の境界を追加")
    boundaries = sorted(boundaries)

    # OCR分析（オプション機能）
    ocr_results = {}
    if args.enable_ocr and OCR_AVAILABLE:
        print(f"\nOCR分析を開始中... (サンプリング間隔: {args.ocr_sample_rate})")
        print("境界フレーム周辺のテキスト情報を分析中...")
        
        # 境界フレーム周辺をOCR分析
        ocr_frames = set()
        for boundary in boundaries:
            # 境界前後のフレームをサンプリング
            for offset in range(-5, 6):  # 境界前後5フレーム
                idx = boundary + offset
                if 0 <= idx < len(frames):
                    ocr_frames.add(idx)
        
        # 追加的に全体をサンプリング
        for i in range(0, len(frames), args.ocr_sample_rate):
            ocr_frames.add(i)
        
        ocr_frames = sorted(ocr_frames)
        print(f"OCR分析対象: {len(ocr_frames)}フレーム")
        
        ocr_start_time = time.time()
        analyzed_count = 0
        interesting_frames = []
        
        for frame_idx in ocr_frames:
            analysis = analyze_frame_with_ocr(frames[frame_idx], args.ocr_confidence)
            if analysis['status'] == 'text_detected':
                ocr_results[frame_idx] = analysis
                if analysis.get('game_state') in ['round_end', 'round_start']:
                    interesting_frames.append(frame_idx)
            analyzed_count += 1
            
            # 進捗表示
            if analyzed_count % 10 == 0 or analyzed_count == len(ocr_frames):
                pct = (analyzed_count / len(ocr_frames)) * 100
                elapsed = time.time() - ocr_start_time
                rate = analyzed_count / elapsed if elapsed > 0 else 0
                print(f"\rOCR分析進捗: {analyzed_count}/{len(ocr_frames)} ({pct:.1f}%) | {rate:.1f} fps", end="", flush=True)
        
        print(f"\nOCR分析完了: {len(ocr_results)}フレームでテキスト検出")
        if interesting_frames:
            print(f"興味深いフレーム: {len(interesting_frames)}個 (ラウンド境界候補)")
            # OCRで検出された境界候補を境界リストに追加検討
            for frame_idx in interesting_frames:
                if all(abs(frame_idx - b) > 50 for b in boundaries):
                    print(f"  フレーム{frame_idx}: OCRで{ocr_results[frame_idx]['game_state']}を検出")
        
        # OCRレポート保存
        if args.ocr_report:
            report_data = {
                'total_frames': len(frames),
                'analyzed_frames': len(ocr_frames),
                'text_detected_frames': len(ocr_results),
                'interesting_frames': interesting_frames,
                'boundaries_detected': boundaries,
                'frame_analyses': {str(k): v for k, v in ocr_results.items()}
            }
            with open(args.ocr_report, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, ensure_ascii=False, indent=2)
            print(f"OCR分析レポート保存: {args.ocr_report}")
    
    elif args.enable_ocr and not OCR_AVAILABLE:
        print("注意: OCRが要求されましたが、EasyOCRライブラリが利用できません")

    boundaries = sorted(boundaries)

    # 境界フレーム検証
    print(f"\n境界フレーム検証を実行中...")
    verification_results = verify_boundary_frames(frames, boundaries, tmpl_gray, args)
    save_boundary_verification_report(verification_results, boundaries, args)

    # 結果表示・確認モード
    segments_info = [b - a for a, b in zip([0]+boundaries, boundaries+[len(frames)])]
    print(f"\n=== セグメンテーション結果 ===")
    print(f"総フレーム数: {len(frames)}")
    print(f"境界フレーム: {boundaries}")
    print(f"各セグメントのフレーム数: {segments_info}")
    
    if args.peek or args.dry_run:
        if args.peek:
            return  
        
    # 出力ディレクトリ構成（data/<upload-date>/形式）
    upload_date = frames_dir.name
    if upload_date == 'frames':
        raise SystemExit('frames_dir must be data/frames/<upload-date>')
    
    out_root = Path('data') / upload_date
    out_root.mkdir(parents=True, exist_ok=True)
    
    # ラウンドディレクトリ作成
    print(f"\n=== ファイル処理開始 ===")
    print(f"出力先: {out_root}")
    rounds = []
    prev = 0
    for i, b in enumerate(boundaries + [len(frames)]):
        rdir = out_root / f'round{i+1}'
        rdir.mkdir(exist_ok=True)
        rounds.append((prev, b, rdir))
        prev = b

    # ファイルコピー処理（元ファイル保持）
    print("ファイルコピー中...")
    moves = []
    total_copied = 0
    for round_idx, (start_i, end_i, rdir) in enumerate(rounds, 1):
        num_frames = end_i - start_i
        print(f"ラウンド{round_idx}処理中: {num_frames}フレーム -> {rdir.name}/")
        
        for idx, f in enumerate(frames[start_i:end_i], 1):
            new_name = f"Frames_{idx:05d}.jpg"  # 連番リセット
            dst = rdir / new_name
            if not args.dry_run:
                shutil.copy2(f, dst)  # 元ファイル保持（copy2使用）
                total_copied += 1
            moves.append((str(f), str(dst)))
        
        print(f"  → {rdir.name}: {num_frames}フレーム完了")
    
    if not args.dry_run:
        print(f"\n合計 {total_copied}ファイルをコピーしました")
    else:
        print(f"\n（ドライラン）合計 {len(moves)}ファイルがコピー対象です")

    # 移動履歴ログ出力
    if args.log_file:
        print(f"処理履歴を{args.log_file}に保存中...")
        with open(args.log_file, 'w') as fp:
            fp.write('src,dst\n')
            for s, d in moves:
                fp.write(f'{s},{d}\n')
        print(f"履歴ファイル保存完了: {args.log_file}")

    print("\n=== 処理完了 ===")

default_main = main

if __name__ == '__main__':
    main()
