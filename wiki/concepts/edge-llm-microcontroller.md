---
title: "Edge LLM on Microcontrollers"
created: 2026-07-26
updated: 2026-07-26
type: concept
tags:
  - edge-ai
  - model
  - inference
  - hardware
  - small-language-model
  - quantization
  - embedded-systems
  - on-device
  - infrastructure
sources: [raw/articles/2026-07-25_slvdev-esp32-llm-microcontroller.md]
---

# Edge LLM on Microcontrollers

Edge LLM inference on microcontrollers (MCUs) refers to running small language models (20–30M parameters) fully on-device on low-cost, resource-constrained chips — no server, no cloud, no network connection needed. This represents a ~100× leap over the previous state-of-the-art for MCU-based language models.

## What This Is

Running language models on microcontrollers was long considered impractical due to extreme memory constraints. The previous record for an MCU-based LLM was ~260K parameters. In July 2026, a project demonstrated a **28.9M parameter model** running on an **$8 ESP32-S3** at ~9.5 tokens/second — two orders of magnitude larger than prior work.

The key insight: most of a language model's parameters reside in an embedding table that is read from (not computed on). By storing this 25M-row table in cheap, high-capacity **flash memory** and loading only the ~450 bytes needed per token into fast SRAM, the model's effective parameter count can be decoupled from the MCU's limited RAM.

## ESP32-S3 Example

The [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) project (HN: 201 points, Jul 25, 2026) demonstrated this on the Espressif ESP32-S3:

| Metric | Value |
|--------|-------|
| Parameters | 28.9M stored (25M in flash lookup table) |
| Chip | ESP32-S3, ~$8 |
| SRAM | 512 KB (fast, internal) |
| PSRAM | 8 MB (medium-speed, external SPI RAM) |
| Flash | 16 MB (slow, bulk storage) |
| Clock | 240 MHz dual-core Xtensa LX7 |
| Inference Speed | ~9.5 tok/s end-to-end (~9.7 tok/s pure compute) |
| Model Size | 14.9 MB at 4-bit quantization |
| Connectivity | None — fully local, on-chip inference |
| Training Data | TinyStories (synthetic short stories) |

### Memory Architecture

```
SRAM  (512 KB, fast)    → the "thinking" core, used on every token
PSRAM (8 MB, medium)    → output head and working memory
FLASH (16 MB, slow)     → 25M-param embedding table, ~6 rows read per token (~450 B)
```

The model was trained on TinyStories (Eldan & Li, Microsoft Research, arXiv:2305.07759), so it writes short, simple stories rather than answering questions or following instructions. The significance lies in the **architecture and deployment technique**, not the model's conversational capability.

## Key Constraints

Microcontrollers impose hard limits that shape the design space:

- **RAM**: The ESP32-S3 has only 512 KB of internal SRAM. Even with 8 MB of external PSRAM, loading a full 28.9M-param model into working memory is impossible. The flash-streaming trick is what makes this viable.
- **Compute**: At 240 MHz dual-core, the chip delivers roughly 0.5 GOPS — about six orders of magnitude less than a modern GPU. Inference must be heavily optimized in plain C.
- **Storage**: 16 MB of flash is ample for model weights, but read bandwidth (~40 MB/s on ESP32-S3) is the bottleneck. Only ~450 bytes per token are fetched, keeping latency manageable.
- **No OS**: No Linux, no virtual memory, no file system. Everything runs bare-metal or on FreeRTOS with manual memory management.

## Techniques Used

### Per-Layer Embeddings (PLE)
Originating from Google's Gemma 3n and Gemma 4 architectures, PLE separates the embedding lookup table from the transformer core. The embedding table — which constitutes the vast majority of parameters — is stored in high-latency flash and accessed sparsely (6 rows per token). The smaller transformer layers (~3.9M params) fit in SRAM/PSRAM and do the actual computation.

### 4-bit Quantization
The full model at FP16 would require ~58 MB, far exceeding the 16 MB flash budget. At 4-bit (INT4), the model shrinks to 14.9 MB. The quantization scheme is applied to both the embedding table and the transformer weights, with careful calibration to preserve text coherence.

### Flash Memory Streaming
Rather than loading the entire model into RAM at startup, the inference loop streams embedding rows from flash on demand. This is conceptually similar to memory-mapped inference in [[concepts/local-llm/llama-cpp]] but adapted for raw flash access on a microcontroller without an OS.

## Comparison to Larger Edge Devices

| Platform | Price | RAM | Compute | Max Model Size | Throughput |
|----------|-------|-----|---------|---------------|------------|
| ESP32-S3 (this project) | ~$8 | 512 KB + 8 MB PSRAM | 240 MHz dual-core | 28.9M (4-bit) | ~9.5 tok/s |
| Raspberry Pi 4 | ~$35 | 2–8 GB | 1.5 GHz quad ARM | ~3B (Q4) | ~3–10 tok/s |
| Raspberry Pi 5 | ~$60 | 4–8 GB | 2.4 GHz quad ARM | ~7B (Q4) | ~5–15 tok/s |
| Jetson Nano | ~$99 | 4 GB | 128 CUDA cores | ~8B (Q4) | ~10–20 tok/s |
| Jetson Orin Nano | ~$199 | 4–8 GB | 1024 CUDA + 32 Tensor | ~70B (Q4) | ~15–40 tok/s |

The ESP32-S3 sits at the extreme low end of both cost and capability. It cannot run practical chatbots or assistants, but it demonstrates a viable path for **sensor-adjacent NLP** — devices that need to understand or generate simple language patterns without any connectivity.

See [[concepts/edge-ai]] for the broader landscape of on-device AI across all device classes.

## Significance

This project represents a **~100× increase** in LLM parameter count on microcontrollers (from 260K → 28.9M). The implications:

- **New device class**: Opens the door for NLP-capable devices in the sub-$10 BOM range — smart sensors, toys, wearables, and industrial monitors that can process language locally.
- **Privacy-preserving**: Fully local inference means zero data leaves the device. No cloud costs, no network dependency, no privacy trade-offs.
- **Architecture innovation**: Proves that Per-Layer Embeddings (originally designed for phone-scale Gemma models) scale down to the extreme edge, bridging the gap between GPU-class and MCU-class inference.
- **Research frontier**: Establishes a baseline for future work in extreme-edge LLM deployment, inviting improvements in quantization, architecture search, and on-chip acceleration.

## Limitations

- **Task scope**: The model generates stories from TinyStories; it cannot answer questions, follow instructions, or write code. The "reasoning" core (~3.9M params) is too small for practical agentic or conversational use.
- **Batch size = 1**: No parallelism. Each token is generated sequentially with no batching or speculative decoding.
- **No fine-tuning on-device**: Training or adaptation on the MCU is infeasible. All weights are statically compiled into flash.
- **Hardware-specific**: The approach is tightly coupled to the ESP32-S3 memory hierarchy. Porting to other MCUs requires re-engineering the memory access patterns.

## Related Pages

- [[concepts/edge-ai]] — Broader landscape of on-device AI inference
- [[concepts/small-language-models]] — Compact language models for edge and mobile
- [[concepts/model-quantization]] — Quantization techniques for model compression
- [[concepts/local-llm/llama-cpp]] — C/C++ inference engine (similar bare-metal philosophy)
- [[concepts/gguf-quantization]] — GGUF quantization format used in local deployment
