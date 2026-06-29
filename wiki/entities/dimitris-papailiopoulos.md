---
title: "Dimitris Papailiopoulos"
type: entity
created: 2026-06-25
updated: 2026-06-25
tags:
  - person
  - evaluation
  - benchmark
aliases: [dimitris_papailiopoulos]
sources:
  - raw/articles/2026-02-25_dimitris-papailiopoulos_benchpress-you-dont-need-to-run-every-eval.md
  - https://github.com/anadim/llm-benchmark-matrix
  - https://x.com/i/article/2026523085545857024
related:
  - concepts/benchpress
  - concepts/llm-evaluation
  - concepts/evaluation/ai-benchmarks-and-evals
---

# Dimitris Papailiopoulos

| | |
|---|---|
| **Handle** | @misc (X/Twitter), anadim (GitHub) |
| **Notable Work** | BenchPress: $0 benchmark prediction system |
| **Background** | EE theory, compressed sensing, matrix completion |
| **Significance** | Demonstrated that LLM benchmarks are rank-2 redundant; 5 benchmarks can predict 44 others within ~5 points |

## Overview

**Dimitris Papailiopoulos** is an AI researcher and author of the February 2026 article *"You Don't Need to Run Every Eval"*, published as an X Article. His work on **[[concepts/benchpress|BenchPress]]** demonstrated that LLM evaluation benchmarks exhibit such strong low-rank structure (rank-2) that only 5 benchmarks are needed to predict scores on 44 others within ~5 percentage points — all using linear algebra with $0 in GPU costs.

Papailiopoulos built the entire BenchPress project using **[[entities/claude-code|Claude Code]]** and **Codex**, spending tens of millions of tokens but zero dollars on GPUs. He used Codex to audit Claude Code's work and vice versa, creating an adversarial code-review loop between the two coding agents.

## Background

