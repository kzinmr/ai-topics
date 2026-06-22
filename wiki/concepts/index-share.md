---
title: IndexShare
type: concept
created: 2026-06-17
updated: 2026-06-17
tags:
  - inference
  - model
  - context-management
aliases: []
sources:
  - raw/articles/2026-06-17_ainews_glm-52-indexshare.md
---

# IndexShare

IndexShare is a novel technique introduced by Z.ai in [[entities/glm-5-zai|GLM-5.2]] that extends DeepSeek Sparse Attention to improve efficiency at ultra-long contexts.

## Overview

First deployed in GLM-5.2 (June 2026), IndexShare reuses one indexer across every four sparse layers, dramatically reducing the computational overhead of sparse attention at long context windows while maintaining or improving model quality.

## How It Works

DeepSeek Sparse Attention works by selecting a subset of key-value positions to attend to rather than attending to all tokens in a sequence. IndexShare modifies this by sharing a single indexing mechanism across multiple sparse attention layers:

- **Shared indexer:** One indexer component is reused across groups of four sparse layers
- **Efficiency gain:** Reduces the cost of computing sparse attention indices at ultra-long contexts (1M+ tokens)
- **Quality preservation:** The shared indexing maintains attention quality by reusing well-calibrated index patterns

## Benefits

- **Lower inference cost** at long context lengths
- **Improved throughput** for 1M-token context windows
- **Enables practical deployment** of sparse attention at scale

## Relationship to Speculative Decoding

IndexShare is paired with an improved MTP (multi-token prediction) mechanism in GLM-5.2 for speculative decoding. While IndexShare optimizes the attention mechanism itself (reducing per-token compute), MTP accelerates generation by predicting multiple tokens at once. Together they form a comprehensive inference optimization stack.

## Related

- [[entities/glm-5-zai]] — GLM-5.2, the model that debuted IndexShare
- [[concepts/speculative-decoding]] — Broader speculative decoding techniques including MTP
- [[concepts/deepseek-r1]] — DeepSeek's sparse attention architecture which IndexShare extends
