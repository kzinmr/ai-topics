---
title: "Claude Managed Agents Self-Hosted Sandbox Providers"
created: 2026-05-19
updated: 2026-05-19
type: comparison
tags:
  - comparison
  - ai-agents
  - sandbox
  - architecture
  - agent-safety
  - company
  - anthropic
  - infrastructure
  - security
  - orchestration
sources:
  - raw/articles/2026-05-19_cloudflare_claude-managed-agents-sandbox.md
  - raw/articles/2026-05-19_daytona_claude-managed-agents-sandbox.md
  - raw/articles/2026-05-19_modal_claude-managed-agents-sandbox.md
  - raw/articles/2026-05-19_vercel_claude-managed-agents-sandbox.md
---

# Claude Managed Agents Self-Hosted Sandbox Providers

A comparison of the four self-hosted sandbox providers that integrate with [[concepts/claude/managed-agents|Claude Managed Agents]], [[entities/anthropic|Anthropic]]'s enterprise agent platform. All four were announced on May 19, 2026 as part of Anthropic's "decouple the brain from the hands" initiative — the agent loop (brain) runs on Anthropic's platform, while code execution and tool calls (hands) run in your infrastructure of choice.

## Summary Comparison Table

| Dimension | Cloudflare | Daytona | Modal | Vercel Sandbox |
|---|---|---|---|---|
| **Architecture model** | Workers-based control plane; brain/hand split via message-passing | Orchestrator process (polling or webhook) manages sandbox lifecycle | Serverless sandbox orchestration; brain/hand split via event stream | Two-plane: Vercel Function (control) → Vercel Sandbox (compute) |
| **Orchestration** | Control plane on Workers; message-based protocol | Long-polling work queue or FastAPI webhook receiver | SDK-driven; `Sandbox.create.aio()` with event streaming | Webhook (`session.status_run_started`) → poll/ack → spawn |
| **Credential brokering** | Outbound proxy injects secrets; agent never sees raw credentials | Environment key scoped to single environment; passed to sandbox runner | Short-lived connect tokens; credentials via SDK, not in sandbox | Firewall-level credential injection; env key never enters VM; scoped path matchers |
| **Sandbox technology** | Dual: **microVM** (Cloudflare Containers) or **V8 isolate** (AgentsSDK/Codemode/Dynamic Workers) | **Docker containers** via Daytona's sandbox platform | **Custom container runtime**; microVM-like isolation with fast cold-starts | **microVM** (10-year battle-tested infrastructure from Vercel's build system) |
| **Boot time** | ~milliseconds (isolates); seconds (microVM) | Seconds (Docker container start from snapshot) | "Fast cold-starts" even on custom images; memory snapshots available | Seconds (from prebuilt snapshot); snapshot eliminates SDK install on every spawn |
| **Custom images** | Custom container images for microVM; isolates use Dynamic Workers code | `Dockerfile` → Daytona snapshot; Dockerfile hashing for idempotent rebuilds | `modal.Image.debian_slim()` + `apt_install`, `uv_sync`; full dependency trees | Prebuilt snapshots from a sandbox instance; `npm install` + `runner.ts` baked in |
| **Max concurrency** | "Tens of thousands" with isolates; microVM scaling via Workers | Not specified; per-session sandbox model | "Upwards of 100,000 concurrent sandboxes per customer" | Battle-tested at billions of deployments; per-session microVMs |
| **Resource limits** | Configurable instance sizes for microVMs; lightweight isolates for scale | `cpu=2, memory=8GB, disk=10GB` (defaults; configurable) | Configurable CPU (request/limit), memory (request/limit), GPU access (H100) | `node24` runtime; 1h timeout default (configurable) |
| **Egress control** | Customizable outbound proxy; allowlist endpoints; per-tenant/per-agent policies | Not specified; sandbox has normal network access | Not specified in detail; connect tokens for authenticated access | Domain allowlist via `networkPolicy.allow`; deny-all default; updatable on running sandboxes |
| **Secret injection** | Proxy-level zero-trust credential injection; headers injected outside sandbox | Environment key scoped to single environment only | Short-lived connect tokens; credentials passed via SDK | Firewall-level `inject` transforms on network policy; scoped by path + method |
| **Private connectivity** | Cloudflare Mesh + Workers VPC (post-quantum encrypted); no VPN/bastion needed | Not specified; standard cloud networking | Not specified; direct egress to customer infrastructure | Direct egress to AWS workloads with low data transfer costs |
| **Session persistence** | State auto-persisted across session sleeps | Filesystem survives sandbox pause; sandboxes stopped after idle timeout; 30-day deletion window | Volumes, directory snapshots, filesystem snapshots, memory snapshots | Ephemeral: fresh microVM per session; exits when session ends |
| **Sandbox lifecycle** | Sandbox created per session; auto-sleep/persist; observable via dashboard | Orchestrator manages: create/start/stop/archive; idle → stop (filesystem survives); terminated → archive (30-day retention) | Pay-per-use; no idle costs; sandbox exits after session | Fresh microVM per session; exits on session end; no pause/resume |
| **Disk storage** | Persisted across sleeps; cloud storage | 10GB per sandbox; 30-day archive in object storage after termination | Volumes with sub-path mounts; directory/filesystem/memory snapshots | No persistent disk; ephemeral microVM filesystem |
| **Pre-built browser** | ✅ Browser Run (browser_search, browser_execute, screenshot, browse, fetch_to_markdown, web_fetch) | ❌ Web tools handled by Anthropic server-side | ❌ Not pre-built; users implement custom tools | ❌ Not pre-built; users implement custom tools |
| **Pre-built email** | ✅ send_email, email_read, email_list; agent inboxes; session kickoff via email | ❌ | ❌ | ❌ |
| **Pre-built filesystem** | ✅ Native (microVM or isolate filesystem) | ✅ bash, read, write, edit, glob, grep (6 filesystem/shell tools) | ❌ Users implement via custom tools | ❌ Users implement run_shell, read_file (example provided) |
| **Custom tools** | ✅ `defineTool()` with zod schemas; Workers AI for image_gen; Cloudflare R2, Artifacts, etc. | ✅ Any code in sandbox runner; full container ownership | ✅ Any Python code; GPU access for ML workloads | ✅ Any code in runner.ts; network policy for external APIs |
| **Pricing model** | Not specified; isolates positioned as cheaper alternative to microVMs | Not specified; per-sandbox model via Daytona platform | Burst pricing; $30/month free compute; pay-per-use, no minimums, no idle costs | Not specified; microVM pricing via Vercel platform |
| **Unique strengths** | Isolates for extreme scale; full Cloudflare Developer Platform (Browser Run, Email, Workers AI, R2, Mesh/VPC); proxy-based zero-trust security | Most detailed "you own it" model; full Dockerfile customization; snapshot hashing for idempotency; dual orchestration modes (polling/webhook); 30-day archive retention | Highest documented concurrency (100K+); GPU access (H100); burst pricing; memory snapshots; Modal Volumes for durable storage; fastest cold-starts on custom images | Battle-tested microVM infra (10 years, billions of deploys); credential brokering at firewall level (key never in VM); scoped path+method matchers; TypeScript-native DX; low-latency AWS egress |
| **Production customers** | Not specified in launch post | Not specified | DoorDash (evaluating), Blend (agent-assisted triage), Mason AI (CTO quoted) | Not specified in launch post |
| **Best for** | Teams needing max scale + built-in browser/email + zero-trust security + Cloudflare ecosystem | Teams wanting full container ownership + flexible lifecycle + Dockerfile-based customization | Teams needing GPU access + massive concurrency + serverless cost model + ML workloads | TypeScript teams needing firewall-level security + AWS adjacency + production-hardened microVMs |

