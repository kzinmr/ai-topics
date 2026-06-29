---
title: "KV Cache Compression and Its Infra Problems"
source: NVIDIA Research (EAI Lab)
author: Weian Mao et al.
date: 2026-06-15
url: https://research.nvidia.com/labs/eai/blogs/kv-cache-compression-and-its-infra-problems/
type: article
tags:
  - kv-cache
  - inference
  - optimization
  - nvidia
  - flash-attention
  - gpu
  - memory-efficiency
  - video-generation
---

# KV Cache Compression and Its Infra Problems

Source: https://research.nvidia.com/labs/eai/blogs/kv-cache-compression-and-its-infra-problems/

## Summary

NVIDIA Research blog post examining KV cache compression through an infrastructure lens — not only what the algorithms do, but whether they can actually run in production. Surveys the field's main methods (StreamingLLM, H2O, SnapKV, R-KV, etc.), identifies two critical infrastructure problems that most papers overlook, and presents TriAttention as a system-level solution.

## Two Infrastructure Problems

### Problem 1: FlashAttention Does Not Expose Attention Scores

Production inference runs on FlashAttention, which tiles attention through SRAM and never materializes the N×N score matrix in HBM. Most eviction methods (H2O, SnapKV, Scissorhands, etc.) need historical attention scores to decide which tokens to keep — but FlashAttention never writes those scores. H2O's reference implementation falls back to eager attention, abandoning FlashAttention entirely.

### Problem 2: Paged Attention Block Reclamation

Production serving systems (vLLM) manage KV cache with paged attention: GPU memory is divided into fixed-size physical blocks (~16 tokens each), and a block can only be freed when completely empty. Repeated decode-time eviction scatters survivors across blocks — evicting 14,400 of 16,000 tokens leaves 1,600 survivors spread across ~1,000 blocks, so almost no blocks become fully empty and the allocator reclaims almost nothing.

## Survey of Existing Methods

### StreamingLLM (2023)
- Keeps only attention sinks (first tokens) + sliding window of recent tokens
- No attention scoring needed, but information outside window is permanently lost

### H2O — Heavy-Hitter Oracle (2023)
- Maintains cumulative attention score per cached token across all decode steps
- Evicts lowest-scoring token after each step
- Requires full attention history → hits Infrastructure Problem 1

### Scissorhands (2023)
- Persistence of Importance hypothesis
- Similar scoring approach, same infrastructure collision

### SnapKV (2024)
- One-shot scoring at end of prefill using observation window of recent ~25 tokens
- Removes per-step bookkeeping, avoids cumulative scoring bias
- Limited by RoPE: only most recent queries reflect actual attention direction

### R-KV (2025)
- Designed specifically for reasoning models
- Reports 90% memory savings but measured with pre-allocated contiguous tensors, not vLLM
- Appendix D acknowledges paged attention integration "presents a non-trivial challenge"

### Quest (2024)
- Keeps full cache, only selects which pages each query reads
- KV memory still grows with context length

## TriAttention — System Solution

### Key Insight: Pre-RoPE Geometry
Instead of asking "which tokens received high attention recently?", asks "does the geometry of the model's learned representation space predict that a token will be important?" Scores tokens from stable pre-RoPE Q/K geometry — no attention scores needed at runtime.

### Forward-Packing Compaction
Consolidates survivors into dense prefix so tail blocks are actually freed:
- **Order-preserving repack**: slides survivors forward, cache stays in token order, minimal vLLM changes
- **Hole-filling variant**: drops survivors into vacated slots, less data movement but scrambled physical order

### Results (Qwen3-8B, 32K-token generation)
| Method | AIME 2024 | AIME 2025 | MATH 500 |
|--------|-----------|-----------|----------|
| Full Attention | 57.1% | 40.8% | 69.6% |
| SnapKV | 34.6% | 20.0% | 49.2% |
| R-KV | 25.4% | 17.5% | 46.4% |
| **TriAttention** | **42.1%** | **32.9%** | **56.0%** |

At budget 3,072 tokens: matches full-attention 40.8% accuracy, 2.5× higher throughput (563 vs 223 tok/s), 10.7× KV memory reduction.

## Video Generation Extension

- **Quant VideoGen** (ICML 2026): 2-bit KV cache quantization using adjacent-frame residuals, up to 7× memory compression
- **LongLive** (ICLR 2026): TriAttention scoring applied to Wan2.1-T2V-1.3B, 50% cache reduction with negligible quality drop
- **LongLive 2.0**: NVFP4 quantization + fused parallel dequantization kernel, 1.84× throughput on 5B-param generator

## References

- TriAttention: Mao W. et al., ICML 2026 — https://github.com/WeianMao/triattention
- StreamingLLM: Xiao G. et al., ICLR 2024 — arXiv:2309.17453
- H2O: Zhang Z. et al., NeurIPS 2023 — arXiv:2306.14048
- Scissorhands: Liu Z. et al., NeurIPS 2023 — arXiv:2305.17118
- TOVA: Oren M. et al., EMNLP 2024 — arXiv:2401.06104
- SnapKV: Li Y. et al., NeurIPS 2024 — arXiv:2404.14469
- PyramidKV: Cai Z. et al., 2024 — arXiv:2406.02069
- Ada-KV: Feng Y. et al., NeurIPS 2025 — arXiv:2407.11550
- Quest: Tang J. et al., ICML 2024 — arXiv:2406.10774
- R-KV: Cai Z. et al., NeurIPS 2025 — arXiv:2505.24133
- Quant VideoGen: Xi H. et al., ICML 2026 — arXiv:2602.02958
- LongLive: Yang S. et al., ICLR 2026 — arXiv:2509.22622
- LongLive 2.0: Chen Y. et al., 2026 — arXiv:2605.18739
