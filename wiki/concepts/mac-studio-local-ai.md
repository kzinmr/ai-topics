---
title: Mac Studio for Local AI
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, optimization, platform]
sources: [raw/articles/spicyneuron-mac-studio-local-ai-6months.md]
---

# Mac Studio for Local AI

## Overview

Using Apple Mac Studio (M3 with 512GB unified memory) as a local inference platform for running frontier-class LLMs (600B–1T+ parameters) without cloud APIs. This approach trades raw throughput for privacy, zero rate limits, and cost predictability.

## Why Mac Studio?

### Advantages
- **Unified memory architecture** — 512GB can house trillion-parameter models entirely in memory
- **Single hardware under $10k** — alternatives include $50k multi-GPU workstations, DIY 3090 clusters, or NVIDIA DGX Sparks
- **Quiet, cool, residential-safe** — won't trip home circuit breakers

### Trade-offs
- **Slow prompt processing** — Apple Silicon's memory bandwidth is the bottleneck (surprisingly negotiable with optimization)
- **Open models lag behind API models** — open models ≈ API models from 6–12 months prior
- **Proprietary ecosystem** — MLX framework is Apple-specific, not portable

## Performance Benchmarks (6-Month Real-World)

| Metric | Result |
|--------|--------|
| Max model size | ~1T parameters (Kimi K2.5) fits with room to spare |
| Simple chat | Replies in seconds |
| ~7k token edit | ~30 seconds |
| ~16k token Claude Code | ~90 seconds |
| Streaming speed | >3x reading speed |

## Key Technical Components

### MLX Framework
Apple's native ML framework for AI inference. As of 2026:
- [[mlx]] for language models, [[mlx]] for multimodal
- **10–25% faster than llama.cpp** on Apple Silicon
- Uses `uvx --from mlx-lm mlx_lm.server` for quick deployment
- Model registry: HuggingFace (e.g., `spicyneuron/Qwen3.5-35B-A3B-MLX-4.8bit`)

### GPU Memory Override
macOS caps GPU memory at 75% by default. Override via sysctl:
```bash
sysctl -w iogpu.wired_limit_mb=$((TOTAL_MEMORY - 6144))
sysctl -w iogpu.wired_lwm_mb=$((TOTAL_MEMORY - 10240))
```
Reclaims ~120GB additional GPU memory on 512GB Mac Studio.

### Model Selection — MoE Architecture
Mixture-of-Experts models keep all weights in memory but activate only a subset per token:

| Model | Total Params | Active Params | Speed |
|-------|-------------|---------------|-------|
| Kimi K2.5 | 1T | 32B | decent |
| GLM 5 | 744B | 40B | ~20% slower |
| Qwen 3.5 397B | 397B | 17B | ~2x faster |

### Quantization
- **4-bit dynamic quantization** is the sweet spot for Apple Silicon
- Larger models tolerate <4-bit; smaller models need ≥4-bit
- Mixed/dynamic precision keeps critical weights at higher precision

### API Gateway — llama-swap
`llama-swap` runs multiple models behind a single endpoint with centralized generation parameters. Useful for routing between different model sizes/capabilities.

### Claude Code on Local Hardware
- Router: `claude-code-router` translates Anthropic's `/v1/messages` to OpenAI-compatible `/v1/chat/completions`
- System prompt reduction: ~20k → <8k tokens by stripping verbose instructions
- Prompt caching issues: Claude Code's random tool/argument key ordering invalidates cache; fix via sorted Jinja templates

## Open Questions

- How long until Apple Silicon prompt processing closes the gap with GPU clusters?
- Will MLX become the de facto standard for Apple local inference, or will llama.cpp adapt?
- Can speculative decoding overcome the bandwidth bottleneck?
- What's the energy efficiency comparison vs cloud GPU inference per token?

## Related Concepts

- [[concepts/mlx-llm]] — MLX framework for language model inference
- [[gguf]] — 4-bit and dynamic quantization techniques
- [[claude-code]] — Local Claude Code deployment patterns
- [[concepts/llama-cpp]] — Alternative inference engine (llama.cpp vs MLX)
- [[mixture-of-experts]] — Mixture-of-Experts model design
