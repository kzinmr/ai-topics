---
title: "Scaling Laws of Synthetic Data for Language Models (SynthLLM)"
authors: Zeyu Qin et al.
source: arXiv / COLM 2025
url: https://arxiv.org/abs/2503.19551
published: 2025-03-25
venue: COLM 2025 (Conference on Language Modeling)
type: paper
tags:
  - synthetic-data
  - scaling-laws
  - data-wall
  - microsoft
  - post-pretraining
  - rectified-scaling-law
---

# Scaling Laws of Synthetic Data for Language Models

## Core Innovation

Introduces **SynthLLM**, a framework that uses graph algorithms to extract and recombine concepts from existing corpora into synthetic datasets. Establishes the **Rectified Scaling Law** — confirming synthetic data follows predictable scaling dynamics, distinct from natural data.

## Key Findings

- **Rectified Scaling Law**: Synthetic data follows a modified scaling law — performance plateaus at ~**300B tokens**
- **Larger models need less synthetic data**: 8B model peaks at 1T tokens, 3B model requires 4T (inverse trend vs natural data)
- SynthLLM outperforms existing synthetic data generation methods

## Connection to Scaling Hypothesis

Validates Daniel Han's "Approach #4" (Data Wall Breakthroughs). Synthetic data is a viable path for continued scaling but follows different dynamics — it saturates faster than natural data and is most effective as a mixture component, not a replacement.

See: [[concepts/scaling-hypothesis#Synthetic Data Scaling Laws: SynthLLM (Microsoft, March 2025)]]
