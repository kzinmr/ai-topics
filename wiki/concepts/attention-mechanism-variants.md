---
title: "Attention Mechanism Variants in Modern LLMs"
created: 2026-04-18
updated: 2026-04-18
tags: [architecture, technique, inference, optimization]
aliases: ["attention-mechanisms", "transformer-attention", "GQA", "MLA", "SWA"]
---

# Attention Mechanism Variants

Modern transformer architectures use different attention mechanisms to optimize the trade-off between modeling capacity, compute efficiency, and context length. A prerequisite concept for [[context-engineering]].

## Attention Spectrum

```
MQA (1 shared K/V group) ← GQA ← MHA (1:1 Q:K/V ratio)
```

## 1. Multi-Head Attention (MHA)

Standard transformer attention. Projects input embeddings X into Q, K, V via learned weight matrices. Multiple heads specialize in different relationships (local, semantic, syntactic).

- **Computation:** Q, K, V = X @ Wq, X @ Wk, X @ Wv → Scores = QK^T → A = softmax(Scores) → Z = A @ V
- **Complexity:** O(n²) with sequence length
- **Examples:** GPT-2, OLMo 2 7B, OLMo 3 7B
- **Use case:** Baselines, smaller models where capacity matters more than efficiency

## 2. Grouped-Query Attention (GQA)

Multiple query heads share fewer key-value heads. Reduces KV cache memory/traffic without altering the core decoder recipe.

- **Key insight:** "GQA remains appealing because it is robust, easier to implement, and also easier to train... The sweet spot is usually somewhere in between multi-query attention and MHA"
- **Examples:** Llama 3 8B, Qwen3 4B, Gemma 3 27B, Mistral Small 3.1, Sarvam 30B
- **Use case:** Production, models <100B, simplicity over maximum capacity

## 3. Multi-Head Latent Attention (MLA)

Compresses full-resolution K/V tensors into a latent representation for caching, then reconstructs during inference. Also applied to queries.

- **Trade-off:** Higher implementation/serving complexity than GQA, but preserves modeling quality better at scale
- **Key insight:** "MLA only works well at a certain size. For smaller models, let's say <100B, GQA seems to work better, or, is at least easier to tune and get right."
- **Examples:** DeepSeek V3, Kimi K2, GLM-5, Ling 2.5, Mistral Large 3, Sarvam 105B
- **Use case:** Models >100B, scale-driven efficiency

## 4. Sliding Window Attention (SWA)

Restricts each token's attention to a fixed local window instead of the full prefix. Often interleaved with occasional global layers.

- **Tuning knobs:** Local-to-global layer ratio & window size
  - Gemma 3: 5:1 ratio, 1024-token window
  - Xiaomi: 128-token window (more aggressive)
- **Synergy:** Frequently paired with GQA (SWA reduces context scope, GQA reduces per-token KV state)
- **Examples:** Gemma 3 27B, OLMo 3 32B, Xiaomi MiMo-V2-Flash, Arcee Trinity, Step 3.5 Flash

## 5. DeepSeek Sparse Attention (DSA)

Learned sparse attention pattern (not fixed windows). Two-stage process:
1. **Lightning Indexer:** Computes relevance scores over prior context using MLA's compressed representations
2. **Token Selector:** Keeps a top-k subset of high-scoring past positions

- **Key insight:** "DeepSeek Sparse Attention does not hard-code the sparsity pattern. It learns which past tokens to keep."
- **Examples:** DeepSeek V3.2, GLM-5
- **Status:** Relatively new/complex; adoption lags behind GQA

## 6. Gated Attention

Modified full-attention block for stability in hybrid stacks. Adds:
- Output gate (scales attention result before residual addition)
- Zero-centered QK-Norm (replaces standard RMSNorm)
- Partial RoPE

- **Usage:** Periodically breaks up runs of cheaper sequence modules (e.g., 3:1 pattern with Gated DeltaNet)
- **Examples:** Qwen3-Next, Qwen3.5, Trinity Large

## 7. Hybrid Attention Architectures

Replace most expensive full-attention layers with linear-time/state-space modules, keeping a few heavy layers for exact retrieval. Targets long-context efficiency (128k–1M tokens).

- **Qwen3-Next/3.5:** 3× Gated DeltaNet : 1× Gated Attention
- **Kimi Linear:** 3:1 pattern with channel-wise gating + gated MLA layers
- **Ling 2.5:** Lightning Attention (recurrent linear) + MLA
- **Nemotron 3:** Mamba-2 state-space blocks + sparse MoE + minimal self-attention

## Architecture Selection Matrix

| Variant | Primary Goal | Complexity | Best Use Case |
|---------|-------------|------------|---------------|
| **MHA** | Max modeling capacity | Low | Baselines, smaller models |
| **GQA** | KV cache reduction | Low-Medium | Production, <100B models |
| **MLA** | KV cache compression | High | >100B models, scale-driven efficiency |
| **SWA** | Compute reduction | Low | Long contexts, paired with GQA |
| **DSA** | Learned sparsity | High | Maximum efficiency, large models |
| **Gated** | Hybrid stack stability | Medium | Mixed architectures (DeltaNet + Attention) |
| **Hybrid** | Long-context efficiency | High | 128k–1M token contexts |

## Context Engineering Connection

These attention variants directly impact [[context-engineering]] because:
- **KV cache size** determines how much context fits in memory (SWA, GQA, MLA all reduce cache)
- **Compute scaling** affects context window feasibility (n² for standard attention vs linear for hybrid)
- **Token economics** (see [[token-economics]]) — different attention mechanisms have different CPM profiles
- **Sub-agent architectures** in context engineering rely on efficient attention to keep context windows manageable

## Related

- [[token-economics]] — Cost per million tokens optimization
- [[context-engineering]] — Managing context windows efficiently
- [[context-window-management]] — Context window management patterns
- [[local-llm/_index]] — Local LLM inference considerations
- [[reasoning-models]] — Reasoning models require long context windows

## Sources

- Sebastian Raschka, "A Visual Guide to Attention Variants in Modern LLMs" (Ahead of AI, 2026)
- [[raw/articles/crawl-2026-04-18-token-economics]] — Attention mechanisms analysis
- Anthropic Engineering Blog, "Effective context engineering for AI agents"
- Karpathy, "Software 2.0" and context engineering definition (X/Twitter, June 2025)
