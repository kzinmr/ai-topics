---
title: InclusionAI
created: 2026-05-13
updated: 2026-05-13
type: entity
tags:
  - company
  - model
  - open-source
  - coding-agents
sources:
  - raw/articles/2026-05-13_inclusionai-ring-2-6-1t.md
  - https://openrouter.ai/inclusionai/ring-2.6-1t:free
---

# InclusionAI

**InclusionAI** is an AI company that develops large language models optimized for agentic workflows. Their flagship model, **Ring-2.6-1T**, was released on May 8, 2026 and is available for free on OpenRouter.

## Overview

- **Website**: inclusion-ai.org
- **Known Product**: Ring model series
- **Focus**: Agent-centric LLMs optimized for coding agents, tool use, and long-horizon task execution
- **Distribution**: OpenRouter (free tier)

## Ring-2.6-1T

Ring-2.6-1T is a **1T-parameter Mixture of Experts (MoE)** thinking model with **63B active parameters**. See [[entities/ring-2-6-1t]] for detailed specifications.

Key design priorities:
- **Coding agents**: Optimized for agentic coding workflows
- **Tool use**: Strong performance in tool-heavy, multi-turn interactions
- **Cost efficiency**: Free on OpenRouter, competitive token economics
- **Adaptive reasoning**: Dynamically scales reasoning effort based on task complexity (high/xhigh modes)

## Competitive Positioning

InclusionAI occupies an interesting niche — providing a frontier-scale (1T parameter) model optimized specifically for agent workflows, at zero cost. This positions them against:
- **[[entities/deepseek]]**: Open-source MoE models with strong agent performance (e.g., DeepSeek-V4)
- **[[concepts/qwen]]**: Qwen's open-source coding models (e.g., Qwen3-Coder)
- **[[entities/anthropic]]** / **[[entities/openai]]**: Proprietary frontier models dominant in SWE-bench but at significant cost

## Open Questions

- **Company background**: Limited public information about InclusionAI's founding, team, and funding
- **Training details**: Architecture, data, and training methodology not publicly documented
- **Sustainability**: Free pricing model raises questions about long-term availability
- **Model family**: Whether Ring-2.6 is part of a broader model family or a one-off release
