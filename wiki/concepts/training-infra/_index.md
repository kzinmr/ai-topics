---
title: "AI Infrastructure Engineering"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - infrastructure
  - inference
  - training
status: L1
aliases:
  - ai-infra
  - ai-infrastructure
  - llm-infrastructure
  - ml-infrastructure
sources: []
related:
  - "[[concepts/llm-inference]]"
  - "[[concepts/inference/_index]]"
  - "[[concepts/serving-llms-vllm]]"
  - "[[concepts/kv-cache]]"
  - "[[concepts/speculative-decoding]]"
  - "[[concepts/model-quantization]]"
  - "[[concepts/prompt-caching]]"
  - "[[concepts/ai-observability]]"
  - "[[concepts/post-training/pytorch-fsdp-distributed-training]]"
  - "[[concepts/local-llm/inference-hardware]]"
---

# AI Infrastructure Engineering

> A comprehensive map of hardware and infrastructure technologies for production-grade LLM/AI operation. Covers everything from GPU to distributed training, model servers, and observability.

## Scope

This category covers the following areas comprehensively:

| Layer | Topic | Coverage |
|----------|----------|-----------|
| **Hardware** | GPU/VRAM fundamentals, Memory Bandwidth, HBM | [[concepts/training-infra/gpu-vram-fundamentals]] ⬜ L1 |
| **Quantization** | FP4/FP8/INT4/INT8, AWQ/GPTQ/GGUF | [[concepts/model-quantization]] ⬜ stub |
| **Inference Engines** | vLLM, TensorRT-LLM, SGLang, llama.cpp | [[concepts/inference/_index]] ✅ LIVE |
| **Inference Optimization** | KV Cache, Speculative Decoding, Continuous Batching | [[concepts/kv-cache]], [[concepts/speculative-decoding]] ✅ LIVE |
| **Distributed Training** | DDP, FSDP, DeepSpeed, 3D Parallelism | [[concepts/training-infra/distributed-training]] ⬜ L1 |
| **Model Serving** | Autoscaling, Load Balancing, Prefix Caching | [[concepts/training-infra/model-serving-autoscaling]] ⬜ L1 |
| **Cost Optimization** | Prompt Caching, Batch Orchestration, Token Economics | [[concepts/prompt-caching]] ✅ LIVE |
| **Observability** | Traces, Metrics, Logs, Evals | [[concepts/training-infra/llm-observability]] ⬜ L1 |
| **Memory Debugging** | PyTorch Memory Snapshot, Memory Profiler, OOM Debugging | [[concepts/training-infra/pytorch-gpu-memory-profiling]] 🟢 L1 |
| **Research Frameworks** | Hardware Lottery, Path Dependency, Infrastructure Decision Theory | [[concepts/training-infra/hardware-lottery]] 🟢 L2 |

## Learning Roadmap

Recommended learning paths by goal:

### 🏗️ Model Serving Engineer (For API Production)
1. [[concepts/training-infra/gpu-vram-fundamentals]] — Essential foundation for understanding GPU capacity
2. [[concepts/inference/_index]] — Engine comparison and selection criteria
3. [[concepts/kv-cache]] — Root cause of memory bottlenecks
4. [[concepts/serving-llms-vllm]] — vLLM in practice
5. [[concepts/training-infra/model-serving-autoscaling]] — Production scaling
6. [[concepts/training-infra/llm-observability]] — Monitoring and operations

### 🚀 Training Infra Engineer (For Training Pipelines)
1. [[concepts/training-infra/gpu-vram-fundamentals]] — GPU memory hierarchy
2. [[concepts/training-infra/distributed-training]] — DDP → FSDP → DeepSpeed
3. [[concepts/model-quantization]] — Quantization fundamentals (FP8 training support)
4. [[concepts/llm-inference]] — Fundamental theory of inference optimization

### 💰 Cost Optimization (API Cost Reduction)
1. [[concepts/training-infra/gpu-vram-fundamentals]] — Relationship between VRAM and cost
2. [[concepts/prompt-caching]] — Caching strategies
3. [[concepts/speculative-decoding]] — Throughput improvement with speculative decoding
4. [[concepts/inference/vllm]]#TurboQuant — Efficiency via KV Cache quantization

## Key Entities

- [[entities/reiner-pope]] — MatX CEO, roofline analysis framework
- [[entities/matx]] — AI chip startup
- [[entities/daniel-han]] — Unsloth/Hugging Face, fine-tuning optimization
- [[entities/arize]] — AI observability platform
- [[entities/elvis-sun]] — Local AI deployment & hardware analysis

## Existing Infrastructure Pages (Reference)

| Page | Status | Content |
|--------|------|------|
| [[concepts/llm-inference]] | 🟢 L2 | Roofline analysis, batch size economics, KV bandwidth |
| [[concepts/inference/_index]] | 🟢 Index | Engine comparison: vLLM / SGLang / llama.cpp |
| [[concepts/inference/vllm]] | 🟢 LIVE | PagedAttention, TurboQuant, continuous batching |
| [[concepts/inference/sglang]] | 🟢 LIVE | RadixAttention, structured generation |
| [[concepts/serving-llms-vllm]] | 🟢 LIVE | vLLM production serving patterns |
| [[concepts/kv-cache]] | 🟢 LIVE | KV Cache fundamentals |
| [[concepts/kv-cache-compaction]] | 🟢 LIVE | Attention matching, latent briefing |
| [[concepts/speculative-decoding]] | 🟢 LIVE | Draft-verify, Medusa, Eagle |
| [[concepts/prompt-caching]] | 🟢 LIVE | Static/semantic/partial caching strategies |
| [[concepts/ai-observability]] | 🟢 LIVE | LLM-specific observability dimensions |
| [[concepts/model-quantization]] | 🔴 Stub | Needs enrichment |
| [[concepts/post-training/pytorch-fsdp-distributed-training]] | 🔴 Stub | Needs enrichment |
| [[concepts/tensorrt-llm]] | ⬜ New | NVIDIA inference optimization |
| [[concepts/local-llm/inference-hardware]] | 🟢 LIVE | Consumer GPU VRAM requirements |

## Skills Reference

- `gguf-quantization` — GGUF format, quantization methods
- `serving-llms-vllm` — vLLM serving setup
- `evaluating-llms-harness` — lm-eval-harness benchmarking
- `llama-cpp` — Local GGUF inference

## TODO

- [ ] GPU VRAM fundamentals: Add NVIDIA GPU architecture table (H100/B100/Rubin)
- [ ] Distributed Training: Add DeepSpeed ZeRO stages comparison
- [ ] Model Serving: Add autoscaling config patterns (K8s HPA, Ray Serve)
- [ ] Observability: Add LLM-specific metrics (TTFT, TPOT, ITL)
- [ ] Enrich `tensorrt-llm.md` with benchmark comparisons
- [ ] Create cost optimization calculator reference
- [ ] Add entity pages for key infra providers
