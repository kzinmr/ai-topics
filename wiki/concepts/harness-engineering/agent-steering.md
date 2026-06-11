---
title: Agent Steering
created: 2026-05-27
updated: 2026-05-27
type: concept
tags:
  - ai-agents
  - search
  - harness-engineering
  - coding-agents
aliases:
  - agent-guidance
  - agent-control-patterns
  - steering-lost-agents
  - harness-control-loop
sources:
  - raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents.md
  - raw/articles/2026-06-04_softwaredoug_exhaustive-search-beam-search.md
---

# Agent Steering

> Agent steering is the discipline of directing LLM agents toward quality outcomes through harness design, validation loops, priming, tool guards, and subagent delegation — without requiring the agent itself to be "smart" about steering.

## Definition

**Agent steering** encompasses the patterns and techniques used to guide an LLM agent's behavior within a tool-calling loop. The core insight, articulated by Doug Turnbull in his "Cheat at Search" series, is that **the agent picks the tools, but the developer controls how tools respond** — and this asymmetry is the primary lever for steering.

The steering metaphor uses a "carrot and stick" model:
- **Carrot 🥕**: Priming, few-shot examples, query expansion, skills lookup — give the agent better starting points
- **Stick 🏒**: Tool guards, validation rules, LLM judges — redirect the agent when it goes off course

## The Two-Loop Architecture

The foundational architecture for agent steering is a **dual-loop system**:

```
┌─────────────────────────────────────────┐
│         Harness (Control Plane)          │
│  ┌───────────────────────────────────┐   │
│  │      Agentic Loop                 │   │
│  │  Agent ⇄ Tool Calls ⇄ Results    │   │
│  └───────────────────────────────────┘   │
│  ↑ evaluate response, force retry,       │
│    stop agent, inject feedback           │
└─────────────────────────────────────────┘
```

- **Agentic Loop (inner):** The standard tool-calling loop — the agent decides which tools to call and in what order
- **Harness (outer):** A control plane that evaluates the agent's output, can force a retry, stop execution, or inject corrective feedback as user messages

The harness has access to `agent_state` — shared state that tools can also inspect and respond to. This enables tools to return context-aware errors: *"Error: you're calling me illegally because you need to do X first"*

> **Key principle:** The harness does more work than the model in any production agent. The model picks the next action; the harness validates it, runs it in a sandbox, captures output, decides what to feed back, and decides when to stop. See [[concepts/harness-engineering]] for the broader discipline.

## Who Controls What

| Layer | Controls | Examples |
|-------|----------|----------|
| **Agent** | Which tools to call, order/frequency, final output (subject to override) | Tool selection, query formulation |
| **Developer (Harness)** | System prompt, tools provided, tool response content, validation feedback, agent_state | Error messages, "try again" prompts, guard disallowances |
| **Human / External Judge** | User validation, quality feedback, corrective messages | "Relevant results look like…", "No, not that" |

The critical insight: **tool responses ARE prompt engineering**. When a tool returns `"You've already searched this area"`, that's not just an error — it's a steering signal that guides the agent toward unexplored territory.

## Steering Patterns

### 1. The Ralph Loop (Simple Retry)

The simplest steering pattern: just tell the agent to try again, up to N times.

```python
max_loops = 10
for _ in range(max_loops):
    resp = agent.loop(inputs=inputs, agent_state=agent_state)
    inputs.append({"role": "user", "content": "Try to find better results!"})
```

**When to use:** Early prototyping. Cheap, easy, surprisingly effective for basic convergence.

### 2. Rule-Based Validation

Force a retry when objective criteria aren't met. The validator returns `True` (pass) or a string (fail, with a message injected as user feedback).

```python
def validate_min_results(resp, min_results=10):
    results = getattr(resp, "ranked_results", None) if resp else None
    if len(results or []) >= min_results:
        return True
    return "Please return at least 10 results to give the user a good variety."
```

**When to use:** When you have clear, objective quality criteria (count thresholds, format requirements, required fields).

### 3. LLM-as-Judge Validation

A dedicated LLM judges the agent's output quality and returns corrective user messages.

```python
msg = validate_llm_judge(query, resp)
if msg is not True:
    inputs.append({"role": "user", "content": msg})
    continue  # Retry the agentic loop
```

The judge behaves like a user reacting: *"These aren't relevant…"*, *"Hmm let's try over here then"*. The LLM judge steers like a human would — through natural language feedback injected as user messages.

**Why user-feedback works:** Models are trained to serve users. User-like messages leverage this training bias more effectively than system-level instructions.

### 4. Quality Model Integration (Reranker / CrossEncoder)

Three architectural options for incorporating ranking quality models:

| Option | Pros | Cons |
|--------|------|------|
| **Reranker inside search tool** | Black-box; agent unaware of complexity | Agent still needs feedback to guide next steps |
| **Reranker as separate tool** | Agent can use it when helpful | Hard to enforce systematic calling |
| **Evaluate in response** | Guides agent using simpler retrieval; emulates human feedback | Requires harness-level integration |

> *"Don't trust the agent to call the tool systematically like code — let code do that!"*

The "evaluate in response" pattern is preferred: use the harness (code) to run the quality model and inject results as feedback, rather than giving the agent a tool it may or may not call.

### 5. Priming (Starting Position Optimization)

**Problem:** Agents waste tokens exploring from poor initial states.

**Few-shot examples in system prompt:** Add concrete relevance examples to prime the agent's judgment:
```
User Query: wood coffee table set by storage
Product Name: stuber 3 piece coffee table set
Relevance: Partial
```

