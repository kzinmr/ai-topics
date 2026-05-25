---
title: Centaur
created: 2026-05-25
updated: 2026-05-25
type: entity
tags: [entity, ai-agents, multi-agent, agent-runtime, open-source, security, infrastructure, platform, orchestration, slack, developer-tooling]
sources: [raw/articles/2026-05-21_paradigm-centaur-open-source.md, https://www.paradigm.xyz/2026/05/open-sourcing-centaur-multiplayer-self-hosted-secure-agents]
---

# Centaur

**Centaur** is an open-source (Apache 2.0), self-hosted, multiplayer AI agent runtime built by [[entities/paradigm|Paradigm]] and Tempo. Used in production since January 2026, it enables organizations to run collaborative AI agents that survive restarts, operate with real credentials securely, and integrate directly into Slack workflows.

## Philosophy

> "We think that organizations should be empowered to own their stack, move at the speed they need and use AI in collaborative not isolated settings."

Centaur addresses the key gaps in personal agent stacks: continuity, reachability, resilience, security, and observability.

## Architecture

```
Slackbot → API (FastAPI) ↔ Postgres (state)
                ↕
       Sandbox Containers ← Firewall (Iron Proxy) ← External APIs
                ↕
          Observability (JSON logs → user's stack)
```

- **Slackbot**: Thin Next.js webhook listener; tags API to spawn runtime
- **API**: FastAPI control plane; session lifecycle, auto-generated REST endpoints, durable workflow engine
- **Postgres**: Single source of truth for thread assignments, execution state, API keys, audit logs
- **Sandbox**: Isolated container per conversation (Linux, Node.js, Python, Rust pre-installed). Warm pool eliminates cold-start latency
- **Iron Proxy**: Firewall between sandbox and external world; agent NEVER holds raw API keys
- **Observability**: Structured JSON logs to stdout; ships with VictoriaLogs/VictoriaMetrics

## Security Model

Centaur's defining innovation is **credential isolation**:

1. Tool declares required hosts and secrets in `pyproject.toml`
2. Iron Proxy builds mapping on sandbox startup: `target host → secret key`
3. Agent requests intercepted by proxy, correct token injected in-flight
4. Agent sees only successful response — **never the raw secret**
5. Response bodies scanned for leaked secret values and redacted in real-time

Network policies prevent containers from accessing secrets service directly or the web without the firewall.

## Key Features

- **One Slack thread = one isolated agent session** with dedicated sandbox
- **Organization-wide tools and skills**: added once, available to all users
- **Durable execution**: agents survive restarts, deploys, disconnects
- **Tools as Python classes**: auto-discovered on startup, REST endpoints auto-generated, hot-reloaded
- **Out-of-the-box integrations**: spreadsheets, docs, slides, PDFs, Slack search, web search, GitHub, image generation, Google Workspace

## Adoption Pattern

1. Create company-wide `#ai-agent` Slack channel
2. Leaders use it first, leading by example
3. Empower everyone to ask questions without fear
4. AI-fluent people nudge others: "Here's how you could've used AI to get unblocked"

## Related

- Paradigm — creator
- [[concepts/agent-executor|Agent Executor]] — Google's distributed agent runtime
- [[concepts/agent-runtime|Agent Runtime]] — concept overview
- [[concepts/managed-agents|Managed Agents]] — Google's managed agents approach
- [[concepts/multi-agent|Multi-Agent Systems]]
