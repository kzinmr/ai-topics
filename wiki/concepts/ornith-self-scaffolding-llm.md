---
title: Ornith-1.0 — Self-Scaffolding LLMs for Agentic Coding
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [concept, model, open-source, coding-agents, agentic-rl, reasoning-model]
sources:
  - raw/articles/simonwillison.net--2026-jun-29-ornith--e3eeed57.md
---

# Ornith-1.0 — Self-Scaffolding LLMs for Agentic Coding

## Overview

Ornith-1.0 is the first open-source model from **DeepReinforce**, released under the permissive **MIT License**. It represents a significant milestone in open-weight agentic coding models, combining reinforcement learning from agentic environments (agentic RL) with a novel self-scaffolding architecture. The model is designed to excel at multi-turn tool-use and autonomous code generation, pushing the state of the art for open-source coding agents.

## Model Variants

Ornith-1.0 comes in four variants, all built on top of existing open-weight base architectures (Gemma 4 and Qwen 3.5, both Apache 2.0 licensed):

| Variant | Parameters | Architecture | Base Model |
|---------|-----------|-------------|------------|
| Ornith-1.0-9B | 9B | Dense | Gemma 4 |
| Ornith-1.0-31B | 31B | Dense | Qwen 3.5 |
| Ornith-1.0-35B-A3B | 35B | Mixture of Experts (MoE) | Qwen 3.5 |
| Ornith-1.0-397B-A64B | 397B | Mixture of Experts (MoE) | Qwen 3.5 |

The 9B dense variant is the most accessible for local deployment, while the 397B MoE variant pushes toward frontier-level performance. All variants inherit the permissive Apache 2.0 license from their base models, with Ornith-specific improvements released under MIT.

## Self-Scaffolding Architecture

The core innovation of Ornith-1.0 is its **self-scaffolding** capability. Unlike traditional LLMs that require external frameworks (e.g., LangChain, CrewAI) to orchestrate multi-step tool-use, Ornith-1.0 can generate its own scaffolding code — the glue logic that manages multi-turn agentic workflows, tool call sequencing, error recovery, and state management.

This means Ornith-1.0 can:

- **Generate its own agent harness** — producing executable Python code that defines tool-using loops, rather than relying on pre-built orchestration layers.
- **Self-correct and re-plan** — when a tool call fails or returns unexpected results, the model can generate new code to handle the edge case inline.
- **Adapt scaffolding to context** — adjusting its tool-use strategy based on the specific task, environment, and available APIs, rather than following a fixed prompt template.

This self-scaffolding approach is trained via agentic reinforcement learning (agentic RL), where the model learns from trajectories of successful and failed multi-tool interactions, internalizing the patterns of effective scaffolding rather than memorizing static solutions.

## Performance

Ornith-1.0 achieves state-of-the-art results among comparable open-source models on a range of coding and agentic benchmarks. Key highlights:

- **SWE-bench Verified**: Top scores among models in its size class for autonomous software engineering tasks.
- **Agentic coding tasks**: Superior performance on multi-step tool-use scenarios involving file editing, shell execution, web browsing, and API calling.
- **Code generation**: Competitive with leading open models on standard coding benchmarks (HumanEval, MBPP) while exceeding them in agentic settings.

The 397B MoE variant approaches closed-source frontier model performance on several agentic coding evaluations.

## Simon Willison's Hands-On Evaluation

Simon Willison tested Ornith-1.0 using **LM Studio** combined with the **Pi** scaffolding tool. Key findings from his evaluation:

- **Local performance**: Achieved approximately **103 tokens per second** on consumer hardware for the 9B variant.
- **Image generation agent**: Successfully generated images via a multi-tool-call agent harness, demonstrating real-world agentic capabilities.
- **Datasette integration**: Used the model against a Datasette instance, demonstrating the ability to discover APIs, plan queries, and execute multi-step data retrieval operations — all driven by self-generated scaffolding code.
- **Reliability**: The model successfully handled complex multi-tool-call sequences, recovering gracefully from intermediate errors and adjusting its approach autonomously.

Willison's hands-on testing validates that Ornith-1.0's self-scaffolding approach works in practice for realistic developer workflows, not just on academic benchmarks.

## Related Pages

- [[entities/simon-willison]] — Simon Willison, who conducted the hands-on evaluation and reported on Ornith-1.0
- [[concepts/coding-agents]] — The broader category of LLM-based coding agents
- [[concepts/agentic-engineering]] — Engineering practices for building agentic systems

## References

- [Simon Willison's blog post on Ornith-1.0](https://simonwillison.net/2026/Jun/29/ornith/) (source article)
- DeepReinforce — Ornith-1.0 model release (Hugging Face)
- Gemma 4 and Qwen 3.5 base model documentation
