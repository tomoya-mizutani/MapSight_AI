# detect_minimap_positions.py

## 概要
`detect_minimap_positions.py` はミニマップフレーム内のプレイヤーアイコンを抽出し、フレーム毎の検出結果を JSONL として出力する CLI ツールです。テンプレートマッチングと HSV しきい値処理の 2 系統の検出方法を提供し、非最大抑制（NMS）で重複を除去します。【F:tools/detect_minimap_positions.py†L1-L230】

## 構成要素
- `Detection` / `FrameRecord`: 各検出結果とフレーム単位の検出リスト。【F:tools/detect_minimap_positions.py†L29-L74】
- `TemplateConfig` / `HSVConfig` / `DetectorConfig`: 実行時設定のデータクラス群。【F:tools/detect_minimap_positions.py†L77-L116】
- 画像ユーティリティ
  - `extract_frame_index`, `list_frame_paths`, `iter_frames`: フレームの列挙と読込。【F:tools/detect_minimap_positions.py†L21-L119】【F:tools/detect_minimap_positions.py†L228-L271】
  - `load_template`: テンプレート画像と OpenCV マッチングモードをロード。【F:tools/detect_minimap_positions.py†L119-L138】
- 検出アルゴリズム
  - `detections_from_template`: テンプレートマッチングのピークを検出へ変換。【F:tools/detect_minimap_positions.py†L171-L220】
  - `detections_from_hsv`: HSV マスク・輪郭解析で検出を生成。【F:tools/detect_minimap_positions.py†L222-L267】
  - `compute_iou`, `nms`: バウンディングボックスの IoU 計算と非最大抑制。【F:tools/detect_minimap_positions.py†L141-L190】
- 出力ユーティリティ: `run_detection` が全フレームの処理をまとめ、`save_results` が JSONL へ書き出します。【F:tools/detect_minimap_positions.py†L273-L344】

## CLI オプション
- `frames_dir` / `output_jsonl`: 入出力パスを指定。【F:tools/detect_minimap_positions.py†L46-L69】
- `--method`: `template`（既定）または `hsv`。【F:tools/detect_minimap_positions.py†L62-L69】
- テンプレート方式専用: `--template`, `--threshold`, `--match-mode`。【F:tools/detect_minimap_positions.py†L69-L99】
- HSV 方式専用: `--hsv-lower`, `--hsv-upper`, `--morph-kernel`, `--morph-iterations`, `--min-area`, `--max-area`。【F:tools/detect_minimap_positions.py†L99-L129】
- 共通: `--nms-threshold`, `--max-detections`。【F:tools/detect_minimap_positions.py†L129-L138】

## 処理フロー
1. `parse_args` で CLI 引数を解析し、`build_detector_config` がテンプレートまたは HSV 設定を組み立てます。【F:tools/detect_minimap_positions.py†L32-L137】【F:tools/detect_minimap_positions.py†L200-L231】
2. `run_detection` がフレーム一覧を取得し、進捗ログを出力しながら各フレームに対して選択した検出法を実行します。【F:tools/detect_minimap_positions.py†L232-L322】
3. 各フレームの検出結果は `FrameRecord` に蓄積され、最終的に `save_results` が JSONL 出力を生成します。【F:tools/detect_minimap_positions.py†L323-L344】
4. 例外発生時には `[ERROR]` メッセージを標準エラーに出力して終了します。【F:tools/detect_minimap_positions.py†L346-L352】

## 出力形式
各行は以下の構造を持つ JSON です。【F:tools/detect_minimap_positions.py†L54-L74】【F:tools/detect_minimap_positions.py†L323-L336】
```json
{
  "frame_index": <int>,
  "image_path": "path/to/frame.png",
  "detections": [
    {"x_px": <float>, "y_px": <float>, "score": <float>, "width": <int>, "height": <int>, "method": "template:TM_CCOEFF_NORMED"}
  ]
}
```
