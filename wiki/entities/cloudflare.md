---
title: Cloudflare
created: 2026-05-01
updated: 2026-05-06
type: entity
tags: [company, platform, ai-agents, infrastructure, open-source]
sources:
  - https://blog.cloudflare.com/agents-stripe-projects/
  - https://blog.cloudflare.com/agents-week-in-review/
  - https://blog.cloudflare.com/internal-ai-engineering-stack/
  - https://blog.cloudflare.com/high-performance-llms/
  - https://blog.cloudflare.com/internal-ai-engineering-stack/
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


## Internal AI Engineering Stack: iMARS (April 2026)

Over 11 months, Cloudflare's "tiger team" **iMARS** (Internal MCP Agent/Server Rollout Squad) built an AI-augmented engineering workflow now supporting **93% of R&D**:

- **3,683 internal users** (60% company-wide; 93% of R&D)
- **47.95M AI requests** routed via AI Gateway, **241.37B tokens** processed
- **51.83B tokens** on Workers AI
- **Merge requests per week**: ~5,600 → 10,900+ (2x velocity increase)

### Platform Layer
Uses a **proxy Worker pattern** for centralized control:
- Cloudflare Access for Zero Trust authentication
- AI Gateway for cost tracking, BYOK, Zero Data Retention
- Workers AI for on-platform inference (open-weight models like Kimi K2.5)
- Agents SDK (Durable Objects) for agent sessions
- Sandbox SDK for isolated build/test environments

### Knowledge Layer
- **Backstage** knowledge graph: 2,055 services, 1,302 databases, 375 teams
- **AGENTS.md** in ~3,900 repos, with AI Code Reviewer auto-flagging stale docs

### Enforcement Layer
- **AI Code Reviewer**: multi-agent MR review (Security, Performance, Documentation, Codex Compliance)
- **Engineering Codex**: standards codified into agent-checkable rules

See: [[concepts/cloudflare-agents]]

## LLM Inference Infrastructure

Cloudflare optimizes its Workers AI platform to host extra-large models like **Moonshot's Kimi K2.5** (1T+ parameters, ~560GB weights):

### PD Disaggregation
**Prefill-Decode** split across separate servers: 3x intertoken latency improvement (100ms → 20-30ms)

### Infire Inference Engine
Custom Rust-based engine outperforming standard vLLM:
- **Llama 4 Scout** on 2 H200s with 56 GiB left for KV-cache (1.2M+ tokens context)
- **Kimi K2.5** on 8 H100s with 30 GiB for KV-cache (vLLM struggles to boot)
- **Cold starts** under 20 seconds
- **20% higher** tokens/sec throughput than vLLM

### Prompt Caching
`x-session-affinity` header increased cache hit ratio from 60% → 80%

### Mooncake Integration
Adopted Moonshot AI's **Mooncake Transfer Engine and Store** for KV-cache offload to NVMe using RDMA protocols

### Speculative Decoding
Uses NVIDIA's **EAGLE-3** draft model for Kimi K2.5, particularly effective for tool calls and structured JSON outputs

See: [[concepts/cloudflare-llm-infrastructure]]

## Strategic Positioning

Cloudflare's bet: the containerless, serverless Workers platform (launched 2018) was purpose-built for the agent era. Unlike [[entities/anthropic]] (developer-owns-harness) or [[entities/openai]] (managed containers), Cloudflare provides the infrastructure layer — agents run on Cloudflare, not inside it.

## Key Events

| Date | Event |
|------|-------|
| Apr 15, 2026 | Project Think announced |
| Apr 16, 2026 | High-performance LLM infrastructure blog post |
| Apr 20, 2026 | Agents Week 2026 — full agentic cloud stack unveiled |
| Apr 20, 2026 | Internal AI Engineering Stack (iMARS) published |
| Apr 30, 2026 | Stripe Projects integration — agents provision Cloudflare autonomously |

## Relationships

- [[concepts/agentic-commerce]] — Stripe Projects enables autonomous Cloudflare provisioning
- [[concepts/cloudflare-agents]] — Internal AI engineering stack (iMARS)
- [[concepts/cloudflare-llm-infrastructure]] — High-performance LLM inference
- [[entities/kimi]] — Kimi K2.5 model hosted on Workers AI
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
