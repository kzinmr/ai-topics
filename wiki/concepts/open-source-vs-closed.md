---
title: "Open-Source vs Closed-Source LLM Gap"
type: concept
aliases:
  - open-source-vs-closed
  - open-weight-vs-frontier
created: 2026-04-25
updated: 2026-06-28
tags:
  - concept
  - open-source
  - benchmark
  - prediction
  - evaluation
related:
  - concepts/open-weight-vs-closed-llm-gap
  - concepts/ai-benchmarks/index
  - concepts/open-source-ai-must-win
sources:
  - raw/articles/2026-06-22_doubleword-open-source-vs-closed-llm-gap.md
status: active
---

# Open-Source vs Closed-Source LLM Gap

## Overview

On June 22, 2026, Jamie Dborin (Founder & MTS, Doubleword) published a data-driven analysis using [[concepts/ai-benchmarks/index|Artificial Analysis benchmarks]] to predict when open-weight LLMs will match frontier closed-source models. The headline finding: **a linear projection of the Artificial Analysis Intelligence Index suggests the gap reaches zero around December 3, 2026**. However, when the same exercise is repeated across 18 different benchmarks, the picture becomes much murkier — depending on which benchmark you choose, you can predict convergence within six months or conclude the gap is stubbornly stuck at ~5 months and possibly widening.

## Benchmark-by-Benchmark Breakdown

Dborin analyzed all 18 benchmarks tracked by Artificial Analysis. The results fall into three categories:

| Benchmark | Gap Trend | Status |
|---|---|---|
| Coding Index | 15 months → **1-2 months** | Rapidly closing |
| LiveCodeBench | 15 months → **1-2 months** | Rapidly closing |
| AIME | Shrinking | Closing |
| AIME25 | Shrinking | Closing |
| MATH 500 | Shrinking | Closing |
| Intelligence Index (overall) | Shrinking steadily | Projects zero by Dec 3, 2026 |
| Math Index | Moderate increase | Slightly widening |
| GPQA | Moderate increase | Slightly widening |
| MMLU Pro | Moderate increase | Slightly widening |
| SciCode | Moderate increase | Slightly widening |
| TAU2 | Moderate increase | Slightly widening |
| TAU Banking | Moderate increase | Slightly widening |
| TerminalBench Hard | Moderate increase | Slightly widening |
| TerminalBench v2.1 | Moderate increase | Slightly widening |
| HLE (Humanity's Last Exam) | Moderate increase | Slightly widening |
| IFBench | Moderate increase | Slightly widening |
| LCR | Moderate increase | Slightly widening |
| Agentic Index | Flat | Stable |

**Overall average across all 18 benchmarks**: Almost completely flat, at **just under 5 months** gap for the entire measurement period.

## Interpretation Challenges

The stark divergence between the Intelligence Index projection (convergence by Christmas 2026) and the multi-benchmark average (persistent ~5-month gap) reveals a fundamental difficulty in measuring LLM quality:

- **Benchmark selection bias** — The Intelligence Index is heavily weighted toward coding and math benchmarks, which are precisely where open-weight models have made the most progress. Other benchmarks (knowledge retrieval, agentic tasks, reasoning) show a much less optimistic picture.
- **Metric choice drives the conclusion** — A single trendline from one composite index yields a dramatic prediction. An unweighted average across all available benchmarks yields stagnation. Both are "correct" descriptions of the data, which means the data alone cannot resolve the question.
- **Benchmark saturation and ceiling effects** — Some benchmarks may be approaching saturation, compressing the apparent gap. Others may not capture the capabilities that differentiate frontier models.
- **Temporal instability** — The gap trajectory itself varies depending on the start date chosen. Using mid-2024 as the starting point shows a different trend than using early 2025.

This is a case study in the [[concepts/open-source-ai-must-win|difficulty of evaluating AI progress]]: the same underlying data can support opposite conclusions depending on methodological choices.

## HN Reception

The analysis generated **299 points and 236 comments** on Hacker News (June 26, 2026), reflecting intense community interest in the open-vs-closed frontier question. Discussion centered on the reliability of benchmark-based predictions, the December 2026 projection's plausibility, and whether the coding-benchmark collapse represented genuine capability convergence or benchmark overfitting.

## Related Pages

- [[concepts/open-weight-vs-closed-llm-gap]] — Strategic and economic implications of the closing gap
- [[concepts/ai-benchmarks/index]] — Full catalog of AI benchmarks and evaluation methodologies
- [[concepts/open-source-ai-must-win]] — Strategic arguments for open-source AI dominance
- [[concepts/scaling-laws]] — Empirical scaling relationships underpinning model capability
