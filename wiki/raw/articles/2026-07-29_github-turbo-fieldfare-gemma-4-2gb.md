---
title: "TurboFieldfare: Open-Source Engine Running Gemma 4 26B in ~2 GB RAM on Apple Silicon"
source_url: https://github.com/drumih/turbo-fieldfare
source_domain: github.com
author: "drumih (Andrey Mikhaylov), HN discussion"
date: 2026-07-29
date_ingested: 2026-07-30
type: raw_article
tags:
  - on-device-ai
  - gemma-4
  - metal
  - swift
  - moe
  - apple-silicon
  - model-inference
  - quantization
  - open-source
  - ssd-streaming
hn_url: https://news.ycombinator.com/item?id=49098510
hn_score: 823
hn_comments: 287
---

# TurboFieldfare: Gemma 4 26B-A4B in ~2 GB RAM on Apple Silicon

**GitHub**: https://github.com/drumih/turbo-fieldfare
**HN Discussion**: https://news.ycombinator.com/item?id=49098510 (823 points, 287 comments)
**Author**: Andrey Mikhaylov (drumih), iOS and Metal engineer

## Executive Summary

TurboFieldfare is a custom Swift + Metal inference runtime that runs **Gemma 4 26B-A4B** (instruction-tuned) in approximately **2 GB of RAM** on any Apple Silicon Mac (even 8 GB models). The full quantized model is ~14.3 GB, but TurboFieldfare keeps only the shared 1.35 GB core and FP16 KV cache in memory, streaming routed experts from SSD on-demand per token. It achieves 5-6 tok/s on an 8 GB M2 MacBook Air and 31-35 tok/s on a 24 GB M5 Pro.

The project includes six Swift packages: a library/runtime, native Mac app, decode service, CLI, OpenAI-compatible server, and streaming model installer (repacker).

---

## HN Show HN Post (by Andrey Mikhaylov / drumih)

> Hi HN,
>
> I built a specialized inference engine for running 4-bit Gemma 4 26B-A4B-IT on any M-series Mac using about 2 GB of RAM. It is called TurboFieldfare and is written in Swift and Metal.
>
> I have always adored on-device AI. It feels like magic that you can run a powerful NN on your Mac or iPhone. So I wanted to push the limits a bit and run a model whose weights don't fit in memory.
>
> The model's 4-bit quantized weights occupy roughly 14 GB, which makes running it with conventional inference tools almost impossible on an 8 GB or even 16 GB Mac once the OS, applications, and KV cache are included.
>
> The trick is to keep the shared part of the model and the KV cache in RAM, then stream only the routed experts needed for each token from SSD. An SSD is way slower than RAM, so the runtime uses a small expert cache and bounded parallel `pread`. While those reads are in flight, the GPU runs the shared part of the layer.
>
> I ran more than 100 experiments. Most didn't work. A few got me here. The experiments are described in the GitHub repo.
>
> It currently generates 5–6 tok/s on an 8 GB M2 MacBook Air and 31–35 tok/s on an M5 MacBook Pro.
>
> I also added an experimental OpenAI-compatible local server. It supports streaming and tool calls, and reuses one prompt prefix from the KV cache.
>
> Try it! The Mac app is easy to install. On the first run, it will download 15 GB of weights from Hugging Face. The model is surprisingly capable.
>
> I would love any kind of feedback!

---

## Full README Content

### Project Description

