---
title: "MLX"
type: concept
created: 2026-04-27
updated: 2026-10-19
tags:
  - hardware
  - inference
  - model
  - apple-silicon
status: L3
aliases: [Apple MLX, MLX Framework, MLX Community]
sources:
  - https://github.com/ml-explore/mlx
  - https://ml-explore.github.io/mlx/build/html/index.html
  - https://machinelearning.apple.com/research/mlx-distributed-inference
---


# MLX

## Summary

MLX (pronounced "mɛlɪks") is an open-source array processing framework for machine learning on Apple Silicon, developed by Apple's machine learning research team. It provides a NumPy-like API on top of hardware-optimized primitives that leverage the unified memory architecture of Apple's M-series and A-series chips. As of 2025-2026, MLX has become the primary local inference and fine-tuning framework for Apple Silicon users, offering memory-efficient model execution where GPU and CPU share a unified memory pool.

## Key Ideas

- **Unified Memory Architecture**: The defining advantage of MLX on Apple Silicon — CPU and GPU share the same memory pool (up to 192GB on Mac Pro, 512GB on Mac Studio), eliminating PCIe transfer overhead and enabling models that would be impossible on discrete GPU setups
- **NumPy-Compatible API**: MLX's functional programming model mirrors NumPy with lazy computation, making it accessible to Python ML practitioners without specialized GPU programming knowledge
- **Hardware-Accelerated Primitives**: MLX leverages Apple's ANE (Neural Engine), GPU, and CPU through Metal Performance Shaders, optimized for the M-series chip architecture
- **Lightweight Fine-Tuning**: Combined with MLX LoRA/QLoRA, users can fine-tune 7B-70B parameter models on a single Mac Studio or MacBook Pro with 64GB+ RAM
- **Ecosystem & Community**: The MLX community (mlx-community on Hugging Face) maintains thousands of pre-converted models in MLX format, alongside tools like MLX-VLM (vision-language), MLX-Whisper (speech), and MLX-Examples
- **Model Serving**: MLX Serve and MLX LM provide efficient local model serving for development and small-scale production use

## Terminology

- **Unified Memory**: Shared memory pool accessible by both CPU and GPU without copying data across PCIe — the key performance differentiator on Apple Silicon
- **MLX LM**: Command-line tool and library for running language models locally with MLX, supporting streaming, batched generation, and prompt caching
- **MLX LoRA**: MLX-native implementation of Low-Rank Adaptation for efficient fine-tuning on Apple Silicon
- **MLX Community**: Hugging Face organization (mlx-community) hosting thousands of MLX-converted models, from tiny (0.5B) to frontier-scale (236B)
- **ANE (Apple Neural Engine)**: Dedicated ML hardware in Apple Silicon chips for energy-efficient neural network inference

## Examples/Applications

- **Local LLM Inference**: Running Llama 3, Qwen 2.5, DeepSeek, and Phi models at interactive speeds on MacBook Pro and Mac Studio
- **Fine-Tuning on Mac**: Using MLX + LoRA to fine-tune 7B-34B models on a single Mac Studio with 192GB unified memory
- **Vision-Language Models**: MLX-VLM enables running LLaVA, Qwen-VL, and other VLMs locally for image understanding
- **Research Prototyping**: MLX's Python-first design makes it ideal for rapid ML research iteration, especially in the Apple ecosystem
- **Model Conversion**: Converting PyTorch models to MLX format, often with float16 → float32 precision adjustment for optimal Apple Silicon performance

## Distributed Inference with RDMA (October 2026)

Apple's ML Research team published a major update on October 16, 2026 (HN 365p), demonstrating that the latest MLX release — paired with the new **RDMA over Thunderbolt driver** — enables multi-Mac distributed inference on frontier-scale models. HN: 365 points.

### Headline result

**Muse Spark Open** (816B parameters, 42B active MoE, ~1 trillion total parameters) generates over **36 tokens/second** on a cluster of **four Mac Studio M5 Ultra** machines using tensor-parallelism across the RDMA interconnect. The previous-generation M3 Ultra required 2 machines; M5 Ultra's 1.2 TB/s memory bandwidth (vs 819 GB/s on M3 Ultra) and GPU Neural Accelerators make 4-node clusters practical for desktop deployment.

### Models benchmarked (Oct 2026)

| Model | Parameters | Architecture | Precision | Fits on 1x Mac Studio 512GB |
|-------|-----------|--------------|-----------|-----------------------------|
| Muse Spark Open | 816B | MoE (42B active) | NVFP4 | No (needs 2–4 nodes) |
| Mistral Medium 3.5 | 128B | Dense | FP8 | Yes (158GB peak RAM) |
| Qwen 3.8 | 27B | Dense | BF16 | Yes (68GB peak RAM) |

### M5 Ultra vs M3 Ultra performance

- **TTFT (time to first token)**: Up to **4.6× faster** on M5 Ultra — GPU Neural Accelerators provide dedicated matrix-multiplication hardware, making Mac Studio M5 Ultra the "desktop of choice" for very large context workloads.
- **Decode throughput (tokens/s)**: **1.6× faster** on M5 Ultra due to 1.2 TB/s unified memory bandwidth (memory-bandwidth-bound metric).
- Benchmarks run at context sizes 8,192 and 65,536 tokens, reflecting agentic coding workloads which require large contexts.

### Parallelization schemes

Three distributed modes are available:
1. **Pipeline parallelization (2 nodes)**: splits model layers across 2 Mac Studios
2. **Tensor parallelization (2 nodes)**: splits individual matrix operations across 2 Mac Studios
3. **Tensor parallelization (4 nodes)**: the highest-throughput configuration used for Muse Spark Open

The **RDMA over Thunderbolt driver** is the key enabling technology — it provides the low-latency, high-bandwidth interconnect needed for synchronous tensor-parallel operations across machines without a dedicated high-speed network fabric.

### Significance

- **First desktop-class frontier-scale LLM inference**: Before this, 800B+ parameter models required rack-scale data-center hardware. A 4× Mac Studio cluster with 2 TB aggregate unified memory is the first consumer-hardware configuration capable of serving an ~1T-parameter MoE model at interactive speeds.
- **Agentic coding on-device**: Apple explicitly frames the use case as agentic workflows — coding agents that need 65K+ token contexts can run entirely locally, in a private environment, with no API dependency.
- **Muse Spark Open tie-in**: This release was timed with Meta's open-weight Muse Spark Open release, making the Apple MLX + Muse Spark Open combination the flagship open-weight local-inference story of October 2026.

## Related Concepts

- [[inference/llama-cpp]]
- [[concepts/local-llm/_index]]
- [[concepts/fine-tuning]]
- [[concepts/mac-studio-local-ai]]
- [[concepts/inference]]
- [[entities/muse-spark]] — 816B MoE open-weight model that is the flagship demonstration for MLX distributed inference
- [[concepts/apple-silicon-m6-m5-ultra]] — hardware platform (M5 Ultra / Neural Accelerators) underlying MLX distributed inference
- [[concepts/mixture-of-experts]] — architecture of Muse Spark Open
- [[concepts/kv-cache]] — memory-bandwidth-bound decode phase that M5 Ultra's 1.2 TB/s bandwidth directly improves

## Sources

- [MLX GitHub Repository](https://github.com/ml-explore/mlx)
- [MLX Documentation](https://ml-explore.github.io/mlx/build/html/index.html)
- [MLX Community on Hugging Face](https://huggingface.co/mlx-community)
- [Apple ML Research: MLX Distributed Inference (Oct 16, 2026)](https://machinelearning.apple.com/research/mlx-distributed-inference)
