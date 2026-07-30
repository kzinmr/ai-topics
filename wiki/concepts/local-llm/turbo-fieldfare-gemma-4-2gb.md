---
title: "turbo-fieldfare: Gemma 4 on Consumer Hardware"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags:
  - local-llm
  - inference
  - quantization
  - moe
  - apple-silicon

  - open-source
  - on-device
sources:
  - raw/articles/2026-07-29_github-turbo-fieldfare-gemma-4-2gb.md
related:
  - "[[entities/gemma-4]]"
  - "[[concepts/local-llm/_index]]"
  - "[[concepts/local-llm/llama-cpp]]"
  - "[[concepts/llm-inference-optimization-performance]]"
  - "[[concepts/apple]]"
---

# turbo-fieldfare: Gemma 4 on Consumer Hardware

## Summary

turbo-fieldfare is an open-source inference engine that runs **Gemma 4 26B-A4B** (26 billion parameters total, ~3.88B active per token) in approximately **2 GB of RAM** on any Apple Silicon Mac, including entry-level 8 GB models. The technique represents a significant achievement in on-device AI: making a large mixture-of-experts model usable on consumer hardware that would otherwise be incapable of loading the full ~14.3 GB of quantized weights into memory.

Built by Andrey Mikhaylov (drumih) entirely in Swift and Metal, the project is model-specific — it is not a general-purpose inference framework like [[concepts/local-llm/llama-cpp|llama.cpp]] or MLX — but its architectural techniques have broad implications for how large MoE models can be deployed on memory-constrained devices.

The project was posted to Hacker News in July 2026 and received 823 points, reflecting strong community interest in practical [[concepts/local-llm/_index|local-llm]] deployment.

## Technical Architecture

### Core Insight: Shared Core + Streaming Experts

The key insight behind turbo-fieldfare is that a Mixture-of-Experts model consists of two fundamentally different weight categories:

1. **Shared weights (~1.35 GB)**: The attention parameters, shared-expert branch, router, embeddings, and norm layers — used for every token. These stay resident in RAM.
2. **Routed experts (~12 GB)**: The per-layer expert MLP blocks — only a small subset (top-8) is needed per token. These are streamed from SSD on-demand.

This split allows the engine to keep just the shared core and FP16 KV cache in memory (~2 GB total), while fetching routed experts from storage only when required.

### Per-Layer Inference Pipeline

At each transformer layer, turbo-fieldfare executes:

1. **Metal computes attention and the router** from resident shared weights. The router produces top-8 expert IDs for the current token.
2. **CPU plans against the layer's 16-slot LFU cache**, then fills cache misses with bounded parallel `pread()` calls into Metal-visible buffers.
3. **Metal computes the shared-expert branch** while those SSD reads are in flight — overlapping I/O latency with useful GPU work.
4. **Combines shared and routed outputs** to produce the layer output.

### Key Optimizations

| Technique | Purpose |
|-----------|---------|
| **LFU expert cache** (16 slots per layer) | Minimizes repeated SSD reads for frequently selected experts |
| **Parallel I/O + compute overlap** | GPU runs shared-expert branch while `pread()` fetches missing experts |
| **Chunked prefill** (128-token chunks) | One fetched expert serves multiple prefill rows, amortizing SSD access cost |
| **Bounded circular KV storage** | 25 sliding-window layers with bounded storage; 5 full-attention layers with linear storage |
| **Streaming model installer** | Never materializes the full source checkpoint — streams byte ranges from Hugging Face and repacks directly into `.gturbo` layout |

### Why Apple Silicon Only

The project is tightly bound to **Metal 4** for GPU compute (quantized GEMV, attention, MoE kernels) and uses Swift 6.2 with Apple's unified memory architecture. It does not target PC/Linux because it relies on Metal Shading Language and the unified memory model where CPU and GPU share the same physical RAM — critical for the zero-copy I/O overlap pattern.

## Performance

### Measured Tokens per Second

| Hardware | RAM | Decode Speed | Notes |
|----------|-----|-------------|-------|
| M2 MacBook Air (8 GB) | 8 GB | 5–6 tok/s | Baseline consumer hardware |
| M4 Mac mini (16 GB) | 16 GB | ~5 tok/s | Comparable to M2 due to SSD bandwidth |
| M1 Max Mac Studio | 32 GB+ | ~12 tok/s | Faster SSD, larger page cache |
| M5 Pro (24 GB) | 24 GB | 31–35 tok/s | Next-gen architecture, faster SSD |
| M4 Max (64 GB) | 64 GB | ~48 tok/s | Entire expert set fits in page cache |