Papailiopoulos came from an **EE theory** background, having been a PhD student ~15 years ago specializing in **compressed sensing** and **matrix completion** — the mathematical foundations that underpin BenchPress. He cites fellow EE theory researcher [@beenwrekt](https://x.com/beenwrekt) as a contemporary from that era.

The core insight of compressed sensing and matrix completion is that if a partially-observed matrix is approximately low-rank, missing entries can be recovered from surprisingly few observations using Singular Value Decomposition (SVD). This theory famously powered the **$1M Netflix Prize** (2006–2009), which catalyzed modern recommender systems and launched thousands of ML careers.

Papailiopoulos recognized that the same mathematical structure applies to **(model, benchmark) score matrices**: models within the same generation are nearly identical in their eval profiles, benchmarks testing similar skills correlate almost perfectly, and hard benchmarks are hard across all models. This redundancy in every direction suggested the matrix would be low-rank — and it was.

## BenchPress Project

### Motivation

The project began with a simple question: *can you exploit the low-dimensional structure of benchmark scores to predict evals without running them?* Given the massive cost of running full benchmark suites (some, like Terminal-Bench 2.0, can cost O($100k) for frontier models), a $0 prediction system has practical value for go/no-go decisions and sanity checks.

### The Matrix

Papailiopoulos had Claude Code search and verify all possible (model, eval) pairs between January 2025 and February 2026, producing an **83 model × 49 benchmark** matrix with **1,375 cited scores** (34% filled). Every entry includes a source URL. Codex independently audited the matrix for hallucinations and verified each entry.

### Method

BenchPress combines two simple ingredients:

1. **Sparse Regression**: For each missing cell, find the 5 benchmarks that best predict the target. A weighted average of their logit-space linear predictions forms the regression estimate.

2. **Rank-2 SVD with Matrix Completion**: Iterative SVD in logit space, starting from column averages for missing entries, projecting onto the top-2 singular vectors, replacing only missing entries while keeping observed scores pinned, and repeating until convergence.

The final prediction is a **60/40 convex combination** of regression and SVD — weights determined by Claude Code through hyperparameter sweep. Rank-2 was chosen because ranks 3+ degrade performance; the third singular value, while visually apparent in the spectrum, is below the noise floor for prediction.

### Results

- **7% median absolute error** on held-out scores across all benchmarks
- **5 benchmarks** are sufficient: with just 5 known scores, median error drops to ~9% (from 12% at 1 score, 17% at 0)
- The greedy optimal 5-benchmark set: **HLE, AIME 2025, LiveCodeBench, SWE-bench Verified, SimpleQA** — spanning four categories and both principal components
- BenchPress (5.8% median error) **edges out Claude Sonnet** (6.1%) at predicting missing entries from a CSV, despite Claude being a trillion-parameter model. Linear algebra wins in under a second, for free.
- Adding model metadata (parameter count, provider, reasoning mode) made predictions **worse** — all signal is already captured in the score pattern
- Alternative matrix factorization methods (NMF, PMF, nuclear norm, ALS) performed no better than plain SVD

### Failure Modes

BenchPress struggles with:
- **Bimodal benchmarks** (ARC-AGI, IMO, USAMO) — step-function distributions resist interpolation
- **Weakly correlated benchmarks** (Terminal-Bench, Arena-Hard, SimpleBench) — these measure capabilities uncorrelated with the rest of the matrix, making them the *interesting* benchmarks that genuinely test new capabilities

### The Rank-2 Interpretation

The two SVD components reveal a meaningful structure:

- **Component 1 (71% of spectrum)**: General capability. Top benchmarks: GPQA-D, LiveCodeBench, MMLU-Pro, HumanEval, MMLU. Top models: Gemini 3.1 Pro, GPT-5.2, Gemini 3 Pro, Opus 4.6, Kimi K2.5. Effectively a frontier-vs-small model classifier.
- **Component 2**: Hard novel reasoning and model recency. Top benchmarks: SimpleQA, ARC-AGI-2, HLE, ARC-AGI-1, FrontierMath. Top models: Gemini 3.1 Pro, Opus 4.6, Gemini 3 Pro, GPT-5.2. Bottom: Claude 3.7 Sonnet, DeepSeek-R1, Gemini 2.5 Flash, o3-mini — models that were frontier in early-mid 2025. Component 2 is almost a "recency of frontier" measure.

### Development Process

The entire project was built over **two days** using coding agents:

- **Claude Code** wrote the code, assembled the matrix, ran experiments, and performed hyperparameter sweeps
- **Codex** audited Claude Code's work for bugs and independently verified all matrix entries
- Claude Code then rebutted Codex's audit, and Codex counter-rebutted — creating an adversarial review loop

Papailiopoulos describes his own role as "mostly giving prompts." The project consumed tens of millions of tokens but **$0 on GPUs**.

## Research Interests

- **Matrix completion** and **compressed sensing** — the mathematical foundations he studied as an EE theory PhD student
- **LLM evaluation methodology** — identifying redundancy in benchmark suites and finding minimal predictive subsets
- **Benchmark design** — identifying which benchmarks measure genuinely new capabilities (orthogonal to existing ones)
- **Coding agents as research tools** — using Claude Code and Codex for end-to-end research workflows, including adversarial code review between agents

## Notable Contributions

| Contribution | Details |
|---|---|
| **BenchPress** | $0 benchmark prediction system using rank-2 SVD + sparse regression; open-sourced at [github.com/anadim/llm-benchmark-matrix](https://github.com/anadim/llm-benchmark-matrix) |
| **83×49 Model-Benchmark Matrix** | Largest publicly cited matrix of LLM benchmark scores, with 1,375 entries across 83 models and 49 benchmarks, each sourced with URLs |
| **"You Don't Need to Run Every Eval"** | X Article (Feb 2026) demonstrating rank-2 redundancy in LLM benchmarks; argues that valuable benchmarks are those nearly orthogonal to existing ones |
| **Agent-to-Agent Code Audit** | Pioneered adversarial code review between Claude Code and Codex as a quality assurance methodology |

## Links

- **GitHub**: [anadim/llm-benchmark-matrix](https://github.com/anadim/llm-benchmark-matrix) — BenchPress code, full matrix, and `predict.py` CLI
- **X/Twitter**: [@misc](https://x.com/misc)
- **X Article**: [You Don't Need to Run Every Eval](https://x.com/i/article/2026523085545857024)

## Related

- [[concepts/benchpress]] — The BenchPress benchmark prediction methodology
- [[concepts/llm-evaluation]] — LLM evaluation landscape and practices
- [[concepts/evaluation/ai-benchmarks-and-evals]] — Broader context on AI benchmarks and evaluation
- [[concepts/ai-benchmarks/benchmaxxing]] — The practice of optimizing for benchmarks rather than capabilities

## Sources

- Papailiopoulos, D. (2026). *"You Don't Need to Run Every Eval"*. X Article. [x.com/i/article/2026523085545857024](https://x.com/i/article/2026523085545857024)
- [github.com/anadim/llm-benchmark-matrix](https://github.com/anadim/llm-benchmark-matrix) — BenchPress repository and full model-benchmark matrix
