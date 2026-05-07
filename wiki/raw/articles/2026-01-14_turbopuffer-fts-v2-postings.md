---
title: "FTS v2 Postings: Building Better Inverted Indexes on Object Storage"
date: 2026-01-14
authors: [Morgan Gallant, Adrien Grand]
source_url: https://turbopuffer.com/blog/fts-v2-postings
type: raw-article
tags: [turbopuffer, full-text-search, inverted-index, bitpacking, lsm-tree, quickwit, compression]
---

# FTS v2 Postings: Building Better Inverted Indexes on Object Storage

A deep dive on the KV-store inverted index design for FTS v2, comparing cluster-based (v1) vs fixed-size block partitioning (v2). Achieves **9.9x index size reduction** (51.6 GiB → 5.22 GiB on MSMARCO) and **741M postings/sec** decompression.

> "The key insight: on object storage, fixed-size blocks are better than variable-size clusters for inverted indexes."

## Cluster-Based (v1) vs Fixed-Size Block (v2)

### v1: Cluster-Based Partitioning

Original design partitioned postings by document cluster (SPFresh centroid proximity):

```
Term "database":
  ┌─────────────────────────────────────┐
  │ Block: Cluster A (42 postings)      │ ← small, poor compression
  ├─────────────────────────────────────┤
  │ Block: Cluster B (1,204 postings)   │ ← large, good compression, more work
  ├─────────────────────────────────────┤
  │ Block: Cluster C (315 postings)     │
  └─────────────────────────────────────┘
```

**Problems:**
- Variable-size blocks → unpredictable disk I/O
- Small clusters → poor compression ratio (delta encoding needs density)
- Large clusters → more work than needed for scoring
- Cluster boundaries don't align with query execution units

### v2: Fixed-Size Block Partitioning

Each block contains exactly ~256 postings:

```
Term "database":
  ┌─────────────────────────────────────┐
  │ Block 0: postings 0-255  (256)      │ ← always 256
  ├─────────────────────────────────────┤
  │ Block 1: postings 256-511 (256)     │ ← optimal for compression
  ├─────────────────────────────────────┤
  │ Block 2: postings 512-767 (256)     │ ← optimal for SIMD
  └─────────────────────────────────────┘
```

## Why N=256?

Three factors determine the optimal block size:

### 1. Compression Efficiency
- **Delta encoding** works better with more postings (denser deltas → smaller)
- **Bitpacking** has overhead per block (schema, width metadata)
- **Sweet spot**: ~256 postings balances per-block overhead vs encoding efficiency

### 2. Skip Performance
- Block is the minimum unit to skip during MAXSCORE pruning
- Smaller blocks → more precise skipping (skip entire block if max score < threshold)
- Larger blocks → fewer blocks to scan on average (less overhead)
- **256 postings**: skip granularity is ~256 documents optimal for precision

### 3. Overhead Balance
- **Block metadata**: doc ID range, max score, block stats (~32 bytes per block)
- **256 postings × 8 bytes avg** = ~2KB of posting data per block, plus ~32B metadata
- **~1.6% overhead** for metadata — the sweet spot

## Index Size Comparison (MSMARCO)

| Component | FTS v1 | FTS v2 | Ratio |
|:---|:---:|:---:|:---:|
| **Doc IDs** | 25.7 GiB | 2.62 GiB | 9.8x |
| **Term Frequencies** | 12.2 GiB | 1.12 GiB | 10.9x |
| **Positions** | 13.7 GiB | 1.48 GiB | 9.3x |
| **Total** | **51.6 GiB** | **5.22 GiB** | **9.9x** |

## Quickwit Bitpacking

turbopuffer adopted Quickwit's bitpacking library for posting list encoding:

- **Achieves 741M postings/sec** decompression throughput
- **SIMD-accelerated**: AVX-512 paths for bit unpacking
- **Schema-per-block**: Each block stores its own bit width for optimal packing
- **Block-level compression**: Delta of delta encoding for document IDs

```
Decode performance:
  Quickwit bitpacking: 741M postings/s
  VByte (baseline):    200M postings/s
  Simple-8b:           400M postings/s
```

## KV Store Design

The inverted index lives in turbopuffer's custom LSM tree:

```
Key format:   (term_hash: u64, block_id: u32)
Value format: BitpackedBlock {
    doc_ids:      DeltaEncoded<Bitpacked<u32>>,
    term_freqs:   Bitpacked<u16>,
    positions:    Option<DeltaEncoded<Bitpacked<u16>>>,
    max_score:    f32,
    num_postings: u16,
}
```

- **LSM-friendly**: Sequential writes from WAL replay
- **Object-storage-aware**: Blocks are the unit of caching and I/O
- **Cache-friendly**: 4KB block size matches NVMe SSD pages

## Key Contributors

- Morgan Gallant (Engineer) — inverted index design
- Adrien Grand (Engineer) — compression analysis, benchmarking

## Related

- [[raw/articles/2026-02-03_turbopuffer-fts-v2]] — FTS v2 overview
- [[raw/articles/2026-01-14_turbopuffer-fts-v2-maxscore]] — MAXSCORE pruning
- Quickwit bitpacking: [quickwit-oss/bitpacking](https://github.com/quickwit-oss/bitpacking)
