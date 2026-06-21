---
title: "MAI-Thinking-1"
type: entity
created: 2026-06-21
updated: 2026-06-21
tags:
  - microsoft
  - moe
  - reasoning-model
  - grpo
  - scaling
  - training
  - post-training
related:
  - [[entities/microsoft]]
sources:
  - [MAI-Thinking-1: Building a Hill-Climbing Machine](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
---
# MAI-Thinking-1

**MAI-Thinking-1** is a powerful reasoning model developed from scratch by Microsoft AI (MAI). It is a 35B active / 1T total parameter Mixture of Experts (MoE) model.

## Key Innovations
- **Hill-Climbing Machine**: The development treats model creation as a system-level optimization problem, using iterative improvements for rapid scaling.
- **From-scratch Training**: Trained on 30T tokens of clean, enterprise-grade data without synthetic distillation.
- **Reinforcement Learning (RL) Climb**: A robust RL recipe for sustained log-linear performance improvement, leveraging chains of thought (CoT) and tool use.
- **Specialist Models**: The process produced three models for STEM reasoning, agentic coding/tool use, and helpfulness/safety.

## Performance
- **SWE-Bench Pro**: 52.8%
- **AIME 2025**: 97.0%
- **AIME 2026**: 94.5%
- **LiveCodeBench v6**: 87.7%
- Competitive with Claude Sonnet 4.6 across various benchmarks.
