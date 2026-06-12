---
title: "Verifiers"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - reinforcement-learning
  - fine-tuning
  - training
  - framework
  - agentic-engineering
  - ai-agents
  - reasoning
  - comparison
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
---

# Verifiers

Verifiers is a **lightweight RL training library built on top of [[concepts/post-training/trl|TRL]]**, first released in February 2025. It extends HuggingFace's TRL `Trainer` with **environment support** and **multi-turn tool use**, specifically addressing TRL's limitations for agentic and reasoning-focused RL. Despite its simplicity, Verifiers has gained rapid adoption with ~2.9k GitHub stars.

## Overview

Verifiers (GitHub: [verifiers-ai/verifiers](https://github.com/verifiers-ai/verifiers)) takes the approach of **extending rather than replacing** TRL. It inherits TRL's familiar HuggingFace `Trainer` API while adding the key missing pieces for modern RL training: environments for multi-turn interactions, tool-calling support, and async inference via vLLM. This makes it an excellent **on-ramp** for researchers who are already comfortable with the HuggingFace ecosystem.

| Attribute | Detail |
|-----------|--------|
| **Organization** | verifiers-ai (community) |
| **First Release** | February 2025 |
| **GitHub Stars** | ~2.9k |
| **Contributors** | ~26 |
| **Training Backend** | HuggingFace Trainer (TRL-based) |
| **Algorithms** | GRPO |
| **Inference Engine** | vLLM, OpenAI (external API) |
| **Async Rollouts** | ✅ Supported |
| **Environment** | ✅ Custom environment support |
| **Orchestrator** | None (uses TRL's simple single-process approach) |

## Key Features

### Built on TRL
Verifiers inherits all of TRL's infrastructure by building on top of it:
- **HuggingFace Trainer**: Familiar training loop, checkpointing, and logging
- **Model Compatibility**: Works with any HuggingFace model
- **Simple Integration**: Drop-in for teams already using TRL

### Environment & Multi-Turn Support
The primary value-add over base TRL is **environment integration**:
- **Custom Environments**: Define environments for agentic training loops
- **Multi-Turn Tool Use**: Agents can call tools across multiple interaction turns
- **Async Rollouts**: Parallel inference with vLLM for efficient data generation

### GRPO-First Design
Verifiers focuses exclusively on [[concepts/post-training/grpo|GRPO]], the algorithm popularized by [[concepts/deepseek-r1|DeepSeek-R1]]:
- **No Critic Model**: Reduced memory footprint compared to PPO-based approaches
- **Group-Relative Scoring**: Multiple outputs per prompt, scored relative to group mean
- **Rule-Based Rewards**: Designed for verifiable reward functions (math, code, format checking)

### Inference Options

| Engine | Use Case |
|--------|----------|
| **vLLM** | High-throughput local inference with async batching |
| **OpenAI API** | Remote inference via external API (less efficient but simpler setup) |

## Architecture Comparison

| Layer | TRL | Verifiers |
|-------|-----|-----------|
| **Training Loop** | HF Trainer | HF Trainer (same) |
| **Algorithm** | SFT, DPO, GRPO, PPO, KTO | GRPO only |
| **Environment** | ❌ None | ✅ Custom environments |
| **Multi-Turn** | ❌ Single-turn only | ✅ Multi-turn tool use |
| **Async Rollouts** | ❌ | ✅ via vLLM |
| **Scalability** | Single-node focused | Single-node (inherits TRL limits) |

## Strengths & Weaknesses

| Strengths | Weaknesses |
|-----------|------------|
| Simple, familiar HF Trainer API | GRPO only (no PPO, DPO, SFT) |
| Adds environment + multi-turn to TRL | Built on TRL's trainer — less scalable than Megatron-based alternatives |
| Popular among researchers (2.9k ⭐) | Single-node focused |
| Async rollouts with vLLM | Smaller feature set vs [[concepts/hybrid-flow|veRL]] or NeMo-RL |
| Easy to adopt for HF ecosystem users | Inherits TRL's architectural limitations |

## Comparison with Related Frameworks

| Aspect | Verifiers | [[concepts/post-training/trl|TRL]] | [[concepts/hybrid-flow|veRL]] | NeMo-RL |
|--------|-----------|-----|------|---------|
| Complexity | Low | Low | High | Medium |
| Algorithms | GRPO only | SFT, DPO, GRPO, PPO | SFT, DPO, GRPO, PPO | SFT, DPO, GRPO |
| Multi-Turn | ✅ | ❌ | 🚧 | ✅ |
| Scale Ceiling | Single-node | Single-node | Multi-node | Multi-node |
| Best For | Quick GRPO experiments | General RLHF | Large-scale production | Modular production RL |

## Use Cases

- **Reasoning RL**: GRPO-based training with verifiable rewards (math, code)
- **Agentic RL research**: Multi-turn tool use in custom environments
- **Quick experimentation**: Familiar HF Trainer API for rapid prototyping
- **TRL migration path**: Add environments and multi-turn to existing TRL workflows

## Related Pages

- [[concepts/post-training/grpo]] — GRPO algorithm details (the only algorithm Verifiers supports)
- [[concepts/post-training/trl]] — HuggingFace TRL (the library Verifiers extends)
- [[concepts/hybrid-flow]] — veRL (more scalable alternative for production)
- [[concepts/deepseek-r1]] — DeepSeek-R1's GRPO-based reasoning training
