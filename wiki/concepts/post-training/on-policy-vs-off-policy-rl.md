---
title: "On-Policy vs Off-Policy RL"
type: concept
created: 2026-06-08
updated: 2026-06-08
tags:
  - concept
  - reinforcement-learning
  - training
  - on-policy
  - off-policy
  - post-training
aliases:
  - on-policy-learning
  - off-policy-learning
  - policy-on-vs-off
sources:
  - raw/articles/2023-04-09_yoavg-rl-for-llms.md
  - https://gist.githubusercontent.com/yoavg/6bff0fecd65950898eba1bb321cfbd81/raw/5ab0bb27909cc625e02c611117a0a2f3a026cb56/rl-for-llms.md
related:
  - concepts/post-training/post-training-distributional-view
  - concepts/post-training/on-policy-distillation
  - concepts/post-training/grpo-rl-training
  - concepts/post-training/asynchronous-rl
  - concepts/post-training/rlhf
  - concepts/deepseek-r1
  - entities/yoav-goldberg
  - entities/nrehiew
---

# On-Policy vs Off-Policy RL

> The distinction between **on-policy** and **off-policy** learning is one of the most fundamental divides in reinforcement learning. In the context of LLM post-training, it determines whether a model learns from its own generated outputs (on-policy) or from external data such as human demonstrations (off-policy) — and this choice has profound implications for hallucination, exposure bias, and training stability.

## Core Distinction

| | On-Policy | Off-Policy |
|---|---|---|
| **Data source** | The current model itself generates training data | External source (human, teacher model, past data) |
| **Data reuse** | Cannot — old data discarded after each update | Can — same data reused across updates |
| **Data efficiency** | Low | High |
| **Distribution match** | Training ≡ inference distribution | Training ≠ inference distribution (exposure bias) |
| **Cost** | High (repeated inference) | Low |
| **LLM examples** | GRPO, PPO, OPD | SFT, DPO |

### Intuition: The Chess Analogy (from [[concepts/post-training/on-policy-distillation]])

| Method | Analogy |
|--------|---------|
| **Off-policy (SFT)** | Watching a grandmaster play — you see strong moves in positions *you* never reach |
| **On-policy (RL)** | Playing games yourself with only outcome feedback — you know you lost, but not which move was bad |
| **On-policy + dense (OPD)** | A coach grading each of *your own* moves in real time |

## Why It Matters for LLMs

### The Exposure Bias Problem

Off-policy methods like SFT train the model on **idealized expert data**. At inference time, the model generates from its own (imperfect) distribution. This mismatch is called **exposure bias**:

```
Training:  "Perfect expert prefix" → predict next token
Inference: "Model's own (flawed) prefix" → predict next token
           ↑ distribution shift — model has never seen its own errors during training
```

[[concepts/post-training/post-training-distributional-view|The distributional view]] frames this precisely: SFT does **forward KL** (mode-seeking) toward the teacher's distribution, while RL and OPD do **reverse KL** on the student's own rollouts.

### The Hallucination Problem (Goldberg, 2023)

Yoav Goldberg's influential 2023 analysis ([[entities/yoav-goldberg|Yoav Goldberg]], [gist](https://gist.githubusercontent.com/yoavg/6bff0fecd65950898eba1bb321cfbd81/raw/5ab0bb27909cc625e02c611117a0a2f3a026cb56/rl-for-llms.md)) identified a deeper problem specific to **knowledge-seeking queries**:

> We want to encourage the model to answer based on its internal knowledge, but **we don't know what this internal knowledge contains**. When the model does not know the answer, supervised training pushes it to associate the answer with the question anyway. If this generalizes, we are actively teaching the model to **make stuff up**.

