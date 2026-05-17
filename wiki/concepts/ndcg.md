---
title: NDCG (Normalized Discounted Cumulative Gain)
created: 2026-05-17
updated: 2026-05-17
type: concept
tags: [evaluation, information-retrieval, search, benchmark]
sources: [raw/articles/2026-05-17_softwaredoug_search-evaluation-ndcg.md]
---

# NDCG (Normalized Discounted Cumulative Gain)

The de facto standard metric for search relevance evaluation. NDCG measures how well a ranked list of search results matches human judgments of relevance, normalized to a 0–1 scale.

## The Pipeline: Judgment List → DCG → iDCG → NDCG

### Step 1: The Judgment List (Ground Truth)

A set of query-document pairs with human-assigned relevance grades (typically 0–1 or 0–3):

| Query | Document | Grade (0-1) |
|-------|----------|-------------|
| Rambo | Rambo III | 0.8 |
| Rambo | First Blood | 1.0 |
| Rambo | Forrest Gump | 0.01 |
| Rocky | Rocky Balboa | 0.9 |
| Rocky | Creed | 0.8 |
| Rocky | Rambo | 0.5 |

aka: ground truth, relevance labels, judgments.

### Step 2: DCG (Discounted Cumulative Gain)

For each result position, multiply the grade by a position discount:

```
GAIN = GRADE × DISCOUNT(rank)
```

Where **discount** is typically `1 / log₂(rank + 1)`. Higher positions get more weight.

**Example**: For a query returning results with grades `[0.01, 1.0, 0.8]` at ranks 1–3:

| Grade | Rank | Discount (1/rank) | Gain |
|-------|------|-------------------|------|
| 0.01 | 1 | 1/1 = 1 | 0.01 × 1 = 0.01 |
| 1.0 | 2 | 1/2 = 0.5 | 1.0 × 0.5 = 0.5 |
| 0.8 | 3 | 1/3 = 0.333 | 0.8 × 0.333 = 0.267 |

**DCG@3** = 0.01 + 0.5 + 0.267 = **0.777**

Note: Some implementations use `(2^grade) - 1` instead of raw grade to amplify differences.

### Step 3: iDCG (Ideal DCG)

The maximum possible DCG — if results were sorted perfectly by grade:

| Grade | Rank | Discount | Gain |
|-------|------|----------|------|
| 1.0 | 1 | 1 | 1.0 |
| 0.8 | 2 | 0.5 | 0.4 |
| 0.01 | 3 | 0.333 | 0.0033 |

**iDCG@3** = 1.0 + 0.4 + 0.0033 = **1.403**

### Step 4: NDCG

```
NDCG = DCG / iDCG
```

For this example: **0.777 / 1.403 = 0.554**

This normalization forces the score between 0 and 1 across queries, enabling meaningful averaging across query sets.

## Sources of Judgment Labels

### 1. Human Raters

The gold standard but expensive.

**Pros**:
- High-quality explicit relevance judgments
- Can assess nuanced aspects like authority, freshness, intent match

**Cons**:
- Time-consuming and fatiguing ⏰
- Raters make mistakes — need inter-rater reliability metrics
- May need domain experts, not just crowdsourced raters (e.g., legal, medical search)
- Measures **explicit** preferences — people's public-facing judgments may differ from private behavior

**Relevance in practice**: "appropriateness, query/result interpretation in a public setting" — searching "cybertruck" should return reviews, not haters.

### 2. Clickstream-Based (Implicit)

Uses clicks, conversions, and other user behavior signals as implicit relevance judgments.

**Pros**:
- Massive scale — every user session generates data
- Measures **implicit** preferences: "Relevance == What people do in private when nobody is looking"
- Captures real behavior, not just stated preferences

**Cons**:
- **Position bias** — users click higher results regardless of relevance
- **Attractiveness bias** — compelling titles/snippets get more clicks
- Captures NSFW, drama, gossip, and other "private" interests that aren't publicly appropriate relevance

#### Click Models: COEC (Clicks Over Expected Clicks)

A simple method to convert click data into relevance grades by normalizing against expected clicks at each position:

```
COEC = Position Clicks / Expected Clicks (across all sessions)
```

**Example** for "First Blood" at query "Rambo":

| Position | Expected Clicks | Position Clicks | COEC |
|----------|----------------|-----------------|------|
| 1 | 1000 | 1250 | 1.25 |
| 2 | 800 | 950 | 1.1875 |
| 3 | 400 | 650 | 1.625 |
| **Average COEC** | | | **1.5833** |

The average COEC becomes the relevance grade for that query-document pair.

### 3. LLM as a Judge

Using language models to automatically label query-result pairs.

**Advantages**:
- Instant labeling at scale
- Can incorporate domain knowledge through prompts
- No rater fatigue

**Prompt Pattern** (from Umbrella, Lin et al.):

```
Given a query and a passage, provide a single integer score (0–3):

0 = nothing to do with the query
1 = related but does not answer
2 = somewhat answers (answer may be unclear or buried)
3 = dedicated to the query and contains exact answer

Steps:
1. Consider search intent and content match (M)
2. Measure passage trustworthiness (T)
3. Decide final score (O)

Format: ##final score: [score]
```

**Key considerations**:
- Descriptive labels matter — generic 0–3 scales miss domain-specific nuance
- Structured outputs (JSON, regex-constrained) improve reliability
- "Chain of thought-y" prompting improves accuracy
- Must validate LLM judge accuracy against human labelers

