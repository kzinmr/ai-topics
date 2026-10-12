---
title: "Run-to-Run Variance in Semantic Query Processing"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [evaluation, reliability, reproducibility, llm-evaluation, agentic-retrieval]
sources: [raw/papers/2026-10-09_2610.13823_run-to-run-variance-semantic-query.md]
confidence: high
related: [concepts/evaluation/evaluation-harness-validity, concepts/benchmark-ceiling, concepts/training-divergence-reproducibility]
---

# Run-to-Run Variance in Semantic Query Processing

"Semantic" query engines ask an LLM to judge individual rows (extract, classify, filter), and
benchmarks compare engines on the quality of a **few executions at temperature 0**. Hassanzadeh &
Subramanian (arXiv:2610.13823, Oct 2026) measure how much *another execution at the same
temperature 0* changes the answer — and find that a surprising number of published comparisons
are not settled by the runs that produced them.

## Method

They re-execute the text and tabular workloads of **SemBench, LRO-Bench, and UDA-Bench** through
their own harnesses, logging **every one of 1.2 million model calls**, and re-analyze SemBench's
published executions.

## Findings

- At **temperature 0**, between **0.07% and 10.2% of rows change their operator output** across
  five executions (model-dependent), and **up to 24.0% on one task**.
- Query plans **amplify row-level nondeterminism exponentially** in the number of rows an answer
  exposes, as a possible-worlds model predicts. On UDA-Bench, a few percent of extracted values
  change but **about two-thirds of final answers do**.
- In SemBench's published results, **21% of text results change quality between executions** —
  including on engines whose plans are deterministic.
- **16 of 28 tests** of LRO-Bench's implementation recommendations, plus several per-query system
  comparisons, are **not settled** by the executions the benchmarks actually ran.
- Diagnostic structure: changing rows are rows on which models *disagree with each other*;
  identical requests *within* one execution disagree as often as across executions; one
  execution's decision margin or reasoning length predicts which rows change.
- **Voting reduces but does not remove** the variance; a **calibrated cascade keeps its guarantee**
  even while the specific rows it returns change.

The paper derives **reporting rules for benchmarks** and **design rules for engines**.

## Why it matters

This is an evaluation-validity result that generalizes well beyond semantic query engines. It
shows that "temperature 0" is not determinism, and that per-query, low-sample comparisons can be
statistical noise — the same class of concern as
[[concepts/evaluation/evaluation-harness-validity]] and [[concepts/benchmark-ceiling]]. The
exponential plan-amplification point is the sharpest warning: row-level noise that looks
negligible becomes answer-level instability once a plan touches many rows. The constructively
useful finding — a well-calibrated cascade stays valid even as its outputs move — offers a design
pattern for building nondeterminism-tolerant engines.

## Related

- [[concepts/evaluation/evaluation-harness-validity]]
- [[concepts/benchmark-ceiling]]
- [[concepts/training-divergence-reproducibility]]
