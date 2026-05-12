---
title: "Accelerating Gemma 4: faster inference with multi-token prediction drafters"
source: Google Blog (The Keyword)
date: 2026-05-05
authors: [Olivier Lacombe, Maarten Grootendorst]
url: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
tags: [google, gemma, speculative-decoding, inference, optimization, open-source]
---

# Accelerating Gemma 4: faster inference with multi-token prediction drafters

Google released Multi-Token Prediction (MTP) drafters for the Gemma 4 family. By using a specialized speculative decoding architecture, these drafters deliver up to 3x speedup without any degradation in output quality or reasoning logic.

## Why Speculative Decoding?

Standard LLM inference is memory-bandwidth bound, creating a significant latency bottleneck. The processor spends the majority of its time moving billions of parameters from memory to compute units rather than performing actual calculations. 

Multi-Token Prediction drafters work alongside the main Gemma 4 model. The drafter is a lightweight model that predicts multiple tokens ahead, and the main model verifies them in parallel. This drastically reduces the sequential dependency that bottlenecks autoregressive generation.

## Key Results

- Up to 3x tokens-per-second speed increase
- No degradation in output quality or reasoning
- Tested on hardware using LiteRT-LM, MLX, Hugging Face Transformers, and vLLM
- Over 60 million Gemma 4 downloads in first few weeks

## Technical Innovation

MTP represents a mature application of speculative decoding — a technique where a smaller, faster "drafter" model proposes candidate tokens and the larger "target" model validates them. The drafter is specifically trained to predict multiple future tokens simultaneously, and the main model verifies all predictions in a single forward pass.

This is significant because it improves latency without changing the model weights — users get exactly the same outputs, just faster. The technique is particularly effective for code generation, long-form text, and structured outputs where tokens have high predictability.
