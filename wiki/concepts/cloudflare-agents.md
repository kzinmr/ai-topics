---
title: "Cloudflare Agents: Internal AI Engineering Stack (iMARS)"
created: "2026-05-06"
updated: "2026-06-21"
type: concept
tags:
  - ai-agents
  - company
  - infrastructure
  - automation
  - developer-tooling
sources: [raw/articles/2026-05-06_cloudflare-internal-ai-engineering-stack.md, raw/articles/2026-06-19_cloudflare_temporary-accounts-agents.md]
---

# Cloudflare Agents: Internal AI Engineering Stack (iMARS)

Cloudflare integrated AI into its engineering workflow using its own product suite. Over 11 months, a "tiger team" called **iMARS** (Internal MCP Agent/Server Rollout Squad) built an infrastructure that now supports **93% of the company's R&D organization**.

## Key Performance Metrics (Last 30 Days as of April 2026)

| Metric | Value |
|--------|-------|
| Internal users | 3,683 (60% company-wide; 93% of R&D) |
| AI requests routed | 47.95 million |
| Tokens via AI Gateway | 241.37 billion |
| Tokens on Workers AI | 51.83 billion |
| Merge requests per week | ~5,600 → 10,900+ (2x velocity increase) |

## Three-Layer Architecture

### 1. Platform Layer: Authentication & Routing

Cloudflare uses a **"proxy Worker" pattern** to centralize control without touching client configurations:

| Component | Product Used |
|-----------|-------------|
| Authentication | Cloudflare Access (Zero Trust) |
| Routing & Tracking | AI Gateway (cost tracking, BYOK, Zero Data Retention) |
| On-Platform Inference | Workers AI (open-weight models like [[entities/kimi|Kimi K2.5]]) |
| Agent Sessions | Agents SDK (Durable Objects) |
| Sandboxing | Sandbox SDK (isolated build/test environments) |

**Key Insight:** Instead of direct client-to-gateway connections, Cloudflare uses a Worker as a "choke point" to:
- Inject API keys server-side (no keys on local machines)
- Map user emails to anonymous UUIDs for cost tracking without exposing identities
- Enforce Zero Data Retention (ZDR) by injecting `store: false` into requests

Users configure their entire environment with one command:
\`\`\`bash
opencode auth login https://opencode.internal.domain
\`\`\`

### 2. Knowledge Layer: Contextual Intelligence

To prevent agents from making "plausible but wrong" changes, Cloudflare provides structured context:

**Backstage Knowledge Graph** tracks:
- 2,055 services and 1,302 databases
- Ownership mappings for 375 teams
- Dependency graphs (which service talks to which Kafka topic/DB)

**AGENTS.md** — every repository (~3,900) contains an AGENTS.md file providing high-signal context directly to the model's context window:
> "A stale AGENTS.md can be worse than no file at all. We closed that loop with the AI Code Reviewer, which can flag when repository changes suggest that AGENTS.md should be updated."

### 3. Enforcement Layer: Quality at Scale

**AI Code Reviewer** — every merge request (MR) undergoes automated multi-agent review:
- **Risk Tiering** — classifies MRs as trivial, lite, or full
- **Specialized Agents** — dedicated agents for Security, Performance, Documentation, and Codex Compliance
- **Cost Efficiency** — Workers AI (Kimi K2.5) handles ~15% of traffic (mostly documentation), being 77% cheaper than mid-tier proprietary models

**Engineering Codex** codifies standards into "agent skills":
- Network Firewall team reduced weeks-long manual audit to a repeatable process by scoring code against Codex rules (COMPLIANT vs. NON-COMPLIANT)
- AI Code Reviewer cites specific RFC/Codex IDs in MR comments

## Future Evolution: Background Agents

The next phase involves agents that run entirely in the cloud using:
- **Durable Objects** — for long-running, stateful sessions
- **Sandbox SDK** — to clone repos, install dependencies, and run full test suites without local machine resources
- **Code Mode** — reduces context window bloat. Instead of loading 34 individual tool schemas (~15k tokens), the model uses two tools (`search` and `execute`) to discover and run code dynamically

## Temporary Cloudflare Accounts for AI Agents

On June 19, 2026, Cloudflare launched **Temporary Cloudflare Accounts for Agents**, eliminating the account-signup bottleneck for AI agent deployments. Agents can run `wrangler deploy --temporary` to deploy a Worker, website, API, or agent without any prior account or OAuth flow. Deployments stay live for **60 minutes**; a human can claim the account to make it permanent, or it expires automatically.

### Motivation

Background AI sessions (no human in the loop) need frictionless deployments. The standard browser OAuth/copy-paste/2FA flow is a hard stop for autonomous agents. Temporary accounts enable a tight write→deploy→verify loop — agents iterate by deploying throwaway Workers, curling their own output, and deciding correctness — without credential management.

### Mechanism

Built on [Wrangler](https://developers.cloudflare.com/workers/wrangler/), Cloudflare's CLI. When an unauthenticated agent runs `wrangler deploy`, Wrangler prompts the agent about the `--temporary` flag (the prompt message is crafted for LLM recognition). On re-run with the flag, Cloudflare provisions a temporary account, issues a scoped API token, and returns a claim URL for the human. The token powers the entire deployment — Workers, D1, R2, Queues, and KV.

### Significance

This pattern addresses a fundamental agentic infrastructure bottleneck: **the deployment auth wall**. It complements Cloudflare's broader agent infrastructure (iMARS stack, Agents SDK, Sandbox SDK) by removing the last mile of human-only account provisioning. See [[concepts/agent-infrastructure]] for related patterns.

## Related

- [[entities/cloudflare]] — parent organization
- [[concepts/cloudflare-llm-infrastructure]] — LLM inference infrastructure
- [[concepts/harness-engineering/agent-harness]] — agent infrastructure patterns
- [[concepts/ai-agent-security]] — security and compliance for agents
- [[entities/kimi]] — Kimi K2.5 model used on Workers AI
- [[concepts/security-and-governance/agent-governance]] — agent identity and access management
