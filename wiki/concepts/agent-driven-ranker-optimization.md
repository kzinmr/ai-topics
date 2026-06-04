---
title: "Agent-Driven Ranker Optimization"
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [agentic-search, eval-loops, bm25, information-retrieval, coding-agents, overfitting, autoresearch, search, methodology, benchmark-optimization, agent-loop]
sources:
  - raw/articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms
  - raw/articles/2026-05-14_softwaredoug_autoresearch-ranking-coded-by-agents-haystackconf
related:
  - autoresearch-bm25-msmarco
  - rlm-recursive-language-models
  - agent-steering
  - agentic-search
  - eval-loops
  - bm25
---

# Agent-Driven Ranker Optimization

## Overview

Agent-Driven Ranker Optimization is a pattern where a **coding agent iteratively edits search ranking code**, evaluates it against a judgment set, and uses guardrails to prevent overfitting. Proposed by [[entities/doug-turnbull|Doug Turnbull]] in Lesson 6 of the "Search with Agents" series (June 2026), it generalizes the earlier [[concepts/autoresearch-bm25-msmarco|Autoresearch BM25]] case study into a reusable framework with explicit guardrail patterns.

The core insight: **AI coding IS model development.** The agent's code edits are functionally equivalent to gradient updates — and require the same train/test discipline.

## Architecture

### Three-Tool Design

| Tool | Role | Visibility |
|------|------|-----------|
| `apply_patch` | Propose code changes (Edit model) | Agent sees edit result |
| `run_reranker` | Run ranking on a single query | Agent sees full output |
| `run_evals` | Run on full judgment set → NDCG | Agent sees per-query deltas |

Plus `revert_changes` for rollback and `search_wands` for direct BM25 exploration.

### Code Editing: The Edit Model

Structured edits via a Pydantic model:

```python
class Edit(BaseModel):
    anchor: str        # Where to start the edit
    block_until: str   # Where the edit block ends
    action: Literal['insert_after', 'replace', 'delete']
    text: str          # Replacement text (ignored for delete)
```

The `apply_patch` tool validates that the edited code is syntactically valid and defines the required function before saving.

### Dependency Injection Pattern

The ranking function receives search primitives as parameters — the agent cannot modify the underlying search infrastructure:

```python
def rerank_wands(search_wands, query):
    # Agent edits ONLY this function
    docs = search_wands(keywords=query, ...)
    return [doc['id'] for doc in docs]
```

This constrains the optimization surface to ranking logic, not search infrastructure.

## The Train/Test Split Discipline

The critical design decision: **separate the agent's training signal from the validation signal.**

| Split | Agent sees? | Purpose |
|-------|------------|---------|
| Training queries | ✅ Full per-query NDCG + results | Guide exploration |
| Holdout queries | ❌ Only aggregate pass/fail | Prevent overfitting |

The agent can overfit to training queries freely — the holdout gate rejects edits that degrade generalization.

## Guardrail Stack

### 1. Pre-Change Guardrails (Before `apply_patch`)

| Guardrail | What it checks |
|-----------|---------------|
| **Overfitting detector** | LLM reviews code for hardcoded product names, brands, query-specific terms |
| **Length validator** | `max_lines=10, max_cols=120` — forces granular, reviewable changes |
| **Syntax check** | `exec()` + function existence check |

Why granular changes matter: agents need to understand **causality** — Change → NDCG altered. Giant changes make attribution impossible.

### 2. Post-Change Validation (After `apply_patch`)

```python
ndcg_before = validation_eval_fn(existing_code).mean()
ndcg_after = validation_eval_fn(code).mean()
if ndcg_after < (ndcg_before + eval_margin):
    reject_with_error()
```

The agent never sees holdout data — only the NDCG delta.

### 3. Feedback Enrichment

```python
class EvalResult(BaseModel):
    success: bool
    error_message: Optional[str]
    ndcg_deltas: Optional[Dict[str, float]]  # Per-query improvements
```

Training feedback includes per-query deltas so the agent can learn which changes helped which queries.

## Empirical Results (WANDS Dataset)

### Without Guardrails (Overfitting)

| Round | NDCG |
|-------|------|
| Baseline | 0.5605 |
| Round 0 | 0.5613 |
| Round 1 | 0.5592 |
| Round 2 | 0.5560 |
| Round 5 | 0.5583 |

Agent's code grew more complex but gains plateaued immediately on holdout. "Just wandering around."

### With Guardrails (10 Iterations)

| Round | NDCG |
|-------|------|
| Round 0 | 0.3428 |
| Round 2 | 0.5441 |
| Round 4 | 0.5620 |
| Round 8 | 0.5753 |
| Round 9 | 0.5753 |

Significant improvement from baseline (0.5605 → 0.5753), with changes rejected when they degraded holdout performance.

## Key Insights

1. **"AI coding IS model development"** — The agent's code edits are the optimization; eval data is the training set; guardrails are regularization.

2. **Granular > Giant changes** — Small, reviewable edits enable causal reasoning. "Agents need to understand causality: Change → NDCG altered."

3. **Dependency injection constrains the surface** — The agent can't modify `search_wands` (the BM25 primitive), only the ranking logic that uses it.

4. **Early decisions compound** — The first edit constrains all subsequent edits. Different initial paths lead to different local optima.

5. **RLM extension** — The final slide asks: "Could we RLM this? Let the search code call a language model!?" — pointing toward recursive agents that can invoke LLMs from within ranking code for dynamic query understanding.

## Connection to RLMs

Turnbull frames this as a natural extension of [[concepts/rlm-recursive-language-models|RLMs]]: if the ranking code can call `llm_query()`, the agent could dynamically generate query expansions, classify queries, or judge result relevance — all within the ranking function itself. This collapses the distinction between "search code" and "search agent."

## Relationship to Existing Frameworks

| Framework | Relationship |
|-----------|-------------|
| [[concepts/autoresearch-bm25-msmarco\|Autoresearch BM25]] | Specific instance on MSMarco — same pattern, smaller scale |
| [[concepts/eval-loops\|Eval Loops]] | Same three-part structure (test cases, metrics, threshold) |
| [[concepts/agent-steering\|Agent Steering]] | Guardrails are a steering pattern (carrot-and-stick) |
| [[concepts/agentic-search\|Agentic Search]] | Ranker optimization is the "coding agent layer" of agentic search |
| [[concepts/rlm-recursive-language-models\|RLMs]] | Natural extension — ranking code that calls LLMs |

## Limitations

- **Constrained sandbox** — Limited by search primitives (BM25). Agent can't install new libraries or change the index.
- **Early path dependence** — First edit constrains all subsequent edits; no mechanism for "undo to round 0 and try a different approach."
- **Environment constraints** — Unlike Claude Code in the wild, the agent can't install dependencies or access external data.
- **Overfitting remains** — Even with guardrails, the agent optimizes against a fixed judgment set that may not represent production queries.

## See Also

- [[concepts/autoresearch-bm25-msmarco]] — Earlier case study (same author, same pattern)
- [[concepts/rlm-recursive-language-models]] — REPL-based recursive agents
- [[concepts/agent-steering]] — Steering patterns for search agents
- [[concepts/agentic-search]] — The broader agentic search paradigm
- [[concepts/eval-loops]] — General eval loop framework
- [[entities/doug-turnbull]] — Author
