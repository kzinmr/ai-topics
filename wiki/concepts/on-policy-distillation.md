---
title: "On-Policy Distillation (OPD)"
type: concept
created: 2026-05-17
updated: 2026-05-17
tags:
  - distillation
  - post-training
  - reinforcement-learning
  - training
  - fine-tuning
aliases:
  - OPD
  - On-Policy Distillation
  - reverse-KL distillation
sources:
  - raw/articles/2025-10-27_thinkingmachines_on-policy-distillation.md
  - https://thinkingmachines.ai/blog/on-policy-distillation/
related:
  - concepts/multi-teacher-on-policy-distillation
  - concepts/model-distillation
  - concepts/post-training-distributional-view
  - concepts/grpo-rl-training
  - entities/thinking-machines-lab
  - entities/kevin-lu
---

# On-Policy Distillation (OPD)

> **On-policy distillation (OPD)** is a post-training technique that combines the best of both worlds: the on-policy relevance of reinforcement learning with the dense, token-level supervision of distillation. It samples trajectories from the **student** model itself and uses a high-performing **teacher** to grade *each token* via reverse KL divergence.

First formally introduced by **Kevin Lu** and **Thinking Machines Lab** in October 2025 ([On-Policy Distillation, DOI: 10.64434/tml.20251026](https://thinkingmachines.ai/blog/on-policy-distillation/)), OPD provides a compute-efficient alternative to both off-policy SFT and on-policy RL for post-training LLMs.

## Core Intuition

OPD fills the gap between two established post-training methods:

| Method | Sampling | Reward Signal | Analogy (Chess) |
|--------|----------|---------------|------------------|
| **Supervised Fine-Tuning (SFT)** | off-policy | dense | Watching a grandmaster play — strong moves in states *you* never reach |
| **Reinforcement Learning (RL)** | on-policy | sparse (1 bit/episode) | Playing games with outcome-only feedback — you know you lost, but not *which* move was bad |
| **On-Policy Distillation (OPD)** | **on-policy** | **dense** (per-token) | A coach grading each of *your own* moves from "blunder" to "brilliant" |

The key insight: **RL searches in the space of semantic strategies, not parameter space**. Once a good strategy is found through expensive RL exploration, OPD serves as a shortcut for learning it — achieving the same performance at 50-100x less compute.

## Mechanism

### Loss Function: Reverse KL Divergence

OPD minimizes the per-token reverse KL divergence between the student's and teacher's distributions:

$$\text{KL}\Bigl(\pi_\theta \lvert\rvert \pi_\text{teacher}\Bigr) = \mathbb{E}_{x \sim {\pi_\theta}} \Bigl[ \log \pi_\theta(x_{t+1} | x_{1..t}) - \log \pi_\text{teacher}(x_{t+1} | x_{1..t}) \Bigr]$$

Key properties of reverse KL:
- **Mode-seeking**: learns one specific behavior (the teacher's) instead of spreading across suboptimal options
- **Unhackable**: low KL *always* corresponds to desirable behavior from the teacher's perspective
- **Reduces exposure bias**: eliminates the compounding error problem of off-policy distillation

### Algorithm (Pseudocode)

```
# 1. Sample trajectories from student
trajectories = student.sample(prompts)

# 2. Teacher computes log-probs on student's own tokens
teacher_logprobs = teacher.compute_logprobs(trajectories)

# 3. Reverse KL = student_logprobs - teacher_logprobs
reverse_kl = trajectories.logprobs - teacher_logprobs

# 4. Set per-token advantage = -reverse_kl, train with RL loss
trajectories.advantages = -reverse_kl
student.train(trajectories, loss_fn="importance_sampling")
```

This is essentially a **one-line change** on top of RL implementations that use KL regularization: swap the KL regularizer model for the teacher model.

## Experimental Results

### Math Reasoning (Qwen3-8B-Base, AIME'24)

Starting from a 400K-prompt SFT checkpoint (60% AIME'24):

| Method | AIME'24 | Compute Efficiency |
|--------|---------|-------------------|
| **SFT-2M** (extrapolated) | ~70% | 1× (baseline) |
| **Reinforcement Learning** | 68% | ~1× |
| **On-Policy Distillation** | **70%** | **9-30× cheaper** |

OPD achieves the same performance in ~150 steps (77K prompts) vs 2M SFT prompts, at 9-30× total compute reduction depending on whether teacher sampling costs are included.

### Efficiency vs RL (Direct Comparison)

Starting from **no SFT** (Qwen3-8B-Base, LoRA rank 128):
- OPD reaches the RL-trained teacher's AIME performance in **7-10× fewer gradient steps**
- Total compute efficiency: **50-100×** reduction
- OPD works at shorter context lengths and smaller batch sizes

### Personalization & Continual Learning

**Problem**: Fine-tuning on new domain knowledge (e.g., company documents) degrades instruction-following behavior learned via RL.

**OPD Solution**: After mid-training on new knowledge, run OPD with the *original* model as teacher to recover post-training behavior:

| Model | Internal QA (Knowledge) | IF-eval (Chat) |
|-------|------------------------|----------------|
| Qwen3-8B (baseline) | 18% | 85% |
| + midtrain (70% docs) | 36% | 79% |
| + midtrain (70%) **+ OPD** | **41%** | **83%** |

OPD recovers nearly full instruction-following without losing newly acquired knowledge — treating the model itself as a reward model.

### Key Finding: SFT on Own Samples Degrades

Even training on a dataset with KL=0 against the teacher (i.e., the teacher's own samples) causes performance degradation. OPD stays on-policy and converges to the teacher's behavior without this regression.

## Intellectual Lineage

OPD draws from and extends:

- **DAGGER** (Ross et al, 2010) — iterative SFT with teacher grading of student-visited states
- **Process Reward Modeling** (Lightman et al, 2023) — per-step scoring in chain-of-thought
- **Agarwal et al. (2023)** — original "On-Policy Distillation of Language Models" paper
- **MiniLLM** (Gu et al, 2023) — reverse KL for knowledge distillation
- **Qwen3 Technical Report (2025)** — demonstrated 74.4% AIME'24 with OPD at 1/10 the cost of RL

## Distinction from Multi-Teacher OPD (MOPD)

OPD (this page) and [[concepts/multi-teacher-on-policy-distillation|MOPD]] are related but distinct:

| Aspect | OPD (Thinking Machines) | MOPD (2026 Frontier Models) |
|--------|------------------------|----------------------------|
| **Introduced** | Oct 2025 | May 2026 |
| **Teachers** | Single teacher | Multiple teachers (SFT + RL specialists) |
| **Primary Use** | Post-training efficiency, continual learning | Capability consolidation across domains |
| **Mathematical Form** | Reverse KL loss | OPD advantage in GRPO loop |
| **Scale** | Single-task (math, assistant) | Multi-domain (Math, Code, Agentic, General) |

MOPD is the **multi-teacher, production-scale** evolution of the core OPD technique. OPD is the foundational concept.

## Discussion Highlights

### RL Searches Strategies; Distillation Learns Them

> "RL explores the space of semantic strategies… Once a good strategy is found, distillation serves as a shortcut for learning it: OPD does not need to model the intermediate strategies during the curriculum of RL, but rather only the final strategy learned."

### Dense Supervision → Order-of-Magnitude Efficiency

RL teaches O(1) bits per episode. Distillation teaches O(N) bits per episode (N = number of tokens). This explains the 50-100× compute efficiency gain.

### Data Efficiency

OPD can train effectively on the *same* prompt across multiple epochs — unlike RL which tends toward memorization. A single prompt with 5,120 graded sequences was sufficient to match teacher performance on AIME'24.

### Continual Learning Promise

OPD always stays on-policy (samples from current student, grades against fixed teacher). This prevents the "off-policy creep" that degrades performance when SFT trains on its own samples.

## Related Pages

- [[concepts/multi-teacher-on-policy-distillation]] — Multi-teacher production-scale evolution (2026)
- [[concepts/model-distillation]] — Broader category of distillation techniques
- [[concepts/post-training-distributional-view]] — SFT vs RL vs OPD through a distributional lens
- [[concepts/grpo-rl-training]] — The RL framework OPD was implemented on top of
- [[entities/thinking-machines-lab]] — Research lab that authored this work
- [[entities/kevin-lu]] — Primary author
