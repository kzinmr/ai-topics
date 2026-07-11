---
title: "Training-Free RL"
created: 2026-06-12
updated: 2026-06-12
type: concept
tags:
  - concept
  - test-time-scaling
  - reinforcement-learning
  - rlvr
  - reasoning
  - inference
  - training-free
  - mcmc
  - optimization
sources:
  - raw/articles/2026-04-09_sheriyuo_test-time-scaling-training-free-rl.md
  - raw/articles/2026-06-01_sheriyuo_rl-for-test-time-scaling.md
  - https://arxiv.org/abs/2601.21484
  - https://github.com/sheriyuo/ETS
related:
  - test-time-scaling
  - reinforcement-learning
  - grpo
  - rlvr
  - self-evolving-agents
  - on-policy-distillation
  - chain-of-thought
  - reasoning
---

# Training-Free RL

**Training-free RL** is a paradigm that achieves the alignment effects of reinforcement learning (improved pass@1, sharper distributions) without updating model weights — instead using inference-time compute strategies (test-time scaling) to sample from the RL-optimal target distribution. The core idea: amortize training compute into inference compute.

> This page synthesizes Xiuyu Li's (@sheriyuo) two-part X Article series on TTS and training-free RL ([Part 1](https://x.com/sheriyuo/status/2042072816712085577), [Part 3](https://x.com/sheriyuo/status/2061382777623519284)).

## Core Intuition

RL does not teach the base model new knowledge per se. Compared with SFT (which broadens the existing distribution), RL **sharpens** the base model's distribution: it trades degraded pass@k for improved pass@1. If we could sample directly from this sharpened distribution at inference time, we would get RL-like improvements without any training.

## Approaches

### Power Sampling (MCMC-Based)

Inspired by the **Metropolis-Hastings** algorithm from Bayesian statistics:

1. Sample an initial state from the base model
2. Cut a prefix at a random point, resample following tokens to get candidate samples
3. Accept/reject candidates based on probability ratios
4. More candidates → closer convergence to the target distribution

