---
title: "DiffusionBlocks"
created: 2026-05-28
updated: 2026-05-28
type: concept
tags:
  - diffusion
  - training-efficiency
  - optimization
  - score-matching
  - transformers
  - residual-networks
  - block-wise-training
  - training
sources:
  - wiki/raw/papers/2025-06-17_2506.14202_diffusionblocks-block-wise-training.md
  - https://arxiv.org/abs/2506.14202
  - https://github.com/SakanaAI/DiffusionBlocks
---

# DiffusionBlocks

> **Block-wise neural network training via diffusion interpretation.** A principled framework from [[entities/sakana-ai|Sakana AI]] that converts transformer-based residual networks into independently trainable blocks, achieving B× memory reduction while matching end-to-end training performance. Published at **ICLR 2026**.

## Overview

**DiffusionBlocks** reinterprets residual connections in transformers as Euler discretization steps of a continuous-time diffusion (reverse probability flow ODE). This theoretical bridge enables decomposing a deep network into blocks that each learn to denoise within an assigned noise-level range — trained independently using score matching, without backpropagation through the full depth.

**Authors:** Makoto Shing (Sakana AI), Masanori Koyama (U. Tokyo), [[entities/takuya-akiba|Takuya Akiba]] (Sakana AI)
**Code:** [github.com/SakanaAI/DiffusionBlocks](https://github.com/SakanaAI/DiffusionBlocks)

## Core Insight

Residual connections `z_ℓ = z_{ℓ-1} + f(z_{ℓ-1})` are structurally identical to Euler discretization of the reverse diffusion ODE:

```
dz_σ/dσ = -σ ∇_z log p_σ(z_σ)
```

Using Tweedie's formula, the Euler step becomes:

```
z_{σ_ℓ} = z_{σ_{ℓ-1}} + (Δσ_ℓ/σ_{ℓ-1})(z_{σ_{ℓ-1}} - D_θ(z_{σ_{ℓ-1}}, σ_{ℓ-1}))
```

This matches the residual update form exactly — **the network itself acts as a denoiser**.

## 3-Step Conversion

### Step 1: Block Partitioning
Divide L layers into B blocks. Each block composes several consecutive layers.

### Step 2: Noise Range Assignment
Define noise distribution (log-normal, following EDM) over [σ_min, σ_max]. Partition into B intervals using **equi-probability partitioning** — each block handles exactly 1/B of the probability mass.

Boundaries: `σ_b = exp(P_mean + P_std · Φ⁻¹(q_b))`

### Step 3: Noise Conditioning
Augment block input to `(x, z_σ)` where `z_σ = y + σϵ`. Add noise-level conditioning via AdaLN (as in DiT). Blocks now act as conditional denoisers.

## Block-Independent Training

Each block b trained independently:

```
L_b(θ_b) = E[ w(σ) · Loss(f̄_{θ_b|σ}(x, y+σϵ), y) ]
```

- `w(σ)`: EDM weighting — `(σ² + σ_data²) / (σ · σ_data)²`
- Noise σ sampled from block's assigned range only
- Only L/B layers require gradient computation → **B× memory reduction**

## Inference

Starting from pure noise `z_0 ~ N(0, σ_max² I)`, iterate through noise levels, apply the block covering the current noise range, then Euler step. Typically T = B denoising steps.

## Architecture Adaptations

| Architecture | Adaptation |
|---|---|
| **ViT (classification)** | Noise added to class label embeddings; blocks denoise label conditioned on image patches |
| **Diffusion models (image gen)** | Natural fit — blocks directly act as denoisers |
| **Autoregressive LMs** | Noise in embedding space; causal consistency via concatenation |
| **Recurrent-depth transformers** | Block recurrence naturally fits iterative denoising |
| **Masked diffusion transformers** | Combined with masked training objectives |

## Key Results

- **Memory**: B× reduction (activations stored for L/B layers instead of L)
- **Performance**: competitive with end-to-end training on all tested architectures
- **Equi-probability partitioning** outperforms uniform partitioning
- **Log-normal noise** (EDM defaults: P_mean=-1.2, P_std=1.2) works best
- Scales block-wise training beyond small-scale classification to modern generative tasks

## Relationship to Other Block-Wise Methods

| Method | Theoretical Basis | Applicability |
|---|---|---|
| Forward-Forward | Ad-hoc local objectives (goodness) | Classification only |
| Greedy layer-wise | Autoencoder reconstruction | Limited architectures |
| **DiffusionBlocks** | Score matching / diffusion ODE | Any transformer with residuals |

DiffusionBlocks provides the first **principled, theoretically-grounded** block-wise training method that works across diverse transformer architectures without custom local objectives.

## Related Concepts

- [[concepts/score-matching]] — the training objective that enables block independence
- [[concepts/training-efficiency]] — broader context of reducing training cost
- [[concepts/memory-efficiency]] — memory optimization in deep learning
- [[concepts/diffusion-models]] — the diffusion framework that inspires this method
- [[concepts/residual-networks]] — the architectural pattern that enables the diffusion interpretation
- [[entities/sakana-ai]] — the lab behind DiffusionBlocks
