---
title: "CountBenchQA"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - reasoning
aliases:
  - countbenchqa
  - count-bench-qa
status: active
sources:
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/ifeval]]"
---

# CountBenchQA

> **Part 14 of @xeophon's 18-part AI Benchmarks & Evals series.** An ultra-simple benchmark that tests one thing — counting — and does it well. A minimalist approach to evaluation design.

## Overview

CountBenchQA is a deliberately minimal benchmark that evaluates whether LLMs can **count correctly**. It asks simple counting questions (e.g., "How many X are in this list?") and measures accuracy. Its value lies not in its difficulty but in its **focus** — it isolates a single, fundamental capability.

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Counting (numerical reasoning) |
| **Task type** | Count items in a list, sequence, or set |
| **Key property** | Ultra-simple, single-capability test |
| **Evaluation** | Exact numerical match |

## @xeophon's Key Insight

> "Ultra-simple. Tests one thing well." — @xeophon, Part 14

Xeophon uses CountBenchQA to make a philosophical point: **good benchmarks don't have to be complex**. A benchmark that tests one thing clearly and unambiguously can be more valuable than a complex benchmark with noisy evaluation. CountBenchQA exemplifies the "single-responsibility principle" applied to evaluation design.

## Why Counting Matters

Counting may seem trivial, but it reveals important model behaviors:
- **Off-by-one errors**: Models frequently miscount by ±1
- **Tokenization effects**: How models tokenize numbers affects counting ability
- **List length degradation**: Accuracy drops as lists grow longer
- **Confidence miscalibration**: Models are often confidently wrong about counts

## Strengths

- **Focused**: Tests exactly one capability — no confounding factors
- **Simple to interpret**: Pass/fail is unambiguous
- **Fast to run**: Low computational cost
- **Reveals fundamental weaknesses**: Counting is a prerequisite for many higher-level tasks

## Weaknesses

- **Extremely narrow**: Tests only counting ability
- **Easy for frontier models**: Most modern LLMs score well, limiting differentiation
- **Low ceiling**: Not useful for comparing top-tier models
- **Limited real-world applicability**: Counting in isolation is rarely the bottleneck in production

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/ifeval]] — IFEval (another focused, simple benchmark)
- [[concepts/evaluation/pass-k-metric]] — Pass@k metric

## Sources

1. @xeophon, "AI Benchmarks & Evals Series, Part 14: CountBenchQA," May 20, 2025.
