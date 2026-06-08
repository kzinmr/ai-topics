---
title: "Cheat at Search Part 4 — LLM as a Judge (Lecture Transcript)"
author: Doug Turnbull (@softwaredoug)
date: 2026-05-28
date_ingested: 2026-06-03
source: https://docs.google.com/presentation/d/16hw0veoCQYKN8hPr8N4EGnXNfUOegGnvKzMpaGZjQjo/edit
type: transcript
tags:
  - search
  - evaluation
  - model
  - evaluation
  - search
---

# Cheat at Search Part 4 — LLM as a Judge (Lecture Transcript)

**Speaker:** Doug Turnbull / SoftwareDoug LLC
**Context:** Live lecture for Cheat at Search Essentials (Maven course), Part 4. This transcript covers the discussion portion starting from approximately slide p7 — the deeper dive into pairwise judging, decision tree aggregation, and ELO-based pointwise recovery.
**Series:**
- Part 1: NDCG / Search Evaluation
- Part 2: LLM Query Understanding
- Part 3: Steering Lost Agents (Agentic Design Patterns)
- Part 4: LLM as a Judge (this lecture)

**Participants:** Doug Turnbull (speaker), hev, Zenit, Joel Turner, Eric Alonas, Joey

---

## Two Feedback Loops

Doug frames LLM-as-a-Judge as having two feedback loops:

1. **Human labelers → LLM Judge**: Can the LLM reproduce human relevance judgments? (Focus of this lecture)
2. **LLM Judge → Search tuning / agent steering**: Use the judge to direct the agentic flow or traditional search tuning.

**Key experiment finding:** Even a naive judge with zero domain tuning ("is this relevant or not?") improved search quality significantly. hev commented: "Sounds like a bitter lesson."

## Pointwise vs. Pairwise Paradigm Shift

### Pointwise (dominant but noisy)

- Single query + single result → grade 0–3
- Descriptive labels (not numbers) help LLMs: "nothing to do with the query" is easier to classify than "score 0"
- **73% agreement** with humans (GPT-4.1) — decent but not production-ready
- At ~90% accuracy, human labelers themselves start being the source of errors (e.g., mislabeling wool products from images when the LLM correctly reads the description)

### Pairwise (Doug's preferred approach)

- Two results (LHS, RHS) → which is more relevant?
- **Much lower noise per decision** — binary comparison is easier than abstract grading
- **Chess tournament metaphor**: 10 results → ₁₀C₂ = 45 comparisons (or 90 with double-checking)
- LLMs can do unlimited comparisons, unlike human labelers
- **Double-checking**: Swap LHS/RHS and re-evaluate. Inconsistent results → unknown (filtered out)

### Precision/Coverage by attribute

| Judge Type | Precision | Coverage |
|---|---|---|
| Product Name | 0.73 | 0.84 |
| Product Description | 0.67 | 0.75 |
| Product Classification | 0.81 | 0.89 |
| All-in-one prompt | 0.74 | 0.81 |

**Critical finding:** All-in-one prompt (all attributes at once) performs **worse** than individual specialized judges.

## Decision Tree Aggregation (Key Insight)

### The "aha moment"

Individual pairwise judges produce noisy signals (-1 = LHS, +1 = RHS, 0 = unknown). Rather than treating any single judge as reliable, feed all judge outputs as **features** into a decision tree that predicts human ground truth:

```
X1 = name judge preference
X2 = description judge preference
X3 = classification judge preference
→ DecisionTreeClassifier → ground truth prediction
```

### Why this works

1. **Weak judges combine into strong predictions**: Individual 73% accuracy judges → 91% precision at 80% threshold on 75% of data
2. **Cheap models suffice**: Simple pairwise comparisons ("which product title is more relevant?") can run on small local Qwen models — no frontier model needed
3. **Explainability**: The decision tree is a human-readable scoring flowchart showing which features matter most

### Results with different feature sets

| Configuration | Precision | Coverage |
|---|---|---|
| Name + Desc + Class (3 features) | 0.91 | 0.75 |
| + Features attribute (4 features) | 0.904 | 0.80 |

Adding the "product features" attribute maintained precision while increasing coverage from 75% → 80%. This doubles as an **opportunity analysis**: if a new attribute improves the judge, it likely matters for the actual search algorithm too.

### Decision tree as feature importance tool

The tree's split structure reveals which attributes most affect relevance:
- Top split = most important feature (usually product name)
- Lower splits = secondary features
- Stakeholders can read the tree as a scoring flowchart

## Recall Expansion Strategy

Zenit raised the problem of **bad recall** — the LLM judge can only label what it sees. Doug's approach:

- Require **minimum 4 BM25 tool calls**, all with different queries
- This broadens recall so the judge sees more of the result space
- Similar to **explore/exploit** in clickstream-based learning-to-rank: show users slightly off-edge results to discover what they react to
- **List-wise approach** (judge sees a very large set and re-ranks) could be even more powerful but is untested

## ELO for Pairwise → Pointwise Conversion

To bridge pairwise results back to pointwise metrics (NDCG):

- Start each result at ELO 100
- Run pairwise "matches" — winner takes a portion of loser's ELO
- Formula: Δ = K × 1/(1 + 10^((loser_elo - winner_elo)/400))
- After many matches, ELO converges to a pointwise relevance score
- Results in this demo: ELO range 50–150 after convergence
- Could apply sigmoid scaling for bounded scores

## Domain-Specific Application (Q&A)

### Joel Turner: How to apply this to non-e-commerce (legal RAG)?

Doug's recommendation:
1. **Start with 10 queries** from the domain
2. Find an **"expert user"** (e.g., a legal colleague) to label results
3. Extract pairs from labeled data: "for this query, case A is more relevant than case B"
4. Prompt-engineer an LLM to reproduce the expert's pairwise judgments
5. **Relevance is domain-specific**: legal = case applicability, e-commerce = product match, social media = popularity

### Eric Alonas: Decision tree vs. all-in-one LLM?

Decision tree with individual judges **outperformed** giving the LLM all attributes at once. The all-in-one prompt scored lower than even just the product classification judge alone.

### Zenit: Implicit judgment vs. LLM judge?

- **Trust implicit judgments** (clicks) where available — they capture patterns LLMs can't know (e.g., Shopify fashion users preferring plain black items)
- **Use LLM judges for tail queries** where click data is sparse
- Implicit judgments have "lizard brain" biases (visual appeal ≠ relevance)

## Comparison with Existing Slides Wiki

This transcript adds the following to the slides-based raw article:
1. **73% → 91% improvement path**: weak judges → decision tree → threshold = 91% precision
2. **Features attribute coverage boost**: 75% → 80%, precision maintained
3. **ELO-based pointwise recovery** mechanism
4. **Recall expansion via forced diverse BM25 calls** (min 4, all different)
5. **Naive judge still helps** — the "bitter lesson" of search evaluation
6. **Domain application guidance** for non-e-commerce use cases
7. **Implicit vs. explicit judgment** tradeoffs
8. **Cheap local models** (Qwen) sufficient for individual pairwise judges

---

## Related Concepts

- [[concepts/llm-search-judge]]
- [[concepts/ndcg]]
- [[concepts/query-understanding]]
- [[concepts/agentic-search]]
- [[concepts/bm25]]
- [[entities/doug-turnbull]]

## Related Raw Articles

- [[raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge]] (slides — source material for this transcript)
- [[raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg]] (Part 1)
- [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search]] (Part 2)
- [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents]] (Part 3)
