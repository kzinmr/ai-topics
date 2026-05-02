---
title: "System Architecture — Harness Engineering配下のシステム設計"
type: concept
aliases:
  - system-architecture
  - agent-system-design
  - agent-architecture-patterns
created: 2026-04-12
updated: 2026-04-19
tags:
  - concept
  - index
  - harness-engineering
  - architecture
status: active
parent: harness-engineering
sources: []
---

# System Architecture — Harness Engineering配下のシステム設計

AI Agentを「構築する」ためのシステム設計・アーキテクチャパターン。**Harness Engineeringのサブセクション**として位置づけられる。

Anthropic EngineeringブログとOpenAI Cookbookが主要出典。エージェントの内部構造、ツール設計、評価、コンテキスト管理などの技術的な側面をカバー。

## Harness Engineering内での位置づけ

| レイヤー | 概念 | 焦点 |
|---------|------|------|
| **最上位** | [[concepts/_index|Harness Engineering]] | Agent = Model + Harness（環境設計哲学） |
| **横断技術** | [[concepts/context-engineering]] | コンテキストの選択・圧縮・配置（有限リソース管理） |
| **応用（人間側）** | [[concepts/agentic-engineering]] | 開発者がエージェントを「活用する」パターン |
| **応用（システム側）** | **System Architecture**（本ページ） | エージェントを「構築する」パターン |

## コンセプト一覧

### 🏗️ エージェント設計パターン

| ページ | 概要 | 出典 |
|-------|------|------|
| [[concepts/building-effective-agents]] | ワークフロー vs エージェント、単純性から始める | Anthropic |
| [[concepts/multi-agent-research-system]] | Orchestrator-Worker、並列サブエージェント | Anthropic |
| [[concepts/harness-engineering/system-architecture/advanced-tool-use]] | Tool Search Tool / PTC / Tool Use Examples | Anthropic |
| [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] | ツール設計の5原則、評価駆動最適化 | Anthropic |
| [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] | MCPをコードAPIとして公開（98.7%トークン削減） | Anthropic |

### 🔄 エージェント実行基盤（OpenAI Responses API）

| ページ | 概要 | 出典 |
|-------|------|------|
| [[concepts/agent-loop-orchestration]] | モデル提案→シェル実行→結果フィードバックの自律ループ | OpenAI |
| [[concepts/harness-engineering/system-architecture/context-compaction]] | 長期実行エージェントのコンテキスト圧縮メカニズム | OpenAI |
| [[concepts/harness-engineering/system-architecture/container-context]] | ホスト型コンテナによる永続的なエージェント作業スペース | OpenAI |
| [[concepts/agent-skills]] | SKILL.md バンドルによる再利用可能なワークフローパターン | OpenAI |

### 🛡️ セキュリティ・制御

| ページ | 概要 | 出典 |
|-------|------|------|
| [[concepts/harness-engineering/system-architecture/agent-security-patterns]] | エグレスプロキシ、ドメインスコープシークレットインジェクション | OpenAI |
| [[concepts/evals-for-ai-agents]] | エージェント評価の基本原則 | Anthropic |
| [[concepts/infrastructure-noise]] | インフラ設定がベンチマークスコアに与える影響 | Anthropic |

### 🧠 コンテキスト・内部構造

| ページ | 概要 | 出典 |
|-------|------|------|
| [[concepts/harness-design-long-running-apps]] | GAN Inspired Generator-Evaluatorループ、コンテキストリセット | Anthropic |
| [[concepts/harness-engineering/system-architecture/effective-harnesses-for-long-running-agents]] | 長期実行エージェントのハーネス設計 | Anthropic |
| [[concepts/claude-code-best-practices]] | Claude Code実践的ベストプラクティス | Sankalp + Anthropic |

## Agentic Workflowsとの違い

| 次元 | Agentic Workflows | System Architecture |
|------|-------------------|---------------------|
| 焦点 | 開発者のワークフロー | システムのアーキテクチャ |
| 主語 | 「人間がエージェントをどう使うか」 | 「エージェントをどう作るか」 |
| 代表例 | WillisonのRed/Green TDD、Cognitive Debt | AnthropicのBuilding Effective Agents |
| レイヤー | 応用・活用 | 基盤・設計 |

## 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-12 | 初期作成 — Anthropic Engineering記事群を再分類 |
| 2026-04-19 | Harness umbrella再編成: タイトル更新、重複エントリ削除、位置づけ表追加 |
