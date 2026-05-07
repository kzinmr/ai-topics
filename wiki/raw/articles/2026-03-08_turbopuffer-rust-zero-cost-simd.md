---
title: "Zero-Cost Abstractions: When Rust Iterator Chains Block SIMD Vectorization"
date: 2026-03-08
author: Xavier Denis (Engineer)
source_url: https://turbopuffer.com/blog/zero-cost
type: raw-article
tags: [turbopuffer, rust, simd, performance, iterator, lsm-tree, optimization]
---

# Zero-Cost Abstractions: When Rust Iterator Chains Block SIMD Vectorization

turbopuffer engineers discovered that Rust's iterator abstractions — normally "zero-cost" — were blocking SIMD vectorization in their LSM tree merge path, causing a **220ms → 47ms latency reduction** (4.7x improvement) through iterator batching.

> "Rust's zero-cost abstractions are zero-cost in terms of runtime overhead, but they can have a hidden cost: they prevent the compiler from seeing optimization opportunities."

## The Problem

The LSM tree merge iterator chains multiple iterators together:

```rust
// Original code — elegant but slow
let merged = merge(
    iter_a.chain(iter_b).chain(iter_c).chain(iter_d),
    |a, b| a.key.cmp(&b.key)
);
```

The compiler sees each individual `next()` call as a separate optimization boundary. LLVM cannot auto-vectorize across these boundaries because the chain depth prevents alias analysis and loop fusion.

### Root Cause

- **Rust's `Iterator::next()` returns `Option<Item>`** — each call is an opaque function boundary to LLVM
- **Multiple levels of indirection** — each `.chain()` adds a nesting level
- **LLVM's inlining heuristics** fail for deeply nested iterator chains
- **Result**: Scalar code generation instead of vectorized SIMD

## The Solution: Batched Iterators

Instead of yielding one value at a time, the batched iterator returns **512 values** per call:

```rust
// Batched iterator — returns chunks of 512 values
trait BatchedIterator {
    type Item;
    fn next_batch(&mut self, buf: &mut [Self::Item]) -> usize;
}
```

### Performance Impact

| Metric | Original (per-item) | Batched (512 items) | Improvement |
|:---|:---:|:---:|:---:|
| **Merge latency** | 220ms | 47ms | 4.7x |
| **Throughput** | baseline | 60x improvement | 60x |
| **SIMD utilization** | None | Full AVX-512 | — |

The 60x improvement comes from:
1. **SIMD vectorization** — LLVM can now auto-vectorize the inner loop
2. **Reduced function call overhead** — 512x fewer `next()` calls
3. **Better cache locality** — data loaded in contiguous batches
4. **Compile-time optimization** — LLVM sees full batch processing as a single optimization unit

## The Merge Iterator Bottleneck

The LSM tree's merge operation was identified as the primary bottleneck:

- **Multiple sorted runs** from different LSM levels need to be merged
- **Each run has its own iterator** — chained together for the merge
- **Deeply nested iterators** → LLVM gives up on optimization
- **Batched merge** enabled full SIMD for key comparison and ordering

## Key Insights

1. **Zero-cost abstractions are zero-cost at runtime but not at compile-time** — the compiler may not be able to see through them
2. **Batch processing unlocks SIMD** — the compiler needs to see large enough loops to justify vectorization
3. **512 is the magic number** for modern CPUs — large enough for SIMD amortization, small enough for L1 cache fit
4. **LSM merge is particularly sensitive** due to its memory-bound nature

## Key Contributors

- Xavier Denis (Engineer) — discovery and implementation of batched iterators

## Related

- Rust iterator optimization patterns
- SIMD programming in Rust
- LSM tree merge algorithms
