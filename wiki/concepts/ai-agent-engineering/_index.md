---
title: "AI Agent Engineering — System Architecture & Design"
aliases:
  - ai-agent-engineering-index
  - agent-system-design
  - agent-architecture-patterns
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - index
  - ai-agent-engineering
  - agent-architecture
status: draft
---

# AI Agent Engineering — システム構築アーキテクチャ

AI Agentを「構築する」ためのシステム設計・アーキテクチャパターンを整理したインデックス。

Anthropic Engineering ブログが主要出典。エージェントの内部構造、ツール設計、評価、コンテキスト管理などの技術的な側面をカバー。

## 関連概念

[[agentic-engineering]] — エージェントを「活用する」開発者のワークフロー（Simon Willison）
[[harness-engineering]] — エージェントを「制御・構造化する」環境設計（共通概念）

## コンセプト一覧

### 🏗️ エージェント設計パターン

| ページ | 概要 | 出典 |
|-------|------|------|
| [[building-effective-agents]] | ワークフロー vs エージェント、単純性から始める | Anthropic |
| [[multi-agent-research-system]] | Orchestrator-Worker、並列サブエージェント | Anthropic |
| [[advanced-tool-use]] | Tool Search Tool / PTC / Tool Use Examples | Anthropic |
| [[writing-tools-for-agents]] | ツール設計の5原則、評価駆動最適化 | Anthropic |
| [[code-execution-with-mcp]] | MCPをコードAPIとして公開（98.7%トークン削減） | Anthropic |

### 🧪 評価・ベンチマーク

| ページ | 概要 | 出典 |
|-------|------|------|
| [[evals-for-ai-agents]] | エージェント評価の基本原則 | Anthropic |
| [[infrastructure-noise]] | インフラ設定がベンチマークスコアに与える影響 | Anthropic |

### 🧠 コンテキスト・内部構造

| ページ | 概要 | 出典 |
|-------|------|------|
| [[context-engineering]] | LLMエージェントのコンテキスト管理・最適化 | Anthropic |
| [[harness-design-long-running-apps]] | GAN Inspired Generator-Evaluatorループ、コンテキストリセット | Anthropic |

## Agentic Engineering との違い

| 次元 | Agentic Engineering | AI Agent Engineering |
|------|-------------------|---------------------|
| 焦点 | 開発者のワークフロー | システムのアーキテクチャ |
| 主語 | 「人間がエージェントをどう使うか」 | 「エージェントをどう作るか」 |
| 代表例 | WillisonのRed/Green TDD、Cognitive Debt | AnthropicのBuilding Effective Agents |
| レイヤー | 応用・活用 | 基盤・設計 |

## 更新履歴

| 日付 | 変更内容 |
|------|---------|
| 2026-04-12 | 初期作成 — Anthropic Engineering記事群を再分類 |
