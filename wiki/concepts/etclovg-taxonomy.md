---
title: "ETCLOVG Taxonomy"
type: concept
created: 2026-05-28
updated: 2026-05-28
tags:
  - harness-engineering
  - ai-agents
  - taxonomy
  - survey
  - agent-architecture
  - agent-infrastructure
aliases:
  - "ETCLOVG"
  - "agent-harness-taxonomy"
  - "seven-layer-harness-taxonomy"
  - "execution-tooling-context-lifecycle-observability-verification-governance"
description: "The seven-layer taxonomy for agent harness engineering: Execution, Tooling, Context, Lifecycle, Observability, Verification, and Governance. Proposed by Li et al. (2026) as a framework for systematically mapping open-source agent infrastructure projects."
sources:
  - raw/articles/2026-05-28_li-et-al_agent-harness-engineering-survey.md
  - https://picrew.github.io/LLM-Harness/
  - https://github.com/picrew/Awesome-Agent-Harness
  - https://openreview.net/pdf?id=eONq7FdiHa
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/bitter-lesson-agent-harnesses]]"
  - "[[comparisons/agent-harnesses]]"
  - "[[comparisons/open-harness-vs-agent-framework]]"
  - "[[concepts/context-engineering]]"
---

# ETCLOVG Taxonomy

The **ETCLOVG taxonomy** is a seven-layer framework for systematically analyzing and organizing **agent harness engineering**. Proposed by Li et al. in their 2026 survey "Agent Harness Engineering: A Survey," it decomposes the agent infrastructure stack into distinct architectural layers that earlier frameworks often conflated.

## Overview

The acronym **ETCLOVG** stands for:

| Layer | Name | Role |
|-------|------|------|
| **E** | Execution environment | Where agent code runs — sandboxes, microVMs, runtimes |
| **T** | Tool interface & protocol | How capabilities are described, discovered, and invoked |
| **C** | Context & memory management | What the model can see at each step across time horizons |
| **L** | Lifecycle & orchestration | Control flow that reads and writes agent state |
| **O** | Observability & operations | Traces, costs, failures, and reliability signals |
| **V** | Verification & evaluation | Metrics, benchmarks, failure attribution, regression feedback |
| **G** | Governance & security | Permission models, hooks, constitutions, audit infrastructure |

The first four layers (E, T, C, L) form the **structural core** of a harness. The last three (O, V, G) form the **control plane** around it. Observability and Governance appear as independent layers because, in production deployments, each has its own tooling stack and is owned by a different team — a distinction that earlier six-component frameworks (which folded them into broader categories) failed to capture.

## Layer Details

### E — Execution Environment

Determines where agent code runs and what sandbox constraints bound it. Covers:

- **Managed sandboxes**: E2B, Daytona, Modal, Fly Machines
- **MicroVMs**: Firecracker, Cloud Hypervisor
- **Code-specialized runtimes**: container-based execution with pre-installed toolchains
- **Computer-use environments**: full desktop VMs, browser sandboxes
- **OS-level permission models**: seccomp, Landlock, Capsicum

Primary concern: **blast radius containment**. The execution environment is the outermost safety boundary — stronger isolation costs latency and infrastructure overhead but limits the damage from misaligned or compromised agent actions.

### T — Tool Interface & Protocol

Specifies how external capabilities are described, discovered, and invoked:

- **Protocol standards**: MCP (Model Context Protocol), A2A (Agent-to-Agent), ACP (Agent Communication Protocol)
- **Tool description & selection**: function schemas, tool-augmented training, learned tool use
- **Session management**: tool state across turns, authentication, rate limiting

Primary concern: **semantic contract enforcement**. Tools are the only interface between the model and the world — the protocol layer must ensure that the model's understanding of a tool's capabilities matches its actual behavior.

### C — Context & Memory Management

Controls what the model can see across three time horizons:

- **Short-term**: the current turn's observations, tool results, and conversation
- **Session-level**: compaction strategies, tool-result ranking, progressive disclosure
- **Persistent**: AGENTS.md, skill systems, long-term memory stores, learned preferences

Primary concern: **context window economics**. Every byte in context costs tokens and latency — the context layer decides what to keep, what to compress, and what to forget. [[concepts/context-engineering]] is the broader field this layer operationalizes.

### L — Lifecycle & Orchestration

Organizes the control flow that reads and writes state, spanning:

- **Single-agent inner loop**: ReAct-style think-act-observe-repeat
- **Multi-agent patterns**: supervisor-worker, peer-to-peer, role-playing organizations
- **Task pipelines**: issue-to-PR workflows, CI-integrated coding agents, autonomous research loops

Primary concern: **control flow ownership**. In early 2026, the field shifted from developer-authored graphs (workflow-centric) to model-driven execution (runtime-centric) as models became reliable enough to maintain execution semantics. See [[comparisons/open-harness-vs-agent-framework]] for the runtime-centric vs workflow-centric analysis.

### O — Observability & Operations

Captures traces, costs, failures, and reliability signals:

- **Tracing platforms**: Langfuse, LangSmith, OpenTelemetry
- **Agent-specific operations**: session replay, tool-call auditing, error categorization
- **Cost tracking**: per-task token budgets, model-switching strategies, unit economics
- **Unified observability**: correlating model calls, tool executions, and infrastructure metrics

Primary concern: **production visibility**. The gap between widespread observability adoption and far less common offline evaluation is a key open problem — traces should be the primary object for computing outcome scores and regression tests.

### V — Verification & Evaluation

Turns tasks and traces into evaluation, failure attribution, and regression feedback:

