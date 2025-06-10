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
|       |-- auto_ai_PR.yml
|       |-- daily-digest.yml
|       `-- update-tree.yml
|-- Agents
|   `-- issue_auto_solver.py
|-- docs
|   |-- GUI_implementation.md
|   |-- GUI_requirements.md
|   `-- JAPANESE_SUPPORT.md
|-- screenshot
|   |-- sample
|   |   |-- frame_00559.jpg
|   |   `-- frame_01387.jpg
|   `-- connect_wsl.png
|-- scripts
|   `-- issue_auto_solver.py
|-- src
|   |-- gui
|   |   |-- main.py
|   |   `-- styles.py
|   |-- check_env.py
|   |-- clean_same_frames.py
|   |-- crop_minimap.py
|   |-- segment_rounds.py
|   `-- utils.py
|-- tests
|   |-- test_clean_same_frames.py
|   `-- test_segment_rounds.py
|-- .gitignore
|-- .markdownlint.json
|-- AGENTS.md
|-- README.md
|-- TREE.md
|-- config.yaml
|-- extract_frames.sh
|-- idea.md
|-- requirements.txt
|-- survey.md
`-- 作業メモ.md

12 directories, 34 files
```
<!-- DIR-END -->

## 動画URLからフレーム抽出  

MapSight_AI/data でコマンド実行．
コマンド例:
./extract_frames.sh "https://www.youtube.com/watch?v=tkbV9EJPak4"

・fps=2 → 0.5 s ごとに 1 枚（後で変更可能） # 0.5に変更済み
・生成先 data/frames/<公開日>/ は後段スクリプトが再帰検索します。
・画質を保ちたい場合は -q:v 2（2-31、数字が小さいほど高画質）。

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

## データ取得の流れ

仮想環境:pubgmapenvの中で

1. extract_frames.sh に対象URLを渡して実行(data/framesに画像データが生成される)
2. crop_minimap.pyを実行（対象ディレクトリの箇所を適宜変更）
3. clean_same_frames.pyを実行
4. segment_rounds.pyを実行

この段階でラウンドごとにマップ画像が保存される．（まだ不必要なデータが含まれている）
