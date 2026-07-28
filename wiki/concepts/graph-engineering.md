---
title: "Graph Engineering"
type: concept
created: 2026-07-28
updated: 2026-07-28
tags:
  - concept
  - ai-agents
  - multi-agent
  - orchestration
  - agent-architecture
  - agent-coordination
  - coding-agents
  - harness-engineering
  - langchain
aliases:
  - graph-engineering
  - agent-graph
  - multi-loop-coordination
related:
  - "[[concepts/loop-engineering]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agent-loop-orchestration]]"
  - "[[concepts/harness-engineering/agentic-loop]]"
  - "[[entities/hamel-husain]]"
  - "[[entities/peter-steinberger]]"
sources:
  - raw/articles/2026-07-25_akshay-pachaar_graph-engineering-clearly-explained.md
  - https://x.com/akshay_pachaar/status/2081089131808243999
---

# Graph Engineering

**Graph Engineering** is the coordination layer across multiple [[concepts/loop-engineering|agent loops]] — governing what runs when, in what order, and who checks whom. A graph connects loops via **nodes** (units of work), **edges** (execution order and conditional routing), and **shared state** (data flowing between nodes). The term was popularized in mid-2026 when Peter Steinberger and Hamel Husain jokingly asked whether the field had "shifted from loops to graphs," but the underlying pattern predates the name: LangGraph shipped nodes-and-edges-over-shared-state in January 2024, Microsoft AutoGen has GraphFlow, and Google ADK 2.0's workflow runtime is built on the same idea.

## Core Abstraction

A graph is three things:

| Component | Role | Examples |
|-----------|------|----------|
| **Nodes** | Units of work | Agent, model call, deterministic function, tool call, human approval gate |
| **Edges** | Execution flow | Sequential, parallel, conditional (based on node output) |
| **State** | Shared data object | Typed schema flowing along edges; every node reads from and writes to it |

The canonical starter graph: researcher → writer → reviewer. If review passes, run ends. If fails, edge loops back to writer. Three nodes, four edges, one of which is a loop.

**Key insight:** A single agent loop is a one-node graph with a self-edge. Graphs don't replace loops — they connect and govern them.

## The Five-Layer Stack

Graph engineering sits atop a stack where each layer wraps the one below:

| Layer | What it minds | Core question |
|-------|---------------|---------------|
| **Prompt engineering** | Words sent to the model | What should I tell the model? |
| **Context engineering** | Everything in the window | What to retrieve, summarize, clear? |
| **Harness engineering** | Code around one run | Tools, actions, completion criteria |
| **Loop engineering** | Autonomous cycle | Self-correcting execution loop |
| **Graph engineering** | Coordination across loops | What runs when, in what order, who checks whom? |

Skip a lower layer and the graph fails in a more elaborate way. A graph of weak loops is just distributed failure.

## Four Hard Problems

### 1. Knowing when a node deserves to exist

The most common failure: turning "summarize this PDF" into a five-node graph. A node earns its place only if it represents a **real specialty** — different model, different toolset, or genuinely separate role (e.g., read-only reviewer). Steps you could inline into an existing loop are not nodes.

> If you can't draw the graph on a napkin, it's too complex. If collapsing two nodes into one loses nothing, they were never two nodes.

### 2. Keeping shared state clean

In a loop, the failure mode is [[concepts/harness-engineering/system-architecture/context-anxiety|context rot]]. In a graph, the same disease moves into shared state. A sloppy write in node 2 becomes a confident input for node 5.

**Mitigations:**
- Typed state schema
- Explicit write-access rules per node
- Checkpoint between nodes for replay
- Side-effect-bearing nodes must be idempotent (safe to re-execute after checkpoint replay)

### 3. Routing you can trust

If a model decides the route, you get flexibility and instability. Google's ADK 2.0 design rule: **deterministic code controls predictable routing**; models handle only steps requiring genuine judgment. Route with code wherever the condition is checkable.

### 4. Agents agreeing with each other

Multiple agents on the same base model, reading the same flawed context, will agree with each other. Models measurably prefer their own outputs — "organized nonsense" at industrial scale.

**Fix:** Reviewer node on a **different model**, with **fresh context** (not the full conversation), anchored to **external evidence** (tests that ran, code that compiled). Cognition's Devin setup: several agents read and weigh in, but only **one** agent is allowed to change anything. Reading is safe in parallel; writing is where damage happens.

## When NOT to use graphs

Most of the time. Anthropic's numbers: single agent ≈ 4x chat tokens; multi-agent ≈ 15x. Every node multiplies cost.

**Use graphs when:**
- Work splits into genuine specialties
- Parallel fan-out and join are needed
- Different models per step
- Failure isolation and auditable routing required

**Stay in the loop when:**
- Straightforward loop with tools suffices
- LangGraph's own guidance: "If your agent is a straightforward loop with tools, LangGraph is overkill"

Anthropic's multi-agent research system outperformed single Opus by 90.2% on internal research eval (research fans out naturally), but their standing advice from *Building Effective Agents* remains: find the simplest solution; add complexity only when the task demands it.

## Getting Started

1. **Master a single loop first** — with brakes, completion check, and critic
2. **Draw on paper** — challenge every node to justify its existence
3. **Define state schema and write access up front** — state drift is how graphs rot
4. **Different-model reviewer** — fresh context, anchored to external evidence
5. **Budget caps per node** — many loops spend tokens in parallel; a weak verifier burns money concurrently

## Relationship to Adjacent Concepts

- [[concepts/loop-engineering]] — The autonomous cycle that drives one agent toward a goal. Graph engineering coordinates multiple loops.
- [[concepts/harness-engineering]] — The code around one model run. Each loop needs a good harness; each harness call is a context problem.
- [[concepts/agent-loop-orchestration]] — Technical architecture of the think-act-evaluate cycle. Graph engineering is the coordination layer above.
- [[concepts/harness-engineering/agentic-loop]] — The ReAct/ralph loop pattern. A graph's node is often a single loop instance.
- [[concepts/compound-engineering-loop]] — Related framework for compound engineering loops.

## Key Figures

- **Peter Steinberger** (@steipete) — Asked "Are we still talking loops or did we shift to graphs yet?" (Jul 18, 2026). Creator of [[entities/openclaw|OpenClaw]].
- **Hamel Husain** — Published "Loop Engineering Is Dead. Enter Graph Engineering." (Jul 18, 2026). Long-time advocate of [[concepts/harness-engineering|harness engineering]].
- **Akshay Pachaar** (@akshay_pachaar) — Wrote the definitive explainer article (1,529 bookmarks, 288K impressions).

## Sources

- [[raw/articles/2026-07-25_akshay-pachaar_graph-engineering-clearly-explained]] — Akshay Pachaar, "Graph Engineering Clearly Explained" (Jul 25, 2026). X Article. 1,529 bookmarks, 288K impressions.
- [Anthropic, "Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — Standing advice: find the simplest solution.
- LangGraph — Nodes and edges over shared state since Jan 2024.
- Google ADK 2.0 — Workflow runtime on the same graph pattern.
- Microsoft AutoGen — GraphFlow for multi-agent coordination.
