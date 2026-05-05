---
title: "Accelerating Gemma 4: faster inference with multi-token prediction drafters"
source: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
date: 2026-05-05
scraped: 2026-05-05
tags: [google, gemma-4, speculative-decoding, inference, multi-token-prediction, mtp]
---

# Accelerating Gemma 4: Multi-Token Prediction (MTP) Drafters

**Source:** Google Blog
**Date:** May 05, 2026

## Key Performance Breakthroughs
Google has introduced **Multi-Token Prediction (MTP) drafters**, a specialized architecture designed to eliminate memory-bandwidth bottlenecks in LLM inference.

- **Speedup:** Up to **3x faster inference** compared to standard methods.
- **Quality:** **Zero degradation** in output quality, reasoning logic, or accuracy.
- **Efficiency:** Utilizes idle compute to predict future tokens while the main model verifies them in parallel.

> "By pairing a heavy target model (e.g., Gemma 4 31B) with a lightweight drafter (the MTP model), we can utilize idle compute to 'predict' several future tokens at once... The target model then verifies all of these suggested tokens in parallel."

## How Speculative Decoding Works
Standard LLMs are **autoregressive** (generating one token at a time), which is inefficient for obvious continuations. MTP changes this:

1. **Drafting:** A lightweight MTP model suggests a sequence of future tokens.
2. **Verification:** The large "target" model (e.g., Gemma 4 31B) checks the entire sequence in a **single forward pass**.
3. **Bonus Token:** If the target model agrees with the draft, it accepts the sequence and generates one additional token simultaneously.

### Technical Enhancements
- **Shared KV Cache:** Drafters utilize the target model's activations and share its Key-Value (KV) cache to avoid redundant calculations.
- **Clustering Technique:** Implemented in the embedder for E2B and E4B edge models to bypass logit calculation bottlenecks.
- **Batch Optimization:** On Apple Silicon, processing batch sizes of 4–8 (rather than 1) unlocks up to a **~2.2x speedup** for the 26B MoE model.

## Use Cases & Benefits
- **Edge Devices (E2B/E4B models):** Faster output on mobile/IoT devices, leading to significantly **preserved battery life**.
- **Workstations (26B MoE / 31B Dense):** Enables complex offline coding and agentic workflows on consumer GPUs (e.g., NVIDIA RTX PRO 6000).
- **Real-time Apps:** Drastically reduced latency for voice applications and multi-step autonomous agents.

## Getting Started
The MTP drafters are released under the **Apache 2.0 license**.

### Supported Frameworks
- **Local/Edge:** LiteRT-LM, MLX, Ollama, Google AI Edge Gallery (Android/iOS).
- **Cloud/Server:** vLLM, SGLang, Hugging Face Transformers.

### Model Access
| Platform | Link |
| :--- | :--- |
| **Hugging Face** | [Gemma 4 Collection](https://huggingface.co/collections/google/gemma-4) |
| **Kaggle** | [Gemma 4 Models](https://www.kaggle.com/models/google/gemma-4) |
| **Documentation** | [MTP Overview](https://ai.google.dev/gemma/docs/mtp/overview) |
