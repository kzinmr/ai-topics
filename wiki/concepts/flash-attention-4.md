---
title: "FlashAttention-4"
created: 2026-05-11
updated: 2026-06-12
type: concept
tags:
  - training
  - optimization
  - inference
  - hardware
  - nvidia
  - kv-cache
  - benchmark
  - lab
sources:
  - raw/articles/2026-03-05_togetherai_flashattention-4.md
  - raw/articles/2025-09-26_modal_reverse-engineer-flashattention-4.md
  - raw/articles/2026-06-11_modal_flashattention-4-faster-inference.md
aliases: ["FA4", "Flash Attention 4"]
related:
  - concepts/flash-attention
  - concepts/flashattention-3
  - concepts/blackwell-gpu
  - concepts/cuda-kernel
---

# FlashAttention-4

FlashAttention-4 (FA4) is the latest iteration of the FlashAttention series of CUDA kernels for Transformer attention, optimized for NVIDIA's Blackwell (B200) GPU architecture. It achieves up to **1605 TFLOPs/s (71% utilization)** on B200 with BF16 — up to **1.3× faster than cuDNN 9.13** and **2.7× faster than Triton**. Published March 2026 by Tri Dao (Princeton / Together AI), along with co-authors from Meta, Colfax Research, and NVIDIA.

## Core Innovation: Asymmetric Hardware Co-Design

FA4's design is driven by a fundamental observation about modern GPU scaling: **tensor core throughput grows much faster than other GPU resources**. From H100 to B200:
- BF16 tensor core throughput: 1 → 2.25 PFLOPs (2.25× increase)
- SFU count (for exponentials): unchanged
- Shared memory bandwidth: unchanged

This "asymmetric hardware scaling" means that in attention computation:
- **Forward pass bottleneck**: SFU units for softmax exponentials (not tensor cores)
- **Backward pass bottleneck**: shared memory traffic (not compute)

FA4 addresses both through algorithm-kernel co-design with three main techniques:

### 1. New Pipelining for Maximum Overlap

Exploits Blackwell's new hardware features:
- **Tensor Memory (TMEM)**: 256 KB per SM on B200 — on-chip scratchpad wired into tensor cores for warp-synchronous intermediate storage. Used to store attention probabilities `P` between forward matmuls, reducing register pressure.
- **Fully asynchronous 5th-gen tensor cores** (`tcgen05.mma`): UMMA tiles up to 128×256×16 — ~2× larger than Hopper WGMMA atoms. Launched by a single thread, enabling warp specialization without Hopper's spilling pain.
- **2-CTA MMA**: Blackwell can execute one UMMA across a CTA pair spanning both TMEM pools. Scales tile dimension to 256×256×16 by splitting M and N across the pair, reducing redundant traffic and lowering per-CTA footprint.

**Forward pass ping-pong schedule**: Processes two query tiles per CTA (Q^H and Q^L, each covering 128 query tokens) in alternating fashion. A dedicated "correction warpgroup" handles softmax rescaling off the critical path.

### 2. Faster Exponential via Hardware-Software Hybrid

Softmax exponentials bottleneck the forward pass because MUFU.EX2 throughput is far below tensor core throughput. FA4 distributes `exp` computation across:
- **Hardware**: MUFU.EX2 for part of the exponent computation
- **Software emulation**: FMA units (otherwise underutilized) compute polynomial approximation of `exp2`

Uses Cody-Waite range reduction: `2^x = 2^n · 2^f`, where `2^f` is approximated via a cubic polynomial in Horner's form. The two softmax warpgroups are explicitly synchronized to avoid evaluating `exp` simultaneously, reducing MUFU contention.

### 3. Conditional Online Softmax Rescaling

FA4 skips rescaling steps when the running max doesn't change significantly:

```
O_j = exp(m_{j-1} - m_j) · O_{j-1} + exp(S_j - m_j) · V_j    (if m_j - m_{j-1} > τ)
O_j = O_{j-1} + exp(S_j - m_{j-1}) · V_j                        (otherwise)
```

The final normalization `O_final = O / l_final` uses true final statistics, so skipping intermediate rescales preserves correctness while eliminating many vector computations. Decision is made at warp granularity to avoid divergence.

### 4. Backward Pass: Shared Memory Relief

- Stores intermediate results in TMEM instead of shared memory
- Uses 2-CTA MMA mode to reduce shared memory traffic further and cut atomic reductions in half
- Supports deterministic execution mode for reproducible training

### 5. Tile Scheduler

New tile scheduler mitigates load imbalance from causal masks and variable sequence lengths.

## Hardware Context: Blackwell B200

| Resource | H100 | B200 | Change |
|----------|------|------|--------|
| BF16 Tensor Core | 1 PFLOP | 2.25 PFLOPs | 2.25× |
| SFU count | same | same | 1× |
| Shared memory bandwidth | same | same | 1× |
| TMEM per SM | none | 256 KB | new |

## The "Feeds and Speeds" Analysis (M=N=D=128)

| Phase | Tensor Cores (cycles) | Exp (cycles) | SMEM (cycles) | Bottleneck |
|-------|----------------------|-------------|---------------|------------|
| Forward (2 MMA + MN exp) | 1024 | 1024 | 768 | Compute + Exp |
| Backward, 1-CTA (5 MMA + MN exp) | 2560 | 1024 | 3328 | **Shared memory** |

## Reverse-Engineering (Modal, Sept 2025)

