---
title: "OpenAI Agents API"
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [openai, api, ai-agents, agent-harness, durable-execution]
sources:
  - https://developers.openai.com/api/docs/guides/agents-api/overview
  - https://developers.openai.com/api/docs/changelog
  - raw/articles/simonwillison.net--2026-sep-29-openai-devday-2026-live-blog--e0ba6a4a.md
  - https://developers.openai.com/cookbook/examples/agents_sdk/migrate-from-claude-agent-sdk/readme
  - https://developers.openai.com/api/docs
---

# OpenAI Agents API

## Definition

The Agents API exposes a managed Codex harness. OpenAI owns session orchestration, compaction, and recovery; applications supply tools and choose an execution environment. Its core objects are agent, environment, durable session, and events/items. The official overview documents sandbox code/file work, MCP, steering, subagents, and session continuation. [Overview](https://developers.openai.com/api/docs/guides/agents-api/overview), checked 2026-10-07.

## Release history

- **2026-09-10:** public beta in the official changelog.
- **2026-09-29:** Computer Use added; the saved [[events/openai-devday-2026]] live blog reports it at 10:31.
- **2026-10-07:** current overview supports OpenAI-hosted and self-hosted execution surfaces. Self-hosted compute does not imply self-hosted orchestration or offline inference.

## Roles and ownership

| Surface | Main responsibility | Harness ownership |
|---|---|---|
| [[concepts/openai/responses-api]] | Direct model requests, outputs and tool interactions | Application chooses workflow orchestration |
| [[concepts/openai/agents-sdk]] | Open-source code framework for tools, handoffs, approvals and tracing | Trusted application runtime |
| Agents API | Managed Codex sessions and execution coordination | OpenAI-managed harness; compute is a separate choice |
| [[concepts/openai/decisions-api]] | Typed bounded judgments | Application consumes the answer and decides what to execute |

This is a responsibility comparison, not a claim that the SDK is required to call Agents API or that Responses cannot support sophisticated agents. [Official build paths](https://developers.openai.com/api/docs) and [SDK architecture](https://developers.openai.com/cookbook/examples/agents_sdk/migrate-from-claude-agent-sdk/readme).

## Engineering implications and open questions

Design interpretation: managed sessions reduce application harness work, while business authorization, tool contracts and side-effect handling still need explicit design. Durable session continuation is not proof of exactly-once external writes.

The sources checked here do not establish recovery guarantees for every tool, session retention limits, customer-specific access, or every regional/security configuration. Consult the dedicated architecture, sandbox security and API reference before committing to deployment requirements. Newsletter descriptions alone do not verify these details.

## Sources

- [Official overview](https://developers.openai.com/api/docs/guides/agents-api/overview).
- [Official changelog](https://developers.openai.com/api/docs/changelog).
- [Saved DevDay live blog](../../raw/articles/simonwillison.net--2026-sep-29-openai-devday-2026-live-blog--e0ba6a4a.md).
- [SDK architecture](https://developers.openai.com/cookbook/examples/agents_sdk/migrate-from-claude-agent-sdk/readme).
