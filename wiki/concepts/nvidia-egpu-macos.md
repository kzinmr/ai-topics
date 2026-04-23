---
title: "NVIDIA eGPU on macOS"
type: concept
status: draft
created: 2026-04-23
updated: 2026-04-23
tags:
  - gpu
  - local-llm
  - apple-silicon
  - nvidia
  - inference-optimization
sources:
  - https://www.lucebox.com/blog/egpu-myth
related:
  - lucebox.md
  - sandro-puppo.md
  - davide-ciffa.md
  - llama-cpp.md
  - tinygrad.md
---

# NVIDIA eGPU on macOS

Research into running NVIDIA GPUs as external GPUs (eGPUs) on Apple Silicon Macs via Thunderbolt/USB4, enabled by tinygrad's custom NVIDIA driver (DEXT).

## Background

In 2018, Apple and NVIDIA had a falling out. Apple dropped NVIDIA support in macOS Mojave, killing CUDA entirely. For seven years, NVIDIA compute on macOS was impossible.

tinygrad built a macOS driver extension (DEXT) called **TinyGPU** from scratch — no NVIDIA drivers needed, no Linux needed. Apple signed the extension. It supports Ampere, Ada Lovelace, and Blackwell architectures.

## Key Findings

### The Driver Works, The Inference Is Slow

On Qwen3-8B Q4 (tinygrad's built-in benchmark), every eGPU lands between 2.28 and 6.0 tok/s. On Qwen3-4B Q4 via llama-bench:
- llama.cpp on Metal (M4 Pro): **~74 tok/s**
- tinygrad eGPU (RTX 5090): **7.39 tok/s**
- **10x performance gap**

### Bottleneck Is Software, Not Cable

GPUs use only 1.2-1.6% of their own memory bandwidth. USB4/Thunderbolt is not the constraint — the inference software stack is immature.

## Blackwell GPU Benchmarks

### Matrix Multiplication

| GPU | TFLOPS | vs M4 Pro |
|-----|--------|-----------|
| M4 Pro (Metal, tinygrad) | ~33 | baseline |
| RTX 5060 Ti (eGPU) | 22.7 | 31% slower |
| RTX 5070 Ti (eGPU) | ~37 | 12% faster |
| RTX 5090 (eGPU) | ~35 | 6% faster |

External Blackwell GPUs match but don't significantly beat the M4 Pro on raw matmul — this measures tinygrad's compiler efficiency on both backends, not the GPUs themselves.

### LLM Inference (tinygrad benchmark)

| GPU | Model | tok/s |
|-----|-------|-------|
| RTX 5090 (eGPU) | Qwen3-8B | ~6.0 |
| RTX 5090 (eGPU) | Qwen3-30B MoE | ~6.5 |
| RTX 5090 (eGPU) | Llama 3.1-8B (INT8) | ~7.5 |
| RTX 5070 Ti (eGPU) | Qwen3-8B | ~5.5 |
| RTX 5060 Ti (eGPU) | Qwen3-8B | ~4.6 |
| M4 Pro (Metal, tinygrad) | Qwen3-8B | 3.66 |

### llama.cpp Reality Check

On Qwen3-4B Q4 via llama-bench:
- tinygrad on RTX 5090 (eGPU): 7.39 tok/s, TTFT ~5000ms
- llama.cpp on M4 Pro (Metal): ~74 tok/s, TTFT 651ms

The gap exists because llama.cpp has years of hand-tuned Metal kernels, fused dequant+matmul for every GGUF format, KV cache layouts tuned per architecture, and thousands of contributors.

## Setup

- USB4 dock for smaller GPUs (RTX 5060 Ti)
- Razer Core X V2 ($349, PSU sold separately) for larger cards (5070 Ti, 5090)
- tinygrad DEXT installed via curl command
- System extension approval required
- Docker Desktop for tinygrad's nvcc/ptxas path (NVIDIA stopped shipping CUDA toolkit for macOS)

## Conclusion

The eGPU approach is promising but the inference numbers need time to mature. The hard part (driver, memory manager, compiler pipeline) is done. What's left is the rest of the inference stack catching up.

## Sources

- [The eGPU Myth blog post](https://www.lucebox.com/blog/egpu-myth) — Lucebox, April 2026
- [Alex Ziskind's Blackwell testing](https://www.youtube.com/watch?v=C4KWsmezXm4) — YouTube
- [tinygrad](https://github.com/tinygrad/tinygrad) — deep learning framework with custom NVIDIA driver
- [llama-benchy](https://github.com/eugr/llama-benchy) — benchmarking tool
