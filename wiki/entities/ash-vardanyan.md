---
title: "Ash Vardanyan"
type: entity
created: 2026-05-27
updated: 2026-05-27
tags:
  - person
  - simd-optimization
  - search
  - open-source
  - infrastructure
aliases:
  - ashvardanian
  - Ash Vardanyan
  - Unum
sources:
  - https://ashvardanian.com/
  - https://github.com/ashvardanian
  - https://ashvardanian.com/posts/numkong/
  - https://ashvardanian.com/posts/stringwars-on-gpus/
  - https://ashvardanian.com/posts/javascript-ai-vector-search/
  - https://ashvardanian.com/posts/apple-m1/
---

# Ash Vardanyan

**Ash Vardanyan** (handle: `ashvardanian`) is an open-source developer and performance engineering specialist focused on SIMD-optimized kernels, vector search, and mixed-precision numerics. Creator of the **NumKong** (formerly SimSIMD), **StringZilla**, and **USearch** libraries, he works on making high-performance computing accessible across 7+ programming languages and multiple hardware architectures.

## Overview

Ash Vardanyan leads the **Unum** organization's open-source performance libraries. His work spans CPU-level SIMD optimization, GPU acceleration, and cross-language bindings for compute-intensive operations. Key technical contributions include:

- **NumKong** (formerly SimSIMD) — ~2,000 SIMD kernels for mixed-precision numerics across 7 languages (C99, C++23, Rust, Swift, JavaScript, Go, Python), supporting RISC-V Vector, Intel AMX, Arm SME, WebAssembly SIMD
- **StringZilla** — SIMD-optimized string processing, now extended to GPU (CUDA) with 500+ GigaCUPS of edit-distance calculations
- **USearch** — vector search engine leveraging NumKong for distance calculations and OpenMP for job scheduling
- **Fused MaxSim for ColBERT** — GPU-free late interaction scoring implementation for neural IR

His work is notable for targeting both server hardware (Xeon4 Sapphire Rapids with AMX) and consumer devices (Apple M4 with SME), with an emphasis on numerical precision as well as raw throughput.

## Key Projects

### NumKong (2026)
Rebranded from SimSIMD, NumKong is one of the largest collections of SIMD-optimized numeric kernels online (~200,000 lines of code, 2,000 kernels). It provides:

- **Mixed Precision Support**: From Float118 (double-double, ~106-bit mantissa) down to Float4 (E2M1), including native Int4/UInt4 dot products via nibble algebra
- **Multi-Architecture Coverage**: RISC-V Vector Extensions (RVV 1.0), Intel AMX (8×1KB tile registers), Arm SME (Scalable Matrix Extensions on M4+), WebAssembly Relaxed SIMD
- **ColBERT MaxSim Acceleration**: GPU-free late interaction scoring via SIMD — `maxsim_packed_f32` and `maxsim_packed_bf16` kernels. Achieves 3.3× speedup over NumPy on Xeon4 (428 vs 129 gso/s) with 4× less memory via fused epilogue (no intermediate score matrix materialization)
- **Geospatial Kernels**: Haversine & Vincenty implementations 5,300× faster than GeoPy
- **Mesh Alignment**: Kabsch & Umeyama algorithms 200× faster than BioPython
- **Ozaki Scheme for Float64 GEMMs**: Achieved via Float32 tile hardware (Intel AMX)
- **Neumaier & Dot2**: Higher-than-BLAS precision accumulation
- **Block-Scaling Rejection**: NumKong explicitly rejects MXFP4/NVFP4 block-scaled formats for dot product primitives — "dequantize first, then process" to preserve element independence

**Fused Epilogue Design**: Traditional ColBERT MaxSim materializes the full `N_query × N_doc` score matrix before reduction. NumKong's fused approach tiles data through registers, progressively reducing to a scalar — eliminating megabytes of intermediate memory. The same pattern applies to bilinear forms (`aᵀ × C × b`) without materializing the intermediate vector.

**Performance on Intel Xeon4 (single-threaded):**
| Input | NumPy+OpenBLAS | PyTorch+MKL | NumKong |
|-------|---------------|-------------|---------|
| Float64 | 65.5 gso/s, 1e-15 err | 68.2 gso/s, 1e-15 err | 8.6 gso/s, 1e-16 err |
| Float32 | 140 gso/s, 9e-7 err | 145 gso/s, 1e-6 err | 37.7 gso/s, 4e-7 err |
| BFloat16 | — | 851 gso/s, 1.8% err | 458 gso/s, 3.6% err |
| Int8 | 0.4 gso/s, overflow | 50 gso/s, overflow | 1,279 gso/s, 0% err |

