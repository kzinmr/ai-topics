---
title: "Multi-Token Residual Prediction (MRP)"
type: concept
created: 2026-07-02
updated: 2026-07-02
tags:
  - inference
  - optimization
  - diffusion
  - speculative-decoding
aliases: ["MRP", "Residual MTP", "Multi-Token Residual Prediction"]
sources:
  - raw/articles/modal.com--blog-multi-token-residual-prediction--56a6f835.md
  - "https://arxiv.org/abs/2605.18817"
  - "https://github.com/heavyball-research/multi-token-residual-prediction"
---

# Multi-Token Residual Prediction (MRP)

Multi-Token Residual Prediction (MRP) is a lightweight inference optimization technique for **Diffusion Language Models (DLMs)** that extends the [[concepts/multi-token-prediction|Multi-Token Prediction]] paradigm from autoregressive models to the diffusion setting. Developed by Modal Research and NYU Shanghai's HeavyBall Research, MRP predicts the **residual** (the difference between adjacent denoising steps) rather than the full next-step distribution — a critical adaptation that makes multi-step prediction viable for DLMs.

## Problem: Why Naïve MTP Fails on DLMs

Autoregressive MTP works by attaching a small head that predicts multiple future tokens from the backbone's hidden states. In diffusion LMs, however, a direct application collapses:

| Method | K=1 | K=2 | K=3 | K=4 |
|--------|-----|-----|-----|-----|
| **Naïve MTP** | 84.8 | 16.9 | 5.9 | 1.9 |
| **MRP** | 88.6 | 84.9 | 70.9 | 57.2 |

(GSM8K 0-shot CoT on SDAR-4B. K = prediction steps.)

The failure occurs because distilling the **full distribution** means every step must reproduce a large, high-dynamic-range target from scratch — errors compound rapidly. By K=4, naïve MTP collapses entirely.

## The Key Insight

The core insight comes from the Markov structure of denoising: each step perturbs only a handful of positions, so by a Lipschitz argument the predictive distribution at untouched positions can only move so far. The **residual between adjacent denoising steps** is a fundamentally easier target to predict than the full distribution, yet it encodes the information needed for multi-step decoding.

## How MRP Works

MRP is a small transformer (3 layers in the main configuration) attached to a frozen DLM backbone:

1. **Reads** the backbone's hidden states
2. **Predicts** the inter-step logit residual (not the full distribution)
3. **Adds** the residual to the backbone's own logits

Only the MRP module is trained. The training objective is a residual version of the MTP distillation loss: run the frozen backbone twice (before and after revealing a set of tokens), and train MRP with a KL divergence on the still-masked positions to minimize the difference.

## Two Operational Regimes

MRP serves two fundamentally different inference regimes with one trained module:

### 1. Static Regime (Lossless Speedup)

When output quality must be preserved, MRP acts as a **speculative drafter** — it proposes the next batch of tokens cheaply, and the backbone verifies in a single forward pass:

| Backbone | GSM8K | MATH500 | HumanEval | MBPP |
|----------|-------|---------|-----------|------|
| SDAR-4B | 90.0 / **1.36×** | 68.0 / **1.26×** | 67.7 / **1.35×** | 66.5 / **1.27×** |
| SDAR-8B | 90.4 / **1.40×** | 74.8 / **1.39×** | 72.6 / **1.34×** | 67.3 / **1.34×** |

(Accuracy % / throughput speedup over backbone baseline. Quality matches by construction.)

For **direct decoding** (skipping verification for higher throughput):

| Setting | GSM8K | MATH500 | HumanEval | MBPP |
|---------|-------|---------|-----------|------|
| Baseline (SDAR-8B) | 90.9 / 1× | 72.2 / 1× | 73.8 / 1× | 67.7 / 1× |
| MRP Step 1 | 90.1 / **1.59×** | 71.4 / **1.61×** | 67.1 / **1.53×** | 63.8 / **1.51×** |
| MRP Step 2 | 89.2 / **1.89×** | 70.8 / **1.91×** | 64.0 / **1.78×** | 59.9 / **1.75×** |

The key is that the user chooses the operating point — lossless when correctness is non-negotiable, faster when latency dominates.

### 2. Dynamic Regime (Quality Recovery)

In interactive settings where latency matters most (low unmasking threshold), MRP runs in the **opposite direction**: after the backbone over-reveals at a low threshold, MRP identifies tokens that were "confident in isolation" but would have been remasked with more context:

| Model | τ | GSM8K Improvement | HumanEval Improvement |
|-------|---|------------------|-----------------------|
| SDAR-4B | 0.5 | +17.7 (63.4→81.1) | +20.8 (32.3→53.1) |
| SDAR-8B | 0.5 | +14.4 (67.9→82.3) | +22.6 (32.3→54.9) |

Gains are largest at aggressive (low) thresholds where the backbone over-commits most, and shrink toward zero as τ rises.

## Architectural Insights

- **Optimal depth**: 2–3 layers. Accuracy plateaus beyond 3 layers while throughput drops. Shallower modules work better in speculative mode (verification corrects errors anyway).
- **No per-layer KV injection**: Unlike DFlash (~5 layers), MRP uses only input-layer hidden states, which is sufficient because the residual target is low-complexity.
- **Composable primitive**: MRP predictions are a cheap, accurate primitive that other methods can build on — the same module supports both speculative decoding and remasking.

## Significance

MRP represents a **fundamental extension of the MTP paradigm** from autoregressive to diffusion architectures. Prior to MRP, DLM inference optimization was a single Pareto curve trading quality for speed; MRP offers a third axis — the ability to **add accuracy where speed has already been prioritized**. This is particularly relevant as Diffusion LMs (SDAR, MDLM, etc.) gain adoption.

The technique also demonstrates a general principle: **predicting residuals rather than full distributions** may have broader applicability wherever the Markov structure constrains step-to-step change — a direction the authors signal for future work on kernel and serving-level optimization.

## Related Concepts

- [[concepts/multi-token-prediction]] — The original MTP paradigm for autoregressive models (Gemma 4)
- [[concepts/speculative-decoding]] — Speculative decoding techniques
- [[concepts/diffusion-language-models]] — Diffusion-based language models (SDAR, MDLM)
- [[concepts/inference]] — LLM inference optimization
