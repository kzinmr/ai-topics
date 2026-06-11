---
title: "Agent Runtime"
created: 2026-05-15
updated: 2026-05-23
type: concept
tags:
  - agent-runtime
  - architecture
  - infrastructure
  - agent-safety
  - isolation
  - sandbox
  - harness-engineering
  - virtualization
  - technical-debt
  - state-management
  - networking
sources:
  - "raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime.md"
  - "https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/"
  - "https://cognition.ai/blog/what-we-learned-building-cloud-agents"
  - "https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal"
  - "https://northflank.com/blog/top-modal-sandboxes-alternatives-for-secure-ai-code-execution"
  - "raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics.md"
  - "raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis.md"
  - "raw/articles/2026-05-15_kzinmr_why-runtime-centric-now-control-flow-ownership.md"
aliases: [agent-serving-infrastructure, agent-sandbox, agent-execution-environment]
---

# Agent Runtime

## Summary

The **agent runtime** is the execution environment where an AI agent operates — the union of compute substrate, filesystem, tools, network boundary, state model, and lifecycle controller. It is the largest and most consequential box in the agent systems diagram, analogous to how Sculley et al.'s classic diagram showed that "ML Code" was the smallest piece of a real ML system.

> The agent is not the model. The agent is the harness plus the model, running inside the runtime. — Han Lee (2026)

The runtime decides whether your agent finishes in eight seconds or eight minutes, whether two users can share an environment safely, and whether a malicious prompt can read your secrets. Almost all teams shipping agents today have **not** built this layer — they have rented it, glued it together from cloud primitives designed for different workloads, or simply not thought about it yet.

However, "runtime" in the agent context also carries a **higher-level meaning**: it is the **execution control system** that manages the agent's lifecycle, mediates tool interactions, maintains state continuity, schedules subtasks, enforces safety policies, and emits events — the layer that makes an agent a **persistent execution entity** rather than a series of stateless completions. This dual nature of runtime — **infrastructure substrate** (Han Lee's framing) and **execution semantics** (the control system framing) — is explored throughout this page.

## Anatomy

### The 5-Layer Agent Stack

Before examining the runtime's internal anatomy, it helps to locate the runtime within the broader agent software stack. kzinmr (2026-05-15) proposes a 5-layer model that clarifies the separation of concerns:

```
┌────────────────────────────────┐
│  Application / Product Layer   │  ← End-user-facing product
├────────────────────────────────┤
│  Agent Framework / Workflow    │  ← LangGraph, PydanticAI
├────────────────────────────────┤
│  Harness / Runtime             │  ← ClaudeCode, Codex, OpenClaw, PI
├────────────────────────────────┤
│  Tool / Environment Layer      │  ← Browser, Computer, Shell
├────────────────────────────────┤
│  Model API                     │  ← Claude, GPT, Gemini
└────────────────────────────────┘
```

This stack structure reveals that the **Harness / Runtime** layer is the architectural center of gravity — it sits between the model's raw intelligence and the developer's application logic, mediating both. All agent stack comparisons can be organized as:
- **Runtime comparison** — how execution is managed (Harness/Runtime layer)
- **Workflow framework comparison** — how orchestration is described (Framework/Workflow layer)
- **Vendor-controlled vs developer-controlled abstraction** — who owns each layer's design decisions

### The Historical Arc: Where the Center of Gravity Moves

The agent stack's center of gravity has shifted dramatically over three years, tracing a trajectory from *description* to *execution*:

```
2023  →  Framework-centric (LangChain)
2024  →  Workflow-centric (LangGraph)
2025- →  Harness/Runtime-centric (ClaudeCode, Codex, OpenClaw, PI)
```

Agent value has migrated: **Prompt → Workflow → Runtime**. This is not a rejection of frameworks or workflows — it's a recognition that as models become more capable, the bottleneck shifts from *what to describe* to *how to execute continuously and safely*. The runtime becomes the primary source of differentiation, not the orchestration DSL.

A more precise periodization (kzinmr, 2026-05-15):

