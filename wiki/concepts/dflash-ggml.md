---
title: "DFlash on ggml"
type: concept
status: draft
created: 2026-04-23
updated: 2026-04-23
tags:
  - speculative-decoding
  - local-llm
  - inference
  - ggml
  - optimization
sources:
  - https://www.lucebox.com/blog/dflash27b
related:
  - lucebox.md
  - sandro-puppo.md
  - davide-ciffa.md
  - llama-cpp.md
  - sglang.md
---

# DFlash on ggml

DFlash (DeltaFlash) speculative decoding implementation ported to the ggml library, enabling high-throughput inference for hybrid DeltaNet/Attention models on consumer GPUs.

## Overview

A standalone C++/ggml speculative decoder for Qwen3.5-27B Q4_K_M with DFlash block-diffusion draft and DDTree verifier, built by Lucebox.

## Key Results

| Metric | Value |
|--------|-------|
| Peak throughput | 207 tok/s (5.46x over AR) |
| Mean throughput (HumanEval) | 129.5 tok/s at DDTree budget=22 |
| Speedup vs AR | 3.43x |
| Speedup vs SGLang AWQ | 2.8x |
| Context length | 128K on 24GB VRAM |
| Code size | ~2000 LOC C++/CUDA |

## Architecture

The library targets one model pair:
- **Target**: Qwen3.5-27B-Q4_K_M.gguf (~16 GB)
- **Draft**: z-lab/Qwen3.5-27B-DFlash (3.46 GB bf16)

Key design decisions:
- Links only `libggml*.a`, never `libllama`
- Greedy verification with block size 16
- CUDA-only implementation
- Q4_0 KV cache compression for long context support
- Rolling 4096-slot target feature buffer

## DDTree Configuration

| Mode | Mean AL | Mean tok/s | Max tok/s | Speedup |
|------|---------|------------|-----------|---------|
| Autoregressive | 1.00 | 37.78 | 45 | 1.00x |
| Chain DFlash | 7.67 | 112.82 | 150.06 | 3.01x |
| DDTree budget=22 (f16) | 8.31 | 129.52 | 158.40 | 3.43x / 4.20x peak |

## Why It Matters

Qwen3.5-27B is a hybrid model: every 4th layer is full softmax attention, the rest (48 of 64) are Gated DeltaNet. This combination previously had no efficient single-24GB-GPU decode path:
- llama.cpp had GGUF loader but no DFlash speculative decoding
- vLLM/SGLang only supported BF16 weights (54GB, doesn't fit on 24GB)
- No GGUF path for Qwen3.5-27B on either runtime

DFlash on ggml bridges this gap, enabling high-throughput inference on consumer hardware.

## Sources

- [DFlash on ggml blog post](https://www.lucebox.com/blog/dflash27b) — Lucebox, April 2026
- [z-lab DFlash reference](https://github.com/z-lab) — original DFlash implementation
- [Qwen3.5-27B model](https://huggingface.co/Qwen/Qwen3.5-27B) — hybrid DeltaNet/Attention architecture
