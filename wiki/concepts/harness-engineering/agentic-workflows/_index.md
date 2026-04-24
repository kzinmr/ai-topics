---
title: "Agentic Workflows — Harness Engineering配下の開発者ワークフロー"
type: concept
aliases:
  - agentic-workflows
  - agentic-coding-patterns
  - developer-agentic-workflows
created: 2026-04-12
updated: 2026-04-19
tags:
  - concept
  - methodology
  - index
  - harness-engineering
  - agentic-workflows
status: active
parent: harness-engineering
sources: []
---

# Agentic Workflows — 開発者ワークフロー

AI Agentを「活用してソフトウェアを開発する」実践的ワークフローとパターン。**Harness Engineeringのサブセクション**として位置づけられる。

## Harness Engineering内での位置づけ

| レイヤー | 概念 | 焦点 |
|---------|------|------|
| **最上位** | [[_index\|Harness Engineering]] | Agent = Model + Harness（環境設計哲学） |
| **横断技術** | [[context-engineering\|Context Engineering]] | コンテキストの選択・圧縮・配置（有限リソース管理） |
| **応用（人間側）** | **Agentic Workflows**（本ページ） | 開発者がエージェントを「活用する」パターン |
| **応用（システム側）** | [[system-architecture/_index\|System Architecture]] | エージェントを「構築する」パターン |

## リーダー別主要コンセプト

| リーダー | コアコンセプト | 関連ページ |
|---------|--------------|-----------|
| [[simon-willison]] | Agentic Engineering Patterns, Red/Green TDD, Cognitive Debt | 以下のWillisonパターン群 |
| [[andrej-karpathy]] | Software 2.0, RLによるエージェント学習, データ中心AI | [[karpathy-rl-agents]] |
| [[entities/sankalp-sinha.md]] | Claude Code 2.0実用ガイド、サブエージェントのlossiness、Throw-Away Draft、コンテキスト60%ルール | 以下のSankalpパターン群 |
|  | Agent-First Design, CLI-First Development, Plan Mode不要論, inference-speed bottleneck | 以下のSteipeteパターン群 |

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
| [[compound-engineering-loop]] | 反復的品質向上ループ |
| [[code-hoarding]] | 重要な知識をエージェントのコンテキスト外に保持するパターン |

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
| [[concepts/harness-engineering/agentic-workflows/prompt-driven-development.md]] | プロンプト駆動開発パターン |

## Agentic Workflows vs System Architecture

| 次元 | Agentic Workflows | System Architecture |
|------|-------------------|---------------------|
| 焦点 | 開発者のワークフロー | システムのアーキテクチャ |
| 主語 | 「人間がエージェントをどう使うか」 | 「エージェントをどう作るか」 |
| 代表例 | WillisonのRed/Green TDD、Cognitive Debt | AnthropicのBuilding Effective Agents |
| レイヤー | 応用・活用 | 基盤・設計 |

## 関連概念マップ

```
Agentic Workflows (Harness Engineering)
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
│   ├── Compound Engineering Loop
│   └── Code Hoarding
└── 🤖 KarpathyのRLエージェント
    └── Software 2.0 / Autoresearch Loop
```

## 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-12 | 初期作成 — Willison開発パターン中心に構築 |
| 2026-04-19 | Harness umbrella再編成: タイトル更新、System Architectureとの位置づけ表追加、重複エントリ整理 |
