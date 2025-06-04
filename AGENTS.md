# AGENTS.md

## エージェント一覧

| エージェント名        | 概要                                      | メインファイル                  | 依存ライブラリ           |
|----------------------|-------------------------------------------|-------------------------------|--------------------------|
| IssueAutoSolver      | GitHub Issueを自動で解析・解決しPRを作成  | agents/issue_auto_solver.py   | openai, PyGithub         |
| TestGenerator        | コードからユニットテストを自動生成         | agents/test_generator.py      | openai                   |
| DocSummarizer        | ドキュメントを自動で要約                  | agents/doc_summarizer.py      | openai                   |

---

## 各エージェント詳細

### IssueAutoSolver

- **概要**  
  GitHubリポジトリのIssueを取得し、内容をAIで解析。  
  解決策を提案し、必要に応じて自動で修正用PRを生成します。

- **主な利用シーン**  
  - バグ報告に対する自動修正提案
  - 機能追加要望に対する自動実装の試行

- **使い方**  
  ```bash
  python -m agents.issue_auto_solver --repo <ユーザー名/リポジトリ名> --token <GITHUB_TOKEN>
