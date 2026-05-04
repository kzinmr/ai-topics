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
  - observability
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
  - "[[concepts/pytorch-fsdp-distributed-training]]"
  - "[[concepts/local-llm/inference-hardware]]"
---

# AI Infrastructure Engineering

> LLM/AIを本番運用するためのハードウェア・インフラ技術の総合マップ。GPUから分散学習、モデルサーバー、オブザーバビリティまでをカバーする。

## Scope

このカテゴリは以下の領域を統合的に扱う:

| レイヤー | トピック | カバレッジ |
|----------|----------|-----------|
| **Hardware** | GPU/VRAM fundamentals, Memory Bandwidth, HBM | [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] ⬜ L1 |
| **Quantization** | FP4/FP8/INT4/INT8, AWQ/GPTQ/GGUF | [[concepts/model-quantization]] ⬜ stub |
| **Inference Engines** | vLLM, TensorRT-LLM, SGLang, llama.cpp | [[concepts/inference/_index]] ✅ LIVE |
| **Inference Optimization** | KV Cache, Speculative Decoding, Continuous Batching | [[concepts/kv-cache]], [[concepts/speculative-decoding]] ✅ LIVE |
| **Distributed Training** | DDP, FSDP, DeepSpeed, 3D Parallelism | [[concepts/ai-infrastructure-engineering/distributed-training]] ⬜ L1 |
| **Model Serving** | Autoscaling, Load Balancing, Prefix Caching | [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] ⬜ L1 |
| **Cost Optimization** | Prompt Caching, Batch Orchestration, Token Economics | [[concepts/prompt-caching]] ✅ LIVE |
| **Observability** | Traces, Metrics, Logs, Evals | [[concepts/ai-infrastructure-engineering/llm-observability]] ⬜ L1 |
| **Memory Debugging** | PyTorch Memory Snapshot, Memory Profiler, OOM Debugging | [[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]] 🟢 L1 |
| **Research Frameworks** | Hardware Lottery, Path Dependency, Infrastructure Decision Theory | [[concepts/ai-infrastructure-engineering/hardware-lottery]] 🟢 L2 |

## 学習ロードマップ

目的別におすすめの学習経路:

### 🏗️ Model Serving Engineer (APIプロダクション向け)
1. [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUキャパシティ理解の必須基礎
2. [[concepts/inference/_index]] — エンジン比較と選定基準
3. [[concepts/kv-cache]] — メモリ律速の根本原因
4. [[concepts/serving-llms-vllm]] — vLLM実践
5. [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — 本番スケーリング
6. [[concepts/ai-infrastructure-engineering/llm-observability]] — 監視・運用

### 🚀 Training Infra Engineer (学習パイプライン向け)
1. [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUメモリ階層
2. [[concepts/ai-infrastructure-engineering/distributed-training]] — DDP → FSDP → DeepSpeed
3. [[concepts/model-quantization]] — 量子化の基礎（FP8学習対応）
4. [[concepts/llm-inference]] — 推論最適化の基礎理論

### 💰 Cost Optimization (APIコスト削減)
1. [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — VRAMとコストの関係
2. [[concepts/prompt-caching]] — キャッシュ戦略
3. [[concepts/speculative-decoding]] — 投機的デコードでのスループット向上
4. [[concepts/inference/vllm]]#TurboQuant — KV Cache量子化による効率化

## Key Entities

- [[entities/reiner-pope]] — MatX CEO, roofline analysis framework
- [[entities/matx]] — AI chip startup
- [[entities/daniel-han]] — Unsloth/Hugging Face, fine-tuning optimization
- [[entities/arize]] — AI observability platform
- [[entities/elvis-sun]] — Local AI deployment & hardware analysis

## Existing Infrastructure Pages (参照)

| ページ | 状態 | 内容 |
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
| [[concepts/pytorch-fsdp-distributed-training]] | 🔴 Stub | Needs enrichment |
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
