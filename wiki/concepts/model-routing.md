---
title: Model Routing — Per-Turn Cost Optimization for AI Coding
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [inference, optimization, coding-agents, economics, claude-code, openai, gemini]
sources: []
---

# Model Routing — Per-Turn Cost Optimization for AI Coding

Model routing is a technique that dynamically selects the best-fit model for each individual query or turn in an AI coding session, rather than committing to a single model upfront.

## Augment Prism (May 2026)

Augment Code's **Prism** is the first production-grade per-turn model router for coding agents. It routes each turn to the model that fits the work, with cache eviction costs baked into the decision.

### Key Metrics
- **20-30% cost reduction** per task at **similar or better quality** (on Augment's internal multi-turn coding benchmark)
- Teams sending 10,000 messages/month: ~$20,000/month savings
- Two routing families:
  - **Prism (Claude + Gemini)**: Targets Opus 4.7 quality
  - **Prism (GPT + Kimi)**: Targets GPT 5.5 quality

### Design
- Billing rolls up under a single "Prism" line item — the underlying model is not surfaced to users
- Router considers: task complexity, context size, cache state, model capability
- Switch decision weighs expected quality gain against cache eviction cost

## Why It Matters

No single model wins every task within a session. Simple autocompletion doesn't need a frontier model; complex debugging might. Per-turn routing optimizes both cost and quality simultaneously, which fixed-model strategies cannot achieve.

## Related Concepts

- [[concepts/inference-optimization]]
- [[entities/augment]]
- [[concepts/llm-cost-optimization]]
