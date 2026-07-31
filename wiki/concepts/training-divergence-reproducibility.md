---
title: "LLM Training Divergence & Reproducibility"
created: 2026-07-31
updated: 2026-07-31
type: concept
tags: [training, reproducibility, gpt-2, overfitting, scaling-laws, fine-tuning, evaluation, pretraining]
sources: ["[[raw/articles/gilesthomas.com--2026-07-why-do-openai-gpt2-weights-beat-mine-3-overtraining--fae7948d]]"]
related: [concepts/scaling-laws, concepts/post-training/fine-tuning, concepts/post-training/instruction-fine-tuning, concepts/nanogpt, concepts/pretraining-parallelisms]
---

# LLM Training Divergence & Reproducibility

## Overview

Training divergence is the phenomenon where a faithfully reproduced model training run — same architecture, same dataset, same hyperparameters — produces weights that behave differently from the original. The model may achieve comparable or even better test loss (perplexity) yet diverge significantly on downstream tasks like [[concepts/post-training/instruction-fine-tuning|instruction fine-tuning]] (IFT). This page examines the reproducibility gap using Giles Thomas's GPT-2 reproduction experiments as a case study, and explores what it tells us about the broader challenge of reproducing LLM training results.

The central puzzle: why do faithfully reproduced models that match or beat the original on test loss still underperform on downstream tasks? Thomas's systematic experiments with overtraining provide empirical data on this question, even if the answer remains elusive.

## Background: GPT-2 Architecture and Training

OpenAI's GPT-2 (2019) is a 124M-parameter decoder-only transformer. It was trained on WebText, a ~40 GB corpus (~10B tokens given the GPT-2 tokenizer's ~4 bytes/token), for what evidence suggests may have been 40–60 epochs — far beyond what later scaling law research would consider optimal.

At the time, the [[concepts/scaling-laws|Chinchilla scaling laws]] (Hoffmann et al., 2022) did not yet exist. The Chinchilla paper established that for compute-optimal training, a model should be trained on roughly 20 tokens per parameter. For GPT-2 Small (124M params), that means ~2.5B tokens — roughly one-quarter of WebText. Modern reproductions using Chinchilla-optimal budgets thus diverge from the original in total data seen, epochs, and the potential effects of repeated data exposure.

## The Reproducibility Gap

Giles Thomas at [[entities/gilesthomas|gilesthomas.com]] set out to faithfully reproduce GPT-2 from scratch, training 124M-parameter models on subsets of the FineWeb dataset using both JAX and PyTorch implementations. His results revealed a striking asymmetry:

| Model | Test Loss | IFT Score (LLM judge) |
|-------|-----------|----------------------|
| OpenAI GPT-2 Small (original) | 3.500 | 25.66 |
| Thomas JAX, MHA bias, no dropout | 3.419 | 17.53 |
| Thomas JAX, no MHA bias, no dropout | 3.420 | 20.25 |

Even though Thomas's Chinchilla-optimal models beat the original GPT-2 Small on test loss (lower is better), they scored significantly worse on the IFT evaluation — a gap of 5–8 points on a scale where the original scored 25.66. Better perplexity did not translate to better instruction-following ability.

## Overtraining Experiments

To test whether the gap was caused by undertraining relative to the original (which may have been heavily overtrained by modern standards), Thomas ran two additional experiments:

1. **Extended single-epoch training**: 6.4B tokens of unique FineWeb data (~2x Chinchilla-optimal). Result: test loss dropped to **3.325**, beating his prior best and approaching OpenAI GPT-2 Medium (3.231). IFT score rose slightly to 18.45, but remained far below the original GPT-2 Small.

2. **Two-epoch training**: 3.2B tokens repeated twice (6.5B tokens total, same data seen twice). Result: test loss **3.326**, nearly identical to the extended run. IFT score of 18.45–19.45, again in the noise.

The key finding: overtraining beyond Chinchilla-optimal budgets improved test loss as expected, but produced only marginal, noise-level improvements in IFT performance. The models remained stubbornly worse than the original OpenAI weights at instruction-following, despite using modern data and matching or exceeding test loss.

This is an example of **training divergence**: two models with similar (or better) perplexity can have meaningfully different downstream capabilities. The divergence likely stems from factors including:

- **Dataset composition**: WebText vs FineWeb differ in content distribution, quality filtering, and domain coverage
- **Training schedule**: Learning rate schedules, batch sizes, and optimizer states can affect which patterns the model latches onto
- **Epoch count and data repetition**: Multi-epoch training over a smaller curated dataset may produce different internal representations than single-pass training over larger data
- **Hardware and numerical precision**: Differences in GPU architectures, mixed-precision implementations, and non-deterministic CUDA operations

## Why This Matters

### For Open-Source Reproduction

The reproducibility gap has practical consequences for the open-source community. Projects like [[concepts/nanogpt|nanoGPT]] and others that aim to reproduce GPT-2-class models face a deeper challenge than matching test loss: downstream capability transfer is not guaranteed. An open-source reproduction that matches perplexity may still underperform the original on real tasks.

### For Training Divergence Science

This case study illustrates a broader phenomenon in [[concepts/post-training/fine-tuning|fine-tuning]] and [[concepts/pretraining-parallelisms|pretraining]]: the relationship between pretraining loss and downstream performance is not strictly monotonic. Small differences in training data, schedule, and implementation can compound into significant capability gaps that test loss alone does not capture. Understanding when and why this happens is an active area of research with implications for [[concepts/scaling-laws|scaling law]] predictions and model development practices.

### For Evaluation Methodology

Thomas's experiments highlight a methodological challenge in [[concepts/post-training/instruction-fine-tuning|IFT evaluation]]: LLM-as-judge scores exhibit run-to-run variance of 1-2 points, making it difficult to detect small but real improvements. The gap between test loss ranking and IFT ranking suggests that standard perplexity-based evaluation alone is insufficient for comparing reproduced models against originals. Multi-dimensional evaluation across diverse downstream tasks is essential for meaningful reproducibility claims.

### Open Questions

- Would training for 40+ epochs over 10B tokens (matching the suspected original recipe) close the gap, or are dataset differences insurmountable?
- Can the divergence be attributed to specific WebText properties (e.g., higher-quality prose, different domain mix) that FineWeb lacks?
- Are there architectural or initialization choices that make models more robust to training data substitutions?

## See Also

- [[concepts/scaling-laws]] — Chinchilla optimal training and compute budgets
- [[concepts/post-training/instruction-fine-tuning]] — Instruction fine-tuning evaluation methodology
- [[concepts/post-training/fine-tuning]] — Fine-tuning strategies and their relationship to pretraining
- [[concepts/nanogpt]] — nanoGPT and GPT-2 reproduction projects
- [[entities/gilesthomas]] — Giles Thomas's blog and GPT-2 reproduction series
