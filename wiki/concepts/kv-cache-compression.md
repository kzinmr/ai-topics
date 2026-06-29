---
title: "KV Cache Compression"
created: 2026-06-29
updated: 2026-06-29
type: concept
tags:
  - kv-cache
  - inference
  - optimization
  - memory-efficiency
  - sparse-attention
  - gpu
  - survey
sources:
  - raw/articles/2026-06-15_nvidia-kv-cache-compression-infra-problems.md
  - raw/articles/martinalderson.com--posts-a-brief-history-of-kv-cache-compression-developments--c7414ee7.md
aliases:
  - kv-cache-eviction
  - token-eviction
---

# KV Cache Compression

KV Cache Compression is a family of techniques for reducing the memory footprint of the [[concepts/kv-cache|KV cache]] during Transformer inference, enabling longer context lengths on fixed GPU memory. The core observation is that **attention is sparse** — a small fraction of tokens collect the overwhelming majority of attention weight — so tokens that never get attended to can theoretically be deleted without changing outputs.

## Why It Matters

Every generated token appends new K and V rows across all layers and heads. For a model like Qwen3-32B with 4-bit quantized weights on a 24 GB GPU, OOM occurs after ~24K generated tokens — short of the 32K-token traces reasoning models routinely produce on hard problems.

## Method Categories

### Fixed-Rule Methods

**StreamingLLM** (Xiao et al., ICLR 2024): Keeps only two kinds of tokens — a handful of "attention sinks" at the very start (not semantically important but always attended to) and a sliding window of recent tokens. Memory stays constant, but information outside the window is permanently lost. No attention scoring needed.

### Attention-Score-Based Eviction

The largest category. Uses the model's own historical attention scores to decide which cached tokens are "heavy hitters."

- **H2O** (Zhang et al., NeurIPS 2023): Maintains cumulative attention score per token, evicts lowest-scoring after each decode step. Requires full attention history per step.
- **Scissorhands** (Liu et al., NeurIPS 2023): Persistence of Importance hypothesis — tokens important once tend to remain important.
- **SnapKV** (Li et al., NeurIPS 2024): One-shot scoring at end of prefill using an observation window of recent ~25 queries. Removes per-step bookkeeping. Most influential refinement.
- **TOVA** (Oren et al., EMNLP 2024): Transformers as Multi-State RNNs, alternative scoring signal.
- **PyramidKV** (Cai et al., 2024): Per-layer, per-head budget splitting.
- **Ada-KV** (Feng et al., NeurIPS 2025): Adaptive budget allocation per head.

### Geometry-Based Methods

- **[[concepts/triattention|TriAttention]]** (Mao et al., ICML 2026): Scores tokens from pre-RoPE Q/K geometry rather than observed attention. No attention scores needed at runtime.

### Query-Selection Methods

- **Quest** (Tang et al., ICML 2024): Keeps full cache, selects which pages each query reads. KV memory still grows with context length.

### Reasoning-Specific Methods

- **R-KV** (Cai et al., NeurIPS 2025): Designed for reasoning models. Reports 90% savings but measured with pre-allocated tensors, not in production serving systems.

## Two Critical Infrastructure Problems

Most compression research evaluates algorithms in isolation from production serving infrastructure. Two problems block deployment:

### Problem 1: FlashAttention Does Not Expose Attention Scores

Production inference runs on [[concepts/flash-attention-4|FlashAttention]], which tiles attention through SRAM and **never materializes the N×N score matrix in HBM**. Eviction methods that need historical attention scores (H2O, SnapKV, Scissorhands) cannot read them. H2O's reference implementation falls back to eager attention, abandoning FlashAttention entirely.

### Problem 2: Paged Attention Block Reclamation

Production serving systems (vLLM) manage KV cache with **paged attention**: GPU memory is divided into fixed-size physical blocks (~16 tokens each), freed only when completely empty. Repeated decode-time eviction scatters survivors across blocks — evicting 14,400 of 16,000 tokens leaves survivors in ~1,000 blocks, reclaiming almost no memory. R-KV acknowledges this as "a non-trivial challenge."

## Quantization Track

Separate from eviction — reduces precision of stored KV entries:

- **Quant VideoGen** (ICML 2026): 2-bit KV quantization using adjacent-frame residuals for video generation, up to 7× compression
- **LongLive 2.0**: NVFP4 (4-bit) quantization with fused parallel dequantization kernel, 1.84× throughput

## Key Insight (from NVIDIA Research)

> Good compression is not primarily about finding the right scoring heuristic. It is about understanding why a signal has the structure it has — and exploiting that structure at the kernel level.

The field's 2023–2025 framing was: find the right heuristic for which tokens matter. The emerging framing is: score tokens from the model's stable geometric properties (pre-RoPE Q/K structure) and physically consolidate survivors into dense prefixes so paged allocators can reclaim blocks.

## Related Concepts

- [[concepts/kv-cache]] — The underlying caching mechanism
- [[concepts/kv-cache-compaction]] — Ramp Labs' attention-matching compaction for multi-agent systems
- [[concepts/triattention]] — NVIDIA's trigonometric KV compression (system solution to both infra problems)
- [[concepts/flash-attention-4]] — FlashAttention kernel that hides attention scores
- [[concepts/kv-aware-routing]] — Request routing based on KV cache state overlap
- [[concepts/context-engineering]] — KV cache as foundational technology for context optimization
