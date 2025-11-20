# build_empty_positions_inex.py

## 概要
`build_empty_positions_inex.py` はロスターとミニマップフレーム群を基に、プレイヤーごとの空のポジションレコードを生成するスケルトン JSONL を作成する CLI ツールです。後続の検出・トラッキング結果を埋め込むための基盤データを提供します。【F:tools/build_empty_positions_inex.py†L1-L86】

## 入力
- `minimap_dir`: ミニマップ画像を含むディレクトリ。【F:tools/build_empty_positions_inex.py†L16-L26】
- `match_id` / `map_name` / `map_round`: 出力レコードに付与するメタ情報。【F:tools/build_empty_positions_inex.py†L17-L26】
- `roster_csv`: `player_uid` 列を含むロスター CSV。【F:tools/build_empty_positions_inex.py†L16-L43】
- `output_jsonl`: 生成する JSONL ファイルのパス。【F:tools/build_empty_positions_inex.py†L16-L43】
- オプション: `--fps` はフレームの時間スタンプ計算に使用する FPS を指定（既定 2.0）。【F:tools/build_empty_positions_inex.py†L23-L26】

## 主要関数
- `parse_args`: CLI 引数を定義。【F:tools/build_empty_positions_inex.py†L15-L26】
- `read_roster`: CSV から `player_uid` を抽出し、処理時間ログを出力。【F:tools/build_empty_positions_inex.py†L29-L46】
- `scan_frames`: フレームディレクトリを走査し、ファイル名の連番でソート。【F:tools/build_empty_positions_inex.py†L49-L64】
- `frame_index_of`: フレームファイル名から連番を抽出。【F:tools/build_empty_positions_inex.py†L67-L73】
- `main`: 上記関数を連携させ JSONL を構築。【F:tools/build_empty_positions_inex.py†L76-L125】

## 出力レコード
生成される各レコードは以下の項目を含みます。【F:tools/build_empty_positions_inex.py†L93-L118】
- 試合メタ情報: `match_id`, `map_name`, `map_round`
- フレーム情報: `frame_index`, `ts_ms`, `image_path`
- プレイヤー識別: `team_id`, `player_slot`, `player_uid`
- 位置情報プレースホルダ: `status`（初期値 `unknown`）、`px_x` / `px_y` / `x_norm` / `y_norm`（初期は `None`）
- `confidence`, `calib_id`, `notes`（いずれも `None` 初期化）

## ログ・エラー処理
処理状況やデバッグ情報を標準エラーへ出力します。`main` は例外発生時に `[ERROR]` メッセージを出力して終了します。【F:tools/build_empty_positions_inex.py†L29-L126】
