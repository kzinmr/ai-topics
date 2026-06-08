---
title: "Data Flow and State Management in AI-Native Applications"
type: concept
created: 2026-05-27
updated: 2026-05-27
tags:
  - concept
  - ai-agents
  - state-management
  - architecture
  - context-engineering
  - memory-systems
  - orchestration
  - event-sourcing
  - durable-execution
  - methodology
  - agentic-engineering
  - data-flow
  - rag
aliases:
  - agent-state-management
  - ai-native-data-flow
  - agent-application-state
sources:
  - concepts/ai-agent-memory-middleware.md
  - concepts/memory-systems-design-patterns.md
  - comparisons/agent-memory-systems-comparison.md
  - concepts/context-engineering.md
  - concepts/context-management.md
  - concepts/agent-harness-primitives.md
  - concepts/agent-patterns.md
  - concepts/subagent-patterns.md
  - comparisons/agent-orchestration-frameworks.md
  - concepts/multi-agent-orchestration-architecture.md
  - concepts/delta-channels.md
  - concepts/agentic-rag.md
  - concepts/db9-fs-sql-pattern.md
  - concepts/agent-sandbox-patterns.md
  - comparisons/llm-integration-patterns.md
  - raw/papers/2601.19752-agentic-design-patterns.md
  - raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph.md
description: "Comprehensive overview of state categories, data flow patterns, and architectural decisions in AI-native full-stack applications — where state itself becomes the center of system design."
---

# Data Flow and State Management in AI-Native Applications

In traditional web apps, state management means form state, UI state, and server cache. In AI-native applications, **state itself becomes the center of system design** — because inference is async, non-deterministic, long-running, and multi-step. This page catalogs the state categories, architectural patterns, and storage layers that emerge when AI agents are first-class components of the application stack.

---

## State Taxonomy

### The 8-State Model

| # | State | Examples | Primary Location | Key Characteristics |
|---|-------|----------|-----------------|---------------------|
| **1** | **Client/UI State** | modal open, selected tab, input textbox, local selection, optimistic UI | Browser memory, React state | Short-lived, UI-centric, minimize duplication |
| **2** | **Server State** | document metadata, enrichment results, ontology graph, workflow status | Server DB + Cache | Persistent, shared, canonical source of truth — "what to make server truth" is the central architectural decision |
| **3** | **Session State** | current workspace, active corpus, selected ontology, temporary memory, user permissions, tenant isolation, retrieval scope, organization settings | Server session store | Identity + scope + permissions — not just login; defines the agent's operational boundary |
| **4** | **Conversation Memory** | chat history, extracted facts, entity relations, active concepts, referenced documents | DB + Memory Layer (L1-L3) | Dynamic ontology — structured as entity relations + active concepts + document references |
| **5** | **Workflow / Tool Execution State** | agent progress, tool call lifecycle (pending/running/retrying/blocked/human-review), subtask completion | Orchestration Layer | Async, partial-failure-tolerant, requires durable execution and state machine semantics |
| **6** | **Retrieval State** | retrieved context, vector search results, document references, RAG artifacts | Transient / Runtime (with optional cache) | Transient execution state that shapes agent reasoning — what was retrieved shapes what is reasoned |
| **7** | **Episodic / Semantic Memory** | long-term facts, user preferences, learned patterns, organizational knowledge, procedural skills | L2/L3 persistent storage | Accumulates across sessions; requires distillation, dedup, freshness management |
| **8** | **Agent Identity / Persona State** | system prompts, behavioral guidelines, skill registry, tool definitions, harness configuration | `SOUL.md`, `CLAUDE.md`, `AGENTS.md`, config files | The "what the agent is" — distinct from memory (what the agent knows) |

### Relationship to Non-AI Apps

