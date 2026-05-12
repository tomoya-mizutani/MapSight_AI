# detect_minimap_positions.py

## 概要
`detect_minimap_positions.py` は、ミニマップフレームからプレイヤーアイコンを検出して JSON Lines 形式で出力する CLI ツールです。テンプレートマッチングと HSV 色空間によるしきい値処理の 2 種類の手法に対応しており、検出結果は追跡 (`assign_tracks_to_players.py`) やスケルトン補完 (`fill_positions_jsonl.py`) に利用されます。

## 対応する検出手法
- **テンプレートマッチング**: OpenCV の `matchTemplate` を使用し、ピーク候補から IoU に基づく NMS で重複を除去します。
- **HSV 閾値処理**: HSV 空間の範囲指定・モルフォロジー処理・輪郭抽出によってアイコン候補を抽出し、重複候補は NMS で整理します。

## 主な構造体
- `Detection`: 単一の検出結果。中心座標、スコア、矩形サイズ、検出手法名を保持します。
- `FrameRecord`: フレーム単位の検出集合。JSON 出力をサポートします。
- `TemplateConfig` / `HSVConfig`: それぞれの検出パラメータを保持します。
- `DetectorConfig`: 実行時に使用する手法種別や NMS 閾値を統合した設定です。

## コマンドライン引数
| 引数 | 説明 |
| ---- | ---- |
| `frames_dir` | ミニマップフレーム画像ディレクトリ |
| `output_jsonl` | 検出結果(JSONL)の出力先 |
| `--method` | `template` または `hsv` (デフォルト: `template`) |
| `--template` | テンプレート画像のパス（`template` 手法で必須） |
| `--threshold` | テンプレートマッチングのスコア閾値 |
| `--match-mode` | OpenCV のテンプレートマッチングモード |
| `--hsv-lower` / `--hsv-upper` | HSV の下限・上限 (例: `0,0,200`) |
| `--morph-kernel` / `--morph-iterations` | HSV 手法のモルフォロジー設定 |
| `--min-area` / `--max-area` | HSV 手法で残す輪郭の面積範囲 |
| `--nms-threshold` | IoU に基づく NMS の閾値 |
| `--max-detections` | NMS 後に保持する最大検出数 (任意) |

## 実行フロー
1. 引数から `DetectorConfig` を構築し、テンプレート画像や HSV 設定を読み込む。
2. フレームディレクトリを走査して画像を読み込み、手法に応じた検出器を実行する。
3. NMS で候補を整理し、`FrameRecord` として集計する。
4. 全フレームの検出統計を標準エラーに出力しながら、結果を JSON Lines 形式で保存する。

## 補足
- 画像ファイル名に含まれる数字を利用してフレーム番号を推定します。連番が含まれない場合は 0 が使用されます。
- OpenCV (`cv2`) と NumPy が必須依存関係です。
- ログは標準エラーに出力され、進捗や設定を確認できます。
