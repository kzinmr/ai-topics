---
title: "Claude Managed Agents"
created: 2026-05-23
updated: 2026-05-23
type: concept
tags:
  - ai-agents
  - claude-code
  - anthropic
  - sandbox
  - agent-runtime
  - architecture
  - self-hosted
  - company
  - modal
  - daytona
  - isolation
sources:
  - raw/articles/2026-05-19_cloudflare_claude-managed-agents.md
  - raw/articles/2026-05-19_modal_claude-managed-agents-sandboxes.md
  - raw/articles/2026-05-19_vercel_claude-managed-agents-sandbox.md
  - raw/articles/2026-05-19_daytona_claude-managed-agents.md
---

# Claude Managed Agents

**Claude Managed Agents** is [[entities/anthropic|Anthropic]]'s REST API-based platform for building, deploying, and running **cloud-hosted autonomous AI agents at scale**. Launched in April 2026, it lets developers define agents that read files, run shell commands, browse the web, execute code, and interact with external services — all within Anthropic's managed harness that provides built-in prompt caching, context compaction, and agent-specific performance optimizations.

The platform's defining architectural innovation is the separation of the **agent reasoning loop** ("brain," running on Anthropic's infrastructure) from **code execution and tool calls** ("hands," running in developer-controlled sandboxes). On May 19, 2026, Anthropic announced self-hosted sandbox partnerships with Cloudflare, Modal, Vercel, and Daytona, making this separation practical for production enterprise deployments.

## Architecture: "Decouple the Brain from the Hands"

The core architecture of Claude Managed Agents separates three concerns:

```
┌─────────────────────────────────────────────┐
│              ANTHROPIC (Brain)                │
│  ┌─────────┐  ┌──────────┐  ┌────────────┐  │
│  │ Agent   │  │ Session  │  │ Prompt     │  │
│  │ Loop    │  │ Manager  │  │ Cache/     │  │
│  │ (Claude)│  │ (Durable)│  │ Compaction │  │
│  └────┬────┘  └──────────┘  └────────────┘  │
│       │                                       │
│       │ Anthropic API (tool calls dispatched) │
│       │ web_search, web_fetch, MCP servers     │
└───────┼───────────────────────────────────────┘
        │
        │ Session Event Stream / Work Queue
        │
┌───────┼───────────────────────────────────────┐
│       │     SELF-HOSTED SANDBOX (Hands)        │
│  ┌────┴─────────────────────────────────────┐ │
│  │  Control Plane (your infrastructure)     │ │
│  │  - Polls work queue or receives webhooks │ │
│  │  - Manages sandbox lifecycle             │ │
│  │  - Brokers credentials (key never in VM) │ │
│  └────┬────────────────────────────────────┐ │
│       │ spawn / stop / archive             │ │
│  ┌────┴────────────────────────────────────┐ │
│  │  Sandbox (Cloudflare / Modal /          │ │
│  │  Vercel / Daytona)                       │ │
│  │  - Executes bash, read, write, edit,    │ │
│  │    glob, grep                           │ │
│  │  - Runs custom tools                    │ │
│  │  - Isolated per session                 │ │
│  └──────────────────────────────────────────┘ │
└───────────────────────────────────────────────┘
```

### Key Architectural Properties

