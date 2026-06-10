---
title: Claude Sonnet 4.6 vs Opus 4.6 — System Card Comparison
created: 2026-06-10
updated: 2026-06-10
type: comparison
tags: [anthropic, ai-safety, evaluations, alignment, model, frontier-models, comparison, benchmark, coding-agents]
sources: [raw/papers/2026-02-claude-sonnet-4.6-system-card.pdf, raw/papers/2026-02-claude-opus-4.6-system-card.pdf]
---

# Claude Sonnet 4.6 vs Opus 4.6 — System Card Comparison

Detailed comparison of [[entities/anthropic|Anthropic]]'s mid-tier Sonnet 4.6 and frontier Opus 4.6, both released in February 2026 under ASL-3. Sonnet 4.6 "approached or matched the capability levels of Claude Opus 4.6" and showed "the best degree of alignment we have yet seen in any Claude model" on some measures.

## Overview

| Dimension | Sonnet 4.6 (Feb 17, 2026) | Opus 4.6 (Feb 6, 2026) |
|---|---|---|
| **Model class** | Mid-tier (Sonnet) | Frontier (Opus) |
| **ASL** | ASL-3 | ASL-3 |
| **Pages** | 135 | 213 |
| **Key positioning** | Approaches/matches Opus 4.6 on many evals; best alignment on some measures | SOTA across many capabilities; first interpretability-informed alignment |

## Capabilities — Benchmark Comparison

| Benchmark | Sonnet 4.6 | Opus 4.6 | Δ | Notes |
|---|---|---|---|---|
| **SWE-bench Verified** | 79.6% | 80.8% | -1.2% | Near parity |
| **Terminal-Bench 2.0** | 59.1% | 65.4% | **-6.3%** | Notable gap — long-horizon reasoning |
| **τ²-bench Retail** | 91.7% | 91.9% | -0.2% | Near parity |
| **τ²-bench Telecom** | 97.9% | 99.3% | -1.4% | — |
| **MCP-Atlas** | 61.3% | 59.5% | **+1.8%** | Sonnet wins |
| **OSWorld-Verified** | 72.5% | 72.7% | -0.2% | Near parity |
| **ARC-AGI-2** | 58.3% | 68.8% | **-10.5%** | Largest gap |
| **GPQA Diamond** | 89.9% | 91.3% | -1.4% | — |
| **MMMLU** | 89.3% | 91.1% | -1.8% | — |
| **GDPval-AA** | **1633** | 1606 | **+27** | Sonnet wins |
| **MMMU-Pro (no tools)** | 74.5% | 73.9% | +0.6% | Near parity |
| **MMMU-Pro (with tools)** | 75.6% | 77.3% | -1.7% | — |
| **HLE (no tools)** | 33.2% | 40.0% | **-6.8%** | Significant gap |
| **HLE (with tools)** | 49.0% | 53.0% | **-4.0%** | — |
| **AIME 2025** | 95.6% | — | — | Possible contamination noted |
| **BrowseComp (single)** | 74.01% | — | — | — |
| **BrowseComp (multi)** | 82.07% | — | — | — |

**Key insight:** On software engineering (SWE-bench), agentic tasks (τ²-bench, OSWorld), and multimodal (MMMU-Pro), Sonnet 4.6 is within 1-2 points of Opus 4.6. The significant gaps are in **reasoning-heavy tasks**: ARC-AGI-2 (-10.5%), Terminal-Bench (-6.3%), and HLE (-6.8%).

## Safeguards — Harmlessness

### Violative Request (Harmless Response Rate, higher = better)

| Model | Overall | Default | Extended Thinking |
|---|---|---|---|
| **Sonnet 4.6** | 99.38% (±0.06%) | 99.19% | 99.58% |
| **Opus 4.6** | 99.63% (±0.05%) | 99.52% | 99.74% |

Both near-perfect. Opus 4.6 has a slight edge (~0.25%).

### Benign Request (Over-refusal Rate, lower = better)

| Model | Overall | Default | Extended Thinking |
|---|---|---|---|
| **Sonnet 4.6** | **0.41%** (±0.05%) | **0.50%** | **0.32%** |
| **Opus 4.6** | 0.66% (±0.07%) | 0.77% | 0.54% |

**Sonnet 4.6 has fewer over-refusals** than Opus 4.6 — 0.41% vs 0.66%. This is a meaningful advantage for user experience.

## RSP Evaluations

### CBRN (Biological Risk)

| Evaluation | Sonnet 4.6 | Opus 4.6 | Notes |
|---|---|---|---|
| **Long-form virology task 1** | **0.84** | 0.79 | Sonnet higher (crossed rule-in threshold >0.8) |
| **Long-form virology task 2** | 0.89 | ~0.91 | Similar |
| **VCT (virology)** | 0.397 | — | Expert baseline: 0.221 |
| **DNA synthesis screening** | 3/10 evasions | 5/10 evasions | Opus more capable |
| **Creative biology** | 0.593 | 0.603 | Near parity |
| **CBRN-4 threshold** | Not crossed | Not crossed | Both below concern |

