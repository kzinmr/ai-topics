---
title: "What Is a Judgment List?"
author: Doug Turnbull
date_published: 2021-02-21
source_url: https://softwaredoug.com/blog/2021/02/21/what-is-a-judgment-list
type: raw_article
tags: [search, evaluation, methodology, information-retrieval]
---

# What Is a Judgment List?

> **Original**: [softwaredoug.com](https://softwaredoug.com/blog/2021/02/21/what-is-a-judgment-list)
> **Author**: Doug Turnbull (@softwaredoug)
> **Published**: 2021-02-21

---

## 1. Why Judgment Lists Matter

Search teams often fear that fixing one query will break many others — a "whack-a-mole" cycle. A judgment list provides a safety net: it defines exactly what's relevant for each query, so changes can be tested objectively.

**Core definition:** A judgment list records a document's relevance grade for a query (e.g., 0 = irrelevant, 1 = relevant).

Example (movie search engine):

```
query,       movie,                            grade
star wars,   "Star Wars: A New Hope",          1
star wars,   "Return of The Jedi",             1
star wars,   "Blair Witch Project",            0
star wars,   "A Star Is Born",                 0
star trek,   "Star Trek Into Darkness",        1
star trek,   "Star Trek II: The Wrath of Khan", 1
star trek,   "Sense and Sensibility",          0
star trek,   "Forrest Gump",                   0
```

---

## 2. Using Judgment Lists for Evaluation

Given a judgment list, replace search results with their grades and compare the ranking to the ideal order.

**Example ranking for `star wars`:**
1. Return Of The Jedi → grade 1
2. Star Wars: A New Hope → grade 1
3. A Star Is Born → grade 0
4. Blair Witch Project → grade 0

Graded list: `[1, 1, 0, 0]` (good: relevant first). A poorer ranking `[0, 0, 1, 1]` would be worse.

---

## 3. Measuring Relevance: Discounted Cumulative Gain (DCG)

DCG assigns higher weight to top positions and sums discounted gains.

**Formula (simplified):** `DCG = Σ (grade / rank)` for each position.

**Poor ranking `[0, 0, 1, 1]` DCG@4:**

| Rank | Grade | Discount (1/rank) | Gain | Accumulated |
|------|-------|--------------------|------|-------------|
| 1    | 0     | 1.0                | 0    | 0.0         |
| 2    | 0     | 0.5                | 0    | 0.0         |
| 3    | 1     | 0.33               | 0.33 | 0.33        |
| 4    | 1     | 0.25               | 0.25 | **0.58**    |

**Ideal ranking `[1, 1, 0, 0]` DCG@4:**

| Rank | Grade | Discount | Gain | Accumulated |
|------|-------|----------|------|-------------|
| 1    | 1     | 1.0      | 1.0  | 1.0         |
| 2    | 1     | 0.5      | 0.5  | 1.5         |
| 3    | 0     | 0.33     | 0.0  | 1.5         |
| 4    | 0     | 0.25     | 0.0  | **1.5**     |

Ideal DCG@4 = 1.5, poor = 0.58. The metric quantifies improvement.

---

## 4. Iterating with Confidence (Test-Driven Relevancy)

A judgment list acts like a unit test for search:

- **Quickly prototype ranking changes** at your laptop, run an evaluation (e.g., in Quepid), and see regressions instantly.
- **Prevent harmful fixes.** If a tweak improves one query but hurts overall DCG, you know not to ship it.
- **Encourage innovation.** With a robust safety net, teams can boldly explore new ranking ideas without fear of silently degrading search.

No need for full A/B or user testing at every step — tests can run locally.

---

## 5. Frequently Asked Questions

### Where do judgments come from?

Three main sources, each with trade-offs:

- **Implicit judgments:** from user behavior (clicks, purchases, conversions). Good for high-traffic, general domains. Requires careful processing (raw CTR alone can be misleading). Covered in *AI Powered Search*, Ch. 11.
- **Crowdsourced judgments:** using platforms like Mechanical Turk, Appen, or Supahands. Scales well; quality depends on clear instructions.
- **Explicit judgments:** human evaluators in a UX-study setting give direct feedback. Works well for domain-specific users with low traffic.

**Key insight:** There is no single "golden set." Each method provides a different lens. Use multiple judgment systems to get diverse perspectives. This is why Turnbull prefers the term **"judgment"** over "golden set" or "ground truth."

### Implementation choices

- **Binary (0/1):** simple, but coarse.
- **Categorical (e.g., 0–4):** with clear definitions. Example for job search:
  > 0 – It's not worth ever applying
  > 1 – Unlikely I would apply
  > 2 – 50/50
  > 3 – I would apply
  > 4 – I would put a high level of effort (call hiring manager, etc.)
- **Probabilities (0.0–1.0):** common from implicit feedback like normalized CTR.

Match the grading scheme to the domain and judgment creation method.

### How to know if judgments are any good?

- **Compare to other judgment methods** — use rank correlation metrics like **Kendall's Tau** to find agreement and differences. Disagreement often reveals valuable insights.
- **A/B test your judgments** — build a search that returns the ideal ranking per your list; if it performs well on KPIs, the judgments are directionally correct.

---

## Key Takeaways

1. A judgment list is a **quantitative safety net** that replaces subjective evaluation with repeatable measurement.
2. DCG (Discounted Cumulative Gain) translates ranked results into a single numeric score, rewarding early relevant hits.
3. Judgments come from implicit (user behavior), crowdsourced, and explicit (human rater) sources — no single method is "ground truth."
4. A judgment list enables **test-driven relevancy**: iterate fast, measure impact, ship confidently.
5. Use multiple evaluation systems to get diverse perspectives on search quality.
