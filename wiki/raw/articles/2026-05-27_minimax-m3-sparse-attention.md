---
title: "MiniMax Teases M3 with Sparse Attention and 15.6x Speed Boost"
source: https://venturebeat.com/technology/minimax-teases-upcoming-m3-model-with-new-sparse-attention-mechanism-and-15-6x-response-speed-boost
date: 2026-05-27
---

# MiniMax M3 & MiniMax Sparse Attention (MSA)

MiniMax released a technical report on its M2 series while previewing M3 with MiniMax Sparse Attention (MSA), achieving up to 15.6x decoding speedup at 1M-token contexts.

## M2 Series
- 229.9B total params, 9.8B active per token, 256 fine-grained experts
- Full multi-head attention with GQA across all 62 layers
- Chose quadratic attention over sub-quadratic alternatives (SWA, Lightning Attention) due to multi-hop reasoning degradation

## MSA (MiniMax Sparse Attention)
- Built on standard GQA backbone with block-level selection on real, uncompressed KVs
- Unlike DeepSeek MLA (latent compression), MSA selects among real KV blocks
- 9.7x faster prefilling, 15.6x faster decoding at 1M tokens
- Solves precision loss and prefix-caching obstacles from M2

## Forge RL System
- Scalable RL infrastructure for long-horizon agent training
- Windowed FIFO Scheduling, Prefix Tree Merging (40x training speedup)
- M2.7 achieved 66.6% medal rate on MLE Bench Lite
