---
title: "Internal Data Repetition Destroys Language Models"
type: concept
created: 2026-07-06
updated: 2026-07-06
tags:
  - training
  - data-science
  - scaling-laws
  - synthetic-data
  - datasets
  - overfitting
  - scaling
sources:
  - https://arxiv.org/abs/2606.24998
---

# Internal Data Repetition Destroys Language Models

A June 2026 paper by Joshua Kazdan et al. (arXiv:2606.24998) revisits the effect of **verbatim data repetition** in pretraining corpora, using Chinchilla-era scaling laws to quantify the damage. The central finding: even aggressively deduplicated corpora retain repetition, and that repetition systematically degrades performance in ways that can be precisely measured as wasted compute.

## Key Findings

### 1. Non-Monotonic Damage Peak

Holding compute constant, eval loss peaks at an **intermediate repeat count**. Repeating a moderately-sized subset a moderate number of times damages performance more than either extreme:

- Repeating a **large** subset a **few** times → less damage
- Repeating a **small** subset **many** times → less damage
- Repeating a **medium** subset a **moderate** number of times → **maximum damage**

This suggests a memorization-vs-generalization tradeoff: moderate repetition is the "sweet spot" for overfitting without the model learning to ignore the data entirely.

### 2. Power-Law Scaling of the Damage Peak

The location of the peak repeat count follows a **power law in model size**. Crucially, the most damaging number of repetitions grows more quickly than compute — meaning as models scale, the repetition problem gets relatively worse.

### 3. Quantified Compute Waste

When repeated documents consume 10% of the FLOPs budget in a controlled exact-document repetition setting:

- On **FineWeb-Edu-Dedup**, the most damaging repeat count for a Qwen3-style 344M-parameter model matches the loss of a no-repetition run using only **67% of the FLOPs**
- This means ~33% of compute is wasted due to internal repetition

### 4. Statistical Model Explanation

The phenomena are not language-model-specific. A **misspecified linear regression** with verbatim duplicates reproduces the same qualitative loss peak, showing the effect arises from a fundamental statistical tradeoff between memorization and generalization.

## Implications for Practitioners

- **Deduplication is necessary but insufficient** — even "deduplicated" corpora retain substantial repetition
- **Repeat structure matters** — the pattern of duplication (how many times, how many documents) matters as much as the total amount
- **Compute-equivalent loss** provides a practical metric: practitioners can quantify wasted compute from the presence and repeat structure of duplicates in pretraining corpora
- **Scaling laws for data quality** — this work adds to the growing body of evidence that data quality has its own scaling laws, alongside model size and compute

## Relationship to Data Quality Research

This paper complements other work on data quality scaling:

- [[concepts/data-filtering-scaling-laws]] — Stanford's work showing data filtering follows its own bitter lesson
- [[concepts/data-scaling-limits]] — broader analysis of when more data stops helping
- [[concepts/scaling-laws]] — Chinchilla-era compute-optimal training laws that this paper builds on
- [[concepts/llm-training-fundamentals]] — foundational training concepts including data preparation

## Related Concepts

- [[concepts/scaling-laws]] — the Chinchilla scaling law framework used to measure repetition damage
- [[concepts/data-filtering-scaling-laws]] — data filtering as a scaling axis
- [[concepts/data-scaling-limits]] — when additional data provides diminishing returns
- [[concepts/llm-training-fundamentals]] — core training pipeline concepts
- [[concepts/model-training-as-code]] — managing training data as part of reproducible pipelines
