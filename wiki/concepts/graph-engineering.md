---
title: "Graph Engineering"
type: concept
created: 2026-07-28
updated: 2026-08-10
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
  - "[[entities/0xmovez-ai]]"
sources:
  - raw/articles/2026-07-25_akshay-pachaar_graph-engineering-clearly-explained.md
  - raw/articles/2026-07-20_movez_graph-engineering-claude-14-step.md
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

## Claude Code Implementation: The 0xMovez 14-Step Course (July 2026)

This 14-step course by [[entities/0xmovez-ai|0xMovez AI]] provides concrete Claude Code patterns for graph engineering, using **dynamic workflows** — JavaScript-based orchestration scripts where Claude writes the graph, spawns a coordinated fleet of subagents, and the coordination itself costs zero model tokens because it runs as code, not conversation.

### The 14 Steps

| Step | Name | Description |
|------|------|-------------|
| 01 | Nodes and Edges | Nodes are bounded units of work; edges carry data between them. An edge exists only when a downstream node reads an upstream node's output. |
| 02 | Linear Script = Degenerate Graph | A chain "do A, then B, then C" is a graph with no branching. Redraw it: cut edges where no data flows to expose parallelism. |
| 03 | Node Contracts (JSON Schema) | Every node gets a JSON schema contract — validated structured output enforced at the tool-call layer, so subagents retry on mismatch. |
| 04 | Edge as Data Contract | The edge is a promise about the shape of data crossing it. Plumbing (flatten, dedupe, filter) is plain JavaScript — edges are free, no agent needed. |
| 05 | Fan-Out with `parallel()` | `parallel()` spawns one subagent per thunk concurrently. A barrier waits for all thunks; failed thunks resolve to `null` instead of rejecting. |
| 06 | Fan-In at a Barrier | Gather all upstream results at once for operations that need the whole set (cross-source dedupe, ranking). Only barrier when cross-item dependency exists. |
| 07 | The Diamond Topology | Split → work → merge. Fan out to gather breadth, reduce with plain code to compress, synthesize with a final agent. The canonical shape for market scans, audits, research. |
| 08 | Conditional Routing | Router node inspects validated output; code (if/switch) picks the downstream path. Claude provides judgment at the node; code provides reliability at the edge. |
| 09 | Adversarial Verification | Verifier node tries to kill each finding before it passes downstream. Patterns: N independent skeptics, perspective-diverse lenses, judge panel synthesis. |
| 10 | Node Isolation (Worktree) | Each agent runs in its own git worktree to prevent file collisions during parallel writes. `parallel()` null-throw containment + `.filter(Boolean)` handles cascading failures. |
| 11 | Convergent Cycles (Loop-Until-Dry) | Keep spawning finders until K consecutive rounds surface nothing new. Dedupe against *everything seen* (not just confirmed) to prevent infinite rediscovery of rejected findings. |
| 12 | Model Tiering | Run repetitive, bounded nodes on cheaper models; reserve expensive tokens for nodes where real judgment lives. Override per-node with the `model` option on `agent()`. |
| 13 | Topology as Cost Lever | `pipeline()` streams items independently with no barrier; `parallel()` makes everything wait for the slowest node. Default to pipeline; barrier only when cross-set dependency demands it. |
| 14 | Self-Routing (Let Claude Draw It) | Describe the objective; Claude writes the orchestration script, decomposes the task, chooses fan-out, spawns subagents, and synthesizes. Save successful scripts to `.claude/workflows/` for re-use. |

### Key Patterns

**Node Contracts (JSON Schema Validated Output):** The `schema` option on `agent()` forces validated structured output — validation happens at the tool-call layer, so the subagent retries on mismatch instead of producing free text that requires downstream parsing. This is the difference between a node Claude can wire into a graph and one that only works when a human reads its output.

**Edges as Free Data Flow:** The reduce step between fan-out and synthesis — flatten, dedupe, filter — is just code operating on shapes returned by nodes. No agent needed. A graph where every edge is an agent is a graph paying rent on its own wiring.

**Fan-Out with `parallel()`:** Claude takes an array of thunks and spawns one subagent per thunk concurrently. It's a barrier (waits for all before returning), failed thunks resolve to `null`, and concurrency is auto-capped. This is how a graph scales to dozens or hundreds of subagents without drowning the session.