TurboFieldfare runs the instruction-tuned **[Gemma 4 26B-A4B](https://ai.google.dev/gemma/docs/core/model_card_4)** without loading the entire 14.3 GB model into memory. It keeps the shared 1.35 GB core and FP16 KV cache in memory, then streams only the experts needed for each token from SSD. This is what lets the model run on Macs with 8 GB of RAM.

The runtime, streaming installer, CLI, and native Mac app are written in Swift and Metal. TurboFieldfare is **model-specific** rather than a wrapper around MLX or llama.cpp. The curated experiment record summarizes **103 measured results** across kernels, caching, I/O, prefill, and decode.

### At a Glance

| Metric | Value |
|--------|-------|
| Model | Gemma 4 26B-A4B IT, 26B total parameters, ~3.88B active per token |
| Weights | MLX affine 4-bit, group 64; 8-bit router; 4-bit shared and routed experts |
| Memory | ~2 GB of weights and 4K KV cache |
| Storage | About 14.3 GB for the installed text-only model |
| Hardware | Apple Silicon Mac; 8 GB of RAM |
| Platform | macOS 26, Metal 4, Swift 6.2 |
| M2 measured decode | 5.1-6.3 tok/s on an 8 GB M2 MacBook Air |
| M5 measured decode | 31-35 tok/s on a 24 GB M5 Pro |

### Quick Start

```bash
git clone https://github.com/drumih/turbo-fieldfare.git
cd turbo-fieldfare
swift build -c release
.build/release/TurboFieldfareMac
```

On the first run, Swift Package Manager downloads and builds required packages. When the app opens, choose **Download** and let TurboFieldfare fetch and repack the pinned model (~15 GB). Once ready, choose **Load Model**, type a prompt, and press **Generate**.

### Swift Package Products (6 total)

| Product | Purpose |
|---------|---------|
| `TurboFieldfare` | Swift library containing the runtime and Metal kernels |
| `TurboFieldfareMac` | Native Mac app for installation and generation |
| `TurboFieldfareDecodeService` | One-shot local model and Metal owner used by the Mac app |
| `TurboFieldfareCLI` | Command-line instruction chat and raw completion |
| `TurboFieldfareServer` | Loopback OpenAI-compatible Chat Completions server |
| `TurboFieldfareRepack` | Streaming model installer and install verifier |

### Requirements

- Apple Silicon Mac (validated: 8 GB M2 MacBook Air)
- macOS 26 with Metal 4
- Xcode 26 and Swift 6.2+
- ~14.3 GB free storage
- Internet connection for first model install
- arm64-only; older macOS/Metal not supported

### How the Inference Engine Works

At each transformer layer:

1. **Metal computes attention and the router from resident weights.** The router produces top-8 expert IDs.
2. **CPU plans against the layer's 16-slot LFU (Least Frequently Used) cache**, then fills cache misses with bounded parallel `pread` calls into Metal-visible buffers.
3. **Metal computes the shared-expert branch** while those SSD reads are in flight.
4. **Combines shared and routed outputs.**

Key optimization: **Prompt prefill uses chunks of up to 128 tokens** so one fetched expert can serve multiple rows. Generation repeats the routed layer loop one token at a time.

### Model Installation (Streaming)

The installer **never materializes the full source checkpoint**. It streams required byte ranges from the pinned Hugging Face revision and repacks them directly into the `.gturbo` layout as they arrive. This avoids a second full checkpoint on disk and keeps scratch memory bounded.

- Transfers ~15 GB through bounded Hugging Face range requests
- Completed `.gturbo` occupies ~14.3 GB
- Accepted only after manifest and file hash validation
- Installation does not load the model into memory

### CLI Usage

Install model from CLI:
```bash
swift run -c release TurboFieldfareRepack --output scratch/gemma4.gturbo --overwrite
```

Instruction chat:
```bash
swift run -c release TurboFieldfareCLI --model scratch/gemma4.gturbo --messages-file messages.json
```

Raw completion:
```bash
swift run -c release TurboFieldfareCLI --model scratch/gemma4.gturbo --prompt "The capital of France is" --max-new 64 --temperature 0
```

### OpenAI-Compatible Server

```bash
swift build -c release --product TurboFieldfareServer
.build/release/TurboFieldfareServer --model scratch/gemma4.gturbo
```

Listens on `http://127.0.0.1:8080/v1`. Supports Chat Completions, streaming, function tools, and single-prefix prompt reuse. No remote auth or TLS — loopback only.

### Status and Scope

Currently includes:
- Remote streaming repack into `.gturbo` model format
- Instruction-tuned Gemma 4 26B-A4B with text-only chat formatting
- 4-bit MLX affine embedding, attention, shared-expert, and routed-expert weights (8-bit router)
- Custom Metal kernels for quantized GEMV, attention, MoE, normalization, RoPE, sampling, and production fusions
- SSD-backed routed-expert streaming with bounded expert cache
- Chunked single-prompt prefill and token-by-token generation
- FP16 KV storage with bounded circular storage (25 sliding-window layers) and linear storage (5 full-attention layers)
- Exact split-K/V decode attention with distinct normalized K and V paths

Future work: iPhone/iPad apps, benchmark more Apple Silicon Macs (base 16 GB M4 Mac mini, other 8 GB models).

### License

Source and documentation: Apache License 2.0. Model weights governed by their source terms. Independent research project — not affiliated with Google.

---

## HN Discussion Highlights

### Performance Reports

- **M4 Max 64 GB** (pwython): 48 tok/s decode at 1.9 GB RSS (2.4 GB peak). Page cache keeps the entire 12 GB packed_experts set resident; only ~1.6 GB per run reaches disk. With DaVinci Resolve open: 42.6 tok/s. With 38 GB incompressible memory squeeze: 41.8 tok/s. "Degrades gradually rather than a cliff."

- **M1 Max Mac Studio** (nvch): 12 tok/s with almost instant response. "Gives hope that large models may run locally from SSDs instead of memory."

- **M4 Mac mini 16 GB** (greggh): ~5 tok/s. "That jump from M4 to M5 is crazy."

- **M1 MBA (8 GPU cores)** (xenonite): 5-6 tok/s on macOS 15 (with Metal 4 `languageVersion` workaround).

### Why Only M-Series Macs?

The project is tightly bound to **Metal 4** for GPU compute (quantized GEMV, attention, MoE kernels) and uses Swift 6.2. It is not a PC/Linux project because it relies on Apple's unified memory architecture and Metal Shading Language.

### Comparison to mmap / llama.cpp

User tredre3 asked about comparison to llama.cpp's mmap approach. The key difference: TurboFieldfare **synchronizes SSD reads with inference activity** (GPU runs shared-expert while I/O is in flight), whereas the OS's mmap would handle paging generically without inference-aware scheduling.

### Speculative Prefetch Idea

User ycui1986 suggested using MTP (Multi-Token Prediction) heads for speculative prefetch of expert weights from SSD — if expert weights can be preloaded before the GPU needs them, cache miss penalty would be significantly reduced.

### Model-Specific Limitation

TurboFieldfare is model-specific (Gemma 4 26B-A4B) rather than a universal engine. It cannot run other models like Qwen 3.6 27B without significant rework, though the techniques could inspire similar projects.

---

## Key Technical Findings

1. **Memory strategy**: Only the shared 1.35 GB core + FP16 KV cache stays resident in RAM. Routed experts (~12 GB) are streamed from SSD on-demand.

2. **LFU expert cache**: 16-slot per-layer Least Frequently Used cache minimizes repeated SSD reads for frequently accessed experts.

3. **Parallel I/O + compute overlap**: While `pread` calls fetch missing experts from SSD, Metal simultaneously runs the shared-expert branch of the current layer — hiding I/O latency.

4. **Chunked prefill**: Processing prefill in 128-token chunks means one fetched expert can serve multiple rows, amortizing SSD access cost.

5. **Performance scales with SSD speed**: M4 Max (~7 GB/s SSD) achieves 48 tok/s vs M2 (~2 GB/s) at 5-6 tok/s. The M5 Pro's 31-35 tok/s reflects both faster SSD and improved architecture.

6. **Page cache is a huge factor**: With 64 GB RAM, the entire experts set stays in the page cache, dramatically reducing actual disk I/O.

7. **103 experiments documented**: The repo includes an audited experiment inventory covering kernels, caching, I/O strategies, prefill, and decode optimizations — providing a valuable reference for similar work.

8. **macOS 26 / Metal 4 / Swift 6.2 required**: The project uses the latest Apple toolchain features including Metal 4's `languageVersion .version4_0`. Can be patched to run on macOS 15 with a ~2.4x prefill speed penalty.
