---
title: "Inkling (Thinking Machines)"
type: concept
aliases:
  - inkling
  - Thinking Machines Inkling
created: 2026-07-15
updated: 2026-11-24
tags:
  - model
  - multimodal
  - open-source
  - quantization
  - reasoning
sources:
  - raw/articles/2026-07-15_danielhanchen_inkling-1bit-gguf-quants.md
  - raw/articles/2026-07-15_danielhanchen_inkling-unsloth-studio.md
  - raw/articles/together.ai--blog-together-ai-brings-thinking-machines-labs-new-model-ink--b5b36c00.md
  - raw/articles/modal.com--blog-inkling-by-thinking-machines-labs-now-available-on-moda--07fbc32a.md
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

## Inkling 2 Mini (Nov 20, 2026) — looped transformer for laptops

Thinking Machines released **Inkling 2 Mini**, a looped transformer that runs its middle layers three times per token: 26.4B total / 3.4B active parameters (5.4B weight activations per token with looping), ~20GB memory footprint, native NVFP4 training and deployment (last four layers MXFP8). It leads all open-weights models under 100B on DeepSWE v1.1 (48.2%) and Vals Index v2.2 (46.5%), and is behind only Qwen3.8-27B on some coding suites. Most weights trained and deployed in NVFP4; a demo built a playable flight simulator offline on an M5 Pro MacBook Pro in airplane mode.

The looped architecture doubles as a monitorability research platform: with the companion variable-loop model, no-CoT reasoning time horizon improved from 16s at one pass to 37s at three, benchmark performance on serial reasoning kept improving out to ten loops (2x the trained depth), the chain of thought grew shorter with more loops but stayed legible, and agentic-sabotage test scores did not trend higher with added loops. Looping improves reasoning/long-context (GraphWalks BFS, MRCR v2) but not factual knowledge (AA-Omniscience, SimpleQA) — knowledge tracks total parameter count; the model compensates with search/tool use (leads its size class on BrowseComp, DeepSearchQA, MCP Atlas).

HN (1060 pts): unsloth GGUF quants landed within hours; llama.cpp looped-architecture support is an open PR (#32695) with the usual worry that exotic architectures stall in PR queues; local-hardware owners (Framework Desktop / Ryzen AI Max / Strix Halo) framed it as the first credible Qwen3.6-35B-A3B-class competitor for commodity boxes.

HN: https://news.ycombinator.com/item?id=50581260

**Third-party hosted demo (Nov 21, 2026):** Eric Zhang (@ekzhang1, ex-Modal founding engineer, now Thinking Machines) posted a "just for fun" hosted chat demo of Inkling 2 Mini on Modal, also exposing a `/v1/chat/completions` endpoint "for your agent". The page's own title was **Resin**, indicating it was served by his Rust inference-engine library rather than a stock server — an early external adoption signal for the model as an *agent-serving* target, not just a laptop model. The endpoint returned 404 when probed on 2026-11-24 (see [[entities/eric-zhang]] Recent Notes).
## Related Pages
- [[entities/thinking-machines-lab]] — Developer of Inkling
- [[entities/daniel-han]] — Unsloth CEO, led Inkling GGUF quantization
- [[concepts/open-source-llms]] — Open-source LLM landscape
- [[concepts/unsloth]] — Unsloth framework
- [[concepts/unsloth-fast-fine-tuning]] — Unsloth's fast fine-tuning approach
