---
title: "GRPO RL Training"
type: concept
aliases:
  - grpo-rl-training
  - GRPO
  - Group Relative Policy Optimization
created: 2026-04-25
updated: 2026-06-15
tags:
  - concept
  - reinforcement-learning
  - training
  - fine-tuning
status: complete
related:
  - concepts/multi-teacher-on-policy-distillation
  - concepts/post-training/on-policy-distillation
  - concepts/post-training/sdar-self-distilled-agentic-rl
  - concepts/model-distillation
  - concepts/deepseek-r1
sources:
  - https://arxiv.org/abs/2402.03300
  - raw/papers/2026-05-18_2605.15155_sdar-self-distilled-agentic-rl.md
  - "https://rlhfbook.com/"
---

# GRPO (Group Relative Policy Optimization)

> **GRPO** (Group Relative Policy Optimization) is a reinforcement learning algorithm for post-training LLMs that eliminates the need for a separate value/critic model by computing advantages relative to a group of sampled completions. Popularized by [[concepts/deepseek-r1|DeepSeek-R1]] (Jan 2025), it has become a standard RL backbone for reasoning, agent, and format-enforcement training.

First proposed by Shao et al. (DeepSeek, 2024) in "[DeepSeekMath: Pushing the Limits of Mathematical Reasoning](https://arxiv.org/abs/2402.03300)".

## Core Mechanism

### Advantage Computation

Unlike PPO (Proximal Policy Optimization), which requires a separate value model to estimate baselines, GRPO computes advantages **within a group**:

For each prompt $x$, sample $G$ completions ${y_1, ..., y_G}$. For each completion $y_i$:

$$A_{i,t} = \\frac{r_i - \\text{mean}(\\{r_1,...,r_G\\})}{\\text{std}(\\{r_1,...,r_G\\})}$$

where $r_i$ is the reward assigned to completion $i$ (from a reward model, verifier, or environment).

### Advantages
- **No critic model needed** — saves memory and compute (no separate value network)
- **Group-relative normalization** — naturally handles reward scale drift
- **Simplicity** — fewer hyperparameters than PPO

### Limitations
- **Trajectory-level only** — knows whether a trajectory succeeded, not which tokens were good
- **Group size $G > 1$ required** — can't operate with single samples (unlike OPD-based methods)
- **Reward model dependency** — quality depends on reward/verifier accuracy

## Relationship to RLOO (Leave-One-Out REINFORCE)

The RLHF Book (Lambert, 2026, Ch.6) clarifies that **GRPO and RLOO are closely related algorithms** — both use group-relative advantages without a value network. The key differences are in implementation details:

| Dimension | GRPO | RLOO |
|---|---|---|
| **KL penalty placement** | Applied at the **loss level** (explicit loss term) | Applied to the **reward itself** (folded into reward) |
| **Clipping** | PPO-style ratio clipping | Varies (often no clipping) |
| **Normalization** | Group std normalization | Leave-one-out baseline (mean of *other* samples) |
| **Advantage granularity** | Sequence-level (same value for all tokens) | Sequence-level (same value for all tokens) |

Both assign the **same sequence-level advantage to every token** in a trajectory — unlike PPO, which assigns a different value to every token individually via the value function. This is the fundamental architectural trade-off: token-level precision (PPO with critic) vs. simplicity and memory efficiency (GRPO/RLOO without critic).

## GRPO as an RL Backbone

GRPO forms the RL backbone for many post-training methods:

| Method | What it adds to GRPO | Reference |
|--------|---------------------|-----------|
| **GRPO (vanilla)** | Group-relative advantage | DeepSeekMath (2024) |
| **[[concepts/multi-teacher-on-policy-distillation\|MOPD]]** | Teacher-student log-ratio replaces advantage; $G=1$ possible | Yumo Xu (2026) |
| **[[concepts/post-training/sdar-self-distilled-agentic-rl\|SDAR]]** | Gated OPSD auxiliary loss; GRPO objective untouched | Lu et al. (2026) |
| **Skill-GRPO** | Privileged skills in training context | SDAR paper baseline |

## SDAR's Relationship to GRPO

[[concepts/post-training/sdar-self-distilled-agentic-rl|SDAR]] uses GRPO as its primary RL backbone and adds a gated token-level distillation term:

$$\\mathcal{L}_{\\text{SDAR}} = \\underbrace{\\mathcal{L}_{\\text{GRPO}}}_{\\text{unchanged}} + \\lambda \\cdot \\mathcal{L}_{\\text{SDAR}}^{\\text{aux}}$$

Key insight: **SDAR does not modify GRPO's advantage computation**. The auxiliary distillation term is gated at the token level, ensuring that unreliable teacher signals never corrupt the RL gradient. This is why SDAR avoids the catastrophic collapse that naïve GRPO+OPSD suffers.

## Practical GRPO Training (from Agents MCP-RL Course)

