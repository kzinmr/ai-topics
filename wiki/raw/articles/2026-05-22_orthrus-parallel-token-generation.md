2026-05-22 | arXiv:2605.12825 | Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion
=========================================================================================================
Source: https://arxiv.org/html/2605.12825
Code: https://github.com/chiennv2000/orthrus
Authors: Chien Van Nguyen et al.

# Orthrus: Memory-Efficient Parallel Token Generation

A dual-architecture Transformer that unifies autoregressive fidelity with diffusion-model parallel generation speed.

## Architecture
- Frozen autoregressive backbone handles context pre-filling, builds KV cache
- Lightweight trainable diffusion module (∼16% of parameters) operates over same KV cache
- Intra-model consensus mechanism guarantees lossless inference (exact distributional parity)

## Key Results
- Up to 7.8× speedup in token generation
- O(1) KV-cache overhead (shares AR cache)
- Only ∼16% parameters trainable, <1B tokens fine-tuning, <24h on 8×H200
- Base models: Qwen3-1.7B, 4B, 8B

## How It Works
1. AR head pre-fills context (causal attention) → high-quality KV cache
2. Diffusion head projects K candidate tokens in single forward pass (masked block prediction)
3. AR head validates candidates; mismatches corrected by teacher AR distribution
4. Block size K=32, single-step projection (no iterative denoising)
