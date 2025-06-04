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

## 📂 ディレクトリ構造図
<!-- DIR-START -->
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
|       |-- daily-digest.yml
|       `-- update-tree.yml
|-- docs
|   |-- DATA_MANAGEMENT.md
|   |-- GUI_implementation.md
|   |-- GUI_requirements.md
|   |-- JAPANESE_SUPPORT.md
|   `-- VIDEO_PIPELINE.md
|-- screenshot
|   `-- connect_wsl.png
|-- src
|   |-- gui
|   |   |-- main.py
|   |   `-- styles.py
|   |-- check_env.py
|   |-- clean_same_frames.py
|   |-- crop_minimap.py
|   |-- data_dirs.py
|   |-- segment_rounds.py
|   |-- utils.py
|   `-- video_pipeline.py
|-- tests
|   |-- test_clean_same_frames.py
|   |-- test_data_dirs.py
|   |-- test_segment_rounds.py
|   `-- test_video_pipeline.py
|-- .gitignore
|-- .markdownlint.json
|-- AGENTS.md
|-- README.md
|-- TREE.md
|-- config.yaml
|-- extract_frames.sh
|-- requirements.txt
|-- survey.md
`-- 作業メモ.md

9 directories, 34 files
```
<!-- DIR-END -->

## 動画取り込み

`video_pipeline.py` を使うと動画URLのダウンロードからフレーム抽出まで一括実行できます。

```bash
python src/video_pipeline.py --url <VIDEO_URL> scrim 2024/05/06 --rounds 2
```

詳細は [docs/VIDEO_PIPELINE.md](docs/VIDEO_PIPELINE.md) を参照してください。

## データディレクトリ生成

`src/data_dirs.py` を使うと、Scrim や tournament フォルダを自動作成できます。詳細は [docs/DATA_MANAGEMENT.md](docs/DATA_MANAGEMENT.md) を参照してください。

## githubの開発フロー早わかり・説明

### Workflow (for my future self)

```text
1. Create an Issue (task / bug / log)
2. Move it to **In Progress** on Projects
3. Commit with `feat: ...  #123`
4. Open PR, merge -> Done (auto-closed)

```

まとめ

```text
    Issues = タスク＋作業ログ

    Projects = カンバンで見える化

    Actions（任意） = 毎日まとめてログ

    これだけで GitHub 内でタスク管理／履歴／振り返りが完結

    後からチームが増えても、そのままスケールアップできる

```

### commit テンプレ

```text
<type>(scope): <短い概要>  #<Issue番号>

type = feat | fix | docs | refactor | chore | test  
scope = オプション: モジュール名や機能名  

<例>
feat(map): add heatmap aggregation logic  #23
fix(ml): prevent NaN in MLP loss          #45
```

### プルリクのテンプレ

```text
概要 / Purpose
<!-- 何を・なぜ -->

🔗 関連 Issue
Fixes #123  <!-- 自動 Close したい場合は Fixes/Closes キーワード -->

✅ チェックリスト
- [ ] ビルドが通る
- [ ] 仕様書 / docs 更新
```

## 🌱 Development Workflow

1. **Issue を作る** (Task/Bug/Log)
2. **Projects の Todo** に置く
3. **branch**:`feature/<short-desc>` → コード
4. `feat: ...  #issue` で commit
5. PR → Merge → Projects Done (auto-archive)

👉 [Backlog Board](https://github.com/<user>/<repo>/projects/1) で全タスクを確認
