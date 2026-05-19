---
title: "Siyan Zhao"
type: entity
created: 2026-05-18
updated: 2026-05-18
tags:
  - person
  - training
sources:
  - https://siyan-zhao.github.io/blog/2026/opsd/
  - https://siyan-zhao.github.io/
aliases:
  - Siyan Zhao
status: stub
---

# Siyan Zhao

> **Siyan Zhao** is a researcher at UCLA and Meta Superintelligence Labs, known for the **On-Policy Self-Distillation (OPSD)** technique for LLM reasoning post-training (2026).

## Bio

- **Affiliation**: UCLA (PhD student) / Meta Superintelligence Labs
- **Research focus**: LLM post-training, reasoning, distillation, reinforcement learning
- **Notable work**: Self-Distilled Reasoner — On-Policy Self-Distillation (OPSD)
- **Website**: https://siyan-zhao.github.io/

## Key Contributions

### On-Policy Self-Distillation (OPSD)

Lead author of the OPSD paper (2026), introducing a post-training method where a single LLM serves as both student and teacher — the teacher has privileged access to ground-truth solutions and provides dense token-level supervision on the student's own on-policy trajectories.

The technique achieves GRPO-level reasoning performance at ~1/64 the token cost (1 rollout vs 8, 1024 tokens vs 16k per problem).

See [[concepts/on-policy-self-distillation]] for the full method.

## Related Pages

- [[concepts/on-policy-self-distillation]] — OPSD technique
- [[concepts/sdar-self-distilled-agentic-rl]] — SDAR: OPSD adapted for agent training
- [[concepts/on-policy-distillation]] — Broader OPD paradigm
- [[concepts/grpo-rl-training]] — GRPO, the baseline OPSD improves upon
