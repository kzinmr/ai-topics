---
title: "AI Engineering Metrics — Vanity vs. Outcome Measurement"
type: concept
created: 2026-06-11
updated: 2026-06-11
tags:
  - concept
  - coding-agents
  - metrics
  - software-engineering
  - ai-adoption
sources:
  - raw/articles/2026-06-10_curlewis_lines-of-code-got-a-better-publicist.md
---

# AI Engineering Metrics — Vanity vs. Outcome Measurement

## Overview

AI vendors increasingly use **volume metrics** — lines of code, percentage of AI-generated code, total tokens — as proxies for productivity and engineering impact. David Curlewis (June 2026) argues these are **vanity metrics**: they measure adoption intensity rather than genuine outcomes, and they cannot be falsified. The industry spent decades learning that lines of code and PR counts are bad ways to measure developers; AI vendors have simply repackaged the same flawed metric with better marketing.

## The Shift from Outcome Claims to Volume Claims

### Then: Falsifiable Outcome Claims

GitHub's original Copilot claim was that developers completed tasks **55% faster** — an outcome claim. It was bold, falsifiable, and about value. If wrong, you could show it was wrong.

### Now: Unfalsifiable Volume Claims (2026)

| Vendor | Claim | Type |
|--------|-------|------|
| Google | 75% of new code is AI-generated | Volume (adoption) |
| Anthropic | ~80% of merged production code written by Claude; "8x more code per quarter" | Volume (adoption) |
| OpenAI | ~80% of code AI-generated | Volume (adoption) |
| Cursor | 100M+ lines of enterprise code written per day | Volume (adoption) |

These claims **cannot fail**: "75% of our code is AI-written" can be true and keep increasing regardless of whether anything actually got better — faster delivery, fewer incidents, happier customers. A volume number only disappoints if adoption stalls, and adoption is the one thing most agree is real.

## The Research Evidence

The strongest pro-adoption result remains **Cui et al.** (~5,000 developers, +26% completed tasks, biggest gains for junior devs). However, the outcome evidence has grown complicated:

### Conflicting Findings

- **GitClear**: Code churn rising and refactoring collapsing as Copilot adoption deepened
- **METR (2024)**: Experienced open-source devs were 19% *slower* with AI in their own codebases, while believing they were 20% faster
- **METR (Feb 2026 walkback)**: Follow-up estimates flipped to a speedup — but with error bars "wide enough to ride a Moto Guzzi through." Abandoned the study design entirely because developers now refuse to work without AI and can't reliably self-report time on agentic work. Latest position: AI probably speeds developers up in 2026, but we can no longer cleanly measure by how much.
- **NBER survey** (~6,000 executives): 69% of firms actively using AI, but ~90% report **no measurable productivity impact**
- **Anthropic RCT**: AI-assisted developers scored **17% lower on code comprehension**, with no statistically significant productivity gain — published by the same company claiming "8x more code shipped"

Cross-study consensus: roughly **10% organizational gains**. Useful, but not "you don't need developers anymore" territory.

## Vanity Metrics Beyond Vendor Claims

The pattern extends beyond AI vendor marketing:

- **CMU SEI + Accenture AI Adoption Maturity Model**: Five levels, eight dimensions, marketed off the stat that 95% of organizations see no returns — measures adoption intensity and calls it maturity
- **Steve Yegge's "8 levels of AI-assisted development"**: Ranks you by which tools you run and how much supervision you give them
- **Every tools vendor's maturity ladder**: Top rung is usually "use more of our product"

Augment surveyed 219 engineering leaders asking them to define "AI-native engineering" — they got 219 different answers. A field with no consensus definition cannot have a consensus maturity model.

## Real-World Impact: Workforce Cuts Citing AI

These metrics are not decorative — they move budgets and headcount plans:

- **Block (Jack Dorsey, Feb 2026)**: Cut over 40% of workforce (4,000+ people) with AI as the explicit core thesis: "A significantly smaller team, using the tools we're building, can do more and do it better." Notably: Dorsey said in the same announcement that the business was strong and gross profit was growing.
- **Atlassian (2026)**: Cut 10% (~1,600 people), conceding it would be "disingenuous to pretend AI doesn't change the mix of skills we need or the number of roles required."

Curlewis's challenge: If AI made everyone more productive and created free headcount, why wouldn't you use it to deliver more value to customers — measured as MAU, conversion, revenue? Choosing layoffs instead suggests the productivity claim is doing PR work for a decision made for other reasons.

## The Core Argument: Measure Outcomes, Not Tokens

We already know how to measure whether engineering is delivering:

- **DORA metrics** (deployment frequency, lead time for changes, change failure rate, time to restore service)
- **Reliability** (incident rates, SLO adherence)
- **Rate of meaningful change** (features shipped, customer value delivered)
- **Revenue and customer value** (MAU, conversion, retention)

These are "battle-tested, crusty" metrics that the industry has validated over decades. Adoption is the **starting line**, not the scoreboard.

## The Litmus Test

> "Is that an outcome, or a volume?"

Asking this question in vendor pitches, exec reviews, or LinkedIn posts quickly deflates positions built on vanity metrics.

## Related Concepts

- [[concepts/llm-code-quality]] — LLM-generated code quality and complexity overhead; the "right there, right now" acceptance problem
- [[concepts/ai-labor-displacement]] — AI-driven workforce reduction and the "hypergrowth, hyper-inequality" thesis
- [[concepts/ai-slop-productivity-paradox]] — Gary Marcus on AI generating massive nominal productivity without real economic impact
- [[concepts/coding-agents/ai-code-quality]] — Quality-first approach to AI coding, counterpoint to volume-focused metrics
- [[concepts/vibe-coding]] — Development style accepting AI-generated code without deep review; enabled by volume-over-outcome thinking
- [[concepts/agent-productivity]] — Impact of AI coding agents on personal productivity and cognitive effects
