---
title: "Gemma 4 - Drafter Explained"
source: "x-bookmarks"
author: "Google Gemma (@googlegemma)"
date: "2026-05-05"
url: "https://x.com/i/article/2049591001967443968"
tweet_id: "2051694045869879749"
bookmarks: 823
likes: 915
retweets: 129
---

# Gemma 4 - Drafter Explained

Google Gemma Team, May 5, 2026. X/Twitter long-form article.

This article explains Multi-Token Prediction (MTP) drafters for Gemma 4 — a specialized architecture that accelerates inference through speculative decoding while maintaining output quality.

## Key Technical Details

### Speculative Decoding with MTP

Standard LLMs generate text autoregressively — one token at a time. This is memory-bandwidth bound: processors spend more time moving parameters from VRAM than computing. MTP solves this by:

1. **Decoupling Generation from Verification:** A lightweight "drafter" model suggests a sequence of tokens ahead
2. **Parallel Verification:** The large "target" model verifies the entire sequence in a single forward pass
3. **Bonus Token:** If the target agrees with the draft, it accepts the full sequence and generates one additional token simultaneously
4. **Shared Resources:** Drafters utilize the target model's activations and share its KV cache

### Drafter Architecture

- **Shared Input Embeddings:** Draft model shares the input embedding table with the target model
- **Target Activations:** Uses activations from the last layer of the target model, concatenated with token embeddings, down-projected to drafter dimensions
- **Efficient Embedder (E2B/E4B only):** Groups similar tokens into clusters, identifies likely clusters, restricts final calculations to those clusters — avoids expensive full-vocabulary prediction

### Performance Gains

- **Up to 3x faster inference** compared to standard autoregressive generation
- **Zero degradation** in output quality, reasoning, or accuracy
- **Apple Silicon (batch sizes 4-8):** ~2.2x speedup for 26B MoE model
- **NVIDIA A100:** Similar gains at higher batch sizes
- **Edge Devices:** Faster generation on E2B/E4B preserves battery life on Android/iOS

### MoE-Specific Considerations

Gemma 4 26B A4B (Mixture of Experts) works differently from dense models:
- Each token may activate different experts, requiring additional expert weights from memory
- At higher batch sizes, more overlap in activated experts across sequences improves reuse
- At batch size 1, limited overlap means the drafter may not yield speedups without good parallelism hardware

### Availability

- **License:** Apache 2.0
- **Supported Frameworks:** LiteRT-LM (Edge/Mobile), MLX (Apple Silicon), Hugging Face Transformers, vLLM, SGLang, Ollama
- **Weights:** Available on Hugging Face and Kaggle
