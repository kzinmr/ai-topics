---
title: "ChartQA"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - multimodal
aliases:
  - chartqa
  - chart-qa
status: active
sources:
  - https://arxiv.org/abs/2203.10244
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/ai-benchmarks/mmmu]]"
---

# ChartQA

> **Part 11 of @xeophon's 18-part AI Benchmarks & Evals series.** A chart understanding benchmark with good underlying data but a noisy test set — @xeophon recommends retirement.

## Overview

ChartQA evaluates how well models can **understand and answer questions about charts** (bar charts, line graphs, pie charts, etc.). While the underlying data quality is good, the benchmark's test set has significant noise and inconsistencies that undermine its reliability.

**Paper**: [arXiv 2203.10244](https://arxiv.org/abs/2203.10244) (Mar 2022)

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Chart comprehension and visual reasoning |
| **Task type** | Answer questions about chart images |
| **Chart types** | Bar charts, line graphs, pie charts, and other visualizations |
| **Evaluation** | Exact match against reference answers |

## @xeophon's Key Insight

> "Noisy test data. Brand recommends retirement." — @xeophon, Part 11

Xeophon's analysis is blunt: despite good underlying data, ChartQA's test set has significant quality issues — inconsistent answers, ambiguous questions, and annotation errors. He recommends the benchmark be **retired** from active use, highlighting the importance of data quality over benchmark quantity.

## The Retirement Argument

ChartQA illustrates a broader principle: **a benchmark with poor data quality is worse than no benchmark at all**. Noisy test sets:
- Create misleading model comparisons
- Reward models that happen to match noise patterns rather than genuine capability
- Erode trust in benchmark-driven evaluation

This makes ChartQA a valuable **case study in benchmark quality management** even if the benchmark itself is flawed.

## Strengths

- **Relevant domain**: Chart understanding is a practical multimodal capability
- **Good underlying data**: The chart images and source data are well-constructed
- **Historical importance**: Contributed to advancing multimodal evaluation

## Weaknesses

- **Noisy test set**: Inconsistent answers and ambiguous questions
- **Retirement recommended**: @xeophon and others advise against continued use
- **Static**: Fixed dataset, increasingly saturated
- **Limited chart types**: Doesn't cover all real-world visualization types

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/ai-benchmarks/mmmu]] — MMMU (broader multimodal, higher quality)
- [[concepts/benchmaxxing]] — Benchmark over-optimization risks

## Sources

1. Masry, A. et al., "ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning," arXiv:2203.10244, 2022. https://arxiv.org/abs/2203.10244
2. @xeophon, "AI Benchmarks & Evals Series, Part 11: ChartQA," May 14, 2025.
