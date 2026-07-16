---
title: "Inkling (Thinking Machines)"
type: concept
aliases:
  - inkling
  - Thinking Machines Inkling
created: 2026-07-15
updated: 2026-07-15
tags:
  - model
  - multimodal
  - open-source
  - quantization
  - reasoning
sources:
  - raw/articles/2026-07-15_danielhanchen_inkling-1bit-gguf-quants.md
  - raw/articles/2026-07-15_danielhanchen_inkling-unsloth-studio.md
---

# Inkling

**Inkling** is a multimodal AI model developed by [[entities/thinking-machines-lab|Thinking Machines Lab]]. It supports vision, audio, and tool calling natively, and uses a numerical reasoning level system (0.0 to 0.99) for controlling inference depth.

## Overview

Inkling is Thinking Machines Lab's flagship multimodal model, designed for native interaction across modalities. Unlike bolt-on multimodal scaffolding, Inkling handles vision, audio, and text natively as part of its architecture.

## Key Features

- **Native multimodal**: Vision, audio, and text processed in a unified architecture
- **Numerical reasoning levels**: Controllable reasoning depth from 0.0 (fast) to 0.99 (deep)
- **Interleaved tool calling**: Use tools mid-generation without breaking context
- **Web search + code execution**: Built-in capabilities

## Quantization

In July 2026, [[entities/daniel-han|Unsloth]] collaborated with Thinking Machines to produce 1-bit GGUF quants of Inkling:

- **86% smaller**: 270GB vs 1.9TB for the full model
- **74.2% top-1% accuracy retention**: High quality despite aggressive quantization
- **Vision and audio support preserved** in the quantized version
- Available at: [huggingface.co/unsloth/inkling-GGUF](https://huggingface.co/unsloth/inkling-GGUF)

This enables running Inkling on consumer hardware that would otherwise require ~2TB VRAM.

## Integration

- **Unsloth Studio**: Full local integration with tool calling, web search, code execution, vision, and audio support since July 2026
- Documentation: [unsloth.ai/docs/models/inkling](https://unsloth.ai/docs/models/inkling)

## Architecture

Inkling is a decoder-only mixture-of-experts transformer with **975B total / 40-41B active** parameters and a 1M token context window. It was trained on 45T tokens using NVIDIA GB300 NVL72 hardware.

### Attention Mechanism
- **Hybrid attention (5:1 ratio)**: Five sliding-window local-attention layers followed by one full-attention global layer per block. This biases compute toward recent context for efficiency while maintaining full-sequence awareness.
- **Query-conditioned relative attention**: Each attention layer combines standard query-key similarity with a learned relative-position bias based on token distance, replacing RoPE/absolute position embeddings.

### Specialized Components
- **Sconv**: Lightweight channelwise causal convolution (4-token receptive field) applied to key/value streams and sublayer outputs, providing local token mixing without full attention cost.
- **Shared Expert Sink MoE**: Routed and shared experts are normalized together, allowing the shared path to dynamically compete for mixture weight on each token — unlike conventional shared-expert designs.

### Speculative Decoding
[[concepts/modal|Modal]] developed a custom DFlash block-diffusion speculator tuned to Inkling's local-attention layout. The drafter uses all-local sliding-window attention (no global layers), enabling flat-cost speculation. On 8× B200 GPUs, this achieves 250 tok/s/user (67% faster than the built-in MTP head).

## Benchmarks & Evaluation

Inkling achieves an **Intelligence Index of 41**, surpassing Nemotron 3 Ultra (38) as the best US-based open-weights model. The same model performs strongly across diverse tasks:
- Graduate-level scientific reasoning
- Competition mathematics
- Software engineering (coding + agentic)
- Browser-based tasks
- Visual document understanding
- Audio comprehension
- Forecasting and calibrated prediction

## Ecosystem

| Platform | Support Level | Details |
|----------|-------------|---------|
| [[entities/together-ai|Together AI]] | Serverless inference | FlashAttention-4 kernel for query-conditioned attention; OpenAI-compatible API |
| [[concepts/modal|Modal]] | Managed Endpoints | Custom DFlash speculator; 250 tok/s/user; token-based pricing |
| [[entities/daniel-han|Unsloth]] | Quantization + Studio | 1-bit GGUF (86% smaller); Unsloth Studio local deployment |
| [[concepts/vllm|vLLM]] | Inference framework | Day-0 support |
| SGLang | Inference framework | Day-0 support |
| Baseten | Deployment | Day-0 support |
| Databricks | Deployment | Day-0 support |
| Hugging Face | Model hub | Model weights + blog post |
| Tinker | Deployment | Day-0 support |

## Variants

- **Inkling** (975B-A41B): Full release, the primary model
- **Inkling-Small** (276B-A12B): Smaller preview variant for reduced compute requirements

## Related Pages
- [[entities/thinking-machines-lab]] — Developer of Inkling
- [[entities/daniel-han]] — Unsloth CEO, led Inkling GGUF quantization
- [[concepts/open-source-llms]] — Open-source LLM landscape
- [[concepts/unsloth]] — Unsloth framework
- [[concepts/unsloth-fast-fine-tuning]] — Unsloth's fast fine-tuning approach
