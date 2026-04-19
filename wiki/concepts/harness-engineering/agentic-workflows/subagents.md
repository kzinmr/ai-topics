---
title: "Subagents — Parallel AI Agent Delegation"
aliases:
  - subagents
  - sub-agent
  - multi-agent-delegation
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - multi-agent
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/"
---

# Subagents

メインのAIエージェントが**独立したサブエージェントを並列に起動**し、それぞれが隔離されたコンテキストとターミナルセッションでタスクを実行するパターン。

## 設計原則

### 1. 独立性
> "Each subagent gets its own conversation, terminal session, and toolset. Only the final summary is returned."

- サブエージェント間は**コンテキストを共有しない**
- メインエージェントとの会話はサブエージェントに伝わらない
- 各サブエージェントは独立した環境で動作

### 2. 並列性
> "Batch mode: up to 3 tasks to run in parallel. All run concurrently and results are returned together."

- 複数の独立したタスクを**同時に実行**
- 結果は配列で返ってくる
- 待ち時間が大幅に短縮

### 3. 自己完結性
> "Subagents have NO memory of your conversation. Pass all relevant info via the 'context' field."

- サブエージェントへの指示は**完全に自己完結**である必要がある
- メインの会話履歴は自動的に渡されない
- 必要なファイルパス、エラーメッセージ、制約条件を明示的に渡す

## 使用すべき場合

| ✅ 向いている | ❌ 向いていない |
|-------------|---------------|
| 推論重視のサブタスク（デバッグ、コードレビュー、リサーチ） | 推論不要の単純作業（`execute_code`で十分） |
| コンテキストが溢れる大規模データ処理 | 単一のツール呼び出し（直接呼び出す） |
| 並列独立ワークストリーム（AとBを同時にリサーチ） | ユーザーとの対話が必要なタスク（サブエージェントは質問できない） |

## 実装パターン

### 基本: 単一サブエージェント
```yaml
delegate_task:
  goal: "Research the latest developments in agentic engineering"
  context: "Focus on Simon Willison's blog posts from 2025-2026"
  toolsets: ["terminal", "web"]
  max_iterations: 50
```

### 並列: バッチモード
```yaml
delegate_task:
  tasks:
    - goal: "Research tool A"
      toolsets: ["web"]
    - goal: "Research tool B"
      toolsets: ["web"]
    - goal: "Analyze codebase structure"
      toolsets: ["terminal", "file"]
  max_iterations: 50
```

### ACPモード: 外部エージェント連携
```yaml
delegate_task:
  goal: "Run Claude Code for deep analysis"
  acp_command: "claude --acp --stdio"
  acp_args: ["--acp", "--stdio", "--model", "claude-sonnet-4"]
```

## Hermesでの実装例

Hermesは`delegate_task`ツールを使用して、サブエージェントを**戦略的に**起動する:

```
1. メインエージェントがタスクを分析
2. 推論が必要か判断 → 必要ならdelegate_task
3. サブエージェントに自己完結な指示を渡す
4. 結果が返ってくるまで他の作業を継続
5. 結果を統合してユーザーに報告
```

### 具体例: Xアカウントのエンリッチメント
```
delegate_task:
  goal: "Research this person's X activity, blog, projects, and contributions"
  context: "Create an L3 thought analysis entity page. Match the depth of antirez-com.md or simon-willison.md."
  toolsets: ["terminal", "web", "file"]
  max_iterations: 50
```

## 注意点

### イテレーション制限
> "Sub-agents of delegate_task can hit iteration limits (around 50) when processing more than 5 entities, which can prevent file writing from completing."

- サブエージェントは**最大イテレーション数**を持つ
- 複雑なタスクでは制限に達する可能性がある
- 5つ以上のエンティティを処理する場合は**バッチ分割**が必要

### コンテキスト圧縮
サブエージェントは**独自のコンテキスト**を持つため:
- メインエージェントのメモリは共有されない
- 必要な情報は`context`フィールドで明示的に渡す
- 「この会話で話したあれ」は通用しない

### サブエージェントの要約はLossy（情報が損失する）

> *"Always have the main agent read relevant files itself. Sub-agent summaries are lossy; cross-attention in the main context window improves pairwise reasoning."*
> — Sankalp (Claude Code 2.0 Guide)

サブエージェントの戻り値（要約）には重要な詳細情報が欠落する。精度が求められる判断は**メインエージェントに直接ファイルを読ませる**。

**使い分け指針**:
| タスク | 推奨 | 理由 |
|--------|------|------|
| ファイルの内容を深く理解 | メインエージェント | クロスアテンションで正確な推論 |
| 独立した調査・リサーチ | サブエージェント | 並列実行で高速 |
| バグ発見・コードレビュー | サブエージェント（Codex等） | 別のモデル視点で発見力向上 |
| 複雑なリファクタリング | メインエージェント | 文脈理解が不可欠 |

### エラーハンドリング
- サブエージェントが失敗してもメインエージェントは継続できる
- 結果は配列で返ってくるので、部分的な成功も処理可能
- エラー情報は`context`として次のサブエージェントに渡せる

## 関連概念

- [[../agentic-engineering]] — 上位概念
- [[context-window-management]] — サブエージェントはコンテキスト問題を回避する手段
- [[cognitive-debt]] — サブエージェントの自己完結性は認知負債を減らす
- [[multi-agent-autonomy-scale]] — サブエージェントは自律性の中間レベル

## 参照

- [[simon-willison]] — 概念提唱者、Hermesでの実装者
- [Subagents guide](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)
- [Hermes delegate_task documentation](~/wiki/concepts/harness-engineering/)