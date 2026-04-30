---
title: "SID-1 Technical Report: Test-Time Compute for Retrieval"
source: "https://www.sid.ai/research/sid-1-technical-report"
authors:
  - SID Research
date: 2025-12-04
---

# SID-1 Technical Report: Test-Time Compute for Retrieval

**Source:** https://www.sid.ai/research/sid-1-technical-report
**Date:** December 4, 2025

SID-1 is the first model trained end-to-end via reinforcement learning (RL) specifically for **agentic retrieval**. Unlike traditional single-step pipelines (vector search + reranking), SID-1 iteratively uses search tools to reason over results.

## Key Metrics

| Model | Recall | Latency (s) | Cost (USD/Q) |
|-------|--------|-------------|--------------|
| **SID-1 (4x)** | **0.84** | 5.5s | $0.0014 |
| GPT-5.1 (high) | 0.78 | 131s | $0.24 |
| Gemini 3 Pro | 0.66 | 156s | $0.12 |
| Sonnet 4.5 | 0.64 | 35s | $0.54 |
| Reranker @10 | 0.45 | 0.78s | $0.00061 |

## Technical Details

- **Base model**: Qwen3-14B
- **Training**: Modified GRPO, no SFT
- **Reward**: Document-centric NDCG (not answer-centric)
- **Training stability**: Tokens-In/Tokens-Out (TI/TO) pipeline — standard message abstractions cause model collapse
- **Length bias fix**: Length scheduling + soft length penalty

## Key Features

- Parallel tool use (naturally emerged)
- Hierarchical retrieval with `read` tool
- Reciprocal Rank Fusion (RRF) for 4x parallel rollouts

## Impact

24x faster than GPT-5.1, 374x lower cost than Sonnet 4.5, with near-doubled recall vs traditional reranking pipelines.
