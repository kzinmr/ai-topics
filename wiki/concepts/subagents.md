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

## Claude Codeサブエージェント実装詳細 (2026-04)

### ビルトインサブエージェント: Explore と Plan
Claude Codeには一般的なケース用のサブエージェントが標準搭載:
- **Explore**: メインコンテキストを汚染せずにコードベースを検索。`grep`、`find`呼び出しを自身のウィンドウで実行し、関連する結果のみを返す
- **Plan**: ファイルを読み込み、アーキテクチャを理解し、ステップバイステップの実装計画を作成。中間的な`read`呼び出しはメインコンテキストに表示されない

### Context Forking (`CLAUDE_CODE_FORK_SUBAGENT=1`)
デフォルトではサブエージェントは空白のコンテキストで始まるが、100kトークン以上を費やしてコードベースの理解を構築した後、その理解をサブエージェントに継承させたい場合にforingが解決策:
- `export CLAUDE_CODE_FORK_SUBAGENT=1` で、すべてのサブエージェント起動時に親のフルコンテキストを継承
- `/fork` スラッシュコマンドでオンデマンドフォークも可能
- フォークされたサブエージェント:
  - フォーク時点の親のフル会話を継承
  - 親とプロンプトキャッシュプレフィックスを共有（子2-Nはインプットトークンが約10分の1のコスト）
  - 隔離実行でツール呼び出しが親を汚染しない
  - 最終要約のみを返す

### Context-Timeline フック
メインエージェントのコンテキストと並列実行するサブエージェントを追跡するのは困難。`context-timeline`フック（https://www.aitmpl.com/component/hook/monitoring/context-timeline）はセッション開始時からタイムラインを表示し、サブエージェントの起動・完了・結果返却をリアルタイムで追跡可能。

### サブエージェントの保存場所
スコープに応じて異なる場所に保存:
- `.claude/agents/` — バージョン管理にコミット、チームと共有
- `~/.claude/agents/` — 個人用、どこでも利用可能
同名のサブエージェントがある場合、優先度の高い場所が勝つ。

## Skills と Subagents の相互関係

@ankrgyl (2026-04-27) の実践的な知見:

Claude Codeでsubagentを起動してメインセッションのコンテキストを隔離していた。複雑なタスクが会話ウィンドウを汚染し、トークンを消費し、推論能力を低下させていた。subagentに重い処理をさせて要約を返すだけで解決した。

その後Skillsが登場し、コンテキスト・規約・パターン・ドメイン知識のライブラリを構築し、要請に応じてClaudeのタスクに注入し始めた。

> "Now both exist at the same time, and they can compose in both directions. A skill can spawn a subagent, and a subagent can use skills."

これはSkillsとSubagentsが双方向に合成可能であることを意味する:
- **Skill → Subagent**: スキル内からサブエージェントを起動してタスクを委譲
- **Subagent → Skill**: サブエージェントがスキルを利用してドメイン知識にアクセス

参考: [Skills can use subagents, Subagents can use skills](../raw/articles/2041185537172607014_skills-can-use-subagents_-subagents-can-use-skills.md)

## Claude Agent SDK — Hub-and-Spoke Orchestration (Exam Knowledge)

Claude Certified Architect 試験の Domain 1（27%）から。詳細: [[concepts/claude-certified-architect-domains]]

### Hub-and-Spoke アーキテクチャ

コーディネーターが Hub で、サブエージェントが Spoke。**全通信はコーディネーター経由**。サブエージェント同士が直接通信することはない。

### 隔離の原則（試験で最もよく問われる）

- サブエージェントはコーディネーターの会話履歴を**自動継承しない**
- サブエージェントは起動間で**メモリを共有しない**
- 必要な情報は**すべて明示的にプロンプトで渡す必要がある**
- これは試験受験者の **#1 誤解**。プロンプトに含めなければサブエージェントはその情報を知らない。

### Task ツール

コーディネーターからサブエージェントを生成するメカニズム。`allowedTools` に `"Task"` が必須。各サブエージェントは `AgentDefinition`（description, system prompt, tool restrictions）を持つ。**並列生成**: 単一レスポンスで複数の Task 呼び出しを発行し、複数サブエージェントを同時起動可能。

### fork_session

独立したブランチを作成。共有ベースラインからの分岐探索に使用（例: 同じコードベース分析から2つの異なるテスト戦略を比較）。

### 狭い分解の失敗（試験固有）

コーディネーターがタスクを不十分に分解した場合、その失敗は**コーディネーターの責任**であり、下流サブエージェントではない。試験は失敗をその発生源まで追跡する能力をテストする。

### 関連

- [[concepts/claude-certified-architect-domains]] — 全5ドメインの包括的知識
- [[concepts/claude-code-best-practices]] — CLAUDE.md設定パターン
- [[concepts/claude-agent-sdk-sre-patterns]] — Agent SDK + MCP SREパターン
