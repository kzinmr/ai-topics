---
title: GRPO (Group Relative Policy Optimization)
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - reinforcement-learning
  - training
  - reasoning
  - alignment
  - deepseek
sources:
  - raw/papers/2025-01-22_2501.12948_deepseek-r1.md
  - https://arxiv.org/abs/2501.12948
---

# GRPO (Group Relative Policy Optimization)

GRPO is a reinforcement learning algorithm introduced in [[concepts/deepseek-r1|DeepSeek-R1]]. Its key innovation is **eliminating the critic model (value function), which was the major computational bottleneck of PPO (Proximal Policy Optimization)**.

## Background: PPO's Limitations

PPO, the standard in traditional RLHF, requires four models:

1. **Policy Model**: The target being trained
2. **Reference Model**: For KL constraints
3. **Reward Model**: For scoring
4. **Critic/Value Model**: For advantage estimation <- **This is the bottleneck**

The critic model must be **the same size** as the policy model, effectively doubling training memory consumption. For DeepSeek-V3-class models with 671B parameters, this was a practical barrier.

## How GRPO Works

### Core Idea

Instead of value estimation via a critic model, GRPO computes advantages via **group-relative comparisons among multiple outputs generated from the same input**.

### Advantage Calculation Formula

For each query $q$, sample $G$ outputs $\{o_1, o_2, \dots, o_G\}$ from the old policy $\pi_{\theta_{old}}$ and compute rewards $\{r_1, r_2, \dots, r_G\}$:

$$A_i = \frac{r_i - \text{mean}(r_1, r_2, \dots, r_G)}{\text{std}(r_1, r_2, \dots, r_G)}$$

- $A_i > 0$: Output better than group average -> reinforce
- $A_i < 0$: Output worse than group average -> suppress
- **Group size G** is a critical hyperparameter (DeepSeek-R1 used large G values)

### GRPO Objective Function

$$\mathcal{J}_{GRPO}(\theta) = \mathbb{E}\left[ \min\left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \ \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta \cdot \mathbb{D}_{KL}(\pi_\theta \| \pi_{ref}) \right]$$

- **Clipping**: Like PPO, clips the probability ratio to $[1-\epsilon, 1+\epsilon]$ to prevent excessive updates
- **KL Regularization**: Penalizes deviation from the reference model (strength controlled by $\beta$)

## Rule-Based Reward Design

A key feature of GRPO in DeepSeek-R1 was the use of **rule-based rewards instead of neural reward models**:

| Reward Type | Description | Purpose |
|-----------|------|------|
| **Accuracy Rewards** | Math: LeetCode-style answer verification. Code: compilation + test passing | Reinforce correct reasoning |
| **Format Rewards** | Whether thoughts are properly placed in `<think>...</think>` tags | Enforce structured reasoning format |

**Why no neural reward model?**: To prevent reward hacking. A neural RM might assign high scores to outputs that "look good" but are actually incorrect. Rule-based rewards only reward verifiably correct answers, avoiding this problem.

## Comparison with PPO

| Aspect | PPO | GRPO |
|------|-----|------|
| Critic Model | **Required** (same size as policy) | **Not needed** |
| Memory Usage | ~2x policy | Policy only |
| Advantage Estimation | Value function (needs training) | Group-relative comparison (computation only) |
| Reward Model | Typically neural | Rule-based recommended |
| Bias | Value function approximation error | Depends on group size |
| Scalability | Bottleneck for large models | Suitable for large models |

## Applications

### DeepSeek-R1 / R1-Zero

- **R1-Zero**: Full training using only GRPO + rule-based rewards. Achieved emergent reasoning.
- **R1 (Stage 2: Reasoning RL)**: GRPO applied to math, code, and logic tasks
- **R1 (Stage 4: General RL)**: GRPO also used for helpfulness and harmlessness alignment (with reward model at this stage)

Training cost: R1-Zero's GRPO training completed in 101K H800 GPU hours ($202K).

### DeepSeek-V3 Post-training

[[concepts/deepseek-v3|DeepSeek-V3]] post-training also uses GRPO, contributing to optimization of reasoning patterns distilled from R1.

## Modern Significance of GRPO

1. **Computational efficiency**: Eliminating the critic model significantly lowers the barrier for RL training of large models
2. **Emergent reasoning**: Key technique enabling autonomous emergence of reasoning through pure RL
3. **Scalability**: The advantage over PPO grows with model size - likely to become the standard for future ultra-large model training
4. **Implementation simplicity**: No need to train or manage a critic model, simplifying the training pipeline

## Limitations and Future Challenges

- **Dependence on group size G**: Small G increases estimation variance; large G increases sampling cost
- **Rule-based reward scope**: Limited to verifiable domains like math and code. Creative tasks still need neural reward models
- **Theoretical guarantees**: Not yet as well-analyzed theoretically as PPO

## Related Pages

- [[concepts/deepseek-r1]] - Original paper introducing GRPO
- [[concepts/deepseek-v3]] - Adopts GRPO for post-training
- [[concepts/post-training/reinforcement-learning]] - Reinforcement learning overview
- [[concepts/post-training/rlhf]] - Reinforcement Learning from Human Feedback
- [[ppo]] - Proximal Policy Optimization (predecessor of GRPO)
- [[reasoning]] - Reasoning capabilities