> Practical insights from the [Agents MCP-RL Course](https://agents-mcp-rl.com/) (2025), particularly lessons 3, 4, and 6 covering GRPO training mechanics, debugging, and tooling.

### Batch Structure

A typical GRPO training batch uses **B=4 unique prompts × G=8 rollouts per prompt = 32 total completions per batch**. In practice, smaller group sizes (G=4) also work well and reduce compute cost. The key constraint is that each group must have at least 2 completions with *different rewards* for the advantage normalization to produce meaningful gradients.

### Training Parameters

- **Temperature must be 1** — this is mandatory, not optional. Lower temperatures cause mathematical issues in the GRPO objective because the policy ratio becomes numerically unstable when sampling probabilities are concentrated.
- **Beta=0 is safe with LoRA** — when using LoRA adapters, the reference model is effectively the base model itself, so the KL penalty term (beta) can be set to 0 without risk of catastrophic policy drift.
- **Learning rate is extremely sensitive** — small changes to LR cause dramatically different training outcomes. RL training is far more finicky than SFT; always sweep LR carefully.

### Key Gotchas

- **Disable KV caching during training** — multiple rollouts on the same model must produce *independent* samples. With caching enabled, later rollouts in a group may be contaminated by earlier ones, violating the i.i.d. assumption.
- **Reward std dev collapse** — if reward standard deviation collapses toward 0, the model is output-saturated: it produces nearly identical completions for every prompt. The normalized advantages all become ~0, gradients vanish, and the model stops learning.
- **GRPO updates fewer weights than SFT** — an experimental finding: GRPO updates a much smaller fraction of model weights compared to SFT on the same task. This makes it more surgical but also means it needs sufficient signal diversity in the reward to converge.

### Dataset Size

GRPO is remarkably sample-efficient:

| Training examples | Typical accuracy | Notes |
|---|---|---|
| 1 | ~63% | No catastrophic overfitting (unlike SFT) |
| 4 | ~70% | Powers-of-4 scaling: 1 → 4 → 16 → 64 → 256 → 1024 → 4096 |
| 16–256 | Task-dependent | Sweet spot for most practical tasks |
| 4096 | Diminishing returns | Rarely needed |

Even a single training example yields meaningful learning without the catastrophic overfitting behavior seen in SFT. This is because GRPO explores via rollouts — the model generalizes through diverse sampled completions rather than memorizing a single trajectory.

### SFT as Gateway to RL

SFT should be used to **validate that a task is learnable** before committing to expensive RL runs:

1. Start with SFT (1K–10K examples sweet spot) to confirm the model can learn the target behavior
2. If SFT succeeds → proceed to GRPO for further improvement
3. If SFT fails → the task may be too hard, or the reward signal is ambiguous

**Recommended SFT tools:** TRL, Unsloth, Axolotl, Torchtune. LoRA is sufficient for most task-specific use cases — full fine-tuning is rarely needed.

### Practical Tooling

| Tool | Provider | Role | Key API |
|---|---|---|---|
| **ART** | OpenPipe | End-to-end GRPO training | `TrainableModel` + `LocalBackend` with vLLM → `model.train()` |
| **Verifiers** | Prime Intellect | Reward function framework | `vf.SingleTurnEnv` with `Rubric` functions |
| **SkyPilot** | — | Remote GPU execution | Abstracts cloud GPU provisioning |

ART provides the simplest loop: define a `TrainableModel`, attach a `LocalBackend` backed by vLLM for fast inference, and call `model.train()` with a reward function. Verifiers from Prime Intellect offers a more flexible environment abstraction with rubric-based scoring.

### Sources

- [[transcripts/2025-06-24_willbrown_agents-mcp-rl-lesson3-lecture]]
- [[transcripts/2025-06-26_willbrown_agents-mcp-rl-lesson4-lecture]]
- [[transcripts/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6-lecture]]

See also: [[concepts/agents-mcp-rl-course]], [[concepts/post-training/grpo-infrastructure]], [[concepts/evaluation/reward-engineering]]

## Related Pages

- [[concepts/post-training/sdar-self-distilled-agentic-rl]] — SDAR: gated OPSD on top of GRPO for multi-turn agent training
- [[concepts/multi-teacher-on-policy-distillation]] — MOPD: GRPO with teacher-student log-ratio advantage
- [[concepts/post-training/on-policy-distillation]] — Foundational OPD (reverse-KL distillation)
- [[concepts/model-distillation]] — Broader distillation category
- [[concepts/deepseek-r1]] — DeepSeek-R1, which popularized GRPO for reasoning RL
- [[entities/_index]]


- [[concepts/post-training/llm-as-policy]] — LLM-as-Policy paradigm: the overarching framework connecting GRPO, RLVR, reward model vs critic, and inference-time scaling
- [[concepts/post-training/hands-on-modern-rl]] — walkinglabs open-source curriculum with line-by-line GRPO code implementations
