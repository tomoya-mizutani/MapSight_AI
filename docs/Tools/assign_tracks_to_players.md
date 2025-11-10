# assign_tracks_to_players.py

## 概要
`assign_tracks_to_players.py` は、ミニマップ上で検出されたプレイヤー位置とロスターに記載されたプレイヤー UID をフレーム毎に対応付ける CLI ツールです。検出結果(JSON Lines)とロスター CSV を入力に、プレイヤーごとの追跡情報を含む JSON Lines を生成します。追跡には定速移動モデルを用いた予測と、ハンガリアン法による最適割当てを組み合わせています。

## 入出力
- **入力**
  - `detections_jsonl`: `detect_minimap_positions.py` が出力した検出結果(JSONL)
  - `roster_csv`: `player_uid` 列を含むロスター CSV
- **出力**
  - `output_jsonl`: 各フレームにおけるプレイヤー割当て(JSONL)

## 主な処理の流れ
1. ロスター CSV を読み込み、追跡対象の `player_uid` を列挙する。
2. 検出 JSONL をフレーム単位に構造化し、各検出を `DetectionObservation` として保持する。
3. 1 フレーム目では x 座標順の貪欲法で初期割当てを行い、各プレイヤーの `TrackState` を初期化する。
4. 2 フレーム目以降は、予測位置と検出位置のユークリッド距離でコスト行列を作成し、`linear_sum_assignment`（ハンガリアン法）で最小コスト割当てを実施する。
5. 割当てられたトラックは速度ベクトルを更新し、未割当てのトラックは欠損カウンタを増やして `unknown` または `eliminated` 状態へ遷移させる。
6. 生成した `FrameAssignments` を JSON Lines として保存する。

## 主要クラスと責務
- `DetectionObservation`: 単一検出の座標・スコア・手法名を保持。
- `FrameDetections`: フレーム単位の検出リストを保持。
- `TrackState`: プレイヤーの状態、最後に観測した座標・速度、欠損フレーム数を管理し、予測・更新・欠損処理を提供。
- `Assignment`: プレイヤーごとの出力レコード。JSON シリアライズ機能を持つ。
- `FrameAssignments`: フレーム単位の出力レコード集合。

## コマンドライン引数
| 引数 | 説明 |
| ---- | ---- |
| `detections_jsonl` | 検出結果(JSONL)のパス |
| `roster_csv` | `player_uid` 列を含むロスター CSV |
| `output_jsonl` | 追跡結果(JSONL)の出力パス |
| `--max-missed` | 割当てなしでもトラックを保持する最大フレーム数（デフォルト: 5） |
| `--eliminate-after` | 欠損が続いた際に `eliminated` とみなすフレーム数（負値で無効） |
| `--distance-threshold` | 割当てを許可する最大ピクセル距離 |
| `--velocity-damping` | 速度更新時の減衰係数（0 で新速度、1 で旧速度を保持） |

## 補足
- 追跡ループではログを標準エラーに出力し、処理状況を把握できます。
- ハンガリアン法の実装には SciPy (`scipy.optimize.linear_sum_assignment`) を使用します。
- 出力 JSON Lines は後続の `fill_positions_jsonl.py` で利用できます。
