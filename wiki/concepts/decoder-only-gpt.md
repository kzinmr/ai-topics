---
title: "Decoder-Only GPT Architecture"
tags: [- llm]
created: 2026-04-13
updated: 2026-04-24
type: concept
---

# Decoder-Only GPT Architecture

## Overview

The **decoder-only GPT** (Generative Pre-trained Transformer) is the dominant architecture behind modern large language models (ChatGPT, Claude, Gemini, etc.). Andrej Karpathy's **microgpt** project (February 2026) demonstrates that the complete algorithmic content of a GPT fits in approximately **200 lines of pure Python with zero dependencies** — making the architecture fundamentally simple to understand, even if engineering-scale implementations are complex.

This concept page synthesizes Karpathy's intuitive explanation of *how GPT works* and *why it works*.

---

## Core Architecture (from microgpt)

### The GPT Function

At its heart, a decoder-only GPT is a **stateless function** that processes one token at a time:

```
gpt(token_id, pos_id, keys, values) → logits → softmax → next_token
```

The entire model consists of these components stacked together:

| Component | Purpose | microgpt Implementation |
|-----------|---------|------------------------|
| **Token Embedding** | Converts token ID to a 27-dimensional vector (26 letters + BOS) | `tok_emb[token_id]` |
| **Positional Embedding** | Encodes position information (no attention = no inherent order) | `pos_emb[pos_id]` |
| **RMSNorm** | Normalizes activations (simpler than LayerNorm, no bias needed) | `rmsnorm(x)` |
| **Self-Attention** | Token-to-token communication mechanism | Multi-head QKV projections + scaled dot-product |
| **MLP (Feed-Forward)** | Where the model does its "thinking" per position | 2-layer FFN: expand 4× → ReLU → contract |
| **Residual Connections** | Stabilize gradient flow through deep networks | Added around Attention and MLP blocks |
| **LM Head** | Projects final hidden state to vocabulary logits | Linear projection to 27 dimensions |

### The Complete Pipeline

```
Input: [BOS, 'e', 'm', 'm', 'a']
        ↓
Token Embedding + Positional Embedding
        ↓
[RMSNorm → Self-Attention → Residual] × N layers
        ↓
[RMSNorm → MLP → Residual] × N layers
        ↓
LM Head → Logits → Softmax → Next Token Prediction
```

---

## Why GPT Works: Intuitive Explanations

### 1. Next-Token Prediction Is Surprisingly Powerful

The core training objective is deceptively simple:

> **Given a sequence of tokens, predict the next token.**

Karpathy's microgpt demonstrates this with names. The model sees:
```
[BOS, 'e', 'm', 'm', 'a'] → predict [BOS] (end of "emma")
[BOS, 'j', 'o', 'h', 'n'] → predict [BOS] (end of "john")
```

Over 1,000 training iterations, the loss drops from **~3.3** (random guessing across 27 tokens) to **~2.37** (meaningful pattern learning). The model learns:
- Which letters follow which letters
- Common name patterns (suffixes like "-son", "-ton")
- Where names typically end

**Key insight:** *Next-token prediction, when scaled up, implicitly learns grammar, facts, reasoning patterns, and world knowledge.* The model doesn't need to be explicitly taught these — they emerge from the statistics of language.

### 2. Attention Is Token Communication

Karpathy's framing: **"Attention is a token communication mechanism."**

In self-attention, each token can "talk to" every other token in the sequence:

```
Query (Q): "What am I looking for?"     ← from current token
Key (K):    "What do I have to offer?"   ← from other tokens
Value (V):  "Here's my actual content"   ← from other tokens
```

The attention score is computed as:
```
attention(Q, K) = softmax(Q · K / √d_k)
```

This creates a **weighted sum of values** where weights depend on how relevant each token is to the current one. In practice:
- "emma" attends heavily to "BOS" (sequence start)
- Position-specific patterns emerge naturally
- No explicit grammar rules needed — they're learned from data

### 3. The MLP Is Where "Thinking" Happens

While attention handles *communication* between tokens, the MLP (Multi-Layer Perceptron) handles *computation*:

```
Input → Linear(4× expansion) → ReLU → Linear(4× contraction) → Output
```

**Karpathy's insight:** *"Where the model does most of its 'thinking' per position."*

The MLP can be understood as:
- **Pattern matcher:** Each neuron activates on specific input patterns
- **Feature transformer:** Converts attention outputs into useful representations
- **Knowledge storage:** Learned facts and patterns are encoded in the weights

### 4. Residual Connections Enable Deep Networks

Without residual connections, training deep networks fails due to **vanishing gradients**. The residual formulation:

```
output = input + sublayer(LayerNorm(input))
```

Ensures that:
- Gradients can flow directly through the "skip connection"
- Each layer only needs to learn a *residual* (difference from identity)
- Deep networks (100+ layers) become trainable

### 5. RMSNorm > LayerNorm for Simplicity

microgpt uses **Root Mean Square Normalization** instead of LayerNorm:

```
rmsnorm(x) = x / sqrt(mean(x²) + ε)
```

**Why it works:**
- Removes the need for learnable bias terms
- Simpler computation, same effectiveness
- Particularly well-suited for decoder-only architectures

---

