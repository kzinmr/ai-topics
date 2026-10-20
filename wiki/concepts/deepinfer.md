---
title: "DeepInfer (DeepSeek Inference Engine)"
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [inference, inference-engine, vllm, sglang, disaggregation, kv-cache, speculative-decoding, mixture-of-experts, structured-outputs, open-source, deepseek, model-optimization]
sources:
  - raw/articles/2026-10-20_deepseek-deepinfer-open-source-inference-engine.md
related:
  - concepts/vllm
  - concepts/inference/sglang
  - concepts/kv-cache
  - entities/deepseek
confidence: high
---

# DeepInfer (DeepSeek Inference Engine)

**DeepInfer** is DeepSeek's high-performance inference framework that powers DeepSeek's large-scale production services. On **2026-10-20** DeepSeek open-sourced a subset of it under the Apache 2.0 license at [`github.com/deepseek-ai/DeepInfer`](https://github.com/deepseek-ai/DeepInfer). It became one of the top HN stories of the day (300+ points), positioned explicitly as "DeepSeek just open-sourced its inference engine."

## What it is

A production-grade, offline inference engine for serving DeepSeek models at scale. Notably, it was "originally built primarily on **vLLM**, with additional inspiration from **SGLang** and **TensorRT-LLM**" — making it DeepSeek's fork-derived, kernel-optimized successor to the mainstream open serving stacks.

- **Supported model:** DeepSeek-V4.1-Flash (default checkpoint `deepseek-ai/DeepSeek-V4.1-Flash-1017`)
- **Supported hardware:** NVIDIA SM100 GPUs, Huawei Ascend 950 NPUs
- **License:** Apache 2.0

## Key features

- **Optimized kernels:** builds on DeepSeek's kernel family — [FlashMLA](https://github.com/deepseek-ai/FlashMLA), [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), [DeepEP](https://github.com/deepseek-ai/DeepEP), [TileKernels](https://github.com/deepseek-ai/TileKernels), [DeepSelect](https://github.com/deepseek-ai/DeepSelect), plus custom TileLang kernels.
- **Parallelism:** Attention Data-Parallelism / balanced Context-Parallelism, MoE Expert-Parallelism + EPLB (Expert Placement Load Balancing).
- **DSpark + confidence-scheduled verification:** speculative decoding with draft tokens; confidence estimates schedule verification (`DEEPINFER_ENABLE_MTP_VARLEN=1`, `DEEPINFER_USE_NEXTN_DECODE` for max draft length, default 5).
- **SWA bounded replay:** reduces decoder prefill work by replaying only a bounded suffix of sliding-window-attention tokens (`...PREFILL_TRUNCATION_MODE=compact`, `KEEP_TOKENS=140` for V4.1).
- **Asynchronous scheduling:** overlaps CPU batch scheduling with device execution ("zero-overhead batch scheduler"), enabled by default.
- **Batch-invariant inference** and **deterministic sampling** (NVIDIA only) for reproducible outputs.
- **Structured outputs:** constrain generation to regex, JSON schema, or EBNF grammar.

## What the open release does NOT include

The public release is explicitly a partial slice of the production system. Still required for a complete online service:

- A KV cache system
- VE / Prefill / Decode **disaggregation** (most required engine functionality is already implemented)
- Load balancing across data-parallel replicas for both prefill and decode

This mirrors DeepSeek's incremental open-sourcing pattern (FlashMLA, DeepGEMM, DeepEP were each released as standalone components earlier).

## Significance

DeepInfer signals DeepSeek entering the "open inference engine" race directly against vLLM and SGLang — the very projects it was forked from — but with DeepSeek's own MoE-aware kernels and Ascend NPU support. The Ascend 950 support is strategically notable: it's a first-party inference path for Huawei hardware, relevant to China's domestic accelerator push and to US export-control dynamics.

## Related

- [[concepts/vllm]] — the base project DeepInfer was built on
- [[concepts/inference/sglang]] — one of DeepInfer's cited inspirations
- [[concepts/kv-cache]] — KV cache management, a component NOT in the public release
- [[entities/deepseek]] — the lab behind DeepInfer
- [[concepts/speculative-decoding]] — the DSpark draft/verify mechanism
- [[concepts/mixture-of-experts]] — MoE EP + EPLB parallelism
