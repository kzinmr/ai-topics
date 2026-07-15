---
title: "Bonsai 27B — First 27B-Class Model That Runs on a Phone"
created: 2026-07-15
updated: 2026-07-15
type: article
source: "https://prismml.com/news/bonsai-27b"
status: complete
sources:
  - "https://prismml.com/news/bonsai-27b"
  - "https://news.ycombinator.com/item?id=48910545"
  - "https://huggingface.co/collections/prism-ml/bonsai-27b"
  - "https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-27b-whitepaper.pdf"
  - "https://github.com/PrismML-Eng/Bonsai-demo/"
  - "https://docs.prismml.com/"
  - "https://huggingface.co/prism-ml"
  - "https://www.together.ai/models/prism-ml-ternary-bonsai-27b"
---

# Bonsai 27B — Prism ML

## Summary

Bonsai 27B is a multimodal AI language model released by Prism ML on July 14, 2026. It is the flagship model in the Bonsai family (also includes 8B, 4B, 1.7B, and Image variants). Its headline claim is being the first 27-billion-parameter class model that can run entirely on a phone. Based on Qwen 3.6 27B, released under Apache 2.0.

## Architecture

Two variants using extreme quantization:

| Variant | Weight Type | Effective Bits/Weight | File Size |
|---|---|---|---|
| Ternary Bonsai 27B | Ternary {-1, 0, +1} with FP16 group-wise scaling | 1.71 bits | 5.9 GB |
| 1-bit Bonsai 27B | Binary {-1, +1} with FP16 group-wise scaling | 1.125 bits | 3.9 GB |

- Low-bit representation applied end-to-end: embeddings, attention, MLPs, LM head
- Multimodal — vision tower in compact 4-bit form
- Full 262K-token context window
- Speculative decoding support
- Hybrid-attention architecture via custom low-bit CUDA/MLX kernels

## Phone Deployment

The 1-bit variant at ~4GB enables phone deployment. A 12GB iPhone offers ~6GB usable memory for an app — no conventional 27B build clears this (even 4-bit is ~18GB). At 4GB, the 1-bit variant is the first 27B-class model to fit.

- Runs on iPhone 17 Pro / Pro Max (via Locally AI iOS app)
- Runs on Mac / iPad via MLX, NVIDIA GPUs via CUDA
- Users reported success on M1 Pro (16GB RAM), M5 Max

## Inference Speed

| Hardware | 1-bit | Ternary |
|---|---|---|
| NVIDIA RTX 5090 | 163 tok/s | 134 tok/s |
| Apple M5 Max | 87 tok/s | 58 tok/s |

## Benchmark Performance (Thinking Mode)

| Category | Qwen 3.6 27B | Ternary Bonsai | 1-bit Bonsai |
|---|---|---|---|
| Math | 95.3 | 93.4 | 91.7 |
| Coding | 88.7 | 86.0 | 81.9 |
| Agentic/Tool-calling | 80.0 | 74.0 | 66.0 |
| Instruction Following | 78.4 | 71.8 | 65.8 |
| Knowledge/STEM | 83.1 | 77.0 | 73.4 |
| Vision | 72.6 | 65.2 | 59.6 |
| **Overall** | **85.0** | **80.5 (95%)** | **76.1 (90%)** |

Claim: "Intelligence density" (IQ per GB) is 0.53 for 1-bit variant — >10x full-precision baseline.

## Background

Prism ML emerged from Caltech researchers. Backed by Khosla Ventures, Cerberus, Google, and Samsung. Full technical details in whitepaper at https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-27b-whitepaper.pdf

## HN Coverage

612 points, 214 comments. Story ID: 48910545. Generally positive but mixed — some skeptical about benchmarks vs real-world performance. Some users reported issues running in LM Studio on launch day. PrismML team directed users to their custom llama.cpp forks.
