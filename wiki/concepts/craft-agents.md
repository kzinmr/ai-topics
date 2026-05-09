---
title: "Craft Agents"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [agent-harness, ai-agents, mcp, open-source, claude-code, browser-automation]
sources:
  - "[[raw/articles/2026-05-xx_craft_agents-interface]]"
related:
  - "[[concepts/agent-harness]]"
  - "[[concepts/mcp]]"
  - "[[concepts/claude-code]]"
  - "[[concepts/codex]]"
---

# Craft Agents

Craft Agentsは、オープンソースの**エージェントインターフェース**。複数のAIモデル・MCPサーバー・API・ブラウザを単一の統合された体験で扱える。

- **ソースコード**: [github.com/craft-ai-agents/craft-agents-oss](https://github.com/craft-ai-agents/craft-agents-oss)

## 特徴

### マルチモデル対応

| プロバイダー | 接続方法 |
|-------------|---------|
| Anthropic Claude | 直接APIキーまたはMaxサブスクリプション |
| OpenAI ChatGPT | 既存のPlusサブスクリプション（Codex経由） |
| OpenRouter | 400+モデルに単一エンドポイントで接続 |
| Ollama / LM Studio | 完全オフライン・プライベート |
| Vercel AI Gateway | 互換エンドポイント |

Vercel AI SDKベースで、Anthropic, OpenAI, Google Gemini, xAI Grok, Mistral, DeepSeek, Meta Llama, Cohere, Groq, Together.ai, Fireworks, Cerebras, Perplexity, Amazon Bedrock, Azure OpenAI, Google Vertex, Alibaba Qwen, MiniMax など広範なプロバイダーに対応。

### 接続性

- **MCP**: 既存のMCPサーバー設定JSONを貼り付けるだけ。ローカルMCP（stdio）も完全サポート
- **API**: OpenAPI spec、エンドポイントURL、スクリーンショットなど、どんな情報からでも接続設定を自律的に構築
- **ブラウザ内蔵**: Chromiumベース。ページ遷移、フォーム入力、ボタンクリック、データ抽出、スクリーンショット
- **カスタムAPI/内部サービス**: jumpbox越しのPostgres直結も可能

### Claude Codeスキルのインポート

既存のClaude CodeスキルとMCPを一度にインポート可能。新しいスキルも自然言語で作成できる。

### 主な統合先

Notion, Obsidian, Gmail, GitHub, GitLab, Figma, Dropbox, Google Drive, Airtable, Trello, Asana, Discord, Stripe, Zendesk, HubSpot, Sentry, Shopify, MongoDB, Redis, PostgreSQL, Supabase, Vercel, Google Cloud, Linear, Jira, Zoom

## ハーネスとしての位置づけ

Craft Agentsは「すべてと繋がる」ことを重視した設計で:
- Claude Code、ChatGPT、OpenRouter、Ollamaを切り替え可能
- MCP、API、ブラウザの3つの接続モード
- フルChromiumブラウザ内蔵（UI操作の自律化）

## 参照

- [Craft Agents](https://agents.craft.do)
- [Craft Agents GitHub](https://github.com/craft-ai-agents/craft-agents-oss)
