---
title: "Fused Kernels (Eliminating Intermediate Memory)"
type: concept
created: 2026-05-27
updated: 2026-05-27
tags:
  - optimization
  - fused-kernels
  - memory-efficiency
  - simd
  - colbert
  - maxsim
  - performance-engineering
related:
  - concepts/colbert
  - concepts/simd-optimization
  - entities/ash-vardanyan
sources:
  - raw/articles/ashvardanian.com--posts-numkong--e99e0a28.md
---

# Fused Kernels (Eliminating Intermediate Memory)

**Fused kernels** are a performance optimization technique in which multiple computation steps are combined into a single pass, eliminating the need to materialize intermediate data structures in memory. In the context of LLM inference and neural information retrieval, this pattern dramatically reduces memory bandwidth and cache pressure.

## The Problem: Intermediate Materialization

Many standard linear algebra and ML operations create temporary buffers that dominate memory usage:

- **ColBERT MaxSim**: Traditional NumPy/PyTorch computes the full `N_query × N_doc` similarity matrix before applying the Max reduction — megabytes of temporary memory for real workloads with thousands of tokens.
- **Bilinear forms**: Computing `aᵀ × C × b` typically materializes the `C × b` intermediate vector before the outer dot product.
- **Transformer attention**: The standard pattern `Attention(Q, K, V) = SoftMax(QKᵀ)V` materializes the full `QKᵀ` attention matrix before SoftMax.

These intermediates are not just wasteful — they force data to move between CPU caches and main memory, creating a memory-bandwidth bottleneck that no amount of compute acceleration can overcome.

## The Solution: Progressive Reduction

Fused kernels address this by streaming data through registers and progressively reducing intermediate results:

```python
# Traditional approach (NumPy) — materializes full score matrix
scores = np.matmul(query, doc.T)   # O(N_query × N_doc) temporary memory
result = scores.max(axis=1).sum()  # reduction after materialization

# Fused approach (NumKong) — no intermediate matrix
query_packed = nk.maxsim_pack(query.astype(nk.bfloat16))
doc_packed = nk.maxsim_pack(doc.astype(nk.bfloat16))
result = nk.maxsim_packed(query_packed, doc_packed)  # progressive reduction in registers
```

The key insight: **tiles flow from one register to another and are progressively reduced to a single scalar**. The intermediate matrix never exists in main memory — only the running maximum accumulates in the CPU register file.

## Real-World Results

**ColBERT MaxSim on Intel Xeon4 (single-threaded, 2048³)**:

| Implementation | Throughput | Memory Footprint | Accuracy |
|---|---|---|---|
| NumPy f32→f32 | 129 gso/s | Full score matrix materialized | Baseline |
| NumKong BFloat16 | **428 gso/s** (3.3×) | 4× less memory overall | 3.6% error vs 1.8% (PyTorch MKL) |

**Bilinear form** (`aᵀ × C × b`):
Same pattern — eliminates the `C × b` intermediate vector. Useful for Mahalanobis distance, attention scoring, and quadratic forms.

## Design Principle: "Dequantize First, Then Process"

NumKong explicitly rejects block-scaled quantization formats (MXFP4, NVFP4) for fused dot product primitives. The rationale: block scaling couples elements through shared exponents — a group of 32 values shares one scale factor, so each element's precision depends on its neighbors. This violates the fundamental invariant that `dot(a, b)` treats every element independently.

**Guideline**: If data arrives in MXFP4 format, unpack to 8-bit mini-floats *before* calling the fused kernel. The conversion cost is trivial compared to the multiply-accumulate, and element independence is preserved.

## Beyond MaxSim: Transformer Attention Fusion

The fused kernel pattern generalizes to entire Transformer blocks. On Apple M4/M5 with Arm SME (Streaming SVE Mode), it is possible to fuse GEMM + SoftMax + GEMM — the complete attention mechanism — without leaving streaming mode. This eliminates the memory roundtrips that dominate attention latency on conventional architectures.

## Related: ForkUnion Thread Pool

Fused kernels are only effective when paired with careful thread management. OpenBLAS allocates per-thread buffers via `mmap` behind every GEMM — leading to lock contention, deadlocks after `fork()`, and silently wrong results. [[entities/forkunion|ForkUnion]] addresses this with a NUMA-aware fork-join thread pool that guarantees "no hidden allocations, no hidden threads."

## Graph Structure Query

```
[fused-kernels] ──extends──→ [concept: simd-optimization]
[fused-kernels] ──applies-to──→ [concept: colbert]
[fused-kernels] ──implemented-by──→ [entity: numkong]
[fused-kernels] ──enables──→ [concept: memory-efficient-attention]
```

This concept enables graph queries: "find all techniques that eliminate intermediate buffers" → fused-kernels. "Which ColBERT implementations use fused kernels?" → NumKong via this concept.

## Related Concepts
- [[concepts/colbert]] — MaxSim scoring benefits from fused epilogue
- [[concepts/simd-optimization]] — Hardware-level implementation of fused kernels
- [[entities/ash-vardanyan]] — Creator of NumKong, the canonical fused MaxSim implementation
- [[entities/forkunion]] — Thread pool that preserves fused kernel memory discipline
- [[concepts/model-quantization]] — Dequantize-first principle interacts with fused kernels

## Sources
- [NumKong: 2,000 Mixed Precision Kernels For All](https://ashvardanian.com/posts/numkong/) — Fused MaxSim epilogue, bilinear forms, block-scaling rejection (Scraped 2026-05-27)
