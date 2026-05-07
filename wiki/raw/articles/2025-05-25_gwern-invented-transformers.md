---
title: "You Could've Invented Transformers"
source: "https://gwern.net/blog/2025/you-could-have-invented-transformers"
author: "Gwern Branwen"
date: 2025-05-25
type: raw-article
tags: [transformer, pedagogy, architecture, self-attention, gwern]
---

# "You Could've Invented Transformers", by Gwern (2025-05-25)

## Overview

This is a **proposal** for a pedagogical "discovery fiction" tutorial, not a full tutorial itself. Gwern outlines a logical recreation of the Transformer architecture from first principles — showing how one could arrive at Transformers by solving concrete problems in sequence prediction, step by step, without following the messy historical trial-and-error.

The core thesis: **self-attention functions mostly as a way to 'propagate' multiplicative interactions around a large input sequence/history, providing 'direct access' for the MLPs to compute on** — as opposed to the hidden-state bottleneck of RNNs.

## The Logical Progression

The proposed "discovery fiction" tutorial structure:

### Step 1: N-grams and the 0-Count Problem
- Classic n-grams on Tiny Shakespeare
- Cannot estimate rare/unseen combinations (curse of dimensionality)
- Smoothing (Laplace, Good-Turing) is inadequate

### Step 2: Word Embeddings (Dense Vectors)
- Cluster "similar" words via dense vectors
- Share statistical strength across semantically similar words
- "king" ≈ "queen" enables generalizing "the queen spoke" from seeing "the king spoke"

### Step 3: Learned End-to-End Embeddings (Bengio 2003)
- word2vec-style embeddings not optimized for sequence prediction
- Learn embeddings as part of the prediction model (Bengio's 2003 neural LM)
- Fixed-size sliding window over the sequence

### Step 4: The Context Bottleneck
- Words are extremely contextual ("river bank" ≠ "investment bank")
- Bigger windows cause combinatorial parameter explosion
- Unique weights per position don't scale

### Step 5: Convolutions (Shared Weights)
- Shared weights slide across windows → pattern detection anywhere
- Depth-wise 1-D convolutions with kernel size k
- Dilated convolutions (WaveNet) grow effective window exponentially
- **Problem: internal forgetting** — signals must pass through many layers, making it hard to track pronouns or long-range dependencies

### Step 6: MLP-Mixer (Global Context)
- Every token directly "aware" of every other token
- Token-mixing MLPs (interaction across sequence) + Channel-mixing MLPs (across features)
- **Problem: frozen weights** — interactions are fixed after training, not input-dependent

### Step 7: Dynamic Convolutions
- Weights vary based on the input tokens themselves
- Context-dependent local filtering
- **Bridge to attention**: what if mixing weights were determined by pairwise token compatibility?

### Step 8: QKV Self-Attention (The Core Innovation)
- **"The single trickiest step"**: going from dynamic convolutions to QKV self-attention
- Each token computes its own mixing weights for every other token
- Determined by query-key relevance
- Direct access for MLPs to compute on specific parts of input history
- "Hard" attention first (REINFORCE/CMA-ES), then generalize to "soft" (quadratic) attention

### Step 9: Multi-Head Attention
- Scale to multiple heads for specialization
- Different heads focus on different linguistic/structural features (syntax vs semantics)

### Step 10: Positional Embeddings
- Self-attention is permutation-invariant (treats input as a set)
- Need to break symmetry → positional encodings
- Simple index → sinusoidal → RoPE (Rotary Position Embedding)

### Step 11: Optimization "Doodads"
- Residual Layers (ResNets) for vanishing gradients
- Layer Normalization for training stability
- Dropout, Decoupled Weight Decay, Bottlenecks
- Empirically chosen via neural architecture search

## Emergence at Scale

Properties that only emerge at billions of parameters + internet-scale data:
- **Induction Heads**: specific circuits for pattern completion
- **In-Context Learning**: ability to learn from prompts during inference
- **Meta-Learning**: attention mechanisms perform a form of meta-descent

## Key Insight: Multiplicative Interactions

> "The Transformer is not 'magic' but a 'fancier MLP' optimized for token-mixing."

Self-attention = **propagating multiplicative interactions** across a sequence. This is what distinguishes it from:
- RNNs: hidden-state bottleneck, hard to learn what to propagate
- Convolutions: indirect signaling, information must survive many layers
- MLP-Mixers: fixed weights, no dynamic adaptation

## Connection to Other Architectures

This framework also helps categorize newer models:
- **SSMs (State-Space Models)** and **Linear Transformers** can be viewed as alternative solutions to the same architectural problems
- Often functionally equivalent to "fast weight programmers"
- Can be understood as moving back and forth along the evolutionary steps

## Footnote

> "Our interest does not fall back upon these causes of the formation of concepts; we are not doing natural science; nor yet natural history—since we can also invent fictitious natural history for our purpose" — Wittgenstein, quoted by Gwern

## Related Content on gwern.net

- [The Scaling Hypothesis](https://gwern.net/Scaling-hypothesis) — Gwern's analysis of scale-driven AI capability emergence
- [Induction Heads](https://gwern.net/ind) — A key emergent mechanism in Transformers