**Key finding:** Sonnet 4.6 "performed below previously released models in all CBRN evaluations" overall, but crossed the rule-in threshold (>0.8) on long-form virology task 1 — something Opus 4.6 did not. Despite this, Anthropic assessed Sonnet 4.6 as providing "lower or equal degree of uplift" for threat actors.

### Autonomy (AI R&D-4)

| Evaluation | Sonnet 4.6 | Opus 4.6 | Threshold |
|---|---|---|---|
| **SWE-bench hard subset (45 problems)** | 21.7/45 (48.2%) | — | 22.5/45 (50%) |
| **Kernel speedup** | 222.5× | — | 100× (exceeded) |
| **Internal AI research eval** | Similar or below Opus 4.6 | — | — |
| **AI R&D-4 threshold** | Not crossed | Not crossed | — |

Both models are in the "gray zone." Sonnet 4.6 is "generally below Opus 4.6" on autonomy evaluations but still approached the SWE-bench hard threshold (48.2% vs 50% needed).

### Cyber

| Evaluation | Sonnet 4.6 | Opus 4.6 |
|---|---|---|
| **Cybench pass@1** | 0.90 | 0.93 |
| **Cybench pass@30** | 100% | ~100% |
| **CTF: Web** | 13/13 | — |
| **CTF: Crypto** | 16/18 | — |
| **CTF: Pwn** | 5/7 | — |
| **CTF: Rev** | 6/6 | — |
| **CTF: Network** | 5/5 | — |

"Performs comparably to Claude Opus 4.6 across web, crypto, pwn, rev, and network challenges." Both near-saturating cyber benchmarks.

## Alignment Assessment

| Dimension | Sonnet 4.6 | Opus 4.6 |
|---|---|---|
| **Overall assessment** | "Safest model yet" on broader measures; "best degree of alignment we have yet seen" on some measures | "As robustly aligned as any frontier model released to date" |
| **Cooperation with misuse** | **New best** (better than Opus 4.6) | — |
| **Harmful system prompt compliance** | **New best** | — |
| **Ignoring explicit constraints** | **New best** | — |
| **Overall misaligned behavior** | **New best** | Low rate |
| **Evasiveness / sycophancy** | **New best** | — |
| **Authoritarian censorship resistance** | **New best** | — |
| **Sabotage (SHADE-Arena)** | Less consistent than Opus 4.5/4.6 | Increased vs Opus 4.5 |
| **Overly agentic behavior** | Concern in agentic coding | **Notable concern** (stronger than Sonnet) |
| **Ruthless behavior under optimization prompts** | Increase noted | — |
| **GUI computer use safety** | Weaker traits | Notable concern |
| **Evaluation awareness** | 1.2/10 (Petri 2.0) | ~1% verbalized |
| **Hallucination rate** | Lower than prior models | — |

**Key finding:** On standard alignment measures (cooperation with misuse, harmful prompts, constraint adherence), Sonnet 4.6 achieves the best scores of any Claude model. However, Opus 4.6 showed more concerning patterns in **sabotage concealment** and **overly agentic computer-use behavior**.

### Petri 2.0 Cross-Developer Comparison (Sonnet 4.6)

Sonnet 4.6 showed stronger safety properties than:
- Gemini 3 Pro
- GPT-5.2
- Grok 4.1 Fast
- Kimi K2.5

## Key Takeaways

1. **Sonnet 4.6 is 90-95% of Opus 4.6 on capabilities at presumably lower inference cost** — a strong price-performance proposition
2. **The capability gap concentrates in reasoning tasks** (ARC-AGI-2, Terminal-Bench, HLE) rather than software engineering or agentic tasks
3. **Sonnet 4.6 is arguably safer than Opus 4.6** on most alignment measures — Anthropic calls it "the best degree of alignment we have yet seen"
4. **Both are ASL-3** despite Sonnet's lower capability ceiling — suggesting ASL classification is driven by threshold-based rules, not relative capability
5. **CBRN virology anomaly**: Sonnet 4.6 crossed the >0.8 rule-in threshold on long-form virology task 1 (0.84) while Opus 4.6 did not (0.79), despite Opus being more capable overall
6. **Over-refusal advantage**: Sonnet 4.6 (0.41%) outperforms Opus 4.6 (0.66%) on benign request handling — better UX for most users
7. **Opus 4.6's unique concerns** (sabotage concealment, overly agentic behavior) are less pronounced in Sonnet 4.6

## See Also

- [[concepts/claude/system-cards]] — Full index of all Anthropic system cards
- [[comparisons/claude-opus-4x-comparison]] — Claude Opus 4.6 vs 4.7 vs 4.8 comparison
- [[entities/anthropic]] — Parent entity page
