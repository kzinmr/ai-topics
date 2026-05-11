---
title: "SkyRL (UC Berkeley / NovaSky)"
type: concept
created: 2026-05-08
updated: 2026-05-08
aliases:
  - skyrl
  - nova-sky-rl
  - uc-berkeley-skyrl
tags:
  - reinforcement-learning
  - fine-tuning
  - training
  - framework
  - agentic-engineering
  - ai-agents
  - open-source
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
---

# SkyRL (UC Berkeley / NovaSky)

> **SkyRL** is an open-source RL training framework for LLMs from UC Berkeley's NovaSky AI lab. Designed for **agentic and multi-turn RL**, SkyRL prioritizes **flexibility** — supporting sync/async pipelining, colocated or disaggregated generation/training, multiple weight sync methods, and both integrated and external inference engines.

## Overview

SkyRL (https://github.com/NovaSky-AI/SkyRL) launched in June 2025 with ~0.8k GitHub stars and 18 contributors. Its core philosophy is **"simple yet flexible"** — providing a clean API that adapts to diverse agentic RL scenarios rather than locking users into a single architectural pattern.

Unlike opinionated frameworks, SkyRL supports **multiple deployment topologies**: generation and training can run on the same GPUs (colocated) or on separate clusters (disaggregated), with synchronous or asynchronous pipelining between them.

## Specifications

| Dimension | Detail |
|-----------|--------|
| **First release** | June 2025 |
| **GitHub stars** | ~0.8k |
| **Contributors** | 18 |
| **Organization** | UC Berkeley (NovaSky AI) |
| **Training backends** | FSDP, DeepSpeed |
| **Algorithms** | GRPO, PPO |
| **Inference engines** | vLLM, SGLang, OpenAI-compatible (external) |
| **Async RL** | ✅ Built-in (sync and async pipelining) |
| **Environment support** | ✅ Custom environment support |
| **Orchestrator** | Ray |
| **Target domain** | Agentic / multi-turn RL |

## Key Features

### Deployment Flexibility

SkyRL's standout feature is its support for multiple deployment topologies:

| Topology | Description | Use Case |
|----------|-------------|----------|
| **Colocated** | Generation and training on same GPU set | Small-scale experiments, single-cluster setups |
| **Disaggregated** | Generation and training on separate GPU clusters | Large-scale production, different GPU types for generation vs training |
| **External inference** | Inference via OpenAI-compatible API (remote) | Offloading generation to external services |

### Pipeline Modes

- **Synchronous**: Generation completes fully before training begins. Simplest to reason about.
- **Asynchronous**: Generation and training run concurrently with a data buffer between them. Maximizes GPU utilization at the cost of training on slightly stale rollout data.

### Multiple Weight Sync Methods

SkyRL supports several strategies for synchronizing weights between the training model and inference/generation model:

- Direct weight transfer (colocated)
- NCCL broadcast
- Checkpoint-based sync
- HTTP-based weight serving

### Multi-Turn Agentic Support

SkyRL was built with **agentic RL** in mind. It includes example scripts for multi-turn tool-use scenarios and supports custom environment integration, making it suitable for training agents that interact with external tools across multiple turns.

## Strengths

- **Maximum flexibility**: Sync/async, colocated/disaggregated, integrated/external inference — choose the topology that fits your infrastructure
- **Multi-backend training**: FSDP and DeepSpeed both supported
- **Multi-engine inference**: vLLM, SGLang, or external OpenAI-compatible APIs
- **Agentic-first design**: Built for multi-turn, tool-using agent scenarios
- **Academic origin**: UC Berkeley pedigree with strong research community ties

## Weaknesses

- **Very new**: Released June 2025; limited production track record
- **Smaller ecosystem**: Fewer integrations, examples, and third-party contributions compared to veRL or TRL
- **Less mature documentation**: Rapidly evolving API may have gaps in documentation
- **No Megatron backend**: Lacks support for the Megatron training stack used by some MoE models

## Use Cases

- **Agentic RL research** requiring flexible deployment topologies
- **Multi-turn tool-use training** for LLM agents
- **Heterogeneous GPU clusters** where generation and training benefit from different hardware
- **Teams needing to switch between sync/async** pipelining without changing codebases
- **External inference setups** where generation is offloaded to API services

## Comparison with Other Frameworks

| Framework | Topologies | Training Backends | Inference Engines | Flexibility |
|-----------|-----------|-------------------|-------------------|-------------|
| **SkyRL** | Colocated, disaggregated, external | FSDP, DeepSpeed | vLLM, SGLang, OpenAI API | **Maximum** |
| **slime** | Fixed (async, centralized buffer) | Megatron only | SGLang only | Low (opinionated) |
| **veRL ([[concepts/hybrid-flow]])** | Primarily colocated | FSDP, Megatron, TorchTitan | vLLM, SGLang, TGI | High |
| **TRL ([[concepts/fine-tuning/trl]])** | Single-process / FSDP | FSDP (HF-native) | HuggingFace generate | Moderate |

## Relationship to DeepSeek-R1

SkyRL implements [[concepts/grpo]] — the same algorithm powering [[concepts/deepseek-r1]]'s reasoning capabilities. While [[concepts/deepseek-r1]] trained on mathematical reasoning using [[concepts/hybrid-flow|veRL]], SkyRL targets the **agentic RL** domain: multi-turn interactions, tool orchestration, and environment-grounded training. Its flexible pipelining makes it well-suited for agentic scenarios where generation patterns are less predictable than pure reasoning rollouts.

## Related Pages

- [[concepts/grpo]] — Group Relative Policy Optimization (core algorithm)
- [[concepts/fine-tuning/trl]] — HuggingFace TRL, the mature general-purpose RLHF framework
- [[concepts/hybrid-flow]] — veRL (HybridFlow), the flexible multi-backend RL framework used by DeepSeek-R1
- [[concepts/deepseek-r1]] — DeepSeek-R1 reasoning model and its GRPO training methodology
- [[concepts/multi-turn-tool-use-rl]] — Multi-turn tool use with RL, directly aligned with SkyRL's agentic focus

## References

- [SkyRL GitHub](https://github.com/NovaSky-AI/SkyRL)
- [NovaSky AI (UC Berkeley)](https://novasky-ai.github.io/)
- [Anyscale: Open-Source RL Libraries for LLMs (Jul 2025)](raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md)
