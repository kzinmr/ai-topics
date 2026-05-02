---
title: "OpenRouter State of AI 2025"
type: concept
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - study
  - analysis
  - ecosystem
  - benchmark
aliases:
  - State of AI 2025
  - 100T Token LLM Usage Study
  - OpenRouter/a16z Study
related:
  - [[entities/openrouter]]
  - [[entities/malika-aubakirova]]
  - [[concepts/glass-slipper-effect]]
  - [[concepts/ai-market-economics]]
sources:
  - raw/articles/2025-12-01_openrouter-state-of-ai-2025.md
  - https://openrouter.ai/state-of-ai
---

# OpenRouter State of AI 2025

> **State of AI 2025** is a landmark study published by OpenRouter and a16z in December 2025, analyzing **100 trillion tokens** of real-world LLM interactions. It is the largest public analysis of actual LLM usage patterns, providing unprecedented visibility into how models are used, by whom, and for what purposes.

## Executive Summary

The study identifies **December 5, 2024** (the release of OpenAI's o1) as the "reasoning inflection point" — the moment when the industry shifted from single-pass pattern generation to multi-step deliberation inference.

### Key Findings
1. **Reasoning Models Dominate:** Tokens through reasoning-optimized models exceeded **50% of all usage** by late 2025.
2. **Open Source at 30%:** Open-weight models reached a steady 30% market share, led by Chinese providers.
3. **The Glass Slipper Effect:** Early-adopter retention is driven by "workload-model fit" rather than raw capability.
4. **Programming is King:** Programming grew from 11% to **over 50% of total token volume**.
5. **Roleplay Surprise:** Roleplay accounts for **over 50% of OSS token usage** — a hidden giant.

## Open vs. Closed Source Dynamics

| Dimension | Proprietary | Open Weight (OSS) |
|-----------|-------------|-------------------|
| **Market share** | ~70% tokens | ~30% tokens |
| **Top models** | Claude 3.7/4.5, GPT-5, Gemini | DeepSeek, Qwen, LLaMA |
| **Usage pattern** | High-value tasks (coding, tech) | High-volume tasks (roleplay, chat) |
| **Dominant region** | North America | Asia (especially China) |
| **Specialization** | Programming + Technology (Anthropic ~80%) | Roleplay (DeepSeek >66%) |

### Chinese OSS Rise
- Chinese OSS grew from **1.2%** to nearly **30%** of weekly share in one year.
- **Top OSS players:** DeepSeek (14.37T tokens), Qwen (5.59T), Meta LLaMA (3.96T), Mistral (2.92T).
- Market shifted from DeepSeek near-monopoly to pluralistic competition (no single model >25%).

### "Medium is the New Small"
- **Small (<15B):** Declining — fragmentation and churn.
- **Medium (15B–70B):** Growing rapidly — found "Model-Market Fit."
- **Large (>70B):** Diversifying — users benchmark multiple frontier models.

## Agentic Inference

Usage is moving from stateless requests to long-running, tool-integrated workflows:
- **Sequence explosion:** Average prompt tokens **4x** (1.5K→6K+), completions **3x** (150→400).
- **Tool calling:** Consistent upward trend, led by Claude Sonnet and Gemini Flash.
- **Programming prompts:** 3–4x longer than general prompts, often exceeding 20K tokens.

## Category Taxonomy

| Category | Key Insight |
|----------|-------------|
| **Programming** | 50%+ of all tokens. Anthropic dominates (~60% share). Prompts 3–4x longer than average. |
| **Roleplay** | 52% of OSS usage. 58% RPG, 15.6% Writers Resources, 15.4% Adult. OSS advantage due to fewer safety constraints. |
| **Technology** | Highest cost-per-token. Sustained high usage. |
| **Science** | 80.4% is actually ML/AI meta-questions. |
| **Health/Legal** | Highly fragmented. Exploratory, not structured. |

### Provider Specializations
- **Anthropic (Claude):** ~80% Programming + Technology. Dominant in tool calling.
- **Google (Gemini):** Broadest mix (Legal, Science, Translation).
- **DeepSeek:** >66% Roleplay and casual chat.
- **xAI (Grok):** Overwhelmingly Programming-focused.

## The Glass Slipper Effect

See the dedicated [[concepts/glass-slipper-effect|Glass Slipper Effect]] concept page for the full framework. In brief:

- **Foundational Cohorts:** Early adopters show ~40% retention at Month 5 vs. declining retention for later cohorts.
- **Boomerang Effect:** Users leave, try alternatives, return to their optimal model.
- **Cognitive Inertia:** Once a model fits a workload, switching costs create lock-in.

## Economics

- **Price Inelasticity:** 10% price drop → only 0.5–0.7% usage increase.
- **Jevons Paradox:** Cheaper/faster models → more total token consumption (longer contexts, more iterations).

### Market Archetypes

| Segment | Examples | Cost | Usage |
|---------|----------|------|-------|
| **Mass-Market Volume** | Programming, Roleplay | Low | High |
| **Premium Leaders** | Claude 3.7 Sonnet | ~$2/1M tokens | High |
| **Efficient Giants** | Gemini 2.0 Flash, DeepSeek V3 | <$0.40/1M tokens | High |
| **Premium Specialists** | GPT-5 Pro | ~$35/1M tokens | Low |

## Geography

- **USA:** 47% of spend.
- **Asia:** 31% (doubled from 13%).
- **Singapore:** 9% — disproportionate share for its population.
- **Key trend:** Rapid globalization of AI usage outside North America.

## Graph Structure Query

```
[openrouter-state-of-ai-2025] ──author──→ [entity: malika-aubakirova]
[openrouter-state-of-ai-2025] ──author──→ [entity: openrouter]
[openrouter-state-of-ai-2025] ──identifies──→ [concept: glass-slipper-effect]
[openrouter-state-of-ai-2025] ──analyzes──→ [concept: ai-market-economics]
[openrouter-state-of-ai-2025] ──documents──→ [concept: agentic-shift]
```

## Related Concepts

- [[concepts/glass-slipper-effect]] — Model retention framework from the study
- [[entities/openrouter]] — Platform that provided the data
- [[entities/malika-aubakirova]] — a16z researcher, co-author

## Sources

- [OpenRouter State of AI 2025](https://openrouter.ai/state-of-ai) — Full study
- `raw/articles/2025-12-01_openrouter-state-of-ai-2025.md`
