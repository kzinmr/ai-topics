---
title: Ling 2.6-1T
created: 2026-05-27
updated: 2026-05-27
type: entity
tags: [entity, model, llm, mixture-of-experts, moe, open-source, china, ant-group, text-generation, coding-agents, agentic-engineering]
sources:
  - raw/articles/2026-05-27_ling-2-6-1t-ant-group.md
  - https://www.i-scoop.eu/ling-2-6-1t-by-ant-group/
---

# Ling 2.6-1T

**Ling 2.6-1T** is a trillion-parameter open-weights language model developed by Ant Group, released under the MIT license through InclusionAI. It uses a Mixture of Experts (MoE) architecture with 63 billion active parameters during inference, designed for enterprise coding, long-context document processing, and multi-step agent workflows.

> "Can a frontier scale model handle complex work with less token waste, stronger tool use and enough reliability for enterprise workflows?"

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Total parameters | 1 trillion |
| Active parameters | 63 billion |
| Architecture | Mixture of Experts (MoE) |
| Context window (native) | 1M tokens |
| Context window (API) | ~256K tokens |
| Modalities | Text in, text out (non-reasoning) |
| License | MIT (open weights) |
| Provider | InclusionAI / Ant Group |

## Architecture & Efficiency

Ling 2.6-1T employs **Contextual Process Redundancy Suppression**, a post-training strategy that reduces reliance on verbose chain-of-thought, aiming for "fast thinking" and fewer output tokens. The MoE design routes each token to selected expert subnetworks, maximizing parameter scale while minimizing activation cost.

## Performance

- **SWE-bench Verified**: 72.2 (Artificial Analysis)
- **Intelligence Index** (AA): 34 — above average for comparable open-weights non-reasoning models
- Additional benchmarks: BFCL-V4, TAU2-Bench, IFBench, AIME26, MRCR

### Pricing
- Input: $0.30 / million tokens
- Output: $2.50 / million tokens
- Blended (3:1 ratio): $0.85 / million tokens

## Agent & Coding Workflows

Positioned for code generation, bug fixing, and full engineering workflows. Compatible with agent frameworks including [[entities/claude-code|Claude Code]], OpenClaw, OpenCode, and CodeBuddy. Benchmarks test tool use, instruction following, and multi-step task completion — not just static knowledge.

## BaiLing Ecosystem

Ling 2.6-1T is part of Ant Group's **BaiLing** foundation model platform:
- Computing cluster with tens of thousands of heterogeneous accelerators
- Integrated security pipeline (detection → defense)
- Knowledge processing at trillions of tokens
- Applications: **Maxiaocai** (financial assistant), **CodeFuse** (AI development tool)

## Sibling Model: Ling 2.6 Flash

| | Ling 2.6 Flash | Ling 2.6-1T |
|---|---|---|
| Total params | 104B | 1T |
| Active params | 7.4B | 63B |
| Use case | High-throughput, low-cost | Ultra-long docs, complex reasoning, coding agents |

## References

- i-Scoop: [Ling 2.6-1T by Ant Group](https://www.i-scoop.eu/ling-2-6-1t-by-ant-group/) (May 19, 2026)
- Artificial Analysis benchmarks
- [[concepts/mixture-of-experts]]
- [[entities/command-a-plus]] — comparable open-weights MoE model
