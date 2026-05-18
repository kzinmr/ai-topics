---
title: "Multi-Token Prediction (MTP) Drafters"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags:
  - inference
  - optimization
  - google
  - open-source
sources: [raw/articles/2026-05-05_google-gemma-4-multi-token-prediction.md]
---

# Multi-Token Prediction (MTP) Drafters

A speculative decoding technique where a lightweight "drafter" model predicts multiple future tokens simultaneously, and the main target model verifies them in a single forward pass. Released for [[entities/gemma-4]] on May 5, 2026.

## How It Works

Standard LLM inference is memory-bandwidth bound — the processor spends most of its time moving parameters from memory to compute rather than performing calculations. Speculative decoding addresses this by:

1. A small, fast drafter model proposes N candidate tokens
2. The large target model validates all N tokens in one forward pass
3. Accepted tokens are kept; rejected tokens trigger re-generation

## Gemma 4 Results

- Up to **3x tokens-per-second speedup**
- No degradation in output quality or reasoning
- Tested on LiteRT-LM, MLX, Hugging Face Transformers, vLLM
- Over 60 million Gemma 4 downloads in first few weeks

## Significance

MTP drafters represent a mature application of [[concepts/speculative-decoding]]. The key innovation is that users get exactly the same outputs, just faster — the model weights are unchanged. This is particularly effective for code generation, long-form text, and structured outputs where tokens have high predictability.

## Related Pages
- [[entities/gemma-4]] — Gemma 4 open models
- [[concepts/speculative-decoding]] — Speculative decoding technique
- [[concepts/inference]] — LLM inference optimization
