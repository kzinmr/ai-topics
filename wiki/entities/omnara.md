---
title: "Omnara"
type: entity
created: 2026-10-24
updated: 2026-10-24
tags:
  - ai-agents
  - agent-platform
  - open-source
  - company
aliases:
  - Omnara AI
  - omnara-ai
sources:
  - raw/articles/2026-10-22_omnara-github-readme.md
  - https://github.com/omnara-ai/omnara
  - https://www.omnara.com
related:
  - omnara
  - managed-agents
  - agent-deployment-engineering
confidence: medium
---

# Omnara

**Omnara** is the company behind [[concepts/omnara|Omnara]], the open-source
(Apache 2.0) managed agent platform — a self-hostable alternative to
[[concepts/managed-agents|Claude Managed Agents]] and OpenAI's Agents API. The
project hit Hacker News Show HN on 2026-10-21 (112 points).

## Product

- **Omnara Cloud** — hosted platform, free with bring-your-own keys and machines,
  or pay-as-you-go for Omnara's models and sandboxes.
- **Self-hosted** — full Apache 2.0 platform on your own infrastructure with agent
  history in your own Postgres.
- Distribution: REST API + `@omnara/sdk` (TypeScript) + `omnara` CLI + MCP server.

## Positioning

Sits between agent frameworks (LangChain, Mastra, OpenAI Agents SDK) and hosted
managed-agent services: frameworks provide agent logic in your app code; Omnara
provides the hosting, state, machines, permissions, and integrations layer — with
agents created and modified via API instead of redeploys.

## See Also

- [[concepts/omnara]] — the platform itself (architecture, features, comparison table)
- [[concepts/managed-agents]] — the Anthropic service it clones openly
- [[concepts/agent-deployment-engineering]] — deployment layer context
