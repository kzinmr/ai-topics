---
title: "BenchPress"
type: concept
created: 2026-06-25
updated: 2026-06-25
tags:
  - benchmark
  - evaluation
  - methodology
  - open-source
  - training
  - benchmark-optimization
sources:
  - raw/articles/2026-02-25_dimitris-papailiopoulos_benchpress-you-dont-need-to-run-every-eval.md
  - https://github.com/anadim/llm-benchmark-matrix
---

# BenchPress

## Summary

**BenchPress** is a $0 benchmark prediction system built by Dimitris Papailiopoulos using Claude Code and Codex. It demonstrates that LLM evaluations are so low-rank (rank-2) that only 5 benchmarks are needed to predict the other 44 to within ~5 points (7% median absolute error). The system uses rank-2 SVD matrix completion combined with sparse regression on an 83-models × 49-benchmarks matrix — no neural networks, no model metadata, no GPU costs. BenchPress's predictive accuracy (5.8% median error) narrowly beats Claude Sonnet (6.1%) at filling in missing benchmark scores, proving that classical linear algebra can outperform a trillion-parameter model on this task.

The project is fully open-sourced at [github.com/anadim/llm-benchmark-matrix](https://github.com/anadim/llm-benchmark-matrix), including the annotated matrix with 1,375 cited entries, the BenchPress code, and a `predict.py` CLI.

## Methodology

BenchPress combines two simple ingredients into a convex combination (60% regression + 40% SVD):

### Ingredient 1: Sparse Regression

For each missing (model, benchmark) cell, the system identifies the 5 benchmarks that best predict the target benchmark. For each candidate predictor benchmark, it plots every model that has scores on both benchmarks as a point, fits a straight line in logit space, and weights predictions by fit quality (R²). The final prediction is a weighted average of the top 5 predictors.

### Ingredient 2: Rank-2 SVD Matrix Completion

Rank-2 SVD finds the best 2D plane through the 49-dimensional benchmark space such that projecting models onto that plane minimizes reconstruction error. The algorithm iterates until convergence: start with column averages for missing entries, run SVD, replace missing entries with SVD projections while keeping observed scores pinned, repeat.

Ranks 1 through 8 were swept systematically. Rank 2 is optimal — rank 3 is already worse by half a point, and rank 8 blows up to 13% absolute error. The third singular value appears real in the spectrum but is below the noise floor for prediction.

### Logit Transform

All operations occur in logit space: `logit(p) = log(p / (1-p))`. This stretches scores near 0% and 100% while compressing the middle, ensuring the gap between 88% and 92% receives appropriate weight. This fix alone improved final accuracy by ~10%.

### What Didn't Work

Claude Code systematically tested alternatives and found that **none** outperformed plain SVD:
- **NMF, PMF, nuclear norm, ALS** — all worse than SVD
- **KNN** instead of SVD — KNN and regression are both local methods that make correlated mistakes; SVD gave a 14% improvement
- **Model metadata** (parameter count, provider, reasoning mode, open-weight status) — made predictions *worse*; everything metadata could reveal is already captured in the model's pattern across scores

## Key Findings

### Five Benchmarks Suffice

With just 5 known benchmark scores for a model, median absolute error across all 83 models drops to ~9%. The greedy forward selection identifies the minimum set as:

> **{HLE, AIME 2025, LiveCodeBench, SWE-bench Verified, SimpleQA}**

These span four categories and cover both principal components. Under proper holdout they achieve ~7.8% error vs. 7% for the full method.

### BenchPress Beats Claude Sonnet

In a direct comparison, BenchPress achieved 5.8% median error vs. Claude Sonnet's 6.1% at predicting held-out entries from a partially filled CSV. Claude has an advantage at k=0 (zero revealed scores: 2.5% error for known models vs. BenchPress's 17%), but by k=5 BenchPress catches up, and beyond that linear algebra wins.

A curious finding: Claude *gets worse* as more benchmark scores are revealed to it, creating a conflict between prior knowledge and prompt data — a phenomenon the author calls "retrieval-augmented degradation." BenchPress, by contrast, improves monotonically with more data.

### The Matrix is Rank-2

