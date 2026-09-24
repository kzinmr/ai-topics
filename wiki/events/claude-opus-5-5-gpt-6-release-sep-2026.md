---
title: "Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna release and the new price war"
created: 2026-09-23
updated: 2026-09-23
type: event
tags:
  - announcement
  - openai
  - anthropic
  - pricing
  - frontier-models
sources:
  - raw/articles/simonwillison.net--2026-sep-22-opus-and-sol-and-luna--3535d880.md
  - raw/newsletters/2026-09-23-ainews-claude-opus-5-5-the-new-default-model-for-ainews-and-everybody-cuts-price.md
related:
  - entities/openai
  - entities/anthropic
  - entities/epoch-ai
  - events/claude-opus-5-release-july-2026
  - events/claude-fable-5-1-release-sep-2026
  - concepts/llm-cost-crisis
---

# Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna release and the new price war (Sep 22, 2026)

On 2026-09-22 Anthropic released **Claude Opus 5.5** and, about an hour later, OpenAI released **GPT-6 Sol** and **GPT-6 Luna** — a same-day double release that ignited a new price war one tier below the $10/$50 flagship models (GPT-6 Astra, Claude Fable 5.1). The day before had already brought Grok 4.7 and MiMo v2.6 Flash/Pro. Simon Willison's same-day write-up is the primary synthesis.

## Pricing

| Model | Input | Cached input | Output |
|---|---|---|---|
| GPT-6 Luna | $0.10/M | $0.01/M | $0.50/M |
| GPT-6 Sol | half of GPT-5.6 Sol | — | — |
| Claude Opus 5.5 | $4/M | cache reads −60% | $20/M |

- **GPT-6 Sol and Luna are half the price of their GPT-5.6 equivalents** (even against November's promotional pricing). GPT-5.6 Terra, now priced the same as GPT-6 Sol, has lost its remaining reasons to exist.
- GPT-6 Luna at $0.10/$0.50 is among the cheapest models OpenAI ever released, beaten only by far weaker GPT-4.1 Nano and GPT-5 Nano.
- Grok 4.7 (priced $2/$6, previously undercutting GPT-5.6 Sol) is now equally priced to GPT-6 Sol on input.
- **Opus 5.5 breaks the Opus price plateau**: Opus 4.5→5 all sat at $5/$25; 5.5 is a 20% cut to $4/$20, with **cache reads down 60%** — significant because 90%+ of input tokens in long agentic conversations are billed at cached prices. Its new price equals *pre-cut* GPT-5.6 Sol, i.e. still above GPT-6 Sol.
- Anthropic says **Sonnet 5.5 and Haiku 5.5 are coming soon**; open question whether Haiku (currently $1/$5) can regain low-end competitiveness against GPT-6 Luna at one-tenth the price.

## Opus 5.5: addressing the communication-style complaints

Anthropic's Thariq Shihipar: "Opus 5.5 is the result of your feedback. It communicates clearly, it's cheaper per token than Opus 5.0 with the intelligence of Fable 5.1, it's very token efficient and works across every effort level." Also claimed better at Blender.

## The max-effort failure (Willison's pelican test)

In a first for the "SVG of a pelican riding a bicycle" test, **Opus 5.5 at "max" thinking failed to return a response twice** — it over-thought until hitting the 128,000 max output token limit *while still reasoning* (each failure cost $2.56 and ~20 minutes). Willison's conclusion: "max" is effectively useless if it breaks on a trivial prompt. Fable 5.1 on max produced his best pelican yet. His family comparison grids (5.6 family → bolder colors; 6 family → muted) remain his tool of choice for comparing a model family across reasoning levels.

## Adoption notes

Willison switched his defaults to GPT-6 Sol (Codex) and Opus 5.5 (Claude Code); the Datasette Agent demo upgraded to GPT-6 Luna ("fast and competent" at SQL and HTML/JS).

## Macro context: "The plunging price of thought"

One day earlier (Sep 22), Epoch AI published its finding that the cost of a given level of AI performance has fallen ~47%/quarter (13×/year) since 2023 — faster than any transformative technology in history — with the o3 → GPT-5.6 Luna 725× GPQA-Diamond cost collapse as its headline. The Sep 22 double release is a live demonstration of exactly that curve; @emollick amplified the report's chart on Sep 23. See [[entities/epoch-ai]].

## See Also

- [[events/claude-opus-5-release-july-2026]] — the model 5.5 supersedes
- [[events/claude-fable-5-1-release-sep-2026]] — flagship tier above this price war
- [[concepts/llm-cost-crisis]] — margin/economics framing of rapid price decline
- [[entities/openai-astra]] — GPT-6 family's flagship
