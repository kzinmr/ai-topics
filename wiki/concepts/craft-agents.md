---
title: "Craft Agents"
type: concept
created: 2026-05-09
updated: 2026-05-27
status: L2
tags:
  - harness-engineering
  - ai-agents
  - mcp
  - open-source
  - claude-code
  - browser-agent
sources:
  - "[[raw/articles/2026-05-xx_craft_agents-interface]]"
related:
  - "[[concepts/agent-harness]]"
  - "[[concepts/mcp]]"
  - "[[concepts/claude-code]]"
  - "[[concepts/codex]]"
---

# Craft Agents

Craft Agents is an open-source **agent interface** that connects multiple AI models, MCP servers, APIs, and browsers into a single unified experience.

- **Source code**: [github.com/craft-ai-agents/craft-agents-oss](https://github.com/craft-ai-agents/craft-agents-oss)

## Features

### Multi-Model Support

| Provider | Connection Method |
|----------|-------------------|
| Anthropic Claude | Direct API key or Max subscription |
| OpenAI ChatGPT | Existing Plus subscription (via Codex) |
| OpenRouter | Connect to 400+ models via single endpoint |
| Ollama / LM Studio | Fully offline and private |
| Vercel AI Gateway | Compatible endpoint |

Built on Vercel AI SDK, supporting a wide range of providers including Anthropic, OpenAI, Google Gemini, xAI Grok, Mistral, DeepSeek, Meta Llama, Cohere, Groq, Together.ai, Fireworks, Cerebras, Perplexity, Amazon Bedrock, Azure OpenAI, Google Vertex, Alibaba Qwen, MiniMax, and more.

### Connectivity

- **MCP**: Paste existing MCP server configuration JSON. Full local MCP (stdio) support.
- **API**: Autonomously builds connection configuration from OpenAPI specs, endpoint URLs, screenshots, or any available information.
- **Built-in Browser**: Chromium-based. Page navigation, form input, button clicks, data extraction, screenshots.
- **Custom API / Internal Services**: Direct Postgres connection via jumpbox.

### Importing Claude Code Skills

Supports bulk import of existing Claude Code skills and MCP configurations. New skills can also be created using natural language.

### Key Integrations

Notion, Obsidian, Gmail, GitHub, GitLab, Figma, Dropbox, Google Drive, Airtable, Trello, Asana, Discord, Stripe, Zendesk, HubSpot, Sentry, Shopify, MongoDB, Redis, PostgreSQL, Supabase, Vercel, Google Cloud, Linear, Jira, Zoom

## Position as a Harness

Craft Agents is designed around "connecting with everything":
- Switchable between Claude Code, ChatGPT, OpenRouter, and Ollama
- Three connection modes: MCP, API, and Browser
- Full Chromium browser built-in (autonomous UI operation)

## References

- [Craft Agents](https://agents.craft.do)
- [Craft Agents GitHub](https://github.com/craft-ai-agents/craft-agents-oss)
