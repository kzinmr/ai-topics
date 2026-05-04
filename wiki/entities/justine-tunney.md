---
title: "Justine Tunney"
type: entity
created: 2026-05-04
updated: 2026-05-04
tags:
  - entity
  - person
  - software-engineer
  - open-source
  - cpp
  - cpu-inference
  - llamafile
  - mozilla
aliases:
  - Justine Tunney
  - jart
  - justine.lol
sources:
  - https://justine.lol/
  - https://github.com/jart
  - https://justine.lol/matmul/
---

# Justine Tunney

**Justine Tunney** is a software engineer and open-source developer known for creating **llamafile**, leading the `llama.cpp` CPU performance work, and her contributions to the Cosmopolitan Libc project. She was previously at Mozilla (llamafile) and Google.

## Overview

Tunney is one of the most impactful engineers in the local LLM ecosystem. Her work on CPU-side optimization for LLM inference — particularly the 84 new matrix multiplication kernels for llamafile — demonstrated that CPUs can achieve competitive performance for prompt processing, challenging the assumption that GPUs are strictly necessary for LLM inference.

She is a prolific systems programmer with deep expertise in CPU architecture (ARM, x86, AVX), assembly optimization, and cross-platform binary distribution through Cosmopolitan Libc.

## Key Projects

| Project | Description |
|:--------|:------------|
| **llamafile** | Single-file executable LLM runner — bundles model weights + inference engine into one binary. Created at Mozilla. |
| **llama.cpp CPU kernels** | 84 matrix multiplication kernels achieving 30-500% speedup over standard llama.cpp on CPUs |
| **Cosmopolitan Libc** | A libc implementation that allows C/C++ programs to run on multiple OSes (Linux, Mac, Windows, FreeBSD) from a single executable |
| **tinyblas** | Custom BLAS implementation for llamafile with hand-tuned CPU matmul kernels |

## Key Technical Contributions

### CPU Matrix Multiplication (84 Kernels)

Tunney's work on `GGML_OP_MUL_MAT` (~95% of llama.cpp's processing time) is foundational to local LLM inference performance:

- **Architecture-specific tuning:** ARMv8.2, Intel Alderlake, AVX512 (Zen 4), Apple Silicon
- **Outer-loop unrolling:** Vectorized outer products sharing register loads across multiple FMA operations
- **Custom threading model:** Avoids OpenMP spinlock starvation via `BEGIN_KERNEL`/`END_KERNEL` macros
- **Efficiency core management:** Specifically avoids running on efficiency cores to prevent lockstep bottleneck

> "I believe by improving the core technology, we can give users the best possible llama.cpp experience... quantization could become the bigger bottleneck [than memory bandwidth]. That would mean less need to trade away knowledge for speed."

### Llamafile

Created a zero-dependency, single-file executable for running LLMs locally by bundling weights and `llama.cpp` into a Cosmopolitan Libc binary. Democratized local LLM access.

## Cross-References

- [[concepts/inference/llama-cpp]] — Contributed CPU matmul optimizations
- [[concepts/local-llm]] — Local LLM ecosystem

## Sources

- [justine.lol](https://justine.lol/)
- [GitHub: jart](https://github.com/jart)
- [LLaMA Goes Faster on CPUs](https://justine.lol/matmul/)