```
Traditional Web App                AI-Native Agent App
┌──────────────┐                   ┌──────────────────────────┐
│ Form State   │                   │ Client/UI State           │
│ UI State     │    expands to     │ Server State              │
│ Server Cache │ ───────────────→  │ Session State             │
└──────────────┘                   │ Conversation Memory       │
                                   │ Workflow/Tool Exec State  │
                                   │ Retrieval State           │
                                   │ Episodic/Semantic Memory  │
                                   │ Agent Identity State      │
                                   └──────────────────────────┘
```

Why this explosion? Three factors: **async** (inference takes seconds to minutes), **non-deterministic** (same input ≠ same output), and **multi-step** (agents chain dozens of tool calls).

---

## Part 1: Client/Server State Separation

### Where is the source of truth?

In AI-native apps, the question "what lives on the server vs. client" is more nuanced because:

1. **Inference is slow** — partial responses and streaming are the norm
2. **Workflows are async** — user triggers action, agent runs in background
3. **Context is expensive** — every token in the context window costs money

```
┌── Client ──────────────────────────────────────┐
│  UI State (ephemeral, optimistic)               │
│  Streaming buffer (partial LLM output)          │
│  Local workspace (current doc, active view)     │
└─────────────────────────────────────────────────┘
         ↕ streaming / sync
┌── Server (Truth) ───────────────────────────────┐
│  Canonical document state                       │
│  Workflow state machine (pending→complete)      │
│  Ontology / knowledge graph                     │
│  Multi-tenant session data                      │
│  Retrieval index (vector + FTS)                 │
└─────────────────────────────────────────────────┘
```

**Key principle**: Server owns the canonical state. Client maintains optimistic projections. Rollback when server disagrees.

### Optimistic Updates

Critical for AI apps because latency is heavy (inference: seconds to minutes):

```
UI: tag appears immediately (optimistic)
    ↓
Backend: validates + persists
    ↓
    success → confirm
    failure → rollback UI + notify
```

Worker & processing state handling relies on **eventual consistency** patterns — async background jobs, retry with backoff, idempotent operations.

---

## Part 2: Streaming Response Architecture

### Token Streaming

The completion pipeline streams tokens, not full responses:

```
LLM → token → token → token → ... → [DONE]
         ↓        ↓        ↓
      UI renders incrementally (React Suspense, streaming SSR)
```

**UI patterns**: React Server Components + streaming SSR + `<Suspense>` boundaries let the UI render tokens as they arrive rather than showing a spinner for 30 seconds.

### Workflow Progress Events

Beyond token streaming, agents produce **structured progress events**:

```
Event: step.started  → tool.called → tool.result → step.completed
                                                      ↓
                                          UI: progress bar, step log
```

This is where [[concepts/delta-channels|Delta Channels]] become critical — writing full state snapshots at every step is unsustainable for agents running thousands of steps. DeltaChannel writes only incremental updates, with periodic full snapshots (every K steps).

---

## Part 3: Caching Architecture

### Beyond API Response Cache

AI apps cache **derived artifacts**, not just HTTP responses:

| Cache Type | What | Where | Invalidation Trigger |
|------------|------|-------|---------------------|
| **Prompt Cache** | Static system prompt prefix | Anthropic/OpenAI server-side | Prompt version change |
| **Retrieval Cache** | Vector search results for query | Redis / DB | Document index update |
| **Embedding Cache** | Pre-computed embeddings | Vector DB | Source document change |
| **Tool Result Cache** | Deterministic tool outputs | Content-addressed store | Tool version change |
| **Ontology Expansion Cache** | Derived entity relations | Graph DB | Source document update |

**Prompt caching** is the most important production metric per Manus — **cache hit rate** directly determines cost. A more expensive model with high cache hit rate can be cheaper than a lower-cost model without caching.

> See: [[concepts/context-engineering|Context Engineering]], [[concepts/prompt-caching|Prompt Caching]]

### The Content-Addressed Cache Pattern (ActiveGraph)

[[raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph|ActiveGraph]]'s deterministic replay uses a content-addressed cache:

