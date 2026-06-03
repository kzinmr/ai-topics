---
title: "Cheat at Search Part 4 — LLM as a Judge"
author: Doug Turnbull (@softwaredoug)
date: 2026-05-28
date_ingested: 2026-05-27
source: https://docs.google.com/presentation/d/16hw0veoCQYKN8hPr8N4EGnXNfUOegGnvKzMpaGZjQjo/edit
type: slides
tags:
  - search
  - evaluation
  - llm
  - query-understanding
  - ndcg
  - structured-outputs
---

# 4. Cheat at Search — LLM as a Judge

**Author:** Doug Turnbull / SoftwareDoug LLC
**Context:** Part 4 of the Cheat at Search series. Covers using LLMs as automated relevance judges for search evaluation.
**Series:**
- Part 1: NDCG / Search Evaluation
- Part 2: Cheat at Search — LLM Query Understanding (slides)
- Part 3: Cheat at Search — Steering Lost Agents (Agentic Design Patterns)
- Part 4: Cheat at Search — LLM as a Judge (this presentation)

---

## Overview

- **Goal:** Automatically evaluate search results using LLMs to replace or supplement human labelers, enabling faster iteration and broader coverage.
- **Context:** Building a complete search system (query understanding → structured query → search engine → ranking → evaluation). Need to know "Is it any good?"
- **Core problem:** Human-annotated labels are scarce and expensive; unlabeled results exist in real-world tuning. How do we compute metrics like NDCG without labels?
- **Two primary LLM judge approaches:**
  1. **Pointwise:** Assign a relevance grade (0-3) directly to each query-document pair.
  2. **Pairwise:** Compare two products and select the more relevant one.

---

## Pointwise LLM Judge

### Inspired by Umbrella (Lin et al.)

- Prompt asks for an integer score 0–3 in exact format: `##final score: [score]`
- Scoring criteria:
  - 0 = nothing to do with the query
  - 1 = related but does not answer
  - 2 = somewhat answers (answer may be unclear or buried)
  - 3 = dedicated to the query and contains exact answer
- Uses chain-of-thought steps: search intent → trustworthiness → final score.

### Adaptation to E-commerce

- Structured output using a Pydantic-like class with Literal labels and an intent description field:

```python
RelevanceLabel = Literal["nothing to do with the query",
                         "related but does not answer",
                         "somewhat answers",
                         "dedicated to the query and contains exact answer"]

class SearchRelevanceEvaluation(Query):
    relevance_label: RelevanceLabel = Field(...)
    search_intent: str = Field(...)
```

- Prompt includes query, product name, category hierarchy, and description.
- Evaluation on 1000 samples: **73% agreement** with human labelers (gpt-4.1).
- Suggests room for improvement: refining prompt with Wayfair's rating guide, better product data, handling labeler errors.

### Challenges with Pointwise

- Difficult to consistently map abstract labels to products.
- Noisy, inconsistent, and easier to "screw up."
- Harder task → needs more complex (expensive) model.
- However, pointwise judgments can be directly used for NDCG.

---

## Pairwise LLM Judge

### Concept

- Present two products (LHS and RHS) and ask: "Which is more relevant for the query?"
- Easier task for both humans and LLMs, fewer degrees of freedom → less noise.
- But requires many comparisons: for 10 results, n(n−1)/2 = 45 decisions (90 if double-checking).
- Ground truth from labeled data: if grade(LHS) > grade(RHS), ground truth preference = LHS.

### Implementation

```python
RelevancePreference = Literal["lhs", "rhs"]

class SearchRelevancePreference(Query):
    pref: RelevancePreference = Field(description="Whether you prefer rhs or lhs product")
```

- Prompt example:

```python
def product_name(pair) -> str:
    prompt = f"""
Given two product names, indicate which is more relevant to the query

Query: {pair['query']}
Product:
Name LHS: {pair['product_name_lhs']}
Name RHS: {pair['product_name_rhs']}
"""
    return prompt
```

### Double-Checking for Consistency

- Swap LHS and RHS, re-run the prompt. If the preference changes, treat the LLM evaluation as **unknown** (to reduce noise).
- `PairwisePreferenceChecker` class runs both directions and caches results via `AutoEnricher`.

### Experiments with Different Product Attributes

Precision/Coverage results (compared to human ground truth):

| Judge Type | Precision | Coverage |
|---|---|---|
| Product Name | 0.73 | 0.84 |
| Product Description | 0.67 | 0.75 |
| Product Classification | 0.81 | 0.89 |
| All-in-one prompt | 0.74 | 0.81 (worse) |
| Features judge added | 0.904 | 0.79 (combined via decision tree) |

---

## Combining Multiple Judges with a Decision Tree

### Insight

- Multiple LLM judges (name, description, classification, features) can be treated as **features** to predict the human ground truth preference.
- Translate preferences numerically: `-1` (LHS preferred), `1` (RHS preferred), `0` (unknown).

### Model

```python
from sklearn.tree import DecisionTreeClassifier

X = training_data[PREDICTORS]   # LLM preferences
y = training_data['ground_truth_pref']

model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=20)
model.fit(X, y)
```

### Results

- Overall precision: 0.831
- **Business impact:** "We're looking at tens of thousands in cost reduction per year."
- The trained decision tree produces an **explainable scoring flowchart** — a major advantage for stakeholder trust.

---

## Key Takeaways

1. **LLMs can effectively serve as search relevance judges**, offering a practical alternative to expensive human labeling.
2. **Pairwise is easier than pointwise** — simpler task, less noise, but requires more comparisons.
3. **Double-checking (swap LHS/RHS) reduces noise** — inconsistent results become "unknown."
4. **Multiple judges + decision tree > single complex judge** — combining cheap, specialized judges with a learned weighting function beats an all-in-one prompt.
5. **Practical accuracy reached**: ~83% precision with decision tree, significant cost reduction for e-commerce search teams.
6. **Explainability matters**: decision tree produces human-readable scoring rules, not a black box.

---

## Companion Resources

- **Course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)
- **Author:** [softwaredoug.com](http://softwaredoug.com)
- **Related raw articles:** [[raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg]], [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search]], [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents]]
- **Lecture transcript:** [[raw/transcripts/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture]] (p7+ deep dive: pairwise, decision tree, ELO)