This argument establishes that for knowledge-seeking tasks (type (b) in Goldberg's taxonomy), **off-policy SFT provably teaches hallucination** when the model's knowledge is incomplete — which is always the case. On-policy RL avoids this because the model generates its own answers and receives feedback; made-up answers receive negative reward over time, driving the model toward either answering from internal knowledge or abstaining.

Goldberg also identified the **distillation trap**: training an open model on GPT outputs via SFT suffers from the same problem because the student model has a different knowledge base than GPT, and learning to replicate GPT's answers encourages fabrication.

### The Abstention Challenge

Teaching a model to say "I don't know" is difficult in **both** paradigms:

- **Off-policy**: We don't know what the model knows, so we cannot create training data that says "I don't know" exactly where the model lacks knowledge
- **On-policy**: The model may never generate "I don't know" spontaneously, so there is nothing to reinforce

Goldberg proposed a **reward shaping** approach: high scores for correct answers, medium-low for abstention, strong negatives for incorrect answers. This remains an active research area in 2026 — see [[concepts/ai-alignment]] for the broader context.

### Why LLMs Blur the Boundary (Traditional RL vs LLM-RL)

In traditional RL (robotics, autonomous driving, game AI), behavior cloning (the RL equivalent of SFT) and off-policy RL are **sharply distinct** — not on a spectrum as in LLM-RL. Three structural reasons:

1. **Compounding error (Distribution Shift)**: In physical environments, a slight deviation leads to states never seen in expert data, causing catastrophic failure. A self-driving model trained only on "drive straight" logs has never seen "slightly off-center" states and cannot recover. Off-policy RL learns recovery from failure data; behavior cloning cannot.

2. **No negative feedback**: SFT/behavior cloning only teaches "do this" — it never signals "don't do that." Traditional off-policy RL assigns low rewards to failure trajectories, teaching the policy to avoid failure states.

3. **No importance sampling correction**: Off-policy RL reweights data with $\frac{\pi_\theta(a|s)}{\mu(a|s)}$ to correct for distribution mismatch between the data-generating policy $\mu$ and the current policy $\pi_\theta$. SFT ignores this mismatch entirely.

LLMs escape these constraints because:
- **Discrete token space** — a wrong token doesn't cause physical catastrophe; language context enables self-recovery
- **Pre-training** — the model already "knows the environment dynamics" (language structure) before SFT, dramatically reducing exposure bias
- **Distributional resilience** — language is more forgiving of small deviations than continuous control

This is why LLM-RL treats SFT and RL as endpoints on a continuum (see below), while traditional RL treats them as categorically different techniques. See [[concepts/post-training/llm-as-policy]] for the broader paradigm context.

## The 2026 Landscape: Not Binary but a Spectrum

Goldberg's 2023 framing was "SFT vs RL" as a dichotomy. By 2026, the field has evolved into a **continuous spectrum** along two axes (Will Brown's unified meta-algorithm, [[entities/will-brown]]):

```
∇_θ J = E_{x ~ π_θ^α} [ λ · A^KL(x) + (1-λ) · A^outcome(x) ]
```

- **α ∈ [0,1]** — how on-policy the sampling is (α=1: fully on-policy; α=0: off-policy)
- **λ ∈ [0,1]** — proportion of teacher KL signal vs outcome reward

| Method | α (on-policy?) | λ (teacher signal?) | Teacher π_T |
|--------|:---:|:---:|---|
| **SFT** | 0 (off-policy) | 1 | Degenerate (δ on data token) |
| **DPO** | 0 (off-policy) | 1 | Implicit (preference pairs) |
| **RL (GRPO)** | 1 (on-policy) | 0 | None (outcome reward) |
| **OPD** | 1 (on-policy) | 1 | Same-family external teacher |
| **OPSD** | 1 (on-policy) | 1 | Self + privileged info |

### Key Modern Methods

#### On-Policy Methods

