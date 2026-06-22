---
title: "Sampling Strategies"
type: concept
aliases:
  - sampling-strategies
created: 2026-04-25
updated: 2026-06-22
tags:
  - concept
  - inference
  - llm-reliability
  - reproducibility
sources:
  - raw/newsletters/2026-06-21-spacex-s-cursor-call-openai-s-codex-clone-and-midjourney-s-medical-moonshot.md
---

# Sampling Strategies

Sampling strategies determine how LLMs select tokens during generation. The key parameter is temperature, which controls randomness in token selection — lower temperatures produce more deterministic outputs.

## The Myth of Deterministic Inference

Even with temperature=0 (which should make the model always pick the highest-probability token), LLM API responses can vary across calls. This phenomenon is known as **batch invariance**.

| Fact | Implication |
|------|-------------|
| Temperature=0 does NOT guarantee identical responses | Users cannot rely on deterministic outputs even with minimal sampling settings |
| The root cause is GPU-level non-determinism from batched processing | Requests are processed alongside other users' queries in GPU batches, causing subtle timing-dependent variations |
| This affects reproducibility for evaluation and testing | Benchmark results may vary between runs, affecting confidence in model comparisons |

## Batch Invariance in Inference

Research by Horace He and Thinking Machines (Mira Murati's lab) identified batch invariance as the primary cause of non-determinism in LLM inference at temperature=0. When multiple user requests are processed together in a GPU batch, the order and composition of the batch introduces micro-variations in floating-point operations that propagate through the model.

This is distinct from training-side batch invariance (covered in [[concepts/batch-invariance-deterministic-training]]) where the focus is on deterministic training pipelines.

**Practical significance**: As coding agents ([[entities/claude-code]], [[entities/openai-codex]]) and agentic workflows become mainstream for business operations, reproducibility across API calls becomes critical. Users expecting identical outputs from identical prompts may encounter unexplained variations, complicating testing and validation.

**Related**: [[concepts/temperature-sampling]] — Temperature sampling parameter, [[concepts/inference/inference]] — LLM inference pipeline

Source: The Signal by Alex Banks, June 21, 2026, citing Horace He and Thinking Machines research.
