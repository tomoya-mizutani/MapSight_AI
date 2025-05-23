terminal :wsl  
python version is 3.12.3  
git version is 2.43.0.windows.1  

仮想環境: python3.12-venv  
起動コマンド: source ~/pubgmapenv/bin/activate   
終了コマンド:deactivate  


## 動画URLからフレーム抽出  
MapSight_AI/data　でコマンド実行．  
コマンド:  
YOUTUBE="https://www.youtube.com/watch?v=tkbV9EJPak4"     
ffmpeg -i "$(yt-dlp -f best -g "$YOUTUBE")" \
       -vf "fps=2,scale=1920:-2" -q:v 2 frames/frame_%05d.jpg  

・fps=2 → 0.5 s ごとに 1 枚（後で変更可能） # 0.5に変更済み
・生成先 frames/ は後段スクリプトが再帰検索します。  
・画質を保ちたい場合は -q:v 2（2-31、数字が小さいほど高画質）。  











## githubの開発フロー早わかり・説明
### Workflow (for my future self)
```
1. Create an Issue (task / bug / log)
2. Move it to **In Progress** on Projects
3. Commit with `feat: ...  #123`
4. Open PR, merge -> Done (auto-closed)
```

まとめ
```
    Issues = タスク＋作業ログ

    Projects = カンバンで見える化

    Actions（任意） = 毎日まとめてログ

    これだけで GitHub 内でタスク管理／履歴／振り返りが完結

    後からチームが増えても、そのままスケールアップできる

```
### commit テンプレ
```
<type>(scope): <短い概要>  #<Issue番号>

type = feat | fix | docs | refactor | chore | test  
scope = オプション: モジュール名や機能名  

<例>
feat(map): add heatmap aggregation logic  #23
fix(ml): prevent NaN in MLP loss          #45
```

### プルリクのテンプレ
```
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