```
Replay event → check cache(hash(prompt+params))
    ├── hit → return stored response (no API call)
    └── miss → call model/tool, store response, continue
```

This guarantees **byte-identical state reconstruction** from any event log — a property retrieval-and-summarization systems cannot provide.

---

## Part 4: Memory Architecture — The 3-Layer Model

Agent memory is the most architecturally rich dimension. The wiki organizes it across three layers:

### L1: In-Context (Inference-Time Working Memory)

| Property | Detail |
|----------|--------|
| **Scope** | Single inference step |
| **Capacity** | 128K–2M tokens (model dependent) |
| **Persistence** | Volatile — cleared after response |
| **Cost** | Highest per-token (KV cache memory + attention compute) |
| **Strategy** | [[concepts/context-engineering|Context Engineering]] — Write/Select/Compress/Isolate |

> "Context is a finite, precious resource. Every token that enters the window should earn its place." — Anthropic Engineering

### L2: Local File (Session Persistence)

| Property | Detail |
|----------|--------|
| **Scope** | Single agent, multi-session |
| **Format** | `CLAUDE.md`, `AGENTS.md`, `MEMORY.md`, `SKILL.md`, `.agent/` directory |
| **Versioning** | Git-native |
| **Philosophy** | Stateless sessions + JIT retrieval — load only what's needed when needed |

This is the **industry converging pattern** (see [[concepts/memory-systems-design-patterns|Memory Systems Design Patterns]]): Anthropic, Cognition, and Vajra all converge on file-based memory. OpenAI's ChatGPT remains the outlier with proprietary database storage.

### L3: Cloud Storage (Multi-Agent Sharing)

| Technology | Approach | Best For |
|------------|----------|----------|
| **S3 Files** | POSIX mount + Stage-and-Commit model | Multi-agent shared workspace |
| **Tigris** | Global edge distribution, zero egress, fork capability | Globally distributed agent memory |
| **LLMFS** | Memory Query Language (MQL), knowledge graph, FUSE | Structured knowledge persistence |
| **db9** | Filesystem + PostgreSQL unification (fs9 extension) | Single agent to small team RAG pipeline |
| **ChromaFS** | Virtual filesystem on vector DB — "agents need the illusion of a filesystem, not a real one" | Read-only documentation agent at scale (30K+ convos/day) |
| **OPFS** | Browser Origin Private File System | In-browser agents |
| **Zero Disk** | Full separation — S3 as direct backend | Large-scale DB vendors |

> See: [[concepts/ai-agent-memory-middleware|AI Agent Memory Middleware]], [[concepts/db9-fs-sql-pattern|db9 FS+SQL Pattern]]

### Memory Architecture Types (Bustamante)

Nicolas Bustamante's 3-type classification:

| Type | Description | Example |
|------|-------------|---------|
| **Bounded Snapshot** | Memory frozen at session start, prefix cache optimized, capacity-limited | Hermes Agent |
| **Typed Live Writes** | Directly writes typed Markdown during session, age-aware reminders | Claude Code |
| **Two-Phase Async Pipeline** | Async: extraction (small model) → integration (large model) | Codex CLI |
| _(Hybrid Search + Flush)_ | Doesn't fully fit any type — hybrid search + pre-compaction flush | OpenClaw |

> See: [[comparisons/agent-memory-systems-comparison|Agent Memory Systems Comparison]]

### Memory Scaling (Databricks, April 2026)

A third axis of agent improvement beyond parametric and inference-time scaling:

| Axis | Mechanism | Limitation |
|------|-----------|------------|
| **Parametric Scaling** | Model weight updates | High compute cost, catastrophic forgetting |
| **Inference-Time Scaling** | Chain-of-thought reasoning | Context window limits, "overthinking" |
| **Memory Scaling** | Performance through external memory accumulation | Quality management, freshness |

> "A smaller model with a rich memory store can outperform a larger model with less memory." — Databricks Engineering Blog

