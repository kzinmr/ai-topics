---
title: "Resin — Library of Building Blocks for LLM Inference"
type: concept
created: 2026-11-05
updated: 2026-11-05
tags: [inference-engine, kv-cache, llm-inference, rust]
aliases:
  - resin
  - resin-inference
description: "ekzhang/Resin — an experimental, non-production library of building blocks for building LLM inference engines: a headless Rust Engine (scheduler + KV cache + metrics) paired with model-specific forward-pass kernels you write for your own hardware, plus tiered prefix-cache storage over CPU DRAM, SSD, etc."
sources:
  - "https://github.com/ekzhang/resin"
---

# Resin — Library of Building Blocks for LLM Inference

**Resin** ([ekzhang/resin](https://github.com/ekzhang/resin)) is an *experimental* library by **Eric Zhang** ([@ekzhang1](https://x.com/ekzhang1), Thinking Machines Lab). It is deliberately **not** an inference engine — it is a library of **building blocks** for *building* inference engines. The tagline framing: use SGLang or vLLM for production; use Resin to hack on LLM inference systems, new models, or new hardware.

## Architecture

At the core is a **headless `Engine`**:

```
token IDs ──► Rust Engine ──► frozen BatchPlan ──► Python Runner ──► token IDs
                  ▲                                    │
                  └──────── ownership & commit ────────┘
```

- **Rust Engine** — a fast scheduler, KV cache, and metrics server. Owns orchestration and batching.
- **Python Runner** — you write the forward pass as **model-specific kernels, optimized for your hardware**. The "model" side is yours; the "systems" side is Resin's.
- Optional HTTP serving and Prometheus metrics.

The pitch is composability-as-code: "it's just code," so exotic pieces (SSD tiers, Mooncake-style distributed KV, custom lookup/store/load paths) can be wired in through the same interfaces rather than being baked into a monolith.

## Tiered KV-cache storage

Resin's prefix-cache storage lets the engine reuse model state **after it has been evicted from GPU memory**. The Engine manages prefix matching and the lifetime of device pages; a **storage provider** keeps immutable checkpoints outside the device cache pool. It ships with a bounded **CPU DRAM provider**, and custom providers can implement other tiers (SSD, remote/distributed, etc.) behind the same interface (`MemoryCacheStorage(max_bytes=…)` passed to `Engine(prefix_cache=True, prefix_cache_storage=…)`). This expands effective KV/recurrent-state capacity beyond VRAM via async fetches.

## Notable result

Using Resin, Zhang's team "vibe-coded" standalone engines for **DeepSeek-V4.1-Flash** and **GLM-5.3-Flash** on Blackwell GPUs in ~12 hours, reporting throughput that **rivals vLLM and SGLang**. This is the concrete demonstration of the "just code" thesis: with the right kernels, a small team can assemble a competitive engine for a brand-new model/hardware combination fast.

## Why it matters

- **Inference engines as a programmable substrate.** Resin's bet is that the next wave of models/hardware will outpace monolithic engines, and that a *library* of well-factored blocks (Rust scheduler + pluggable kernels + tiered cache storage) lets practitioners keep up.
- **KV-cache beyond VRAM.** The tiered-storage design is the same problem space as LMCache/Mooncake/KTransformers-style KV offload, but framed as a first-class, pluggable interface inside a composable engine.
- **AI-assisted systems programming.** The 12-hour Blackwell engines are a data point for Zhang's broader thesis that AI accelerates the mechanical code while humans still own architecture — see [[entities/eric-zhang]] ("AI tools made coding a lot faster… they don't replace the need for systems understanding").

## Related

- [[entities/eric-zhang]] — author
- [[concepts/system-one-models]] — Zhang's related openjev-sglang work
- SGLang / vLLM — the production engines Resin contrasts against (see [[concepts/serving-llms-vllm]])
