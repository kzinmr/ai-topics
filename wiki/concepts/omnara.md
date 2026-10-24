---
title: "Omnara (Open-Source Managed Agent Platform)"
type: concept
created: 2026-10-24
updated: 2026-10-24
tags:
  - ai-agents
  - agent-platform
  - open-source
  - developer-tools
  - infrastructure
aliases:
  - Omnara
  - omnara-ai/omnara
sources:
  - raw/articles/2026-10-22_omnara-github-readme.md
  - https://github.com/omnara-ai/omnara
related:
  - managed-agents
  - agent-deployment-engineering
  - self-hosting-ai-development
  - agent-skills
  - sandbox
confidence: medium
---

# Omnara (Open-Source Managed Agent Platform)

**Omnara** is an open-source (Apache 2.0) **managed agent platform** — a
self-hostable alternative to [[concepts/managed-agents|Claude Managed Agents]] and
OpenAI's Agents API. It reached HN Show HN on 2026-10-21 (112 points). The pitch:
run AI agents on **any model and any machine** via an API, with tools, secrets,
permissions, and streaming built in — free when self-hosted, or via Omnara Cloud.

It fills the gap explicitly flagged in the managed-agents community: frontier-lab
managed platforms are closed, model-locked, and store your agent history in *their*
database. Omnara replicates the same operating model under an open license.

## What it provides

### Build agents
- **Any model**: bring your own keys for OpenAI, Anthropic, OpenRouter, Amazon
  Bedrock, LiteLLM, Ollama, or any compatible endpoint — including self-hosted models.
- **Tools**: built-in shell, files, web search/fetch, and ask-a-human; plus
  [[concepts/mcp|MCP servers]] and custom tools running in your own systems.
- **Skills**: packaged instructions + files attached to any agent, loaded on demand
  (same paradigm as [[concepts/agent-skills|Agent Skills]]).
- **Memory stores**: files that persist between conversations, shareable across
  agents with per-agent read / read-write access.
- **Subagents**: an agent can spawn subagents with fresh context, inspect their
  progress, and send new instructions — each subagent is a full inspectable agent.

### Run them anywhere
- **Machines**: install the Omnara daemon on any macOS/Linux laptop, VM, or container
  — agents run commands and edit files there with **no inbound ports or SSH keys**.
  Alternatively use sandboxes from eleven providers (Daytona, E2B, Modal, Freestyle,
  Unikraft, …) — see [[comparisons/agent-sandboxing]]. Agents can use several
  machines at once and move between them; if a laptop drops, the agent continues in
  a sandbox and syncs work back with git.
- **Durable state**: every step persisted — agents resume after crashes, restarts,
  and machine disconnects.
- **Schedules**: timezone-aware cron triggers that message an existing agent, launch
  one from a profile, or start a Slack/Discord thread.

### Connect & control
- Slack/Discord/GitHub integrations (mention the bot → agent in a thread; PR-triggered
  review agents), streaming events + webhooks, per-tool **permissions**
  (run immediately / ask a human / block, enforced by the platform).
- REST API (OpenAPI), TypeScript SDK (`@omnara/sdk`), CLI, and an MCP server.
- RBAC + secrets management, multi-tenant deployments, and — for self-hosters —
  **agent history lives in your own Postgres**, queryable for analytics, evals, and
  training datasets.

## Positioning (vs. hosted alternatives)

| | Omnara | Claude Managed Agents | OpenAI Agents API |
| --- | --- | --- | --- |
| Source | Open source (Apache 2.0) | Closed | Open harness (Codex); hosted service is OpenAI's |
| Models | Any compatible | Claude | OpenAI |
| Where agents run | 11 sandbox providers or your own machines | Anthropic sandboxes | OpenAI/partner sandboxes |
| Agent history | Your own Postgres (self-hosted) | Anthropic's DB | OpenAI's DB |
| Pricing | Free self-host; bring-your-own-keys cloud | Token rates + $0.08/session-hour | Model + tool rates |

The README's own guidance: pick the hosted services if you live on one vendor's
models; pick Omnara to choose your own models and machines, run the platform
yourself, or keep agent data in your own database.

**Fit vs other layers** (from the README): workflow builders (n8n/Zapier) get
open-ended stateful agents; agent frameworks (LangChain, Mastra, Agents SDK) get
hosting/state/machines/permissions without redeploys; coding-agent harnesses
(Claude Code, Codex, OpenCode, Pi) get cloud agents running as a service across
machines and users — see [[concepts/agent-deployment-engineering]] and
[[concepts/self-hosting-ai-development]].

## Significance

1. **Managed agents as an open commodity**: the "brain/hands separation" hosting
   model pioneered by Anthropic is now reimplemented in Apache 2.0 with
   provider-agnostic execution — evidence the managed-agent layer is commoditizing.
2. **Your-agent-history-as-data-asset**: self-hosted Postgres history (queryable for
   evals/training data) directly counters the hosted services' data-retention
   limitations — a practical answer to the frontier-lab lock-in risk documented on
   [[concepts/managed-agents]].
3. **No-inbound-port machine mesh**: the daemon model turns ordinary laptops/GPU
   servers into agent-executable machines without SSH exposure — a lighter-weight
   execution fabric than per-session sandboxes.

## See Also

- [[concepts/managed-agents]] — the Anthropic hosted service Omnara clones
- [[concepts/agent-deployment-engineering]] — deploying agents as services
- [[concepts/self-hosting-ai-development]] — self-hosting AI tooling motivation
- [[comparisons/agent-sandboxing]] — sandbox provider landscape
- [[concepts/agent-skills]] — the skills packaging paradigm Omnara adopts
