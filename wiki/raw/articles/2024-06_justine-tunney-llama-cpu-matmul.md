---
title: "LLaMA Now Goes Faster on CPUs"
source: "Justine Tunney's Blog"
url: "https://justine.lol/matmul/"
author: "Justine Tunney"
date: 2024-06
tags:
  - cpu-inference
  - optimization
  - matmul
  - llamafile
  - llama-cpp
  - arm
  - avx
---

# LLaMA Now Goes Faster on CPUs

Justine Tunney introduced **84 new matrix multiplication kernels** for llamafile, significantly improving prompt and image processing speeds on CPUs. Improvements range from **30% to 500% faster** than standard `llama.cpp` when using F16 and Q8_0 weights.

## Core Innovation: Vectorized Outer Products

Instead of unrolling the innermost loop (handled by CPU speculative execution), Tunney **unrolls the outer loops**, allowing a single register load to be shared across multiple FMA operations. This reduces memory references significantly.

## Performance Results (Prompt Tokens/s)

| Hardware | Model | Weights | llamafile-0.7 | llama.cpp (Mar 2024) |
|:---|:---|:---|:---|:---|
| Intel i9-14900K | TinyLlama 1.1B | f16 | **407** | 90 |
| RPi 5 (ARMv8.2) | TinyLlama 1.1B | f16 | **62** | 28 |
| M2 Ultra (CPU) | Mistral 7B | f16 | **79** | 57 |
| Threadripper 7995WX | Mistral 7B | f16 | **485** | 197 |

**Key Finding:** 2x faster than Intel MKL for matrices fitting in L2 cache (prompts under 1,000 tokens).

## Hardware-Specific Insights

- **ARMv8.2+ (RPi 5):** 2x boost using AVX512-derived kernels. Note: fp16 lacks Kahan summation → Q8_0 preserves better perplexity.
- **Intel Alderlake (i9-14900K):** Quintupled f16 perf using float32 compute internally. Avoids efficiency cores to prevent lockstep bottleneck.
- **Apple Silicon (M2 Ultra):** Vertical integration (RAM in CPU) makes token generation fast, but raw compute is only ~30% above high-end Intel.
- **AMD Zen 4 (Threadripper):** 7x more raw compute than M2 Ultra. Native bf16 support critical (Mistral is bf16; converting to fp16 loses precision for ~87% of representable numbers).

## Implications

The speedups are so significant that **memory bandwidth may no longer be the primary bottleneck** for CPU inference. This suggests:
- Quantization may become less necessary for speed (only for memory)
- CPU offloading during training could become more viable if CPUs can process tokens faster
- Custom kernel framework avoids OpenMP spinlock starvation in llama.cpp
