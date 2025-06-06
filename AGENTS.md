# Project Agents

このプロジェクトでAIエージェント（Codex）が行うタスクやその具体的な挙動を定義します。

## Available Tasks

### 1. Issue Auto Solver

- **Description**: GitHubのIssueを検出し、AIが自動的に解析して解決方法を提示し、プルリクエストを作成する。
- **Trigger Condition**: Labelが「auto-solve」に設定されたIssueを検知したとき。
- **Expected Behavior**:
  1. Issueを解析して適切な解決策を提案。
  2. コードの変更案を作成。
  3. 提案した解決策をPull RequestとしてGitHubへ送信。

### 2. Documentation Agent

- **Description**: プロジェクト内のソースコードから自動的にドキュメントを生成する。
- **Trigger Condition**: プロジェクト内の特定のファイルが変更された際や明示的なコマンドが与えられた時。
- **Expected Behavior**:
  1. 変更を検出したソースコードを解析。
  2. ドキュメント形式に変換し、docsフォルダ内に自動更新。

## Allowed Commands and APIs

Codexが使用可能な外部コマンドやAPIの一覧。

- `Github` (PyGithubを経由して利用)
- `OpenAI API`
- `dotenv`を用いた環境変数読み込み

## Project Constraints

- コードの生成・変更時には常にブランチを作成。
- PR作成時はレビュワーを自動設定。

