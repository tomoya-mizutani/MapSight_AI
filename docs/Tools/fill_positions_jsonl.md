# fill_positions_jsonl.py

## 概要
`fill_positions_jsonl.py` は、スケルトン化されたポジション JSON Lines を、追跡結果で補完して最終的な座標情報を生成する CLI ツールです。`assign_tracks_to_players.py` の出力を読み込み、ピクセル座標・正規化座標・ステータス・信頼度・ノートを反映します。

## 入出力
- **入力**
  - `positions_jsonl`: `build_empty_positions_inex.py` などで作成したスケルトン JSONL
  - `assignments_jsonl`: 追跡結果(JSONL)
- **出力**
  - `output_jsonl`: 座標やステータスを埋めた JSON Lines

## 主な処理の流れ
1. 割当て JSONL をフレーム番号と `player_uid` で多重辞書に読み込む。
2. スケルトン JSONL を 1 行ずつ読み込み、対応する割当てがあれば座標・ステータス・信頼度・ノートを更新する。
3. 座標が得られた場合は画像の幅・高さを取得し、`x_norm` / `y_norm` を算出する。
4. 割当てが見つからない場合も既存の座標があれば正規化値を補完する。
5. `calib_id` を付与し、プレイヤーが一度 `eliminated` になった後に `alive` へ戻らないよう履歴で補正する。
6. 更新したレコードを JSON Lines として出力する。

## コマンドライン引数
| 引数 | 説明 |
| ---- | ---- |
| `positions_jsonl` | スケルトン JSONL のパス |
| `assignments_jsonl` | 割当て JSONL のパス |
| `output_jsonl` | 補完後 JSONL の出力先 |
| `--calib-id` | 出力レコードに設定するキャリブレーション ID (デフォルト: `simple_norm_v1`) |
| `--image-root` | 画像パス解決時に使用するルートディレクトリ (任意) |

## 補足
- 画像サイズの取得には OpenCV (`cv2`) を使用し、ファイルはキャッシュして重複読み込みを避けています。
- 割当てが存在しない場合でも、元の JSON に座標があれば正規化座標を再計算します。
- 標準エラーには処理件数や欠損数などの統計が出力されます。