The M4 Max at 64 GB achieves 48 tok/s because the operating system's page cache can hold the complete ~12 GB expert set in RAM after the first token, effectively eliminating disk I/O for subsequent tokens. With an additional 38 GB of incompressible memory pressure, throughput only drops to 41.8 tok/s — the performance degrades gradually rather than hitting a cliff.

### Performance Drivers

Turbo-fieldfare's throughput scales primarily with two factors:

1. **SSD read bandwidth**: The engine reads expert weights from SSD on cache misses. M2 (~2 GB/s SSD) yields 5–6 tok/s; M4 Max (~7 GB/s) yields 48 tok/s. The M5 Pro's 31–35 tok/s reflects both faster storage and architectural improvements.
2. **Available RAM for page cache**: More free RAM means more expert weights stay in the kernel page cache, reducing actual disk reads. On 64 GB systems, essentially zero real disk I/O occurs after the first token.

## Platform Requirements

- **Hardware**: Any Apple Silicon Mac (M1 or later), minimum 8 GB RAM
- **OS**: macOS 26 with Metal 4 (can be patched for macOS 15 with ~2.4x prefill penalty)
- **Storage**: ~14.3 GB free for the installed `.gturbo` model file
- **Toolchain**: Xcode 26, Swift 6.2+
- **Network**: Required for first-time model download from Hugging Face (~15 GB transfer)

The project includes six Swift package products: a runtime library, native Mac app, decode service, CLI, OpenAI-compatible local server (loopback only, no auth/TLS), and a streaming model installer/repacker.

## Comparison to llama.cpp and MLX

turbo-fieldfare is fundamentally different from general-purpose inference frameworks:

| Dimension | turbo-fieldfare | llama.cpp / MLX |
|-----------|----------------|-----------------|
| Scope | Model-specific (Gemma 4 26B-A4B only) | General-purpose, many models |
| Memory strategy | Selective SSD streaming with inference-aware scheduling | Full model in RAM via mmap |
| I/O approach | Application-level `pread()` with expert cache, overlapped with GPU compute | OS-managed mmap paging |
| GPU API | Metal-only (Swift + Metal Shading Language) | Multi-backend (Metal via MLX, Vulkan, CUDA) |
| MoE optimization | Deeply integrated — router, cache, streaming all specialized for MoE topology | Generic MoE support without SSD streaming |

The critical architectural difference is that turbo-fieldfare **synchronizes SSD reads with inference activity** — the GPU runs the shared-expert branch while I/O is in flight — whereas mmap-based approaches delegate all paging decisions to the OS, which has no knowledge of which weights will be needed next. This inference-aware scheduling is what makes the 2 GB footprint possible.

## Significance for On-Device AI

turbo-fieldfare demonstrates that large MoE models can be made practical on memory-constrained consumer devices by splitting responsibility between resident weights and on-demand expert streaming. This has several implications:

1. **MoE is the right architecture for on-device**: The expert-sparse nature of MoE models makes them naturally suited for SSD-backed execution, since only a small fraction of parameters is active per token.
2. **SSD bandwidth is the limiting factor**: As Apple Silicon SSD speeds continue to improve (M4 generation already at ~7 GB/s), this approach becomes increasingly viable for even faster interactive use.
3. **Application-level I/O wins over mmap**: Knowledge of the model topology allows the runtime to prefetch and cache with far better hit rates than the OS page cache alone.
4. **The gap between local and cloud narrows**: Running a 26B-parameter model on an 8 GB laptop was previously impossible without this technique. At 5–6 tok/s, it is usable for batch processing and background tasks, and at 31–48 tok/s on newer hardware, it approaches interactive conversational speeds.

The author documented 103 experiments across kernels, caching, I/O strategies, prefill, and decode optimization — providing a valuable reference for anyone attempting similar SSD-backed MoE inference.

## See Also

- [[entities/gemma-4]] — Gemma 4 model architecture and capabilities
- [[concepts/local-llm/_index]] — Overview of local LLM deployment approaches
- [[concepts/local-llm/llama-cpp]] — General-purpose local inference with mmap
- [[concepts/llm-inference-optimization-performance]] — Broader inference optimization landscape
- [[concepts/apple]] — Apple's role in on-device AI infrastructure
- [turbo-fieldfare on GitHub](https://github.com/drumih/turbo-fieldfare)
- [HN Discussion (823 points)](https://news.ycombinator.com/item?id=49098510)
