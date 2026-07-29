---
title: camelAI
type: entity
created: 2026-07-29
updated: 2026-07-29
tags:
  - entity
  - startup
  - coding-agents
  - cloudflare
  - pi
  - serverless
  - agent-platform
  - agent-harness
  - product
  - open-source
  - cost-optimization
  - edge-computing
sources:
  - raw/articles/2026-07-28_camelai_agent-durable-object-pi-code-mode.md
  - https://github.com/qaml-ai/camelAI
  - https://camelai.com/blog/we-tried-every-container-service-then-built-our-own
related:
  - "[[entities/pi]]"
  - "[[entities/mario-zechner]]"
  - "[[concepts/harness-engineering/agent-serverless]]"
  - "[[concepts/harness-engineering/agent-harness]]"
  - "[[comparisons/agent-harnesses]]"
---

# camelAI

**camelAI** is an open-source AI coding agent platform that runs entirely on Cloudflare's edge infrastructure — no virtual machines required. Founded by Miguel (CTO), camelAI is notable for a radical architectural decision: replacing the traditional VM + bash execution model with Cloudflare Durable Objects + pi harness + JavaScript sandbox (Code Mode).

## Architecture Evolution

camelAI went through three major architectural redesigns to achieve its current serverless architecture:

### Step 0: VM Era (Claude Code Harness)

Launched on the Claude Code harness, running in full Linux VMs. The team built their own container service because existing VM providers didn't fit their persistence and performance requirements. Always-on VMs with attached disks were too expensive to scale at target user counts.

### Step 1: Brain-Hands Split (July 2026)

Built a custom harness on [[entities/pi|pi]] (Mario Zechner's open-source coding agent), importing pi's lower-level agent primitives (agent loop, state management) without depending on pi's OS-assuming upper layers. The agent process moved into a **Cloudflare Durable Object** — a small stateful compute instance on Cloudflare's edge. VMs still existed but only as remote execution targets ("hands"), controlled by the agent ("brain").

This split mirrors [[entities/anthropic|Anthropic]]'s managed agent architecture (brain separated from hands) and gave three benefits:
- Agent starts responding before VM boots
- VM can sleep when not needed
- One brain can control multiple hands (projects)

### Step 2: VM Removal — Filesystem in Durable Object + R2

Replaced the VM's filesystem with Durable Object SQLite storage (10GB cap) backed by R2 for files >1.5MB. Built on Cloudflare's **Shell** project (experimental filesystem + execution runtime for Workers). Git history via Cloudflare Artifacts.

### Step 3: Bash Removal — JavaScript Sandbox

Replaced bash with JavaScript executed through **Code Mode** and dynamic Workers. Each execution runs in a fresh V8 isolate (millisecond boot, few MB memory). Benefits:
- **Security**: Credentials never enter the sandbox — authentication happens server-side
- **Cost**: Dynamic Workers billed per execution, not uptime; thousands of executions ≈ few minutes of container time
- **Small model performance**: Explicit methods outperform bash for cheaper models in open-ended environments
- **Observability**: Platform has full visibility into every operation (e.g., deploy detection for live preview)

Containers are still used only for **builds** (Vite/Tailwind/React Router, bun install) and **notebook execution** — jobs that genuinely need Linux. All other operations use explicit JavaScript methods.

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Agent Harness | [[entities/pi|pi]] (Mario Zechner) — lower-level primitives |
| Compute | Cloudflare Durable Objects (per-thread stateful instances) |
| Execution | Code Mode + Dynamic Workers (V8 isolates) |
| Filesystem | SQLite (Durable Object) + R2 (large files) |
| Git History | Cloudflare Artifacts |
| Build/Notebook | Cloudflare Sandbox SDK (short-lived containers) |
| Deployment | wrangler deploy via controlled `deploy_project` method |

## Key Design Decisions

1. **Explicit methods over bash**: The agent can only do things the platform has built explicit methods for. This constrains the agent but forces first-class product experiences instead of letting the agent improvise.

2. **Edge-native**: Everything runs on Cloudflare's edge, close to the user. No centralized VM hosts to manage.

3. **Per-execution billing**: Dynamic Workers are billed per execution, orders of magnitude cheaper than always-on containers.

4. **Source-available**: Full codebase at [github.com/qaml-ai/camelAI](https://github.com/qaml-ai/camelAI).

## Related Concepts

- [[concepts/harness-engineering/agent-serverless]] — camelAI is a canonical implementation of the agent serverless pattern
- [[concepts/harness-engineering/agent-harness]] — Custom harness built on pi's lower layers
- [[comparisons/agent-harnesses]] — pi-based harness in the comparison matrix
- [[concepts/sandbox]] — JavaScript sandbox model vs Linux containers

## Sources

- [We rewrote our agent to run entirely in a Durable Object](https://x.com/i/article/2082137754788646912) — X Article, July 2026
- [camelAI on GitHub](https://github.com/qaml-ai/camelAI)
- [We tried every container service, then built our own](https://camelai.com/blog/we-tried-every-container-service-then-built-our-own) — Previous architecture blog post
