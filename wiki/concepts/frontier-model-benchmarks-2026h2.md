---
title: "Frontier-Model Benchmarks (ARC-AGI-3, LIFE, GAIA2, HLE, Vending-Bench 2, UEBench)"
created: 2026-09-13
updated: 2026-09-13
type: concept
tags: [benchmark, evaluation, frontier-models, reward-hacking]
sources:
  - raw/articles/arxiv-2609-04684-frontier-bench-suite.txt
confidence: medium
description: "A July–September 2026 benchmark matrix of six frontier evals (ARC-AGI-3, ARC-AGI-1, LIFE, GAIA2, Humanity's Last Exam, Vending-Bench 2, plus UEBench) run across seven frontier models, showing non-uniform capability landscapes and effort-dependent scores."
related: [benchmark-ceiling, arc-agi-3, reward-hacking, agents-last-exam, ai-benchmarks]
aliases: ["Frontier Model Benchmarks July-September 2026", "frontier bench suite"]
---

# Frontier-Model Benchmarks (ARC-AGI-3, LIFE, GAIA2, HLE, Vending-Bench 2, UEBench)

**Frontier-Model Benchmarks** refers to a September 2026 arXiv evaluation study (arXiv:2609.04684, "Frontier Model Benchmarks — July–September 2026") that ran one benchmark suite across seven frontier models — Claude Fable 5, GPT-5.5, GPT-5.4, GPT-5.2, Claude Opus 4.8, Grok 4.1, Muse Spark — and reported a **non-uniform capability landscape**: no model dominates every axis, and scores move with reasoning-effort settings and scaffolding. ([raw](raw/articles/arxiv-2609-04684-frontier-bench-suite.txt))

## Headline Numbers

| Benchmark | Best score | Model | Notes |
|---|---|---|---|
| ARC-AGI-3 public | 31.7% | GPT-5.4 (xhigh) | all frontier models < 3pt above random (27.8%); no solved games |
| ARC-AGI-1 semi-private | 84.6% | Fable 5 | 95.2% with 2× answer selection |
| LIFE (4000-token budget) | 35.3% | GPT-5.5 xhigh | 25.5% at low effort |
| GAIA2 | 44.8% | GPT-5.5 xhigh | full set 13.2%; hallucination axis 66% |
| Humanity's Last Exam | 53.3% | GPT-5.5 xhigh | |
| Vending-Bench 2 | −$7,350 | GPT-5.5 | best of six; five bankrupt, Fable 5 crashed at +$4,819 |
| UEBench (semantic utility) | 94.8% | Fable 5 | 77.3% public |

## Key Findings

1. **Abstract reasoning is still unsolved.** ARC-AGI-3 remains near-random for every frontier model — even Fable 5's "13-hour autonomous run" (see [[concepts/arc-agi-3]]) scored 0.50 normalized against 0.28 random. The capability that *is* near-saturated is the old one: ARC-AGI-1 at 84.6–95.2%.
2. **Long-context memory degrades sharply with budget.** On LIFE, scores collapse from 53.9% (full context) to 35.3% (4000-token budget) — "a long multi-session conversation compressed into one prompt is not the same thing as memory."
3. **Effort is a first-class variable.** LIFE: 25.5% → 35.3% low→xhigh; HLE: 46.2% → 53.3%; GPT-5.4 beats GPT-5.5 on 7 of 10 LIFE domains at *low* effort. Single-number "model X > model Y" claims are meaningless without the effort setting.
4. **Real-world agent loops still fail.** All six Vending-Bench 2 runs failed (bankruptcy or runtime crash) — operational failures, not reasoning failures. A different eval (UEBench, 14.9M tokens of consumer-electronics queries) shows the opposite: near-ceiling *semantic* quality (94.8%). Agent competence and answer quality are separate, uncoupled axes.
5. **Self-reported accuracy is unreliable.** One model misreported 12 of 400 LIFE answers as correct and 169 as wrong — a direct, measured case for the verification-first argument in [[concepts/evaluation-integrity]].
6. **Benchmark-specific regressions exist.** GPT-5.4 scored *worse* than GPT-5.2 on HLE and AIME-2025, with a mid-May discontinuity — a ceiling-adjacent artifact ([[concepts/benchmark-ceiling]]) rather than a capability story.

## Methodological Notes Worth Borrowing

- ARC-AGI-3 scores are reported against a **random-policy floor** (27.8% public / 22.7% private), not absolute % — the right frame for near-floor regimes.
- ARC-AGI-3 leaderboard runs use a **fresh container per run**; model-reported scores are unreliable because models misreport and the framework's own verification is incomplete.
- "Best score" ≠ best config: scores come from *different* configs per model (harness, scaffolding, effort, context budget, tool access).

## See Also

- [[concepts/benchmark-ceiling]] — why near-floor and near-ceiling regimes need different reporting
- [[concepts/arc-agi-3]] — detailed page on the ARC-AGI-3 results
- [[concepts/evaluation-integrity]] — contamination, self-report, and verification
- [[concepts/agents-last-exam]] — the closing-benchmark argument this suite implicitly tests
