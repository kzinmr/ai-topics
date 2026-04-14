---
title: "RAM — Relative Adoption Metric"
created: 2026-04-14
updated: 2026-04-14
tags: [concept, open-models, model-evaluation, nathan-lambert, atom-project, ai-ecosystem-metrics]
related:
  - entities/nathan-lambert
  - concepts/atom-project
  - concepts/ai-evals
  - concepts/model-distillation
---

# RAM — Relative Adoption Metric

## Overview

The **Relative Adoption Metric (RAM)** is a time-varying, size-normalized metric developed by Nathan Lambert and Florian to evaluate whether a new language model is on track to be ecosystem-defining. It was introduced as part of **The ATOM Report** (April 2026) and **The ATOM Project** memo.

## The Problem RAM Solves

Raw download counts are misleading in the open model ecosystem:

- **Small model dominance**: Models in the 1-9B parameter range account for ~1.4 billion of ~2 billion total HuggingFace downloads (70%)
- **CI/test downloads**: Many downloads come from automated systems (CI pipelines, developer testing) rather than actual usage
- **Parameter count bias**: Organizations releasing many small models appear more popular simply due to volume
- **Time-varying context**: A model's trajectory matters as much as its absolute numbers

Among the top 10 downloaded models at each size category, median 1-9B models are only ~4X the download count of 100B+ models — a far smaller gap than raw totals suggest.

## RAM Score Definition

The RAM Score is designed so that:

- **RAM > 1**: Model is on track to be a top-10 most downloaded model of its size category, ever
- **RAM < 1**: Model is below the adoption trajectory of top performers in its class
- **Time-normalized**: Accounts for how long the model has been available
- **Size-normalized**: Compares within parameter bins, not across the entire ecosystem

## Key Findings from The ATOM Report

### GPT-OSS Exceptionalism
- OpenAI released only 2 models (GPT-OSS), yet ranks among the **top 5-10 open model labs** by adoption metrics
- This is obscured in raw organization-vs-organization comparisons where competitors release many more models
- RAM reveals the outsized impact of each individual OpenAI open model release

### Chinese Model Dominance
The RAM score chart from the report shows recent Chinese models (Qwen, Kimi, MiniMax, Z.ai) consistently scoring high, reflecting:
- Rapid release cadence
- Strong per-model adoption trajectories
- Growing ecosystem share

### Meta's Declining Share
- Llama models' share of derivatives dropped from ~50% (fall 2024) to ~15% (April 2026)
- RAM contextualizes this: it's not just that Llama is declining, but that competitors are accelerating faster

## Methodology

RAM uses:
1. **Daily download data** from HuggingFace for 1,100+ leading LLMs
2. **Parameter size bins** (1-9B, 10-30B, 31-100B, 100B+)
3. **Time-decayed adoption curves** — how quickly a model reaches milestones relative to its release date
4. **Normalized ranking** — position within size class, not absolute position

## Comparison to Other Metrics

| Metric | Strength | Weakness |
|--------|----------|----------|
| Raw downloads | Simple, objective | Heavily skewed by small models and CI usage |
| LMArena rankings | Quality-focused | Small sample, crowdsourced bias |
| ArtificialAnalysis | Comprehensive benchmark blend | Lagging indicator |
| **RAM Score** | Time+size normalized, trajectory prediction | Requires sustained tracking infrastructure |

## Integration with ATOM Project

RAM is one of the core analytical tools behind The ATOM Project's thesis that:
1. Chinese open models are outpacing American ones
2. The U.S. needs at least one lab focused on training open models with 10,000+ leading-edge GPUs
3. GPT-OSS's strong per-model performance shows OpenAI could be a major open model player

## Sources

- Nathan Lambert, "The ATOM Project" memo (August 2025)
- Nathan Lambert & Florian, "The ATOM Report" (April 2026)
- Interconnects.ai newsletter, "Gemma 4 and what makes an open model succeed"
- Substack article: "ATOM Report, post-training course, finishing my book, and research"
