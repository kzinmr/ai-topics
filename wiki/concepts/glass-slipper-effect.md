---
title: "Glass Slipper Effect"
type: concept
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - economics
  - user-behavior
  - ecosystem
aliases:
  - Cinderella Effect
  - Foundational Cohorts
  - Boomerang Effect
  - workload-model fit
related:
  - [[concepts/openrouter-state-of-ai-2025]]
  - [[entities/openrouter]]
sources:
  - raw/articles/2025-12-01_openrouter-state-of-ai-2025.md
  - https://openrouter.ai/state-of-ai
---

# Glass Slipper Effect

The **Glass Slipper Effect** (also called the **Cinderella Effect**) is a framework for understanding LLM user retention, introduced by the [[concepts/openrouter-state-of-ai-2025|OpenRouter State of AI 2025]] study. It describes how early users who find a perfect "workload-model fit" become "foundational cohorts" with durably high retention — analogous to Cinderella's glass slipper fitting perfectly.

## Definition

> "When a newly released model happens to match a previously unmet technical and economic constraint, it achieves the precise fit — the metaphorical 'glass slipper.' For the developers... this alignment creates strong lock-in effects."

## Key Mechanisms

### Foundational Cohorts
Early adopters who discover a model that perfectly matches their specific workload show ~40% retention at Month 5, far higher than later cohorts. This suggests that:
- The **first model** to solve a specific user's problem creates a durable switching cost.
- Later, "better" models have difficulty dislodging these users because their pipelines, tooling, and mental models are anchored to the first solution.
- Examples: Gemini 2.5 Pro's June 2025 cohort, Claude 4 Sonnet's early adopters.

### The Boomerang Effect
Observed in DeepSeek models: users churn to try alternatives, but a significant fraction return to DeepSeek. This confirms that within each user's workload, certain models occupy an optimal niche that competitors cannot easily replicate despite being "better" on aggregate benchmarks.

### Cognitive Inertia
The study frames this as "cognitive inertia" — once a development workflow is tuned to a specific model's behavior (its latency profile, output style, error patterns, API quirks), the cost of retuning to a different model exceeds the marginal benefit of switching.

## Implications

- **For Model Providers:** The first-mover advantage is stronger than benchmark performance would suggest. Capturing a developer segment early creates durable revenue.
- **For Developers:** Switching costs are real and significant. Optimizing for a specific model creates lock-in that may be costly to undo.
- **For the Ecosystem:** Explains why "best model" aggregate comparisons don't fully predict market share — the fit to specific workloads matters more than absolute capability.

## Evidence

- Gemini 2.5 Pro's foundational cohort (June 2025) retained ~40% at Month 5 vs. declining retention for later cohorts.
- DeepSeek cohorts showed clear "resurrection jumps" in retention curves.
- The effect was strongest for **Programming** workloads (highest switching cost) and weakest for **general Q&A** (low switching cost).

## Related Concepts

- [[concepts/openrouter-state-of-ai-2025]] — The study that identified this effect
- [[entities/openrouter]] — Platform that observed the phenomenon
- [[entities/malika-aubakirova]] — Co-author who identified the framework

## Sources

- [OpenRouter State of AI 2025](https://openrouter.ai/state-of-ai) — Original study, Section 6: Retention
- `raw/articles/2025-12-01_openrouter-state-of-ai-2025.md`
