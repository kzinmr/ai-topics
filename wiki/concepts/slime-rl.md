---
title: "slime (Z.ai / Tsinghua)"
type: concept
created: 2026-05-08
updated: 2026-05-08
aliases:
  - slime-rl
  - slime
  - slime-framework
tags:
  - reinforcement-learning
  - rlhf
  - grpo
  - distributed-training
  - training
  - framework
  - agentic-engineering
  - ai-agents
  - open-source
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
---

# slime (Z.ai / Tsinghua)

> **slime** is an open-source RL training framework for LLMs developed by Tsinghua University and Z.ai (THUDM). Designed for **agentic RL**, it takes opinionated yet high-performance choices: Megatron for training and SGLang for inference, with async decoupled generation and training via Ray orchestration.

## Overview

slime (https://github.com/THUDM/slime) was first released in June 2025 and rapidly gained attention with ~1.5k GitHub stars and 33 contributors. Unlike general-purpose frameworks, slime prioritizes **simplicity and high performance for large MoE models** in agentic RL settings by making deliberate, opinionated architectural choices.

Its core design centers on **async RL** — decoupling the training and generation phases so that rollout generation can proceed independently of model updates, maximizing GPU utilization.

## Specifications

| Dimension | Detail |
|-----------|--------|
| **First release** | June 2025 |
| **GitHub stars** | ~1.5k |
| **Contributors** | 33 |
| **Organization** | Tsinghua University + Z.ai (THUDM) |
| **Training backend** | Megatron (opinionated, single choice) |
| **Algorithms** | GRPO, PPO |
| **Inference engine** | SGLang (opinionated, optimized for MoE) |
| **Async RL** | ✅ Built-in (decoupled training + generation) |
| **Environment support** | ✅ Example provided; flexible for custom rollout data |
| **Orchestrator** | Ray |
| **Target domain** | Agentic RL |

## Key Features

### Opinionated Architecture

slime makes three deliberate, fixed choices to reduce complexity:

1. **Megatron** as the sole training backend — optimized for large MoE models (e.g., GLM architectures). No FSDP or DeepSpeed alternatives.
2. **SGLang** as the sole inference engine — chosen for high-throughput generation with MoE architectures.
3. **Async decoupling** — generation workers and training workers operate on independent schedules via a centralized data buffer, enabling continuous rollout generation even during model update steps.

### Centralized Data Buffer

All rollout data flows through a centralized buffer, simplifying the data flow compared to frameworks that require manual sharding and distribution logic. This design makes the codebase small and auditable.

### Designed for Agentic RL

slime targets **agentic RL** scenarios (multi-turn, tool-using agents) rather than pure mathematical reasoning RL. It includes example environments for custom rollout data generation and supports flexible environment integration.

## Strengths

- **Simplicity**: Small, readable codebase with clear architectural boundaries
- **High performance for MoE models**: Megatron + SGLang combination is optimized for sparse models
- **Reduced complexity**: Opinionated choices eliminate configuration surface area
- **Async-first**: Built from the ground up for decoupled training/generation

## Weaknesses

- **Megatron-only**: No support for FSDP, DeepSpeed, or TorchTitan. Users locked into Megatron ecosystem.
- **Very new**: Released June 2025; limited community ecosystem, documentation, and production track record
- **Smaller ecosystem**: Fewer third-party integrations and examples compared to veRL or TRL
- **SGLang-only inference**: Users cannot switch to vLLM or other engines

## Use Cases

- **Agentic RL research** targeting tool-use, multi-turn agents
- **MoE model RL training** (e.g., GLM family) where Megatron is the natural backend
- **Teams prioritizing simplicity** over flexibility — want a "batteries included" RL stack with minimal configuration

## Comparison with Other Frameworks

| Framework | Training Backends | Inference Engines | Flexibility | Maturity |
|-----------|-------------------|-------------------|-------------|----------|
| **slime** | Megatron only | SGLang only | Low (opinionated) | Very new (Jun 2025) |
| **veRL ([[concepts/hybrid-flow]])** | FSDP, Megatron, TorchTitan | vLLM, SGLang, HuggingFace TGI | High | Moderate (2024+) |
| **TRL ([[concepts/fine-tuning/trl]])** | FSDP (HuggingFace-native) | HuggingFace generate | Moderate | High (mature) |
| **[[concepts/grpo]] training stacks** | Varies by framework | Varies | Varies | N/A |

## Relationship to DeepSeek-R1

slime implements [[concepts/grpo]] (Group Relative Policy Optimization) — the same core algorithm used by [[concepts/deepseek-r1]] for reasoning RL. However, while [[concepts/deepseek-r1]] used [[concepts/hybrid-flow|veRL]]'s Flexible architecture, slime targets a different niche: agentic scenarios with opinionated MoE-optimized stack choices rather than general-purpose multi-backend flexibility.

## Related Pages

- [[concepts/grpo]] — Group Relative Policy Optimization (core algorithm)
- [[concepts/fine-tuning/trl]] — HuggingFace TRL, the mature general-purpose RLHF framework
- [[concepts/hybrid-flow]] — veRL (HybridFlow), the flexible multi-backend RL framework used by DeepSeek-R1
- [[concepts/deepseek-r1]] — DeepSeek-R1 reasoning model and its GRPO training methodology
- [[concepts/multi-turn-tool-use-rl]] — Multi-turn tool use with RL, closely related to agentic RL use cases

## References

- [slime GitHub](https://github.com/THUDM/slime)
- [Z.ai (THUDM)](https://z.ai)
- [Anyscale: Open-Source RL Libraries for LLMs (Jul 2025)](raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md)
