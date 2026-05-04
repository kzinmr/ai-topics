---
title: "SSM / Mamba — State Space Models for Sequence Modeling"
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level3
tags: [ssm, mamba, architecture, sub-quadratic, state-space-model, sequence-modeling]
aliases: [structured-state-space, mamba-architecture, selective-ssm, s4-model, mamba-2, mamba-3, state-space-duality]
sources:
  - https://arxiv.org/abs/2312.00752
  - https://arxiv.org/abs/2405.21060
  - https://arxiv.org/abs/2603.15569
  - https://arxiv.org/abs/2111.00396
  - https://srush.github.io/annotated-s4/
  - https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state
  - https://hazyresearch.stanford.edu/blog/2022-01-14-s4-1
  - https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture)
  - raw/articles/2026-05-04_genai-handbook.md
---

# SSM / Mamba — State Space Models for Sequence Modeling

State Space Models (SSMs) are a family of sequence modeling architectures that offer a **linear-time alternative to Transformers** for processing long sequences. They draw inspiration from classical control theory and have evolved through several generations — from the foundational **S4** through **Mamba** (selective SSM), **Mamba-2/SSD** (State Space Duality), to the inference-first **Mamba-3** (ICLR 2026 Oral).

> **Core Advantage:** SSMs scale **O(L)** in sequence length during inference (vs Transformer's O(L²)), while maintaining or matching Transformer quality on language tasks. This makes them particularly attractive for long-context applications and edge deployment.

---

## 🧠 Core Mechanism

### Continuous State Space Model

An SSM is a mathematical framework that maps an input sequence to a latent state representation:

```
State Equation:  h'(t) = A·h(t) + B·x(t)
Output Equation: y(t)  = C·h(t) + D·x(t)
```

- **A**: How the internal state evolves over time
- **B**: How input influences the state
- **C**: How state translates to output
- **D**: Skip-connection (often omitted in practice, absorbed into residual)

### Discretization

To process discrete data (text tokens), the continuous SSM is discretized using a **step size Δ** (learnable parameter). Common methods include Zero-Order Hold (ZOH) and bilinear transform.

### Three Representations

One of SSMs' key innovations is having **three equivalent representations**:

| Representation | Use Case | Benefit |
|---------------|----------|---------|
| **Continuous** | Theory/analysis | Understanding dynamics |
| **Recurrent** | Inference | O(L) generation, like RNN |
| **Convolutional** | Training | Parallelizable, like CNN |

This allows SSMs to get "the best of both worlds" — parallel training like Transformers, linear inference like RNNs.

### HiPPO (Initialization for Matrix A)

The **HiPPO** framework (High-order Polynomial Projection Operators) provides a principled initialization for Matrix A that captures recent tokens accurately while decaying older information gracefully. It's the key reason S4 could handle sequences of 16K+ tokens while prior RNNs failed.

---

## 📜 Evolution: S4 → Mamba → Mamba-2 → Mamba-3

### S4 (2021, ICLR 2022 Outstanding Paper Honorable Mention)

**Authors:** Albert Gu, Karan Goel, Christopher Ré (Stanford Hazy Research)
**Paper:** [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396)

The foundational SSM architecture. Key innovations:
- **Structured parameterization** of Matrix A via Normal Plus Low-Rank (NPLR) decomposition, enabling stable diagonalization
- HiPPO initialization for long-range dependency capture
- **S4D** (diagonal) variant simplified the architecture

S4 achieved **91% on sequential CIFAR-10** and **SoTA on every Long Range Arena task**, including solving the Path-X challenge (16K length) that all prior work failed on. However, it was **Linear Time Invariant (LTI)** — parameters were static, making it poor at content-aware tasks.

> **Best resource:** [The Annotated S4](https://srush.github.io/annotated-s4/) — Sasha Rush's code walkthrough in JAX, very much in the style of The Annotated Transformer.

### Mamba (Dec 2023) — Selective SSM (S6)

**Authors:** Albert Gu, Tri Dao
**Paper:** [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752)

The breakthrough that made SSMs competitive with Transformers on language. Two key innovations:

**1. Selective Scan Algorithm (S6)**
- Made parameters **B, C, and Δ input-dependent** (time-varying rather than time-invariant)
- This enables **content-aware filtering** — the model can "choose" what to remember and what to ignore
- A small Δ ignores current input (focus on context); a large Δ focuses on current input
- Uses a **parallel associative scan** instead of convolution (since parameters are dynamic)

**2. Hardware-Aware Algorithm**
- **Kernel fusion:** discretization, selective scan, and multiplication fused into a single CUDA kernel
- **Recomputation:** intermediate states recomputed on backward pass (reducing memory)
- Up to **3× faster on A100 GPUs** vs comparable Transformer

**Architecture:** Simplified — combines SSM block and MLP into a single homogeneous block, replacing both self-attention and FFN in Transformers.

**Performance:** Matched或 exceeded Transformer quality at small to medium scale, while offering linear-time inference.

> **Best resource:** [A Visual Guide to Mamba and State Space Models](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state) — Maarten Grootendorst's excellent visual walkthrough.

### Mamba-2 / SSD (May 2024)

**Authors:** Tri Dao, Albert Gu
**Paper:** [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060)

Introduced **State Space Duality (SSD)** — a theoretical framework showing that SSMs and attention are **two sides of the same coin**, connected through structured semiseparable matrices. This revealed:

- Transformers can be viewed as a special case of SSMs, and vice versa
- Enables **2-8× faster training** than Mamba-1 while maintaining quality
- Simplified the architecture (scalar-times-identity state transition)
- Provides a **rich theoretical foundation** connecting linear attention, gated convolution, and SSMs

The SSD framework allows researchers to design architectures by choosing where on the spectrum between pure SSM and pure attention they want to operate.

### Mamba-3 (Jan 2026, ICLR 2026 Oral)

**Authors:** Aakash Lahoti, Kevin Li, Berlin Chen, Caitlin Wang, Aviv Bick, J Zico Kolter, Tri Dao, Albert Gu
**Paper:** [Mamba-3: Improved Sequence Modeling using State Space Principles](https://arxiv.org/abs/2603.15569)

An **inference-first** redesign recognizing that prior SSMs were optimized for training, leaving inference memory-bound. Three innovations:

**1. Exponential-Trapezoidal Discretization**
- Formalizes Mamba-1/2's heuristic discretization ("exponential-Euler")
- New "exponential-trapezoidal" variant reveals an implicit convolution, allowing SSM to replace the short causal convolution entirely

**2. Complex-Valued State Space Model**
- Complex-valued state update enables richer state tracking
- Equivalent to a data-dependent rotary embedding (RoPE)
- Overcomes state-tracking limitations common in linear models

**3. MIMO (Multi-Input Multi-Output) Formulation**
- Improves model performance without increasing decode latency

**Results:** At 1.5B scale, Mamba-3 improves average downstream accuracy by **+0.6 points** vs Gated DeltaNet; MIMO variant adds another **+1.2 points** (+1.8 total). Achieves comparable perplexity to Mamba-2 with **half the state size**.

---

## 🔬 Comparison with Transformers

| Aspect | Transformer | SSM (Mamba-3) |
|--------|------------|---------------|
| **Training scaling** | O(L²) | O(L) — linear |
| **Inference scaling** | O(L²) per token (KV cache grows) | O(L) per token (state is constant) |
| **Content awareness** | High (full attention) | High (selective SSM) |
| **Long-range capture** | Degraded beyond context window | Theoretically unbounded |
| **Hardware efficiency** | FlashAttention helps | Custom CUDA kernels (scan) |
| **State tracking** | Strong (attention heads) | Improved with complex-valued states (Mamba-3) |
| **Ecosystem maturity** | Extremely mature | Growing (HuggingFace, vLLM support) |
| **Training parallelization** | Excellent (all-pairs) | Good (associative scan, but sequential within states) |

### Hybrid Models

A growing trend is **Transformer-SSM hybrids** (e.g., Jamba, Samba, TransMamba) that use attention for some layers and SSM for others. This combines the content-awareness of attention with the efficiency of SSMs. Mamba-3's compatibility with Transformer norms (QKNorm) makes hybridization easier.

---

## 📊 Key Benchmarks

| Model | Scale | Key Result |
|-------|-------|------------|
| S4 | Various | SoTA on all Long Range Arena tasks; 91% on sequential CIFAR-10 |
| Mamba (S6) | 1B–3B | Matches Transformer perplexity; 3× faster on A100 |
| Mamba-2 | 1B–3B | 2-8× faster training than Mamba-1; same quality |
| Mamba-3 | 1.5B | +1.8 points vs Gated DeltaNet; half state size for same PPL as Mamba-2 |
| Mamba-3 (MIMO) | 1.5B | Additional +1.2 points over base Mamba-3 |

---

## 🗺️ Resource Evaluation

| Resource | Quality | Type | Notes |
|----------|---------|------|-------|
| [The Annotated S4](https://srush.github.io/annotated-s4/) (Sasha Rush) | 🟢 | Interactive blog | コード+理論。S4をJAXでゼロから実装。SSM理解への最短路 |
| [Visual Guide to Mamba](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state) | 🟢 | Blog with visuals | Maarten Grootendorstによる最高のビジュアル解説。数学が少なめ。 |
| [Hazy Research S4 Blog Series](https://hazyresearch.stanford.edu/blog/2022-01-14-s4-1) | 🟢 | 3-part blog | 原論文著者チームによる公式解説 |
| [Mamba-2 SSD Series](https://tridao.me/blog/2024/mamba2-part1-model/) (Tri Dao) | 🟢 | 4-part blog | SSD理論の完全解説。Part I-IVでモデル→理論→アルゴリズム→システム |
| [Mamba-3 Princeton Blog](https://pli.princeton.edu/blog/2026/mamba-3-improved-sequence-modeling-using-state-space-principles) | 🟢 | Blog | 最新Mamba-3の平易な解説。Inference-first設計思想の理解に必須 |
| Mamba Paper (arXiv:2312.00752) | 🟢 | Paper | 原著論文。選択的SSMの理論的基礎 |
| [HuggingFace SSM Introduction](https://huggingface.co/blog/lbourdois/get-on-the-ssm-train) | 🟡 | Blog | SSM歴史の俯瞰的まとめ。やや広範だが入門に有用 |
| Yannic Kilcher S4/Mamba videos | 🟡 | Video | 論文解説。理解の補助に |
| Wikipedia: Mamba | 🟡 | Reference | 用語確認に |

---

## 🔗 Related Wiki Pages

- [[concepts/transformer-architecture]] — Transformer (SSMの主たる比較対象)
- [[concepts/attention-mechanism-variants]] — Attention変種（SSMとAttentionの関係）
- [[concepts/kv-cache-compaction]] — KV Cache最適化（SSMはKV cache不要）
- [[concepts/speculative-decoding]] — 投機的復号（SSMとの併用可能性）
- [[concepts/genai-handbook]] — GenAI Handbook（Section VIIでSSMをカバー）
- [[entities/maarten-grootendorst]] — Mamba視覚ガイドの著者
- [[entities/tim-dettmers]] — 量子化の権威（SSM量子化の研究も存在）

## TODO

- [ ] Tri Dao のエンティティページ作成
- [ ] Albert Gu のエンティティページ作成
- [ ] Jamba (AI21)、Samba、TransMamba などハイブリッドモデルの比較セクション拡充
- [ ] SSMの実装フレームワーク（HuggingFace transformers, vLLMでのサポート状況）の追加