Memory taxonomy per Databricks: **Episodic** (raw logs), **Semantic** (generalized facts), **Personal** (user preferences), **Organizational** (shared conventions).

---

## Part 5: Conversation Memory — Dynamic Ontology

Conversation state is effectively a **dynamic ontology** built during agent execution:

| Memory Type | Content | Storage Pattern |
|-------------|---------|-----------------|
| **Short-term** | Recent messages (sliding window) | In-context (L1) |
| **Semantic** | Extracted facts, entity relations | L2 files / L3 DB |
| **Procedural** | Workflow state, task progress | Orchestration layer |
| **Retrieval-linked** | Document references with attribution | L2 + L3 |

See [[concepts/context-engineering|Context Engineering]] for the **Write / Select / Compress / Isolate** strategy taxonomy by Lance Martin.

---

## Part 6: Workflow & Tool Execution State

### The Tool Call Lifecycle

Tool calls in agent systems are not simple request/response — they have complex state machines:

```
pending → running → success
                  → partial_success
                  → failed → retrying → success
                                      → failed → blocked
                                               → human_review_required
```

This requires **durable execution** infrastructure:

| Pattern | How It Works | Key Feature |
|---------|-------------|-------------|
| **[[concepts/delta-channels|Delta Channels]]** (LangGraph) | Write only incremental deltas, periodic full snapshots | Resume bounded to K steps, not full session |
| **[[raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph|ActiveGraph]]** (Yohei Nakajima) | Append-only event log as source of truth; graph as deterministic projection | Deterministic replay, cheap forking, end-to-end lineage |
| **Context Reset** (Anthropic) | New agent launch over in-conversation summarization | Clean context, reproducible |
| **Pre-Compaction Flush** (OpenClaw) | Auto memory flush at ~80% context usage, silent turn | Prevents state loss during compaction |

### ActiveGraph: The Log IS the Agent

The most radical architectural proposal in the wiki:

> "What if the rules, tool calls, and content were all events in a single append-only log, and the agent's behavior were just reactions that fire when that log grows and write new events back into it?"

```
Event Types: pack.loaded → goal.created → behavior.started 
           → object.created → llm.request → llm.response
           → tool.called → tool.result → object.patched

Behaviors are reactions:
  Subscription: event type + predicate + graph-shape pattern (Cypher)
  Body: function | class | LLM-backed routine | relation-behavior
```

Three unique properties:
1. **Deterministic replay** — byte-identical reconstruction from any log
2. **Cheap forking** — branch at any event without re-executing shared prefix
3. **End-to-end lineage** — trace from goal to individual model call

No orchestrator — coordination emerges from the shared graph.

---

## Part 7: Agent Patterns — From Single to Multi-Agent

### The 5 Subsystem Model (System-Theoretic)

From [[raw/papers/2601.19752-agentic-design-patterns|Agentic Design Patterns (Dao et al., 2026)]]:

```
┌──────────────────────────────────────────┐
│ 5. Learning & Adaptation (outer shell)   │
│    ├─ 4. Inter-Agent Communication       │
│    │   ├─ 2. Perception & Grounding      │
│    │   │   ├─ 1. Reasoning & World Model │ ← Innermost core
│    │   │   ├─ 3. Action Execution        │
│    │   ├─────────────────────────────────│
│    ├─────────────────────────────────────│
└──────────────────────────────────────────┘
```

Mapped to 12 Agentic Design Patterns (ADPs):
- **Foundational**: Integrator, Retriever, Recorder
- **Cognitive**: Selector, Planner, Deliberator
- **Execution**: Executor, Tool Use, Orchestrator, Observer
- **Adaptive**: Reflector, Aligner, Communicator

### Subagent Patterns — 5 Levels of Coordination

From [[concepts/subagent-patterns|Subagent Patterns]] (Philipp Schmid, May 2026):

