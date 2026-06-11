---
title: "RL Algorithms for LLM Training"
type: concept
created: 2026-06-08
updated: 2026-06-08
tags:
  - reinforcement-learning
  - training
  - alignment
  - rlhf
  - grpo
  - importance-sampling
  - optimization
sources:
  - raw/articles/2026-06-08_arjunkocher_rl-algorithm-questions.md
  - https://www.k-a.in/rl-algo.html
---

# RL Algorithms for LLM Training

> A comprehensive overview of reinforcement learning algorithms used in LLM post-training, covering policy optimization, advantage estimation, reward design, and the trade-offs between PPO, GRPO, and their variants.

Based on [Arjun Kocher's RL Algorithm Q&A](https://www.k-a.in/rl-algo.html), compiled from Xiuyu Li's question set.

## Actor-Critic vs Pure Policy Methods

**Actor-Critic** combines a parameterized policy (actor) with a value function (critic):
- Handles continuous/large action spaces naturally (no argmax over vocabulary needed)
- Lower variance than pure policy gradient ([[concepts/reinforcement-learning|REINFORCE]]) because the critic serves as a baseline
- Enables bootstrapping — credit assignment doesn't require waiting for full episode completion

**Why GRPO drops the critic**: In LLM RL, the value function over token sequences is hard to learn well. GRPO replaces the critic with a **group mean baseline**, avoiding the need for a value network entirely. See [[concepts/grpo]].

## KL Divergence, Cross Entropy, and MLE

These three concepts are mathematically connected:

$$D_{KL}(P \| Q) = H(P, Q) - H(P)$$

Since $H(P)$ (entropy of the data distribution) is constant, minimizing KL divergence from data to model is equivalent to minimizing cross-entropy, which is equivalent to **MLE** (maximum likelihood estimation).

**KL direction in RLHF**: The RLHF penalty uses **reverse KL** (model-seeking), which causes RL'd models to lose diversity — the policy chases high-reward modes and abandons broad coverage. DPO inherits this reverse KL behavior.

## Reward Design Taxonomy

| Reward Type | Domain | Characteristics |
|---|---|---|
| **Verifiable** | Math, code | Clean signal via unit tests and symbolic checks |
| **LLM-as-judge** | Writing, open-ended | Noisy, gameable, prone to reward hacking |
| **Format rewards** | Structural | Should decay after format is learned to prevent gaming |
| **Outcome (ORM)** | General | Rewards final answer correctness |
| **Process (PRM)** | Reasoning | Rewards intermediate steps |

Most large-scale LLM RL uses ORMs. For verifiable domains (math/code), rule-based rewards avoid neural reward model vulnerabilities entirely (see [[concepts/grpo#Rule-Based Reward Design]]).

## Importance Sampling and Rejection Sampling

**Importance Sampling (IS)** corrects off-policy data by reweighting with the IS ratio:

$$\rho = \frac{\pi_\theta(a|s)}{\beta(a|s)}$$

- PPO uses a **clipped** IS ratio to bound variance
- GRPO uses IS implicitly (old policy generates rollouts, new policy trains on them)
- High variance when $\pi_\theta$ and $\beta$ diverge significantly

**Rejection Sampling**: Filtering strategy — best-of-N, dropping too-easy/hard prompts, or ReST-style (sample → keep good ones → refit).

## Advantage Estimation

### PPO: Generalized Advantage Estimation (GAE)

$$A_t^{GAE} = \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}, \quad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

Requires a learned value function (critic). Advantages are typically whitened (mean-subtracted, std-divided) per minibatch.

### GRPO: Group-Normalized Reward

$$A_i = \frac{r_i - \text{mean}(\{r_j\})}{\text{std}(\{r_j\})}$$

No value network — baseline is the group mean. See [[concepts/grpo]] for full mechanics.

### Why Subtract a Baseline?

Subtracting any baseline $b$ from the policy gradient is unbiased (because $\mathbb{E}[\nabla \log \pi \cdot b] = 0$) but reduces variance dramatically. The optimal baseline is $\mathbb{E}[G_t]$, which the value function approximates.

### Std Normalization Trade-offs

- **Pro**: Stabilizes training by keeping gradient magnitudes consistent regardless of reward scale
- **Con**: Distorts advantage when group variance is near-zero — systematically upweights low-variance prompts (all-correct or all-wrong groups carry no learning signal)
- **Dr.GRPO** and **DAPO** clip or skip updates for such zero-variance groups

## PPO Clipping Mechanics

$$L^{CLIP}(\theta) = \mathbb{E}_t \left[ \min\left( r_t(\theta) A_t, \ \text{clip}(r_t(\theta), 1{-}\epsilon, 1{+}\epsilon) A_t \right) \right]$$

- **$A_t > 0$ (good action)**: If ratio exceeds $1+\epsilon$, the clipped term is smaller → prevents overconfident updates
- **$A_t < 0$ (bad action)**: If ratio goes below $1-\epsilon$, the clipped term is larger (less negative) → doesn't let policy escape punishment
- **Without clipping**: Pure IS-weighted gradient can cause catastrophically large steps and policy collapse (why TRPO used hard KL constraint)

### CISPO (Clipped IS Policy Optimization)

Instead of clipping the objective, CISPO clips the IS ratio **before computing the gradient** — clips $r_t$ to $[1-\epsilon, 1+\epsilon]$ in gradient computation but not in loss value. Avoids the **flat gradient problem** in PPO where clipped samples contribute zero gradient despite containing information.

## KL Penalty in GRPO

Per-token KL between current policy and frozen reference:

$$\text{KL}(\pi_\theta \| \pi_{ref}) = \sum_t \left[ \pi_\theta(a_t|s_t, a_{<t}) \log \frac{\pi_\theta(a_t|s_t, a_{<t})}{\pi_{ref}(a_t|s_t, a_{<t})} \right]$$

**Why it exists**: Prevents policy drift and reward hacking. Requires a reference model forward pass.

**Why DAPO/GSPO remove it**: In RLVR (RL with Verifiable Rewards), the verifier self-insures against hacking — a unit test can't be gamed by drifting from the reference. The KL becomes pure drag, preventing the model from learning new domains. The clip already bounds step size, and removing the reference model saves memory.

## RL Training vs Test-Time Scaling

| Dimension | RL Training | Test-Time Scaling |
|---|---|---|
| **Nature** | Learning (weight updates) | Exploration/Search (inference budget) |
| **Exploration** | Stochastic sampling during rollouts | Best-of-N, beam search, MCTS, sequential revision |
| **Policy change** | Yes — reshapes weights | No — uses fixed policy more extensively |
| **Failure mode** | Zero-reward prompts are never learned | Can't find trajectories the policy never samples |

## Key Algorithm Variants

| Algorithm | Critic | KL Penalty | Clipping | Key Innovation |
|---|---|---|---|---|
| **PPO** | Required (GAE) | Optional | Objective clipping | Standard RLHF backbone |
| **GRPO** | None (group mean) | Yes (reference) | Like PPO | Eliminates critic via group normalization |
| **DAPO** | None | Removed | Clipping | Verifiable rewards replace KL |
| **Dr.GRPO** | None | Yes | Clips zero-variance groups | Handles low-variance groups |
| **CISPO** | Varies | Varies | IS ratio clipping (not objective) | Maintains gradient flow for clipped samples |

## Related Pages

- [[concepts/grpo]] — GRPO detailed mechanics and DeepSeek-R1 application
- [[concepts/grpo-rl-training]] — GRPO as an RL backbone with variants
- [[concepts/rlhf]] — RLHF overview
- [[concepts/reinforcement-learning]] — RL fundamentals
- [[concepts/evaluation/reward-hacking]] — Reward hacking vulnerabilities
