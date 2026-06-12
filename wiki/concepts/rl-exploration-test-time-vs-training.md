---
title: 'RL Exploration: Training vs Test-Time Scaling'
type: concept
created: 2026-06-12
updated: 2026-06-12
tags: [reinforcement-learning, test-time-scaling, scaling, inference, reasoning]
sources:
  - url: https://x.com/sheriyuo/status/2063295181131247674
    title: 'RL Interview Questions 2026 — Q6'
    date: 2026-06-06
  - url: https://arxiv.org/abs/2506.07976
    title: 'Scaling Test-Time Compute Without Verification or RL is Suboptimal (ICML 2025)'
  - url: https://arxiv.org/abs/2601.21590
    title: 'Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning (ICML 2025)'
---

# RL Exploration: Training vs Test-Time Scaling

A core question in [[rl-interview-questions-2026]]: how does exploration during [[reinforcement-learning]] training differ from exploration at test time?

## RL Training Exploration

During training, exploration happens **inside rollout generation**:

- The policy samples stochastically from its distribution — exploration is implicit, driven by entropy.
- Weights are **updated** based on the reward signal from explored trajectories.
- As training progresses the policy becomes more deterministic (entropy shrinks), naturally reducing exploration.
- Maintenance strategies: entropy bonuses, KL penalties against a reference policy (see [[grpo-rl-training]]), and temperature scaling.

**Critical failure mode:** if the policy *never* samples a correct trajectory for a given prompt, that prompt yields zero reward and contributes nothing to learning. This makes coverage of the search space during early training essential.

## Test-Time Scaling Exploration

At inference, exploration happens **without modifying weights**:

- Methods include best-of-N sampling, beam search, MCTS, sequential revision (self-refine), and verifier-based reranking.
- More compute → more candidate completions → higher probability of finding a correct answer.
- The base model's capabilities set the ceiling: test-time exploration can only surface what the model can *already* produce.

See [[test-time-scaling]] for the broader framework.

## The Fundamental Difference

| | RL Training | Test-Time Scaling |
|---|---|---|
| **What changes** | The policy distribution (weights) | Nothing — search within fixed distribution |
| **Duration** | Permanent | Ephemeral (per-query) |
| **Effect** | Reshapes what the model *can* generate | Finds the best from what it *already* can |
| **Learning** | Yes — improves future generations | No — next query starts from scratch |

## Why Training Still Matters: The Aviral Kumar Result (ICML '25)

Test-time scaling **without verification or RL is asymptotically suboptimal** (Kumar et al., 2025). The key insight: the verifier signal must flow back into training for test-time compute to convert into accuracy. A verifier-based (VB) approach enjoys an **Ω(√H)** asymptotic advantage over verifier-free (VF) methods. Simply generating more samples at test time without a training loop that leverages the verifier hits diminishing returns.

## Bridging the Gap: Meta Reinforcement Fine-Tuning (MRT)

Standard outcome-reward RL (e.g., [[rlvr]]) gives a single 0/1 at the end of a trace. MRT instead optimizes the training objective to **maximize expected test-time performance** — explicitly linking training-time weight updates to test-time search effectiveness. This bridges the two exploration regimes.

## Intrinsic Rewards and Their Limits

Self-consistency reward schemes (TTRL-style) can replace external verifiers but cause **distribution sharpening** → eventual model collapse. They are safe only on small sample sets (<128). This highlights that not all reward signals are equal; poorly shaped intrinsic rewards can destroy the diversity needed for exploration.

## Key Takeaway

RL training and test-time scaling are **complementary, not interchangeable**. Training expands what the model can reach; test-time search finds the best within that reach. The strongest systems combine both — training with verifier signals (via [[rl-algorithms-for-llm-training]]) and allocating extra compute at inference. See also [[training-free-rl]] for approaches that attempt to get training benefits without full RL loops.