## When NDCG Goes Wrong

### Problem 1: Not Enough Ratings

Many results in the ranked list have no judgment labels:

| Grade |
|-------|
| 1.0 |
| 0.8 |
| ??? |

**Solution 1 — Pessimistic imputation**: Assume unrated = 0 (irrelevant). Simple but harsh.

**Solution 2 — NDCG-f (filtered)**: Only evaluate on rated results. Send a filter to the search engine:
```
q=rambo
Only return: Rambo III, Rambo II, First Blood, Forrest Gump…
```
"Work within a sample of rated results to improve relevance" — but also work to improve the sample itself.

### Problem 2: Bad Ideal DCG (Lack of Ratings)

If all rated results have low grades, even terrible search can achieve NDCG=1:

| Grade |
|-------|
| 0.1 |
| 0.05 |
| ??? |

**Solutions — Better iDCG variants**:

| iDCG Type | Grades Used | Measures |
|-----------|-------------|----------|
| **Local iDCG** | Max in retrieved top N | Precision in retrieved docs |
| **Global iDCG** | Max for all query labels | Recall + Precision |
| **Max iDCG** | Max label everywhere (1.0, 1.0, 1.0) | Recall + Precision + Content |

### Problem 3: NDCG Doesn't Measure Diversity

"Action Movies" returning 10 Rambo sequels = perfect NDCG, terrible user experience.

### Problem 4: NDCG Doesn't Measure UI Quality

Perfect results can still be "boring, few clicks, poor ratings" due to bad presentation.

### Problem 5: NDCG Requires Painstaking Data Work

**Clickstream challenges**: Enough clicks? Biases? Enough ratings per query? Sparsity on long tail?

**Human rater challenges**: Disagreement between raters? Enough results rated per query? Representative queries? Rater education and management?

### Problem 6: NDCG Requires Interpreting Information Need

"What's the user's actual intent?" — especially ambiguous queries. Unlabeled results aren't necessarily irrelevant (in research datasets like WANDS, unlabeled = irrelevant is assumed, but real life is more complex).

## What NDCG Actually Answers

NDCG is **not ground truth**. It answers narrow questions:

| Question | Answer |
|----------|--------|
| Did I impact the queries I expected? | ✅ |
| Did I impact them positively? | ✅ |
| Did I impact unexpected queries? | ❌ |

**Practical example**: An experiment to improve movie name search:

| Query | NDCG (Experiment A) | NDCG (Experiment B) |
|-------|---------------------|---------------------|
| rambo | 📈 | 📈 |
| rocky | 📈 | 📈 |
| movie about squirrels | 📈 | (no change) |
| movie with arnold | 📉 | (no change) |

Experiment A has higher overall NDCG, but it changed unexpected queries — 👎. Experiment B targeted only the expected queries — 👍. **Ship B**.

## Beyond NDCG

### Side-by-Sides (Underrated)

Give domain experts two result sets and ask for a preference. Simple, effective, often more informative than aggregate metrics.

### A/B Tests

Once you've verified offline that the change works as intended, run an A/B test. NDCG offline validation is a **unit test**, not a true "quality check."

### The "Just Ship It" Philosophy

Doug Turnbull's evolved view (2010s → 2025):

| 2010s Approach | 2025 Approach |
|----------------|---------------|
| Careful methodical testing | Ship behind feature flag |
| Staging → Prod gating | Continuous delivery |
| Build perfect offline eval infra | Analyze in prod |

**"Test in prod or live a lie"** — Charity Majors

**Don't build complex lab infra**: How to sample corpus representatively? Gather representative test queries? Match prod search engine setup? Match actual UI presentation? — these are endless rabbit holes.

**A real painful search project** (Doug's experience):
- 6 months: Build the perfect click → eval set
- 1 month: Actually tune search results
- Result: Project canceled — no impact delivered

### The "Grug-Brained" Cycle

```
ship → eval → analyze → iterate
         ↓
    slightly less grug-brained evals
         ↓
    (all while continuously shipping)
```

**What to do instead**:
1. Ship idea to prod (LGTM) behind feature flag
2. Ship iteration to prod
3. Get side-by-side preferences
4. Gather clickstream data incrementally
5. Baby-step toward better measurement + CD
6. Analyze features in prod, not in lab

### "Offline" Evaluation in Prod

Run NDCG with feature flag on/off in production — no separate "lab" world needed:
- Direct shadow traffic to change for perf measurement
- Change lives in main codebase
- Can easily turn into A/B test
- Can easily ship to all users

## Summary

NDCG is the industry-standard metric for search relevance, but it's a tool with sharp limitations. It answers "did I impact the queries I expected?" — not "did I improve search quality?" The best evaluation strategy combines NDCG with side-by-sides, A/B tests, and production observability, following the principle: **ship → evaluate → iterate**, not **build perfect eval → eventually ship**.

## See Also

- [[entities/softwaredoug]] — Doug Turnbull, author of the "Cheat at Search Essentials" training
- [Search Evaluation Slides](https://docs.google.com/presentation/d/1WJknXxaim_Z8aiVuQx6wr7W6MAWeaUJK0-NrgcEVQfQ) — Source presentation
- [Maven: Cheat at Search Essentials](https://maven.com/softwaredoug/cheat-at-search) — Course with promo code `ndcgrocks`
- [Colab: Synonym Notebook](https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1) — Hands-on exercises referenced in the talk