- **[[concepts/post-training/grpo-rl-training|GRPO]]** — Group Relative Policy Optimization. Eliminates critic model by computing advantages within a group of sampled completions. The dominant RL backbone for reasoning training ([[concepts/deepseek-r1|DeepSeek-R1]]). Fully on-policy.
- **[[concepts/post-training/on-policy-distillation|OPD]]** — On-Policy Distillation. Student generates rollouts; teacher provides per-token reverse KL supervision. 50-100× more compute-efficient than RL while being fully on-policy.
- **[[concepts/post-training/asynchronous-rl|Async RL]]** — Decouples rollout and training for throughput, but introduces **policy lag** (staleness). As lag K grows, the method becomes increasingly off-policy, requiring importance sampling corrections.

#### Off-Policy Methods

- **SFT** — Classic supervised fine-tuning on curated input-output pairs. Off-policy by definition.
- **DPO** — Direct Preference Optimization. Trains on preference pairs without a reward model. Off-policy (data is fixed).
- **KTO** — Kahneman-Tversky Optimization. Binary feedback (good/bad). Off-policy, scalable.

#### Hybrid Methods

- **DeepSeek-R1 pipeline** — Cold Start SFT (off-policy) → Reasoning RL (on-policy) → Rejection Sampling + SFT (off-policy) → General RL (on-policy). Stages alternate between paradigms.
- **[[concepts/post-training/sdar-self-distilled-agentic-rl|SDAR]]** — Gated OPSD + GRPO for multi-turn agents. Combines on-policy RL with on-policy self-distillation.

## Information-Theoretic Perspective

[[concepts/post-training/post-training-distributional-view|The distributional view]] (@nrehiew) quantifies the information density difference:

| Method | Information per episode | Sampling |
|--------|------------------------|----------|
| SFT | O(n) tokens (dense) | Off-policy |
| RL (GRPO) | O(1) bits (sparse) | On-policy |
| OPD | O(n) tokens (dense) | On-policy |

RL provides only 1 bit of information per episode (the reward signal), but that bit is **unbiased** and **on-policy**. SFT provides O(n) bits per episode, but they are **biased** toward the teacher's distribution and **off-policy**. OPD achieves the best of both: O(n) bits of dense, on-policy supervision.

## Goldberg's 2023 Predictions vs 2026 Reality

| Goldberg's Argument (2023) | 2026 Status | Evidence |
|---|---|---|
| SFT teaches hallucination for unknown knowledge | ✅ Confirmed | [[concepts/deepseek-r1]] pure RL avoids SFT entirely |
| RL without human feedback is coming | ✅ Realized | [[concepts/post-training/grpo-rl-training]] with rule-based rewards; [[concepts/post-training/reinforcement-fine-tuning]] |
| Distillation needs RL to avoid knowledge mismatch | ✅ Addressed | [[concepts/post-training/on-policy-distillation]] (on-policy distillation) |
| "I don't know" training is unsolved | ⚠️ Partially | Negative alignment progresses; positive alignment ([[concepts/ai-alignment]]) remains open |
| RL is expensive and hard | ❌ Less true | GRPO eliminates critic model; OPD is 50-100× cheaper than RL |

## Related Pages

- [[concepts/post-training/post-training-distributional-view]] — Distributional lens: SFT vs RL vs OPD
- [[concepts/post-training/on-policy-distillation]] — On-policy distillation mechanism and variants
- [[concepts/post-training/grpo-rl-training]] — The dominant on-policy RL algorithm (2025-2026)
- [[concepts/post-training/asynchronous-rl]] — Async RL and the policy-lag / off-policy tradeoff
- [[concepts/post-training/rlhf]] — The full spectrum from SFT to DPO to GRPO
- [[concepts/deepseek-r1]] — Pure RL reasoning emergence (R1-Zero)
- [[concepts/post-training/sdar-self-distilled-agentic-rl]] — Gated OPSD + GRPO for agent training
- [[entities/yoav-goldberg]] — Author of the foundational "why RL" analysis (2023)
- [[entities/nrehiew]] — Author of the distributional post-training view
- [[concepts/post-training/llm-as-policy]] — LLM-as-Policy paradigm: SFT as behavior cloning, the DPO/GRPO convergence toward implicit modeling
- [[entities/will-brown]] — Unified meta-algorithm (α × λ taxonomy)
