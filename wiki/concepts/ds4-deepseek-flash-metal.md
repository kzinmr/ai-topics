---
title: "ds4.c — DeepSeek V4 Flash Metal Inference Engine"
created: 2026-05-08
updated: 2026-08-05
type: concept
tags:
  - local-llm
  - hardware
  - inference
  - quantization
  - coding-agent
  - tool
  - open-source
  - amd
aliases: [ds4, ds4-deepseek-flash-metal, deepseek-v4-flash-metal]
related:
  - concepts/deepseek-v4
  - entities/deepseek
  - entities/armin-ronacher
  - concepts/llama-cpp
sources:
  - raw/articles/2026-05-07_mitsuhiko_ds4-deepseek-flash-metal.md
  - https://github.com/mitsuhiko/ds4
  - raw/articles/2026-08-04_github-ryanzhou_deepseek-v4-flash-mi300x.md
---

# ds4.c — DeepSeek V4 Flash Metal Inference Engine

## Overview

**ds4.c** is a native inference engine developed by **Armin Ronacher (@mitsuhiko)** forking antirez's original work, **specialized exclusively for DeepSeek V4 Flash on Apple Silicon (Metal)**. Rather than a general GGUF runner, it is a specialized design that directly executes V4 Flash Metal graphs. Features seamless integration with Pi extensions.

### AMD MI300X Deployment

While ds4.c is purpose-built for Apple Silicon, the broader community has also demonstrated DeepSeek V4 Flash running on **AMD MI300X** hardware. The GitHub repository by **ryanzhou** ([deepseek-v4-flash-mi300x](https://github.com/ryanzhou/deepseek-v4-flash-mi300x)) provides a production-ready Docker Compose stack for serving DeepSeek V4 Flash on a single MI300X GPU, using vLLM ROCm nightly builds.

**Key characteristics of MI300X deployment:**
- **Single-GPU deployment**: The entire 304B-parameter checkpoint fits in 192 GB HBM3 (156.67 GiB for weights), with room for a 20 GB GPU KV pool and 96 GiB CPU tier — no PCIe weight streaming or layer offload required
- **Performance**: 168.6 tok/s single-stream decode, 542 tok/s across 8 concurrent streams, 830 tok/s at 64-stream burst; prefill reaches ~7.9–8.5K tok/s with tuned kernels
- **Context**: 256K tokens validated (architecture supports up to 1M)
- **FP8 correctness**: MI300X (CDNA3) uses the AMD/Graphcore `fnuz` variant of E4M3, which differs from the OCP-standard FP8 used by MI325X and newer GPUs — requiring format-aware kernel patches
- **vLLM patches**: The repository ships production overlays for MXFP4 MoE routing fixes, FP8 format handling, causal speculative verification, CPU-KV synchronization, and AITER GEMM tuning for `gfx942`

This deployment demonstrates that DeepSeek V4 Flash can run cost-effectively on non-NVIDIA hardware, with the MI300X's 2.4× HBM capacity advantage over H100 SXM5 enabling a simple single-card production configuration.

See also: [[entities/amd]], [[concepts/deepseek-v4]], [[concepts/deepseek-v4-serving]]

## Key Features

| Feature | Details |
|------|------|
| **Metal Exclusive** | Optimized for macOS. CPU path is for verification only (unstable due to macOS virtual memory bugs) |
| **Disk-First KV Cache** | Treats KV cache as a "first-class disk citizen", persistent across sessions and restarts |
| **1M Token Context** | Full support for V4 Flash's massive context window |
| **Asymmetric 2-bit Quantization** | MoE routed experts use IQ2_XXS/Q2_K, shared experts and projections remain unquantized for quality |
| **Agent Integration** | Direct integration with Claude Code, OpenCode, Pi |

## Performance

*Measured with 2-bit quantization, 32K context, no-think mode, greedy decoding*

| Machine | Prompt Size | Prefill Speed | Generation Speed |
|--------|-----------------|-------------|---------|
| MBP M3 Max (128GB) | Short | 58.52 t/s | 26.68 t/s |
| MBP M3 Max (128GB) | 11,709 tokens | 250.11 t/s | 21.47 t/s |
| Mac Studio M3 Ultra | Short | 84.43 t/s | 36.86 t/s |
| Mac Studio M3 Ultra | 11,709 tokens | 468.03 t/s | 27.39 t/s |

## Installation and Usage

### Via Pi Extension (Recommended)
```bash
pi install https://github.com/mitsuhiko/ds4
```

### Manual Build
```bash
./download_model.sh q2   # For 128GB RAM machines
./download_model.sh q4   # For 256GB+ RAM machines
make
```

### Interactive CLI
```bash
./ds4
# Commands: /think, /nothink, /ctx N, /read FILE, /quit
# Ctrl+C to interrupt generation
```

### Local Server
Provides OpenAI/Anthropic compatible API:
```bash
./ds4-server --ctx 100000 --kv-disk-dir /tmp/ds4-kv --kv-disk-space-mb 8192
```
- Endpoints: `/v1/chat/completions` (OpenAI), `/v1/messages` (Anthropic/Claude Code)
- SSE streaming support (text + thinking blocks)

## Claude Code Integration

```bash
export ANTHROPIC_BASE_URL="http://127.0.0.1:8000"
export ANTHROPIC_MODEL="deepseek-v4-flash"
exec "$HOME/.local/bin/claude" "$@"
```

## Technical Constraints

- **Memory Requirements**: Approximately 81GB with 2-bit quantization. +26GB for 1M token context. 100K-300K recommended for 128GB machines
- **Thinking Mode**: Supports thinking, nothink, Think Max. Think Max requires sufficient context window
- **MTP (Speculative Decoding)**: Experimental support (`--mtp` flag), currently only minor speedup
- **Development**: Built with strong assistance from GPT 5.5, on top of llama.cpp / GGML foundations

## Disk KV Cache System

Persists token prefixes with filenames using SHA1 hashes (`<sha1>.kv`):
- **Save Triggers**: cold (after long initial prompt), continued (periodic during generation), evict/shutdown (memory release or stop)
- **Observability**: Cache files include plain-text headers, human-inspectable via `hexdump`

## Related Pages

- [[concepts/deepseek-v4]] — DeepSeek-V4 model series
- [[entities/armin-ronacher]] — Developer
- [[entities/deepseek]] — DeepSeek company