Charles Frye and the Modal team reverse-engineered FA4 from the [open-source code](https://github.com/Dao-AILab/flash-attention) before the official paper was published. Their analysis (which made HackerNews front page) traces the "Life of a Tile" — how a block of Q/K/V inputs moves through the kernel:

1. Tiles loaded from global memory to shared memory
2. Asynchronous `tcgen05.mma` launched for `S = QK^T` (tensor memory accumulator)
3. Softmax: rowmax reduce → rowsum reduce → exp (hardware + software hybrid) → normalize → convert to BF16 → store P to TMEM
4. `PV` matmul triggered as soon as 3/4 of P is stored
5. Correction warpgroup handles rescaling, final normalization

The Modal team emphasized that FA4's architecture is understandable to general software engineers — the biggest innovation is the asynchronous pipeline complexity, not black-box math.

## Inference Optimization (Modal, June 2026)

In June 2026, Modal published a follow-up detailing their contributions to make FA4 faster for LLM inference — specifically **decode-heavy workloads**, where the memory bandwidth-limited token generation phase dominates (unlike pre-training, which is compute-bound). Inference introduces challenges absent in training: variable batch sizes, non-uniform sequence lengths, and keys/values retrieved from KV cache. The changes fall into two categories:

### Parallelism Strategy Adjustments

The original FA4 parallelizes across **query tiles** (query parallelism), which is well-suited for pre-training's many-query regime but leaves most SMs idle during decode, where batch sizes are small and queries are few. Modal made three key changes:

- **Split KV (Flash-Decoding)**: Ported the "split KV" technique from FA2, where multiple CTAs work concurrently per query tile, each processing a portion of the KV sequence, followed by a reduction step (`flash_fwd_combine`). This parallelizes across the KV dimension instead of the query dimension, achieving up to **4.37× memory throughput** for small query lengths. Flag: `num_splits = 0` triggers an automatic heuristic based on SM count and sequence length.
- **Single query tile mode** (`q_stage = 1`): The original kernel assumes ≥256 queries (two tiles of 128), wasting work on the second tile during decode. A single-tile path avoids this waste, achieving up to **3.06× throughput** for single-token decode. The freed second softmax warpgroup is repurposed for additional KV page loads.
- **GQA packing extension** (`pack_gqa = True`): Grouped-query attention (GQA) increases arithmetic intensity at inference, but by default FA4 handles each query head separately, redundantly loading KV data. GQA packing maps the group into a single tile. Modal extended this to work with `cp.async` loads (bypassing TMA alignment restrictions), enabling models like GLM 4.7 with irregular head ratios — yielding **2.92× throughput** for single-token decode.

### Handling Irregular Global Memory Accesses

The original FA4 uses the **Tensor Memory Accelerator (TMA)** for loading tiles via `cp.async.bulk`. TMA excels at large, regular affine memory accesses but struggles with small or scattered loads — exactly what KV cache retrieval produces, especially with small page sizes. Modal added `cp.async`-based load paths:

- **Arbitrary KV page sizes** (`page_size = 1`): TMA required pages to match tile size (128), causing severe internal fragmentation (>99% for single-token pages). Modal's `cp.async` path decouples page size from tile size. A key optimization was **transposing address generation**: instead of each thread redundantly computing its own row pointer (expensive 64-bit int ops), threads in different warp "columns" precompute pointers and share them via warp shuffles, achieving up to **2.40× throughput** for `page_size=1`.
- **FP8 support** (`dtype = 'fp8'`): Added e4m3/e5m2 8-bit float inputs, reducing memory and arithmetic bandwidth demand. Speedup reaches **1.16×** over BF16 baseline. The gain is less than the theoretical 2× because the softmax still runs at higher precision on CUDA Cores/SFUs.

### Signature Config

The "canonical" inference configuration combining all optimizations:
```
dtype = 'fp8', num_splits = 0, pack_gqa = True, q_stage = 1, page_size = 1
```

**Authors**: Charles Frye, Timothy Feng, David Wang (Modal). All contributions merged upstream into the [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) repository between November 2025 and April 2026.

## Performance

- **1605 TFLOPs/s** at 71% utilization on B200 (BF16)
- 1.3× faster than cuDNN 9.13
- 2.7× faster than Triton
- 20% improvement over prior state-of-the-art for attention kernels

## References

- [Paper: FlashAttention-4 (arXiv:2603.05451)](https://arxiv.org/abs/2603.05451)
- [Code: Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)
- [Together AI Blog: FlashAttention-4 announcement](https://www.together.ai/blog/flashattention-4) (March 5, 2026)
- [Modal Blog: We reverse-engineered Flash Attention 4](https://modal.com/blog/reverse-engineer-flash-attention-4) (September 26, 2025)
- [Modal Blog: Making FlashAttention-4 faster for inference](https://modal.com/blog/flash-attention-4-faster) (June 11, 2026)
- [HN Discussion of Modal reverse-engineering](https://news.ycombinator.com/item?id=45399637)

## See Also

- [[concepts/flash-attention]] — Original FlashAttention (Dao et al., 2022)
- [[concepts/blackwell-gpu]] — NVIDIA Blackwell architecture
- [[concepts/kv-cache-compression]] — FlashAttention's hidden scores create Infrastructure Problem 1 for eviction methods
- [[entities/charles-frye]] — Reverse-engineered FA4 and led inference optimization contributions (Modal)
