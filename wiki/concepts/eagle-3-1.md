---
title: EAGLE 3.1
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [concept, speculative-decoding, inference, optimization, vllm, torchspec, benchmark]
sources:
  - raw/articles/2026-05-26_vllm_eagle-3-1.md
  - https://vllm.ai/blog/2026-05-26-eagle-3-1
---

# EAGLE 3.1

**EAGLE 3.1** is a targeted reliability upgrade to the widely deployed EAGLE family of speculative decoding algorithms. Jointly developed by the EAGLE, vLLM, and TorchSpec teams (May 2026), it addresses **attention drift** — a newly identified instability that degrades speculative decoding performance under real-world conditions like varying chat templates, long contexts, and out-of-distribution prompts.

## The Problem: Attention Drift

As speculation depth increases, the draft model gradually shifts attention away from sink tokens toward its own generated tokens, causing degraded acceptance length and reduced output stability.

Two underlying causes:
1. **Imbalanced fused input** — higher-layer hidden states increasingly dominate the drafter's input
2. **Growing hidden-state magnitude** — unnormalized residual path inflates hidden states across decoding steps

## Architectural Fixes

### FC Normalization
Normalization applied after each target hidden state, before the FC layer. Without it, hidden-state magnitude grows across steps, making the drafter increasingly unreliable.

### Post-Norm Hidden-State Feedback
Post-normalization hidden states are fed into the next decoding step, making the method behave more like recursively invoking the drafter rather than appending layers to the target model.

## Improvements Over EAGLE 3

- Better training-to-inference extrapolation
- Stronger long-context robustness
- Higher resilience to chat template and system prompt variation
- More stable acceptance length across diverse serving environments
- **Up to 2× longer acceptance length** in long-context workloads

## Performance (Kimi K2.6 on SPEED-Bench, vLLM TP=4, GB200)

| Concurrency | Throughput Speedup |
|------------|-------------------|
| C=1 | **2.03×** |
| C=4 | **1.71×** |
| C=16 | **1.66×** |

## vLLM Integration

EAGLE 3.1 integrates into vLLM as a config-driven extension of the existing EAGLE 3 path, fully backward-compatible. Available in vLLM v0.22.0.

## Training with TorchSpec

TorchSpec provides efficient training support. A draft model for Kimi K2.6 is open-sourced: `lightseekorg/kimi-k2.6-eagle3.1-mla` on HuggingFace.

## Related Concepts

- [[concepts/speculative-decoding]] — broader speculative decoding landscape
- [[concepts/speculative-decoding-mtp]] — multi-token prediction approach
- [[concepts/inference]] — LLM inference optimization
- [[entities/nvidia]] — GPU support for benchmarks

## References

- vLLM Blog: [EAGLE 3.1: Advancing Speculative Decoding](https://vllm.ai/blog/2026-05-26-eagle-3-1) (May 26, 2026)
- HuggingFace: [lightseekorg/kimi-k2.6-eagle3.1-mla](https://huggingface.co/lightseekorg/kimi-k2.6-eagle3.1-mla)