This effectively performs MCMC sampling over the RL-optimal distribution. **Power Sampling v2** (Scalable Power Sampling, ICML'26) adds a look-ahead guide to approximate the MCMC process autoregressively without resampling, achieving ~10× speedup with vLLM.

### Energy-Guided Test-Time Scaling (ETS)

**ETS** (Energy-Guided Test-Time Scaling for Training-Free RL Alignment) extends the idea to general RL scenarios (RLHF, RLVR):

1. For RLHF objectives with KL constraint (PPO, GRPO), a **closed-form solution** exists (via Lagrange multipliers)
2. Using masked language modeling, autoregressive and diffusion models can be unified as a reverse Markov chain
3. Analogous to **Gibbs sampling**, decompose the optimal transition distribution into:
   - A known **posterior transition** (from the base model)
   - An **energy term** related to reward (guides toward higher-reward outputs)
4. Monte Carlo estimation: sample continuations from the posterior, estimate their rewards
5. Samples converge to the optimal target distribution (provable)

**Results**: ETS outperforms GRPO RL-trained models on reasoning, math, and coding benchmarks. Accelerated via **ETS-IS** (importance sampling) and async inference pipeline.

- **Paper**: [arxiv.org/abs/2601.21484](https://arxiv.org/abs/2601.21484)
- **Code**: [github.com/sheriyuo/ETS](https://github.com/sheriyuo/ETS)

### Self-Evolving Approaches

Self-Evolving is the **sequential** counterpart to TTS's parallel approach. Multiple rounds of rollout + update (prompt, memory, or model):

| Update Type | Method | Training Required |
|-------------|--------|-------------------|
| Gradients/LoRA after rollouts | Test-time RL / training-free GRPO | Minimal (single-step) |
| Prompt/memory only (no gradients) | [[self-evolving-agents\|Reflexion]] | None |

**RSE** (Reinforced Self-Evolution): Uses Self-Guided Experience Distillation — the model judges which trajectory parts are useful and adds that to prompts for subsequent rounds.

## Fundamental Limits

### Why Training-Free Does Not Scale (ICML'25 Spotlight)

**Scaling Test-Time Compute Without Verification or RL is Suboptimal** proves that verifier-based (VB) approaches enjoy an **Ω(√H) asymptotic advantage** over verifier-free (VF) approaches, where H is the compute budget:

- **VF route** (distilling reasoning traces into SFT): imitation around the policy mean, cannot amplify the rare-but-correct tail
- **VB route** (feeding verifier signal into training): importance-weighted update, exploits reward anti-concentration

**Implication**: If you want test-time compute to convert into accuracy, the verifier/reward signal must flow back into training.

### Intrinsic Rewards Hit a Ceiling (ICLR'26)

**How Far Can Unsupervised RLVR Scale LLM Training?** shows all "intrinsic rewards" (majority-voting, entropy minimization) perform **distribution sharpening** — collapsing the policy onto a fixed point. The empirical signature is a universal **"rise then collapse" curve** at the **Model Collapse Step**, invariant to data volume. Safe only on small (sub-128 sample) sets.

### The Suboptimality Conclusion

Unsupervised TTS, even when it fits the RLHF objective (ETS), still cannot escape this suboptimality. The practical conclusion: **we do not need to insist on being fully training-free**. The shift is from "how to spend inference compute cleverly" to "how to train the model so it knows how to spend that compute."

## RL for Test-Time Scaling (The Other Direction)

Rather than making TTS training-free, the complementary approach is to **train models specifically to leverage test-time compute**:

| Method | Key Idea | Venue |
|--------|----------|-------|
| **MRT** (Meta Reinforcement Fine-Tuning) | Progress reward ΔP(success) per chunk of reasoning trace | ICML'25 Spotlight |
| **e3** (Learning to Explore) | Train in-context exploration as a skill; 2× extrapolation | ICLR'26 |
| **Privileged On-Policy Exploration** | Oracle prefix for hard problems; pass@1 → 58% | — |
| **InT** (Self-Proposed Interventions) | Step-level credit assignment from failed traces; +10pts | ICLR'26 |
| **TTI** (Test-Time Interaction) | Interaction-scaling > thought-scaling for agents | NeurIPS'25 Best Paper |

→ See [[concepts/test-time-scaling]] for full treatment of these methods.

## Relationship to Other Paradigms

```
                    ┌─────────────────────────┐
                    │   Training-Free RL       │
                    │  (ETS, Power Sampling)   │
                    │  No weight updates       │
                    └────────┬────────────────┘
                             │ approximates
                             ▼
                    ┌─────────────────────────┐
                    │   Standard RL (GRPO,    │
                    │   PPO, RLHF)            │
                    │  Weight updates required │
                    └────────┬────────────────┘
                             │ trains for
                             ▼
                    ┌─────────────────────────┐
                    │  RL for TTS (MRT, e3,   │
                    │  InT, TTI)              │
                    │  Models learn to use    │
                    │  test-time compute      │
                    └─────────────────────────┘
```

## Open Questions

1. Can better estimators (ETS-v2) close the gap with trained RL?
2. What is the practical compute crossover: when does training become cheaper than inference-time sampling?
3. How do these methods compose with [[concepts/self-evolving-agents|self-evolving]] approaches?
4. Industry view: gpt-oss 120b as the dividing line between "weak" and "strong" RL models — does the training-free vs trained distinction matter at frontier scale?

## Related Pages

- [[concepts/test-time-scaling]] — The broader TTS landscape (CoT, self-consistency, beam search, RL-trained reasoning)
- [[reinforcement-learning]] — RL fundamentals (PPO, GRPO, reward design)
- [[grpo]] — Group Relative Policy Optimization
- [[rlvr]] — RL with Verifiable Rewards
- [[concepts/self-evolving-agents]] — Reflexion, self-play, self-distillation
- [[on-policy-distillation]] — SDFT, SDPO as the "other direction"
- [[concepts/chain-of-thought]] — The substrate for all TTS methods
- [[reasoning]] — AI reasoning capabilities
