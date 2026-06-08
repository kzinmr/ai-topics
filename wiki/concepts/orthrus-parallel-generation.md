---
title: Orthrus (Parallel Token Generation)
created: 2026-05-22
updated: 2026-05-22
type: concept
tags:
  - concept
  - inference
  - optimization
  - kv-cache
  - model
  - training
  - diffusion
sources: [raw/articles/2026-05-22_orthrus-parallel-token-generation.md, https://arxiv.org/html/2605.12825]
---

# Orthrus

A **dual-architecture Transformer** framework that unifies autoregressive (AR) generation fidelity with diffusion-model parallel generation speed. Uses a frozen AR backbone + lightweight trainable diffusion head over a shared KV cache. Up to **7.8× token generation speedup** with lossless output (exact distributional parity).

## Architecture

### Two Views, One KV Cache

1. **Autoregressive View** (frozen): Standard causal self-attention for context pre-filling. Builds high-quality KV representations.
2. **Diffusion View** (trainable, ∼16% params): Parallel token generation operating over the same KV cache. Predicts K future tokens in a single forward pass.

### Intra-Model Consensus

At each decoding step:
1. Diffusion head projects K candidate tokens in a **single forward pass** (block size K=32, single-step projection)
2. Frozen AR head validates candidates — tokens matching AR distribution are accepted
3. On divergence, AR head corrects the token; shared KV cache is synchronized

This guarantees **exact distributional parity** with the base model — a form of exact rejection sampling without quality degradation.

## Key Results

| Metric | Value |
|---|---|
| Speedup | Up to 7.8× |
| Average effective tokens/forward | 5.39 (at 8B scale) |
| Trainable parameters | ∼16% of total |
| Fine-tuning data | <1B tokens |
| Training hardware | Single 8×H200 node, <24h |
| KV-cache overhead | O(1) |
| Base models tested | Qwen3-1.7B, 4B, 8B |

## Training

- Frozen AR model provides teacher distribution
- Diffusion head trained to minimize forward KL divergence from AR teacher on masked positions
- Block masking: K=32 positions with first token as anchor, rest masked
- 600K examples (balanced chat, math, code), FlashAttention-4 + FlexAttention

## Comparison to Speculative Decoding

Unlike [[concepts/speculative-decoding|speculative decoding]] which requires a separate draft model and creates KV-cache overhead, Orthrus:
- Shares the KV cache between AR and diffusion views
- Adds minimal parameters (16%) vs separate draft model
- Guarantees lossless output via consensus mechanism (same guarantee as speculative decoding)
- Single forward pass for K tokens vs sequential draft-then-verify

## Related

- [[concepts/speculative-decoding|Speculative Decoding]]
- [[concepts/kv-cache|KV Cache Optimization]]
- [[concepts/inference|LLM Inference]]
- [[concepts/diffusion|Diffusion Models]]
- [[concepts/quantization|Quantization]] — complementary inference optimization
