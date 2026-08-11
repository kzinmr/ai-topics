---
title: "Cactus Compute"
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [local-llm, open-source]
sources: [raw/articles/2026-08-10_needle2-agentic-llm.md]
---

## Overview

**Cactus Compute** is the company behind Needle, an open-source family of tiny agentic LLMs purpose-built for tool calling and structured extraction on edge devices. Their flagship model, [[local-llm/needle2-agentic-edge-llm|Needle 2]], is a 45M-parameter model compressed to a 14MB binary that runs in 28MB of RAM — targeting phones, wearables, smart home devices, robots, and microcontrollers.

## Key Products

- **Needle 2** (August 2026): 45M parameters, CQ2-bit quantization, Apache 2.0 license, weights on Hugging Face
- **Cactus Quants**: Proprietary quantization-aware training methodology that bakes compression into the training process from pretrain through post-train, achieving effective 2-bit weights without post-hoc degradation
- **Needle Engine**: Single dependency-free C++ inference binary with auto-detecting CPU kernel selection (SDOT, NEON, AVX2, RISC-V vectors, wasm SIMD, scalar)

## Technology Philosophy

Cactus Compute's core bet is that device control and structured extraction do not need world knowledge or open-ended prose — they only need to map natural language onto typed function schemas. This framing allows 45M parameters to suffice where general-purpose chat models require billions.

The company builds co-designed model-and-engine pairs, benchmarking every architectural choice on target hardware before committing to it. The deliverable is always the pair: a model with its sealed inference engine, not standalone weights.

## Production Deployment

Pebble runs Needle locally in the Index 01 wearable app, converting spoken requests into device actions without cloud dependency. The model targets hardware under $200 — roughly four in five edge devices — with no GPU or NPU requirements.

## Related Pages

- [[local-llm/needle2-agentic-edge-llm]] — Needle 2 concept page
- [[edge-llm-microcontroller]] — LLMs on microcontroller hardware
- [[small-language-models]] — Small language model ecosystem
