# MAP_SIGHT_AI

terminal :wsl  
python version is 3.12.3  
git version is 2.43.0.windows.1  

仮想環境: python3.12-venv  
起動コマンド: source ~/pubgmapenv/bin/activate  
終了コマンド:deactivate  

## 📂 ディレクトリ構造図
<!-- DIR-START -->
```
.
|-- .git
|   |-- hooks
|   |   |-- applypatch-msg.sample
|   |   |-- commit-msg.sample
|   |   |-- fsmonitor-watchman.sample
|   |   |-- post-update.sample
|   |   |-- pre-applypatch.sample
|   |   |-- pre-commit.sample
|   |   |-- pre-merge-commit.sample
|   |   |-- pre-push.sample
|   |   |-- pre-rebase.sample
|   |   |-- pre-receive.sample
|   |   |-- prepare-commit-msg.sample
|   |   |-- push-to-checkout.sample
|   |   |-- sendemail-validate.sample
|   |   `-- update.sample
|   |-- info
|   |   `-- exclude
|   |-- logs
|   |   |-- refs
|   |   |   |-- heads
|   |   |   |   `-- main
|   |   |   `-- remotes
|   |   |       `-- origin
|   |   |           |-- HEAD
|   |   |           `-- main
|   |   `-- HEAD
|   |-- objects
|   |   |-- 07
|   |   |   `-- dd7c10b9e70aaf16687d387f3fe35b3990984c
|   |   |-- 31
|   |   |   `-- c520e5f99c213cab90c0d819c1c11cb54f7748
|   |   |-- 36
|   |   |   `-- b4c23f7b8d69923d0daa9515a7855e2dae3c32
|   |   |-- 47
|   |   |   `-- 70b82f1d0f8dd728df9c53ccf617d39b579328
|   |   |-- 48
|   |   |   `-- ebdbca592f979832d474db5b8638325f5b7797
|   |   |-- 4a
|   |   |   `-- 09ac579b2642cc6fe3be4dd626ce4601e5c871
|   |   |-- 51
|   |   |   `-- 9f4d08168e88af7911a23dea0e6a0a4d603c2b
|   |   |-- 55
|   |   |   `-- f392ff827e5cdaf9b62ddd8ba4b9a1abedb4ce
|   |   |-- 5c
|   |   |   `-- 01865d7c63170180961988b7fc3ca4a325cabd
|   |   |-- 63
|   |   |   `-- 3efc0d014d0c1edf6e269571089e26c7b20c15
|   |   |-- 74
|   |   |   `-- de66f0fc821ab529c8f96daff2c38ceb3d873b
|   |   |-- 8f
|   |   |   `-- ce603003c1e5857013afec915ace9fc8bcdb8d
|   |   |-- 96
|   |   |   `-- ead1d6bf0a23c745f59db87f7355e4be793a1d
|   |   |-- 9d
|   |   |   `-- 75bf9903ce631aa37e904c391c7e5d2abc87c9
|   |   |-- aa
|   |   |   `-- 91f41eaca77d41efe604e1c22f93ea9a60a232
|   |   |-- ae
|   |   |   `-- 3af18eb60090ead80c76a0d6a5c846e335fda5
|   |   |-- bb
|   |   |   `-- ddef655f8f30471c09e94c28d6536dee0a8042
|   |   |-- c9
|   |   |   |-- 6a3ef4590b956f5f0ce80187c2e2a5fc923fae
|   |   |   `-- a6644ea7913d87dbc4b287ef3096ab398710dd
|   |   |-- cc
|   |   |   `-- c7d7c0a9fcf41486ba29d63328e4a3142e1f19
|   |   |-- dc
|   |   |   `-- 40b58fbc09b7f8e052d96a1e14859c784e13a6
|   |   |-- de
|   |   |   `-- 38b51384caa6c8e2a20ba319f0d38353a6bb1c
|   |   |-- e6
|   |   |   `-- 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
|   |   |-- ee
|   |   |   `-- d3c9bab5abbbff504e54ebe0bae000003428e7
|   |   |-- f0
|   |   |   `-- 9609b87278813c05b27f47476810127017f82d
|   |   |-- info
|   |   `-- pack
|   |-- refs
|   |   |-- heads
|   |   |   `-- main
|   |   |-- remotes
|   |   |   `-- origin
|   |   |       |-- HEAD
|   |   |       `-- main
|   |   `-- tags
|   |-- FETCH_HEAD
|   |-- HEAD
|   |-- config
|   |-- description
|   |-- index
|   `-- shallow
|-- .github
|   |-- ISSUE_TEMPLATE
|   |   |-- bug.yaml
|   |   |-- log.yaml
|   |   `-- task.yaml
|   `-- workflows
|       |-- daily-digest.yml
|       `-- update-tree.yml
|-- screenshot
|   `-- connect_wsl.png
|-- src
|   |-- check_env.py
|   |-- clean_same_frames.py
|   |-- crop_minimap.py
|   |-- segment_rounds.py
|   `-- utils.py
|-- .gitignore
|-- README.md
|-- TREE.md
|-- config.yaml
|-- extract_frames.sh
|-- requirements.txt
|-- survey.md
`-- 作業メモ.md

46 directories, 72 files
```
<!-- DIR-END -->


## 動画URLからフレーム抽出  

MapSight_AI/data　でコマンド実行．  
コマンド:  
YOUTUBE="<https://www.youtube.com/watch?v=tkbV9EJPak4>"  
ffmpeg -i "$(yt-dlp -f best -g "$YOUTUBE")" \
       -vf "fps=2,scale=1920:-2" -q:v 2 frames/frame_%05d.jpg  

・fps=2 → 0.5 s ごとに 1 枚（後で変更可能） # 0.5に変更済み
・生成先 frames/ は後段スクリプトが再帰検索します。  
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
