---
title: "Speculative Decoding for Reducing Latency in AI Inference"
url: "https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/"
source: "nvidia_blog"
authors: ["NVIDIA Technical Blog"]
published: "2025-04-18"
crawled: "2026-04-18"
type: "article"
tags: [inference, optimization, speculative-decoding, EAGLE, tensorrt]
---

# Speculative Decoding: Comprehensive Overview (NVIDIA)

## Primary Techniques
1. **Draft-Target:** Two-model system (large target + small draft). Draft proposes 3-12 tokens; target verifies in parallel.
2. **EAGLE-3:** Single-model with attached lightweight head. Extrapolates from target's internal hidden states. Uses dynamic draft trees & parallel tree attention.
3. **Multi-Token Prediction (MTP):** DeepSeek-R1 style. Multiple specialized prediction heads guess sequential future tokens.

## Key Insights
- Speculative decoding guarantees identical output quality to baseline model
- EAGLE head is instance-adaptive: dynamically evaluates confidence during tree generation
- Zero accuracy trade-off through rejection sampling
- Compatible with TensorRT-LLM, SGLang, vLLM

## Performance
- Standard autoregressive: 200ms/token → 3 tokens = 600ms
- Speculative decoding: ~250ms/pass → 3 tokens = 250ms
- EAGLE-3 eliminates separate draft model overhead
