---
title: Ring-2.6-1T
created: 2026-05-13
updated: 2026-05-13
type: entity
tags:
  - model
  - coding-agents
  - text-generation
sources:
  - raw/articles/2026-05-13_inclusionai-ring-2-6-1t.md
  - https://openrouter.ai/inclusionai/ring-2.6-1t:free
---

# Ring-2.6-1T

**Ring-2.6-1T** is a 1T-parameter Mixture of Experts (MoE) thinking model by [[entities/inclusionai]], released May 8, 2026. It is optimized for agentic workflows — coding agents, tool use, and long-horizon task execution — and is available for free on OpenRouter.

## Specifications

| Spec | Value |
|------|-------|
| Total Parameters | 1 trillion |
| Active Parameters | 63 billion |
| Architecture | Mixture of Experts (MoE) |
| Context Window | 262,144 tokens |
| Max Output Tokens | 65,536 |
| Input Modalities | Text |
| Output Modalities | Text |
| Reasoning Modes | high, xhigh (adaptive) |
| Pricing | Free ($0/M tokens) |
| Release Date | May 8, 2026 |
| OpenRouter Rank | #29 (weekly) |

## Benchmark Performance

Ring-2.6-1T delivers leading results on agent-centric benchmarks:

- **PinchBench**: Agent task completion benchmark
- **ClawEval**: Coding agent evaluation
- **TAU2-Bench**: Tool-augmented user interaction
- **GAIA2-search**: General AI assistant with search

## Adaptive Reasoning

Ring-2.6-1T features adaptive reasoning effort across **high** and **xhigh** modes. Rather than applying uniform reasoning depth to all queries, it dynamically allocates reasoning budget based on task complexity:

- **Simple queries**: Low reasoning overhead, fast response
- **Complex multi-step tasks**: Deeper reasoning, higher token allocation
- **Tool-heavy workflows**: Balanced allocation preserving context for tool interactions

This design aims to achieve strong performance with lower total token overhead compared to models that apply uniform deep reasoning.

## Target Use Cases

- **Advanced coding agents**: Long-horizon software engineering tasks
- **Complex reasoning pipelines**: Multi-step analytical workflows
- **Large-scale autonomous systems**: Agent systems requiring both capability and efficiency
- **Tool-heavy multi-turn interactions**: Navigating APIs, databases, and external services

## Competitive Context

Ring-2.6-1T enters a competitive landscape of MoE models:

| Model | Total Params | Active Params | Focus | Cost |
|---|---|---|---|---|
| **Ring-2.6-1T** | 1T | 63B | Agent workflows | Free |
| DeepSeek-V4-Flash-Max | ~671B | ~37B | General + code | Low |
| Qwen3-Coder-480B | 480B | ~36B | Code | Low |
| GPT-5.5 | Unknown | Unknown | General + agentic | High |
| Claude Opus 4.6 | Unknown | Unknown | General + code | High |

## Relationship to Other Entities

- **[[entities/inclusionai]]**: Parent company, limited public information
- **[[concepts/mixture-of-experts]]**: MoE architecture enabling 1T parameters with 63B active
- **[[concepts/coding-agents/coding-agents]]**: Primary target use case
- **[[entities/openrouter]]**: Distribution platform