1. **Session-based durable context**: Each agent session maintains state across multiple turns. The Anthropic platform handles session lifecycle, while the sandbox handles filesystem state.
2. **Tool dispatch split**: Filesystem and shell tools (`bash`, `read`, `write`, `edit`, `glob`, `grep`) execute inside the self-hosted sandbox. Web tools (`web_search`, `web_fetch`) and MCP server calls execute on Anthropic's side — the sandbox never needs internet access for these.
3. **Credential brokering**: The Anthropic environment key is injected at the proxy or firewall level; it never enters the sandbox VM. Path and method scoping ensures the key can only be used for the current session.
4. **Orchestration flexibility**: Control planes can use either **polling** (long-poll Anthropic's work queue) or **webhooks** (HTTP endpoint triggered by session events). Some providers support both modes.
5. **Per-session isolation**: Each agent session gets its own sandbox. No cross-session state leakage. Sandboxes are ephemeral by default.

## Sandbox Provider Comparison

Anthropic launched self-hosted sandbox support on May 19, 2026 with four integration partners. Each provider implements the same fundamental architecture (brain/hands split) but differs significantly in sandbox technology, security model, and operational characteristics.

| Dimension | Cloudflare | Modal | Vercel Sandbox | Daytona |
|-----------|-----------|-------|----------------|---------|
| **Sandbox technology** | Dual: microVM (Cloudflare Containers) + V8 isolates (AgentsSDK) | Firecracker microVMs with GPU access (H100) | Firecracker microVMs (10 years production) | Docker containers (Daytona platform) |
| **Boot time** | ~ms (isolates); seconds (microVM) | Fast cold-starts on custom images; memory snapshots | Seconds from prebuilt snapshots | Seconds from Docker snapshot |
| **Max concurrency** | "Tens of thousands" (isolates) | "Upwards of 100,000" per customer | Battle-tested at billions of deployments | Per-session containers |
| **Credential brokering** | Proxy-level injection; zero-trust; key never in sandbox | Short-lived connect tokens; SDK-mediated | Firewall-level injection; key never in VM; path+method scoping | Environment key passed to sandbox runner (scoped to one environment) |
| **GPU access** | ❌ | ✅ H100 GPUs | ❌ | ❌ |
| **Built-in browser** | ✅ Browser Run (6 tools, session recording) | ❌ (custom) | ❌ (custom) | ❌ (Anthropic server-side) |
| **Built-in email** | ✅ send/receive, agent inboxes | ❌ | ❌ | ❌ |
| **Custom images** | Dockerfile for microVMs; Dynamic Workers code for isolates | `modal.Image.debian_slim()` with full dependency trees | Prebuilt snapshots from sandbox instance | `Dockerfile` → Daytona snapshot with content hashing |
| **Persistence** | Auto-persisted across session sleeps | Volumes, directory/filesystem/memory snapshots | Ephemeral; fresh microVM per session | 10GB disk; 30-day archive after termination |
| **Egress control** | Customizable outbound proxy; allowlist endpoints | Not specified | Domain allowlist via `networkPolicy.allow`; deny-all default | Standard cloud networking |
| **Orchestration** | Workers control plane; message-based protocol | SDK-driven; event stream | Webhook → poll/ack → spawn; TypeScript/Next.js control plane | Polling (long-poll) or webhook (FastAPI); your orchestrator process |
| **Pricing model** | Not disclosed; isolates cheaper than microVMs | Burst pricing; $30/mo free; pay-per-use, no idle costs | Not disclosed; microVM pricing via Vercel | Not disclosed; per-sandbox via Daytona |
| **Best for** | Extreme scale + built-in browser/email + zero-trust security | GPU workloads + massive concurrency + serverless cost model | Firewall-level security + TypeScript teams + AWS adjacency | Full container ownership + flexible lifecycle + Dockerfile customization |

### Choosing a Provider

- **Cloudflare**: Best for teams needing extreme scale (10K+ concurrent agents via isolates), built-in browser and email tooling, and zero-trust proxy-level security within the Cloudflare ecosystem.
- **Modal**: Best for ML/AI workloads requiring GPU access (H100), massive concurrency (100K+), serverless burst pricing, and memory snapshots for rapid resume.
- **Vercel Sandbox**: Best for TypeScript/Next.js teams prioritizing firewall-level credential brokering (key never in VM), production-hardened microVM infrastructure, and low-latency AWS egress.
- **Daytona**: Best for teams wanting full Docker container ownership, sophisticated lifecycle management (pause/resume, 30-day archive), and dual orchestration modes (polling + webhook).

For a comprehensive 19-dimension comparison with decision guidance, see [[comparisons/claude-managed-agents-sandbox-providers]].

## Self-Hosted Environment Model

### How It Works

1. **Create a Self-Hosted Environment** via the Anthropic API or Console. This registers your sandbox infrastructure with Anthropic's platform.
2. **Generate an Environment Key** from the Anthropic Dashboard. This key is scoped to a single environment — it can only act on sessions and work items within that environment.
3. **Create an Agent** with custom tool definitions matching your sandbox runner's implementations.
4. **Deploy a Control Plane** (your application) that watches the work queue (polling or webhook) and manages sandbox lifecycle.
5. **Run a Tool Runner** inside each sandbox that attaches to the session event stream, executes tool calls, and posts results back.

### Three-Party Architecture

Every Claude Managed Agents session involves three parties:

| Party | Responsibility |
|-------|---------------|
| **Anthropic** | Runs the Claude agent loop, session state, work queue, prompt caching, compaction. Handles `web_search`, `web_fetch`, and MCP server calls. |
| **You** | Run the control plane (application) that creates sessions and manages sandbox lifecycle via an orchestrator. |
| **Sandbox Provider** | Provides isolated execution environments (microVMs, containers, or isolates) where filesystem and shell tools execute. |

### Orchestration Modes

- **Polling**: Your orchestrator long-polls Anthropic's work queue endpoint for new work items. Only needs the environment key. Works behind NAT/firewalls without a public URL.
- **Webhook**: Anthropic delivers `session.status_run_started` webhooks to your HTTP endpoint. Your handler polls/acks the work item and spawns a sandbox. Lower latency but requires a public URL.

### Credential Security Spectrum

The four providers represent a spectrum of credential security postures:

1. **Vercel (most hardened)**: Firewall-level header injection. Key never in VM. Path and method scoping.
2. **Cloudflare**: Proxy-level injection. Zero-trust. Key never in sandbox. Post-quantum encrypted tunnels for private services.
3. **Modal**: Short-lived connect tokens. SDK-mediated credential passing.
4. **Daytona (most permissive)**: Environment key passed to sandbox runner. Scoped to one environment. Recommended: one environment per tenant for multi-tenant deployments.

## Tools & Capabilities

### Standard Agent Tools

Claude Managed Agents provide a standard set of tools that all managed agents can use:

| Tool | Where Executed | Description |
|------|---------------|-------------|
| `bash` | Self-hosted sandbox | Run arbitrary shell commands |
| `read` | Self-hosted sandbox | Read file contents |
| `write` | Self-hosted sandbox | Write files to the sandbox filesystem |
| `edit` | Self-hosted sandbox | Targeted string replacements in files |
| `glob` | Self-hosted sandbox | Pattern-based file search |
| `grep` | Self-hosted sandbox | Content search in files |
| `web_search` | Anthropic server-side | Search the web |
| `web_fetch` | Anthropic server-side | Fetch and extract web page content |
| MCP tools | Anthropic server-side | Any MCP server tools configured for the agent |

### Built-in Platform Features

All Claude Managed Agents benefit from Anthropic's platform-level optimizations:

- **Prompt Caching**: Frequently used system prompts and tool definitions are cached server-side, reducing latency and cost.
- **Context Compaction**: When the conversation approaches the context window limit, the platform automatically summarizes and compacts earlier turns.
- **Agent-specific Performance**: The Claude agent loop is tuned for multi-turn tool-use workloads with optimized scheduling and token management.
- **Session State**: Anthropic manages session lifecycle — create, sleep, resume, terminate — with durable state across turns.

### Anthropic Skills Integration

The sandbox runner can download and install **Anthropic Skills packages** from the API, creating a drop-in experience for modular agent capabilities (such as the `claude-api` skill) in self-hosted environments.

## Getting Started

### Prerequisites

- An Anthropic API account with Managed Agents access
- A sandbox provider account (Cloudflare, Modal, Vercel, or Daytona)
- The `claude-api` skill from [Anthropic's skills repository](https://github.com/anthropics/skills/tree/main/skills/claude-api)

### Quick Start

1. **Create a Self-Hosted Environment**:
   ```bash
   curl https://api.anthropic.com/v1/environments \
     -H "x-api-key: $ANTHROPIC_API_KEY" \
     -H "anthropic-version: 2026-04-01" \
     -d '{"type": "self_hosted", "name": "my-sandbox-env"}'
   ```

2. **Generate an Environment Key** from the Anthropic Dashboard (Console → Managed Agents → Environments → your environment → Keys).

3. **Clone and customize a cookbook example** from [github.com/anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes) — choose the directory matching your sandbox provider.

4. **Deploy your control plane** (Cloudflare Workers, Modal app, Vercel Function, or Daytona orchestrator) with the environment key configured as a secret.

5. **Create an Agent** and start a session — your control plane will automatically provision sandboxes per session.

### Reference Implementations

- **Cloudflare**: Workers-based control plane with dual sandbox primitives (microVM + V8 isolates), Browser Run, Email, and Workers AI tooling
- **Modal**: Python SDK-based orchestration with serverless sandbox creation, GPU access, and memory snapshots
- **Vercel**: TypeScript/Next.js control plane + runner in a single app; firewall-level credential brokering
- **Daytona**: Python orchestrator (polling or webhook) managing Docker sandboxes with 30-day lifecycle

## Related Pages

- [[comparisons/claude-managed-agents-sandbox-providers]] — Comprehensive 19-dimension provider comparison with decision guidance
- [[entities/anthropic]] — The company behind Claude and Managed Agents
- [[entities/claude-code]] — Anthropic's CLI coding agent; Managed Agents is the API-based platform counterpart
- [[entities/lance-martin]] — Anthropic MTS and context engineering researcher who co-authored the Managed Agents architecture
- [[entities/rlancemartin]] — Lance Martin's DevRel/X handle; primary evangelist for self-hosted sandboxes
- [[entities/cloudflare-sandbox]] — Cloudflare's self-hosted sandbox integration
- [[entities/modal-sandbox]] — Modal's serverless sandbox integration
- [[entities/vercel-sandbox]] — Vercel's microVM sandbox integration
- [[entities/daytona-sandbox]] — Daytona's container sandbox integration
- [[concepts/agent-sandboxing]] — Broader concept of agent sandbox isolation
- [[concepts/agent-runtime]] — The execution environment layer in AI agent architecture
- [[concepts/context-engineering|Context Engineering]] — Lance Martin's 4-strategy taxonomy (Write/Select/Compress/Isolate)
- [[concepts/firecracker]] — Firecracker microVM technology used by Modal and Vercel

---

*Merged from :*


# Anthropic Managed Agents

**Source:** Anthropic Claude Blog + Engineering Blog + Platform Docs (April 2026)
**Status:** Public Beta on Claude Platform
**Related:** [[concepts/agent-team-swarm]], [[concepts/harness-engineering]], [[concepts/meta-harness]]


## Architecture: Brain/Hands/Session Separation

Core thesis from the Anthropic Engineering Blog post "[Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)":

> Agent harnesses inevitably encode assumptions about current model limitations. As AI capabilities improve, these assumptions become obsolete.

In the initial design, Session, Harness, and Sandbox were coupled in a single container ("pets"). The current design fully decouples these three elements ("cattle"):

| Element | Role | Benefit of Separation |
|---|---|---|
| **Brain** | Claude + Harness | Stateless → horizontally scalable |
| **Hands** | Sandbox/Tools | Provisioned on demand, recreated on failure |
| **Session** | Event Log (persistent) | State management beyond context window |

### Key Interfaces

```
Sandbox Execution:  execute(name, input) → string
Container Lifecycle: provision({resources})
Harness Recovery:   wake(sessionId) → reboot stateless harness
                    getSession(id) → retrieve durable event log
                    emitEvent(id, event) → append to session
Context Query:      getEvents() → fetch positional slices
```

### Meta-Harness Philosophy

> "We're opinionated about the shape of these interfaces, not about what runs behind them."

Managed Agents is designed as a **meta-harness** (see [[concepts/meta-harness]]). It doesn't prescribe specific implementations — it strictly defines interface boundaries.


## Multi-Agent Coordination → Expanded Features (May 2026)

Four new features of Managed Agents were released as GA/Research Preview. See [[concepts/anthropic/managed-agents]] for details.

1. **Multi-Agent Orchestration (GA)** — Coordinator agent manages up to 20 specialized sub-agents. Shared filesystem + isolated context windows. Up to 25 parallel threads.
2. **Outcomes Loop (GA)** — Rubric-driven self-improvement cycle. An independent Grader agent evaluates → feedback loop (up to 20 iterations).
3. **Dreams (Research Preview)** — Reviews past sessions to optimize Memory Store (deduplication, conflict resolution, pattern extraction). Non-destructive.
4. **Webhooks (GA)** — Push-based state change notifications. `whsec_` signature verification, lightweight payload (event type + id only).


## Performance Impact

| Metric | Improvement | Reason |
|---|---|---|
| TTFT p50 | ~60% reduction | Inference starts immediately, Sandbox on demand |
| TTFT p95 | >90% reduction | Same as above |
| Horizontal Scale | Many Brains | Stateless Harness enables parallel execution |
| Tool Context | Many Hands | Operates across multiple execution contexts |


## Pricing

- Standard Claude Platform token rates
- **+$0.08/session hour** (active runtime)


## Related

- [[concepts/agent-team-swarm]] — Higher-level concept of multi-agent coordination
- [[concepts/harness-engineering]] — Single-agent execution environment design
- [[concepts/meta-harness]] — Interface-centric design philosophy
- [[concepts/openai/symphony]] — Competitor's Agent Team orchestrator
- [[concepts/dark-factory-software-factory]] — Cutting-edge fully autonomous development

