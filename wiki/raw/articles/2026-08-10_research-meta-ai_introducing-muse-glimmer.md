---
title: "Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device"
type: article
date: 2026-08-10
source: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
author: Meta Superintelligence Labs
tags:
  - model
  - ai-agents
  - local-llm
  - on-device
  - open-source
  - meta
  - quantization
  - speculative-decoding
---

# Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device

**Source**: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
**Published**: 2026-08-10
**Author**: Meta Superintelligence Labs

## Summary

Muse Glimmer is a 30-billion-parameter open agentic model from Meta Superintelligence Labs, optimized for always-on local agent workflows on consumer hardware. Released under Apache 2.0 license with weights on [HuggingFace](https://huggingface.co/meta-models/Muse-Glimmer-30B) and [developer documentation](https://dev.meta.ai/docs).

## Key Points

- **Parameters**: 30B, optimized for local deployment on Mac/PC with single consumer GPU
- **License**: Apache 2.0 (permissive open source)
- **Training**: 3-phase approach using logit distillation from Muse Spark teacher model:
  1. **Pre-Training**: Trained on Muse Spark's outputs using logit distillation
  2. **Mid-Training**: Longer-context, agent-heavy data with richer reasoning traces
  3. **Post-Training**: SFT + on-policy distillation + RL across general, reasoning, coding, and agentic domains
- **Evaluation**: Under Meta's Advanced AI Scaling Framework

## Agentic Capabilities

- End-to-end agentic task completion (DeepSearch QA, MCP-Atlas, τ-Bench, SWE-Bench)
- Reliable tool use with precise schemas across extended workflows
- Multi-step reasoning over long horizons
- Failure recovery — diagnoses errors and retries
- Multimodal input via dedicated perception encoder (text + images)
- Scaffold compatibility (OpenClaw and other orchestration patterns)
- Controllable effort (reasoning strength levels)
- Multilingual (100+ languages)

## Performance

Compared with Gemma4-31B and Qwen3.6-27B, Muse Glimmer performs strongly for its size class across agentic, coding, multimodal, safety, and reasoning benchmarks.

## Local Deployment Optimizations

- **Quantization**: ~4-bit precision, compresses LM to under 20GB (from 55GB+ full precision). Fits within 24-32GB envelope alongside KV cache, perception encoder, and drafter
- **Speculative Decoding**: Ships with DFlash-based lightweight drafter model. Speed improvements:
  - RTX 5090: 3.1x faster
  - M5 Max: 1.8x faster
  - M4 Max: 1.5x faster

## Ecosystem Integration

- **Edge frameworks**: llama.cpp, MLX, ExecuTorch (optimized integrations coming)
- **Serving**: vLLM, SGLang
- **Local tools**: Ollama, LM Studio, Unsloth (coming)
- **Cloud partners**: Together AI, Fireworks AI, OpenRouter
- **Training customization**: PyTorch TorchTitan
- **Hardware partners**: AMD, Arm, Dell, Intel, NVIDIA
