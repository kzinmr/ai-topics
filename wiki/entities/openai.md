---
title: "OpenAI"
created: 2026-04-16
updated: 2026-04-16
tags: [llm, ai-agents, company, product]
aliases: ["OpenAI, Inc."]
---

# OpenAI

## Overview

OpenAIはAI研究・開発企業。GPTシリーズ、ChatGPT、Codex、DALL·Eなどの製品で知られる。2026年4月、**Agents SDK v0.14.0** をリリースし、サンドボックス実行機能、ハーネス/コンピューティング分離アーキテクチャ、マルチクラウドストレージ対応を発表。

## Key People
- [[entities/sam-altman|Sam Altman]] — CEO
- [[entities/greg-brockman|Greg Brockman]] — Co-founder & President
- [[entities/ilya-sutskever|Ilya Sutskever]] — Co-founder & former Chief Scientist (2023年離脱、SSI設立)

## Products & Services
- **GPT Series** — 大規模言語モデル (gpt-5.4等)
- **ChatGPT** — 800M+ weekly users
- **Codex** — コーディングエージェント
- **Agents SDK** — Pythonベースのエージェント開発フレームワーク (2026年4月 v0.14.0 GA)
- **Symphony** — マルチエージェントオーケストレーションプラットフォーム

## Agents SDK (v0.14.0) — 2026-04-15

### Core Features
- **Sandbox Execution:** ネイティブサンドボックス実行 — 安全なファイルI/O、コマンド実行、依存関係インストール
- **Harness vs Compute Separation:** オーケストレーションと実行を分離し、セキュリティ・耐久性・スケーラビリティを確保
- **Manifest Abstraction:** ワークスペースポータビリティ — AWS S3、GCS、Azure Blob、Cloudflare R2対応
- **Provider Ecosystem:** Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop、Vercelとビルトイン互換性
- **Standardized Integrations:** MCP、Skills、AGENTS.md、Shell、Apply Patchツール

### Architecture
- `SandboxAgent` — エージェント定義＋サンドボックスデフォルト
- `Manifest` — セッション初期ワークスペース契約（パスはワークスペース相対のみ、`..`エスケープ禁止）
- `Capabilities` — Filesystem、Shell、Compaction（デフォルト）、Skills、Memory（カスタム）
- `SandboxRunConfig` — 実行セッションのソース/オプション
- **Session Resolution:** ライブセッション再利用 → RunStateレジューム → session_stateレジューム → 新規セッション

### Pricing & Availability
- **GA** via API, Python SDK (TypeScript planned)
- 標準API価格（トークン + ツール使用ベース）
- 今後の機能: コードモード、サブエージェント、サンドボックス統合拡大

### Customer Validation
- Oscar Healthが臨床記録ワークフロー自動化で採用 — 「従来アプローチでは信頼性が不十分だったが、Agents SDKによりプロダクションレベルで可能に」

## Connections
- [[concepts/harness-engineering]] — OpenAI Symphonyのハーネスエンジニアリング哲学
- [[concepts/agent-skills]] — SKILL.mdバンドル、プログレッシブディスクロージャー
- [[entities/anthropic]] — 競合（Claude、Computer Use、Managed Agents）
- [[entities/cognition]] — 競合（Devin、Cloud Agent）
- [[concepts/sandbox-agents]] — OpenAIサンドボックス実行の詳細仕様

## Sources
- [[raw/articles/openai-agents-sdk-next-evolution-2026-04.md]]
- [[raw/articles/openai-sandbox-agents-api-guide-2026-04.md]]
- [OpenAI Agents SDK Blog](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [OpenAI API Sandbox Docs](https://developers.openai.com/api/docs/guides/agents/sandboxes)
