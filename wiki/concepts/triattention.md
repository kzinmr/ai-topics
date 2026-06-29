---
title: "TriAttention — Trigonometric KV Compression"
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
  - nvidia
sources:
  - raw/articles/2026-06-15_nvidia-kv-cache-compression-infra-problems.md
aliases:
  - triattention
  - trigonometric-kv-compression
---

# TriAttention — Trigonometric KV Compression

TriAttention is a KV cache compression method developed by NVIDIA Research (Weian Mao et al.) that resolves both critical infrastructure problems in KV cache compression simultaneously. Published at **ICML 2026**.

**Code**: https://github.com/WeianMao/triattention

## Core Innovation: Pre-RoPE Geometry Scoring

The key insight is that a stable geometric property of the model's learned Q/K vectors — **before RoPE rotation is applied** — predicts whether a token will be important at any distance. This replaces the need for observed attention scores entirely.

Instead of asking "which tokens received high attention recently?", TriAttention asks: "does the geometry of the model's learned representation space predict that a token will be important?"

### Why This Works

[[concepts/rope|RoPE]] (Rotary Position Embedding) orients every query by its position, so only the most recent ~25 queries reflect where the model is actually attending. This is why observation-window methods like SnapKV are limited. But the **pre-RoPE** Q/K geometry is position-independent and contains stable information about token importance regardless of distance.

## Solution to Infrastructure Problem 1

[[concepts/flash-attention-4|FlashAttention]] never writes attention scores to HBM — the N×N score matrix is computed entirely in SRAM. TriAttention never needs those scores, since it scores tokens from pre-RoPE geometry. Problem 1 does not apply.

## Solution to Infrastructure Problem 2: Forward-Packing Compaction

After scoring, survivors must be physically consolidated so that paged-attention allocators (vLLM) can reclaim fully-empty blocks. TriAttention runs consolidation roughly every 128 decoded tokens:

### Order-Preserving Repack
- Slides every survivor forward so cache stays in original token order
- No extra position bookkeeping, minimal changes to inference engine
- Single gather–clone–scatter pass: every survivor read before any written
- Emptied block returned to paged allocator

### Hole-Filling Variant
- Drops newest survivors into slots vacated by eviction
- Far less data movement per compaction (3 copies vs 18 in example)
- Scrambled physical order → must track each entry's logical position explicitly
- Available since v0.1.0

## Results

### Accuracy (Qwen3-8B, 32K-token generation)

| Method | AIME 2024 | AIME 2025 | MATH 500 |
|--------|-----------|-----------|----------|
| Full Attention (no compression) | 57.1% | 40.8% | 69.6% |
| SnapKV | 34.6% | 20.0% | 49.2% |
| R-KV | 25.4% | 17.5% | 46.4% |
| **TriAttention** | **42.1%** | **32.9%** | **56.0%** |

At budget 2,048 tokens (one-sixteenth of full 32K trace).

### Accuracy-Matched Comparison (AIME 2025)

At KV budget 3,072 tokens, TriAttention matches full-attention baseline (40.8%):
- **2.5× higher throughput**: 563 vs 223 tokens/second
- **10.7× KV memory reduction**

## Video Generation Extension

TriAttention's trigonometric scoring has been applied to **LongLive** (Yang et al., ICLR 2026), a real-time video generator built on Wan2.1-T2V-1.3B. Each KV entry corresponds to spatial patches from one frame; scoring decides which frames to evict — cutting cache by 50% with negligible quality drop. Integrated in the TriAttention repository.

## Open Questions

- **Per-head budget allocation**: TriAttention uses uniform KV budget across heads, but pre-RoPE distance-preference curves already classify heads by behavior (local, sink, range-specific). Natural next step: allocate budget proportional to head complexity.
- **Generalization**: Whether the pre-RoPE insight extends to model interpretability, dynamic sparse attention, other modalities.

## Related Concepts

- [[concepts/kv-cache-compression]] — The broader field of KV cache compression methods and infrastructure problems
- [[concepts/kv-cache]] — The underlying KV caching mechanism
- [[concepts/flash-attention-4]] — FlashAttention kernel (TriAttention avoids its limitations)
- [[concepts/rope]] — Rotary Position Embedding (pre-RoPE geometry is the key insight)
- [[concepts/kv-cache-compaction]] — Ramp Labs' attention-matching approach (different technique, same goal)
