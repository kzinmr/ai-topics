---
title: "AI Agent Engineering — System Architecture & Design"
aliases:
  - ai-agent-engineering
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
[[harness-engineering]] — エージェントを「制御・構造化する」環境設計（横断概念→タグ管理）

## コンセプト一覧

### 🏗️ エージェント設計パターン

| ページ | 概要 | 出典 |
|-------|------|------|
| [[building-effective-agents]] | ワークフロー vs エージェント、単純性から始める | Anthropic |
| [[multi-agent-research-system]] | Orchestrator-Worker、並列サブエージェント | Anthropic |
| [[advanced-tool-use]] | Tool Search Tool / PTC / Tool Use Examples | Anthropic |
| [[writing-tools-for-agents]] | ツール設計の5原則、評価駆動最適化 | Anthropic |
| [[code-execution-with-mcp]] | MCPをコードAPIとして公開（98.7%トークン削減） | Anthropic |

### 🔄 エージェント実行基盤（OpenAI Responses API）

| ページ | 概要 | 出典 |
|-------|------|------|
| [[agent-loop-orchestration]] | モデル提案→シェル実行→結果フィードバックの自律ループ | OpenAI |
| [[context-compaction]] | 長期実行エージェントのコンテキスト圧縮メカニズム | OpenAI |
| [[container-context]] | ホスト型コンテナによる永続的なエージェント作業スペース | OpenAI |
| [[agent-skills]] | SKILL.md バンドルによる再利用可能なワークフローパターン | OpenAI |

### 🛡️ セキュリティ・制御

| ページ | 概要 | 出典 |
|-------|------|------|
| [[agent-security-patterns]] | エグレスプロキシ、ドメインスコープシークレットインジェクション | OpenAI |
| [[evals-for-ai-agents]] | エージェント評価の基本原則 | Anthropic |
| [[infrastructure-noise]] | インフラ設定がベンチマークスコアに与える影響 | Anthropic |

### 🧠 コンテキスト・内部構造

| ページ | 概要 | 出典 |
|-------|------|------|
| [[context-engineering]] | LLMエージェントのコンテキスト管理・最適化 | Anthropic |
| [[harness-design-long-running-apps]] | GAN Inspired Generator-Evaluatorループ、コンテキストリセット | Anthropic |
| [[context-window-management]] | コンテキストウィンドウの戦略的管理（圧縮、構造化、優先順位付け） | Simon Willison |
| [[context-anxiety]] | Claude Sonnet 4.5のコンテキスト不安現象、Anthropicの6操作ファイルメモリ、Cognitionの戦略 | Shlok Khemani |
| [[ai-memory-systems]] | AIメモリシステムの設計哲学比較（ChatGPT明示的 vs Claude暗黙的 vs Cognitionハイブリッド）、Bitter Lesson観点 | Shlok Khemani |
| [[anthropic-memory-tool-cognition]] | Anthropic Memory Tool (view/create/str_replace/insert/delete/rename)とCognitionの戦略的追随、「盗む」vs「独自開発」 | Shlok Khemani |

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
