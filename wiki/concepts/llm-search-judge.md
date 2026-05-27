---
title: LLM Search Judge
type: concept
created: 2026-05-27
updated: 2026-05-27
aliases:
  - llm relevance judge
  - llm-as-a-judge for search
tags:
  - evaluation
  - search
  - llm
  - structured-outputs
  - information-retrieval
sources:
  - raw/articles/2026-05-27_softwaredoug_cheat-at-search-llm-as-judge.md
  - raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg.md
related:
  - concepts/ndcg
  - concepts/query-understanding
  - concepts/bm25
  - entities/doug-turnbull
---

# LLM Search Judge

**LLM Search Judge** is the practice of using large language models to automatically evaluate search result relevance, replacing or supplementing expensive human labelers. It enables computation of standard IR metrics ([[concepts/ndcg|NDCG]]) on unlabeled real-world query traffic, dramatically reducing the cost and turnaround time of relevance evaluation.

The technique was systematized by **Doug Turnbull** in Part 4 of his *Cheat at Search* course (2026), building on the Umbrella framework by Lin et al. and drawing on the broader "LLM as a Judge" paradigm (MT-Bench, AlpacaEval). The key insight is that while LLMs are not perfect judges (~73% pointwise agreement with humans), they are **consistent enough at a fraction of the cost** to enable rapid search iteration.

## Core Problem

Traditional search evaluation requires **human-annotated relevance labels** for query-document pairs. These labels power metrics like NDCG, which normalize discounted cumulative gain against an ideal ranking. Human labels are:

- **Expensive**: $1-5 per query-document pair at scale
- **Slow**: Days to weeks for a judgment round
- **Scarce**: Only a tiny fraction of production queries get labeled

The LLM Search Judge addresses this by using structured LLM outputs to generate synthetic relevance labels, enabling NDCG computation on **any query, any result set, at any time.**

## Two Judge Architectures

### Pointwise Judge

Assign a relevance grade (0–3) to a single query-document pair. This is the direct parallel to human labeling.

```
QUERY + DOCUMENT → LLM → Relevance Grade (0-3)
```

**Scoring rubric (0–3 scale):**
| Grade | Meaning |
|---|---|
| 0 | Nothing to do with the query |
| 1 | Related but does not answer |
| 2 | Somewhat answers (unclear or buried) |
| 3 | Dedicated to the query; contains exact answer |

**Implementation** uses structured output (Pydantic `Literal` types) with chain-of-thought reasoning — the LLM first describes search intent and trustworthiness, then assigns the score.

**Accuracy:** ~73% agreement with human judges on 1000 e-commerce samples (gpt-4.1). Room for improvement via prompt refinement and better product data.

**Trade-off:** Pointwise judgments map directly to NDCG without further computation, but the task is harder for LLMs — abstract labels are inconsistently applied to varied product descriptions.

### Pairwise Judge

Present two results (LHS, RHS) and ask: *"Which is more relevant for this query?"* This is a relative preference rather than an absolute grade.

```
QUERY + RESULT A + RESULT B → LLM → Preference (LHS or RHS)
```

**Why it's easier:** For both humans and LLMs, comparing two items is simpler than independently assigning an abstract grade. Fewer degrees of freedom → less noise.

**Cost of simplicity:** Pairwise requires n(n−1)/2 comparisons for n results (45 comparisons for 10 results, 90 with double-checking). This is O(n²) in result count, vs O(n) for pointwise.

**Double-checking for consistency:** The same pair is evaluated twice — once as presented, once with LHS/RHS swapped. If the LLM's preference changes, the evaluation is treated as **unknown** (filtered out to reduce noise). This is a critical quality control technique.

**Precision/Coverage by attribute (vs human ground truth):**

| Judge Type | Precision | Coverage |
|---|---|---|
| Product Name only | 0.73 | 0.84 |
| Product Description only | 0.67 | 0.75 |
| Product Classification only | 0.81 | 0.89 |
| All-in-one prompt | 0.74 | 0.81 |
| Combined (decision tree) | **0.831** | — |

Key finding: **multiple specialized judges > one complex judge.** The all-in-one prompt that asks for relevance based on all product attributes simultaneously performs *worse* than individual judges combined intelligently.

## Decision Tree Aggregation

Multiple pairwise judges (name, description, classification, features) produce preference signals (`-1` = LHS, `+1` = RHS, `0` = unknown). These signals are fed as **features** into a decision tree classifier that learns to predict the human ground truth preference:

```python
from sklearn.tree import DecisionTreeClassifier

X = training_data[["name_pref", "desc_pref", "class_pref", "features_pref"]]
y = training_data["ground_truth_pref"]   # -1, 0, or 1

model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=20)
model.fit(X, y)
```

**Why a decision tree?** Trees produce **explainable scoring flowcharts** that stakeholders can read and trust — a major advantage over black-box models when evaluation methodology needs to be defensible.

**Reported results:** 0.831 overall precision, translating to "tens of thousands in cost reduction per year" for an e-commerce search team.

## Workflow Integration

The LLM judge pipeline integrates into a search relevance workflow:

```
1. COLLECT: Sample unlabeled query-result pairs from production
2. JUDGE: Run pointwise/pairwise LLM judges with structured output
3. AGGREGATE: Combine judges via decision tree (if pairwise)
4. COMPUTE: Derive NDCG from the synthetic relevance labels
5. ITERATE: Tune ranking, re-judge, measure improvement
```

This enables **continuous evaluation** — every ranking change can be immediately assessed against a large, diverse set of queries without waiting for human labelers.

## Relationship to Other Concepts

### [[concepts/ndcg|NDCG]]
NDCG is the target metric; LLM search judging is the **label-generation method** that enables NDCG computation without human annotations. The two form a complete evaluation stack: LLM judges produce grades, NDCG normalizes and aggregates them.

### [[concepts/query-understanding|Query Understanding]]
Both are part of Doug Turnbull's Cheat at Search framework. LLM search judging evaluates the **output** of query understanding pipelines — it answers "did our QU improvements make search better?" QU transforms raw queries into structured attributes; judging verifies the result quality.

### Model-as-Judge (broader paradigm)
LLM Search Judge is a domain-specific instance of the broader **model-as-judge** pattern (MT-Bench for chatbots, AlpacaEval for instruction following, LLM-as-RAG-judge for retrieval). The search variant adds domain-specific concerns: position-aware metrics (NDCG discount), product attribute hierarchies, and double-checking for pairwise consistency.

## Pitfalls & Limitations

- **Position bias in LLM outputs:** LLMs may systematically prefer LHS or RHS regardless of relevance. Double-checking with swapped positions mitigates this.
- **Combining judges requires labeled ground truth:** The decision tree approach needs some human-labeled data for training — it doesn't eliminate human labeling entirely, but makes each label go further.
- **Domain adaptation:** 73% agreement on e-commerce doesn't guarantee similar performance on legal, medical, or technical search.
- **Cost still matters:** While cheaper than humans, running pairwise LLM judges on 10K+ query-result pairs isn't free. Caching, batching, and cheap model selection (gpt-4.1-nano) are essential.

## References

- **Doug Turnbull**, *Cheat at Search Part 4: LLM as a Judge* (slides), 2026 — [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-llm-as-judge]]
- **Doug Turnbull**, *Search Evaluation: NDCG* (blog), 2026 — [[raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg]]
- **Lin et al.**, *Umbrella: A Framework for LLM-based Search Evaluation*
- **Turnbull & Grainger**, *AI-Powered Search* (Manning, 2025)
