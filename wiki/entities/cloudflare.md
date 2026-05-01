---
title: Cloudflare
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [company, platform, ai-agents, infrastructure, open-source]
sources:
  - https://blog.cloudflare.com/agents-stripe-projects/
  - https://blog.cloudflare.com/agents-week-in-review/
  - https://open.substack.com/pub/bensbites/p/building-gets-easier
---

# Cloudflare

**Cloudflare** is a global cloud platform providing CDN, DNS, DDoS protection, and serverless compute. In 2026, it positioned itself as the foundational infrastructure for the **agentic cloud** — "Cloud 2.0" — with a comprehensive suite of agent-native primitives across compute, security, tooling, and deployment.

## Agentic Cloud Stack

### Agents SDK & Runtime

Cloudflare's open-source **Agents SDK** ([github.com/cloudflare/agents](https://github.com/cloudflare/agents)) provides persistent, stateful execution environments for agentic workloads:

- **Per-agent isolation**: Each agent is its own Durable Object with state, storage, and lifecycle
- **Zero cost when idle**: Agents hibernate via DO Hibernation API, wake on demand
- **Persistent state**: Queryable, transactional SQLite storage per agent
- **Durable filesystem**: Workspace (SQLite + R2) that survives restarts
- **Web automation**: Browser Run for navigate/browse/fill-forms
- **MCP support**: Multiple MCP server/client examples in the SDK

### Project Think (April 2026)

A next-generation agents platform announced during Agents Week 2026. Builds on the Agents SDK with "batteries-included" platform capabilities: agents that think, act, and persist. Includes built-in scheduling, real-time communication, AI model calls, MCP, and workflows.

### Code Mode & Agent Tooling

- **Code Mode MCP Server**: Gives coding agents structured access to Cloudflare's platform
- **Agent Skills** ([github.com/cloudflare/skills](https://github.com/cloudflare/skills)): Pre-built skill bundles for Cloudflare operations
- **cf CLI**: New unified CLI for consistency across ~3,000 API operations
- **Local Explorer**: Debug local data during development

### Registrar API (Beta, April 2026)

Developers and AI agents can search, check availability, and register domains at cost directly from editor, terminal, or agent — without leaving the workflow.

## Autonomous Agent Provisioning (with Stripe Projects)

As of April 30, 2026, agents can autonomously provision Cloudflare infrastructure via [[concepts/agentic-commerce|Stripe Projects]]:

1. Create a Cloudflare account
2. Start a paid subscription
3. Register a domain
4. Obtain an API token
5. Deploy code to production

The agent discovers available services through the protocol, prompts for human approval where needed (ToS acceptance), but requires no dashboard interaction or manual API token copy-paste.

## Agent Readiness

Cloudflare introduced the **Agent Readiness Score** — a tool to check if websites are "agent-ready," reflecting the emerging **agentic web** where agents are a primary traffic source.

## Strategic Positioning

Cloudflare's bet: the containerless, serverless Workers platform (launched 2018) was purpose-built for the agent era. Unlike [[entities/anthropic]] (developer-owns-harness) or [[entities/openai]] (managed containers), Cloudflare provides the infrastructure layer — agents run on Cloudflare, not inside it.

## Key Events

| Date | Event |
|------|-------|
| Apr 15, 2026 | Project Think announced |
| Apr 20, 2026 | Agents Week 2026 — full agentic cloud stack unveiled |
| Apr 30, 2026 | Stripe Projects integration — agents provision Cloudflare autonomously |

## Relationships

- [[concepts/agentic-commerce]] — Stripe Projects enables autonomous Cloudflare provisioning
- [[entities/stripe]] — Co-designed Stripe Projects
- [[entities/openai]] — Competitor in agent infrastructure (managed containers)
- [[entities/anthropic]] — Alternative agent deployment model
- [[concepts/harness-engineering]] — Cloudflare provides the infrastructure harness
- [[concepts/ai-agent-engineering]] — Agent execution platform

## Sources

- [Cloudflare: Agents can now create accounts, buy domains, deploy](https://blog.cloudflare.com/agents-stripe-projects/)
- [Cloudflare: Agents Week 2026 Review](https://blog.cloudflare.com/agents-week-in-review/)
- [Cloudflare: Project Think](https://blog.cloudflare.com/project-think/)
- [Cloudflare Agents SDK (GitHub)](https://github.com/cloudflare/agents)
- [Ben's Bites: Building gets easier (Apr 30, 2026)](https://open.substack.com/pub/bensbites/p/building-gets-easier)
