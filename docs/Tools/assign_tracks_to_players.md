# assign_tracks_to_players.py

## 概要
`assign_tracks_to_players.py` は検出済みのミニマップ座標をプレイヤーのロスター情報に基づいてトラッキングし、各フレームにおけるプレイヤーの位置と状態を JSONL 形式で出力する CLI ツールです。検出結果 (`detect_minimap_positions.py`) とロスター CSV を入力として、ハンガリー法と一定速度モデルを用いたフレーム間対応付けを行います。【F:tools/assign_tracks_to_players.py†L1-L213】

## 入出力
- **入力**
  - `detections_jsonl`: `detect_minimap_positions.py` などで生成されたフレーム毎の検出結果 JSONL。【F:tools/assign_tracks_to_players.py†L163-L205】
  - `roster_csv`: `player_uid` 列を含むロスター CSV。【F:tools/assign_tracks_to_players.py†L173-L198】
- **出力**
  - `output_jsonl`: 各フレームのプレイヤーごとのアサイン結果を格納した JSONL。【F:tools/assign_tracks_to_players.py†L284-L311】

## 主要データ構造
- `DetectionObservation`: フレーム内の検出結果を表現。【F:tools/assign_tracks_to_players.py†L23-L33】
- `FrameDetections`: 1 フレーム分の検出群と画像パス。【F:tools/assign_tracks_to_players.py†L36-L45】
- `TrackState`: プレイヤートラックの状態（最新位置・速度・ステータスなど）を保持し、予測・更新・ロスト処理を担当。【F:tools/assign_tracks_to_players.py†L48-L121】
- `Assignment` / `FrameAssignments`: 出力 JSONL に記録されるプレイヤー毎・フレーム毎の結果。【F:tools/assign_tracks_to_players.py†L124-L152】

## 処理フロー
1. **ロスター読み込み**: `read_roster` が `player_uid` を収集し検証します。【F:tools/assign_tracks_to_players.py†L205-L228】
2. **検出読み込み**: `load_detections` が JSONL を `FrameDetections` リストへ変換します。【F:tools/assign_tracks_to_players.py†L231-L269】
3. **トラック初期化**: `initialise_tracks` が全プレイヤーの `TrackState` を生成。【F:tools/assign_tracks_to_players.py†L272-L275】
4. **初期割当**: 最初のフレームは X 座標でソートした貪欲法で決定。【F:tools/assign_tracks_to_players.py†L278-L320】
5. **フレーム更新**:
   - `build_cost_matrix` が予測位置と検出座標から距離コスト行列を作成。【F:tools/assign_tracks_to_players.py†L323-L356】
   - `linear_sum_assignment` によりハンガリー法で最小コスト割当を取得。【F:tools/assign_tracks_to_players.py†L360-L422】
   - マッチしなかったトラックは `mark_missing` によって状態更新し、`max_missed` や `eliminate_after` に応じて `unknown` / `eliminated` を設定。【F:tools/assign_tracks_to_players.py†L85-L121】【F:tools/assign_tracks_to_players.py†L407-L453】
6. **結果出力**: `save_assignments` が `FrameAssignments` を JSONL として書き出す。【F:tools/assign_tracks_to_players.py†L455-L466】

## CLI オプション
- `--max-missed`: 連続して未検出でもトラックを保持する最大フレーム数。【F:tools/assign_tracks_to_players.py†L179-L185】
- `--eliminate-after`: 指定フレーム数を超えて未検出の場合に `eliminated` へ移行（負値で無効化）。【F:tools/assign_tracks_to_players.py†L186-L196】
- `--distance-threshold`: 割当に許容する最大距離（px）。【F:tools/assign_tracks_to_players.py†L197-L201】
- `--velocity-damping`: 速度更新の減衰係数（0=新しい速度、1=既存速度保持）。【F:tools/assign_tracks_to_players.py†L202-L207】

## エラーハンドリング
`main` は例外発生時にメッセージを標準エラーへ出力し、ステータス 1 で終了します。【F:tools/assign_tracks_to_players.py†L478-L484】
