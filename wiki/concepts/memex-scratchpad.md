---
title: "MemEx — Programmable Scratchpad for LLM Agents"
created: 2026-06-12
updated: 2026-06-12
type: concept
tags:
  - context-management
  - ai-agents
  - code-act
  - tool-calling
  - programmatic-tool-calling
  - databricks
  - agent-architecture
  - context-management
  - cost-optimization
  - enterprise-ai
aliases: [memex-scratchpad]
sources:
  - raw/articles/2026-05-19_databricks_memex-programmable-scratchpad-llm-agents.md
  - "https://www.databricks.com/blog/memex-programmable-scratchpad-llm-agents"
related:
  - concepts/coding-agents/codeact
  - concepts/programmatic-tool-calling
  - concepts/context-engineering/context-management
  - entities/databricks
  - concepts/dspy-rlm
---

# MemEx — Programmable Scratchpad for LLM Agents

> **MemEx** gives LLM agents a **typed Python kernel** (scratchpad) that persists across turns. Tool outputs land as Python objects in scope — only `print()` stdout enters the context window. This replaces JSON/XML tool calling with **code-as-action**, lifting accuracy and cutting token cost on enterprise tasks.

Developed by **Databricks AI Research Team** (Baheti, Toshniwal, Singhvi, et al., May 2026), MemEx extends the [[concepts/coding-agents/codeact|CodeAct]] paradigm with persistent scope, typed returns, and sub-agent primitives — dropping directly into existing [[concepts/agent-architecture|ReAct-style]] agent frameworks.

## Core Problem

In standard **Agentic Tool Calling**, the context window is the only persistent substrate: system prompt, user query, reasoning, tool calls, and raw tool outputs all share the same space. Tool outputs are the worst offenders — a single SQL query can return millions of rows that ride along in every subsequent turn, even if only one cell matters. The agent has no way to slice, summarize, or stash results before they flood the window.

## How MemEx Works

```
┌────────────────────────────────────────────────────┐
│                    MemEx Agent                       │
│                                                      │
│  User Task ──→ LLM generates Python code block       │
│                      │                               │
│                      ▼                               │
│  ┌──────────────────────────────────────────┐        │
│  │         Typed Python Kernel (scope)       │        │
│  │                                           │        │
│  │  tools: {query_db, search, ...}           │        │
│  │  scope: {prev_results, helpers, ...}      │        │
│  │  → execute code block                     │        │
│  │  → only print() enters context            │        │
│  └──────────────────┬────────────────────────┘        │
│                      │                               │
│                      ▼                               │
│  LLM observes stdout ──→ authors next code block     │
│                                                      │
│  Loop continues until agent calls submit(result)     │
└────────────────────────────────────────────────────┘
```

### Key Mechanisms

| Mechanism | Description |
|-----------|-------------|
| **Persistent REPL** | Code executes in a namespace that persists across turns. Tools, scope objects, and prior results all live in that namespace. |
| **Typed Python tools** | Tools are auto-injected as Python functions with parameter schemas and typed return values. Tool outputs are Python objects, not strings. |
| **Print-only materialization** | Only `print()` stdout enters the context window. Intermediate DataFrames, datasets, and objects stay in scope. |
| **Typed `submit()`** | Structured return mechanism for final answers. |
| **`spawn_agent()`** | Non-blocking sub-agent spawning with shared scope access — generalizes [[concepts/dspy-rlm|Recursive Language Models]]. |

### Example: Enterprise Funnel Analysis

**Task:** Compare signup-to-activation funnels for three customer segments and identify the biggest drop-off.

**Tool Calling agent** (step-by-step):
- Turn 1: SQL query for signup events → serialize DataFrame to text in context
- Turn 2: SQL query for activation events → serialize again
- Turn 3: Python join/merge → serialize again
- Turn 4: Compute conversion rates → serialize again
- Turn 5: Rank drop-offs → final answer
- *Total: 5+ turns, heavy intermediate text in context*

**MemEx agent** (single block):
```python
signups = query_db("SELECT ... FROM signups")
activations = query_db("SELECT ... FROM activations")
merged = signups.merge(activations, on="user_id")
rates = merged.groupby("segment").apply(conversion_rate)
dropoffs = rates.diff().abs().sort_values(ascending=False)
submit({"biggest_dropoff": dropoffs.index[0], "details": rates})
```
- *Total: 1 turn, only the submit result enters context*

