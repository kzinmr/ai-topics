---
title: "Using Git with Coding Agents"
aliases:
  - using-git-with-agents
  - git-integration-patterns
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - git
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/"
---

# Using Git with Coding Agents

コーディングエージェントとGitを統合するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)で詳述。

## 核心哲学

### Agent Fluency Over Memorization
> "Coding agents deeply understand Git jargon and operations. Developers don't need to memorize commands—just know what's possible and prompt accordingly."

開発者はGitコマンドを暗記する必要はなく、**何が可能か**を知り、自然言語でエージェントに指示すればよい。

### History as a Curated Narrative
> "Don't think of the Git history as a permanent record of what actually happened - instead consider it to be a deliberately authored story that describes the progression of the software project."

Git履歴は「実際に起きたことの記録」ではなく、**意図的に編集されたプロジェクトの物語**として捉える。

### Zero-Risk Experimentation
> "Everything in Git can be undone. Agents safely handle complex operations (rebases, conflict resolution, history rewriting), making advanced Git accessible to all skill levels."

Gitの操作はすべて取り消し可能。エージェントが複雑な操作を安全に処理できる。

## 実用的なプロンプトライブラリ

| プロンプト | エージェントの行動 | 戦略的利点 |
|-----------|-------------------|-----------|
| `Start a new Git repo here` | `git init` | 即時プロジェクト開始 |
| `Commit these changes` | `git commit -m "..."` | バージョンスナップショット |
| `Review changes made today` | `git log` | **セッションコンテキストの seeding** |
| `Sort out this git mess for me` | マージ競合解決、ステージ修正 | 複雑なGitエラーの自動処理 |
| `Find and recover my code that does ...` | `reflog`、ブランチ、`git stash`検索 | 未コミット作業の回復 |
| `Use git bisect to find when this bug was introduced: ...` | コミットの二分探索 | バグ発生源の特定 |

## Context Seeding パターン

> "Starting a session with `Review changes made today` loads the agent's context with recent work, enabling seamless continuation, targeted fixes, or next-step proposals."

セッション開始時に`Review changes made today`を実行することで、エージェントが最近の作業内容を把握し、継続的な開発が可能になる。

## git bisect の民主化

歴史的に学習曲線が急で敬遠されがちだった`git bisect`が、エージェントによってオンデマンドデバッグツールに変貌。

> "Agents handle the test-condition boilerplate, transforming it into an on-demand debugging tool."

## reflog as a Safety Net

> "Captures uncommitted/stashed changes. Agents can search it to recover work that wasn't formally committed."

`reflog`は未コミット/スタッシュされた変更を記録。エージェントが「失った」コードを回復できる。

## 高度な操作：履歴の書き換え

### コミットサージェリー
- 最後のコミットを取り消し：`git reset --soft HEAD~1`
- 特定ファイルの削除：きめ細かいコミット編集
- コミットの結合とメッセージ書き換え

> "I've found that frontier models usually have really good taste in commit messages. I've accepted that the quality they produce is generally good enough, and often even better than what I would have produced myself."

### モジュール抽出
エージェントは元のコミットメタデータを保持したまま、モジュールを独立ライブラリとして抽出可能。

## 関連概念

- [[../agentic-engineering]] — 上位概念
- [[how-agents-work]] — エージェントの内部仕組み
- [[subagents]] — マルチエージェントパターン
