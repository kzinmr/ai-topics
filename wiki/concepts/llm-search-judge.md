---
title: LLM Search Judge
type: concept
created: 2026-05-27
updated: 2026-06-03
aliases:
  - llm relevance judge
  - llm-as-a-judge for search
tags:
  - evaluation
  - search
  - model
  - structured-outputs
sources:
  - raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge.md
  - raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg.md
  - raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture.md
  - raw/articles/2026-06-01_llmdata-notes-on-choosing-rubric-judge.md
related:
  - concepts/ai-benchmarks/ndcg
  - concepts/query-understanding
  - concepts/bm25
  - entities/doug-turnbull
  - concepts/llm-as-judge
---

# LLM Search Judge

**LLM Search Judge** is the practice of using large language models to automatically evaluate search result relevance, replacing or supplementing expensive human labelers. It enables computation of standard IR metrics ([[concepts/ai-benchmarks/ndcg|NDCG]]) on unlabeled real-world query traffic, dramatically reducing the cost and turnaround time of relevance evaluation.

The technique was systematized by **Doug Turnbull** in Part 4 of his *Cheat at Search* course (2026), building on the Umbrella framework by Lin et al. and drawing on the broader "LLM as a Judge" paradigm (MT-Bench, AlpacaEval). The key insight is that while LLMs are not perfect judges (~73% pointwise agreement with humans), they are **consistent enough at a fraction of the cost** to enable rapid search iteration.

A "bitter lesson" from Turnbull's experiments: even a **naive judge** with zero domain-specific tuning ("is this relevant or not?") significantly improved search quality — suggesting that the bottleneck is not prompt engineering but the availability of any automated evaluation signal at all.

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

**Reported results (from live lecture experiments):**

| Configuration | Precision | Coverage | Notes |
|---|---|---|---|
| 3 features (name, desc, class) | 0.91 | 0.75 | At 80% confidence threshold |
| 4 features (+ product features) | 0.904 | 0.80 | Precision maintained, coverage ↑5% |

**Key insight — weak judges combine into strong predictions:** Individual pairwise judges achieve only ~73% accuracy, but when their outputs are combined as features in a decision tree, the ensemble reaches **91% precision** at an 80% confidence threshold on 75% of the data. This is the core "aha moment" — no single judge is reliable, but the combination is.

**Cheap models suffice:** Individual pairwise comparisons ("which product title is more relevant?") are simple enough for small local models (e.g., Qwen). Frontier models are only needed for complex reasoning; the per-comparison task is deliberately kept trivial.

**Decision tree as feature importance / opportunity analysis:** The tree's split structure reveals which attributes most affect relevance. When a new attribute (e.g., product features) is added as a judge:
- If precision holds and coverage increases → the attribute matters for search quality
- If precision drops → the attribute adds noise
- This doubles as a signal for **which product attributes to invest in** for the actual search index

## ELO-Based Pairwise → Pointwise Conversion

To bridge pairwise results back to pointwise metrics like NDCG, Turnbull uses **ELO rating** (chess tournament scoring):

1. Start each search result at ELO 100
2. Run pairwise "matches" — winner takes a portion of loser's ELO
3. Formula: `Δ = K × 1/(1 + 10^((loser_elo - winner_elo)/400))`
4. After many matches, ELO converges to a pointwise relevance score
5. Results in the demo converged to ELO range 50–150

This enables **back-and-forth between pairwise and pointwise universes** — pairwise for accurate comparisons, ELO-derived pointwise for NDCG computation.

## Recall Expansion via Diverse Queries

A critical limitation of LLM judges: they can only evaluate what they see. Poor recall means the best results may never be presented to the judge. Turnbull's mitigation:

- Require **minimum 4 BM25 tool calls**, all with different queries (duplicates = failure)
- This broadens recall so the judge sees more of the result space
- Analogous to **explore/exploit** in clickstream-based learning-to-rank
- **List-wise judging** (present a large set, ask LLM to re-rank) is theoretically more powerful for recall but remains untested

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

### [[concepts/ai-benchmarks/ndcg|NDCG]]
NDCG is the target metric; LLM search judging is the **label-generation method** that enables NDCG computation without human annotations. The two form a complete evaluation stack: LLM judges produce grades, NDCG normalizes and aggregates them.

### [[concepts/query-understanding|Query Understanding]]
Both are part of Doug Turnbull's Cheat at Search framework. LLM search judging evaluates the **output** of query understanding pipelines — it answers "did our QU improvements make search better?" QU transforms raw queries into structured attributes; judging verifies the result quality.

### Model-as-Judge (broader paradigm)
LLM Search Judge is a domain-specific instance of the broader **model-as-judge** pattern (MT-Bench for chatbots, AlpacaEval for instruction following, LLM-as-RAG-judge for retrieval). The search variant adds domain-specific concerns: position-aware metrics (NDCG discount), product attribute hierarchies, and double-checking for pairwise consistency.

## Domain Adaptation Guidance

When applying LLM Search Judge to non-e-commerce domains (legal RAG, job matching, etc.), Turnbull recommends:

1. **Start with 10 queries** from the target domain
2. Find an **"expert user"** — a domain specialist who can sit beside you and label results (e.g., a legal colleague for case law search)
3. Extract **pairs** from labeled data: "for this query, case A is more relevant than case B"
4. Prompt-engineer an LLM to reproduce the expert's pairwise judgments
5. **Relevance is domain-specific**: legal = case applicability, e-commerce = product match, social media = popularity. The evaluation attributes (product name, description) must be replaced with domain-relevant fields (e.g., job skills, case citations, document sections)

## Implicit vs. Explicit Judgment

Turnbull distinguishes between LLM judges and implicit user signals (clicks, engagement):

- **Trust implicit judgments** where available — they capture behavioral patterns LLMs cannot know (e.g., Shopify fashion users preferring plain black items over floral patterns)
- **Use LLM judges for tail queries** where click data is sparse — long-tail or novel queries have insufficient implicit signal
- **Implicit judgments have biases**: "lizard brain" click behavior (visual appeal, position bias) does not always equal relevance
- The two signals are **complementary**, not competing

## Pitfalls & Limitations

- **Position bias in LLM outputs:** LLMs may systematically prefer LHS or RHS regardless of relevance. Double-checking with swapped positions mitigates this.
- **Combining judges requires labeled ground truth:** The decision tree approach needs some human-labeled data for training — it doesn't eliminate human labeling entirely, but makes each label go further.
- **Domain adaptation:** 73% agreement on e-commerce doesn't guarantee similar performance on legal, medical, or technical search.
- **Cost still matters:** While cheaper than humans, running pairwise LLM judges on 10K+ query-result pairs isn't free. Caching, batching, and cheap model selection (gpt-4.1-nano) are essential.

## Rubric Judges for RL Training (The LLM Data Company, 2026)

The LLM Data Company's [rubric judge study](https://www.llmdata.com/blog/rubric-judge) examines the same LLM-as-judge paradigm from the **RL training** perspective rather than search evaluation. The connection is deep:

### Convergent Findings

| Dimension | Search Judge (Turnbull) | Rubric Judge (LLM Data Co.) |
|-----------|------------------------|----------------------------|
| **Core insight** | Weak judges combine into strong predictions | Well-designed rubrics make cheap judges match expensive ones |
| **Aggregation** | Decision tree over pairwise judges | Full-rubric grading (one call for all criteria) |
| **Cost discovery** | Cheap local models (Qwen) suffice per comparison | gpt-oss-120b at $0.001/run matches Opus 4.7 at $0.076 |
| **Criteria design** | Specialized per-attribute judges > all-in-one | Explicit rule-like criteria > standard-like criteria |
| **Model scaling** | Frontier models only needed for complex reasoning | Reasoning buys marginal F1 (0.002–0.010) at huge latency cost |

### Divergent Approaches

- **Grading mode**: Turnbull uses **pairwise** (A vs B → preference), then aggregates via ELO/decision tree. LLM Data Co. uses **full-rubric** (one call grades all criteria as MET/UNMET). Both beat per-criterion approaches.
- **Domain scope**: Turnbull's search judges evaluate **relevance** (is this result good for this query?). Rubric judges evaluate **correctness** (does this output satisfy medical criteria?). The former is relative, the latter is absolute.
- **Reward hacking**: The rubric judge article explicitly addresses reward hacking as the primary risk — underspecified criteria become exploit surfaces for RL optimization. Turnbull's search judges face analogous risks (position bias, all-in-one prompt gaming).

### Synthesis: Criteria Design > Model Choice

Both lines of research converge on one principle: **the quality of the evaluation criteria matters more than the model running the judge.** Turnbull shows that multiple cheap specialized judges outperform one expensive all-in-one judge. LLM Data Co. shows that explicit rubric criteria eliminate the need for expensive judge models entirely.

For search RL (e.g., training retrieval agents), this suggests: design the reward rubric with explicit, rule-like criteria for each relevance dimension (precision, recall, freshness, authority), then use cheap judges per dimension, aggregated by a decision tree or weighted sum — not a single frontier model making holistic judgments.

### Implications for Agentic Search

The rubric judge framework extends naturally to [[concepts/agentic-search|agentic search]] evaluation:
- **Document-centric reward** (SID-1's NDCG) is a rubric with one criterion: retrieval quality
- **Multi-criteria rubrics** could evaluate agent search behavior: query diversity, result coverage, tool usage efficiency, answer grounding
- **Reward hacking in search RL** mirrors the rubric case: agents can game NDCG by over-reporting or gaming recall metrics

## References

- **Doug Turnbull**, *Cheat at Search Part 4: LLM as a Judge* (slides), 2026 — [[raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge]]
- **Doug Turnbull**, *Cheat at Search Part 4: LLM as a Judge* (lecture transcript), 2026 — [[raw/articles/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture]]
- **Doug Turnbull**, *Search Evaluation: NDCG* (blog), 2026 — [[raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg]]
- **Lin et al.**, *Umbrella: A Framework for LLM-based Search Evaluation*
- **Turnbull & Grainger**, *AI-Powered Search* (Manning, 2025)
- **The LLM Data Company**, *Notes on Choosing a Rubric Judge*, 2026 — [[raw/articles/2026-06-01_llmdata-notes-on-choosing-rubric-judge]]
- **Mahmoud et al.**, *Reward Hacking in Rubric-Based RL*, 2026
- **Rao & Callison-Burch**, *AutoRubric: Unifying Rubric-based LLM Evaluation*, 2026
