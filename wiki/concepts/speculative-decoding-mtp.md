---
title: "Speculative Decoding and Multi-Token Prediction"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [inference, optimization, speculative-decoding, mtp, performance, google]
aliases:
  - multi-token-prediction
  - mtp
  - speculative-decoding
  - drafter-model
related:
  - [[concepts/gguf-quantization]]
  - [[concepts/serving-llms-vllm]]
sources:
  - raw/articles/2026-05-05-gemma-4-drafter-explained.md
  - https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
  - https://ai.google.dev/gemma/docs/mtp/overview
  - https://ai.google.dev/gemma/docs/mtp/mtp
  - https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/
  - https://arxiv.org/abs/2211.17192
description: "Speculative decoding and Multi-Token Prediction (MTP) techniques that accelerate LLM inference by using a smaller draft model to predict multiple tokens ahead, verified in parallel by the larger target model. Achieves up to 3x speedup with zero quality loss."
---

# Speculative Decoding and Multi-Token Prediction (MTP)

**Speculative decoding** is an inference optimization technique that accelerates LLM generation by using a smaller, faster "draft model" to predict multiple tokens ahead, which are then verified in parallel by the larger "target model." **Multi-Token Prediction (MTP)** is Google's specific implementation of speculative decoding, introduced with the Gemma 4 model family in 2026.

## The Bottleneck: Memory-Bandwidth Bound Inference

Standard autoregressive LLM generation produces exactly one token at a time. This process is fundamentally **memory-bandwidth bound**: the processor spends more time moving model parameters from VRAM than actually computing. This is especially wasteful for obvious continuations (predicting "words" after "Actions speak louder than...") that consume the same computation as complex reasoning steps.

## How Speculative Decoding Works

1. **Draft Phase:** A smaller, faster draft model predicts a sequence of N tokens ahead
2. **Verification Phase:** The large target model verifies all N drafted tokens in a single forward pass
3. **Acceptance:** If the target agrees with the draft, the entire sequence is accepted
4. **Bonus Token:** The target model also generates one additional token of its own during verification
5. **Rejection:** If the target rejects a draft token, it produces the correct token for that position, and the draft model resumes from the new correct token

This means the system can produce tokens from the draft sequence AND a newly generated target token in parallel, in the time it would normally take to generate a single token.

## Original Research

Speculative decoding was introduced by Google researchers in ["Fast Inference from Transformers via Speculative Decoding"](https://arxiv.org/abs/2211.17192). The approach guarantees **exact same output quality** as standard autoregressive generation — no approximation or quality loss.

## Gemma 4 MTP Enhancements

Google's Gemma 4 introduces several architectural optimizations:

### Shared Input Embeddings
The draft model shares the input embedding table with the target model, reducing memory overhead.

### Target Activations
The draft model uses activations from the last layer of the target model, concatenates them with token embeddings, and down-projects them to the drafter model's dimension. This gives the drafter better contextual information than training it independently.

### Efficient Embedder (E2B/E4B)
To avoid expensive full-vocabulary logit prediction, the model:
1. Groups similar tokens into clusters
2. Identifies the most likely clusters
3. Restricts final calculations to only tokens within selected clusters

This sparse decoding technique dramatically reduces computation for edge/mobile deployments.

### Shared KV Cache
The drafter shares the target model's key-value cache, eliminating redundant context calculations. The main model has already computed the KV cache for the context window — the drafter reuses it directly.

## Performance Results

| Configuration | Speedup | Notes |
|--------------|---------|-------|
| **Standard Gemma 4** | Baseline | Autoregressive generation |
| **Gemma 4 + MTP** | Up to **3x faster** | All model sizes benefit |
| **Apple Silicon (batch 4-8)** | ~2.2x | 26B MoE model (MLX) |
| **NVIDIA A100 (batch >1)** | ~2-3x | Higher batch = more expert overlap |
| **E2B/E4B on-device** | Significant | Efficient embedder avoids vocab bottleneck |

### MoE-Specific Considerations

For Mixture of Experts models like Gemma 4 26B A4B:
- Each token may activate **different experts**, requiring additional expert weights from memory
- At **higher batch sizes**, more overlap in activated experts across sequences improves weight reuse
- At **batch size 1**, limited overlap means the drafter may not yield speedups without hardware with good parallelism
- This makes MoE speculative decoding particularly well-suited for server/batch inference scenarios

## Supported Frameworks

MTP drafters are available under the **Apache 2.0 license** and supported by:

- **LiteRT-LM** — Edge/mobile deployment
- **MLX** — Apple Silicon optimization
- **Hugging Face Transformers** — Standard inference
- **vLLM / SGLang** — High-throughput serving
- **Ollama** — Local deployment

## Use Cases

- **Real-time chat and voice applications** — Reduced latency improves user experience
- **Agentic workflows** — Faster generation enables more tool-use iterations per unit time
- **Local workstations** — Run 26B MoE and 31B Dense models on consumer GPUs with high speed
- **On-device/mobile** — E2B and E4B drafters preserve battery life on Android/iOS
- **Coding assistants** — Seamless, complex offline coding with reduced latency for obvious continuations

## Relationship to Other Techniques

- **[[concepts/gguf-quantization]]** — Both reduce inference cost; quantization compresses weights, MTP reduces forward passes
- **[[concepts/serving-llms-vllm]]** — vLLM supports MTP drafters for high-throughput serving
- **Continuous batching** — MTP works synergistically with batched inference; higher batches improve MoE expert overlap

## References

- [Google Blog — Accelerating Gemma 4 with MTP](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)
- [Google AI Dev — MTP Overview](https://ai.google.dev/gemma/docs/mtp/overview)
- [Google AI Dev — MTP with Hugging Face](https://ai.google.dev/gemma/docs/mtp/mtp)
- [Ars Technica — Google's Gemma 4 Gets 3x Speed Boost](https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/)
- [Original Paper — Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