**Query expansion:** Use an LLM to interpret the user's query into a richer formulation before the agent starts:
```python
def interpret_query(keywords):
    # "red shoes" → "I am looking for red-colored footwear, preferably athletic or casual style..."
```

**Agentic skills / query plan:** Maintain a vector DB of "how to search for X" documents. Match incoming queries to relevant skill docs, inject them into the prompt. Rules managed by dev team/PMs — domain expertise encoded as retrievable steering documents.

### 6. Tool Guards (State-Based Rejection)

Tools inspect `agent_state` and reject invalid or redundant calls:

```python
def search_bm25(keywords, top_k=5, agent_state=None):
    guard_error = guard_disallow_repeated_queries(
        {"tool_name": "search_bm25", "query": keywords}, agent_state)
    if guard_error:
        return guard_error  # "You've already searched this area!"
```

**Tool guard patterns:**
- **Deduplication:** Reject queries too similar to previous ones — *"You've already been here dope!"*
- **Constraint enforcement:** Reject invalid parameters — *"top_k must be <= 100"*
- **Directional steering:** Reject searches in already-explored areas, or enforce specific next-search directions
- **Category/domain enforcement:** Force the agent to explore different categories or filters

### 7. Subagent Delegation

**Problem:** Long-running agents suffer from **context rot** — they forget mistakes made at step #10 by step #50. Complex tools with many parameters create a **curse of dimensionality** where agents spend 100K+ tokens just learning the tool surface.

**Solution:** Delegate independent search tasks to subagents with fresh context:

```python
# Orchestrator delegates to subagents
Main agent (orchestrator):
    → Subagent A: Search task (fresh agent_run, clean context)
    → Subagent B: Search task (fresh agent_run, clean context)
    → Synthesize results + automated feedback
```

**Key properties:**
- Each subagent gets a **fresh run** — no accumulated context debt
- Subagents are **stateless between runs** — the orchestrator owns state
- Subagents can receive **automated feedback** injected by the harness
- Different subagents can explore **different starting positions** (e.g., different categories, different query strategies)

This maps to the **orchestrator-subagent pattern** documented in [[concepts/harness-engineering/agent-engineering-guide-2026]] and [[concepts/harness-engineering/agentic-workflows/subagents]].

## Results: What Works

Turnbull's experiments on the WANDS e-commerce dataset (~45K products) show progressive NDCG improvements as steering patterns are layered:

| Variant | Mean NDCG | Δ from baseline |
|---------|-----------|-----------------|
| BM25 (no agent) | 0.5408 | — |
| Agentic + FS Tools | 0.5565 | +0.0157 |
| + Few-Shot Priming | 0.5652 | +0.0244 |
| + Subagent Delegation | 0.5661 | +0.0253 |

**Key takeaways:**
1. **Priming has the largest impact** — few-shot examples (+0.0087 over FS Tools) provide better ROI than delegation (+0.0009 over few-shot)
2. **Simple tools work** — constrained filesystem-like tools (`ls`/`grep`/`cat`) beat complex search APIs; the agent's reasoning compensates for tool simplicity
3. **Delegation is situational** — with simple tools and small search spaces, the overhead of delegation may outweigh benefits
4. **BM25 is a strong baseline** — the agent+steering stack improves it, but doesn't replace its fundamental quality

## BEAM Search: Beyond Random Exploration

Turnbull raises the question of whether "search" (randomly issuing keyword queries) is the right primitive for exhaustive exploration. **BEAM search** over a structured filesystem may be more systematic:

1. Navigate to categories/subcategories (like directory traversal)
2. Search (grep) within each location
3. Track visited locations to avoid redundancy
4. Implement pruning based on relevance signals

This reimagines search as **systematic traversal** rather than **stochastic probing** — closer to how a human researcher explores a library than how a search engine retrieves documents.

> For full implementation details (filesystem tools, subagent-as-tool composition, orchestrator pattern, expert gathering with NAICS classification, personality tracking), see [[concepts/exhaustive-agentic-search]].

## Design Principles

1. **Agent picks tools; you control tool responses** — tool responses ARE prompt engineering
2. **Harness > Model** — the control loop matters more than which model is inside it
3. **User-feedback messages steer agents better than system instructions** — leverage training bias
4. **Tool guards prevent wasted exploration** — return errors for redundant/inefficient calls
5. **Prime with few-shot examples** — avoid wasting tokens on initial exploration (highest ROI)
6. **Delegate long/complex tasks to subagents with fresh context** — prevents context rot
7. **Simple, constrained tools > complex, parameter-rich tools** — avoids curse of dimensionality
8. **Start with dumb retrievers and smart steering** — add complexity only when data proves it's needed

## Related

- [[concepts/agentic-search]] — The broader search paradigm that steering patterns support
- [[concepts/harness-engineering]] — The engineering discipline behind the harness layer
- [[concepts/harness-engineering/agentic-workflows/subagents]] — Subagent patterns in detail
- [[concepts/harness-engineering/agent-engineering-guide-2026]] — Orchestrator-subagent pattern and harness mindset
- [[concepts/harness-engineering/agentic-engineering-guardrails-layer]] — Guardrails as a harness layer
- [[concepts/query-understanding]] — LLM query understanding (Part 2 of Cheat at Search)
- [[concepts/ai-benchmarks/ndcg]] — NDCG evaluation metric (Part 1 of Cheat at Search)
- [[entities/doug-turnbull]] — Doug Turnbull, creator of the Cheat at Search series
- [[entities/doug-turnbull-speaking]] — Complete list of Turnbull's talks/lectures
