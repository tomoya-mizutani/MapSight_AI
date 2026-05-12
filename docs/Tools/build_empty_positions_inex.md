# build_empty_positions_inex.py

## 概要
`build_empty_positions_inex.py` は、試合用のミニマップフレームに対して 64 プレイヤー分の空レコードを生成するスケルトン作成ツールです。ロスター CSV とフレーム画像群を読み込み、後続処理で座標やステータスを埋められるよう初期値を設定した JSON Lines を出力します。

## 入出力
- **入力**
  - `minimap_dir`: ミニマップフレーム画像を格納したディレクトリ
  - `match_id`, `map_name`, `map_round`: 生成レコードに埋め込むメタデータ文字列
  - `roster_csv`: `player_uid` を含むロスター CSV
- **出力**
  - `output_jsonl`: 各フレーム・各プレイヤーについて空の位置情報を記録した JSONL

## 主な処理の流れ
1. ロスターを読み込み、全プレイヤー UID を抽出する。
2. フレームディレクトリから `frame001.png` 等のパターンに合致するファイルを走査し、フレーム番号でソートする。
3. 各フレームについて、`player_uid` ごとに初期状態 (`status=unknown`, 座標は `None`) のレコードを生成する。
4. 生成レコードにはチーム ID やスロット情報を `player_uid` から派生させて格納する。
5. JSON Lines として書き出し、進捗と統計情報を標準エラーにログする。

## コマンドライン引数
| 引数 | 説明 |
| ---- | ---- |
| `minimap_dir` | ミニマップフレーム画像ディレクトリ |
| `match_id` | 例: `2025-09-21_PMJL_R1` |
| `map_name` | 例: `erangel` |
| `map_round` | 例: `R1` |
| `roster_csv` | `player_uid` 列を含むロスター CSV |
| `output_jsonl` | 出力 JSONL の保存先 |
| `--fps` | フレーム間隔から `ts_ms` を計算するためのフレームレート (デフォルト 2.0 FPS) |

## 補足
- フレームファイル名からフレーム番号を抽出するため、`frame_001.png` のように末尾に連番が含まれている必要があります。
- 各レコードには `team_id` や `player_slot` など、後段処理で必要となるメタ情報が含まれます。
- 出力は `fill_positions_jsonl.py` の入力スケルトンとして想定されています。
