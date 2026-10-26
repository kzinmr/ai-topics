---
title: "Test-Time Compute"
type: concept
aliases:
  - test-time-compute
  - TTC
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - reasoning
  - test-time-scaling
  - inference
  - token-economics
related:
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/inference-time-compute]]"
  - "[[concepts/sleep-time-compute]]"
  - "[[concepts/elo-per-token-analysis]]"
  - "[[concepts/machine-studying]]"
sources:
  - "[[queries/test-time-compute-three-axes-2026-09-24]]"
  - raw/articles/2026-09-23_arxiv_2504.13171_sleep-time-compute.md
  - raw/articles/2026-09-23_arxiv_2609.15309_elo-per-token-test-time-strategies.md
---

# Test-Time Compute

**Test-time compute (TTC)** is the compute a model spends solving a given problem at inference time — thinking tokens, samples, search, tool calls. It became the dominant capability lever after o1/R1 showed that reasoning models trained to exploit it can outperform much larger non-reasoning models. This page is the **concept hub**; the detailed technical treatment lives in [[concepts/test-time-scaling]].

## The Three Axes (wiki synthesis, Sep 2026)

Per [[queries/test-time-compute-three-axes-2026-09-24]], the compute-vs-accuracy frontier has three axes, and benchmarks only measure the middle one:

| Axis | Question | Measured? | Representative |
|---|---|---|---|
| **Before the query** | What can I precompute offline? | Barely | [[concepts/sleep-time-compute]] (~5× less test-time compute at same accuracy) |
| **At the query** | How many tokens should I spend? | Yes — pass@k, Elo | [[concepts/test-time-scaling]] |
| **After the peak** | Does the next token still help, or hurt? | Only via Elo-per-token | [[concepts/elo-per-token-analysis]] (post-peak degradation: self-contradiction, context loss, misleading feedback) |

## Key Ideas

- **More compute ≠ monotonically better.** Accuracy peaks, then marginal tokens become negative-value; there is no universal fix (context preservation helps some models, verification others).
- **Efficiency, not just spending.** [[concepts/machine-studying]] frames expertise as the *weighted area under* the performance-vs-compute curve, not its endpoint — the frontier is becoming cheap at spending compute, not just spending more.
- **Budget control as interface.** Practical knobs: token budgets (s1-style), budget forcing, guidance schedulers (Cadence's +25.33% on mini-swe-agent with ~60% fewer guidance calls).

## Related Concepts

- [[concepts/test-time-scaling]] — canonical deep-dive (scaling laws, parallel vs sequential, RLVR)
- [[concepts/inference-time-compute]] — general concept and economics of inference-side compute
- [[concepts/chain-of-thought]] — the original cheap TTC technique
- [[concepts/token-economics]] — cost framing of the same axis

## Graph Structure Query

```
[test-time-compute] ──has-canonical-page──→ [concept: test-time-scaling]
[test-time-compute] ──synthesized-in──→ [query: test-time-compute-three-axes-2026-09-24]
[test-time-compute] ──relates-to──→ [concept: sleep-time-compute]
[test-time-compute] ──contrasts──→ [concept: training-time scaling]
```

## Sources

- [[queries/test-time-compute-three-axes-2026-09-24]]
- arXiv:2504.13171 (sleep-time compute), arXiv:2609.15309 (Elo-per-token) — see raw articles in frontmatter
