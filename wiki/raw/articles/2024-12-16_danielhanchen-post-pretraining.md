---
title: "My Take on the Post-Pretraining World — Daniel Han on Ilya Sutskever's NeurIPS 2024 Talk"
author: Daniel Han (@danielhanchen)
source: X/Twitter
url: https://x.com/danielhanchen/status/1868748998783517093
published: 2024-12-16
type: thread
tags:
  - scaling-hypothesis
  - ilya-sutskever
  - post-pretraining
  - memory-layers
  - blt
  - moe
  - synthetic-data
  - test-time-scaling
  - data-wall
---

# My Take on the Post-Pretraining World — Daniel Han on Ilya's Talk

Daniel Han's detailed analysis of Ilya Sutskever's NeurIPS 2024 talk, expanding on the implications of the "post-pretraining" world.

## Core Thesis

Ilya is implying we need to find **something else to scale**. The brain–body mass ratio graph in the talk showed human intelligence "scaled" better than mammals — suggesting biological evolution found a different scaling path. Similarly, LSTMs got out-scaled by transformers — the goal is to **"edit" the scaling laws** to make them more efficient.

## Key Insights

### Evolution as a Scaling Analogy

- Evolution first tried scaling intelligence for mammals
- Pushed the frontier up for non-human primates
- Large elephants which exceeded the 700g gram brain wall were extinct
- Hominids broke the wall and scaled far better

### Five Post-Pretraining Approaches

| # | Approach | Description |
|---|----------|-------------|
| 1 | **Scaling test-time compute** | Search, agents, O1-style reasoning — spending compute at inference instead of training |
| 2 | **Architecture changes** | MoEs, Memory+ layers — holding training compute constant while scaling active parameters |
| 3 | **Editing scaling law definitions** | Byte Latent Transformers (BLTs) — changing what "tokens" means in data scaling |
| 4 | **Breaking the Data Wall** | Synthetic data generation, RL, DPO, PPO, better filtering (FineWeb) |
| 5 | **Something else** | Unknown future paradigm shifts |

## Technical Deep Dives

### Data Scaling: The Data Wall

There exists a theoretical "Data Wall" — when all the data in the world (the internet and everything else) gets consumed by large models. Approaches to overcome it:
- **Synthetic Data Generation** — using trained models to augment datasets (question: will this plateau?)
- **Better filtering** — FineWeb dataset as an example
- **RL & post-training** — DPO, PPO to squeeze more performance from same tokens

### Parameter Scaling: Active Parameters > Total Parameters

- **MoE (Mixture of Experts)**: Replace MLP/FFN in dense transformers with MoE layers — smartly select only a few column groups to multiply instead of doing huge matrix multiplies
- Scale transformers to trillions of parameters (Switch Transformers)

### Byte Latent Transformers (BLTs)

Meta's BLT paper edits the scaling laws themselves:
- Removes BPE tokenization
- Learns to allocate optimal tokens/bytes to certain groups of patches through a smaller encoder
- Runs transformer on combined patches, uses a decoder for prediction
- Changes the definition of "tokens" in data scaling

### Memory+ Layers

The most interesting approach according to Han:

- Essentially **sparse lookup tables** replacing FFN MLP
- Giant learnable matrix V (Values) of size (100M, d)
- Select top K rows of V via weighted sum (softmax)
- Key matrix K (100M, d) for dot-product indexing
- **Product Key trick**: split K into KA and KB (sqrt(100M), d/2) using Cartesian product to avoid 100M operations
- Indices: sqrt(N) × topK_indices(KA·q) + topK_indices(KB·q)
- Memory+ adds nonlinearity (GLU variant) — scales better than MoEs!

### Three Scaling Axes (Kaplan et al.)

1. Training compute: N (parameters) × D (tokens/data) → test loss decreases in log-log
2. Test-time compute (Sutskever's shift): search, O1, QwQ — scaling inference instead of training
3. Architecture + data efficiency: editing the scaling law itself

## Connection to the Scaling Hypothesis

Daniel Han's thread operationalizes Sutskever's "end of pretraining" claim into concrete technical directions. The core insight: **the Scaling Hypothesis was correct about the first decade, but the second decade requires moving beyond simple compute×data×parameters scaling** into:
- Architectural innovation (MoE, Memory+, BLT)
- Test-time compute scaling
- Data efficiency breakthroughs
- Post-training (RL, DPO, PPO)

## References

- [Original tweet](https://x.com/danielhanchen/status/1868748998783517093)
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Kaplan et al.
- [FineWeb Datasets](https://arxiv.org/abs/2406.17557) — Penedo et al.
- [Outrageously Large Neural Networks (MoE)](https://arxiv.org/abs/1701.06538) — Shazeer et al.
- [Switch Transformers](https://arxiv.org/abs/2101.03961) — Fedus et al.
- [Byte Latent Transformer](https://ai.meta.com/research/publications/byte-latent-transformer-patches-scale-better-than-tokens/) — Meta
- [Memory Layers at Scale](https://ai.meta.com/research/publications/memory-layers-at-scale/) — Meta
- [Large Memory Layers with Product Keys](https://arxiv.org/abs/1907.05242) — Lample et al.
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) — Shazeer
