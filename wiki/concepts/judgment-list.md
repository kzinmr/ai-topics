---
title: Judgment List
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - search
  - evaluation
  - methodology
  - benchmark
sources: [raw/articles/2021-02-21_softwaredoug_judgment-list.md]
---

# Judgment List

A **judgment list** (also called a **relevance judgment set** or **test collection**) is a curated collection of query-document pairs with human-assigned relevance grades. It's the foundational tool for systematic search relevance evaluation — serving simultaneously as a **test suite**, **training data**, and **communication artifact** for search engineering teams.

> **"A judgment list defines a document's relevance for a query."** — Doug Turnbull

## Core Purpose

Without judgment lists, search tuning is subjective — teams operate in a "whack-a-mole" cycle where fixing one query silently breaks others. A judgment list provides a **quantitative safety net**: changes can be tested objectively against known relevance expectations.

### The Three Roles of a Judgment List

| Role | Description |
|------|-------------|
| **Test suite** | Measure whether ranking changes improve or degrade quality |
| **Training data** | Feed learning-to-rank (LTR) models with labeled examples |
| **Communication tool** | Align cross-functional teams on what "good" search looks like |

This concept was popularized by **[[entities/doug-turnbull]]**, who made it a centerpiece of his search relevance engineering methodology, particularly in his books *Relevant Search* (2016) and *AI-Powered Search* (2025).

## Anatomy

A judgment list is structured as a table of query-document-grade triples:

```
query,       document,                         grade
star wars,   "Star Wars: A New Hope",          1
star wars,   "Return of The Jedi",             1
star wars,   "Blair Witch Project",            0
star wars,   "A Star Is Born",                 0
star trek,   "Star Trek Into Darkness",        1
star trek,   "Star Trek II: The Wrath of Khan", 1
star trek,   "Sense and Sensibility",          0
star trek,   "Forrest Gump",                   0
```

Each row answers a single question: **for this query, is this document relevant?**

## Measuring Quality with DCG

Once you have a judgment list, you can measure search quality using **Discounted Cumulative Gain (DCG)**: replace each search result with its grade, then compute a weighted sum that rewards relevant results appearing early.

The intuition:
- A good search puts relevant documents first → grades like `[1, 1, 0, 0]`
- A poor search buries relevant documents → grades like `[0, 0, 1, 1]`
- DCG assigns **higher weight to top positions** via a rank-based discount

For the poor ranking `[0, 0, 1, 1]` at position 4: **DCG@4 = 0.58**
For the ideal ranking `[1, 1, 0, 0]` at position 4: **DCG@4 = 1.5**

> The full normalized metric is [[concepts/ai-benchmarks/ndcg]] (Normalized DCG), which divides DCG by the ideal DCG to produce a 0–1 score.

## Sources of Judgments

There is no single "ground truth" — each method provides a different lens on relevance:

### 1. Implicit Judgments
Derived from **user behavior**: clicks, purchases, dwell time, conversions.
- **Best for**: high-traffic, broad domains with abundant behavioral data
- **Caveat**: raw CTR alone is misleading — position bias, presentation bias, and other confounds must be accounted for
- See: *AI-Powered Search*, Chapter 11

### 2. Crowdsourced Judgments
Via platforms like Amazon Mechanical Turk, Appen, or Supahands.
- **Best for**: scaling judgment collection across many query-document pairs
- **Caveat**: quality depends heavily on clear instructions and qualification tests

### 3. Explicit Judgments
**Human raters** in controlled UX-study settings provide direct relevance assessments.
- **Best for**: domain-specific use cases with low traffic, where implicit signals are sparse
- **Caveat**: expensive, slow, and subject to rater disagreement

### The "No Golden Set" Principle

Turnbull specifically advocates against calling judgment lists "golden sets" or "ground truth." Instead, he recommends using **multiple evaluation systems** in parallel and comparing them via rank correlation metrics like **Kendall's Tau**. Differences between judgment sources often reveal the most valuable insights about what "relevance" actually means for a given domain.

