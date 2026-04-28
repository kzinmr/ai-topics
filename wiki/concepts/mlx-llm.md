---
title: MLX for LLM Inference
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, platform, tool]
sources: [raw/articles/spicyneuron-mac-studio-local-ai-6months.md]
---

# MLX for LLM Inference

## Overview

[[mlx]] and [[mlx]] are Apple's MLX framework packages for running large language models and multimodal models on Apple Silicon. As of 2026, MLX provides **10–25% faster inference** than llama.cpp on Apple Silicon hardware.

## Key Packages

### mlx-lm
Language model inference server. Quick start:
```bash
uvx --from mlx-lm mlx_lm.server \
  --host 127.0.0.1 \
  --port 8080 \
  --model spicyneuron/Qwen3.5-35B-A3B-MLX-4.8bit
```

### mlx-vlm
Multimodal (vision-language) model inference. Supports image + text inputs.

## Model Format

MLX uses a custom quantized format optimized for Apple Silicon unified memory. Models are published on HuggingFace with MLX-specific naming conventions:
- `spicyneuron/Qwen3.5-35B-A3B-MLX-4.8bit`
- Other community-converted models follow similar patterns

## Key Features

### Dynamic Memory Management
- Integrates with macOS GPU memory override (sysctl `iogpu.wired_limit_mb`)
- Leverages Apple's unified memory architecture for models exceeding GPU memory
- Automatic CPU-GPU memory swapping for models larger than available VRAM

### Custom Forks
The community has developed custom forks for advanced features:
- **Speculative cache warmup** — pre-process next turn while reading current response (addresses Claude Code's dynamic `<thought>` tag cache invalidation)
- **Sorted template rendering** — fix prompt caching by deterministic key ordering in Jinja chat templates

### Model Architecture Support
- Strong support for **Mixture-of-Experts (MoE)** models
- MoE models keep full weights in memory but activate only a subset per token
- Ideal for Apple Silicon's massive RAM + moderate bandwidth profile

## Comparison with Alternatives

| Aspect | MLX | llama.cpp |
|--------|-----|-----------|
| Speed on Apple Silicon | 10–25% faster | baseline |
| Portability | Apple Silicon only | Cross-platform (CPU, GPU, all OS) |
| Model formats | Custom MLX format | GGUF (industry standard) |
| Ecosystem maturity | Growing (2026) | Mature |
| Community models | HuggingFace (growing) | HuggingFace + many converters |
| Customization | Custom forks available | Extensive CLI options |

## Open Questions

- Will MLX format become widely adopted beyond Apple Silicon?
- Can MLX match llama.cpp's cross-platform availability?
- How will MLX handle emerging model architectures (state space models, etc.)?

## Related Concepts

- [[concepts/mac-studio-local-ai]] — Mac Studio hardware setup for local inference
- [[gguf]] — 4-bit and dynamic quantization techniques
- [[mixture-of-experts]] — Mixture-of-Experts model design
- [[concepts/llama-cpp]] — Cross-platform inference engine alternative
- [[claude-code]] — Local Claude Code deployment using MLX
