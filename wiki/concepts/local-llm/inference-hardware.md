---
title: "Local LLM Inference Hardware"
type: concept
created: 2026-04-15
updated: 2026-04-15
status: skeleton
tags: [local-llm, hardware, gpu, consumer, edge]
aliases: [inference-hardware, consumer-gpu-llm]
related: [[local-llm]], [[compute-scaling-bottlenecks]], [[concepts/local-llm/server-dgx-spark.md]]
sources:
  - url: "https://github.com/ggerganov/llama.cpp"
    title: "llama.cpp — GPU Support"
---

# Local LLM Inference Hardware

Hardware options for running LLMs locally, from consumer GPUs to edge devices.

## TODO

- [ ] Consumer GPU landscape (NVIDIA RTX 40/50 series, AMD Radeon)
- [ ] Apple Silicon (M1/M2/M3/M4 — unified memory advantage)
- [ ] Edge devices (Jetson, Raspberry Pi)
- [ ] VRAM requirements by model size (7B, 13B, 30B, 70B at various quants)
- [ ] Memory bandwidth as the key bottleneck
- [ ] Multi-GPU setups
- [ ] Cloud GPU rental vs buy analysis

## Related wikilinks

- [[concepts/local-llm/server-dgx-spark.md]] — DGX Spark: compact enterprise-grade local AI server
- [[compute-scaling-bottlenecks]] — Compute scaling and hardware constraints