Notably, NumKong prioritizes numerical precision over raw throughput — NumKong's Int8 achieves 0% error vs overflow in OpenBLAS/PyTorch, and Float64 achieves lower error (1e-16) despite lower throughput.

### StringZilla (2024–2026)
SIMD-optimized string processing library. v4 added CUDA GPU acceleration, delivering 500+ GigaCUPS of edit-distance calculations. Originally started as conference talk material in the late 2010s showcasing AVX-512 vectorization of non-data-parallel workloads.

### USearch
Vector search engine that uses NumKong for distance calculations and OpenMP for job scheduling. Supports bindings for NodeJS and other runtimes. Enables SIMD-accelerated ANN search on ARM Neoverse N2 (AWS Graviton3) with 10× performance boost over pure AVX2 baselines.

## Hardware Architecture Philosophy

Ash's work demonstrates a key convergence trend in hardware: **every major vendor is arriving at tiled mixed-precision multiply-accumulate** — just with different register files, predicate models, and memory hierarchies.

His comparison of Intel AMX vs Arm SME vs RISC-V RVV vs NVIDIA Tensor Cores shows that CPUs and GPUs are becoming increasingly similar in their approach to matrix operations. The key insight is that the CPU's role in modern data centers is shifting from pure compute to "connecting sub-systems and guaranteeing correctness" — making numerical precision a first-class concern alongside throughput.

**Arm SME on Apple M4** is particularly notable as the most efficient hardware for mixed-precision numerics among consumer chips — achieving 4,027 gso/s (4+ TOPS) on a single core for 4096³ dense matrix operations, nearly 10× the tiled GEMM-like NEON kernel for the same task. SME's composability makes it the "most convenient platform for advanced AI architectures, opening the door to fusing entire Transformer attention blocks — GEMM + SoftMax + GEMM — on Apple M4 and M5 without leaving streaming mode."

## ForkUnion: NUMA-Aware Thread Pooling

A recurring pain point in high-performance numeric computing is thread management — particularly on heterogeneous and NUMA architectures:

- **Apple M4**: 4 performance cores + 6 efficiency cores at different frequencies — equal thread splits leave fast cores idle
- **Intel 2-socket Xeon4**: NUMA nodes with vastly different memory latencies — cross-socket reads pay 2-3× latency
- **OpenBLAS**: Allocates per-thread buffers via `mmap` behind every GEMM — leading to 14 lock/unlock pairs per small multiply, deadlocks after `fork()`, and silently wrong results

Ash is building **ForkUnion** — a NUMA-aware fork-join thread pool with core pinning and heterogeneous QoS awareness. The design philosophy: "No hidden allocations. No hidden threads. You own the buffer, you own the threads."

Key design patterns:
- Each NUMA node gets a local copy of packed B, works on local A slices, writes to local C rows
- `nk_configure_thread()` flushes denormals to zero, requests AMX tile permission via `ARCH_REQ_XCOMP_PERM`, sets rounding mode
- No mutexes, no dynamic allocation on the hot path, no CAS primitives

## Writing Style

Ash's blog posts are deeply technical, combining:
- Detailed benchmark tables with specific hardware configurations
- Code-level instruction explanations (e.g., `_tile_dpbf16ps`, `svfmopa_za32_f16_m`)
- Cross-architecture comparisons with performance/accuracy tradeoffs
- Practical guidance for developers using the libraries in production
- Geopolitical context for hardware trends (RISC-V adoption driven by US-China tensions)

## Cross-References

- [[concepts/model-quantization]] — NumKong's mixed precision kernels complement LLM quantization at the CPU level
- [[concepts/colbert]] — Fused MaxSim implementation enables GPU-free late interaction scoring
- [[concepts/vector-search]] — USearch provides ANN search with SIMD acceleration
- [[concepts/simd-optimization]] — NumKong is the canonical implementation
- [[concepts/fused-kernels]] — NumKong's fused epilogue pattern for eliminating intermediate memory
- [[entities/unum]] — Organization behind the libraries
- [[entities/forkunion]] — NUMA-aware thread pool project

## Sources

- [ashvardanian.com — NumKong](https://ashvardanian.com/posts/numkong/) — SimSIMD rebrand, 2,000 SIMD kernels, multi-architecture coverage (Scraped 2026-05-05)
- [ashvardanian.com — StringZilla on GPUs](https://ashvardanian.com/posts/stringwars-on-gpus/) — CUDA extension, 500+ GigaCUPS
- [ashvardanian.com — JavaScript AI Vector Search](https://ashvardanian.com/posts/javascript-ai-vector-search/) — USearch NodeJS bindings, SimSIMD usage
- [ashvardanian.com — Apple M1](https://ashvardanian.com/posts/apple-m1/) — ARM optimization insights
- [GitHub: ashvardanian](https://github.com/ashvardanian)