## Grading Schemes

| Type | Values | Use Case |
|------|--------|----------|
| **Binary** | 0/1 (irrelevant/relevant) | Simplest; good for known-item search |
| **Categorical** | 0–4 with per-level definitions | Best for explicit human raters; provides nuance |
| **Probabilistic** | 0.0–1.0 (e.g., normalized CTR) | Natural fit for implicit behavioral data |

### Categorical Example (Job Search)

```
0 – It's not worth ever applying
1 – Unlikely I would apply
2 – 50/50
3 – I would apply
4 – I would put a high level of effort (call hiring manager, etc.)
```

The key is matching the grading scheme to both the **domain** and the **judgment creation method**.

## Test-Driven Relevancy

A judgment list enables **test-driven search engineering**, analogous to unit tests in software development:

1. **Define** what "relevant" means for your use case
2. **Build** a judgment list of query-document-grade triples
3. **Measure** current quality via [[concepts/ai-benchmarks/ndcg]]
4. **Iterate** on ranking signals, re-running evaluation each time
5. **Ship** only changes that improve or maintain overall DCG

This closes the feedback loop: teams can **prototype ranking changes locally** (e.g., in [[concepts/quepid]]), run evaluation instantly, and catch regressions before they reach users. No full A/B test or user study required at every step.

> **"A judgment list gives your team permission to iterate quickly on relevance improvements."** — Doug Turnbull

## Relationship to Learning to Rank

Judgment lists are the essential input to **[[concepts/learning-to-rank]] (LTR)** systems. LTR models (XGBoost, LambdaMART, neural rankers) learn from labeled query-document pairs — the judgment list _is_ the training data. The quality of an LTR system is bounded by the quality of its judgment list:

- **Garbage in, garbage out**: poor judgments → poor ranking model
- **Coverage matters**: a judgment list covering only 50 queries won't generalize
- **Position bias**: judgments collected from production search results (where users only see top-ranked items) introduce systematic bias

## "Grug-Brained Evals"

Turnbull advocates for a pragmatic approach he calls **"grug-brained evals"**:

> "Big brain spend months building perfect quality metrics. Grug brain just want dumb labels from coworkers 👍/👎."

The principle: **start simple**. Binary thumbs-up/thumbs-down labels from domain experts beat months of methodology design. Get a judgment list into production fast, then iterate on quality — rather than waiting for a "perfect" set that never arrives.

## In the AI Era

Judgment lists remain relevant even as search evolves toward AI-powered and agentic approaches:

- **LLM-as-a-Judge**: LLMs can generate synthetic judgments at scale, but should be validated against human judgments
- **Agentic search**: [[entities/doug-turnbull]] argues agents need judgment lists as quality guardrails — the agent iterates, but the harness validates against known relevance expectations
- **Engagement signals**: Turnbull identifies the lack of implicit judgment collection as "RAG's big blindspot" — most RAG teams rely entirely on LLM evaluation without collecting click/behavior data

## Tools

| Tool | Description |
|------|-------------|
| **[[concepts/quepid]]** | Open-source search relevance testing workbench — upload judgment lists, run evaluations, compare ranking configurations |
| **Elasticsearch LTR Plugin** | Uses judgment lists as training data for learning-to-rank within Elasticsearch |
| **SearchArray** | Pandas-based BM25 library — fast local experimentation without a full search engine |

## See Also

- [[concepts/ai-benchmarks/ndcg]] — The normalized metric built on judgment lists
- [[concepts/learning-to-rank]] — ML-based ranking that trains on judgment lists
- [[concepts/bm25]] — Lexical retrieval baseline often evaluated against judgment lists
- [[concepts/quepid]] — Open-source workbench for judgment list management and evaluation
- [[entities/doug-turnbull]] — The search relevance expert who popularized judgment list methodology
- [[entities/doug-turnbull-core-ideas]] — Judgment list's role in Turnbull's broader philosophy
- [[concepts/searcharray]] — Lightweight tool for local experimentation with judgment lists
