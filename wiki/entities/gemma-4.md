---
title: Gemma 4
created: 2026-05-11
updated: 2026-05-11
type: entity
tags: [google, model, open-source, optimization, inference]
sources: [raw/articles/2026-05-05_google_gemma-4-mtp.md]
---

# Gemma 4

Google's family of open-weight models, part of the Gemma series. Launched April 2026. Downloaded over 60 million times in its first month.

## Multi-Token Prediction (MTP) Drafters

Released May 5, 2026. Google added MTP drafters to Gemma 4 for **up to 3x faster inference** with no degradation in output quality or reasoning logic.

### How It Works
MTP uses a lightweight "drafter" model that proposes multiple tokens simultaneously. The main Gemma 4 model verifies these proposals — a form of [[speculative-decoding]] optimized for the Gemma architecture. This reduces the number of sequential inference steps needed while maintaining full output fidelity.

### Impact
- Faster inference on both cloud and local deployments
- No quality trade-off — identical outputs to standard decoding
- Benefits all downstream use cases: chat, code generation, RAG, agent workflows

## Context
Gemma 4 competes in the open-weight model space against Meta's Llama 4, Mistral 3, and Qwen models. Google positions it as developer-friendly with strong ecosystem integration (HuggingFace, Ollama, llama.cpp).

## Related Pages
- [[entities/google]] — Google's AI strategy
- [[concepts/speculative-decoding]] — Multi-token prediction technique
- [[concepts/model-optimization]] — Inference optimization approaches
- [[entities/gemma]] — Gemma model family overview
- [[comparisons/open-weight-models]] — Open model landscape comparison
