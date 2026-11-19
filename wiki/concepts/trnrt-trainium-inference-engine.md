---
title: "TrnRT: Trainium Inference Engine"
created: 2026-11-19
updated: 2026-11-19
type: concept
tags:
  - inference-engine
  - aws
  - ai-hardware
  - open-source
  - kv-cache
  - inference
status: L3
confidence: medium
aliases: [TrnRT, Trainium inference engine, runanywhere trnrt]
sources:
  - raw/articles/2026-11-17_runanywhere.ai_trnrt-trainium-inference-engine.md
  - https://news.ycombinator.com/item?id=50533270
---

# TrnRT: Trainium Inference Engine

**TrnRT** is an open-source LLM inference engine for **AWS Trainium2**, built by RunanywhereAI. It serves an OpenAI-compatible API from a single `trn2.48xlarge` instance, runs decode as **NKI (Neuron Kernel Interface) megakernels** — roughly one fused kernel per layer-half — and keeps a prefix cache spanning both device and host memory. First supported model is **GLM-5.3-Flash** (320B MoE / 18B active, FP8, 1M-token context), with more open models planned. Posted to Hacker News 2026-11-17 (54 points, deferred from the 2026-11-18 crawl for traction check).

## Why it matters

AWS Trainium has historically been underserved on the software side: training is well supported via Neuron, but **competitive open serving engines (vLLM/SGLang-class) have been largely absent**. TrnRT is an early answer to "can non-NVIDIA silicon serve agentic workloads economically?", which is central to the [[concepts/inference-hardware|custom-AI-silicon]] and [[concepts/cuda-moat|CUDA-moat]] debates.

## Architecture highlights

| Feature | What it does |
|---|---|
| **NKI megakernels** | One fused kernel per layer half for decode: KDA attention, fused DSA layer, mHC, and the MoE FFN — collapsing kernel-boundary overhead. |
| **1M-token context** | Sparse attention (top-2,048) + linear attention with fixed-size state. |
| **Prefix cache** | Radix tree over FP8 KV pages, plus a host-memory tier for evicted pages and state checkpoints ([[concepts/kv-cache|KV-cache]] tiering). |
| **Two engines per box** | Each engine tensor-parallel over 32 logical NeuronCores, behind a session-affine router (sticky `session_id` keeps a conversation on one engine's prefix cache). |
| **OpenAI API** | Chat + completions, streaming, tool calls, reasoning. |

The decode design philosophy is explicit: on Trainium, decode is **not** memory-bandwidth-bound — small instructions, kernel boundaries, and exposed collectives dominate. Hence the megakernel strategy: keep the working set in SBUF (the on-chip SRAM), use both physical cores symmetrically, and hide collectives inside the fused kernel.

## Benchmarks (vendor-reported)

Measured with SemiAnalysis **AgentX** (replays real coding-agent sessions) on one `trn2.48xlarge` at 1M context, 32 concurrent agents:

| Decode batch | Requests/min | Tokens/min | Decode tok/s/user (p50) | First-token cached (p50) | $/M tokens (spot) |
|---|---|---|---|---|---|
| 4 | 19.3 | 2.36M | 46.6 | 76.7s | $0.061 |
| 8 | 25.2 | 3.02M | 29.4 | 28.8s | $0.047 |
| 12 (default) | 28.9 | 3.57M | 22.3 | 6.5s | $0.040 |

Spot $8.60/h (us-east-2, Nov 3 2026); on a capacity block ($35.76/h) the batch-12 cost rises to ~$0.167/M tokens.

**Confidence caveat:** all performance and cost numbers are RunanywhereAI's own measurements against their chosen harness and pricing assumptions; not independently replicated. The repo's graph-equivalence checks (EQUAL on all 32 ranks / 157 graphs) and byte-identical-output checks (384/384) suggest correctness discipline, but the throughput/cost story still needs third-party confirmation.

## Related pages

- [[concepts/inference-hardware]] — Trainium in the accelerator-diversification story
- [[concepts/cuda-moat]] — the software-moat thesis TrnRT tests
- [[concepts/inference]] — engine landscape (vLLM/SGLang/TensorRT-LLM)
- [[concepts/kv-cache]] — prefix caching and KV tiering
