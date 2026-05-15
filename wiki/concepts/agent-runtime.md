---
title: "Agent Runtime"
created: 2026-05-15
updated: 2026-05-15
type: concept
tags:
  - agent-runtime
  - agent-architecture
  - ai-infrastructure
  - agent-security
  - isolation
  - sandbox
  - harness-engineering
  - infrastructure
  - virtualization
  - technical-debt
sources:
  - "raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime.md"
  - "https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/"
  - "https://cognition.ai/blog/what-we-learned-building-cloud-agents"
  - "https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal"
  - "https://northflank.com/blog/top-modal-sandboxes-alternatives-for-secure-ai-code-execution"
  - "raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics.md"
aliases: [agent-serving-infrastructure, agent-sandbox, agent-execution-environment]
---

# Agent Runtime

## Summary

The **agent runtime** is the execution environment where an AI agent operates — the union of compute substrate, filesystem, tools, network boundary, state model, and lifecycle controller. It is the largest and most consequential box in the agent systems diagram, analogous to how Sculley et al.'s classic diagram showed that "ML Code" was the smallest piece of a real ML system.

> The agent is not the model. The agent is the harness plus the model, running inside the runtime. — Han Lee (2026)

The runtime decides whether your agent finishes in eight seconds or eight minutes, whether two users can share an environment safely, and whether a malicious prompt can read your secrets. Almost all teams shipping agents today have **not** built this layer — they have rented it, glued it together from cloud primitives designed for different workloads, or simply not thought about it yet.

However, "runtime" in the agent context also carries a **higher-level meaning**: it is the **execution control system** that manages the agent's lifecycle, mediates tool interactions, maintains state continuity, schedules subtasks, enforces safety policies, and emits events — the layer that makes an agent a **persistent execution entity** rather than a series of stateless completions. This dual nature of runtime — **infrastructure substrate** (Han Lee's framing) and **execution semantics** (the control system framing) — is explored throughout this page.

## Anatomy

An agent runtime is the union of six components:

| Component | Role |
|---|---|
| **Compute substrate** | Container, microVM, or full VM where code runs |
| **Filesystem** | Read/write, with snapshot and rollback semantics |
| **Tools** | Shell, code interpreter, browser, file editor, MCP servers |
| **Network boundary** | Defines what the agent can reach and what can reach it |
| **State model** | Decides what persists across turns, episodes, and users |
| **Lifecycle controller** | Starts, suspends, snapshots, resumes, and tears down environments |

In Han Lee's [[concepts/rl-environments-for-llm-agents|taxonomy of RL environments]], these correspond to the $H$ (harness) and $S$ (state) components.

## Execution Semantics: The Control System Layer

While the anatomy above describes the runtime as **infrastructure** — what machines, containers, and filesystems the agent runs on — there is a complementary view: runtime as the **execution semantics** layer. This is the software control system that sits between the model (which decides *what to do*) and the environment (where actions take effect), managing *how execution proceeds safely and continuously*.

> **Agent runtime is the execution control system that makes an agent a persistent, stateful execution entity — not a series of stateless completions.**

This framing distinguishes agent runtime from three things it is often confused with:

| What It Is NOT | What It IS | Why the Distinction Matters |
|---|---|---|
| **Language runtime** (Python, Node.js, asyncio, containers, VMs) | An **execution semantics** layer above the OS — closer to browser runtime, game engine runtime, or actor runtime | The language runtime provides processes and threads; the agent runtime provides lifecycle, tool mediation, and state continuity on top of them |
| **Workflow framework** (LangGraph, Temporal) | An **execution continuity** system | Workflow frameworks describe *what should happen* (execution topology); the runtime maintains *how execution continues* (lifecycle, recovery, state) |
| **The model** (LLM) | The **complement** to the model | The model owns *reasoning* ("what to do"); the runtime owns *execution semantics* ("how to proceed safely") |

### The Eight Responsibilities of an Agent Runtime (Execution Semantics View)

