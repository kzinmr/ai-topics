---
title: Diffusion Language Models
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [diffusion, inference, model, llm, autoregressive, code-model, kv-cache, speculative-decoding]
sources:
  - raw/articles/2025-12-01_inceptionlabs_mercury-diffusion-llm.md
  - raw/articles/2026-02-19_togetherai_consistency-diffusion-lms.md
---

# Diffusion Language Models (dLLMs)

Diffusion language models (dLLMs or DLMs) are a class of large language models that generate text through iterative denoising rather than the standard left-to-right, token-by-token autoregressive generation. They represent a paradigm shift in text generation, borrowing the "coarse-to-fine" refinement process that has powered state-of-the-art image, video, and audio models (e.g., Sora, Midjourney, Riffusion) and applying it to discrete text data for the first time at commercial scale.

## How Diffusion LMs Work

Unlike autoregressive models, which generate tokens sequentially and cannot produce token N until all preceding tokens are generated, diffusion LMs operate through an iterative refinement process:

1. **Masked initialization**: Generation begins from a fully masked (or noisy) sequence.
2. **Iterative denoising**: Over N discrete sampling steps, the model progressively unmasks and refines tokens. At each step, a Transformer-based neural network predicts a clean sequence distribution given the current partially-masked state.
3. **Coarse-to-fine refinement**: The output starts as pure noise and is gradually refined — early steps establish the overall structure, and later steps fill in details. Multiple tokens can be modified in parallel at each step.
4. **Confidence-based finalization**: A common deterministic strategy is low-confidence remasking: the model greedily unmasks the highest-confidence tokens while keeping others masked, repeating until the full sequence is revealed.

Because diffusion LMs use bidirectional (non-causal) attention, they can consider the full context at every step — including future positions — unlike autoregressive models restricted to only previous tokens. This enables capabilities such as text infilling, editing, and structured generation.

## Key Models

### Mercury (Inception Labs)
Announced December 2025 by Inception Labs, Mercury is the first commercial-scale diffusion LLM family. Key characteristics:
- **Speed**: Over 1,000 tokens/sec on commodity NVIDIA H100s — a 5-10x speedup over speed-optimized autoregressive models like GPT-4o Mini and Claude 3.5 Haiku.
- **Mercury Coder**: A code generation variant achieving competitive benchmark scores (HumanEval 88.0, MBPP 77.1) while running at 1,109 tok/s on H100s. Available in a public playground.
- **Drop-in replacement**: dLLMs support all standard LLM use cases including RAG, tool use, and agentic workflows. Compatible with existing hardware, datasets, SFT, and RLHF pipelines.
- **Mercury 2** (July 2026): Extended with reasoning capabilities — described as "the first reasoning model fast enough to pick up the phone." Mercury 2 for Search (August 2026) runs hundreds of queries per request.

### Consistency Diffusion LMs (Together AI)
Published February 2026 by Together AI, Consistency Diffusion Language Models (CDLM) address two key inefficiencies of standard DLMs:

1. **KV caching incompatibility**: Standard DLMs use full bidirectional attention, requiring recomputation of O(L²) attention at every denoising step — no standard KV caching possible. CDLM introduces a block-wise causal attention mask that enables exact KV caching for finalized blocks.
2. **High step counts**: CDLM reduces refinement steps by 4.1x-7.7x through a post-training recipe combining:
   - **Distillation loss**: Matching student predictions to teacher distributions at block-completion points.
   - **Consistency loss**: Enforcing within-block temporal consistency (stop-gradient target).
   - **Auxiliary masked-denoising loss**: Preserving general masked-token prediction capability.

Results: Up to 14.5x latency speedups on coding and math tasks (11.2x on GSM8K-CoT, 14.5x on MBPP-Instruct) without significant accuracy degradation. CDLM is a post-training recipe applicable to any block-diffusion model.

### Other Notable dLLMs
- **LLaDA** (InclusionAI): Diffusion language model scaled to 100B parameters (LLaDA 2.0).
- **Block Diffusion**: Interpolating between autoregressive and diffusion language models — a hybrid approach enabling exact KV caching within blocks while maintaining diffusion-style generation.
- **DiffusionGemma**: A diffusion-based variant of Google's Gemma architecture.
- **Fast-DLLM**: A training-free acceleration technique for diffusion LLMs enabling KV cache and parallel decoding (February 2025, 70 HN points).
- **Introspective Diffusion LMs**: A variant emphasizing self-reflection and error correction during the denoising process (281 HN points).
- **Seed** (ByteDance): A diffusion-based language model from ByteDance.

## Advantages vs. Autoregressive Models

| Dimension | Diffusion LMs | Autoregressive LMs |
|---|---|---|
| **Speed** | 5-14x faster; 1,000+ tok/s on H100s | Typically 50-200 tok/s |
| **Generation pattern** | Iterative denoising, multiple tokens in parallel | Sequential, one token at a time |
| **Context access** | Bidirectional — full context at every step | Causal — only previous tokens |
| **Error correction** | Can revise earlier tokens during refinement | Cannot revise once generated |
| **Editing/infilling** | Natural fit — can modify any position | Requires special handling |
| **Reasoning** | Not constrained to left-to-right; can plan globally before committing | Must reason sequentially; long traces increase latency |
| **Latency for long outputs** | Steps decoupled from generation length | Latency scales linearly with output length |
| **Hardware efficiency** | Higher arithmetic intensity; can be compute-bound at small batch sizes | Memory-bound at small batch sizes |

Key insight from Inception Labs: the speed advantage means applications previously constrained to smaller, less capable models for latency reasons can now use larger, more capable dLLMs while meeting the same cost and speed requirements.

## Limitations

- **Quality vs. step count**: Naively reducing denoising steps degrades quality sharply. CDLM's post-training approach mitigates this, but step reduction requires deliberate training.
- **KV caching complexity**: Full bidirectional attention precludes standard KV caching; block-wise causal masking (CDLM approach) is an effective workaround but trades some expressiveness.
- **Maturity**: Diffusion LMs are newer than autoregressive models; the ecosystem of fine-tuning techniques, inference optimizations, and production tooling is less mature.
- **Commercial availability**: As of mid-2026, commercial dLLM offerings are limited primarily to Inception Labs (Mercury API and on-premise) with Together AI's CDLM as a research/open approach.
- **Scaling trajectory**: While LLaDA has reached 100B parameters, the scaling behavior of diffusion LMs relative to autoregressive models at frontier sizes is still being explored.

## Related Pages

- [[concepts/inference]] — LLM inference engine comparison and architecture
- [[concepts/kv-cache]] — Key-Value caching in Transformer inference; central to CDLM's block-wise caching innovation
- [[concepts/speculative-decoding]] — Alternative approach to accelerating LLM inference via draft models
- [[concepts/llm-training-fundamentals]] — Training fundamentals relevant to understanding dLLM training objectives
- [[entities/together-ai]] — Publisher of CDLM research and consistency diffusion approach
