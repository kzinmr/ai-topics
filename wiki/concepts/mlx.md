---
title: "MLX"
type: concept
tags:
  - mlx
  - apple-silicon
  - inference
  - model
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Apple MLX, MLX Framework, MLX Community]
related: [[concepts/inference/llama-cpp]], [[concepts/local-llm]], [[concepts/fine-tuning]], [[concepts/mac-studio-local-ai]]
sources: [https://github.com/ml-explore/mlx, https://ml-explore.github.io/mlx/build/html/index.html]
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

## Related Concepts

- [[inference/llama-cpp]]
- [[local-llm]]
- [[fine-tuning]]
- [[mac-studio-local-ai]]
- [[inference]]

## Sources

- [MLX GitHub Repository](https://github.com/ml-explore/mlx)
- [MLX Documentation](https://ml-explore.github.io/mlx/build/html/index.html)
- [MLX Community on Hugging Face](https://huggingface.co/mlx-community)
