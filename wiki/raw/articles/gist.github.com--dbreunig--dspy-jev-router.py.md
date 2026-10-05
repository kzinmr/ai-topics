---
title: "dspy-jev-router.py — Model Router via DSPy + Jev"
url: "https://gist.github.com/dbreunig/949b42c7202508881d7c5a64ccd0fb9b"
author: "Drew Breunig"
date: 2026-10-03
source: "X/Twitter @dbreunig"
tags: [model-routing, dspy, llm-judge, cost-optimization, example-code]
scraped_at: 2026-10-05
status: full
---

# dspy-jev-router.py — Model Router via DSPy + Jev

**Author:** Drew Breunig (@dbreunig)
**Type:** GitHub Gist (Python)
**Date:** October 3, 2026
**URL:** https://gist.github.com/dbreunig/949b42c7202508881d7c5a64ccd0fb9b

## Overview

A ~15-minute sketch of a **model router** built with two tools:

- **DSPy** — declarative self-improving Python for language models (signature-based module abstraction)
- **Jev** — Breunig's own library for **LLM classification** (used to predict a task's "answerability" / difficulty from the initial prompt)

## How It Works

1. **Classify the incoming prompt**: A Jev classifier is trained on 80 sample prompts labeled by a strong model (gpt-5.6-sol) across five levels:
   - L1: no reasoning required (e.g. "what's my current balance?")
   - L2: minimal reasoning (e.g. summarizing an email thread)
   - L3: multi-hop reasoning (e.g. multi-document policy questions)
   - L4: multi-hop + tool use (e.g. SQL query + calculation)
   - L5: research, ambiguity, synthesis (e.g. competitive analysis + memo)
2. **Route by predicted difficulty**: a lookup table maps level → model. In the sketch, the mapping is "small" (L1–L3) vs. "large" (L4–L5) — both set to gpt-5.6-terra for demo, but the table is trivial to repoint (e.g. L1–L2 → `gpt-5.6-luna`, L3 → `gpt-5.6-terra`, L4–L5 → `gpt-5.6-sol`).
3. **Answerability gate**: if the classifier predicts "No" (unanswerable), the router short-circuits with `Answerability.NO` instead of burning tokens on a doomed query.

```python
LEVEL_TO_MODEL = {
    "L1": "gpt-5.6-terra",
    "L2": "gpt-5.6-terra",
    "L3": "gpt-5.6-terra",
    "L4": "gpt-5.6-terra",
    "L5": "gpt-5.6-terra",
}
```

The DSPy entrypoint is a single `dspy.Predict("question -> answer")`, wrapped by `ModelRoutedModule` which overrides `forward()` to consult Jev's prediction and rewrite the active LM before delegating.

## Why It Matters

Breunig tweeted he was "surprised at how well it works" for 15 minutes of work. The gist is a concrete, minimal demonstration of his **model routing** thesis — using cheap models for easy tasks and reserving expensive frontier models for genuinely hard ones. It connects directly to two of his established frameworks:

- **The Model Routing problem** ([[concepts/model-routing]]) — routing queries across a heterogeneous model pool by predicted difficulty/cost
- **Prompt Debt** ([[concepts/prompt-debt]]) — the router treats model selection as a *measurable specification* (Jev classifier) rather than a hand-tuned heuristic

The DSPy+Jev pairing also demonstrates his broader argument that prompt-writing should give way to measurement-driven programmatic abstractions.

## Related Wiki Pages

- [[entities/drew-breunig]] — author; CEO of Cmpnd, creator of Jev
- [[entities/samuel-colvin]] — DSPy creator
- [[concepts/dspy]] — declarative LM programming framework
- [[concepts/model-routing]] — routing queries across model tiers by predicted difficulty/cost
- [[concepts/prompt-debt]] — hand-tuned prompts as accumulating technical debt
- [[concepts/llm-as-judge]] — using LLMs to label training data for classifiers

## Source Tweet

> "A quick example of a model router, using DSPy and Jev, based on your initial prompt. Sketched this out in ~15 min, by request, and am surprised at how well it works!"
> — @dbreunig, 2026-10-03
