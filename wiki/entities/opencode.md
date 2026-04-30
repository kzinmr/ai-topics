---
title: OpenCode
created: 2026-04-30
updated: 2026-04-30
type: entity
tags: [product, coding-agents, open-source, framework]
sources: [raw/articles/2026-04-30_ramp-inspect-background-agent.md]
---

# OpenCode

## Overview

**OpenCode** is an open-source AI coding agent framework used by [[entities/ramp]] as the foundation for their **Inspect** background coding agent. Key characteristics that made it attractive for Ramp's use case:

1. **Server-first architecture** — designed for cloud deployment, not local IDE use
2. **Typed SDK** — enables robust tool integration and type-safe agent interactions
3. **Open-source** — agents can read their own source code to understand capabilities (self-documenting)

## Why Ramp Chose OpenCode

Ramp's selection criteria:
- Must run in cloud sandbox environments (not local)
- Must have a clean, typed API for custom tool integration
- Must be open-source so the agent can introspect its own capabilities
- Must support headless operation (no GUI requirement)

## Architecture Role

OpenCode sits between:
- **Modal Sandboxes** (infrastructure layer)
- **Cloudflare Durable Objects** (state management)
- **Custom Tools** (Ramp-specific integrations: Postgres, Sentry, Datadog, etc.)

## Relationship to Other Agent Frameworks

| Framework | Primary Target | Architecture | Open Source |
|-----------|---------------|--------------|-------------|
| OpenCode | Cloud/Server | Server-first, typed SDK | Yes |
| Claude Agent SDK | API integration | Python SDK | Yes |
| LangGraph | Orchestration | Graph-based | Yes |
| Devin/Cognition | Full IDE | Proprietary | No |

## Related Entities

- [[entities/ramp]] — Uses OpenCode for Inspect
- [[entities/inspect]] — Ramp's background agent built on OpenCode
- [[concepts/modal-sandboxes]] — Execution layer for OpenCode
- [[concepts/background-coding-agent]] — Architectural pattern

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
- https://opencode.ai/