**Barrier Semantics:** Use a barrier (`parallel()` → gather) only when a stage genuinely needs every prior result together. If the middle transform has no cross-item dependency, use `pipeline()` and skip the barrier entirely.

**Diamond Topology (Split → Work → Merge):** Fan out → reduce → synthesize. One node splits the job, many nodes do the work in parallel, one node merges. The canonical form behind market scans, dependency audits, code reviews, and research reports.

**Conditional Routing:** A router node classifies, code picks the edge. Claude's judgment at the node, the script's reliability at the edge — no emergent "Claude decided to skip the audit" surprises.

**Adversarial Verification:** For each finding, spawn N independent skeptics prompted to refute it. Perspective-diverse verify: give each verifier a distinct lens (correctness, security, does-it-reproduce). Judge panel: N attempts → parallel judges → synthesize from the winner. This pattern enabled a real team to port the Bun runtime with adversarial code review baked into the loop.

**Node Isolation (Worktree):** Each agent runs in its own git worktree, does its work in a sandbox, and merges cleanly. Reach for it only when nodes actually write in parallel — it's the seatbelt for the one topology that needs it.

**Convergent Cycles (Loop-Until-Dry):** Keep spawning finders until K consecutive rounds surface nothing new. The critical detail: dedupe against *everything seen*, not just confirmed results. Otherwise rejected findings reappear every round and the loop never runs dry.

**Model Tiering:** The `model` option on `agent()` routes just that node to a cheaper model. Check `/model` before a large run, route fan-out's repetitive nodes down, keep the merge node up — this turns a token-hungry graph from expensive into economical without touching its shape.

**Topology as Cost Lever:** `pipeline()` vs `parallel()` is the single biggest lever on wall-clock time. Default to `pipeline()`; reach for a barrier only when a stage truly needs every prior result at once.

### Practical Takeaway

The article's code examples show Claude Code writing **JavaScript orchestration scripts** — the coordination costs zero model tokens because it's code, not conversation. Claude's own context never holds dozens of sources at once; each subagent carries its own, and only the final answer comes back. A saved workflow (in `.claude/workflows/`) is version-controlled, re-runnable by name, and usable by anyone who clones the repo. The `/deep-research` command shipping in Claude Code is a real graph: scope → parallel search → fetch → adversarial verify → synthesize — the exact skeleton taught in this course.

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
- [[concepts/model-switching-in-graph-workflows]] — How different models handle KV cache and context when switching between graph nodes.
- [[concepts/dynamic-workflows]] — Claude Code's JavaScript-orchestrated graph execution model where coordination costs zero tokens because routing and fan-out live in code, not conversation.

## Key Figures

- **Peter Steinberger** (@steipete) — Asked "Are we still talking loops or did we shift to graphs yet?" (Jul 18, 2026). Creator of [[entities/openclaw|OpenClaw]].
- **Hamel Husain** — Published "Loop Engineering Is Dead. Enter Graph Engineering." (Jul 18, 2026). Long-time advocate of [[concepts/harness-engineering|harness engineering]].
- **Akshay Pachaar** (@akshay_pachaar) — Wrote the definitive explainer article (1,529 bookmarks, 288K impressions).
- **0xMovez AI** (@0xMovez) — Published the 14-step Claude Code graph engineering course (Jul 20, 2026). Introduced dynamic workflow patterns for [[concepts/dynamic-workflows|JavaScript-orchestrated agent graphs]] with zero-token coordination costs.

## Sources

- [[raw/articles/2026-07-25_akshay-pachaar_graph-engineering-clearly-explained]] — Akshay Pachaar, "Graph Engineering Clearly Explained" (Jul 25, 2026). X Article. 1,529 bookmarks, 288K impressions.
- [[raw/articles/2026-07-20_movez_graph-engineering-claude-14-step]] — 0xMovez AI, "Graph Engineering with Claude: 14-Step roadmap from 0 to graph architect (Full Course)" (Jul 20, 2026). X Article. Covers dynamic workflows, `parallel()`, adversarial verification, convergent cycles, model tiering, and self-routing patterns in Claude Code.
- [Anthropic, "Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — Standing advice: find the simplest solution.
- LangGraph — Nodes and edges over shared state since Jan 2024.
- Google ADK 2.0 — Workflow runtime on the same graph pattern.
- Microsoft AutoGen — GraphFlow for multi-agent coordination.
