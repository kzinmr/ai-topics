---
title: "Transformer Architecture"
type: concept
aliases:
  - transformer-architecture
  - decoder-only-transformer
  - attention-is-all-you-need
created: 2026-04-25
updated: 2026-05-07
tags:
  - concept
  - architecture
  - attention
  - sequence-modeling
sources:
  - raw/articles/2025-05-25_gwern-invented-transformers.md
---

# Transformer Architecture

> **Core Insight**: The Transformer is not "magic" but a "fancier MLP" optimized for token-mixing. Self-attention functions as a way to **propagate multiplicative interactions** across a sequence, providing "direct access" for the MLPs to compute on — as opposed to the hidden-state bottleneck of RNNs or fixed weights of MLP-Mixers.

## Overview

The Transformer architecture (Vaswani et al., 2017, "Attention Is All You Need") is a sequence-to-sequence model that replaced recurrence and convolutions entirely with **self-attention mechanisms**. It was discovered through extensive trial-and-error at Google, but can be understood as a **logical evolution** of sequence prediction models, each step solving a concrete limitation of its predecessor.

This page documents both the canonical architecture and a pedagogical "discovery fiction" — how one could logically re-invent Transformers from first principles ([Gwern, 2025](https://gwern.net/blog/2025/you-could-have-invented-transformers)).

## The "Discovery Fiction": A Logical Derivation

The following progression shows how each limitation in sequence modeling motivates the next architectural innovation, culminating in the modern Transformer.

### 1. N-grams → The Sparsity Problem

| Limitation | Solution |
|---|---|
| N-grams cannot estimate rare/unseen word combinations | Embeddings (dense vectors) share statistical strength across similar words |

Classic n-grams on a dataset like Tiny Shakespeare fail on the **0-count problem**: unseen word combinations have zero probability. Smoothing (Laplace, Good-Turing) is inadequate against the **curse of dimensionality** — requiring independent estimates for each combination.

### 2. Embeddings → Fixed-Window Bottleneck

| Limitation | Solution |
|---|---|
| Fixed-size windows cannot handle contextuality | Shared weights (convolutions) enable pattern detection anywhere |

Word embeddings cluster "king" ≈ "queen" so that seeing "the queen spoke" benefits from having seen "the king spoke." However, **fixed-size sliding windows** require a unique weight for each position: windows of 3 words work, but 10 words cause combinatorial parameter explosion. Words are highly contextual ("river bank" ≠ "investment bank").

### 3. Convolutions → Internal Forgetting

| Limitation | Solution |
|---|---|
| Signals must pass through many layers; information "forgotten" internally | Global mixing (MLP-Mixer) makes every token aware of every other |

Depth-wise 1-D convolutions with shared weights let the same pattern detector (e.g., "adjective noun") fire anywhere. **Dilated convolutions** (WaveNet) grow the effective receptive field exponentially per layer. But information must survive multiple layers to propagate from start to end of a long sequence — making it hard to track pronouns or pluralization.

### 4. MLP-Mixer → Frozen Weights

| Limitation | Solution |
|---|---|
| Token-mixing weights are fixed after training | Dynamic convolutions make weights input-dependent |

MLP-Mixer uses **token-mixing MLPs** (interaction across the sequence) and **channel-mixing MLPs** (across features) for global context fusion. However, the interaction weights are learned and frozen — they cannot adapt based on which tokens are present.

### 5. Dynamic Convolutions → Local Context Only

| Limitation | Solution |
|---|---|
| Weights adapt but only within a local filter window | Self-attention (QKV) enables global, dynamic, context-aware mixing |

Dynamic convolutions change their weights based on input tokens, but only within a small local region. The key leap: **what if each token computed mixing weights for every other token, determined by pairwise relevance?**

### 6. QKV Self-Attention (THE Core Innovation)

This is the fundamental architectural insight. Instead of fixed mixing weights from MLP-Mixer or local dynamic weights from convolutions:

- Each token generates a **Query**, **Key**, and **Value** vector
- Its mixing weight for every other token = compatibility of its Q with that token's K
- Output = weighted sum of all tokens' V vectors
- **Result**: the network can learn *which* parts of the input history matter for the current prediction, and directly access them

> Why does this work so well? Self-attention lets information propagate via multiplicative interactions with **direct access** — bypassing the indirect signaling of convolutions and the narrow bottleneck of RNN hidden states.

### 7. Multi-Head Attention

Multiple attention heads run in parallel, enabling specialization:
- One head learns syntax (e.g., subject-verb agreement)
- Another learns semantics (e.g., word sense disambiguation)
- Others track positional patterns

### 8. Positional Embeddings

Self-attention is **permutation-invariant** — it treats input as a set. To restore order:
- Simple index encoding → sinusoidal positional encodings → **RoPE** (Rotary Position Embedding)
- RoPE encodes relative position via rotation matrices, naturally decaying attention for distant tokens

### 9. Optimization Components

The architectural "doodads" added for training stability (empirically selected via search):
- **Residual connections** (skip connections) for vanishing gradient mitigation
- **Layer Normalization** for stable training dynamics
- **Dropout** for regularization
- **Decoupled Weight Decay** for improved generalization

## Emergence at Scale

Certain properties only appear at billions of parameters + internet-scale data:

- **Induction Heads**: Specific circuits for pattern matching and completion — the mechanism behind in-context learning
- **In-Context Learning**: The ability to learn from prompt examples during inference, without gradient updates
- **Meta-Learning**: Attention mechanisms performing a form of meta-descent

Gwern's **Scaling Hypothesis** (see [[concepts/scaling-hypothesis]]) predicts that these emergent properties are not architectural bugs but consequences of training large Transformers on diverse data — the model's learned representations naturally converge toward general reasoning capabilities.

## Architectural Variants

See [[concepts/attention-mechanism-variants]] for a detailed comparison of:

| Variant | Primary Change | Motivation |
|---------|---------------|------------|
| **MHA** | Standard multi-head | Max capacity |
| **GQA** | Fewer KV heads than query heads | KV cache reduction |
| **MLA** | Latent KV compression | Scale efficiency (>100B) |
| **SWA** | Local windowed attention | Compute reduction |
| **Hybrid** | Mix attention + SSM layers | Long-context efficiency (128K–1M) |

## Connection to Newer Architectures

Gwern's logical derivation framework also helps categorize post-Transformer models:

- **SSMs (Mamba, Mamba-2)** and **Linear Transformers** can be seen as alternative solutions to the same sequence-modeling problems
- Many are functionally equivalent to **"fast weight programmers"** — architectures that learn to generate their own weights based on input
- Hybrid architectures (e.g., Qwen3-Next) move back and forth along the evolutionary steps, keeping expensive full-attention layers for exact retrieval while replacing others with linear-time alternatives

## Related Pages

- [[concepts/attention-mechanism-variants]] — Detailed comparison of attention variants (GQA, MLA, SWA, hybrid)
- [[concepts/scaling-hypothesis]] — Gwern's theory that scale alone drives capability emergence
- [[concepts/ssm-mamba]] — State-space models as an alternative to attention
- [[concepts/decoder-only-gpt]] — The decoder-only variant used by GPT models
- [[concepts/context-engineering]] — Managing context windows built on attention mechanisms
- [[concepts/token-economics]] — How attention compute scales with token count
- [[entities/gwern]] — Gwern Branwen, author of the "discovery fiction" derivation
- [[entities/jay-mody]] — Jay Mody's picoGPT and attention derivations

## Sources

- Vaswani et al., "Attention Is All You Need" (NeurIPS 2017) — Original Transformer paper
- [Gwern, "You Could've Invented Transformers"](https://gwern.net/blog/2025/you-could-have-invented-transformers) (2025-05-25) — Pedagogical "discovery fiction" derivation
- [Jay Mody, "Attention Intuition"](https://jaykmody.com/blog/attention-intuition/) — First-principles attention explanation
- Sebastian Raschka, "A Visual Guide to Attention Variants in Modern LLMs" (Ahead of AI, 2026)
