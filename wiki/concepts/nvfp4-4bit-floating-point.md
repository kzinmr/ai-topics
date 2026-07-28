---
title: "NVFP4 — 4-Bit Floating Point on Blackwell"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags:
  - quantization
  - inference
  - nvidia
  - hardware
  - llm-inference
  - gpu
sources:
  - raw/articles/2026-07-28_mayhem4markets_nvfp4-blackwell-4bit-floating-point.md
---

# NVFP4 — 4-Bit Floating Point on Blackwell

## Overview

NVFP4 is NVIDIA's proprietary 4-bit floating-point format, natively supported in hardware on Blackwell-generation GPUs through their Tensor Cores. It represents a significant step in the industry's push toward ultra-low-precision inference, following the progression from INT8 → FP8 → FP4. Unlike generic IEEE-style FP4 formats, NVFP4 is specifically optimized for the weight and activation distributions found in neural network inference workloads.

## Format and Hardware

Blackwell's Tensor Cores include dedicated silicon for NVFP4 multiply-accumulate operations. This is not emulated or simulated — it's native hardware acceleration, similar to how FP8 was introduced with Hopper (H100). The format is designed to balance dynamic range (via the exponent) against precision (via the mantissa) within just 4 bits, making it suitable for the skewed, near-zero distributions typical of LLM weights and activations.

## Performance

Based on published data from NVIDIA and ecosystem reports:

| Metric | Improvement |
|--------|-------------|
| Throughput vs FP8 | **2–3× higher** inference throughput |
| Memory vs BF16 | **3.5× less** memory usage |
| Accuracy vs higher precision | **Within 1–2%** on large models |

These gains translate directly into practical benefits:
- **Fewer GPUs** for the same model size, or larger models on the same hardware
- **Lower cost per token** for inference serving
- **Reduced memory bandwidth pressure**, a dominant bottleneck in transformer inference
- **Better energy efficiency**, reducing both operational cost and carbon footprint

## Use Cases

NVFP4 is primarily targeted at LLM inference serving, where the combination of reduced memory footprint and higher throughput directly improves economics. It is supported in [[concepts/tensorrt-llm]], NVIDIA's optimized inference framework, which handles FP4 quantization and deployment. The format is also relevant for:
- Batch inference at scale
- Edge and on-device deployment of large models
- Real-time serving where latency budgets are tight

## Quantization Landscape

NVFP4 fits into the broader low-precision ecosystem as the next step down from FP8:

| Precision | Bits | Typical Use | Native HW Support |
|-----------|------|-------------|-------------------|
| BF16/FP16 | 16 | Training, high-accuracy inference | A100, H100, consumer GPUs |
| FP8 | 8 | High-throughput inference, some training | H100 (Hopper) |
| INT8 | 8 | Inference (established, mature) | A100, H100, consumer GPUs |
| INT4 | 4 | Aggressive inference quantization | Limited native support |
| **NVFP4** | **4** | **Ultra-low-precision inference** | **B200 / Blackwell** |

Key distinctions:
- NVFP4 uses a **floating-point** representation, unlike INT4 which is integer-based. Floating point provides non-uniform quantization steps that better match weight distributions, often yielding better accuracy at the same bit width.
- Unlike generic 4-bit schemes (GPTQ, AWQ, GGUF Q4 variants), NVFP4 is hardware-accelerated — the quantization gains translate to actual throughput, not just memory savings.
- FP8 on Hopper already proved the value proposition of natively accelerated low-precision floating point. NVFP4 extends this one bit-width further.

For broader context on how quantization reduces model size and inference cost, see [[concepts/model-quantization]]. For the inference optimization techniques that complement NVFP4 (KV cache management, speculative decoding, batching), see [[concepts/llm-inference-optimization-performance]].

## Relationship to NVIDIA Ecosystem

NVFP4 is part of [[entities/nvidia]]'s multi-generational precision roadmap:

- **A100 (Ampere)**: Introduced BF16 and TF32, established the pattern of mixed-precision training
- **H100 (Hopper)**: Introduced FP8 with the Transformer Engine, proving native low-precision floating point at scale
- **B200 (Blackwell)**: Introduces NVFP4, pushing to 4-bit native floating point

Each generation reduces the minimal viable precision by roughly one bit, roughly doubling throughput density while maintaining acceptable accuracy. This progression is a key driver of NVIDIA's inference cost reductions from one generation to the next.

## Open Questions

- How much accuracy degradation occurs on smaller (<7B parameter) models, where the 1–2% figure may not hold
- Whether NVFP4 can be used for any training workloads (quantization-aware training, fine-tuning) or is strictly inference-only
- Adoption timeline for cloud providers and model-serving platforms beyond NVIDIA's own stack
- Competition from alternative low-precision approaches (AMD's FP6, custom silicon with INT4)
