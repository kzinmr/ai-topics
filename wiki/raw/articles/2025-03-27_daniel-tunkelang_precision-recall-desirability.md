---
title: "Precision, Recall, and Desirability: A Deep Dive"
author: Daniel Tunkelang
date: 2025-03-27
source: https://dtunkelang.medium.com/precision-recall-and-desirability-a-deep-dive-822d931256c8
type: blog-post
tags:
  - information-retrieval
  - search
  - evaluation
  - precision-recall
---

# Precision, Recall, and Desirability: A Deep Dive

**Author:** Daniel Tunkelang | **Published:** March 27, 2025

This article expands on the classic search tensions — **precision** (nothing but the truth), **recall** (the whole truth), and **desirability** (query-independent quality signals) — and provides structured guidance for measuring, identifying, and fixing problems in each.

## Key Definitions

- **Precision:** "Precision quantifies what most people mean by relevance: the fraction of search results that satisfy or directly relate to the searcher's intent."
- **Recall:** "Recall measures the fraction of relevant documents retrieved."
- **Desirability:** "Query-independent factors, such as popularity, quality, or recency, often determine which relevant results to present to searchers on the first page and in what order."
- **Precision vs. Recall:** "Precision ensures 'nothing but the truth,' while recall ensures 'the whole truth.'"

## 1. Precision

### Why It Matters
- Relevance is the **prime directive** of search.
- Precision is necessary but not sufficient: "desirable yet irrelevant results will not satisfy users."

### How to Measure
- **Unsupervised approaches:** result coherence or self-similarity as proxies (useful as negative signals).
- **Model-based evaluation:** using an existing relevance model (loses independence but still a negative signal).
- **LLM-based judgments:** scalable and cost-effective; judgment quality under debate.
- **Human judgments:** traditional stratified sampling for top-ranked results; binary relevance or graded with positional weighting (e.g., DCG).

### How to Identify Low Precision
- **Search engagement metrics:** low CTR often signals poor precision (can be confused with desirability issues).
- **Query reformulation & filtering:** frequent reformulation, especially when final engagement is very different from original top results.
- **Dissimilar engagement:** interaction with results vastly different from top-ranked ones points to precision problems.

### How to Address Precision Problems
1. **Query triage:** diagnose patterns to guide targeted fixes.
2. **Pseudo-relevance feedback:** rerank to promote results similar to top-ranked ones — may reduce diversity.
3. **Query categorization:** filter or boost results matching the query intent — requires robust content representation.

## 2. Recall

### Why It Matters
- Ensures searchers see **all** relevant content; low recall leads to dissatisfaction and lost revenue.
- Not all recall gaps are equal: "omitting a best-selling product in e-commerce is far worse than missing a less popular one."
- Recall often trades off against precision; retrieval strategies must balance them carefully.

### How to Measure
- **Retrievability analysis:** how often a document appears for queries that should retrieve it, weighted by query frequency.
- **Sampling-based estimation:** use stratified samples from retrieval strategies with different precision–recall tradeoffs.

### How to Identify Low Recall
- **Retrievability analysis:** identify documents absent from results of frequent, relevant queries.
- **Alternate retrieval strategies:** test recall-heavy methods and detect queries most sensitive to the tradeoff.
- **Low-specificity queries with few results:** broad queries should yield many results; sparse results indicate recall gaps.

### How to Address Recall Problems
1. **Query expansion:** synonyms, stemming/lemmatization — but context loss can hurt precision. Combine with a guardrail.
2. **Query relaxation:** make some terms optional — risk of critical term loss; need a precision guardrail.
3. **Whole-query expansion:** map queries to embeddings/intents and retrieve results for similar queries — avoids token-level context loss.

## 3. Desirability

### Why It Matters
- Determines which relevant results are most **useful**; not a substitute for relevance.
- "If a search engine prioritizes desirability over relevance, it may promote highly desirable but irrelevant results."

### How to Measure
- **Engagement probability:** historical probability of engagement (clicks/conversions) conditioned on relevance.
- **Position bias adjustment:** clicks are biased by rank; must correct for it.
- **Content-based modeling:** train regression models on content features to estimate desirability.

### How to Address Desirability Problems
- Combine query-dependent relevance with query-independent desirability in final ranking.
- Use machine-learned ranking (LTR) models like XGBoost for non-linear combination.
- Ensure desirability does not override relevance for critical queries.
