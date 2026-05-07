---
title: "Memory Layers at Scale"
authors: Vincent-Pierre Berges, Barlas Oğuz, Daniel Haziza, Wen-tau Yih, Luke Zettlemoyer, Gargi Ghosh
source: arXiv / Meta AI
url: https://arxiv.org/abs/2412.09764
published: 2024-12-13
venue: Meta Tech Report
type: paper
tags:
  - memory-layers
  - sparse-lookup
  - architecture
  - meta
  - scaling
  - post-pretraining
  - ffn-replacement
---

# Memory Layers at Scale

## Core Innovation

Replaces FFN MLPs with **trainable key-value lookup tables** (sparse memory layers) that add parameters without increasing FLOPs. This decouples model capacity from computational cost.

## Key Results

- Scales up to **128B memory parameters**, pretrained to 1 trillion tokens
- Models augmented with memory layers outperform dense models with **2× the compute budget**
- Outperforms MoE models when matched for both compute and total parameters
- **100%+ improvement** in factual accuracy (factual QA benchmarks)
- Significant gains on coding (HumanEval, MBPP) and general knowledge (HellaSwag, MMLU)

## Technical Approach

- Giant learnable matrix V (Values, size ~100M×d) with Key matrix K for dot-product indexing
- Select top-K rows via weighted sum (softmax)
- Fully parallelizable implementation
- Memory+ variant adds GLU-style nonlinearity — scales better than MoEs

## Connection to Scaling Hypothesis

Validates Daniel Han's "Approach #2" — architecture innovation. Memory+ layers represent a genuine new primitive beyond both dense FFNs and MoEs, enabling models to store and retrieve information cheaply rather than simulating lookup through computation.

See: [[concepts/scaling-hypothesis#Memory Layers at Scale (Meta, 2025)]]
