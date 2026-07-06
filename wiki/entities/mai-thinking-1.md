---
title: "MAI-Thinking-1"
type: entity
created: 2026-06-21
updated: 2026-07-06
tags:
  - microsoft
  - model
  - reasoning-model
  - training
  - optimization
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

## Key Ideas
- **Hill-Climbing Machine**: Treating model development as an iterative, system-level optimization problem.
- **Reinforcement Learning (RL)**: Using a robust RL recipe to achieve sustained log-linear performance improvements.
- **From-Scratch Training**: Utilizing clean, enterprise-grade data without distillation from third-party models.
- **STEM Reasoning**: High performance on benchmarks like AIME 2025 and SWE-Bench Pro.

## Training Infrastructure
- **YOLO Framework**: MAI's in-house "You Only Launch Once" distributed training framework built on PyTorch, supporting pre-training, mid-training, and RL phases with custom kernels, parallelism, and fault-tolerance.
- **Cluster**: 8K GB200 GPUs, single logical cluster, one site (Phoenix, AZ)
- **Goodput**: 90.0% at 8K GPUs — primary production KPI
- **Determinism**: First-class infrastructure property; eliminates silent data corruption
- **Serving**: SGLang
- **Inference hardware**: MAIA-200 (Microsoft custom silicon) — 40% higher token generation throughput per Watt vs GB200

## Safety & Red Teaming
- Continuous red-teaming throughout model development to surface and remediate vulnerabilities
- Internal and independent red teaming programs
- Safety benchmarks developed for internal grounding
- Helpfulness & Safety RL climb trains human preference and safety signals alongside reasoning

## Sources
- [MAI-Thinking-1: Building a Hill-Climbing Machine — Microsoft AI Technical Report](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)
