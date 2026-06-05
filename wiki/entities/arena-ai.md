---
title: "Arena AI"
type: entity
created: 2026-05-08
updated: 2026-06-05
tags:
  - company
  - evaluation
  - benchmark
  - model
  - comparison
aliases:
  - "Arena"
  - "arena.ai"
  - "LMSYS Chatbot Arena"
sources:
  - https://arena.ai/
  - https://arena.ai/blog/
  - https://arena.ai/blog/feed
  - raw/articles/2026-06-04_arena-ai_agent-arena-methodology.md
---

# Arena AI

**Arena** (arena.ai) is an AI company that operates a platform for AI model evaluation and comparison. It is best known for running blind pairwise comparisons (Chatbot Arena) where users vote on model outputs to produce crowdsourced leaderboards across text, vision, code, and search tasks.

> **Note:** Arena (arena.ai) is an AI model evaluation platform. It is **not** to be confused with [[entities/contextarena|Context Arena]] (contextarena.ai), which is a long-context benchmark leaderboard built on the GDM-MRCRv2 8-Needle test.

| | |
|---|---|
| **Type** | AI Evaluation Platform / Company |
| **Key Platform** | Chatbot Arena — blind pairwise LLM comparison and leaderboard |
| **Evaluation Domains** | Text, vision, code, search |
| **Website** | [arena.ai](https://arena.ai) |
| **Tech Blog** | [arena.ai/blog](https://arena.ai/blog/) |
| **RSS** | [arena.ai/blog/feed](https://arena.ai/blog/feed) |

## Key Facts

- Operates the Chatbot Arena, one of the most widely referenced LLM evaluation leaderboards
- Uses blind pairwise comparisons where users vote on model outputs (no ground-truth labels required)
- Originally developed by LMSYS (Large Model Systems Organization)
- Covers text generation, vision understanding, code generation, and search capabilities
- Elo-based ranking system derived from user preference votes

## Platform

The Chatbot Arena platform allows users to submit prompts to two anonymous models simultaneously and vote on which response is better. Results are aggregated into Elo scores that rank models across multiple categories. The platform has become a de facto standard for comparing frontier AI models from OpenAI, Anthropic, Google, Meta, and others.

## Agent Arena — Causal Agent Evaluation (June 2026)

On June 4, 2026, Arena launched **Agent Arena**, a new evaluation system for AI agents using **causal tracing** methodology:

- **Methodology**: Multi-component system view where randomized component selection creates a multi-intervention RCT, measuring causal treatment effects (τ̂) rather than pairwise votes
- **Five signals**: Confirmed success, Praise vs. complaint, Steerability, Bash recovery, Tool hallucination
- **Scale** (7-day window): 160K tasks, 128K sessions, 2M tool calls, 40.3M lines of code
- **Cost analysis**: Realized post-deployment costs reveal some models more expensive in practice than on-paper pricing
- **Decoupled ranking**: Separates orchestrator model contributions from harness components

See [[concepts/agent-arena]] for full methodology and data.

## Related

- [[entities/openai]] — GPT models regularly evaluated on Chatbot Arena
- [[entities/anthropic]] — Claude models ranked on Chatbot Arena leaderboards
- [[entities/contextarena]] — Separate long-context benchmark (contextarena.ai); not the same entity
- [[concepts/agent-arena]] — Agent Arena causal evaluation methodology