---

## Detailed Provider Analysis

### 1. Cloudflare

**Integration model.** Cloudflare provides a Workers-based control plane that receives messages from the Claude agent loop and provisions sandboxed environments per session. The control plane ships with a built-in dashboard UI, sandbox metrics, log shipping (Datadog/Splunk), and SSH access into running machines.

**Sandbox technology.** Cloudflare is unique in offering **two sandbox primitives**: traditional **microVMs** (Cloudflare Containers) for full Linux environments, and lightweight **V8 isolates** (AgentsSDK + Dynamic Workers via Codemode) for millisecond boots at massive scale. Isolates still provide a filesystem but run within a V8 engine rather than a full VM — positioned as "a faster, cheaper, and more scalable alternative" for workloads that don't need a full Linux toolchain.

**Security model.** The standout feature is **proxy-based zero-trust credential brokering**. Secrets are injected into outbound requests at the proxy layer, so the agent sandbox never has access to raw credentials. Combined with Cloudflare Mesh and Workers VPC, agents can reach private services (AWS, on-premises) over post-quantum encrypted tunnels without VPNs or bastion hosts. Egress policies are definable per tenant, per agent, or per arbitrary metadata.

**Built-in tooling.** Cloudflare provides the richest out-of-the-box tool set: Browser Run (with session recording, allowlists/denylists, audit trails), email tools (send/read/list with agent inboxes), Workers AI for image generation, and easy custom tool definitions via `defineTool()` with zod schemas. The Cloudflare Developer Platform (R2, Artifacts, Dynamic Workers) enables agents to host files, run edge inference, and deploy applications on the fly.