| # | Responsibility | What It Does |
|---|---|---|
| **1** | **Execution Lifecycle Management** | Manages `agent run` as a first-class entity: start, pause, resume, cancel, retry, checkpoint, terminate. This is the runtime's most fundamental job — treating an agent execution as a managed lifecycle, not a fire-and-forget API call. |
| **2** | **Tool Mediation** | Intermediates between LLM and tools. The runtime owns: tool schema registration, argument validation, execution, timeout enforcement, retries, sandboxing, auth, and rate limits. A "tool" is not a simple function call — it has runtime semantics. |
| **3** | **State Continuity** | Maintains *execution identity* across turns: message history, scratchpad, memory, intermediate observations, browser state, filesystem state. The agent is treated as a **persistent execution entity**, not a stateless completion. |
| **4** | **Environment Mediation** | Mediates interaction with the external world: browser session, shell session, GUI control, DOM, screenshots, filesystem. Critical for browser-use and computer-use agents. The runtime is the **"world interface"** — the single point through which the agent perceives and acts upon its environment. |
| **5** | **Scheduling** | Manages subtask spawning, delegation, concurrency, prioritization, and interruption. The most OS-like responsibility — the runtime decides what runs when, with what priority, and whether it can be preempted. |
| **6** | **Event System** | Emits a stream of execution events: token stream, tool start, tool end, approval request, delegation, retry, failure, completion. Because execution is an *ongoing process*, not a single atomic operation, the event stream is the primary observability surface. |
| **7** | **Safety / Policy Enforcement** | Enforces permissions, approval boundaries, sandbox quotas, and tenant isolation. For tools like Claude Code, this is architecturally critical — the model decides *what to attempt*; the runtime decides *what is allowed*. |
| **8** | **Observability** | Provides traces, spans, event logs, and replayability. A runtime that cannot be observed cannot be debugged; a runtime that cannot replay trajectories cannot be improved. |

### Model ↔ Runtime Separation

The runtime does **not** own reasoning. That belongs to the model.

| | Model | Runtime |
|---|---|---|
| **Owns** | Reasoning: *what to do* | Execution: *how to proceed safely and continuously* |
| **Example** | "Open the file, find the bug, edit the function" | Start session → spawn shell → validate file path → execute edit → run tests → emit completion event |
| **Intelligence** | Yes | No — execution semantics only |
| **State** | Stateless (by default) | Maintains all execution state |

This separation explains why the OS metaphor is apt: the runtime manages process lifecycle, scheduling, I/O mediation, permissions, eventing, and state — exactly the responsibilities of an operating system's kernel, but at the agent execution layer rather than the hardware layer.

### Workflow Framework vs Runtime System

This is one of the most consequential architectural distinctions:

| | Workflow Framework | Runtime System |
|---|---|---|
| **Core question** | *What should happen?* | *How does execution continue?* |
| **Primary concern** | Describe execution topology (DAG, state machine, graph) | Maintain execution continuity (lifecycle, recovery, state) |
| **Example** | LangGraph — defines nodes, edges, conditional routing | Claude Code's loop — manages tool mediation, safety gates, event emission |
| **State model** | Explicit, graph-structured, designed by the developer | Implicit, maintained by the runtime across turns |
| **Relationship** | A workflow framework can be *implemented on top of* a runtime | A runtime can *execute* a workflow framework's topology |

**Concrete difference**: PI, OpenAI Agents SDK, and Claude Agent SDK are all building **agent execution substrates** (runtimes) to varying degrees. LangGraph is closer to an **orchestration description layer** (workflow framework). The former maintains *how execution continues*; the latter describes *what should happen*.

### The Diagram

```
           ┌─────────────────┐
           │     Model        │  ← "what to do" (reasoning)
           └────────┬────────┘
                    │
          reasoning/tool intent
                    │
           ┌────────▼────────┐
           │     Runtime      │  ← "how execution proceeds"
           │──────────────────│
           │ lifecycle         │
           │ tool mediation    │
           │ state continuity  │
           │ scheduling        │
           │ safety/policy     │
           │ event system      │
           │ observability     │
           └────────┬────────┘
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Browser         Shell         GUI/OS
```

