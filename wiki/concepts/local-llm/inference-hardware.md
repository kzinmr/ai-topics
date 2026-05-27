---
title: "Local LLM Inference Hardware"
type: concept
created: 2026-04-15
updated: 2026-05-27
status: complete
tags:
  - local-llm
  - hardware
  - inference
  - infrastructure
aliases: [inference-hardware, consumer-gpu-llm, local-llm-hardware]
sources:
  - url: "https://localllm.in/blog/ollama-vram-requirements-for-local-llms"
    title: "Ollama VRAM Requirements: Complete 2026 Guide"
  - url: "https://www.spheron.network/blog/gpu-memory-requirements-llm"
    title: "GPU Memory Requirements for LLMs: VRAM Calculator"
  - url: "https://www.sitepoint.com/local-llm-hardware-requirements-mac-vs-pc-2026"
    title: "Local LLM Hardware Requirements: Mac vs PC 2026 (SitePoint)"
  - url: "https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026"
    title: "LLM Quantization Explained: INT4, INT8, FP8, AWQ, GPTQ in 2026"
---
---
---


# Local LLM Inference Hardware

**Local LLM Inference Hardware** refers to hardware configurations for running LLMs in a local environment. **VRAM capacity** is the most important constraint, with required hardware determined by model size, quantization method, and context length.

## VRAM Requirements Basics

### Required VRAM by Model Size (Inference)

| Model Size | BF16 | FP8 | INT8 | INT4 (AWQ/GPTQ) | GGUF Q4_K_M |
|------------|------|-----|------|-----------------|-------------|
| **7B** | 14GB | 7GB | 7GB | 4-5GB | 4-5GB |
| **13B** | 26GB | 13GB | 13GB | 7-8GB | 8-9GB |
| **30B** | 60GB | 30GB | 30GB | 16-18GB | 18-20GB |
| **70B** | 140GB | 70GB | 70GB | 36-40GB | 40-45GB |
| **180B** | 360GB | 180GB | 180GB | 92-100GB | — |

* **15-25% additional** needed for KV cache and framework overhead

### Quantization vs Quality Trade-offs

| Quantization | VRAM Reduction | Quality Impact | Recommended Use |
|-----------|-----------|------------|---------|
| BF16 | 0% (baseline) | Baseline | When maximum quality is needed |
| FP8 | 50% | Negligible (<2% degradation) | Best for Blackwell/Hopper GPUs |
| INT8 | 50% | Minor | Alternative for older GPUs |
| INT4 (AWQ/GPTQ) | 75% | Noticeable but usable | Running 70B on a single GPU |
| GGUF Q4_K_M | 75% | Good | Standard for Ollama / llama.cpp |

## Consumer GPU Options

### NVIDIA (as of 2026)

| GPU | VRAM | Memory Bandwidth | Supported Models (INT4) | Price Range |
|-----|------|------------|-----------------|--------|
| **RTX 4060** | 8GB GDDR6 | 272 GB/s | 7B-8B | Entry |
| **RTX 4070** | 12GB GDDR6X | 504 GB/s | 7B-13B | Mid-range |
| **RTX 4080** | 16GB GDDR6X | 736 GB/s | 7B-30B | High-end |
| **RTX 4090** | 24GB GDDR6X | 1,008 GB/s | 7B-30B (70B at INT4) | Flagship |
| **RTX 5090** | 32GB GDDR7 | 1,792 GB/s | 7B-30B (70B comfortably) | Latest Gen |
| **RTX PRO 6000** | 96GB | — | 70B FP8 possible | Workstation |

### Apple Silicon

| Chip | Unified Memory | Memory Bandwidth | Supported Models |
|-------|-----------|------------|-----------|
| **M3 Pro** | 18-36GB | 150 GB/s | 7B〜13B |
| **M3 Max** | 36-128GB | 400 GB/s | 7B-70B (70B F16 possible with 128GB) |
| **M4 Pro/Max** | 24-128GB | Improved vs M3 expected | Comparable or better |

**Apple's advantage**: Unified memory allows running 70B+ models on a single device, which is impossible on consumer NVIDIA GPUs.

### AMD

| GPU | VRAM | Memory Bandwidth | Notes |
|-----|------|------------|------|
| **RX 7900 XTX** | 24GB GDDR6 | 960 GB/s | ROCm compatible, usable with llama.cpp/Ollama |
| **MI300X** | 192GB HBM3 | 5.2 TB/s | Datacenter-grade |

## Edge Devices

| Device | Memory | Performance | Use Case |
|---------|-------|------|------------|
| **Jetson Orin NX** | 8-16GB | 70 TOPS | Robotics, edge AI |
| **Jetson AGX Orin** | 32-64GB | 275 TOPS | Advanced edge inference |
| **Raspberry Pi 5** | 8GB | Limited | Small models (<1B) |

## Why VRAM Matters Most

**VRAM is a hard boundary, not a soft limit.** When a model doesn't fit in VRAM, offloading to system RAM occurs, causing **5-20x performance degradation**. Memory bandwidth becomes the practical determinant of tokens/second.

## Purchase Guidelines (2026)

| Budget | Recommended Configuration | Runable Models |
|------|---------|--------------|
| Entry (~$500) | RTX 4060 8GB | 7B Q4_K_M |
| Mid-range (~$1,000) | RTX 4070/5070 12GB | 7B-13B Q4_K_M |
| High-end (~$2,000) | RTX 4090/5090 24-32GB | 7B-30B, 70B (INT4) |
| Pro (~$4,000+) | Mac M3 Max 128GB / 2x RTX 5090 | 70B+, Multi-GPU |
| Datacenter | H100/B200 / DGX | Any model |

## Related Links

- [[concepts/local-llm]] — Local LLM ecosystem overview
- [[concepts/local-llm/ollama]] — Ollama local LLM runner
- [[concepts/inference/sglang]] — SGLang fast inference
- [[concepts/inference/llama-cpp]] — llama.cpp CPU/Apple inference

## Sources

- [Ollama VRAM Requirements Guide](https://localllm.in/blog/ollama-vram-requirements-for-local-llms)
- [GPU Memory Requirements for LLMs](https://www.spheron.network/blog/gpu-memory-requirements-llm)
- [Local LLM Hardware Requirements: Mac vs PC 2026](https://www.sitepoint.com/local-llm-hardware-requirements-mac-vs-pc-2026)
- [LLM Quantization Explained 2026](https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026)
