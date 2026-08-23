---
title: "Fable & The End of the Free Lunch"
author: Drew Breunig
type: article
date: 2026-08-23
date_ingested: 2026-08-23
source_url: https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html
ingested_via: x-accounts-scan (tweet 2091606513853042760 by @dbreunig)
tags:
  - inference-cost
  - model-routing
  - context-engineering
  - agentic-coding
---

# Fable & The End of the Free Lunch

Source: https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html (published 2026-08-23)
Retrieved via Jina Reader, 2026-08-23.

## Summary

Breunig's thesis: Claude Fable (Anthropic's frontier coding model) ended the "free lunch" era of agentic coding — the period when a new, cheaper model every few months would paper over the inefficiencies of your coding harness and context strategy, making optimization pointless (by analogy to Herb Sutter's "The Free Lunch" and the mid-2000s stagnation of single-thread Moore's Law performance).

Key arguments:

1. **Cost shock changes the calculus.** Fable is incredible but extremely expensive; Opus was "good enough" (as were GPT-5.6, Kimi K3, and even GLM) for most code that teams actually need. So practitioners started "thinking about what work went where."

2. **GLM 5.2 is the exemplar of the tiering shift.** Released the same week as Fable, it costs roughly 1/9th of Fable (~1/5th of Opus 5). For most rote coding it is more than sufficient — *especially when provided with great context*. Breunig's personal workflow: chat with Fable to interrogate and shape a design, then hand a brief off to GLM for execution.

3. **Falling inference prices won't reverse the trend.** Those same price gains benefit the K3s and Qwens; and as harnesses get better (cf. his "harnesses are situated agents" post, 2026-08-14), it becomes easier to give weaker-but-great models enough context to perform well.

4. **Fable's "other shock" locks in the change.** Fable's access controls, dynamic degradation, and required data retention spooked enough companies (and countries) into thinking about where they send their traces and where they get their tokens — a data-sovereignty push that further fragments the "send everything to one frontier API" default.

## Context / why it matters

- Continues Breunig's 2026 thread: prompt debt → task/model separation (DSPy/GEPA) → model tiering/routing economics.
- Reinforces the "tiered model cascade" pattern already documented in wiki concepts (e.g., DeepSWE's Pro-first cascade: 82.7% pass rate at $8.28; NanoGPT Speedrun Frontier's harness×model cost/quality analysis).
- Echoes production model-routing products (Ramp Router: ~40% average cost cut, 2.75T+ tokens routed/month; NVIDIA NeMo Switchyard: -59% cost / -35% runtime for coding agents) and the open question of whether cost-based routing is durable or a transient phase.
- Ties to Claude Fable 5's documented friction points: dynamic degradation and required data retention (see [[entities/fable]], [[concepts/claude/fable-5]]).
