---
title: Bonsai 27B
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [model, quantization, on-device, local-llm, bonsai, prism-ml, open-source, benchmark, multimodal, reasoning]
sources:
  - raw/articles/2026-07-15_bonsai-27b-prism-ml.md
---

# Bonsai 27B

**Bonsai 27B** is a multimodal AI language model released by [[entities/prism-ml|Prism ML]] on July 14, 2026. It is the first 27-billion-parameter class model capable of running entirely on a phone, achieved through extreme quantization techniques. Based on [[entities/qwen|Qwen]] 3.6 27B and released under Apache 2.0.

## Architecture

Two variants using extreme low-bit quantization:

| Variant | Effective Bits/Weight | File Size |
|---|---|---|
| Ternary Bonsai 27B | 1.71 bits | 5.9 GB |
| 1-bit Bonsai 27B | 1.125 bits | 3.9 GB |

The low-bit representation is applied **end-to-end** across embeddings, attention, MLPs, and the LM head — no higher-precision escape hatches. The model carries a full 262K-token context window and supports speculative decoding via custom low-bit CUDA/MLX kernels.

## Phone Deployment

The 1-bit variant at ~4GB fits within the ~6GB usable memory of a 12GB iPhone, enabling the first on-device 27B-class model. Runs on iPhone 17 Pro / Pro Max (via Locally AI app), Mac/iPad via MLX, and NVIDIA GPUs via CUDA.

## Performance

| Hardware | 1-bit Speed | Ternary Speed |
|---|---|---|
| NVIDIA RTX 5090 | 163 tok/s | 134 tok/s |
| Apple M5 Max | 87 tok/s | 58 tok/s |

Overall benchmark retention: **95%** (ternary) and **90%** (1-bit) vs Qwen 3.6 27B baseline across 15 benchmarks. The claimed "intelligence density" (IQ per GB) is 0.53 for the 1-bit variant — over 10× the full-precision baseline.

## Agentic Use Cases

Framed as enabling on-device persistent agents, hybrid deployments (privacy-sensitive tasks locally, hardest steps to cloud), and sustained multi-step reasoning with tool calls, structured outputs, and computer-use agentic loops.

## Significance

Bonsai 27B represents a landmark in [[concepts/model-quantization|model compression]] and [[concepts/edge-ai|edge AI]], demonstrating that frontier-scale models can be deployed on consumer devices with acceptable performance degradation. It also marks the entry of Prism ML as a major player in the [[concepts/inference|inference]] ecosystem.

## External Links
- [Prism ML Announcement](https://prismml.com/news/bonsai-27b)
- [HN Discussion (612 points)](https://news.ycombinator.com/item?id=48910545)
- [HuggingFace Collection](https://huggingface.co/collections/prism-ml/bonsai-27b)