### Why This Distinction Matters Now

The transition from **completion-centric** to **agent-centric** computing is what makes the runtime layer necessary:

- **Old world**: `LLM call = atomic operation` — a single request/response with no continuity. A completion API was sufficient.
- **New world**: `LLM execution = long-lived process` — spanning minutes to hours, with tool calls, sub-agent delegation, interruptions, and recovery. A completion API cannot handle state continuity, interruption, environment interaction, delegation, or recovery.

The runtime is the architectural answer to this shift. Every major agent platform (PI, OpenAI Agents SDK, Claude Agent SDK, LangGraph) is converging on the same realization: agents need an execution substrate that treats them as **persistent execution entities**, not stateless completions.

> **Shortest definition**: The agent runtime is the control system that makes an agent a **persistent, stateful execution entity** — not a series of stateless completions.

**Source**: kzinmr, "Agent Runtime as Execution Control System" (2026-05-15), [[raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics]].

## Why Sandboxing Is Not Optional

Models hallucinate code. They run `rm -rf`. They paste credentials into curl commands. They follow instructions embedded in untrusted documents. None of these are exotic edge cases — they are the modal behavior of capable models when handed unrestricted tool access.

The sandbox is the layer that stops these behaviors from becoming incidents. Four reasons it must be a first-class layer:

1. **Isolation against the model's mistakes** — Filesystem isolation, copy-on-write snapshots, per-session ephemerality turn destructive actions into recoverable ones
2. **Isolation against prompt injection** — Tool outputs are attacker-controlled the moment the agent visits a webpage or processes a customer email. This is the agent-systems version of the SQL injection lesson, roughly at the 2003 stage of learning it
3. **Multi-tenancy at training scale** — RL training spins up thousands of concurrent rollouts; each needs its own filesystem, process tree, and network namespace
4. **Reproducibility** — A sandbox you can snapshot is a sandbox you can replay, enabling debugging of six-hour agent trajectories

### Cognition's Post-Mortem

The [[entities/cognition|Cognition]] team (Devin) learned that **containerized agents share a kernel**, meaning a single compromised session can reach every other container's filesystem, credentials, and network connections. Their conclusion after over a year of hypervisor engineering: **VM-level isolation**, where each session gets its own kernel and there is no shared attack surface.

Similarly, the [[entities/manus|Manus]] team built all agent runtimes with snapshotted, restorable formats so users can replay what agents have done.

## The Isolation Primitive Stack

Five primitives in serious use, with very different trade-offs:

| Primitive | Isolation model | Cold start | Workload fit | Notable users |
|---|---|---|---|---|
| **Linux containers** (runc, Podman) | Shared host kernel, namespaces + cgroups + seccomp | ~100ms | Trusted code, internal CI | Docker, Kubernetes default |
| **Firecracker** | KVM-based microVM, dedicated kernel per VM | ~125ms boot, sub-second from snapshot | Untrusted code at high density | AWS Lambda, Fargate, E2B, Fly.io |
| **gVisor** | Userspace kernel intercepting syscalls; runc-compatible | Container-class | Defense in depth | Google Cloud Run, App Engine, Modal |
| **Kata Containers** | Lightweight VM per pod, OCI-compatible | Few hundred ms | Multi-tenant Kubernetes | Confidential Containers |
| **V8 isolates** | Per-tenant JS heap inside a single process | Sub-millisecond | JavaScript-only, no arbitrary binaries | Cloudflare Workers, Deno Deploy |

### Critical Distinctions

