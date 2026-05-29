---
title: GRAM (Generative Recursive Reasoning)
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [concept, reasoning, research, architecture, agent-foundations, model, recursive-self-improvement]
sources: [raw/articles/2026-05-19_gram-recursive-reasoning.md]
---

# GRAM: Generative Recursive Reasoning Models

GRAM (Generative Recursive reAsoning Models) is a framework that turns recursive latent reasoning into **probabilistic multi-trajectory computation**. Published in May 2026 by researchers from KAIST, Mila, NYU, and Universite de Montreal, GRAM addresses a key limitation of existing Recursive Reasoning Models (RRMs): their deterministic nature.

## Core Innovation

Traditional RRMs (like [[concepts/attractor-models|Attractor Models]], Looped Transformers, HRM, TRM) follow a **single deterministic latent trajectory** — they converge to one prediction, failing to maintain uncertainty or explore alternatives. GRAM introduces **stochastic latent transitions**, enabling:

- **Multiple hypotheses** maintained simultaneously
- **Alternative solution strategies** explored in parallel
- **Width-based inference-time scaling**: scale with both recursive depth AND number of sampled trajectories
- **Unconditional generation**: the same recursive process can generate new data, not just reason about inputs

## Architecture

GRAM uses a **two-level hierarchical latent state**:

| Level | Component | Behavior | Purpose |
|-------|-----------|----------|---------|
| **High-level (h)** | Abstract reasoning | **Stochastic** — Gaussian noise injected around deterministic proposal | Exploration, multi-hypothesis maintenance |
| **Low-level (l)** | Fine-grained refinement | **Deterministic** — refined K times per transition | Efficient local computation |

### Transition Process

1. Refine low-level state l deterministically K times (holding h fixed)
2. Compute deterministic high-level proposal u_t from (h_t-1, l_t)
3. Sample stochastic guidance epsilon_t from learned Gaussian
4. Set h_t = u_t + epsilon_t — stochasticity at high level only
5. Decoder reads h_T for final output

### Training

Trained with **amortized variational inference** — the model learns both the proposal distribution and the stochastic guidance parameters. Supervision steps provide training signal at regular intervals throughout the recursion.

## Empirical Results

- **10M parameter GRAM** outperforms **27M parameter deterministic baselines** on structured reasoning tasks
- **Sudoku-Extreme**: 91%+ with GRAM vs 0% for direct-prediction baselines
- **ARC-AGI-2**: Direct prediction scores 0% — recursive computation is essential for these tasks
- **Multi-solution tasks** (N-Queens, Graph Coloring): GRAM recovers multiple valid solutions while deterministic baselines collapse to one
- **Unconditional generation**: Successfully generates valid binarized MNIST digits and Sudoku puzzles

## Significance

GRAM establishes **probabilistic multi-trajectory recursion** as a design principle for future reasoning architectures. The finding that width (parallel sampling) matters as much as depth challenges the prevailing focus on deeper recursion alone.

From a broader perspective, GRAM connects to [[concepts/test-time-scaling|test-time compute scaling]] — showing that inference can scale along two axes simultaneously (depth and width), not just one.

## Related Pages

- [[concepts/attractor-models]] — Attractor Models for language and reasoning
- [[concepts/recursive-self-improvement]] — Recursive self-improvement in AI
- [[concepts/test-time-scaling]] — Test-time compute scaling
- [[concepts/reasoning]] — Reasoning in language models
- [[concepts/agent-foundations]] — Agent foundations
