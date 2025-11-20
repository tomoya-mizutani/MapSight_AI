# fill_positions_jsonl.py

## 概要
`fill_positions_jsonl.py` はスケルトンのポジション JSONL を、トラッキングで得られたアサインメント情報で更新する CLI ツールです。ピクセル座標の反映、正規化座標の計算、ステータス・信頼度の更新、キャリブレーション ID 付与などを自動化します。【F:tools/fill_positions_jsonl.py†L1-L179】

## 入出力
- `positions_jsonl`: `build_empty_positions_inex.py` などで生成されたスケルトン JSONL。【F:tools/fill_positions_jsonl.py†L17-L36】
- `assignments_jsonl`: `assign_tracks_to_players.py` の出力など、プレイヤー毎のアサインメント情報。【F:tools/fill_positions_jsonl.py†L17-L36】
- `output_jsonl`: 更新済みレコードを書き出す JSONL。【F:tools/fill_positions_jsonl.py†L17-L36】
- オプション
  - `--calib-id`: 出力に付与するキャリブレーション ID（既定 `simple_norm_v1`）。【F:tools/fill_positions_jsonl.py†L36-L43】
  - `--image-root`: 画像パスの解決に使用するルートディレクトリ。【F:tools/fill_positions_jsonl.py†L43-L49】

## 主要コンポーネント
- `AssignmentData`: アサインメントの座標・状態を保持するデータクラス。【F:tools/fill_positions_jsonl.py†L9-L21】
- 読み込み処理: `load_assignments` がフレーム・プレイヤー単位にアサインメントを辞書化します。【F:tools/fill_positions_jsonl.py†L51-L91】
- 画像サイズ関連
  - `resolve_image_path`, `get_image_size`, `lookup_image_size`: 画像パスの解決とサイズ取得をキャッシュ付きで実施。【F:tools/fill_positions_jsonl.py†L23-L84】
  - `normalise_coordinates`: ピクセル座標を画像サイズで正規化。【F:tools/fill_positions_jsonl.py†L86-L102】
- メイン処理: `fill_positions` が各レコードを更新し、既存座標がある場合には再計算も行います。ステータスの復活誤りを補正し、統計ログを出力します。【F:tools/fill_positions_jsonl.py†L104-L173】

## 処理フロー
1. `parse_args` で引数を解析後、`load_assignments` でアサインメント辞書を準備。【F:tools/fill_positions_jsonl.py†L17-L91】
2. `fill_positions` がスケルトンファイルを 1 行ずつ読み、該当プレイヤーのアサインメントを適用。
   - 座標が存在すれば画像サイズを取得し正規化座標を再計算。
   - アサインメントが欠落している場合でも既存の座標があれば正規化値を再生成。
   - `status_history` を用いて `eliminated` が `alive` へ戻らないよう補正。【F:tools/fill_positions_jsonl.py†L104-L173】
3. 出力ファイルへ書き出し、統計を `[INFO]` ログとして出力します。【F:tools/fill_positions_jsonl.py†L158-L173】
4. 例外時には `[ERROR]` ログを出力し終了します。【F:tools/fill_positions_jsonl.py†L175-L179】

## 出力レコードの更新点
- `px_x`, `px_y`: アサインメントからのピクセル座標を反映。
- `x_norm`, `y_norm`: 画像サイズから正規化した座標（利用可能な場合）。
- `status`, `confidence`, `notes`: 最新のトラッキング情報で更新し、`calib_id` を指定値で上書き。【F:tools/fill_positions_jsonl.py†L104-L173】
