---
title: Model Routing — Per-Turn Cost Optimization for AI Coding
created: 2026-05-09
updated: 2026-05-12
tags:
  - inference
  - optimization
  - coding-agents
  - economics
  - claude-code
  - openai
  - google
sources:
  - https://x.com/i/article/2053183959341711361
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
- [[concepts/ai-coding-cost-optimization]] — Ronin's complete system with manual config-based router

## Manual Router Architecture (Ronin, May 2026)

As an alternative to automated routing like Prism, [[entities/ronin-deronin|Ronin]] (@DeRonin_) documented a **static, keyword-triggered** router config that splits work across 4 model tiers:

| Tier | Model | Trigger Keywords | % of Work |
|------|-------|-----------------|-----------|
| Premium | Claude Opus 4.6 | "plan", "architect", "design system", "security review" | ~10% |
| Workhorse | Kimi 2.6 | "review", "debug", "refactor", "implement", "build" | ~80% |
| Utility | Claude Haiku 4.5 | "lint", "format", "fix typo", "rename" | ~5% |
| Local | Ollama:Qwen 3:7b | "autocomplete", "stub", "boilerplate" | ~5% |

Key difference from Prism: Ronin's router uses **explicit keyword matching** against the user's prompt (static config) while Prism uses **per-turn learned routing** with cache-awareness built into the decision. Ronin's approach is simpler to implement and reason about, and achieved a 92.6% bill reduction ($4,200→$312/month) with no quality loss.

The core insight: Kimi 2.6 matches Sonnet 4.6 on shipped code quality at 1/6 the cost, making Sonnet a poor default in 2026. The router is complementary to Augment Prism — Prism automates the routing that Ronin's config manually encodes.

See full router config and benchmarks: [[concepts/ai-coding-cost-optimization]].
