---
title: "Reinforcement Learning"
type: concept
tags:
  - concept
  - reinforcement-learning
status: complete
description: "Fundamental concepts of RL applied to LLM training."
created: 2026-04-14
updated: 2026-06-08
related:
  - "[[concepts/post-training/rlhf]]"
  - "[[concepts/gpt/chatgpt-memory-bitter-lesson]]"
sources:
  - raw/articles/2026-06-08_arjunkocher_rl-algorithm-questions.md
---

# Reinforcement Learning

> Core RL concepts as applied to LLM post-training and alignment.

## Overview

Reinforcement Learning in the LLM context covers policy optimization (PPO, GRPO, DPO), reward design (verifiable, LLM-as-judge, process vs outcome), advantage estimation (GAE, group-normalized), and the exploration-exploitation trade-off between training-time and test-time scaling.

## Key Topics

- [[concepts/post-training/rl-algorithms-for-llm-training]] — Comprehensive Q&A covering Actor-Critic, PPO, GRPO, KL divergence, advantage estimation, reward design, and algorithm variants
- [[concepts/post-training/grpo]] — Group Relative Policy Optimization (DeepSeek-R1)
- [[concepts/post-training/grpo-rl-training]] — GRPO as an RL backbone with method variants
- [[concepts/post-training/rlhf]] — Reinforcement Learning from Human Feedback
- [[concepts/trl-transformer-reinforcement-learning]] — TRL library for RL-based LLM training

## Related Pages

- [[concepts/evaluation/reward-hacking]] — Reward hacking vulnerabilities in RL training
- [[concepts/gpt/chatgpt-memory-bitter-lesson]] — The Bitter Lesson applied to RL
