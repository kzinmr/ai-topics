---
title: Muse Glimmer
type: entity
created: 2026-08-10
updated: 2026-08-12
tags:
  - model
  - ai-agents
  - local-llm
  - on-device
  - open-source
  - meta
  - quantization
  - speculative-decoding
  - edge-ai
aliases:
  - Meta Muse Glimmer
  - Muse Glimmer 30B
sources:
  - raw/articles/2026-08-10_research-meta-ai_introducing-muse-glimmer.md
  - raw/newsletters/2026-08-11-meta-s-big-open-source-comeback.md
  - raw/articles/2026-08-12_fireworks-ai_meta-muse-glimmer.md
---

# Muse Glimmer

A 30-billion-parameter open agentic model from [[entities/meta|Meta Superintelligence Labs]], optimized for always-on local agent workflows on consumer hardware. Released August 10, 2026 under Apache 2.0 license.

## Overview

Muse Glimmer is designed to run locally on a Mac or PC with a single consumer GPU, enabling local agents, function calling, local coding, and LLM-as-a-judge evaluation. It is distilled from the larger [[entities/muse-spark|Muse Spark]] teacher model using a novel logit distillation recipe.

## Architecture & Training

30B parameter model trained in three phases:

1. **Pre-Training**: Logit distillation from Muse Spark outputs, leveraging a similar data mix as the teacher
2. **Mid-Training**: Longer-context, agent-heavy data with richer reasoning traces alongside organic data
3. **Post-Training**: SFT combined with on-policy distillation and reinforcement learning across general, reasoning, coding, and agentic domains

Evaluated under Meta's Advanced AI Scaling Framework for open-weight release.

## Agentic Capabilities

- **End-to-end task completion**: DeepSearch QA, MCP-Atlas, τ-Bench, SWE-Bench
- **Reliable tool use**: Precise function calling across extended workflows
- **Multi-step reasoning**: Sustained coherent plans across complex workflows
- **Failure recovery**: Diagnoses tool call errors and retries rather than halting
- **Multimodal input**: Dedicated perception encoder for interleaved text and images (screenshots, charts, documents)
- **Scaffold compatibility**: Works with OpenClaw and other orchestration patterns
- **Controllable effort**: Adjustable reasoning strength for quality/speed tradeoff
- **Multilingual**: Trained on 100+ languages

## Performance

Competes with Gemma4-31B and Qwen3.6-27B, performing strongly for its size class across agentic, coding, multimodal, safety, and reasoning benchmarks. Detailed evaluation methodology available at `/static/muse-glimmer-methodology`.

## Openness & Benchmarks (Aug 2026)

Coverage from [Superintel+ (2026-08-11)](https://getsuperintel.com) highlights Muse Glimmer's headline benchmark results, Meta's jump on the Artificial Analysis Openness Index, and the Apache 2.0 license shift.

### Benchmarks

| Benchmark | Muse Glimmer 30B | Comparison 1 | Comparison 2 |
|-----------|------------------|--------------|--------------|
| MCP Atlas | 75.5 | 54.2 | 62.5 |
| SWE-Bench Pro | 51.2 | 36.9 | 50.2 |

### Openness Index

Meta jumped from **5.0 to 8.0** on the [Artificial Analysis Openness Index](https://artificialanalysis.ai) with the Muse Glimmer release.

### Apache 2.0 License Transition

Muse Glimmer is downloadable today as a 30B model under **Apache 2.0**, running on a single consumer GPU when quantized under 20GB. The release marks a deliberate transition from Meta's previous **Llama Community License**, dropping:

- **700M MAU cap** — no monthly-active-user ceiling
- **"Built with Llama" attribution** — no mandatory branding requirement
- **EU feature exclusion** — feature parity restored for EU users

This makes Apache 2.0 Meta's most permissive license ever on its best local model.

## Architecture Details & Fireworks Serving (Aug 2026)

[Fireworks AI's launch post](https://fireworks.ai/blog/meta-muse-glimmer) (Aug 10, 2026) adds concrete architecture and serving specifics:

### Architecture Specs

- **30B dense model, 52 transformer layers**, grouped-query attention with **32 query heads and 2 KV heads**, SwiGLU feed-forward layers
- **~1.8B perception encoder** gives native image understanding alongside text
- **128K+ token context window**
- **Sliding-window attention over 2,048 tokens on most layers**, with a full global attention layer every fourth layer — paired with just 2 KV heads this keeps the KV cache small, the core reason long-context agent workloads are economical to serve at high concurrency
- Built to fit in 24GB (quantized); the same design makes serverless concurrency affordable
- Supports **DFlash speculative decoding** for lower-latency generation
- **Knowledge cutoff: January 4, 2026** — time-sensitive agent work needs tools

### Benchmark Table vs Size-Class Peers (all at high reasoning effort, per Meta)

| Benchmark | Muse Glimmer 30B | Gemma 4 31B (Thinking) | Qwen 3.6 27B (Thinking) |
|-----------|------------------|------------------------|-------------------------|
| MCP Atlas (Public) | 75.5 | 54.2 | 62.5 |
| DeepSearch QA | 74.6 | 61.7 | 71.1 |
| Gaia2 | 43.3 | 36.4 | 40.0 |
| WildClawBench | 47.6 | 37.6 | 43.2 |
| SWE-Bench Pro | 51.2 | 36.9 | 50.2 |

Also leads its class on **CharXiv Reasoning (78.8)** and **SciCode (43.6)**. Benchmark figures are Meta-reported.

### Reasoning-Effort & Sampling Controls

- Reasoning effort is set via system prompt: **`Reasoning strength: <value>`** with low/medium/high/xhigh — use high or xhigh for agentic and coding work
- Meta-recommended sampling: **temperature = 1.0, top_p = 0.95, top_k = 64**

### Fireworks Deployment

- Available on Fireworks in **serverless and on-demand** deployments
- Fireworks shipped **a day later than other providers deliberately** — correcting the model's shipped generation config and wiring reasoning-effort control end-to-end before launch
- Positioned for **bursty agent traffic**: autoscaling rather than peak provisioning, given agent workloads spike unpredictably
- Prototype against the quantized build on a workstation, deploy the same model on Fireworks to serve thousands of sessions — a symmetric path enabled by Apache 2.0

## Local Deployment

### Quantization

Full precision requires 55GB+ memory. Uses ~4-bit quantization to compress the LM to under 20GB, fitting within 24-32GB envelope with room for KV cache, perception encoder, and speculative decoding drafter. Minimal to no degradation on agentic tasks.

### Speculative Decoding (DFlash)

Ships with a lightweight drafter model based on [DFlash](https://arxiv.org/abs/2602.06036) — proposes entire token blocks that the main model verifies in parallel:

| Hardware | Speedup |
|----------|---------|
| RTX 5090 | 3.1x |
| M5 Max | 1.8x |
| M4 Max | 1.5x |

## Ecosystem

- **Local runtimes**: llama.cpp, MLX, ExecuTorch (optimized integrations)
- **Serving**: vLLM, SGLang
- **Local tools**: Ollama, LM Studio, Unsloth
- **Cloud**: Together AI, Fireworks AI, OpenRouter
- **Training**: PyTorch TorchTitan for customization
- **Hardware**: AMD, Arm, Dell, Intel, NVIDIA partnerships

## Weights

- [HuggingFace: meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [Developer Documentation](https://dev.meta.ai/docs)
- [Meta AI Developer Center](https://developer.meta.com/ai/models/muse-glimmer/)

## Related

- [[entities/meta]]
- [[entities/muse-spark]]
- [[concepts/inference/llama-cpp]]
