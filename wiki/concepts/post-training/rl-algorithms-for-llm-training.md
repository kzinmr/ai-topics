---
title: "RL Algorithms for LLM Training"
type: concept
created: 2026-06-08
updated: 2026-06-15
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
  - "https://rlhfbook.com/"
  - https://www.k-a.in/rl-algo.html
---

# RL Algorithms for LLM Training

> A comprehensive overview of reinforcement learning algorithms used in LLM post-training, covering policy optimization, advantage estimation, reward design, and the trade-offs between PPO, GRPO, and their variants.

Based on [Arjun Kocher's RL Algorithm Q&A](https://www.k-a.in/rl-algo.html), compiled from Xiuyu Li's question set.

## Actor-Critic vs Pure Policy Methods

**Actor-Critic** combines a parameterized policy (actor) with a value function (critic):
- Handles continuous/large action spaces naturally (no argmax over vocabulary needed)
- Lower variance than pure policy gradient ([[concepts/post-training/reinforcement-learning|REINFORCE]]) because the critic serves as a baseline
- Enables bootstrapping — credit assignment doesn't require waiting for full episode completion

**Why GRPO drops the critic**: In LLM RL, the value function over token sequences is hard to learn well. GRPO replaces the critic with a **group mean baseline**, avoiding the need for a value network entirely. See [[concepts/post-training/grpo]].

### Reward Model vs Critic (Value Function)

These two components are often confused but serve fundamentally different roles in LLM-RL:

| Dimension | Reward Model $R(s, a)$ | Critic / Value Function $V^\pi(s_t)$ |
|---|---|---|
| **What it evaluates** | The completed output (final answer) | The *in-progress* state (partial trajectory) |
| **Time orientation** | Past/present (what was produced) | Future (what can still be expected) |
| **When it fires** | Once, at end of trajectory | At every token step |
| **Formula** | $R(s, a)$ or $R(\tau)$ | $V^\pi(s_t)$ |
| **Role in credit assignment** | "This answer scored 0.85" | "From this point, ~0.95 is achievable" |

**Why the critic is needed for credit assignment**: When a 100-token response scores 0 from the reward model, which token caused the failure? The critic tracks how the expected value shifts at each step:

- Tokens 1–20: expected value stays at 0.9 (on track)
- Token 21: expected value crashes from 0.9 to 0.1

This pinpoints the exact action that derailed the trajectory — the reward model alone cannot provide this granularity.

**How GRPO sidesteps this**: By generating multiple completions per prompt and comparing their final rewards, GRPO uses the group's relative ranking as a coarse substitute for per-token value estimation. This loses token-level resolution but eliminates the expensive critic model entirely.

For the broader paradigm context of this convergence toward implicit modeling, see [[concepts/post-training/llm-as-policy]].

### Reward Model Taxonomy: RM, ORM, PRM, Value Function

The RLHF Book (Lambert, 2026, Ch.5) provides a clear four-way taxonomy of reward-related models in LLM-RL — the boundaries between these are not always clear-cut:

| Model | Question It Answers | Output | Training Signal | When It Fires |
|---|---|---|---|---|
| **Reward Model (RM)** | "How good is this whole answer?" | Scalar per response | Human preference pairs (Bradley-Terry) | End of trajectory |
| **Outcome RM (ORM)** | "Is the final answer correct?" | Scalar per response (or per-token) | Ground-truth labels (correct/incorrect) | End of trajectory |
| **Process RM (PRM)** | "Are the reasoning steps sound?" | Scalar per step | Step-level human or automated labels | Every reasoning step |
| **Value Function** | "How much reward remains from here?" | Scalar per token | On-policy rollouts (temporal difference) | Every token step |

Key distinction: **ORMs and Value Functions both produce per-token outputs but differ in what they predict and how targets are generated.** An ORM learns $p(\text{correct}_t)$ from offline labels; a value function learns the expected remaining return $V(s_t) = \mathbb{E}[\sum_{k \geq t} r_k]$ from on-policy rollouts. As Lambert notes: *"If you define a dense token reward $r_t = \mathbf{1}[\text{correct}]$ and use $\gamma=1$, then an ORM is learning $r_t$ while the value head is learning the remaining-sum $\sum_{k \geq t} r_k$."*

Most large-scale LLM RL uses ORMs (outcome-only). For verifiable domains (math/code), rule-based rewards bypass the learned RM entirely — see [[concepts/post-training/rlvr]].

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

Most large-scale LLM RL uses ORMs. For verifiable domains (math/code), rule-based rewards avoid neural reward model vulnerabilities entirely (see [[concepts/post-training/grpo#Rule-Based Reward Design]]).

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

No value network — baseline is the group mean. See [[concepts/post-training/grpo]] for full mechanics.

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

- [[concepts/post-training/llm-as-policy]] — LLM-as-Policy paradigm: the overarching framework connecting these algorithms, with reward model vs critic distinction and DPO/GRPO convergence analysis
- [[concepts/post-training/grpo]] — GRPO detailed mechanics and DeepSeek-R1 application
- [[concepts/post-training/grpo-rl-training]] — GRPO as an RL backbone with variants
- [[concepts/post-training/rlhf]] — RLHF overview
- [[concepts/post-training/reinforcement-learning]] — RL fundamentals
- [[concepts/evaluation/reward-hacking]] — Reward hacking vulnerabilities
