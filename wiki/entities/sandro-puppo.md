---
title: "Sandro Puppo"
type: person
status: complete
created: 2026-04-23
updated: 2026-04-23
tags:
  - ai
  - local-llm
  - inference
  - speculative-decoding
  - company
sources:
  - https://x.com/pupposandro
  - https://www.lucebox.com
  - https://github.com/Luce-Org/lucebox-hub
related:
  - davide-ciffa.md
  - lucebox.md
  - trycua-cua.md
  - dflash.md
  - megakernel.md
---

# Sandro Puppo (@pupposandro)

Co-founder of Cua (YC X25) and Lucebox. Focus on local LLM inference optimization and computer-use agent infrastructure.

## Background

- Co-founder of **Cua** (trycua) — Y Combinator X25 batch. Open-source framework for computer-use agents that enables AI agents to control full operating systems within lightweight virtual containers. 13.3k+ GitHub stars.
- Co-founder of **Lucebox** — building personal computers for local AI agents with custom CUDA kernel optimizations.
- Former team member at **Notion**.
- Collaborates closely with **Davide Ciffa** (@davideciffa) on inference optimization research.

## Key Contributions

### Speculative Decoding (DFlash)
- Built standalone C++/ggml speculative decoder for Qwen3.5-27B achieving **207 tok/s** on single RTX 3090 (5.46x over autoregressive baseline).
- DDTree verification approach achieving 3.43x speedup over AR and 2.8x over SGLang AWQ reference.
- Demonstrated that consumer GPUs can outperform Apple Silicon for large model inference through software-level optimization.

### Megakernel Optimization
- First megakernel for hybrid DeltaNet/Attention LLMs (Qwen 3.5-0.8B).
- Fused all 24 layers into single CUDA dispatch, achieving 1.87 tok/J efficiency — matching M5 Max at 2x throughput on a 2020 RTX 3090.
- Power sweep experiments showing optimal efficiency at 220W (95% speed, 30% less power).

### eGPU Research
- Comprehensive benchmarking of NVIDIA eGPUs on macOS via Thunderbolt/USB4.
- Profiled tinygrad's NVIDIA driver (DEXT) across RTX 3090, 5060 Ti, 5070 Ti, and 5090.
- Identified that inference bottlenecks are software stack maturity, not cable bandwidth — GPUs using only 1.2-1.6% of their own memory bandwidth.

## Philosophy

Advocates for software-level GPU optimization over hardware upgrades. Key insight: "The engineering is beautiful. The numbers need time." — referring to early-stage driver and kernel development for consumer GPU inference.

## Links

- X: [@pupposandro](https://x.com/pupposandro)
- Lucebox: [lucebox.com](https://www.lucebox.com)
- Cua: [cua.ai](https://cua.ai), [GitHub](https://github.com/trycua/cua)
- Lucebox Hub: [github.com/Luce-Org/lucebox-hub](https://github.com/Luce-Org/lucebox-hub)

## See Also

- [[lucebox]] — Personal computer for local AI agents, co-founded by Sandro Puppo.
- [[trycua-cua]] — Open-source framework for computer-use agents, co-founded by Sandro Puppo.
- [[davide-ciffa]] — Co-founder and CUDA/kernel engineer at Lucebox and Cua.
- [[speculative-decoding]] — Inference optimization technique pioneered by Puppo's DFlash work.
- [[gpu-inference]] — Local LLM inference on consumer GPUs.
