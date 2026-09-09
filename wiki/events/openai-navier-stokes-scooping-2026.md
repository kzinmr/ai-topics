---
title: "OpenAI Navier–Stokes Millennium Prize Resolution & Scooping Controversy"
created: 2026-09-09
updated: 2026-09-09
type: event
confidence: medium
tags:
  - openai
  - anthropic
  - ai-ethics
  - datasets
  - generative-ai
  - ai-agents
sources:
  - raw/articles/simonwillison.net--2026-sep-8-on-navier-stokes--9538509f.md
  - raw/articles/johndcook.com--blog-2026-09-08-navier-stokes-in-the-news--3248b841.md
related: [openai-astra, openai, simon-willison, data-repetition-in-training]
---

# OpenAI Navier–Stokes Millennium Prize Resolution & Scooping Controversy

On September 8, 2026 OpenAI announced that an **unreleased internal model** had produced a resolution to the **Navier–Stokes existence and smoothness problem** — one of the seven Millennium Prize Problems ($1,000,000 prize since May 24, 2000). The announcement triggered an immediate priority/scooping controversy and reopened the question of what "using my data to improve model performance" actually means. Simon Willison's write-up ([On the Navier–Stokes Millennium Prize Problem](https://simonwillison.net/2026/Sep/8/on-navier-stokes/), Sep 8) is the sharpest third-party analysis.

## The scale of the compute effort

OpenAI's own account of the effort:

- Sep 1: OpenAI heard rumors that two Millennium Prize problems had been resolved; launched an internal effort to evaluate its internal model on **all open Millennium Prize problems** plus other high-impact problems.
- Sep 5: agents arrived at the Navier–Stokes resolution ~**88 hours** after launch; Lean formalization and verification took **17 more hours via GPT-6 Astra**.
- Across all attempted problems: **4.9 million agent messages, ~300 billion output tokens**. Navier–Stokes alone: **2.7 million messages, ~130 billion output tokens**.
- Simon's cost estimate: 300B output tokens at public GPT-6 Astra API prices ≈ **$15,000,000** (internal cost structure unknown).

## The scooping controversy

- **Tristan Buckmaster** (NYU) and **Levent Alpöge** (then at Anthropic) had worked on related problems for almost a year, making heavy use of Claude and Codex (mainly GPT-5.6 Sol), with a breakthrough on **August 15**. Buckmaster published a hastily-prepared account of what happened alongside their own results.
- Buckmaster learned OpenAI had a team on a related problem with a similar approach, and asked **when OpenAI's first prompt had been sent**. Per Buckmaster: not answered directly for some time; eventually agreed it was "in the past few days, **after information about our work had reached OpenAI**."
- Buckmaster asked whether OpenAI's model had been **trained on or had access to their Codex sessions** (which contained all their drafts for the whole project). Told the model "did not look up user data"; the **training question was not answered**.
- OpenAI offered a concurrent release or to have Buckmaster author their result, but stated **Alpöge would not be invited as co-author due to OpenAI's competitive relationship with Anthropic**.
- OpenAI's position: "We did not see any of their work through any means until they released it publicly — in particular, no specific user data was accessed." But: "While unlikely, we **cannot rule out that de-identified data derived from their usage of our products helped improve our models**." OpenAI notes their proofs differ significantly, and even the precise results proved differ in the Euler case (forced vs unforced).

## Simon Willison's interpretation

Willison reads the episode as OpenAI hearing rumors of LLM-solved Millennium problems and moving to demonstrate its latest model's power "**without thinking too hard about the optics of scooping a team who had been using OpenAI's own models** to work on the problem for the best part of a year." Two generalizations he draws:

1. **Rumors as capability triggers** — echoing Anil Madhavapeddy's observation that "just a rumour of a bug is enough to find a security exploit these days," Willison asks whether the same now holds in mathematics: *knowing an unpublished solution exists may trigger millions of dollars of LLM spending to get there first.*
2. **"Used to improve model performance" is still undefined** — his new favorite hypothetical, replacing the API-key-regurgitation and competitor-brainstorming thought experiments: *if I use ChatGPT/Codex to partially solve a Millennium Prize problem, what are the chances my work influences training such that a later model helps someone else solve it first?* This is the same under-specified training-data consent question that surfaces across [[concepts/data-repetition-in-training]] and the regurgitation literature.

## See Also

- [[entities/openai-astra]] — the GPT-6 Astra family used for Lean verification of the proof
- [[entities/simon-willison]] — source of the analysis above
- [[entities/openai]] — OpenAI company page
- [[concepts/ai-training-data-controversies]] — the recurring "improve model performance" consent gap
- [[concepts/ai-mathematics-theorem-proving]] — AI-driven theorem proving context
