---
title: "Test-Time Compute Has Three Axes — And Only Two Get Benchmarked"
created: 2026-09-24
updated: 2026-09-24
type: query
tags: [test-time-scaling, token-economics, agent-evaluation, ai-agents, inference]
sources:
  - raw/articles/2026-09-23_arxiv_2609.15309_elo-per-token-test-time-strategies.md
  - raw/articles/2026-09-23_arxiv_2504.13171_sleep-time-compute.md
  - https://jacobxli.com/blog/2026/machine-studying/
related:
  - "[[concepts/sleep-time-compute]]"
  - "[[concepts/elo-per-token-analysis]]"
  - "[[concepts/machine-studying]]"
  - "[[concepts/test-time-compute]]"
  - "[[concepts/token-economics]]"
confidence: medium
---

# Test-Time Compute Has Three Axes — And Only Two Get Benchmarked

## Synthesis

Three pages ingested around 2026-09-23 ([sleep-time-compute](../sleep-time-compute.md), [elo-per-token-analysis](../elo-per-token-analysis.md), [machine-studying](../machine-studying.md)) turn out to be one story told from three ends: the *compute-vs-accuracy frontier* has **three axes**, and the field only measures the middle one.

| Axis | Question | Measured? | Representative |
|---|---|---|---|
| **Before the query** | What can I precompute offline? | Barely | [sleep-time compute](../sleep-time-compute.md) (~5× less test-time compute for same accuracy; +13–18% accuracy) |
| **At the query** | How many tokens should I spend? | Yes — pass@k, Elo | [test-time scaling](../test-time-compute.md) |
| **After the peak** | Does the next token still help, or hurt? | No — until Elo-per-token | [elo-per-token analysis](../elo-per-token-analysis.md) (3 failure modes: self-contradiction, context loss, misleading feedback) |

## The Contrarian Read

- Benchmarks report a **single number at a single budget**. Elo-per-token shows accuracy can *degrade* past a peak — agents get worse with more tokens. A benchmark that stops at the plateau measures the wrong thing.
- "More inference compute = better" is only true pre-peak. Post-peak, marginal tokens are **negative-value**: they burn budget and inject self-contradiction. There is no universal fix — context preservation helps GPT-5, verification helps DeepSeek.
- Machine studying is the third leg: the frontier is not just *spending* compute but *becoming efficient* at spending it. Expertise = **weighted area under the performance-vs-compute curve**, not the endpoint. The Qwen3.5-9B study results (baseline 3.3→11.6%, SFT+OPSD 9.4→8.5% and *degrading* at high budget) show current "studying" buys low-budget fluency, not high-budget expertise.
- Economic frame: sleep-time compute is an **arbitrage** — idle GPU cycles vs latency-critical request-path cycles ([token economics](../token-economics.md)). Elo-per-token is the **marginal-price gauge** that tells you when the arbitrage is exhausted.

## Open Thread

No one has published a scheduler that spans all three axes: sleep budget → test-time budget → online stop-truncation at the pre-peak/post-peak boundary. Each paper solves one quadrant. The composite is the actual deployment problem.

## Sources

- arXiv:2609.15309 — When Agents Slow Down (Liu, Mang, et al., Sep 2026)
- arXiv:2504.13171 — Sleep-time Compute (Lin, Snell, et al., Letta/UC Berkeley, Apr 2025)
- jacobxli.com — Machine Studying (Li, Battle, Khattab, MIT CSAIL/Broadcom, Jun 2026)
