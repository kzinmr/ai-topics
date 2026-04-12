---
title: "Agentic Engineering — Developer Workflows & Patterns"
aliases:
  - agentic-engineering
  - agentic-engineering-index
  - agentic-coding-patterns
  - developer-agentic-workflows
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - methodology
  - index
  - agentic-engineering
status: draft
---

# Agentic Engineering — 開発者ワークフロー

AI Agentを「活用してソフトウェアを開発する」実践的ワークフローとパターンを整理したインデックス。

## 関連概念

[[ai-agent-engineering]] — エージェントを「構築する」システム設計・アーキテクチャ（Anthropic Engineering）
[[harness-engineering]] — エージェントを「制御・構造化する」環境設計（横断概念→タグ管理）

## リーダー別主要コンセプト

| リーダー | コアコンセプト | 関連ページ |
|---------|--------------|-----------|
| [[simon-willison]] | Agentic Engineering Patterns, Red/Green TDD, Cognitive Debt | 以下のWillisonパターン群 |
| [[andrew-karpathy]] | Software 2.0, RLによるエージェント学習, データ中心AI | [[karpathy-rl-agents]] |
| [[sankalp]] | Claude Code 2.0実用ガイド、サブエージェントのlossiness、Throw-Away Draft、コンテキスト60%ルール | 以下のSankalpパターン群 |
| [[steipete]] | Agent-First Design, CLI-First Development, Plan Mode不要論, inference-speed bottleneck | 以下のSteipeteパターン群 |

## Simon Willisonの開発パターン

### 🧪 テスト駆動開発

| ページ | 概要 |
|-------|------|
| [[first-run-the-tests]] | エージェントにコードを変更させる前に、まずテストを実行させる |
| [[red-green-tdd]] | エージェントがテストを書いてから実装するRed/Green TDDサイクル |
| [[agentic-manual-testing]] | エージェントによる手動テストの自動化 |

### 📝 ドキュメンテーション & 成果物

| ページ | 概要 |
|-------|------|
| [[linear-walkthroughs]] | Linearチケットの解説生成 |
| [[showboat]] | エージェントの作業内容を可視化するドキュメンテーションツール |
| [[interactive-explanations]] | 対話的アニメーションでアルゴリズムを説明させる |
| [[vibe-coding]] | テスト不要の「感覚で書く」アプローチとその限界 |

### 🔧 ツール統合

| ページ | 概要 |
|-------|------|
| [[using-git-with-agents]] | Gitワークフローへのエージェント統合 |
| [[how-agents-work]] | コーディングエージェントの内部仕組みの概念モデル |

### 🧠 認知と品質

| ページ | 概要 |
|-------|------|
| [[cognitive-debt]] | エージェント生成コードを理解せずにマージすると蓄積する「認知負債」 |
| [[harness-engineering]] | OpenAI Symphony、エージェント協調制御（[[ryan-lopopolo]]） |

### 🏗️ Sankalpの実用パターン

| ページ | 概要 |
|-------|------|
| [[context-window-management]] | コンテキスト60%ルール、圧縮戦略 |
| [[throw-away-draft-pattern]] | 捨て台本→比較→反復の開発サイクル |
| [[subagents]] | サブエージェントのlossiness、使い分け指針 |

### 🚀 Steipeteの推論速度開発

| ページ | 概要 |
|-------|------|
| [[agent-first-design]] | 「人間向け」ではなく「エージェント向け」コード設計 |
| [[cli-first-development]] | CLIから始めてフィードバックループを高速化 |
| [[how-agents-work]] | Plan Mode不要論、会話的計画、Task Toolアーキテクチャ |

## Agentic Engineering vs AI Agent Engineering

| 次元 | Agentic Engineering | AI Agent Engineering |
|------|-------------------|---------------------|
| 焦点 | 開発者のワークフロー | システムのアーキテクチャ |
| 主語 | 「人間がエージェントをどう使うか」 | 「エージェントをどう作るか」 |
| 代表例 | WillisonのRed/Green TDD、Cognitive Debt | AnthropicのBuilding Effective Agents |
| レイヤー | 応用・活用 | 基盤・設計 |

## 関連概念マップ

```
Agentic Engineering
├── 🧪 Willisonのテストパターン
│   ├── First Run the Tests
│   ├── Red/Green TDD
│   └── Agentic Manual Testing
├── 📝 ドキュメンテーション
│   ├── Linear Walkthroughs
│   ├── Showboat
│   └── Interactive Explanations
├── 🔧 ツール統合
│   ├── Using Git with Agents
│   ├── How Coding Agents Work
│   └── Vibe Coding
├── 🧠 認知と品質
│   ├── Cognitive Debt
│   └── Harness Engineering (Lopopolo)
└── 🤖 KarpathyのRLエージェント
    └── Software 2.0 / Autoresearch Loop
```

## 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-12 | Anthropic系概念をai-agent-engineering/へ分離 |
| 2026-04-12 | Willison開発パターン中心に再構築 |
