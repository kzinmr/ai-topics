---
title: "Epoch AI"
created: 2026-05-30
updated: 2026-09-23
type: entity
tags:
  - lab
  - benchmark
  - evaluation
  - open-source
  - agent-safety
sources:
  - raw/articles/epoch.ai--publications-the-plunging-price-of-thought--e7c1a0f3.md
---

# Epoch AI

**Epoch AI** is an AI research organization focused on measuring and forecasting AI capabilities, progress trends, and societal impact. Founded in 2021 as a volunteer group collecting and analyzing data on AI progress, it has grown into a leading independent voice in AI capability tracking and benchmark development.

## Overview

Epoch AI's mission is to improve society's understanding of what is happening in AI from a neutral perspective, grounded in the best possible evidence. They focus on building a shared scientific foundation for thinking about AI — neutral to any specific agenda — so decisions about this technology are informed by data rather than hype.

## Key Products and Contributions

### Epoch Capabilities Index (ECI)

The **ECI** is Epoch AI's flagship composite metric that combines scores from 40+ distinct benchmarks into a single "general capability" scale, enabling comparisons between models even over timespans long enough for individual benchmarks to reach saturation. The ECI uses an item-response-theory model (similar to IQ tests) where:
- Each benchmark gets a difficulty score (EDI) and a slope parameter (how well it discriminates between capability levels)
- Each model gets an ECI score based on its performance across benchmarks, weighted by difficulty
- Domain-specific ECIs (SWE, Math) are computed by refitting only the model capability parameters while keeping benchmark difficulty fixed

The methodology is detailed in their paper **"A Rosetta Stone for AI Benchmarks"** (funded by Google DeepMind, written with their AGI Safety & Alignment team).

### Benchmarking Hub

Epoch AI maintains a comprehensive database of model benchmark results, tracking performance across hundreds of models and benchmarks. This includes:
- **Internally run evaluations**: Epoch conducts their own benchmark runs for consistency
- **Benchmark creator-reported scores**: Direct from benchmark developers
- **Model developer-reported scores**: From model cards and technical reports

### Notable Benchmarks Developed/Featured

- **FrontierMath**: State-of-the-art benchmark for testing frontier math capabilities
- **ARC-AGI-2**: Abstract reasoning challenge (featured on their Benchmarking Hub)
- **SWE-bench Verified**: Epoch AI provided the 5-10% error rate analysis
- **HLE (Humanity's Last Exam)**: Featured on their hub
- **Factorio Learning Environment (FLE)**: Featured on their hub
- **GPQA Diamond**: Featured on their hub
- **MirrorCode**: Long-duration coding benchmark (co-developed with METR)

## History

- **2021**: Founded as a volunteer group collecting and analyzing data on AI progress, curating information from hundreds of machine learning models
- **2022**: Published influential paper analyzing training compute trends, which led to formal organization
- **2024**: Released "Artificial Capable Intelligence" paper (arXiv:2512.00193) introducing ECI methodology
- **2025**: Published "Open-weight models lag state-of-the-art by around 3 months on average" (October)
- **2026**: Published "Open models lag state-of-the-art closed models by 4 months" (May) — showing the gap widened from 3 to 4 months

## Partnerships

- Stanford AI Index
- UK Department for Science, Innovation & Technology
- Google DeepMind (ECI methodology paper funding)
- METR (MirrorCode co-development)

## Key Personnel

- **Tom Adamczewski** — Led MirrorCode development
- **David Owen** — MirrorCode contributor (writing, planning, coding)
- **Rasmus Faber-Espensen** — Infrastructure improvements

## Research Themes

1. **AI capability measurement**: Tracking and comparing model performance across benchmarks
2. **Training compute trends**: Analyzing how computational requirements scale with capability
3. **Benchmark saturation**: Understanding when benchmarks lose discriminative power
4. **Open vs. closed model gaps**: Quantifying the time lag between frontier and open-weight models
5. **Forecasting**: Predicting future AI capability trajectories
6. **Infrastructure analysis**: Satellite monitoring of data center construction, compute supply chains

## Data Insights

Epoch AI regularly publishes data-driven insights on their website (epoch.ai/data-insights). Recent notable findings include:
- **May 2026**: Open models lag closed models by 4 months (ECI gap of 8 points)
- **October 2025**: Open models lagged by 3 months (previous analysis, Jan 2023–Oct 2025)
- **May 2026**: Token demand vs. global inference capacity gap warning for agentic workloads
- **April 2026**: ARC-AGI-2 featured on Benchmarking Hub

### "The plunging price of thought" (Sep 22, 2026)

Report by Luke Emberson and David Roodman, one of Epoch AI's most-cited macro findings to date (amplified by @emollick the next day):

- The cost of achieving a **given level of AI performance** has fallen **~47% per quarter (13×/year) since 2023** — faster than any transformative technology in history: 4× faster than DNA sequencing, 6× faster than compute, 18× faster than lithium batteries, 54× faster than electricity (century to 1973).
- Headline example: OpenAI o3 needed ~$0.30/question for 75% on GPQA Diamond (Jan 2025); under 18 months later **GPT-5.6 Luna matched it for $0.0004/question — a 725-fold drop**, "like a $50,000 car falling to $69".
- Method measures *actual cost to reach a performance level* (not price per token) across five benchmarks in math, hard sciences, and games — a distinction made necessary by reasoning models.
- Domain variation: 50–52%/quarter on math vs 39–43% on game puzzles. Declines are steepest at freshly-debuted SOTA (66%/quarter, 75×/year) and halve after ~2 years (32%/quarter, 4.7×/year).
- Author-stated caveats: benchmaxxing, frontier-switching user assumption, noisy 3-year data — "should not be read as exact".

Supersedes/extends Epoch's March 2025 estimate (9–900×/year, per-token) and sits alongside Gundlach et al. (Mar 2026). Directly relevant to [[concepts/llm-cost-crisis]] economics-of-inference and the Sep 2026 price war ([[events/claude-opus-5-5-gpt-6-release-sep-2026]]). The report is the anchor source for [[concepts/token-economics]].

## See Also

- [[concepts/evaluation/epoch-capabilities-index]] — ECI methodology and interpretation
- [[concepts/benchmark-optimization]] — The broader benchmark landscape and saturation dynamics
- [[entities/met]] — METR (co-developer of MirrorCode)
- [[concepts/open-vs-closed-model-gap]] — The 4-month capability lag analysis

## Sources

- [Epoch AI About Page](https://epoch.ai/about)
- [Epoch Capabilities Index](https://epoch.ai/eci)
- [ECI Documentation](https://epoch.ai/data/eci-documentation)
- [Open models lag closed models by 4 months](https://epoch.ai/data-insights/open-closed-eci-gap)
- [Open-weight models lag by 3 months (Oct 2025)](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models)
- [ECI Public GitHub Repository](https://github.com/epoch-research/eci-public)