## Evaluation Results

### Enterprise Structured Retrieval

Natural-language questions over enterprise relational data with schema-discovery and SQL-query-execution tools.

| Model | Tool Calling Acc. | MemEx Acc. | Tool Calls (TC → MemEx) | Cost Reduction |
|-------|-------------------|------------|--------------------------|----------------|
| Qwen3.5-122B | 18% | 36% | 56 → 28 | ~50% |
| Qwen3.5-397B | 20% | 38% | — | ~40-50% |
| Sonnet 4.6 | ~baseline | +2-5pp | 28 → 17 | ~25-30% |
| Opus 4.6 | ~baseline | +2-5pp | 33 → 21 | ~25-30% |
| GPT 5.5 | ~parity | ~parity | — | — |

### OfficeQA Pro

Grounded reasoning over U.S. Treasury Bulletins (~89,000 pages, 1939–present). Four of five cost-vs-accuracy Pareto frontier points are MemEx configurations.

- **Gemini 3.1 Pro MemEx**: $0.62/rollout, 52.9% accuracy (cheapest frontier point)
- **Sonnet 4.6 MemEx**: approaches GPT-5.5 Tool Calling accuracy at ~70% of the cost
- **Qwen 3.6 27B** and **Gemini 3.1 Pro**: ~10 percentage point gains

## Trajectory Analysis Applications

### MemEx Auditing MemEx

MemEx can load agent trajectories as Python scope objects and reason over them — something impossible when trajectories span multiple context windows. An audit agent analyzing OfficeQA Pro trajectories found:

| Failure Axis | MemEx Errors | Tool Calling Errors | Reduction |
|---|---|---|---|
| Source Selection | 32 | 45 | 29% |
| Interpretation | 28 | 38 | 26% |
| Search Strategy | 6 | 15 | 60% |
| Execution | 3 | 6 | 50% |
| **Total** | **69** | **104** | **34%** |

Root cause: retrieval results land directly in Python variables, so the model avoids copying values between tool calls (e.g., 3,501 → 3531 transcription error).

### Agentic Parallel Thinking

MemEx loads multiple full trajectories as scope variables for an aggregator agent — no lossy summarization needed. A Sonnet 4.6 MemEx aggregator over 8 Qwen-3.6-27B trajectories outperforms the equivalent Tool Calling aggregator limited to summaries.

## Architecture

### Three Design Choices

1. **Code as action, in a persistent REPL** — same observe-act loop as ReAct, only the action space changes
2. **Drop-in for Tool Calling** — existing tools auto-injected as Python functions; switching is a single config change
3. **Backend-agnostic execution** — three backends:
   - **In-process**: fast iteration (research)
   - **Subprocess**: isolation (evaluation)
   - **Pool**: high-throughput batch (training data generation)

### Relationship to the Code-as-Action Family

MemEx is in the [[concepts/coding-agents/codeact|CodeAct]] lineage, with four extensions:

| Extension | CodeAct | MemEx |
|-----------|---------|-------|
| Tool integration | Manual | Drop-in with parameter schemas preserved |
| Scope | Per-turn | Live Python scope at rollout start |
| Return type | stdout | Typed `submit()` for structured returns |
| Sub-agents | Not built-in | `spawn_agent()` for parallel sub-agents |

**Production variants in the same family:**
- [[concepts/programmatic-tool-calling|Anthropic's Programmatic Tool Calling]] — code-as-action for tool orchestration
- Cloudflare Code Mode — code-as-action in V8 isolates
- **MemEx** — code-as-action with persistent scope + sub-agents, integrated into aroll (Databricks' agentic rollouts framework powering Genie and Agent Bricks)

## What's Next (as of May 2026)

- Rolling out across Databricks' first-party agents and Agent Bricks
- Post-training models for the MemEx action space
- MemEx itself generates synthetic data, runs agentic verifiers, and feeds the training loop

## Related Pages

- [[concepts/coding-agents/codeact]] — the academic ancestor (CodeAct paradigm)
- [[concepts/programmatic-tool-calling]] — Anthropic's production variant of code-as-action
- [[concepts/context-engineering/context-management]] — broader context management strategies
- [[concepts/dspy-rlm]] — Recursive Language Models (generalized by MemEx's `spawn_agent()`)
- [[entities/databricks]] — Databricks company page (MemEx developer)
- [[concepts/ai-agent-architecture]] — agent architecture overview
