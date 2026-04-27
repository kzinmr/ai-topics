---
title: "Subagents — Parallel AI Agent Delegation"
type: concept
aliases:
  - subagents
  - sub-agent
  - multi-agent-delegation
tags:
  - concept
  - agentic-engineering
  - multi-agent
  - orchestration
status: complete
description: "メインエージェントが独立したサブエージェントを並列に起動し、タスクを委譲するパターン。"
created: 2026-04-12
updated: 2026-04-24
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/"
related:
  - "[[concepts/harness-engineering/agentic-workflows/subagents]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/cognitive-debt]]"
  - "[[concepts/multi-agent-consensus-patterns]]"
  - "[[concepts/harness-engineering]]"
---

# Subagents

メインのAIエージェントが**独立したサブエージェントを並列に起動**し、それぞれが隔離されたコンテキストとターミナルセッションでタスクを実行するパターン。

## 3つの設計原則

1. **独立性** — サブエージェントはメインの会話コンテキストを共有しない。指示は完全に自己完結である必要がある。
2. **並列性** — 複数の独立タスクを同時実行（バッチモード）。待ち時間を大幅に短縮。
3. **自己完結性** — 必要なファイルパス、エラーメッセージ、制約条件を`context`フィールドで明示的に渡す。

## 使い分け

| ✅ 向いている | ❌ 向いていない |
|-------------|---------------|
| 推論重視のサブタスク（デバッグ、コードレビュー、リサーチ） | 推論不要の単純作業（`execute_code`で十分） |
| コンテキストが溢れる大規模データ処理 | 単一のツール呼び出し |
| 並列独立ワークストリーム | ユーザーとの対話が必要なタスク |

## 重要な制約

- **Lossy Summary Problem**: サブエージェントの戻り値（要約）には詳細情報が欠落する。精度が求められる判断はメインエージェントに直接ファイルを読ませる。
- **イテレーション制限**: サブエージェントは最大イテレーション数（~50）を持つ。複雑なタスクでは制限に達する可能性がある。
- **コンテキスト非共有**: メインエージェントのメモリは自動的に共有されない。

## 実装パターン (Hermes)

```yaml
delegate_task:
  goal: "Research the latest developments in agentic engineering"
  context: "Focus on Simon Willison's blog posts from 2025-2026"
  toolsets: ["terminal", "web"]
  max_iterations: 50
```

詳細: [[concepts/harness-engineering/agentic-workflows/subagents]]

## 関連概念

- [[concepts/harness-engineering/agentic-workflows/subagents]] — 詳細実装ガイド
- [[concepts/agentic-engineering]] — 上位概念
- [[concepts/cognitive-debt]] — サブエージェントの自己完結性は認知負債を減らす
- [[concepts/harness-engineering]] — 環境設計哲学としての位置付け

## Skills と Subagents の相互関係

@ankrgyl (2026-04-27) の実践的な知見:

Claude Codeでsubagentを起動してメインセッションのコンテキストを隔離していた。複雑なタスクが会話ウィンドウを汚染し、トークンを消費し、推論能力を低下させていた。subagentに重い処理をさせて要約を返すだけで解決した。

その後Skillsが登場し、コンテキスト・規約・パターン・ドメイン知識のライブラリを構築し、要請に応じてClaudeのタスクに注入し始めた。

> "Now both exist at the same time, and they can compose in both directions. A skill can spawn a subagent, and a subagent can use skills."

これはSkillsとSubagentsが双方向に合成可能であることを意味する:
- **Skill → Subagent**: スキル内からサブエージェントを起動してタスクを委譲
- **Subagent → Skill**: サブエージェントがスキルを利用してドメイン知識にアクセス

参考: [Skills can use subagents, Subagents can use skills](../raw/articles/2041185537172607014_skills-can-use-subagents_-subagents-can-use-skills.md)
