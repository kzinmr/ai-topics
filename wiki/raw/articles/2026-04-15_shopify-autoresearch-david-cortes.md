---
title: "Autoresearch isn't just for training models"
author: David Cortés (Shopify Polaris team)
date: 2026-04-15
source: https://shopify.engineering/autoresearch
tags: [autoresearch, pi-autoresearch, ralph-loop, agent-loop, shopify]
---

# Autoresearch isn't just for training models

David Cortés on the Shopify Polaris team shares the story of how he and Tobi Lütke generalized Andrej Karpathy's Autoresearch concept to improve 40+ metrics across Shopify, then open-sourced the project as **pi-autoresearch** (3,600+ GitHub stars, 200+ forks).

## The Problem

CI build times were a persistent bottleneck — every tiny change triggered random visual regression failures, each taking 30 minutes. Manual optimization was deprioritized because "no one's sprint plan includes 'spend three months reducing build time by 30%'."

## The Insight

Autoresearch was originally designed for ML model training (Karpathy's GPT-2 experiments). Cortés initially dismissed it: "This is for smart people that train models, not for me." But colleague Swati Swoboda had been experimenting with it for **more than model training** — using it to improve arbitrary metrics.

## The pi-autoresearch Extension

Built as a Pi agent harness extension in under 30 minutes of back-and-forth prompting:

1. **Find a metric to improve** (e.g., Polaris build time: 19.1s baseline)
2. **Measure the baseline**
3. **Hypothesis testing**: For each iteration, form a hypothesis, test it, three outcomes: faster (keep), crashes (discard), slower (discard)
4. **Repeat infinitely** — system prompt says "NEVER STOP LOOPING"

## Key Differentiator from One-Shot Agent Prompts

A one-shot prompt ("Improve Polaris build time") failed to produce working code. The Autoresearch loop succeeds because:
- **Targeted focus on a single metric** with clear measurement
- **Clear goal and clear way to measure progress**
- **Permission to try crazy things** — "While running this infinitely, it has the option to try things it wouldn't try in a normal run"
- **Small increments compound** — even 1% improvement per iteration adds up to significant gains

## Results at Shopify

- Polaris build time: **65% faster** (removed redundant VRT+Storybook compilation, TypeScript transform reduced from 580→105 files)
- Liquid codebase: **53% faster** combined parse+render, **61% fewer object allocations**
- Unit tests running **300x faster** in some cases
- React component mounting: **20% faster**
- pnpm performance improvements
- Playwright test speed improvements

## Tobi Lütke's Contribution

Tobi sent a 32-commit PR adding: multi-metric support, consistent per-iteration execution scripts, skill improvements, auto-commits, and more. They pair-programmed across timezones (Barcelona ↔ Toronto).

## The Key Shift

> "Before autoresearch, AI agents were doing the same work humans did, just faster. Autoresearch is different — it does work nobody would attempt manually. The toil that humans correctly deprioritize turns out to be the perfect workload for an autonomous loop."

## Open Source

- GitHub: pi-autoresearch (3,600+ stars, 200+ forks)
- Install: `pi install <repo-url>`
- Internal `#autoresearch-wins` Slack channel at Shopify
