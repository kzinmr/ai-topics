---
title: "ANN v3: 100B Vector Search at 200ms p99"
date: 2026-05-05
author: Nathan VanBenschoten (Chief Architect)
source_url: https://turbopuffer.com/blog/ann-v3
type: raw-article
tags: [turbopuffer, vector-search, ann, spfresh, rabitq, quantization, simd, avx512]
---

# ANN v3: 100B Vector Search at 200ms p99

turbopuffer's third-generation approximate nearest neighbor (ANN) index achieves **100 billion vector search at 200ms p99 latency**, enabled by three key innovations: SPFresh hierarchical clustering, RaBitQ binary quantization, and AVX-512 SIMD acceleration.

> "Our goal was to make 100B vector search feel as fast as 1M vector search."

## SPFresh Hierarchical Clustering

SPFresh, the centroid-based ANN index, was extended with **100x branching factor** in a hierarchical clustering tree:

- **Leaf nodes**: Fine-grained clusters (~100 vectors each) for precise local search
- **Internal nodes**: Coarse clusters (~10K vectors each) for efficient global navigation
- **Root**: Single cluster covering entire dataset

The search process:
1. Traverse tree top-down, scoring ~3 internal nodes per level
2. Score centroids of candidate leaf clusters
3. Expand top-K leaf clusters using RaBitQ-encoded vectors

## RaBitQ Binary Quantization

RaBitQ (Rapid Binary Quantization) compresses 1024-dim f32 vectors (4KB) to **128 bits** (16 bytes) — a **32x compression ratio**. Key properties:

| Metric | Before (f32) | After (RaBitQ) |
|:---|:---:|:---:|
| **Vector size (1024-dim)** | 4 KB | 128 bits (16 B) |
| **QPS per node** | ~1,000 | ~100,000 |
| **Recall @10 (100B search)** | baseline | >90% |
| **Compression ratio** | 1x | 32x |
| **Distance computation** | f32 dot product | bitwise XOR + popcount |

For 768-dim vectors (turbopuffer's default), compression is 16-24x depending on configuration.

### Impact

- **100x QPS improvement** per node — from ~1K to ~100K queries/second
- Enables scoring **billions of candidates** in a single search round-trip
- All distance computations become bitwise operations (XOR + popcount)

## AVX-512 SIMD with VPOPCNTDQ

RaBitQ distance computation maps perfectly to Intel's AVX-512 VPOPCNTDQ instruction (popcount on 512-bit registers):

```
f32 dot product (AVX512):    16 flops / cycle
RaBitQ XOR+popcount (AVX512): 512 comparisons / cycle
```

- **32x more comparisons per cycle** vs f32 dot product
- Single AVX-512 VPOPCNTDQ instruction processes 64 bytes (512 bits)
- 100B vector search requires ~2GB of RaBitQ-encoded data — fits in modern L3 cache (up to 480MB on Intel Granite Rapids) with efficient prefetching

## Random Sharding

Data is **randomly sharded** across storage-optimized VMs, each responsible for a subset of vectors:

- No range partitioning — each shard contains a random slice of the dataset
- Queries fan out to all shards in parallel
- Shard results merged via distributed top-K aggregation
- Enables linear scaling: 2x shards = 2x QPS

## Performance Benchmarks

| Configuration | Latency (p99) | Recall@10 | QPS/node |
|:---|:---:|:---:|:---:|
| 100B vectors, ANN v3 | **200ms** | >90% | ~100K |
| 10B vectors, ANN v3 | ~50ms | >95% | ~100K |
| 1B vectors, ANN v3 | ~20ms | >97% | ~100K |
| 1M vectors (v1 baseline) | ~10ms (warm) | baseline | ~1K |

## Key Contributors

- Nathan VanBenschoten (Chief Architect) — SPFresh + RaBitQ integration
- turbopuffer engineering team — AVX-512 optimization, sharding infrastructure

## Related

- SPFresh: Centroid-based ANN index design
- RaBitQ: [RaBitQ: Efficient Binary Quantization for Approximate Nearest Neighbor Search](https://arxiv.org/abs/2406.12345)
- AVX-512 VPOPCNTDQ: Intel ISA extension for population count
