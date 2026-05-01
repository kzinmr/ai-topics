---
title: "Lucebox"
type: project
status: complete
created: 2026-04-23
updated: 2026-04-23
tags:
  - local-llm
  - gpu-inference
  - cuda
  - speculative-decoding
  - hardware
sources:
  - https://www.lucebox.com
  - https://github.com/Luce-Org/lucebox-hub
  - https://www.lucebox.com/blog
related:
  - sandro-puppo.md
  - davide-ciffa.md
  - megakernel.md
  - dflash.md
---

# Lucebox

A personal computer built for local AI agents. Open-source project focused on maximizing inference throughput on consumer hardware through custom CUDA kernel optimization.

## Mission

"Plug-and-play local inference. Open source, built for throughput."

## Key Projects

### DFlash on ggml
Standalone C++/ggml speculative decoder for Qwen3.5-27B Q4_K_M with DFlash block-diffusion draft + DDtree verifier.
- **207 tok/s** peak on single RTX 3090 (5.46x over AR baseline)
- 3.43x speedup over autoregressive, 2.8x over SGLang AWQ reference
- 128K context on 24GB VRAM
- Only ~2000 LOC of C++/CUDA, no libllama dependency
- Published: April 2026

### Megakernel
First megakernel for hybrid DeltaNet/Attention LLMs.
- Fused all 24 layers of Qwen 3.5-0.8B into single CUDA dispatch
- **1.8x throughput** vs Apple M5 Max (411 vs 229 tok/s) on RTX 3090
- **1.87 tok/J** efficiency matching M5 Max at 220W power limit
- 3.4x faster prefill, 1.55x faster decode vs llama.cpp
- Published: April 2026

### eGPU Research
Comprehensive benchmarking of NVIDIA eGPUs on macOS.
- Profiled RTX 3090, 5060 Ti, 5070 Ti, 5090 over Thunderbolt/USB4
- Identified software stack as bottleneck, not cable bandwidth
- tinygrad DEXT driver enables NVIDIA compute on macOS for first time since 2019
- Published: April 2026

## Team

- **Sandro Puppo** (@pupposandro) — Co-founder, ex-Notion, YC X25
- **Davide Ciffa** (@davideciffa) — Co-founder, CUDA/kernel engineer

## Technology

Lucebox publishes deep technical blog posts covering:
- Custom CUDA kernel development for LLM inference
- Speculative decoding algorithms (DFlash, DDTree)
- Hardware profiling and benchmarking
- Open-source inference stack optimization

## Links

- Website: [lucebox.com](https://www.lucebox.com)
- Blog: [lucebox.com/blog](https://www.lucebox.com/blog)
- GitHub: [github.com/Luce-Org/lucebox-hub](https://github.com/Luce-Org/lucebox-hub) (541+ stars)
- X: [@pupposandro](https://x.com/pupposandro)

## See Also

- [[sandro-puppo]] — Co-founder of Lucebox, expert in speculative decoding and CUDA optimization.
- [[trycua-cua]] — Computer-use agent framework by the same team as Lucebox.
- [[davide-ciffa]] — Co-founder and CUDA/kernel engineer at Lucebox.
- [[speculative-decoding]] — DFlash block-diffusion draft technique developed by Lucebox.
- [[gpu-inference]] — Local LLM inference optimization on consumer hardware.
