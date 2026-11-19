---
title: "Just Large Models"
type: concept
created: 2026-04-25
updated: 2026-11-19
tags:
  - concept
  - bitter-lesson
  - scaling
  - ai-industry
  - foundation-models
aliases:
  - just-large-models
  - scale-first thesis
sources:
  - raw/articles/2020-05-28_gwern-scaling-hypothesis.md
related:
  - "[[concepts/rich-suttons-bitter-lesson]]"
  - "[[concepts/scaling-laws]]"
status: active
---

# Just Large Models

**"Just large models"** is the position that most apparent AI-engineering problems — capabilities, reliability, tool use, alignment surface — are best solved by scaling the base model (data + compute + RL) rather than by hand-built scaffolding, clever prompting, or bespoke pipelines around small models. It is a practical restatement of the [[concepts/rich-suttons-bitter-lesson]] for product builders: bet on the model improving, and design so that improvements transfer.

## The Claim

| Strategy | "Just large models" view |
|----------|-------------------------|
| Hand-crafted rules / heuristics | Eaten by scale; brittle at the long tail |
| Elaborate scaffolds compensating for weak models | Deprecated by the next model release ("harness tax") |
| Fine-tuning small models for narrow tasks | Still valid where cost/latency/privacy dominate, but capability ceilings stay fixed |
| Prompt/context engineering | Durable, because it *feeds* the model rather than substituting for it |

The distinguishing move is **directionality**: scaffolds should *elicit* model capability (tools, feedback loops, verification), not *substitute* for it. When a scaffold exists only to paper over a model deficiency, it becomes technical debt the moment the deficiency is trained away.

## Arguments For

- **Scaling laws are empirical and cheap to exploit**: loss falls predictably with compute ([[concepts/scaling-laws]], [[concepts/scaling-hypothesis]]).
- **Historical pattern**: hand features (OCR pipelines, NLU slots, code-completion heuristics) repeatedly lost to end-to-end models — Gary Marcus vs. the bitter lesson, over and over.
- **Scaffold depreciation is measurable**: coding-agent harnesses built to compensate for 2024-era models (retry loops, output-format guards) lose their reason to exist under 2025–26 frontier models; see [[concepts/agent-model-drift]] and harness migration patterns.
- **Capability transfers downstream**: a stronger base model improves tool use, planning, and self-verification simultaneously — improvements you'd otherwise hand-engineer per-domain.

## Arguments Against / Nuance

- **The bitter lesson has latency/cost/privacy edges**: small specialized models remain rational where $/token, ms, or on-device constraints bind (small language model, on device inference).
- **RL and environments are now part of "scale"**: "just large models" in 2026 includes RL post-training on verifiable environments — the model gets better because someone built the *environment and reward*, which is engineering (agent training, [[concepts/post-training/rlvr]]).
- **Data wall / diminishing returns**: pretraining data quality and repetition effects complicate naive scale maximalism ([[concepts/data-repetition-in-training]]).
- **Economic framing**: labs' scaling bets vs. application-layer value capture is a live industry debate (absorption frontier, ai moat).

## Practitioner Heuristics

1. Prefer elicitation scaffolds (tools, tests, feedback) over compensation scaffolds (patches for known model failures).
2. Version-pin your assumptions: record which model release motivated each piece of harness complexity; delete on upgrade.
3. Spend scarce engineering time on **environments, evals, and data** — the parts of "scale" that don't get commoditized.
4. Choose small models deliberately for cost/latency/edge niches, not by default out of model-size superstition.

## Related Concepts

- [[concepts/rich-suttons-bitter-lesson]] — the historical argument this operationalizes
- [[concepts/scaling-laws]] / [[concepts/scaling-hypothesis]] — the empirical basis
- [[concepts/harness-engineering]] — what to build *instead* of compensation scaffolds
- [[concepts/test-time-scaling]] — scaling compute at inference as an extension of the same bet
- [[concepts/just-large-models]] competitors: [[concepts/agentic-alternative-to-graphrag]] (task-specific retrieval engineering as counterexample)

## Sources

- Gwern, "The Scaling Hypothesis" (2020) — `raw/articles/2020-05-28_gwern-scaling-hypothesis.md`
- Rich Sutton, "The Bitter Lesson" (2019) — via [[concepts/rich-suttons-bitter-lesson]]
