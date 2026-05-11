---
title: Agentic Identity — Modeling AI Agents as Financial Actors
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - ai-agents
  - security
  - governance
  - company
  - safety
sources: []
---

# Agentic Identity — Modeling AI Agents as Financial Actors

Agentic Identity is the practice of modeling AI agents as distinct actors within an organization's permission and identity systems — capable of transacting, authoring, and executing actions while maintaining audit trails and human accountability.

## Ramp's OBOU Model (April 2026)

Ramp's engineering team published a production implementation of agentic identity called **OBOU (On Behalf Of User)**, designed for their "Ramp for Agents" platform where AI agents can manage cards, bills, expenses, and approvals.

### Core Design Principles

1. **No API keys for agents** — Agent keys do NOT become authentication material; they extend the sponsor user's existing role
2. **Every action has a human accountable** — OBOU ties every agent action to a human sponsor for compliance
3. **RBAC extension** — Agent's access stems purely from the sponsor user's existing role and capabilities
4. **Reuses existing systems** — Auditing, permissioning, and compliance systems extend trivially

### OBOU vs Standalone Agents (SA)

| Dimension | OBOU | Standalone Agent |
|-----------|------|-----------------|
| Identity source | Sponsor user's role | Independent entity |
| Accountability | Human-backed | Agent-level |
| Compliance | Existing models work | New models needed |
| Implementation | Quick extension | Full new system |
| Use cases | Most current demand (coding agents, scripts) | Future autonomous businesses |

## Significance

As AI agents move from generating text to managing money and shipping code, the identity layer becomes critical. Ramp's OBOU is the first production framework showing how enterprise-grade agent identity can work without breaking existing compliance models.

## Related

- [[concepts/agent-security]]
- [[entities/ramp]]
- [[concepts/agent-governance]]
