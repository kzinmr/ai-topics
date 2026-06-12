---
title: "RAGEN"
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
  - comparison
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
---

# RAGEN

RAGEN is an open-source reinforcement learning library built **on top of veRL** ([[concepts/hybrid-flow]]), extending it with explicit environment support for agentic and multi-turn RL training. First released in January 2025, it has 2.3k GitHub stars and 16 contributors. RAGEN bridges the gap between veRL's powerful distributed training infrastructure and the growing need for training LLM agents in interactive environments.

## Quick Specs

| Dimension | Detail |
|-----------|--------|
| **First Release** | January 2025 |
| **Stars** | 2.3k ⭐ |
| **Contributors** | 16 |
| **Built On** | veRL ([[concepts/hybrid-flow]]) |
| **Training Backend** | veRL backend (FSDP, Megatron) |
| **Algorithms** | GRPO, PPO |
| **Inference** | Hugging Face, vLLM, SGLang |
| **Async Training** | ❌ |
| **Environment Support** | ✅ Custom environment support, explicit environment interface |
| **Orchestrator** | Ray |
| **GitHub** | https://github.com/ZihanWang314/ragen |

## Key Features

### Explicit Environment Interface
RAGEN's defining feature is its **dedicated environment interface** for defining custom RL environments. Unlike veRL's limited tool-based environment support, RAGEN provides a clean abstraction that makes it significantly easier to define and integrate custom environments for agentic RL training.

### Built on veRL
By building on [[concepts/hybrid-flow]], RAGEN inherits veRL's battle-tested infrastructure:
- Multi-backend training support (FSDP, Megatron)
- Multiple inference engines (vLLM, SGLang, HuggingFace)
- Ray-based distributed orchestration
- Proven at scale (veRL was used for [[concepts/deepseek-r1]]'s GRPO training)

### Agentic/Multi-Turn RL Focus
RAGEN targets the specific challenges of training LLMs as agents:
- Multi-turn interactions with environments
- Tool-use RL training
- Custom reward functions tied to environment state

## Architecture

RAGEN layers its environment abstraction on top of veRL's HybridFlow architecture:

```
┌─────────────────────────────────┐
│  RAGEN Environment Layer         │
│  - Custom env definitions        │
│  - Multi-turn state management   │
└──────────┬──────────────────────┘
           │
┌──────────▼──────────────────────┐
│  veRL (HybridFlow)              │
│  - Controller (Ray)             │
│  - WorkerGroup (FSDP/Megatron)   │
│  - Rollout (vLLM/SGLang)        │
└─────────────────────────────────┘
```

The environment interface allows users to define stateful environments where the LLM agent interacts across multiple turns — a critical capability for training tool-using or game-playing agents with RL.

## Use Cases

- **Agentic RL training**: Primary use case. Train LLMs to interact with tools, APIs, and environments
- **Multi-turn RL**: Training agents that need to reason and act across multiple interaction steps
- **Custom environment integration**: Define domain-specific environments (games, simulators, code execution sandboxes)

## Limitations

- **Inherits veRL complexity**: veRL's HybridFlow architecture has a learning curve; RAGEN inherits this
- **Smaller community**: 2.3k stars / 16 contributors — much smaller than veRL or [[concepts/post-training/trl|TRL]]
- **No async training**: Unlike OpenRLHF or AReaL, does not support asynchronous rollout generation
- **Built on veRL**: Dependency on veRL means being tied to its release cycle and architectural decisions

## Comparison

| Aspect | RAGEN | [[concepts/hybrid-flow\|veRL]] | AReaL |
|--------|-------|------|-------|
| **Environment Support** | ✅ Explicit interface | 🚧 via tools | ✅ Custom env |
| **Agentic RL** | ✅ Primary focus | 🚧 Limited | ✅ Supported |
| **Async Training** | ❌ | 🚧 | ✅ Core feature |
| **Maturity** | New (Jan 2025) | Medium (Nov 2024) | New (Feb 2025) |
| **Community Size** | 2.3k ⭐ | 12.9k ⭐ | 2.5k ⭐ |

## Related Pages

- [[concepts/hybrid-flow]] — veRL, the underlying framework RAGEN is built on
- [[concepts/post-training/grpo]] — GRPO algorithm, the primary RL method used in RAGEN
- [[concepts/post-training/trl]] — HuggingFace TRL for simpler RLHF workflows
- [[concepts/deepseek-r1]] — DeepSeek-R1, the model that popularized GRPO-based reasoning training