| Pattern | Tools | Main Role | Lifespan | Model Required |
|---------|-------|-----------|----------|----------------|
| **1. Inline Tool** | `call_agent` | Caller | Single task | Small/cheap |
| **2. Fan-Out** | `spawn`, `wait` | Dispatcher | Single task | Small/cheap |
| **3. Agent Pool** | `spawn`, `send`, `wait`, `list`, `kill` | Coordinator | Multi-turn | Mid-range |
| **4. Teams** | All + cross-agent `send` | Supervisor | Persistent | Frontier (all members) |
| **5. Orchestrator-Worker** | `spawn_subagent`, `Memory`, parallel tools | Orchestrator | Multi-turn | Frontier orchestrator |

**Key finding**: Anthropic's Claude Research achieved **90.2% performance improvement** over single agent via Orchestrator-Worker pattern. Token usage explains 80% of performance variance.

### Multi-Agent Coordination

From [[comparisons/agent-orchestration-frameworks|Agent Orchestration Frameworks]]:

| Pattern | Description | Best For |
|---------|-------------|----------|
| **Hierarchical** | Manager decomposes, workers execute, manager synthesizes | Structured workflows |
| **Peer-to-Peer** | Direct agent-to-agent negotiation, no central coordinator | Open-ended problem solving |
| **Sequential Pipeline** | Fixed order processing chain | Linear workflows |
| **Debate/Consensus** | Multiple agents generate → debate → converge | High-stakes decisions |
| **Swarm (Emergent)** | Large number of simple agents, minimal coordination | Exploration, search, optimization |

---

## Part 8: Context Management — The 4-Strategy Taxonomy

From [[concepts/context-engineering|Context Engineering]] (Lance Martin, Anthropic):

```
┌─────────────────────────────────────────────────────────┐
│                 CONTEXT ENGINEERING                       │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│   │  WRITE   │  │  SELECT  │  │ COMPRESS │  │ ISOLATE  ││
│   │  Save    │  │  Pull    │  │  Keep    │  │  Split   ││
│   │ context  │  │ context  │  │ relevant │  │ context  ││
│   │ outside  │  │ into the │  │ tokens   │  │ across   ││
│   │ the      │  │ window   │  │ only     │  │ agents   ││
│   │ window   │  │          │  │          │  │          ││
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘│
└─────────────────────────────────────────────────────────┘
```

| Strategy | How | Examples |
|----------|-----|----------|
| **Write** | Scratchpads, memories, structured notes | `MEMORY.md`, `.agent/`, Anthropic research plan files |
| **Select** | JIT retrieval, tool RAG, progressive disclosure | glob/grep/read, skill index → skill load |
| **Compress** | Summarization, trimming, compaction | Claude Code 95% auto-compact, Cognition fine-tuned summarizer |
| **Isolate** | Sub-agents, sandboxes, filesystem communication | Orchestrator-Worker, Ralph Loop, ChromaFS |

---

## Part 9: Storage Architecture Spectrum

Where does an agent's state live? A spectrum from minimal to maximal:

```
Integration ←──────────────────────────────────────→ Separation
(compute + data together)                (compute and data separated)

OPFS    db9     S3 Files/Tigris    Zero Disk
 │       │            │                │
 │       │            │                └─ Full S3 backend
 │       │            └─ Cloud POSIX mount
 │       └─ PG + fs9 in one process
 └─ Browser-local private FS
```

