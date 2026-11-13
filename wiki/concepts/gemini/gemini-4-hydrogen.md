---
title: "Gemini 4 Hydrogen"
type: concept
created: 2026-11-13
updated: 2026-11-13
tags:
  - model
  - gemini
  - google
  - deepmind
  - code-model
  - pricing
  - token-economics
  - model-economics
  - ai-agents
confidence: medium
sources:
  - raw/articles/simonwillison.net--2026-nov-12-llm-gemini--4a05ae5e.md
related:
  - concepts/gemini/index
  - concepts/gemini/gemini-4-carbon
  - events/2026-10-01-gemini-4-argon-release
---

# Gemini 4 Hydrogen

**Gemini 4 Hydrogen** is the lowest-cost member of Google's Gemini 4 family, launched **2026-11-12** and confirmed publicly via Simon Willison's `llm-gemini` **0.37** plugin release notes (as usual, the plugin release is among the earliest reliable public sources of model availability).

## Positioning

Google describes Hydrogen as a **fast, disciplined execution model** for everyday work — writing code, running tests, verifying changes — either standing alone or pairing with the frontier siblings [[concepts/gemini/gemini-4-carbon|Carbon]] and [[events/2026-10-01-gemini-4-argon-release|Argon]] as "the high-efficiency execution engine in multi-model workflows." Most notably, **Hydrogen is the new Gemini free-tier model and the model that powers AI features in Google Search**.

## Pricing (the confusing part)

| Model | Dates | Input ($/M) | Cached input | Output ($/M) |
|-------|-------|-------------|--------------|--------------|
| Gemini 4 Carbon | Through Nov 30, 2026 | $2.00 | $0.10 | $10.00 |
| Gemini 4 Carbon | From Dec 1, 2026 | $4.00 | $0.20 | $20.00 |
| Gemini 4 Argon | Through Nov 30, 2026 | $2.00 | $0.10 | $10.00 |
| Gemini 4 Argon | From Dec 1, 2026 | $4.00 | $0.20 | $20.00 |
| **Gemini 4 Hydrogen** | (no date change announced) | **$1.50** | **$0.075** | **$7.50** |

Observations from Willison's analysis:

- **Carbon and Argon are identically priced** — and both **double in price on December 1, 2026**. Google's differentiation is behavioral, not price: Argon "delivers Gemini 4 intelligence with faster responses and lower token spend per turn compared to Gemini 4 Carbon," so same list price but fewer tokens per task.
- **Hydrogen is only a 25% discount today** — the "cheap model" label only makes sense after Dec 1, when it becomes a **75% discount** vs the doubled sibling prices.
- **Hydrogen is still expensive for the budget tier**: Claude Haiku 5.5 and GPT-6 Luna are both $0.10/$0.50 per M — **Hydrogen is 15x that** on input. This places Google's "cheap" tier far above the Anthropic/OpenAPI budget floor (cf. [[entities/gemini-decision-1]] at $0.10/MTok).

## Quality

Willison's standard pelican-SVG generation test, run across **all three Gemini 4 family members at all three supported effort levels** (full comparison grid), shows a **"quite stark" quality drop for Hydrogen** relative to Carbon/Argon — remarkable given how close the three models currently are in price.

## Related

- [[concepts/gemini/index]] — family overview
- [[concepts/gemini/gemini-4-carbon]] — frontier sibling (cyber/long-horizon positioning)
- [[events/2026-10-01-gemini-4-argon-release]] — Argon release
- [[concepts/model-economics]] / [[concepts/token-economics]] — budget-tier price war vs Haiku 5.5 / GPT-6 Luna

## Sources

- Simon Willison, "Release: llm-gemini 0.37" (Nov 12, 2026) — https://simonwillison.net/2026/Nov/12/llm-gemini/ (raw: `raw/articles/simonwillison.net--2026-nov-12-llm-gemini--4a05ae5e.md`)
- Google's Gemini 4 launch materials (as quoted in the above)