- **Containers are not a sandbox for agent code** — Shared kernel means a kernel exploit takes down the isolation boundary. Not safe for agents that may execute attacker-controlled instructions.
- **Firecracker is the de facto industry primitive** — Strong isolation, fast boot (125ms), high density. Almost all agent-sandbox startups run on it.
- **gVisor is the middle path** — Stronger isolation than namespaces without full VM cost. Trade-off: some syscalls are slower or unsupported.
- **V8 isolates are the wrong primitive for general agent workloads** — Cannot run arbitrary Python, install packages, or execute compiled binaries.

## The Sandbox-as-a-Service Landscape

A category of startups has emerged in the last two years, almost all building on the primitives above:

### Startup Vendors

| Vendor | Isolation | Snapshot model | Cold start | Notable |
|---|---|---|---|---|
| **Modal** | gVisor | Filesystem diffs from base image | Sub-second | GPU support; reference case: Ramp Inspect |
| **E2B** | Firecracker microVM | Full VM snapshot | ~150ms | Open-source SDK, language-agnostic |
| **Daytona** | Containers / VMs | Forkable workspaces | Few seconds | Forked dev environments, OCI-compatible |
| **Northflank** | Containers, GPU-aware | Persistent volumes | Container-class | GPU sandboxes |
| **Browserbase / Steel / Hyperbrowser** | Containerized browsers | Session replay | Seconds | Browser-only runtimes (CDP, DOM, screenshots) |
| **Cloudflare Workers Sandbox** | V8 isolates + containers | Object snapshots | Milliseconds | Edge-first, shared-nothing |
| **Vercel Sandbox** | Firecracker | Snapshot from build | Sub-second | Tied to Vercel deploy/preview |

### Ramp Inspect Case Study (Modal)

Ramp's background coding agent now writes **more than half of Ramp's merged PRs**. Each session runs in its own Modal sandbox containing Postgres, Redis, Temporal, RabbitMQ, VS Code server, and VNC/Chromium. Filesystem snapshots are refreshed every 30 minutes by cron.

> The agent's productivity is bounded by the runtime's startup time, not by the model's tokens-per-second.

### Hyperscaler Offerings

| Provider | Product | Isolation | Notable gaps |
|---|---|---|---|
| **AWS** | Bedrock AgentCore | microVM-class | Limited heterogeneous workload support; runtime must be coded like a Lambda function |
| **Azure** | Container Apps Dynamic Sessions | Hyper-V | Strongest if already on Azure OpenAI + AKS; limited heterogeneous workload support |
| **GCP** | Cloud Run Sandboxes | gVisor (Cloud Run) | Ahead of pack in usability; supports heterogeneous workloads |

**Warning**: Lambda, Fargate, App Runner, and Cloud Run (in their generic form) are **not suitable** as agent sandboxes — they are designed for stateless, request-response workloads with strict execution-time limits and no native snapshot model.

## Experimentation vs Production: Different Runtimes

One of the major differences between AI engineering and traditional web development: training and production require fundamentally different runtimes.

| Dimension | Experimentation / Training | Production / Serving |
|---|---|---|
| **Concurrency shape** | Thousands of parallel rollouts, bursty | One session per user, steady-state |
| **Cold start tolerance** | Critical — 5s × 10k rollouts is real money | Forgivable — users wait |
| **State model** | Fork, branch, replay, snapshot | Durable, per-user, auditable |
| **Network policy** | Often offline or recorded for determinism | Open internet, real APIs |
| **Failure model** | Drop the rollout, sample more | Retry, degrade, page someone |
| **Observability** | Full trace, every token, replayable | SLOs, error budgets, sampling |
| **Cost model** | Spot, preemptible, batch | Reserved, predictable, latency-bound |
| **Lifetime** | Seconds to minutes | Minutes to hours, or pinned for a session |

Optimizing the same runtime for both is how you end up with a system too slow for training and too brittle for production.

### The Async Gap Problem

Production agents need to survive **async gaps** — an agent opens a PR, waits on CI, responds to a review comment, reruns tests, pushes a follow-up commit. Between each step there are minutes, hours, or days where the agent's working state must persist.