## Training: How the Model Learns

### Cross-Entropy Loss

The loss function measures "surprise" at the correct next token:

```
L = -log(p(target_token))
```

- **L ≈ 3.3:** Random guessing across 27 tokens (uniform distribution)
- **L → 0:** Perfect prediction (probability 1.0 on correct token)
- **L ≈ 2.37:** Learned meaningful patterns (microgpt result)

### Adam Optimizer

microgpt implements Adam from scratch:

```python
# Per-parameter update
m = β₁·m + (1-β₁)·g          # First moment (momentum)
v = β₂·v + (1-β₂)·g²        # Second moment (adaptive LR)
m̂ = m / (1-β₁^t)            # Bias-corrected first moment
v̂ = v / (1-β₂^t)            # Bias-corrected second moment
θ = θ - α·m̂ / (√v̂ + ε)     # Parameter update
```

**Key properties:**
- **Momentum (β₁=0.9):** Smooths gradient updates, accelerates convergence
- **Adaptive LR (β₂=0.999):** Scales learning rate per-parameter
- **Bias correction:** Compensates for initialization at zero
- **Linear LR decay:** Gradually reduces learning rate over training

### Autograd from Scratch

microgpt includes a complete autograd engine:

```python
class Value:
    def __init__(self, data, children=(), local_grads=()):
        self.data = data          # Forward pass scalar
        self.grad = 0             # d(loss)/d(this node)
        self._children = children # Graph inputs
        self._local_grads = local_grads  # Local derivatives

    def backward(self):
        # Reverse topological traversal
        # Chain rule: child.grad += local_grad * parent.grad
```

**Algorithmically identical to PyTorch's `.backward()`**, but operates on scalars instead of tensors. This demystifies backpropagation — it's just the chain rule applied systematically.

---

## Inference: How the Model Generates Text

### Autoregressive Sampling

```python
# Start with BOS
tokens = [BOS]
for _ in range(max_length):
    logits = gpt(tokens[-1], len(tokens)-1, keys, values)
    probs = softmax(logits)
    next_token = sample(probs)
    if next_token == BOS:
        break  # End of sequence
    tokens.append(next_token)
```

**Key properties:**
- **One token at a time:** Each step depends on all previous tokens
- **KV Cache:** Pre-computed key/value vectors avoid redundant computation
- **No parallelism during generation:** Inherent sequentiality limits inference speed

### Temperature Control

```python
temperature = 0.5
probs = softmax([l / temperature for l in logits])
```

- **temp → 0:** Greedy (always pick highest probability)
- **temp = 1:** Standard sampling (natural distribution)
- **temp > 1:** More creative/diverse (flattened distribution)

**Intuition:** Temperature controls the "sharpness" of the probability distribution. Low temperature makes the model more confident and conservative; high temperature makes it more exploratory.

---

## Scaling: From microgpt to Production LLMs

| Aspect | microgpt | Production LLM (e.g., GPT-4) |
|--------|----------|------------------------------|
| **Parameters** | 4,192 | ~1.8 trillion |
| **Vocabulary** | 27 (chars) | ~100,000 (subword tokens) |
| **Layers** | 2 | 90+ |
| **Training Data** | 32K names | Trillions of tokens |
| **Compute** | CPU, seconds | GPU clusters, months |
| **Architecture** | RMSNorm + ReLU + Multi-head | RMSNorm + GeLU + Multi-head + Flash Attention |
| **Optimizer** | Adam | AdamW |

**Karpathy's thesis:** *"Everything else is just efficiency."* The core algorithm is the same — production LLMs scale up the same fundamental components with engineering optimizations (parallelism, mixed precision, distributed training, etc.).

---

## Key Educational Projects in the Lineage

Karpathy's progression of educational implementations:

1. **micrograd (2019):** Scalar autograd engine → teaches backpropagation
2. **makemore (2022):** Character-level language model → teaches autoregressive generation
3. **nanoGPT (2022):** Minimal PyTorch GPT → teaches practical LLM training
4. **llm.c (2024):** C/CUDA GPT-2 → teaches low-level implementation
5. **nanochat (Oct 2025):** Full-stack ChatGPT for <$100 → teaches deployment
6. **microgpt (Feb 2026):** 200 lines pure Python → teaches the complete GPT algorithm

**Philosophy:** If you can understand it in 200 lines of Python, you understand it. Everything else is engineering.

---

## Related Concepts

-  — Neural networks as programs
- [[concepts/vibe-coding]] — Natural language programming
-  — Managing AI agents in parallel
- [[concepts/local-llm]] — Running LLMs locally (nanochat, llm.c)
-  — Teaching LLMs from first principles

## References

- Karpathy, A. (2026). "microgpt" — https://karpathy.github.io/2026/02/12/microgpt/
- Karpathy, A. (2019). "A Recipe for Training Neural Networks" — https://karpathy.github.io/2019/04/25/recipe/
- Karpathy, A. (2017). "Software 2.0" — https://karpathy.github.io/2017/07/20/software-2.0/
- Karpathy, A. (2015). "The Unreasonable Effectiveness of Recurrent Neural Networks" — https://karpathy.github.io/2015/05/21/rnn-effectiveness/
- microgpt source: https://github.com/karpathy/microgpt
