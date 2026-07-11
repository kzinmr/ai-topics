---
title: DeepSeek-V3.2
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - model
  - reasoning
  - training
  - ai-agents
  - benchmark
  - deepseek
sources:
  - raw/papers/2025-12-02_2512.02556_deepseek-v3.2-technical-report.md
  - https://arxiv.org/abs/2512.02556
---

# DeepSeek-V3.2

DeepSeek-V3.2 is a **685B parameter** high-efficiency reasoning model. Announced by DeepSeek-AI in December 2025. Evolving [[concepts/deepseek-v3|V3]] with three innovations — **DeepSeek Sparse Attention (DSA)**, **scalable RL (GRPO)**, and **large-scale agent task synthesis** — it aimed to close the performance gap between open-source and commercial frontier models (GPT-5, Gemini-3.0-Pro). The high-compute variant **V3.2-Speciale** won gold medals at IMO 2025 and IOI 2025.

## Architecture Innovations

### DeepSeek Sparse Attention (DSA)

A new attention mechanism that reduces standard self-attention's $O(L^2)$ complexity to $O(Lk)$ (where $k$ is the number of selected tokens).

**Lightning Indexer**:
- Computes an **index score** $I_{t,s}$ between query token $h_t$ and past token $h_s$
- Formula: $I_{t,s} = \sum_{j=1}^{H^I} w^I_{t,j} \cdot \text{ReLU}(q^I_{t,j} \cdot k^I_s)$
- Rather than hardcoded sparse patterns, it **learns which past tokens to retain**

**Fine-grained Token Selection**:
- Retrieves only top-k KV entries based on indexer scores
- Significantly reduces inference cost in long-context scenarios (up to 128K)
- Achieves efficiency without performance degradation

DSA was later adopted in successor [[concepts/deepseek-v4|V4]] (CSA: Compressed Sparse Attention) and [[concepts/glm-5-1|GLM-5.1]], becoming a standard technique for long-context efficiency in open-source LLMs. See [[concepts/attention-mechanism-variants]] for comparison with existing techniques.

### Scalable RL Framework (GRPO Enhancement)

Three enhancements to [[concepts/post-training/grpo|GRPO]] (Group Relative Policy Optimization) introduced in [[concepts/deepseek-r1|R1]]. The post-training budget exceeded **10%** of pre-training cost.

| Improvement | Content | Effect |
|--------|------|------|
| **Unbiased KL Estimate** | Removes systematic estimation bias | Stable convergence |
| **Off-Policy Sequence Masking** | Masks negative sequences with large policy divergence | Improved training stability |
| **Keep Routing / Sampling Mask** | Ensures MoE routing and sampling consistency across inference and training frameworks | Framework alignment |

### Large-Scale Agent Task Synthesis

To enhance the model's tool-use capabilities, a data synthesis pipeline was developed that generates **1,827 different environments** and **85,000 complex prompts**.

**Synthetic Task Types**:
- **Trip Planning**: Multi-step constraint satisfaction planning problems
- **Code Agent**: Composite tasks involving code execution
- Characteristic: "Hard to solve, easy to verify"

**Thinking in Tool-Use**:
- Keep reasoning traces (`<tool_thinking>`) during tool conversations
- Discard traces when new user messages arrive to save tokens
- Maximum code execution rounds: 20, prioritize code execution over language reasoning where possible

## Model Variants

| Model | Parameters | Characteristics |
|--------|-----------|------|
| **V3.2 (Standard)** | 685B | Supports both reasoning and agents, GPT-5-High level |
| **V3.2-Speciale** | 685B (high-compute reasoning) | Relaxed length constraints, increased reasoning tokens, competition-focused |

## Benchmark Performance

| Benchmark | GPT-5 High | Gemini-3.0 Pro | DeepSeek-V3.2 | **V3.2-Speciale** |
|-------------|:----------:|:--------------:|:-------------:|:-----------------:|
| **AIME 2025** | 94.6% | 95.0% | 93.1% | **96.0%** |
| **HMMT Feb 2025** | 88.3% | 97.5% | 92.5% | **99.2%** |
| **GPQA Diamond** | 85.7% | **91.9%** | 82.4% | 85.7% |
| **Codeforces (Rating)** | 2537 | **2708** | 2386 | 2701 |
| **SWE-bench Verified** | 74.9% | 76.2% | 73.1% | — |

### Competitive Programming Results (Speciale)

| Competition | Result |
|------|------|
| **IMO 2025** (International Mathematical Olympiad) | 🥇 Gold Medal |
| **IOI 2025** (International Olympiad in Informatics) | 🥇 Gold Medal |
| **ICPC World Finals 2025** | 🥈 World 2nd Place |

## Context Management in Search & Long Context

Three strategies implemented to address the long-context bottleneck in search agents:

| Strategy | Behavior | Efficiency |
|------|------|------|
| **Summary** | Summarize overflowed trajectory | Medium |
| **Discard-75%** | Discard oldest 75% of tool history | High |
| **Discard-all** | Reset context while preserving current goal | **Most efficient and scalable** |

## Limitations & Future Work

1. **World Knowledge**: Still lags behind proprietary models due to fewer total training FLOPs
2. **Token Efficiency**: Requires longer generation trajectories (more tokens) to achieve quality comparable to Gemini-3.0-Pro
3. **Intelligence Density**: Optimizing the "density" of reasoning chains is a future challenge — reducing latency and cost

## Position in DeepSeek Evolution

```
V3 (Dec 2024)         671B MoE, FP8 training, DualPipe — GPT-4o-class at $5.6M
    ↓
V3.2 (Dec 2025)       685B, DSA + GRPO enhanced + Agent synthesis — Approaches GPT-5/Gemini-3.0-Pro
    ↓
V4 (Apr 2026)         1.6T Pro / 284B Flash, 1M context, Hybrid Attention — Full frontier
```

V3.2's positioning is a **transitional milestone built on V3's efficient architecture, adding DSA for inference efficiency and scalable RL for reasoning capability enhancement**. While it lacks the architectural leaps of V4's 1M context, mHC, and Muon Optimizer, DSA and agent task synthesis are important technical contributions inherited by successor models.

## Historical Significance

1. **DSA Established**: Learnable sparse attention validated as a practical long-context efficiency technique, propagated to successors V4, GLM-5.1
2. **Open-Source Competitiveness Proved**: Demonstrated that open-weight models can approach commercial frontiers of the GPT-5/Gemini-3.0-Pro generation
3. **Agent Capability via Synthetic Data Scaling**: The synthesis pipeline of 1,827 environments and 85K prompts showed transferability to real-task performance
4. **Competitive AI Milestone**: IMO/IOI gold medals mark a significant milestone in AI's mathematical and algorithmic reasoning capabilities

## See Also

- [[entities/deepseek]] — DeepSeek company overview
- [[concepts/deepseek-v3]] — Previous generation (V3 architecture)
- [[concepts/deepseek-v4]] — Successor model (1M context, Hybrid Attention)
- [[concepts/deepseek-r1]] — Reasoning-specialized model (origin of GRPO)
- [[concepts/post-training/grpo]] — Group Relative Policy Optimization
- [[concepts/attention-mechanism-variants]] — Comparison of attention techniques including DSA
- [[concepts/glm-5-1]] — Successor model adopting DSA
- [[agent-training]] — Agent task synthesis context
- [[concepts/speculative-decoding]] — Inference efficiency techniques
- [[concepts/mixture-of-experts]] — MoE architecture
