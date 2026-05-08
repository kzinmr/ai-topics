---
title: "AReaL"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - reinforcement-learning
  - rlhf
  - grpo
  - training
  - distributed-training
  - framework
  - agentic-engineering
  - ai-agents
  - reasoning
  - comparison
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
---

# AReaL (Ant Group)

AReaL (Ant Reinforcement Learning) is an open-source RL library for LLMs developed by Ant Research (Ant Group), first released in February 2025. With 2.5k GitHub stars and 31 contributors, it is distinguished by its **core focus on asynchronous training throughput** — making it the most aggressively optimized library for maximizing GPU utilization during RL training. AReaL targets RLHF, reasoning model training, and agentic RL use cases.

## Quick Specs

| Dimension | Detail |
|-----------|--------|
| **First Release** | February 2025 |
| **Stars** | 2.5k ⭐ |
| **Contributors** | 31 |
| **Org** | Ant Research (Ant Group) |
| **Training Backend** | DeepSpeed, Megatron |
| **Algorithms** | GRPO, PPO |
| **Inference** | vLLM, SGLang |
| **Async Training** | ✅ (core feature — optimized for asynchronous execution) |
| **Environment Support** | ✅ Custom environment support |
| **Orchestrator** | Ray (optional) |
| **GitHub** | https://github.com/inclusionAI/AReaL |

## Key Features

### Maximal Async Throughput
AReaL's defining differentiator is its deep investment in asynchronous execution:

- **Interruptible rollouts**: Rollout generation can be interrupted mid-batch for higher-priority training operations, reducing idle time
- **Algorithmic modifications to PPO**: Custom modifications account for **data staleness** that occurs when rollouts and training updates run asynchronously — a fundamental challenge in async RL
- **Maximal GPU utilization**: By overlapping generation and training as aggressively as possible, AReaL achieves the highest throughput among open-source RL libraries

### Custom Environment Support
Like RAGEN, AReaL provides explicit support for custom RL environments, making it suitable for agentic and multi-turn RL training scenarios.

### Multi-Backend Training
Supports both DeepSpeed and Megatron training backends, providing flexibility for different hardware configurations and model scales. Inference supports vLLM and SGLang.

## Architecture

AReaL's architecture is built around async execution:

```
┌─────────────────────────────────────────┐
│  Async Orchestrator (Ray, optional)      │
│  ┌─────────────┐   ┌──────────────────┐ │
│  │ Rollout      │   │ Trainer           │ │
│  │ (vLLM/SGLang)│◄──│ (DeepSpeed/       │ │
│  │              │──►│  Megatron)        │ │
│  │ interruptible│   │ staleness-aware   │ │
│  └─────────────┘   └──────────────────┘ │
│         │                                 │
│         ▼                                 │
│  ┌─────────────┐                         │
│  │ Environment  │  (custom env support)  │
│  └─────────────┘                         │
└─────────────────────────────────────────┘
```

### Async Data Staleness Handling
A key technical challenge in async RL is **data staleness**: when the policy model is updated while rollout generation is still in progress, the training data no longer reflects the current policy. AReaL incorporates algorithmic modifications to PPO that account for this staleness, ensuring stable training even under aggressive async execution.

## Use Cases

- **RLHF fine-tuning**: Standard alignment workflows with maximal throughput
- **Reasoning model training**: GRPO-based training (algorithm behind [[concepts/deepseek-r1]])
- **Agentic RL**: Custom environments for multi-turn agent training
- **Throughput-critical deployments**: Scenarios where GPU cost optimization is paramount

## Limitations

- **Newer library**: Released Feb 2025, less ecosystem maturity and community size compared to [[concepts/fine-tuning/trl|TRL]] or [[concepts/hybrid-flow|veRL]]
- **Smaller community**: 2.5k stars / 31 contributors — growing but relatively small
- **Ant Group affiliation**: While open-source, the library is primarily driven by Ant Research, which may affect long-term governance and community direction
- **No DPO support**: Currently limited to GRPO and PPO; no DPO or SFT trainers

## Comparison

| Aspect | AReaL | [[concepts/hybrid-flow\|veRL]] | OpenRLHF |
|--------|-------|------|----------|
| **Async Training** | ✅ Maximal (core) | 🚧 Partial | ✅ Supported |
| **Environment** | ✅ Custom env | 🚧 via tools | 🚧 via function |
| **Training Backends** | DeepSpeed, Megatron | FSDP, Megatron, TorchTitan | DeepSpeed only |
| **Staleness Handling** | ✅ Algorithmic | ❌ | ❌ |
| **Maturity** | New (Feb 2025) | Medium (Nov 2024) | High (Jul 2023) |
| **Community** | 2.5k ⭐ | 12.9k ⭐ | 7.8k ⭐ |

## Related Pages

- [[concepts/grpo]] — GRPO algorithm, one of the two algorithms AReaL supports
- [[concepts/fine-tuning/trl]] — HuggingFace TRL for simpler RLHF workflows
- [[concepts/hybrid-flow]] — veRL, the most comparable multi-backend RL library
- [[concepts/deepseek-r1]] — DeepSeek-R1, which popularized GRPO-based RL training