Cognition's solution: **hypervisor-level snapshotting** of the full machine state (memory, process tree, filesystem). The agent shuts down while idle and resumes exactly where it left off when a CI result arrives. Building this took longer than any other piece of infrastructure they had shipped.

## Runtime Shift: The New Distributional Shift

The agent learns the runtime — tool latencies, failure modes, shell quirks, filesystem layout, the exact way `ls` formats output. Move to a different runtime and behavior shifts. This is **runtime shift**: silent quality regressions that no eval catches because the eval runs in the training runtime.

### Three Honest Paths Through Runtime Shift

1. **Co-locate train and prod on the same runtime** — Pick one sandbox provider, run RL rollouts and production sessions on it, accept the lock-in. This is what the most disciplined AI engineering teams do.
2. **Define a runtime contract** — A versioned interface covering API surface, timing, and failure semantics. Implement once on training infra, once on production infra. Harder than it sounds.
3. **Train against production noise** — Inject latency, errors, and tool failures during training so the policy is robust to runtime variance. [[concepts/step-deepresearch|Step-DeepResearch]] reports tangible gains from injecting 5–10% tool errors during training — the runtime analog of dropout.

## Runtime Debt: The Bill Coming Due

Runtime debt follows a predictable pattern:

1. Team picks the sandbox easiest to integrate at prototype time
2. Production traffic exposes different failure modes
3. Team patches with retries, longer timeouts, prompt-engineered apologies
4. Agent behavior gets entangled with that runtime's quirks through whack-a-mole fixes
5. A year later, switching runtimes is a six-month migration because nobody can predict which behaviors will move

This is the direct agent-systems analog of the technical debt patterns described in Sculley et al. (2015).

> The agent has to live on a runtime. The teams that internalize that early will spend the next two years compounding the advantage. The teams that do not will spend the next two years paying down a debt they did not know they were taking on. — Han Lee

## Relationship to Other Concepts

- **[[concepts/agent-harness]]** — The harness + model run inside the runtime. The runtime is the execution environment; the harness is the orchestration layer within it. Han Lee's taxonomy: $H$ (harness) and $S$ (state) are runtime components. **Distinction from the execution semantics view**: the harness decides *what the agent attempts*; the runtime (as control system) decides *how execution proceeds* — managing lifecycle, tool mediation, state continuity, scheduling, events, safety, and observability independent of the harness's orchestration choices.
- **[[concepts/context-engineering]]** — Context engineering manages what the model sees; the runtime defines where and how the model executes. The runtime's network boundary and filesystem shape what context is even available.
- **[[concepts/reduce-offload-isolate]]** — Anthropic/Lance Martin's three principles for stripping harness complexity. The runtime's isolation model directly impacts how well you can "isolate" sub-agent contexts.
- **[[concepts/harness-commoditization]]** — As models absorb harness features, the runtime (not the harness) may become the durable differentiator.
- **[[concepts/workflow-orchestration-frameworks]]** — Workflow frameworks describe *execution topology* (what should happen); the runtime maintains *execution continuity* (how execution proceeds). LangGraph is closer to a workflow framework; Claude Agent SDK and PI are closer to runtimes.
- **[[entities/han-lee]]** — Original source of the infrastructure-centric runtime framing and the runtime debt concept.

## References

- Lee, H. (2026). [Hidden Technical Debt of AI Systems: Agent Runtime](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/)
- Lee, H. (2026). [A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/)
- Cognition. (2026). [What We Learned Building Cloud Agents](https://cognition.ai/blog/what-we-learned-building-cloud-agents)
- Workman, G. (2026). [How Ramp built a full-context background coding agent on Modal](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal)
- Northflank. (2026). [Top Modal Sandboxes Alternatives for Secure AI Code Execution](https://northflank.com/blog/top-modal-sandboxes-alternatives-for-secure-ai-code-execution)
- Sculley et al. (2015). Hidden Technical Debt in Machine Learning Systems. NeurIPS.
