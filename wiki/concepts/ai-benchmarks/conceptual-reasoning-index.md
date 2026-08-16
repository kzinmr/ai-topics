---
title: "Conceptual Reasoning Index (CRI)"
type: concept
created: 2026-08-16
updated: 2026-08-16
tags:
  - benchmark
  - evaluation
  - reasoning
  - alignment
  - ai-safety
  - anthropic
  - redwood-research
sources:
  - raw/articles/2026-08-12_anthropic_conceptual-reasoning-index.md
  - https://alignment.anthropic.com/2026/conceptual-reasoning-index/
  - https://arxiv.org/abs/2607.27499
related:
  - concepts/ai-benchmarks/agentharm
  - concepts/evaluation/ai-benchmarks-and-evals
  - concepts/ai-alignment
  - concepts/security-and-governance/ai-safety
  - entities/redwood-research
  - entities/anthropic
---

# Conceptual Reasoning Index (CRI)

The **Conceptual Reasoning Index (CRI)** is an aggregate benchmark for measuring models' ability to reason about questions where empirical evidence is limited, there is no practically verifiable answer, and progress relies heavily on argumentation — what its authors call **conceptual reasoning**. It was introduced on August 12, 2026 by Redwood Research (Emery Cooper, Caspar Oesterheld, Chi Nguyen, Alex Kastner) in collaboration with Anthropic (Joe Benton, Ethan Perez), and is published on the Alignment Science Blog.

## Motivation

A core hope for managing AI risk is that AIs will help humans understand the situation, plan ahead, and develop mitigations. Much of that work — reasoning about AIs more capable than any human, choosing research agendas and governance interventions with long feedback timescales, and arguing about which values AIs should have — **cannot be empirically or mathematically verified**. Current training depends on abundant data and reliable feedback, so models are typically weakest at exactly these tasks. The CRI exists because *improving* conceptual reasoning first requires *measuring* it.

## The Three Benchmarks

The CRI is a weighted average of three sub-benchmarks:

| Benchmark | Weight | What it measures |
|-----------|--------|------------------|
| **LMCA** (Language Model Conceptual Argumentation) | 60% | Judging expert-rated conceptual arguments against position texts |
| **ACCoRD** (Assessment of Consistency in Conceptual Reasoning Domains) | 20% | Logical consistency of reported beliefs/probabilities and preferences |
| **DTBench capabilities** (Decision Theory Benchmark) | 20% | Multiple-choice reasoning about decision-theoretic situations involving self-prediction and near-copies |

### LMCA

A dataset of **560 position texts with 1,461 arguments against them**, on decision theory, philosophy, and risks from advanced AI. Nearly all arguments were rated by conceptual researcher Emery Cooper (2,140 ratings total), following a detailed rubric. Models are scored on how well their argument-judging ratings match human ratings. LMCA also supports evaluating models' *argumentation* ability (generate an argument, have another model rate it), though only argument-judging currently feeds the CRI. See the companion paper "A dataset of rated conceptual arguments" ([arXiv:2607.27499](https://arxiv.org/abs/2607.27499)).

### ACCoRD

Measures whether a model's reported beliefs and preferences are **logically consistent** — e.g., does it report P(A) ≥ P(A&B) across separate instances of itself? The dataset contains close to 14,000 model-generated consistency constraints across 18 constraint types; 567 were manually checked and approved, and only those are used in the CRI. Inconsistency is treated as a signal that a model's reasoning on that domain cannot be trusted by default.

### DTBench capabilities

**407 handcrafted multiple-choice questions** (mostly original, authored by Caspar Oesterheld) measuring decision-theoretic reasoning involving faithful predictions of a model's own behavior or interactions with near-copies. A further 130 questions measuring decision-theoretic *attitudes* exist but are excluded from the CRI.

## Results (as of Aug 10, 2026)

- Scores run 0–100 (0 = random guessing; 100 = ceiling). The **estimated CRI ceiling is ~91** (LMCA tops out around 85 due to human-rating noise).
- The highest-scoring model is **Opus 5 at 73.6** (95% CI ± 2.1) — still well below the ceiling.
- **DTBench capabilities is near-saturated**: Claude Fable 5 got 98% of questions right.
- LMCA and ACCoRD remain well below their ceilings; LMCA is loosely estimated to begin saturating ~a year from now.
- **Scores have increased roughly linearly since late 2024, with no signs of flattening.**

## Significance

The CRI is a leading example of an **AI-safety-shaped benchmark**: it measures the capabilities most relevant to "AI helping reduce AI risk" rather than consumer-facing usefulness, and it is explicitly designed for tasks with no verifiable ground truth. Its introduction highlights the gap between models' rapid progress on empirically-verifiable tasks (coding, math — "hill-climbable" problems) and their slower, but steadily improving, performance on unverifiable conceptual reasoning.

## Related Pages

- [[concepts/ai-benchmarks/agentharm]] — Agent safety benchmark (another safety-oriented eval)
- [[concepts/evaluation/ai-benchmarks-and-evals]] — Broader benchmark landscape
- [[concepts/ai-alignment]] — The alignment problem
- [[concepts/security-and-governance/ai-safety]] — AI safety
- [[entities/redwood-research]] — Redwood Research
- [[entities/anthropic]] — Anthropic
