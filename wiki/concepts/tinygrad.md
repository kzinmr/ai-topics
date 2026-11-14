---
title: "Tinygrad"
type: concept
aliases:
  - tinygrad
  - geohot/tinygrad
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - open-source
  - ai-infrastructure
  - gpu
  - python
sources:
  - https://github.com/tinygrad/tinygrad
  - https://tinygrad.org
  - entities/george-hotz
---

# Tinygrad

**tinygrad** is an minimalist open-source deep learning framework created by [[entities/george-hotz|George Hotz]] (geohot) and maintained by tiny corp. Its tagline — "You like pytorch? You like micrograd? You love tinygrad!" — states the lineage directly: it is the production-scale descendant of Hotz's ~100-line teaching engine [[concepts/micrograd]], built on the philosophy that a full tensor library does not need millions of lines of code. GitHub: ~34k stars, MIT license, Python, actively developed (verified 2026-11-15).

## Core Thesis

Hotz's argument is a software-engineering application of the [[concepts/rich-suttons-bitter-lesson]]: simple, comprehensible systems that leverage raw computation beat complex hand-optimized ones. tinygrad targets roughly ~15–30k lines of Python to cover what PyTorch + CUDA + cuDNN + build toolchains cover in millions, trading peak-vendor performance for total inspectability and portability.

## Architecture

```
Python frontend (Tensor API, ~PyTorch-compatible)
        │
   lazy compute graph (linearize / symbolic reshape+buffer fusion)
        │
   renderer → backend-specific codegen
        │
┌──────┬──────┬──────┬──────┬──────┬──────┐
│ CUDA │ METAL│  ROCm│  NVVM│  LLVM│  C   │ ... tiny Jit backends
└──────┴──────┴──────┴──────┴──────┴──────┘
```

- **Everything is one kernel when possible.** The lazy graph fuses reshape/buffer ops symbolically before codegen, so whole networks can lower to a single fused kernel — no XLA graph compiler required.
- **Backend as codegen target.** Backends are Python modules emitting CUDA C, Metal, OpenCL, LLVM IR, or plain C. Adding a hardware target does not require vendor library dependencies, which is why tinygrad runs on NVIDIA, AMD, Apple Silicon, Qualcomm Hexagon, and even CPU.
- **tinygrad is also a hardware discovery tool**: Hotz has used it to run models on exotic devices (e.g., Qualcomm NPUs, PS3-era hardware experiments), because the whole stack fits in one engineer's head.

## Notable Milestones

| Year | Milestone |
|------|-----------|
| 2020 | Initial release as a minimal PyTorch alternative |
| 2022 | tinygrad rewritten; "tiny corpus" era, LLaMA inference on Apple GPU |
| 2023 | tiny corp founded; Hotz's "GPU kernel" competition (vs NVIDIA/AMD vendor lock-in) |
| 2024 | [[concepts/nanogpt|nanoGPT]] speedrun era — Hotz's team (Geohot + the tinygrad crowd) set GPT-2 pretraining speed records, beating earlier PyTorch/Jax-based efforts and popularizing "speedrun" benchmark culture |
| 2025–26 | Continued LLM inference work; used in Hotz's writing on breaking CUDA lock-in ([[concepts/cuda-moat]]) |

## Positioning in the Framework Landscape

| Framework | LOC scale | Philosophy |
|-----------|----------|------------|
| PyTorch | millions | Research default, vendor kernels |
| JAX | large | Compiler-first (XLA) |
| [[concepts/micrograd|micrograd]] | ~100 | Pedagogy only |
| **tinygrad** | ~tens of thousands | Full stack, one-kernel fusion, any-hardware portability |

Related minimal-stack efforts: ggml/llama.cpp (C inference), [[concepts/nanogpt]] (the model side of the same culture).

## Relation to Hotz's Broader Work

- **comma.ai**: open-source ADAS trained end-to-end — the flagship real workload for tinygrad's training ambitions.
- **AI sovereignty**: Hotz repeatedly frames CUDA lock-in as the bottleneck for open AI ([[concepts/cuda-moat]]); tinygrad is the practical counter-argument — a framework whose entire lowering pipeline is auditable.

## Related Concepts

- [[concepts/micrograd]] — the ~100-line ancestor
- [[concepts/nanogpt]] — the model whose speedrun culture tinygrad joined
- [[concepts/cuda-moat]] — the vendor lock-in tinygrad attacks
- [[entities/george-hotz]] — creator
- [[concepts/open-source-ai]] — the ecosystem argument tinygrad serves

## Sources

- [github.com/tinygrad/tinygrad](https://github.com/tinygrad/tinygrad) — star count/license verified via GitHub API 2026-11-15
- [tinygrad.org](https://tinygrad.org) — docs
- [[entities/geohot-github-io]] — Hotz's blog entity page (tinygrad thesis posts)