| Architecture | Scale | Data Volume | Complexity | Wiki Reference |
|-------------|-------|-------------|------------|----------------|
| **OPFS** | Browser agent | KB-MB | Low | [[concepts/ai-agent-memory-middleware#OPFS]] |
| **L2 (CLAUDE.md + Git)** | Individual session | KB | Minimal | [[concepts/memory-systems-design-patterns]] |
| **db9** | Single agent / small team | MB-GB | Low | [[concepts/db9-fs-sql-pattern]] |
| **S3 Files / Tigris** | Multi-agent team | GB-TB | Medium | [[concepts/ai-agent-memory-middleware]] |
| **Zero Disk** | Enterprise / DB vendor | TB+ | High | [[concepts/zero-disk-architecture]] |

---

## Part 10: Retrieval State as Execution State

Retrieval is not just "fetch data" — it shapes agent reasoning. From [[concepts/agentic-rag|Agentic RAG]]:

```
Naïve RAG → Advanced RAG → Modular RAG → Graph RAG → Agentic RAG
  (keywords)  (dense+rerank)  (hybrid+tools)  (graph+relations)  (autonomous agents)
```

Retrieval state flows through 5 agentic patterns:

| Pattern | Description | State Impact |
|---------|-------------|--------------|
| **Reflection** | Self-evaluate and refine queries | Iterative query state |
| **Planning** | Decompose into sub-queries | Multi-step retrieval plan |
| **Tool Use** | Use multiple retrieval strategies | Diverse retrieval artifacts |
| **Multi-Agent** | Specialized retrieval agents | Parallel retrieval state |

The Hamel Husain P5 principle: **"The Map is Not the Territory"** — create multiple specialized representations (maps) of the same data instead of searching for one perfect embedding. Route queries to the right map based on inferred user intent.

---

## Part 11: LLM Integration Paradigms — Who Controls the Data Flow?

From [[comparisons/llm-integration-patterns|LLM Integration Patterns]]:

| Paradigm | Control Subject | Optimization Timing | State Management |
|----------|----------------|---------------------|-----------------|
| **Orchestration** (LangChain) | Developer (code) | None (manual) | Explicit, developer-managed |
| **Declarative** (DSPy) | Optimizer (compile-time) | Compile-time (Teleprompter) | Model-independent signatures |
| **Recursive** (RLMs) | LM itself (REPL) | Inference-time (self-adaptation) | External environment, unlimited context |
| **Agentic** (Anthropic, OpenAI) | Orchestrator + LM | Runtime (tool selection) | Fixed + tool outputs |
| **Genetic** (GEPA) | Evolutionary algorithm | Inter-generational | Evolved prompts |

> Evolution direction: **Full developer control → Optimizer control → LM self-control**

---

## Part 12: Agent Identity — Separating SOUL from Memory

A critical architectural decision: distinguishing **what the agent is** from **what the agent knows**.

| Layer | Content | Example | Storage |
|-------|---------|---------|---------|
| **SOUL / Identity** | Persona, behavioral guidelines, system prompt | `SOUL.md`, system prompt slot #1 | Config, version-controlled |
| **MEMORY** | Accumulated facts, preferences, patterns | `MEMORY.md`, `USER.md` | Filesystem (L2) |
| **SKILLS** | Reusable procedural knowledge | `~/.hermes/skills/` | Filesystem, auto-generated |
| **SESSION** | Current execution context | Conversation history SQLite + JSONL | L2/L3 |

Hermes Agent exemplifies this separation with slot-based prompt assembly:
- Slot #1: `SOUL.md` (persona, static)
- Slot #2: `MEMORY.md` + `USER.md` (bounded snapshot, prefix-cache optimized)
- Slot #3: Skills index (progressive disclosure — titles only, load on demand)
- Slot #4: Conversation history (FTS5 search, not full load)

> See: [[comparisons/agent-memory-systems-comparison|Agent Memory Systems Comparison]]

---

## Part 13: Sandbox Architecture — Where Does the Agent Run?

From [[concepts/agent-sandbox-patterns|Agent Sandbox Patterns]]:

### Pattern 1: Isolate the Tool
Agent runs on main infra. Only dangerous operations run in sandbox. Simpler, but agent shares secrets.

### Pattern 2: Isolate the Agent (Production Standard)
Entire agent runs in sandbox with **zero secrets**. Communicates through control plane. Browser Use migrated to this pattern.

```
┌── Sandbox (Zero Secrets) ──────┐     ┌── Control Plane ────────────┐
│  Agent process                  │     │  LLM Proxy (stores history) │
│  - SESSION_TOKEN only           │ ←→  │  Auth (bearer token)        │
│  - Files in /workspace          │     │  File Sync (presigned URLs) │
│  - No AWS/DB credentials        │     │  Horizontal scaling         │
└─────────────────────────────────┘     └─────────────────────────────┘
```

---

## Part 14: Design Decision Framework

### What to Ask When Designing State for an AI App

| Decision | Options | Tradeoff |
|----------|---------|----------|
| **Memory architecture** | Bounded Snapshot vs. Typed Live Writes vs. Async Pipeline | Prefix cache efficiency vs. freshness vs. automation |
| **Context strategy** | Full pre-load vs. JIT retrieval | Simplicity vs. token efficiency |
| **Session model** | Stateless (context reset) vs. Stateful (compaction) | Reproducibility vs. continuity |
| **Storage layer** | L2 filesystem vs. L3 cloud | Simplicity vs. multi-agent sharing |
| **Orchestration** | Single agent vs. Orchestrator-Worker vs. Teams | Cost vs. capability |
| **Durable execution** | Delta Channels vs. Event Sourcing (ActiveGraph) vs. Context Reset | Infrastructure complexity vs. replay/fork capability |
| **Sandbox** | Isolate tool vs. Isolate agent | Simplicity vs. security |

### The Bitter Lesson for State

> "The best way to build agent memory is not to build one at all. Stateless agents that receive full context every time are more reliable than stateful agents that try to remember." — Shlok Khemani

**Counterpoint**: Databricks' Memory Scaling thesis — "the differentiator for enterprise agents will be what memory they have accumulated rather than which model they call."

The synthesis: **start stateless, add memory only where evals prove it helps**.

---

## Related Pages

### Core Concepts
- [[concepts/ai-agent-memory-middleware|AI Agent Memory Middleware]] — L1-L3 storage architecture, S3 Files, Tigris, LLMFS, ChromaFS, OPFS
- [[concepts/memory-systems-design-patterns|Memory Systems Design Patterns]] — Anthropic vs OpenAI vs Cognition
- [[concepts/context-engineering|Context Engineering]] — Write/Select/Compress/Isolate taxonomy
- [[concepts/context-management|Context Management]] — Context window as finite resource
- [[concepts/agent-harness-primitives|Agent Harness Primitives]] — 6 core primitives of agent infrastructure
- [[concepts/delta-channels|Delta Channels]] — Incremental checkpoint storage for long-running agents
- [[concepts/db9-fs-sql-pattern|db9: FS + SQL Pattern]] — PostgreSQL-first agent architecture
- [[concepts/agentic-rag|Agentic RAG]] — Retrieval state as execution state

### Comparisons
- [[comparisons/agent-memory-systems-comparison|Agent Memory Systems Comparison]] — OpenClaw vs Claude Code vs Codex vs Hermes
- [[comparisons/agent-orchestration-frameworks|Agent Orchestration Frameworks]] — LangGraph, CrewAI, AutoGen, Semantic Kernel
- [[comparisons/llm-integration-patterns|LLM Integration Patterns]] — 5 paradigms for LLM integration

### Agent Patterns
- [[concepts/agent-patterns|Agent Patterns]] — Full catalog of agent architecture patterns
- [[concepts/subagent-patterns|Subagent Patterns]] — 4-5 levels of agent-to-agent coordination
- [[concepts/multi-agent-orchestration-architecture|Multi-Agent Orchestration Architecture]] — Roles, layers, responsibilities
- [[concepts/agent-sandbox-patterns|Agent Sandbox Patterns]] — Isolate the tool vs. isolate the agent

### Papers
- [[raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph|ActiveGraph]] — Event-sourced reactive graphs
- [[raw/papers/2601.19752-agentic-design-patterns|Agentic Design Patterns]] — 5 subsystems + 12 ADPs

### Engineering Guides
- [[concepts/agent-engineering-guide-2026|Agent Engineering Guide 2026]] — What to learn, build, and skip
