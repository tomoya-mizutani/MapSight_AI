# githubの開発フロー早わかり・説明

開発時におけるGithub運用ルールというか，基本的な使いかと記述しておく

## Workflow (for my future self)

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


## commit テンプレ

```text
<type>(scope): <短い概要>  #<Issue番号>

type = feat | fix | docs | refactor | chore | test  
scope = オプション: モジュール名や機能名  

<例>
feat(map): add heatmap aggregation logic  #23
fix(ml): prevent NaN in MLP loss          #45
```

```text
/notes/*.md は，差分ごとにcommitを出す．意味的な変更を含まない場合は daily updateで済ませる．

```

### 作業途中の場合

git stashを使う
- 新規ファイルがある場合:git stash -u
- 退避に名前をつけるコマンド: git stash push -u -m "WIP: message(作業内容) "

- 取り出し方: git stash pop (stashは消える)　or git stash apply(stashは残す)

## プルリクのテンプレ

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