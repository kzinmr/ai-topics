---
title: "MAI-Thinking-1"
type: concept
created: 2026-06-18
updated: 2026-06-18
tags:
  - microsoft
  - moe
  - reasoning-model
  - scaling
aliases: []
sources:
  - [MAI-Thinking-1: Building a Hill-Climbing Machine](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
---
# MAI-Thinking-1

MAI-Thinking-1 is a powerful reasoning model developed from scratch by the Microsoft AI Team. It is designed to compete with frontier models on STEM reasoning and coding tasks.

## Technical Details
- **Architecture**: 35B active parameters / 1T total parameter Mixture of Experts (MoE).
- **Training Strategy**: Trained from scratch on clean, enterprise-grade data without distillation from third-party models.
- **Methodology**: Utilizes a "hill-climbing machine" approach, leveraging reinforcement learning (RL) for sustained log-linear performance improvement.
- **Performance**:
  - SWE-Bench Pro: 52.8%
  - AIME 2025: 97.0%
  - LiveCodeBench v6: 87.7%

## Sources
- [MAI-Thinking-1: Building a Hill-Climbing Machine](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