```
2023: Weak model → explicit workflows dominate
     (framework compensates for weak models)
2024: Stronger models → hybrid orchestration
2025+: Runtime-mediated execution → runtime-centric systems dominate
     (runtime amplifies strong models)
```

> **Core message**: As models become capable of owning control flow, the bottleneck shifts from orchestration logic to execution runtime design. Model quality alone no longer determines agent capability. Runtime design increasingly dominates real-world performance.

See [[concepts/agent-runtime#execution-semantics-the-control-system-layer|§Execution Semantics]] for the detailed analysis of what makes the runtime layer architecturally distinct from workflow frameworks.

### Internal Anatomy: The Six Infrastructure Components

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

### Why Now: Control Flow Ownership and the Real Shift

The transition from **completion-centric** to **agent-centric** computing is the surface explanation. But a deeper question remains: ReAct loops existed in the LangChain era — why did they not drive a runtime-centric architecture shift until now?

**The loop was always possible.** Developers have been able to write `while True: thought = llm(...); action = parse(thought); result = tool(action)` since the first tool-calling API. The presence of a loop is **not** the structural difference.

#### Who Owns Control Flow?

The real shift is about **who can safely hold control flow authority** (kzinmr, 2026-05-15):

| Era | Model Capability | Control Flow Authority | Architecture |
|---|---|---|---|
| **Workflow-centric (2023)** | Model is an *unreliable primitive* — tool misuse, context drift, hallucinated routing, loop collapse, inconsistent planning | **Developer** holds authority via graphs, constraints, explicit routing, structured transitions | LLM embedded inside developer-authored workflow |
| **Runtime-centric (2025+)** | Model can *maintain execution semantics* — tool continuation, long-horizon tasks, retry adaptation, context tracking, subtask decomposition, failure recovery | **Model** drives what happens next; **runtime** mediates how it happens safely | Runtime loop is primary; workflow emerges from execution |

The LangGraph worldview was correct *for its time*: when models could not safely own control flow, developers needed to hold control flow authority through explicit graphs. What changed in 2024-2025 was not that loops became possible — it was that **models became reliable enough to maintain execution semantics across long, open-ended trajectories**.

#### The Question Shift

This capability shift transforms the central engineering question:

| Era | Core Question | Primary Concern |
|---|---|---|
| **Workflow-centric** | "How do we constrain flow?" | Developer-authored topology, explicit routing, structured transitions |
| **Runtime-centric** | "How do we execute safely?" | Lifecycle management, tool sandboxing, interruption, retries, observability, approval boundaries |

When the model can participate in orchestration, the bottleneck shifts from *orchestration logic* to *execution runtime design*. This is the deepest architectural implication of the runtime-centric shift.

#### Why Browser/Computer-Use Forced the Shift

The single biggest forcing function was **open-ended environments**. Coding tasks are comparatively deterministic, symbolic, and replayable — a developer-authored graph can enumerate valid paths. But browser and computer-use environments are dynamic, stateful, partially observable, and failure-prone:

- You cannot pre-author **all valid paths** in a graph for a GUI interaction — the DOM changes, selectors break, rendering is asynchronous
- You cannot predict what the model will see next — every screenshot is a new observation with no symbolic representation
- You cannot hardcode recovery strategies — failures take novel forms that require model-level reasoning

In these environments, **developer-authored graphs break down**. The runtime must handle retries, replanning, interruption, adaptive tool use, and opportunistic delegation — not as pre-scripted graph branches, but as emergent execution behaviors. Runtime-centric systems are fundamentally an adaptation to **open-world agent execution**.

> **As models become capable of owning control flow, the bottleneck shifts from orchestration logic to execution runtime design.** — kzinmr (2026-05-15)

### The Structural Inversion: Graph Primary vs Loop Primary

At the deepest architectural level, the shift from workflow-centric to runtime-centric is a **structural inversion** of what is primary and what is emergent:

| | Workflow-Centric | Runtime-Centric |
|---|---|---|
| **What is primary?** | Graph — developer-authored topology | Runtime loop — model-driven execution |
| **What is emergent?** | LLM behavior constrained by graph edges | Workflow emerges from execution trajectory |
| **Who decides what's next?** | Developer (via graph structure) | Model (via reasoning); runtime mediates |
| **System character** | Predictable, constrained | Adaptive, open-world |
| **Analogy** | Railroad tracks — the path is laid before the train moves | Autonomous navigation — the path is discovered in real time |
| **Best for** | Deterministic business logic, audit trails, compliance | Unpredictable environments, exploration, creative problem-solving |

#### The "PydanticAI Can Do ReAct" Question

A natural objection: PydanticAI and other workflow-centric frameworks can implement ReAct loops. Doesn't that mean they can achieve the same runtime-centric behavior?

The answer is no — because **architecture is about what is primary, not what is possible**. In a workflow-centric framework, even a ReAct loop is *embedded inside a developer-authored graph*. The graph owns the lifecycle; the loop is a component. In a runtime-centric system, the loop owns the lifecycle; the graph (if it exists at all) is an emergent description of what happened, not a prescriptive description of what must happen.

| | PydanticAI + ReAct | PI / ClaudeCode / OpenClaw |
|---|---|---|
| **Loop status** | Component inside graph | Primary execution substrate |
| **Graph status** | Primary (prescriptive) | Emergent (descriptive) or absent |
| **Control flow ownership** | Developer (via graph edges) | Model (via runtime mediation) |
| **What happens when the model does something unexpected** | Constrained by graph topology | Runtime mediates, adapts, recovers |

The difference is not capability — both can execute tool-calling loops. The difference is **who holds the architecture's center of gravity**: the developer's pre-authored topology, or the model's runtime-mediated execution.

### What Dies and What Survives: The Future of Agent Infrastructure

If the shift is real, what parts of today's agent infrastructure become more important and what parts decline?

#### Declining: Explicit Orchestration DSL

As models internalize decomposition, routing, planning, and recovery, the value of developer-authored orchestration decreases:

- `graph.add_edge(...)` — explicit routing rules
- Hand-coded state transitions
- Pre-scripted retry/recovery branches
- Developer-authored planning decompositions

These are not going to zero — deterministic business logic still needs explicit structure. But their relative importance declines as models become more capable of owning control flow.

#### Growing: Execution Semantics

The runtime layer becomes **more** important, not less:

| Growing Concern | Why It Matters More |
|---|---|
| **Observability** | When the model owns control flow, you need traces, spans, and replayability to understand what happened |
| **State management** | Runtime-managed state across turns, sessions, and interruptions becomes the backbone |
| **Permissions & safety** | The runtime must enforce what the model is *allowed* to do, independent of what it *decides* to do |
| **Scheduling & delegation** | Sub-agent spawning, concurrency, prioritization — OS-like scheduling becomes critical |
| **Isolation & sandboxing** | Every tool execution, every sub-agent, every environment interaction needs runtime-enforced boundaries |
| **Memory continuity** | Across turns, sessions, and interruptions — the runtime holds the agent's identity |
| **Runtime policies** | Approval boundaries, quotas, rate limits — enforced at the runtime level, not in application code |

#### The Half-Right, Half-Wrong Thesis

> "As models improve, frameworks become irrelevant."

- **Half right**: workflow-centric abstraction shrinks. Explicit orchestration DSLs decline in relative importance.
- **Half wrong**: runtime abstraction becomes **more** important. The bottleneck shifts from orchestration logic to execution runtime design.

The future is not a "workflow compiler" — it's an **agent operating runtime**. This is why ClaudeCode and Codex's advantage is not just model quality but **model × runtime co-design**: the model is trained on the runtime's trajectories, and the runtime is optimized for the model's failure modes.

> **Shortest definition**: The agent runtime is the control system that makes an agent a **persistent, stateful execution entity** — not a series of stateless completions.

**Source**: kzinmr, "Why Runtime-Centric Now — Control Flow Ownership" (2026-05-15), [[raw/articles/2026-05-15_kzinmr_why-runtime-centric-now-control-flow-ownership]].

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

## The State Model: Snapshot, Replay, Rollback

State management is not a nice-to-have in agent systems — it is the foundation of debugging, evaluation, and iterative improvement. The runtime must provide primitives for capturing, restoring, and replaying agent state across turns, episodes, and sessions.

### Core Primitives

| Primitive | Description | Use Case |
|---|---|---|
| **Filesystem snapshots** | Copy-on-write filesystem state capture | Rollback after destructive operations; checkpoint before risky tool calls |
| **Memory snapshots** | Full process memory capture via CRIU or VM snapshot | Suspend/resume for long-running agents; async gap survival |
| **Session replay** | Deterministic re-execution from recorded trajectories | Debugging failure modes; regression testing; eval reproducibility |
| **State export/import** | Checkpoint-restore across environments | Migration between runtimes; sharing agent progress; CI/CD integration |

### Production Evidence

- **Cognition (Devin)**: Hypervisor-level snapshotting of full machine state (memory, process tree, filesystem) to survive async gaps. The agent shuts down while idle and resumes exactly where it left off when a CI result arrives. Building this took longer than any other piece of infrastructure they shipped.
- **Manus**: Snapshotted all agent runtimes in restorable formats for future replay — users can replay everything an agent has done.
- **Daytona**: Snapshot-based sandboxes with 30-day lifecycle, enabling fork-and-resume workflows.

> *"The ability to snapshot and replay agent sessions is not a nice-to-have. It is the foundation of debugging, evaluation, and iterative improvement of agent behavior."* — Han Lee

## Network Boundary Design

The runtime's network boundary defines what the agent can reach and what can reach it. Lee catalogs six patterns, from most to least restrictive:

### Six Patterns

| # | Pattern | Description | Use Case |
|---|---|---|---|
| 1 | **No network** | Air-gapped sandbox; zero external connectivity | RL training rollouts where determinism matters; classified data processing |
| 2 | **Egress-only allowlist** | Explicit domains only via firewall rules | Production agents that need specific APIs; reduces blast radius |
| 3 | **Proxy-mediated** | All traffic routed through a controllable proxy with logging, filtering, and rate limiting | Enterprise deployments requiring audit trails and content filtering |
| 4 | **Credential brokering** | Sandbox never sees raw secrets; runtime injects short-lived tokens at call time | Agents that need authenticated API access; prevents credential exfiltration |
| 5 | **VPN/VPC peering** | Private network access to internal services | Enterprise agents operating within corporate networks |
| 6 | **Full internet** | Unrestricted outbound access | Research/exploration agents; highest risk profile |

### Design Principles

- **Default-deny**: Start with no network and open only what's needed. The pattern number should increase only with justification.
- **Credential brokering is a hard requirement** for any agent that touches production data. The sandbox must never hold long-lived credentials.
- **Proxy-mediated is the pragmatic default** for most enterprise deployments — it enables observability without the operational overhead of allowlist maintenance.

## Lifecycle Management

The runtime must treat agent execution as a managed lifecycle, not a fire-and-forget API call. Lee identifies five lifecycle operations:

| Operation | Description | Latency Expectation |
|---|---|---|
| **Cold start** | Provision new sandbox from base image | ~125 ms (Firecracker) to seconds (full VM) |
| **Warm start** | Resume from a pre-built snapshot | Sub-second from snapshot |
| **Suspend** | Pause execution and save state to disk | Milliseconds to seconds depending on memory size |
| **Resume** | Restore execution from suspended state | Sub-second from snapshot |
| **Teardown** | Destroy sandbox, archive artifacts, release resources | Seconds |

### The Async Gap Problem

Production agents encounter **async gaps** — periods of minutes, hours, or days where the agent must wait (for CI results, human review, external events) while preserving its working state. Lifecycle management must handle suspend/resume across these gaps without losing context, tool state, or filesystem modifications.

### Cost Distribution Insight

> *"For a typical agent task that takes 30 minutes: 15 seconds is model inference, 30 seconds is tool execution, and 29 minutes is waiting for the runtime to do its job. The runtime is where the time goes."* — Han Lee

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

## Web App Runtime vs Agent Runtime

Lee draws a sharp contrast between the runtime assumptions of traditional web applications and those required by autonomous agents:

| Concern | Web App Runtime | Agent Runtime |
|---|---|---|
| **User drives interaction** | Yes — user clicks, types, navigates | No — agent is autonomous, makes its own decisions |
| **Refresh fixes most things** | Yes — reload clears transient state | No — state must persist correctly across turns and interruptions |
| **Session isolation** | Nice to have — mostly for security | Mandatory — one compromised session must not reach others |
| **Network boundary** | Firewall rules at service level | Per-session network policy with credential brokering |
| **State snapshot** | Rarely needed — stateless is preferred | Foundation of debugging, evaluation, and recovery |
| **Multi-tenancy** | Request-level — requests are independent | Session-level — each session needs complete isolation |
| **Failure model** | Return error, let user retry | Survive, recover, adapt — the agent will keep going |
| **Lifetime** | Seconds (request-response) | Minutes to hours to days (async gap survival) |

> *"A web app's runtime can be sloppy because the user is the one driving and a refresh fixes most things. An agent's runtime cannot, because the agent will keep going long after a human would have stopped to ask a question."* — Han Lee

This comparison explains why agent runtimes cannot simply reuse web infrastructure primitives. Web runtimes are built for stateless, request-response, user-driven interaction. Agent runtimes require stateful, autonomous, session-level isolation with snapshot/replay capabilities. The gap between these two models is the primary source of **runtime debt** — the mismatch between what agents need and what existing cloud infrastructure provides.

## Relationship to Other Concepts

- **[[concepts/harness-engineering/agent-harness]]** — The harness + model run inside the runtime. The runtime is the execution environment; the harness is the orchestration layer within it. Han Lee's taxonomy: $H$ (harness) and $S$ (state) are runtime components. **Distinction from the execution semantics view**: the harness decides *what the agent attempts*; the runtime (as control system) decides *how execution proceeds* — managing lifecycle, tool mediation, state continuity, scheduling, events, safety, and observability independent of the harness's orchestration choices.
- **[[concepts/context-engineering|Context Engineering]]** — Context engineering manages what the model sees; the runtime defines where and how the model executes. The runtime's network boundary and filesystem shape what context is even available.
- **[[concepts/reduce-offload-isolate]]** — Anthropic/Lance Martin's three principles for stripping harness complexity. The runtime's isolation model directly impacts how well you can "isolate" sub-agent contexts.
- **[[concepts/harness-commoditization]]** — As models absorb harness features, the runtime (not the harness) may become the durable differentiator.
- **[[concepts/workflow-orchestration-frameworks]]** — Workflow frameworks describe *execution topology* (what should happen); the runtime maintains *execution continuity* (how execution proceeds). LangGraph is closer to a workflow framework; Claude Agent SDK and PI are closer to runtimes.
- [[entities/han-lee]] — Original source of the infrastructure-centric runtime framing and the runtime debt concept.
- [[entities/hanchunglee]] — Focused page on Lee's Agent Runtime analysis, isolation primitives, and core ideas from the Hidden Technical Debt series.
- **[[concepts/runtime-opinionated-sdk]]** — Claude/OpenAI Agents SDKs as mini runtimes that embed a specific execution model (reactive tool loop, runtime-owned tool orchestration, composable actors, native observability). These SDKs provide an *agent execution abstraction*, not an *LLM call abstraction* — developers configure behavior, not control flow.

## References

- Lee, H. (2026). [Hidden Technical Debt of AI Systems: Agent Runtime](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/)
- Lee, H. (2026). [A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents/)
- Cognition. (2026). [What We Learned Building Cloud Agents](https://cognition.ai/blog/what-we-learned-building-cloud-agents)
- Workman, G. (2026). [How Ramp built a full-context background coding agent on Modal](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal)
- Northflank. (2026). [Top Modal Sandboxes Alternatives for Secure AI Code Execution](https://northflank.com/blog/top-modal-sandboxes-alternatives-for-secure-ai-code-execution)
- Sculley et al. (2015). Hidden Technical Debt in Machine Learning Systems. NeurIPS.
