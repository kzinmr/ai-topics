---
title: Seirênes (Adversarial Self-Play for LLM Reasoning)
created: 2026-05-21
updated: 2026-05-21
type: concept
tags: [concept, reasoning, reinforcement-learning, adversarial, training, grpo, robustness, self-play, evaluation]
sources: [raw/articles/2026-05-21_seirenes.md]
---

# Seirênes: Adversarial Self-Play with Evolving Distractions

Seirênes is a **self-play RL framework** that transforms contextual interference (misleading hints, distracting context) from a failure mode into an **internal training signal** for more robust reasoning. A single shared-parameter LLM plays two competing roles — Adversary and Reasoner — in a co-evolutionary loop.

Named after the **Seirênes (Sirens)** of Greek mythology, whose alluring songs misled sailors — here, misleading hints tempt the Reasoner to follow plausible but wrong paths.

**Paper**: arXiv:2605.11636v1 (May 2026) | **Code**: [MiliLab/Seirenes](https://github.com/MiliLab/Seirenes)

## The Problem

Modern reasoning LLMs trained with RLVR (Reinforcement Learning with Verifiable Rewards) exhibit fragility under non-idealized contexts:

- Structural reformulations of math problems reduce accuracy by **27–31%**
- Irrelevant context silently redirects chain-of-thought
- Irrelevant retrievals drop accuracy from **96% to 65%**

Seirênes exploits these vulnerabilities as an **online curriculum** rather than just testing robustness.

## Method

### Self-Play Loop

1. **R1 (Clean reasoning)**: Reasoner solves original question q → binary verifiable reward
2. **R2 (Adversarial hints)**: Adversary generates G₂ misleading hints {h_k}, each appended to form q⊕h_k
3. **R3 (Hint-conditioned reasoning)**: Reasoner solves q⊕h_k under adversarial context → reward

Both roles share the same model parameters, differentiated only by **role-conditioned prompts**.

### Three Objective Streams

Uses **GRPO** (Group Relative Policy Optimization) as the base RL algorithm:

- **Reasoner (Clean)** — Maximize L_clean on plain question rollouts
- **Adversary** — Minimize L_adv (negative GRPO objective). Reward: `R_Adv(q,h_k) = 1[p_clean(q) > p_hinted(q,h_k)]` — rewarded when it trips up the Reasoner relative to clean baseline
- **Reasoner (Robustness)** — Maximize L_robust on hinted rollouts

### Orchestration

- **Separate update streams**: Gradients kept separate via per-stream FIFO buffers, preserving credit assignment
- **Bounded FIFO buffers**: Carry over unused groups to later steps, avoiding wasteful "reject-and-regenerate" filtering
- **Latency-aware scheduling**: R1 and R2 concurrent; R3 only depends on R2 outputs — collapses critical path to ≈ T_R1 + T_R3
- **Mastery-aware sampling**: Questions too easy (all rollouts correct) moved to "mastered set" M and deprioritized, saving compute

## Results

Tested on Qwen2.5-7B-Instruct, Qwen3-4B-Instruct, and Qwen3-30B-A3B-Instruct backbones with DAPO-Math-17K and OpenR1-Math training data. Seirênes-trained models achieve stronger robustness against adversarial context without sacrificing clean accuracy.

## Significance

Seirênes addresses a fundamental limitation of current reasoning LLM training: models overfit to clean, idealized problem formats and fail when context is noisy or adversarial. By making the training process itself adversarial, it forces the model to develop reasoning strategies robust to distraction — moving beyond superficial pattern matching toward genuine logical reasoning.

The framework is complementary to other RL training approaches: the adversarial self-play loop can be added on top of existing GRPO/RLVR pipelines.

## Related Pages

- [[concepts/grpo-rl-training]] — GRPO and reinforcement learning for LLMs
- [[concepts/reasoning]] — Reasoning in LLMs
- [[concepts/adversarial]] — Adversarial approaches in AI
- [[concepts/rlhf]] — RLHF and related RL training methods
- [[concepts/robustness]] — Robustness in AI systems
- [[concepts/test-time-scaling]] — Test-time compute scaling
