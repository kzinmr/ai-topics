---
title: MiniMax Sparse Attention (MSA)
created: 2026-05-29
updated: 2026-05-29
type: concept
tags: [concept, architecture, inference, optimization, long-context, model, china]
sources: [raw/articles/2026-05-27_minimax-m3-sparse-attention.md]
---

# MiniMax Sparse Attention (MSA)

MiniMax Sparse Attention (MSA) is a novel sub-quadratic attention mechanism designed by [[entities/minimax|MiniMax]] for its upcoming M3 model series. MSA achieves **9.7x faster prefilling** and **15.6x faster decoding** at 1-million-token sequence lengths compared to full-attention architectures, making ultra-long-context AI agent deployment economically viable.

## Motivation

MiniMax's M2 series used strict quadratic (full) attention across all 62 layers. While this preserved multi-hop reasoning quality, it created a growing computational bottleneck at long contexts. The team had tested sub-quadratic alternatives (Sliding Window Attention, Lightning Attention) but found they severely degraded multi-hop reasoning — e.g., on RULER 128K complex word extraction, an SWA variant fell from 90.0 to 72.0. MSA was designed to deliver speed without this intelligence compromise.

## How MSA Works

MSA is built on a **standard Grouped Query Attention (GQA) backbone** with three key innovations:

1. **Block-level selection** on real, uncompressed Key-Value pairs — unlike [[concepts/deepseek-mla|DeepSeek's Multi-head Latent Attention (MLA)]] which compresses KVs into a low-dimensional latent space
2. **Dynamic filtering** that selects block-level sequences based on relevance
3. **Standard attention computation** on the selected blocks — preserving the fidelity of full attention

This design solves the precision loss and prefix-caching obstacles identified in the M2 technical report, while maintaining compatibility with existing inference infrastructure.

## Comparison with Other Sub-Quadratic Approaches

| Mechanism | Approach | Key Trade-off |
|-----------|----------|---------------|
| **MSA (MiniMax)** | Block selection on real KVs | Balances speed and precision |
| **MLA (DeepSeek)** | Latent KV compression | Smaller KV cache, potential precision loss |
| **Sliding Window** | Fixed local window | Fast but loses long-range dependencies |
| **Lightning Attention** | Linear attention approximation | Fast but lower quality on complex reasoning |

## Performance

- **Prefilling**: 9.7x faster than full-attention M2
- **Decoding at 1M tokens**: 15.6x faster
- Enables economically viable deployment of agents requiring million-token contexts

## Context: M2 Series Foundation

MSA builds on lessons from the M2 series (229.9B total params, 9.8B active per token, 256 fine-grained experts with sigmoid gating). M2 achieved [[concepts/swe-bench-pro|SWE-Bench Pro]] scores of 56-59 and demonstrated self-evolving agent capabilities via the **Forge** RL training system.

## Related Pages

- [[entities/minimax]] — MiniMax company overview
- [[concepts/deepseek-mla]] — DeepSeek's Multi-head Latent Attention
- [[concepts/long-context]] — Long context handling in LLMs
- [[concepts/kv-cache]] — KV cache optimization
- [[concepts/swe-bench-pro]] — SWE-Bench Pro benchmark
