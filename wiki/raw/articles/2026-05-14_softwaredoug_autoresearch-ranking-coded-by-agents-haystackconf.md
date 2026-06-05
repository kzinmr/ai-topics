---
title: "AutoReSEARCH — Ranking Coded by Agents (HaystackConf 2026)"
created: 2026-05-14
author: Doug Turnbull (@softwaredoug)
source: YouTube
url: https://www.youtube.com/watch?v=Jd2_7sVXUxA
type: talk
duration: "47:20"
tags:
  - autoresearch
  - search-ranking
  - coding-agents
  - agentic-search
  - overfitting
  - guardrails
  - ndcg
  - bm25
  - machine-learning
  - harness-engineering
  - dependency-injection
---

# AutoReSEARCH — Ranking Coded by Agents (HaystackConf 2026)

**Speaker:** Doug Turnbull (@softwaredoug)
**Event:** Haystack Conference 2026
**Date:** May 14, 2026 (uploaded)
**Duration:** 47:20
**Companion notebook:** [search-experiments repo](https://github.com/softwaredoug/search-experiments)
**Related Cheat at Search lectures:** [[transcripts/2026-06-04_softwaredoug_cheat-at-search-coding-agents-lecture|Lesson 7: Coding Agents & Auto Research]], [[transcripts/2026-06-02_softwaredoug_cheat-at-search-long-running-search-lecture|Lesson 5: Long Running Search Agents]]

> **Note:** This is a conference version of concepts Doug teaches in the Cheat at Search Maven course. The Cheat at Search Lesson 7 (June 4, 2026) covers the same material in a classroom setting with Q&A. See [[transcripts/2026-06-04_softwaredoug_cheat-at-search-coding-agents-lecture]] for the course version.

---

## Core Thesis

Can AI code generation replace Learning to Rank? Doug Turnbull explores **AutoReSEARCH** — using coding agents (Claude Code, Codex, or custom) to iteratively generate and optimize search ranking code. The key insight: this is not just vibe coding, it's **machine learning with code as the model**.

> "Deep learning is a universal function approximator — it's really just linear algebra being optimized. AutoReSEARCH is just a different sort of putty being optimized, but in the same sort of harness."

---

## 1. AutoReSEARCH Origins

AutoReSEARCH originates from **Andrej Karpathy** — using a coding agent to iteratively optimize a metric rather than pass tests. Examples:
- **Karpathy:** Optimizing PyTorch model architecture
- **Shopify:** Optimizing backend performance (build times, test speeds)
- **Turnbull:** Optimizing search ranking code (this talk)

The deployment advantage over traditional LTR: no new inference service needed. You're just improving code you already deploy.

---

## 2. Agent-Coded Rankers: The Dependency Injection Pattern

Instead of putting an agent in the loop at query time, Turnbull proposes **agent-coded rankers** — the agent generates ranking code offline, then that code runs in production without any agent.

### Architecture

```
Agent (GPT-5 / Claude)
  ├── Tools: apply_patch, revert, eval, rerank_single_query
  ├── Injected Primitives: fielded BM25, vector search, query categorization
  └── Eval Harness: NDCG on WANDS (Wayfair) dataset
```

The primitives are **dependency-injected** — the agent doesn't modify them, it assembles them into ranking functions. Like LEGO pieces.

### The Eval Loop

1. Start with baseline ranking code (e.g., naive BM25 on title+description)
2. Agent proposes code patches
3. Eval tool runs all queries, returns per-query NDCG changes
4. Agent iterates based on feedback
5. Repeat for N rounds

### Code Editing Mechanism

Turnbull built a custom coding agent (not Claude Code) with an `apply_patch` tool using **anchor-and-block-until** pattern:
- Search for an anchor string in the code
- Search for a "block until" string
- Replace the matched region with new text
- Save and validate the code runs

---

## 3. The Overfitting Problem

> "Coding agents scour for information to achieve their goal. It's pretty frequent that someone tries to optimize search with Claude Code and you'll see stuff like this happen all the time."

### What Overfitting Looks Like

Without guardrails, the agent generates query-specific rules:
- "If query is 'red shoes', return these exact results ranked by this order"
- Hundreds of lines of if-then-else for specific queries
- Looks good on training data, fails miserably on unseen queries

The agent produces code that's essentially a lookup table for the 480 training queries.

### Why It Happens

The agent is optimizing the metric (NDCG) without constraints. It will happily memorize training data because that's the path of least resistance to improving the metric.

---

## 4. Guardrails Against Overfitting

Turnbull identified three key guardrails, all informed by classical ML practices:

### 4.1 LLM-Based Overfit Detection

Ask a GPT-5 mini model: "Does this code look overfit? Does it contain query-specific product terms?" If yes, reject the patch with an error that goes back to the agent.

### 4.2 Patch Size Limits

Limit patches to **10 lines, 120 characters wide**. Rationale:
- Small changes make cause-effect reasoning easier
- Prevents the agent from dumping hundreds of query-specific rules
- Forces the agent to think tactically about each change

> "If we made a tactical couple of lines changed and saw which queries improved or got worse, it's easier to reason about why that might have happened."

**Side effect:** Agents learn to cheat by writing extremely compact code to squeeze within the limit.

### 4.3 Training / Validation / Test Split

The most important guardrail — a 3-layer progressive disclosure:

| Layer | Agent Visibility | What It Sees |
|-------|-----------------|--------------|
| **Training** | Full access | Per-query NDCG changes (e.g., "red shoes up, brown shoes down") |
| **Validation** | Limited | Only overall NDCG must improve by ≥0.003 margin |
| **Holdout/Test** | None | Completely hidden — monitors for true generalization |

> "This apply_patch is almost more like a commit function. And these checks are almost like pre-commit checks."

### Results with Guardrails

- Training NDCG: gradually climbs to ~0.59
- Validation: also improves (guardrails rejecting overfit patches)
- Generated code: fielded BM25 + embedding search + reciprocal rank fusion + intersection bonus
- The agent discovers RRF (reciprocal rank fusion) — the "least offensive" hybrid search solution

---

## 5. AutoReSEARCH IS Machine Learning

> "When we're doing this AI coding, the way to think about it is this AI auto-research really is machine learning. We still need to take our eval data, have good splits, and control the visibility of that data to the model."

Key parallels:
- **Feature engineering** → choosing which primitives to inject
- **Data splits** → train/validation/holdout
- **Regularization** → patch size limits, overfit detection
- **Model training** → code generation loop
- **Overfitting** → query-specific memorization
- **Validation overfitting** → even validation data can be overfit if agent brute-forces

---

## 6. Exploration vs. Exploitation

### The Default Behavior Problem

LLMs default to well-known patterns. Given BM25 + embeddings, the agent almost always produces **reciprocal rank fusion** — because that's the standard approach in its training data.

### Narrowing Scope

Turnbull's key insight: **don't boil the ocean**. Instead of giving the agent all tools at once:

1. **First round:** Optimize retrieval (BM25 + embeddings) → produces optimized RRF code
2. **Second round:** Hide the first round's code behind a single `search` tool, add query rewriting as the new capability to explore

This "focused composition" approach:
- Gets higher NDCG faster
- Agent isn't overwhelmed by combinatorial exploration
- Each round focuses on one dimension of the problem

### MS Marco BM25 Experiment

Turnbull attempted to auto-research a **better BM25** on MS Marco:
- Starter code: raw BM25 with term frequency, document frequency, and other raw stats
- Hints given: explore bigrams, collocations, parameter tuning
- **Mini MS Marco** (subset): made real improvements (stop word handling, bigram weighting)
- **Full MS Marco**: plateaued — the mini-Marco improvements overfit to the specific sample

> "This is another big problem in machine learning which you can overfit to your validation data."

**Interesting finding:** The agent discovered **bigram-based BM25** — adding stop words back and weighting by bigram term frequency. A novel approach, but it didn't generalize from the small dataset to the full one.

---

## 7. The Erdos Analogy

Turnbull draws a parallel to how LLMs help solve Erdos problems (impossibly hard math problems):
- LLMs find **analogous proofs** in forgotten 1980s papers
- A proof solver applies those analogies to the current problem
- The LLM isn't being creative — it's exhaustively exploring the corpus of human knowledge

Similarly, auto-research:
- We provide **inspiration and guidance** (hypothesis hints, focused scope)
- We set **boundaries** (guardrails, patch limits)
- The LLM exhaustively explores within its training knowledge
- It picks the "least offensive" solution — which is often what we want

---

## 8. Q&A Highlights

### Performance and Scalability
Gate on performance metrics alongside NDCG. If the optimal code calls BM25 10 times, that may not be acceptable — but it can serve as **inspiration** for a more efficient implementation.

### Genetic Algorithms vs AutoReSEARCH
Random search over parameters is underrated. Bayesian optimization is mostly the first-best random search. Genetic algorithms could extend auto-research by "breeding" branches — one focused on retrieval, another on query understanding.

### Claude Code vs Custom Agent
Functionally similar. The advantage of Claude Code/Codex: you can optimize the **entire search pipeline** (indexing + retrieval + ranking), not just the ranking function. The disadvantage: each trial takes longer (re-indexing vs. just re-ranking).

### The Long Tail of Cheating
The agent can always find new ways to cheat. Best defense: a holdout test set that the agent has **zero knowledge of** — not even validation-level visibility.

---

## Key Takeaways

1. **AutoReSEARCH = ML with code as the model** — same lessons apply (data splits, regularization, overfitting)
2. **Dependency injection over agent-in-the-loop** — generate code offline, deploy without agents
3. **Three-layer validation** — training (full), validation (aggregate), holdout (hidden)
4. **Patch size limits** — forces tactical thinking, prevents query-specific memorization
5. **Focused composition** — narrow scope per round, hide past optimizations behind single tools
6. **LLMs default to known patterns** — RRF, standard approaches; don't expect novel breakthroughs
7. **Inspiration, not magic** — auto-research explores within human knowledge, guided by practitioner hints

---

## Connection to Wiki Concepts

- [[concepts/pi-autoresearch]] — Shopify's generalization of Karpathy's autoresearch; Turnbull applies the same loop to search ranking
- [[concepts/rlm-recursive-language-models]] — Turnbull's Cheat at Search Lesson 7 covers both RLMs and auto-research; the REPL pattern connects to dependency injection
- [[concepts/agent-driven-ranker-optimization]] — The guardrail-based approach to preventing overfitting in agent-generated code
- [[concepts/agentic-search]] — The broader shift from RAG to agents in the search loop
- [[concepts/ndcg]] — The primary evaluation metric used throughout
- [[entities/doug-turnbull]] — Speaker