**Scale positioning.** Isolates are designed for "bursts of tens of thousands of concurrent agents or more" — a scale that Cloudflare argues "no VM-based solution allows."

For deeper context, see [[entities/cloudflare-sandbox|Cloudflare]].

---

### 2. Daytona

**Integration model.** Daytona's approach is the most **explicitly developer-owned**: you run an orchestrator as a long-lived process that watches Anthropic's work queue (via long-polling or webhook) and manages Daytona sandbox containers. The orchestrator handles create/start/stop/archive lifecycle, while an in-sandbox runner process (`sandbox_runner.py`) attaches to the session event stream and executes the six filesystem/shell tools. Reference implementations are provided for both polling (`host_orchestrator_polling.py`) and webhook (`host_orchestrator_webhook.py`) modes.

**Three-party architecture.** Daytona explicitly documents the three-party split: Anthropic (API + agent loop + work queue), You (application + orchestrator), and Daytona (sandbox containers). The agent loop and web tools (`web_search`, `web_fetch`) and MCP server calls stay on Anthropic's side. Only filesystem and shell tools (`bash`, `read`, `write`, `edit`, `glob`, `grep`) execute inside the Daytona sandbox.

**Sandbox technology.** Docker containers via Daytona's sandbox platform. Customization is through `Dockerfile` → Daytona snapshot, with content-hashing (`byoc-env-default-<sha8>`) for idempotent rebuilds — re-running the build script no-ops if the Dockerfile hasn't changed. A minimal snapshot (`Dockerfile.minimal`) is `FROM python:3.12-slim` with basic utilities. Per-session overrides are possible via `session.metadata` keys (`daytona.snapshot_name`, `daytona.sandbox_id`).

**Lifecycle management.** Daytona has the most sophisticated lifecycle: sandboxes idle-stopped (filesystem survives), archived on session termination (30-day window in object storage), and automatically deleted after 30 days of inactivity. Activity restarts the deletion timer. This balances cost (not paying for idle sandboxes) with durability (state preserved across pauses).

