---
title: "Needle2 — 14MB Agentic LLM for Edge Devices"
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [local-llm, ai-agents, edge-computing, open-source]
sources: [raw/articles/2026-08-10_needle2-agentic-llm.md]
---

## Overview

Needle 2 is an open-source, 14MB agentic large language model (LLM) developed by **Cactus Compute**, purpose-built for tool calling, device use, and structured extraction on tiny edge devices. With only 45 million parameters, the entire model ships as a single binary that runs a full session in just 28MB of RAM — making it viable for microcontrollers, budget phones, wearables, smart home hubs, and small robots.

Licensed under Apache 2.0, weights are available on Hugging Face, and the model runs across architectures from Cortex-M to x86 and WebAssembly via a single dependency-free C++ engine.

## Architecture

Needle 2 is built on the **Simple Attention Network (SAN)**, a novel architecture that achieves competitive tool-calling performance at a fraction of the parameter count and compute budget of conventional transformers.

### Key Architectural Innovations

- **Hadamard MLP**: Replaces dense up-and-down projections with a fixed Walsh-Hadamard transform and learned diagonals, making channel mixing nearly parameter-free.
- **Engram (hashed n-gram tables)**: Moves world knowledge out of the transformer stack into gathered memory — 8M of the 45M parameters are engram entries read by gather, costing no arithmetic at decode time.
- **Multi-lane residual streams**: A 27-layer, 512-wide network with four residual streams per block gives routing flexibility comparable to a much wider model.
- **256-token sliding window attention**: KV cache is bounded deterministically at 28MB regardless of session length. System prompts and tool declarations are pinned as permanent sinks so tools can never be evicted.
- **Byte-level grammar compiler**: Enforces structured output by constraining every token against declared schemas. This is an optimization as well as a guarantee — up to 98% of vocabulary projection is skipped on structural tokens.
- **Cactus Quants (CQ2-bit)**: Quantization-aware training from pretrain through post-train — weights, activations, and KV cache all trained at ~2 bits. The deployed model is the trained model; nothing is post-hoc quantized.

### Compute Efficiency

| Model | Params | Matmul-active | MFLOPs/token |
|-------|--------|---------------|-------------|
| Needle 2 (CQ2-bit) | 45M | 35M | 70 |
| Same-shape transformer, dense MLP | 82M | 82M | 164 |
| LFM2.5 (f16) | 230M | 230M | 460 |
| FunctionGemma (f16) | 270M | 270M | 540 |
| Apple FM (on-device) | ~3B | ~3B | ~6,000 |

Needle 2 spends 7× to 85× fewer MFLOPs per token than competing models.

## Inference Engine

The engine is a single dependency-free C++ binary that probes the CPU at startup and self-selects its kernel tier: SDOT, NEON, AVX2, RISC-V vectors, wasm SIMD, or scalar fallback. Weights never decompress into RAM — 2-bit codes expand inside vector registers and fuse into integer dot products, keeping resident memory at blob size (14MB). The engine ships as a static library for bare-metal Cortex-M4, M7, and M55 targets.

## Supported Platforms

| Platform | Performance |
|----------|------------|
| Raspberry Pi 5 | 500+ tok/s decode, 800+ tok/s prefill |
| Meta Quest 3S / Apple Vision Pro | 400–1,500 tok/s |
| Sub-$200 phones (e.g., Samsung A-Series) | 300–700 tok/s |
| ESP32-S3 / ESP32-P4 (32MB PSRAM) | Viable (28MB RAM ceiling) |
| STM32H7 / NXP i.MX RT + SDRAM | Viable |
| WebAssembly (browser playground) | Interactive |

## Use Cases

- **Smart Home**: Multi-step device control — lights, thermostats, locks — with typed function schemas and multi-turn reasoning.
- **Wearables**: Voice-to-action on ring/band devices without network dependency (deployed by **Pebble** in the Index 01 app).
- **Robots**: Chained movement commands and sensor-driven actions on small robots like Reachy Mini.
- **Phones**: Always-on assistant within tight power budgets; no GPU or NPU required.
- **Automotive**: In-vehicle voice control for navigation, climate, and entertainment.
- **Structured Extraction**: Schema-defined field extraction from documents, sentiment classification, and live API data marshaling.

## Comparison to Other Tiny/Edge LLMs

Needle 2 trades wins with much larger models on public function-calling benchmarks while being 5× to 70× smaller and running at 2-bit precision against their float16.

### Benchmark Highlights (Ordered Strict Exact Match)

**Mobile Actions** (961 rows):
- LFM2.5 230M: 69.1%
- FunctionGemma 270M: 64.0%
- Needle 2 (CQ2-bit): 63.7%
- Apple FM (on-device): 57.6%

**Seal-Tools in-domain** (700 rows):
- Needle 2: 32.6% (64.9% on single-call)
- LFM2.5 230M: 26.9%
- FunctionGemma 270M: 16.3%

**Seal-Tools out-of-domain** (654 rows, tool domains held out):
- Needle 2: 28.7%
- LFM2.5 230M: 17.0%
- FunctionGemma 270M: 15.6%

Needle 2 is trained specifically for consumer device actions (smart home, mobile, wearables, TV, automotive) plus structured extraction — it does not aim to be a general-purpose chat model. When a request is out of distribution, the model returns an empty call (refusal) with a learned confidence score, enabling edge-cloud collaboration where routine actions stay local and complex queries escalate.

## Edge-Cloud Collaboration

Every response carries a learned confidence score. Above the threshold, the model acts locally. Below it, the request is re-asked or escalated to the cloud. Since most device requests are routine control, escalation stays rare, keeping the default path private, instant, and free of network dependency.

## Fine-Tuning

A 45M-parameter model is small enough to fine-tune on a personal computer in minutes to hours. Cactus Compute provides a Python package and repo that lets device makers train Needle on their own tool vocabularies.

## Related Pages

- [[edge-llm-microcontroller]] — LLMs on microcontroller-class hardware
- [[small-language-models]] — The broader category of sub-1B parameter models
- [[ai-agents]] — Agentic AI systems and autonomous tool use
- [[edge-ai]] — AI deployment on edge devices
- [[programmatic-tool-calling]] — Structured function calling patterns
- [[structured-outputs]] — Schema-constrained model outputs
- [[local-llm/model-quantization]] — Quantization techniques for local LLMs
- [[webassembly]] — WASM as a deployment target (Needle playground runs in-browser via WASM)