On the largest fully-observed submatrix (31 models × 10 benchmarks), the first singular value captures 71% of the spectrum; the first three capture >90%. This confirms the deep structural redundancy in LLM evaluations — most benchmarks are measuring the same two underlying dimensions.

## SVD Components

The two principal components extracted by SVD carry interpretable semantic meaning:

### PC1: General Capability

Benchmarks with highest weights: GPQA-D, LiveCodeBench, MMLU-Pro, HumanEval, MMLU. This component functions almost as a classifier for frontier vs. small models, and interestingly, closed vs. open. Top-scoring models: Gemini 3.1 Pro, GPT-5.2, Gemini 3 Pro, Opus 4.6, Kimi K2.5.

### PC2: Novel Reasoning + Recency of Frontier

Benchmarks with highest weights: SimpleQA, ARC-AGI-2, HLE, ARC-AGI-1, FrontierMath. These are the hard, novel tasks that recent frontier models excel at. Benchmarks like MATH-500 and MMLU max out in the opposite direction. This component almost functions as a "recency of frontier" measure — the latest frontier models (Gemini 3.1 Pro, Opus 4.6, GPT-5.2) score highest, while earlier-2025 frontier models (Claude 3.7 Sonnet, DeepSeek-R1, o3-mini) score lower.

## Hard-to-Predict Benchmarks

Benchmarks that resist prediction share two traits:

1. **Bimodal score distributions**: Competition math benchmarks like IMO and USAMO are essentially step functions — a model either solves olympiad problems or doesn't. Linear methods cannot interpolate a step function.

2. **Weak correlation with everything else**: Terminal-Bench, SimpleBench, and ARC-AGI-1 show high prediction errors because they measure capabilities orthogonal to the rest of the benchmark ecosystem. These are, paradoxically, the **most valuable** benchmarks — they escape the rank-2 structure and test genuinely novel capabilities.

> If your eval correlates with existing ones, it's not adding much. The valuable benchmarks are the ones that are nearly orthogonal to everything else.

## Practical Implications

### When to Predict vs. Run

The cost/error tradeoff drives decision-making:
- **Predict** (BenchPress, ~$0): ~5 points error. Useful for go/no-go decisions when full eval costs $5K+ (e.g., SWE-bench).
- **Run the benchmark**: True score. Costs range from $5 to $100K depending on benchmark and model.
- **Cheaper proxy model**: Lower cost but measures the wrong model.

### For Benchmark Designers

The rank-2 finding carries a clear message: if a new benchmark correlates strongly with existing ones, it's adding little information. The benchmarks that matter most are those nearly orthogonal to the existing suite — like Terminal-Bench, which defies prediction from the rest of the matrix.

### For Model Evaluators

For labs and teams evaluating new models, BenchPress offers a rapid sanity check: run 5 carefully chosen benchmarks and predict the rest within acceptable error margins. This doesn't replace full evaluation suites, but it dramatically reduces the cost of early-stage model assessment.

## Historical Context

BenchPress draws on two well-established traditions:

- **Compressed sensing and matrix completion theory**: Recover a low-rank matrix from a sparse set of observations — the theoretical foundation Ben Recht, Emmanuel Candès, and others developed in the mid-2000s.
- **Netflix Prize (2006)**: A $1M competition to predict missing movie ratings in a 100M-entry user×movie matrix. Drew tens of thousands of teams, launched modern recommender systems, and proved matrix completion's practical value — though Netflix never deployed the winning solution.

The author spent two days mass-prompting Claude Code and Codex, spent $0 on GPUs, and produced a result that "would have been a decent workshop paper."

## Related Concepts

- [[concepts/ai-benchmarks/benchmaxxing]] — Benchmark over-optimization trap; BenchPress reveals the structural redundancy that makes benchmaxxing possible
- [[concepts/evaluation/ai-benchmarks-and-evals]] — Comprehensive benchmark landscape overview and the benchmarks-vs-evals framework
- [[concepts/evaluation/ai-evaluation]] — AI evaluation methodology and infrastructure

## Sources

- Papailiopoulos, D. (2026). "You Don't Need to Run Every Eval." [X Article](https://x.com/i/article/2026523085545857024)
- [llm-benchmark-matrix](https://github.com/anadim/llm-benchmark-matrix) — Open-source repository containing the 83×49 matrix, BenchPress code, and predict.py CLI