**Credential model.** The environment key is scoped to a single Anthropic environment — the runner can act on sessions in that environment and nothing else. For multi-tenant deployments, Daytona recommends giving each tenant its own environment. The environment key is passed to the sandbox runner (unlike Cloudflare and Vercel's proxy/firewall injection model).

For deeper context, see [[entities/daytona-sandbox|Daytona]].

---

### 3. Modal

**Integration model.** Modal provides a serverless sandbox orchestration layer with SDK-driven sandbox creation (`modal.Sandbox.create.aio()`). The integration ships with two reference examples: a CLI agent and a Slack bot, both on the same Modal + Managed Agents backbone. Modal positions itself as "a cloud platform built for AI workloads, with a custom container runtime and orchestration layer designed for fast, flexible, isolated compute."

**Sandbox technology.** Modal's custom container runtime is the most performance-oriented, optimized for AI workloads with: fast cold-starts even on custom images (using `modal.Image.debian_slim()` with full dependency trees via `apt_install` and `uv_sync`), memory snapshots for near-instant resume, and directory/filesystem snapshots. The platform supports **GPU access** (H100) — the only provider in this comparison offering GPU sandboxes, making it suitable for ML inference or training workloads within agent sessions.

**Persistence options.** Modal offers the richest persistence menu: Volumes (with sub-path mounts per session), directory snapshots, filesystem snapshots, and memory snapshots. This graduated approach gives developers the right tool for different persistence needs.

**Scale and pricing.** Modal claims "upwards of 100,000 concurrent sandboxes per customer" — the highest documented concurrency ceiling among the four providers. Pricing is burst/pay-per-use with no minimums, no idle costs, and $30/month of free compute. Resource configuration is fine-grained: CPU (request, limit), memory (request, limit in MiB), and optional GPU.

**Security.** Modal provides **short-lived connect tokens** that give clients authenticated, direct access to running sandbox services without exposing them to the public internet. Credentials are passed via the Modal SDK rather than injected at a network layer.

**Production adoption.** Modal is the only provider that named specific production customers: **DoorDash** (evaluating Managed Agents for their merchant intelligence system, building on existing Modal + Claude infrastructure), **Blend** (agent-assisted support triage across hundreds of unique banking environments), and **Mason AI** (CTO quoted on security boundaries for enterprise customers).

For deeper context, see [[entities/modal-sandbox|Modal]] and [[concepts/modal-sandboxes|Modal Sandboxes]].

---

### 4. Vercel Sandbox

**Integration model.** Vercel uses a **two-plane architecture**: a **control plane** (Vercel Function, a Next.js API route) receives `session.status_run_started` webhooks from Anthropic, polls and acks work items, and spawns one **compute plane** (Vercel Sandbox microVM) per session. The sandbox attaches to the session event stream, executes tool calls, posts results back, and exits when the session ends. The full implementation lives in a single Next.js app.

**Sandbox technology.** Vercel Sandbox runs on **microVMs** backed by 10 years of infrastructure that powers Vercel's build system — handling over a billion deployments. The runtime is Node.js-based (`node24`), making it TypeScript-native. Snapshots are built by creating a sandbox, installing dependencies (`npm install @anthropic-ai/sdk tsx`), copying in the runner, snapshotting, then using that snapshot for all future spawns.

**Credential brokering (standout feature).** Vercel's approach is the most security-hardened: the Anthropic environment key **never enters the sandbox VM**. Instead, the control plane configures a `networkPolicy` on each sandbox that injects the `Authorization: Bearer` header at the **firewall level**, scoped by path and method. The sandbox runner uses a placeholder `authToken: "_brokered_"` — even if compromised, an agent cannot extract the key or use it to act on other sessions. Path matchers ensure only `/v1/sessions/<thisSessionId>/...` and `/v1/environments/<envId>/work/<thisWorkId>/...` receive authentication.

**Egress control.** `networkPolicy.allow` defines a domain allowlist; the default mode is deny-all once a policy is set. Policies can be updated on running sandboxes without restarting. A useful pattern: start with allow-all to install dependencies, then tighten before running agent-generated code.

**TypeScript-native DX.** The entire integration (control plane, runner, UI) is TypeScript/Next.js, following the same developer experience principles as the Vercel AI SDK and Turborepo. OIDC authentication eliminates long-lived Vercel tokens.

**Durable streaming.** For production chat UIs, Vercel offers an integration with Vercel Workflow for durable polling, multi-turn conversations, and full event replay — addressing the serverless function timeout problem on long-running sessions.

For deeper context, see [[entities/vercel-sandbox|Vercel]].

---

## Architecture Comparison: How Each Provider Handles the Agent Loop

All four providers implement the same fundamental pattern: Anthropic's agent loop runs remotely, and the provider's sandbox executes tool calls. But the **orchestration models** differ significantly:

```
CLOUDFLARE:
  Claude Agent Loop → message → Workers Control Plane → sandbox provision
  Sandbox ← tool calls ← Control Plane → post results → Agent Loop

DAYTONA:
  Claude Agent Loop → work queue → Your Orchestrator (poll/webhook) → Daytona sandbox
  Sandbox runner ← tool calls ← session event stream → post results → Agent Loop

MODAL:
  Claude Agent Loop → event stream → Modal SDK → sandbox created
  Sandbox ← tool calls ← event stream → post results → Agent Loop

VERCEL:
  Claude Agent Loop → webhook → Vercel Function (poll/ack) → Vercel Sandbox spawn
  Sandbox runner ← tool calls ← session event stream → post results → Agent Loop
```

**Polling vs Webhook:**
- **Daytona** offers both (polling for NAT/firewall-friendly deployments; webhook for lower latency)
- **Vercel** uses webhook-triggered polling (webhook delivery → poll/ack → spawn)
- **Cloudflare** uses a message-based protocol (details not fully specified)
- **Modal** uses event-stream-driven SDK calls

**Credential brokering spectrum (most secure → most permissive):**
1. Vercel: Firewall-level injection, key never in VM, path+method scoping
2. Cloudflare: Proxy-level injection, zero-trust, key never in sandbox
3. Modal: Short-lived connect tokens, SDK-mediated
4. Daytona: Environment key passed to sandbox runner (scoped to one environment)

---

## Tooling Comparison: What Ships vs. What You Build

| Tool category | Cloudflare | Daytona | Modal | Vercel |
|---|---|---|---|---|
| Shell / code exec | ✅ Built-in | ✅ Built-in (bash) | ❌ Custom | ❌ Custom (example provided) |
| File read/write/edit | ✅ Built-in | ✅ Built-in (read, write, edit) | ❌ Custom | ❌ Custom (example provided) |
| File search (glob/grep) | ✅ Built-in | ✅ Built-in (glob, grep) | ❌ Custom | ❌ Custom |
| Browser automation | ✅ Browser Run (6 tools) | ❌ Handled by Anthropic | ❌ Custom | ❌ Custom |
| Email | ✅ Full email suite | ❌ | ❌ | ❌ |
| Image generation | ✅ Workers AI | ❌ | ❌ (GPU available for custom) | ❌ |
| MCP servers | ✅ | ✅ Server-side (Anthropic) | ✅ Server-side (Anthropic) | ✅ Server-side (Anthropic) |
| Web search/fetch | ✅ Browser-based + web_fetch | ✅ Anthropic server-side | ❌ Custom | ❌ Custom |
| Custom tool authoring | ✅ `defineTool()` + zod | ✅ Any Python in runner | ✅ Any Python + GPU | ✅ Any TypeScript in runner |

**Key insight:** Cloudflare is the only provider that ships a **full agent tool suite** out of the box — browser, email, filesystem, and custom tools. Daytona provides the 6 Anthropic-standard filesystem/shell tools. Modal and Vercel provide the sandbox infrastructure only, leaving all tool implementations to the developer (with reference examples).

---

## Verdict and Decision Guidance

### Choose Cloudflare when:
- You need **extreme scale** (tens of thousands of concurrent agents via isolates)
- You want **built-in browser and email** capabilities without building them yourself
- **Zero-trust security** via proxy-level credential injection is a hard requirement
- You're already in the **Cloudflare ecosystem** (Workers, R2, D1, Mesh/VPC)
- You need **private service connectivity** without VPNs/bastions

### Choose Daytona when:
- You want **full ownership** of the container environment ("the sandbox is yours")
- You need **sophisticated lifecycle management** (pause/resume, 30-day archive, idle timeout)
- **Dockerfile-based customization** with content-hashing for idempotent builds matters
- You need **both polling and webhook** orchestration modes
- You want the cleanest separation of concerns (three-party architecture explicitly documented)

### Choose Modal when:
- You need **GPU access** (H100) for ML workloads within agent sessions
- You require **massive concurrency** (100K+ sandboxes)
- **Serverless cost model** (pay-per-use, no idle costs) fits your budget
- You want **memory snapshots** for near-instant resume
- You need **fine-grained resource control** (CPU/memory request vs limit)
- You're building for **ML/AI workloads** specifically

### Choose Vercel Sandbox when:
- **Credential security** is your top concern (firewall-level injection, key never in VM)
- You're a **TypeScript/Next.js team** wanting native DX
- You need **low-latency egress to AWS** workloads
- You want **battle-tested microVM infrastructure** (10 years, billions of deployments)
- You need **fine-grained egress control** (domain allowlist + path/method matchers)
- You value **production durability** (Vercel Workflow for long-running sessions)

### Cross-cutting observations

- **Security posture** follows a spectrum: Vercel (most hardened credential brokering) > Cloudflare (proxy-level) > Modal (connect tokens) > Daytona (env key in sandbox)
- **Tooling completeness** is inversely correlated with environment ownership: Cloudflare (most tools, least ownership) → Daytona (balanced) → Modal/Vercel (most ownership, least built-in tools)
- **Scale ceiling** differs dramatically: Modal (100K+ documented) > Cloudflare (10Ks isolates) > Vercel (billions of builds, per-session microVMs) > Daytona (per-session containers, scale not specified)
- **MCP server support** is handled server-side by Anthropic on all four providers — MCP calls never touch the sandbox, which is a consistent architectural choice across the ecosystem

---

## Related Pages

- [[concepts/claude/managed-agents|Claude Managed Agents]] — The Anthropic platform these sandbox providers integrate with
- [[concepts/modal-sandboxes|Modal Sandboxes]] — Modal's sandbox technology and use cases (pre-dates CMA integration)
- [[comparisons/agent-sandboxing|Agent Sandboxing]] — Broader comparison of agent sandboxing approaches
- [[entities/cloudflare-sandbox|Cloudflare]] — Cloudflare's platform and AI security research
- [[entities/vercel-sandbox|Vercel]] — Vercel's platform and developer tooling
- [[entities/modal-sandbox|Modal]] — Modal's serverless GPU cloud
- [[entities/daytona-sandbox|Daytona]] — Daytona's sandbox platform
- [[entities/anthropic|Anthropic]] — The company behind Claude and Managed Agents
- [[comparisons/agent-harnesses|Agent Harnesses]] — Comparison of agent harness frameworks
- [[comparisons/ai-agent-platforms|AI Agent Platforms]] — Broader platform comparison
