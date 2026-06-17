---
title: "MAI-Thinking-1"
type: concept
created: 2026-06-17
updated: 2026-06-17
tags:
  - model
  - reasoning
  - moe
  - reinforcement-learning
sources:
  - https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf
---

# MAI-Thinking-1

MAI-Thinking-1 is a frontier reasoning model developed by the Microsoft AI Team, designed for high performance in STEM and coding tasks.

## Technical Specifications
- **Architecture**: 35B active / 1T total parameter Mixture of Experts (MoE).
- **Training**: Developed from scratch using clean, enterprise-grade data (no distillation from third-party models).
- **Context Length**: 256K tokens.
- **Performance**: Achieved 52.8% on SWE-Bench Pro and 97.0% on AIME 2025.

## Development Methodology
- **Hill-Climbing Machine**: Built using a framework that treats model development as an empirical optimization loop.
- **Reinforcement Learning**: Uses specialized RL recipes to teach models to reason via Chains of Thought (CoT) and use external tools.
- **Specialist Models**: The process produced domain-specific models for STEM reasoning, agentic coding, and helpfulness/safety.

## Related Entities
- [[entities/microsoft-ai-team]]
- [[concepts/hill-climbing-machine]]
