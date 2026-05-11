---
title: "KV Caching in LLMs, Explained Visually"
source: https://blog.dailydoseofds.com/p/kv-caching-in-llms-explained-visually
author: Avi Chawla
date: 2025-02-14
scraped: 2026-05-11
tags: [kv-cache, inference, optimization, transformer]
x_article_id: 2034896077460316163
x_author: "@_avichawla"
type: raw_article
---

# KV Caching in LLMs, Explained Visually

**Author:** Avi Chawla
**Date:** February 14, 2025

KV caching is a popular technique to speed up LLM inference. With KV caching: ~9 seconds. Without: ~40 seconds (~4.5x slower, and the gap widens as more tokens are produced).

## How It Works

To understand KV caching, we must know how LLMs output tokens:
1. Transformer produces hidden states for all tokens
2. Hidden states are projected to vocab space
3. Logits of the last token is used to generate the next token
4. Repeat for subsequent tokens

Thus, to generate a new token, **we only need the hidden state of the most recent token**. None of the other hidden states are required.

## The Key Insight

During attention computation:
- Only the last token's query vector is needed
- All key & value vectors are needed
- As we generate new tokens, the KV vectors for ALL previous tokens do NOT change

Therefore: instead of redundantly computing KV vectors of all context tokens, CACHE them. To generate a token:
1. Generate QKV vector for the token generated one step before
2. Get all other KV vectors from the cache
3. Compute attention
4. Store the newly generated KV values in the cache

## Why First Token Is Slow

This is why ChatGPT takes some time to generate the first token — during that pause, the KV cache of the prompt is computed. Subsequent tokens stream almost instantly.

## Memory Cost

KV cache takes significant memory. Llama3-70B (80 layers, 8k hidden size, 4k max output):
- Every token takes ~2.5 MB in the KV cache
- 4k tokens will take up 10.5 GB
- More users → more memory