- **Benchmark grounding**: SWE-bench, Terminal-Bench, AgentBench, WebArena, GAIA
- **Controlled execution**: deterministic replay, ablation studies, harness-only variation
- **Multi-level judgement**: LLM-as-judge, human review gates, task-specific evals
- **Deployment-time loops**: CI-integrated eval pipelines, canary deployments, regression detection

Primary concern: **signal fidelity**. [[concepts/harness-engineering]] covers the eval-centric view in depth — this layer is the operationalization of those principles within the broader taxonomy.

### G — Governance & Security

Constrains behavior across three sub-layers:

- **Model-level**: prompt injection defenses, output filtering, refusal mechanisms
- **System-level**: permission models, lifecycle hooks (pre/post-tool), component hardening
- **Organizational-level**: declarative constitutions, audit infrastructure, compliance reporting

Primary concern: **defense in depth**. Governance cannot be a single gate — it must be layered across the model, system, and organization, with each sub-layer catching failures that escape the ones below.

## Project Mapping

The survey codes **138+ open-source projects** against ETCLOVG (primary layer assignment):

| Layer | Projects | Density |
|-------|----------|---------|
| E — Execution | 20 | High — coding, web, terminal agents all need sandboxes |
| T — Tooling | 12 | Moderate — protocol standardization is still maturing |
| C — Context | 9 | Low as standalone — often embedded in larger frameworks |
| L — Lifecycle | **47** | **Highest** — orchestration is the most crowded layer |
| O — Observability | 15 | Moderate — concentrated in commercial platforms |
| V — Verification | 21 | High — benchmarks and evals are well-represented |
| G — Governance | 14 | Low — thinner in open source, concentrated in commercial SDKs |

The corpus is maintained at [Awesome-Agent-Harness](https://github.com/picrew/Awesome-Agent-Harness) (747 stars, 220 entries, 9 categories as of May 2026) and accepts community contributions via pull requests.

## Cross-Layer Synthesis

Composing all seven layers reveals system-level dynamics that no single layer captures alone:

### Cost–Quality–Speed Trilemma
Stronger sandboxes, richer context, and deeper evaluation improve quality but cost tokens, latency, and infrastructure. Production harnesses must decide which risks justify expensive controls and which checks can run asynchronously.

### Capability–Control Tradeoff
Larger tool menus, persistent memory, and permissive sandboxes broaden task coverage but enlarge the blast radius. Capability and control form a single design axis spanning tool schemas, context policy, runtime permissions, identity, and auditability.

### Harness Coupling Problem
Harness layers are coupled in ways that make local optimization fragile. A prompt, tool, sandbox, verifier, or monitor may look beneficial in isolation while degrading the whole rollout when combined with the rest of the control loop.

## Engineering Phases (2022–2026)

The taxonomy emerges from a coherent shift in where the marginal effort of agent engineering lands:

| Phase | Years | Focus | Primary Lever |
|-------|-------|-------|--------------|
| **Prompt Engineering** | 2022–2024 | Input text optimization | Instructions, few-shot examples, reasoning templates |
| **Context Engineering** | 2025 | What the model sees per step | Retrieval, compaction, tool-result ranking, context saturation |
| **Harness Engineering** | 2026– | Full infrastructure wrapper | All seven ETCLOVG layers operationalized |

This shift is visible in the systems themselves: from ReAct loops and AutoGPT/BabyAGI exposing infrastructure failures, through tool integration and multi-agent coordination (CAMEL, ChatDev, MetaGPT), to the 2025–2026 wave where harness engineering is named as its own discipline.

## Open Problems

Five questions remain open across the taxonomy:

1. **Hardening execution environments** — Common security evaluations for prompt injection and goal misalignment; cost models across container/microVM/desktop VM/browser boundaries; portability across deployment targets.
2. **Reliable state in long-running agents** — Recasting context management as state estimation: characterizing information loss, adding provenance and staleness markers, recovering from durable artifacts.
3. **Trace-native failure diagnosis** — Making traces the primary object for computing outcome scores, trajectory quality, failure attribution, and regression tests.
4. **Standard handoffs** — Transferring not just text summaries but intent, constraints, permissions, artifacts, provenance, budget state, and unresolved decisions across agent-tool-human boundaries.
5. **Adaptive simplification** — As models improve, harnesses need mechanisms for ablating, optimizing, and simplifying themselves under joint quality, latency, cost, and risk constraints.

## Relationship to Other Frameworks

The ETCLOVG taxonomy complements but does not replace existing frameworks:

- **[[concepts/harness-engineering|Harness Engineering]]** (Hamel Husain, Addy Osmani, Viv Trivedy) — Focuses on the eval-centric, data-science aspects. ETCLOVG provides the systems/architecture counterpart, organizing the full stack into named layers.
- **[[concepts/agent-harnesses|Agent Harnesses]]** / **[[concepts/bitter-lesson-agent-harnesses|Bitter Lesson]]** (Browser Use) — Advocates minimalism. ETCLOVG identifies *which* layers are necessary and which can be simplified.
- **[[comparisons/open-harness-vs-agent-framework|Open Harness vs Framework]]** — The runtime-centric vs workflow-centric axis. ETCLOVG's Lifecycle layer (L) is where this distinction manifests most sharply.
- **[[concepts/context-engineering|Context Engineering]]** — ETCLOVG's Context layer (C) is the operationalization of context engineering within a broader architectural framework.

## Companion Resources

- **Survey paper**: "Agent Harness Engineering: A Survey" — Li et al. (2026), OpenReview
- **Project catalog**: [Awesome-Agent-Harness](https://github.com/picrew/Awesome-Agent-Harness) — 220 entries, community-maintained
- **HuggingFace dataset**: [Awesome-Agent-Harness](https://huggingface.co/Awesome-Agent-Harness)
- **Website**: [picrew.github.io/LLM-Harness](https://picrew.github.io/LLM-Harness/)
