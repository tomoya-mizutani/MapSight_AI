#!/usr/bin/env python3
"""
IssueAutoSolver – GitHub Issueを自動で解析し解決案PRを提案するエージェント
"""
import argparse
from github import Github
from openai import OpenAI  # 新しいインポート方法
import os
import sys

def solve_issue(repo):
    # GitHub認証
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[ERROR] GITHUB_TOKEN環境変数が設定されていません。")
        sys.exit(1)
    g = Github(token)
    try:
        repository = g.get_repo(repo)
    except Exception as e:
        print(f"[ERROR] リポジトリ取得失敗: {e}")
        sys.exit(1)

    # OpenAI認証
    openai_key = os.environ.get("OPENAI_API_KEY")
    if not openai_key:
        print("[ERROR] OPENAI_API_KEY環境変数が設定されていません。")
        sys.exit(1)
    client = OpenAI(api_key=openai_key)

    # 未解決Issueの1件を取得（最初のopen Issueのみ）
    issues = repository.get_issues(state="open")
    issues = [i for i in issues if not i.pull_request]
    if not issues:
        print("[INFO] Open Issueがありません。")
        return

    issue = issues[0]
    print(f"[INFO] Issue #{issue.number}: {issue.title}")

    # OpenAIで解決案を生成
    prompt = f"次のGitHub Issueを解決するためのPythonコード例と解決方針を出力してください。\n\nタイトル: {issue.title}\n本文: {issue.body}\n"
    print("[INFO] OpenAIで解決案を生成...")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは優秀なPythonプログラマーです。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=512,
        )
        answer = response.choices[0].message.content
        print(f"[INFO] AI解決案:\n{answer}")

        # サンプル：PRとしてmainブランチに「dummy_fix.py」をコミット
        pr_title = f"AI解決案: Issue #{issue.number} {issue.title}"
        pr_body = f"IssueへのAI提案\n\n---\n\n{answer}"
        branch_name = f"ai/fix_issue_{issue.number}"
        base = repository.get_branch("main")

        # ブランチ作成
        repository.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base.commit.sha)

        # ファイル追加（ダミーコード）
        dummy_code = "# AIによる自動修正サンプル\n" + (answer or "")
        repository.create_file(
            path="dummy_fix.py",
            message="AIによるIssue修正案コミット",
            content=dummy_code,
            branch=branch_name
        )

        # PR作成
        pr = repository.create_pull(
            title=pr_title,
            body=pr_body,
            head=branch_name,
            base="main"
        )
        print(f"[SUCCESS] PRを作成しました: {pr.html_url}")

    except Exception as e:
        print(f"[ERROR] OpenAI or GitHub操作で失敗: {e}")

def main():
    parser = argparse.ArgumentParser(description="GitHub Issueを自動で解決するエージェント")
    parser.add_argument('--repo', required=True, help='GitHubリポジトリ (例: username/project)')
    args = parser.parse_args()

    solve_issue(args.repo)

if __name__ == "__main__":
    main()