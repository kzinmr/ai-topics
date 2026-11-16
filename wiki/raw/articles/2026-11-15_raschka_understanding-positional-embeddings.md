---
title: "Understanding Positional Embeddings in Modern LLMs (Sebastian Raschka)"
url: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings
date: 2026-11-15
fetched_at: 2026-11-16T11:10:00Z
source: active-crawl
status: raw
tags: [education, transformer, rope, training]
---

# Understanding Positional Embeddings in Modern LLMs

The Methods Behind How LLMs Represent Token Positions — Sebastian Raschka, PhD, Nov 15, 2026 (AI Messages Substack). HN 228 points / 27 comments (item 50512xxx surfaced 2026-11-15).

This article explains how LLMs encode and process token position information by covering classic and contemporary methods like RoPE, with visual examples, math, and a small PyTorch implementation, then looks at how modern architectures adapt or omit explicit positional encodings.

Written as a standalone building block ahead of Raschka's upcoming LLM architecture/trends analysis article; the requested RoPE tutorial follow-up to his learned-absolute-embeddings GPT material. Assumes familiarity with self-attention (Q/K/V).

## 1. Where position information enters an LLM

- Tokenizer → token IDs → input token embedding layer → transformer blocks → output logits.
- GPT-2 adds a position vector to each token embedding *before* the first transformer block; MiniMax-M3 (and most 2026 LLMs) add positional information *inside each attention block* via RoPE.
- Why position at all: "The red fox jumps over the gray fox" vs "The gray fox jumps over the red fox" — same token IDs, same embeddings, so an attention layer without position info (and without a causal mask) is permutation-invariant.
- The causal mask itself gives *implicit* order information (a causal LLM can already distinguish the two fox sentences — foreshadowing the NoPE concept), but the mask does not distinguish a separation of one position from ten, so explicit positional methods remain useful or essential.

## 2. Adding a position vector to each token embedding

### 2.1 Learned absolute position embeddings (GPT-2)
- GPT-2 learns a table of position vectors, same dimensions as token embeddings, added element-wise before the first block (`x = tok_embeds + pos_embeds`).
- GPT-2 shipped 1,024 learned position vectors → context length fixed before training; extending context is expensive: at 1,024 positions the positional table is 0.30% of GPT-2 Medium weights, but at a modern ~100k context it would exceed 22% of total weights — very uneconomic.

### 2.2 Fixed sinusoidal encodings (original Transformer, 2017)
- Same addition mechanism but position vectors computed with fixed sine/cosine functions; added before both encoder and decoder stacks. The sinusoids reappear later as the basis of RoPE.

## RoPE (relative positional embeddings)

- RoPE encodes relative position inside attention by rotating query and key vectors; the rotation is built from the same sinusoid family as the 2017 sinusoidal encodings. Attention scores then depend on relative distance rather than absolute position, giving natural distance decay.
- Partial RoPE (rotating only a subset of query/key features) became the majority of RoPE models in 2026 gallery entries vs a minority in 2025. Commenter note (Nan Deng): partial RoPE shrinks the cos/sin tables but the KV cache still stores the full key, so the memory win is small — the quality rationale is unclear, possibly implementation carryover.

## 6. Positional choices in modern architectures (gallery survey)

Raschka grouped his LLM Architecture Gallery entries by release date (2025 vs early-2026 vs late-2026 snapshots):

- **RoPE in every softmax attention layer is still the most common choice**, but its share fell from 2025 to 2026 and again in late 2026 — a possible trend.
- A growing number of models **mix RoPE and NoPE** (omit explicit positional encoding in some layers). Groups still small.
- "NoPE only" entries were all recurrent hybrids with softmax attention layers using no explicit positional encoding.
- "Other": xLSTM 7B (2025; no softmax attention layers) and **Inkling (2026)** — Inkling adds a **learned, query-conditioned relative position bias to attention scores before softmax**, reviving a T5 idea (see Thinking Machines' Inkling architecture description).
- Among RoPE users, **partial RoPE became a majority in both 2026 groups** (was a minority in 2025).

## 7. Final thoughts

- GPT-2/original Transformer add a position vector before the blocks; modern LLMs switched to RoPE (relative position by rotating Q/K). RoPE remains the predominant method and Raschka expects it to carry into 2027.
- Inkling's T5-style learned relative bias is the notable new entrant; he expects possibly more Inkling-like designs in 2027.
- Recommended learning path: start from a GPT-2-style model (Build a LLM From Scratch), then layer on RoPE and other methods; companion explainers cover self-attention, attention variants (GQA/MLA/SWA/sparse), KV cache, SwiGLU/norms, MoE routing, mHC hyper-connections, and Qwen3 from scratch.
