# MAP_SIGHT_AI

## システム概観図

### システム概要

``` text
[試合録画またはライブフィード]
          ↓（2秒間隔）
[マップ画像データ取得]
          ↓
[位置・状況データ抽出]
   ・プレイヤー位置(x,y,z)
   ・安全圏情報
   ・イベント情報（撃破、交戦）
          ↓
[データ前処理]
   ・座標正規化
   ・チーム単位のデータ統合
          ↓
[分析モデル適用]
   │
   ├───→ [行動予測モデル]
   │             ・時系列モデル（LSTM、Transformer）
   │             ・グラフニューラルネットワーク（GNN）
   │
   ├───→ [重要イベント検出]
   │             ・撃破、交戦開始などの検出
   │
   └───→ [戦術理論モデル]
                 ・安全圏戦略
                 ・カバーリング理論
                 ・物資取得・管理
                 ・エリアコントロール
                 ・リスク管理
          ↓
[分析結果統合]
          ↓
[テキストレポート生成]
   ・戦術的アドバイス
   ・イベントタイムライン
   ・次回試合への改善ポイント
          ↓
[可視化オプション]
   ・マップ軌跡表示
   ・イベントマーカー表示
          ↓
[コーチ・選手向け出力]
```

## 開発環境

terminal :bash  
python version is 3.12.3  
git version is 2.43.0.windows.1  

仮想環境: python3.12-venv  
起動コマンド: source ~/pubgmapenv/bin/activate  
終了コマンド:deactivate  

## Red Team Detector (Version 1)

`Faze_***` などの赤チーム表示から位置座標を取得する検出器の仕様は
`src/mapsight/analysis/red_team_detector.md` を参照してください。

## 📂 ディレクトリ構造図
<!-- DIR-START -->
<details>
<summary>📂 ディレクトリ構造図 (クリックで展開)</summary>

``` text
.
├── .git
.
|-- .github
|   |-- ISSUE_TEMPLATE
|   |   |-- bug.yaml
|   |   |-- log.yaml
|   |   `-- task.yaml
|   `-- workflows
|       |-- auto_ai_PR.yml
|       |-- daily-digest.yml
|       `-- update-tree.yml
|-- docs
|   |-- DATA_MANAGEMENT.md
|   |-- GUI_implementation.md
|   |-- GUI_requirements.md
|   |-- JAPANESE_SUPPORT.md
|   `-- VIDEO_PIPELINE.md
|-- screenshot
|   |-- sample
|   |   |-- frame_00559.jpg
|   |   |-- frame_00559_annotated.png
|   |   |-- frame_01387.jpg
|   |   |-- frame_01387_annotated.png
|   |   |-- test.png
|   |   `-- test_annotated.png
|   |-- connect_wsl.png
|   `-- スクリーンショット 2025-10-01 135237.png
|-- scripts
|   `-- issue_auto_solver.py
|-- src
|   |-- __pycache__
|   |   |-- clean_same_frames.cpython-312.pyc
|   |   `-- segment_rounds.cpython-312.pyc
|   |-- gui
|   |   |-- main.py
|   |   `-- styles.py
|   |-- mapsight
|   |   |-- analysis
|   |   |   |-- __pycache__
|   |   |   |   |-- __init__.cpython-312.pyc
|   |   |   |   `-- player_tracking.cpython-312.pyc
|   |   |   |-- __init__.py
|   |   |   |-- player_tracking.py
|   |   |   |-- red_team_detector.md
|   |   |   `-- red_team_detector.py
|   |   `-- schemas
|   |       `-- positions.py
|   |-- check_env.py
|   |-- clean_same_frames.py
|   |-- crop_minimap.py
|   |-- data_dirs.py
|   |-- segment_rounds.py
|   |-- utils.py
|   `-- video_pipeline.py
|-- tests
|   |-- __pycache__
|   |   |-- test_clean_same_frames.cpython-312-pytest-8.3.5.pyc
|   |   |-- test_clean_same_frames.cpython-312-pytest-8.4.2.pyc
|   |   |-- test_player_tracking.cpython-312-pytest-8.3.5.pyc
|   |   |-- test_player_tracking.cpython-312-pytest-8.4.2.pyc
|   |   |-- test_segment_rounds.cpython-312-pytest-8.3.5.pyc
|   |   `-- test_segment_rounds.cpython-312-pytest-8.4.2.pyc
|   |-- sample
|   |   `-- test_detect.py
|   |-- test_clean_same_frames.py
|   |-- test_data_dirs.py
|   |-- test_segment_rounds.py
|   `-- test_video_pipeline.py
|-- .gitignore
|-- .markdownlint.json
|-- README.md
|-- TREE.md
|-- config.yaml
|-- erangel_players.json
|-- extract_frames.sh
`-- requirements.txt

9 directories, 34 files
```
</details>
<!-- DIR-END -->

## 動画取り込み

`video_pipeline.py` を使うと動画URLのダウンロードからフレーム抽出まで一括実行できます。

```bash
python src/video_pipeline.py --url <VIDEO_URL> scrim 2024/05/06 --rounds 2
```

詳細は [docs/VIDEO_PIPELINE.md](docs/VIDEO_PIPELINE.md) を参照してください。

## データディレクトリ生成

`src/data_dirs.py` を使うと、Scrim や tournament フォルダを自動作成できます。詳細は [docs/DATA_MANAGEMENT.md](docs/DATA_MANAGEMENT.md) を参照してください。



## データ取得の流れ

仮想環境:pubgmapenvの中で

1. extract_frames.sh に対象URLを渡して実行(data/framesに画像データが生成される)
2. crop_minimap.pyを実行（対象ディレクトリの箇所を適宜変更）
3. clean_same_frames.pyを実行
4. segment_rounds.pyを実行

この段階でラウンドごとにマップ画像が保存される．（まだ不必要なデータが含まれている）

### 解析データについて

詳細は [データ設計.md](データ設計.md)に記述している

### やりたいこと

マップ画像を解析し，試合におけるマクロの動きとして何が重要か？を分析したい．

具体的に数値として分析できるものは
- 各プレイヤーの位置情報
   被っていたりもするので，そのあたりの処理をどうするか？も課題として残っているんだが）
ぐらいかなぁ，
それ以外にできることと言えば，時間を書ければ？
マップに対して，アノテーションを付けることができそう？かな

影とかそういうものから，高低差を推測する仕組みも導入したいかあ．

[高低差マップ erangel](https://pubgmap.io/ja/erangel.html?/v2/20/5qst94/BlEG)　を参照すれば，Mapの高低差も分析対象に含めることができるかもしれない．

高いところが強いとかね

もう一歩踏み込めば，家屋の位置情報と高低差の位置情報を含むことで，射線の通せる幅を考慮したマクロを組むことができるかもしれない．ルートの検出とかもしたいかも．
ルートの検出は探索問題としてできると思う．

なんやかんやで，肝となるのはオントロジーとか知識グラフをどうやって組み合わせるか？みたいな話なんだろうねぇ