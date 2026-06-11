---
title: "LLM Code Quality"
type: concept
created: 2026-06-09
updated: 2026-06-11
tags:
  - concept
  - llm
  - coding-agents
  - ai-coding
  - software-engineering
sources:
  - raw/articles/entropicthoughts.com--llms-and-almost-good-code--38c3d31a.md
  - raw/articles/2026-06-10_curlewis_lines-of-code-got-a-better-publicist.md
---

# LLM Code Quality

## Overview
LLM-generated code tends to be approximately 10% more complex than necessary, even on easy tasks. This complexity is readily accepted because the code solves immediate problems, but may have long-term maintenance consequences.

## Key Findings

### Complexity Overhead
- Frontier models working on easy tasks generate code ~10% more complex than necessary
- Complexity comes from code that is "right here, right now" solving an immediate problem
- Developers accept this complexity too easily

### Case Study: HTTP Header Encoding (Haskell)

A frontier model generated a 24-line Haskell function (`toHeaderValue`) to safely encode arbitrary strings as HTTP header values (RFC 5987). The function was **functionally correct** and passed all generated tests — but contained subtle inefficiencies:

- **Dead code in `padHex`**: The function zero-pads hex values below `0x10`, but the upstream `isPrintable` filter already removes all bytes below `0x20`. The padding branch is **unreachable** — a CI statement coverage check flagged it.
- **Custom `percentEncode`**: The model wrote its own percent-encoding implementation instead of using the standard library's `urlEncode`.
- **"Spooky action at a distance"**: The dead code resulted from implicit assumptions about the function's calling context — correct in practice but fragile.

**Human rewrite**: 15 lines shorter (8% of the 200-line change), using standard library functions (`urlEncode`, `Text.replace`). Technically over-encodes (RFC 5987 is more lax than URL encoding) but simpler and more maintainable.

### The "Right There, Right Now" Acceptance Problem

The core insight is that developers accept LLM-generated code because it solves the immediate problem:

- The code **works** and is **proven correct by tests**
- It is **highly local** — can be replaced without touching anything else
- Rejecting it to rewrite manually feels **silly** when there's pressure to ship
- The complexity is only ~8% — not a disaster today

This acceptance is rational in the moment but creates **systemic technical debt** when repeated across thousands of LLM-assisted changes.

### Scaling Concern

The author raises an open question: if frontier models generate ~8% excess complexity on **easy** tasks, what happens on harder tasks?

- Could the overhead grow to 20%, 40%, or even 3×?
- Will developers "put their foot down" at some threshold?
- Or will they keep accepting because it's "right there, right now"?
- Counter-argument: code-writing robots improve fast enough that future models may handle the cleanup. Author is "not convinced."

## Connection to AI Vanity Metrics

The "Lines of Code Got a Better Publicist" analysis by David Curlewis (June 2026) connects directly to the LLM code quality findings: when AI-generated code is **~10% more complex** and human comprehension drops by **17%** (Anthropic's own RCT), volume-based metrics become especially misleading.

- **More code ≠ better code**: LLMs produce more lines of code that is measurably more complex — yet AI vendors report volume metrics (lines of code, percentage of AI-generated code) as if they were productivity gains.
- **The "right there, right now" acceptance problem** compounds: developers accept the 10% complexity overhead because it works *now* — volume metrics then count this acceptance as progress, creating a feedback loop that rewards complexity accumulation.
- **DORA metrics vs. token counts**: The industry has validated outcome metrics (deployment frequency, lead time, change failure rate, time to restore service) over decades. LLM code quality analysis suggests that volume metrics may actually *mask* degradation in these real outcomes.
- See [[concepts/ai-engineering-metrics-vanity]] for the full argument on why volume metrics systematically misrepresent AI engineering impact.

## Related Concepts
- [[concepts/ai-coding]] — broader AI-assisted development practices
- [[concepts/coding-agents/coding-agents]] — autonomous coding agent systems
- [[concepts/technical-debt]] — accumulated complexity costs
- [[concepts/vibe-coding]] — the broader trend of accepting AI-generated code without deep review
