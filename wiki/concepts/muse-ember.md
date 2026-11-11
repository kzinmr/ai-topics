---
title: Muse Ember
type: concept
created: 2026-11-11
updated: 2026-11-11
tags:
  - model
  - muse-ember
  - meta
  - ai-agents
  - price-performance
  - model-economics
  - small-language-model
aliases:
  - Muse Ember 1.0
sources:
  - raw/articles/research.meta.ai--blog-muse-ember--muse-ember.md
  - raw/articles/simonwillison.net--2026-nov-10-muse-ember--7579b7c0.md
---

# Muse Ember

**One-line summary**: Meta's smallest, most efficient agent model — AA Intelligence Index 33.9 at $0.116/task, matching Haiku 5.5's best score at roughly a third of the cost.

## What it is

Muse Ember is Meta Superintelligence Labs' entry in the low-cost / high-throughput agent tier occupied by Claude Haiku 5.5 and GPT-6 Luna — the model class built for "the work agents repeat all day: tool calls, coding subtasks, routing, extraction, and long document parsing." Released **2026-11-09** alongside [[concepts/claude/fable-5|Claude Fable 5.2]], it is the fourth entry in the Muse family after [[entities/muse-spark|Muse Spark]], Muse Spark Open, and [[entities/muse-glimmer|Muse Glimmer]].

Meta's headline claim: "no model scores higher for less per task" on the full Artificial Analysis leaderboard — Ember sits on the efficiency Pareto frontier rather than merely being cheap.

## Intelligence per dollar

Artificial Analysis Intelligence Index against cost per task (Ember costs are Meta's estimates at proposed pricing):

| Model | Cost per task (USD) | Intelligence Index |
|---|---|---|
| Muse Ember | $0.116 | 33.9 |
| Muse Ember | $0.136 | 35.8 |
| Claude Haiku 5.5 | $0.092 | 24.6 |
| Claude Haiku 5.5 | $0.159 | 29.6 |
| Claude Haiku 5.5 | $0.248 | 34.3 |
| Claude Haiku 5.5 | $0.411 | 36.2 |
| GPT-6 Luna | $0.073 | 21.4 |
| GPT-6 Luna | $0.104 | 23.3 |
| GPT-6 Luna | $0.152 | 27.8 |

At max reasoning (Meta's own eval set, best published harness for Terminal-Bench):

| Eval | Muse Ember | Claude Haiku 5.5 | GPT-6 Luna |
|---|---|---|---|
| AutomationBench-AA (E2E business workflows) | **37.8** | 13.9 | 20.2 |
| [[concepts/agents-last-exam]] (end-to-end agent tasks) | **61.6** | 57.0 | 57.1 |
| Personal Superintelligence Index (internal composite) | **46.8** | 36.1 | 37.0 |
| Terminal-Bench 4.0 (agentic terminal coding) | **40.9** | 39.2 | 16.4 |

The AutomationBench-AA gap is the outlier: 37.8 vs 13.9 for Haiku 5.5 is a ~2.7x margin, far larger than Ember's margins on the other three suites. The "Personal Superintelligence Index" is a Meta-internal composite and is not externally comparable.

## Pricing and the long-context cliff

Base pricing matches both competitors at $0.10/M input, $0.01–$0.05/M cached, $0.50/M output — but each model raises price at a different prompt-size threshold, which is where the tier actually differentiates:

| Model | Prompt size | Input ($/M) | Cached input | Output |
|---|---|---|---|---|
| GPT-6 Luna | ≤272k | $0.10 | $0.01 | $0.50 |
| GPT-6 Luna | >272k | $0.20 | $0.02 | $0.75 |
| Muse Ember 1.0 | ≤200k | $0.10 | $0.004 | $0.50 |
| Muse Ember 1.0 | >200k | $0.30 | $0.012 | $1.50 |
| Claude Haiku 5.5 | ≤100k | $0.10 | $0.01 | $0.50 |
| Claude Haiku 5.5 | >100k | $0.50 | $0.05 | $2.50 |

Ember's cached-input rate ($0.004/M) is 2.5x cheaper than either competitor's. Its long-context cliff is the *latest* of the three (200k vs Haiku's 100k) but the steepest once crossed (3x input, 3x output vs Haiku's 5x/5x on a shorter free window). All three support up to 1M input tokens.

Willison's caveat applies: per-token pricing is a weak comparison once reasoning tokens mean models consume radically different token counts on the same problem — which is exactly why the cost-per-task table above is the operative comparison.

## Reasoning-effort behavior (independent test)

Ember exposes six reasoning levels — minimal, low, medium, high, xhigh, max. Simon Willison's SVG-rendering probe found the effort axis **did not cleanly map to output quality**: the `high` level failed to return a full SVG at all, and quality across levels was non-monotonic. Notably, Ember's `max` pelican was comparable in quality to one obtained from **Muse Wonder at 40x Ember's price** — an independent hint that the effort ladder is poorly calibrated relative to the price ladder within Meta's own family. See [[concepts/claude/effort-control]] for the broader effort-control design space.

## Reception

HN 50429024 — 330 points, 140 comments (2026-11-10).

The launch lands on the same day as Fable 5.2 at **80x Ember's price** ($8/$40 per M). That pairing is the strategic story: Meta is competing at the bottom of the tier ladder that Anthropic has restructured into a tiered agent topology (Opus 5.5 daily driver, Fable 5.2 as Advisor/Orchestrator). Ember is a bet that the repeatable sub-task layer, not the frontier layer, is where agent volume — and therefore spend — concentrates.

## Related

- [[entities/meta]] — publisher; Meta Superintelligence Labs
- [[entities/muse-spark]] — flagship closed sibling in the Muse family
- [[entities/muse-glimmer]] — open/community Muse model
- [[concepts/claude/fable-5]] — Claude Fable 5.2, launched the same day at 80x the price
- [[concepts/claude/opus-5]] — Anthropic's recommended daily-driver tier
- [[concepts/agents-last-exam]] — agent benchmark on which Ember posts 61.6
- [[concepts/ai-benchmarks/terminal-bench]] — agentic terminal coding suite
- [[concepts/claude/effort-control]] — reasoning-effort ladders and their calibration
- [[concepts/token-economics]] — cost-per-task framing
- [[concepts/meta-harness]] — Meta's agent execution stack

## Sources

- [Introducing Our Smallest, Most Efficient Model: Muse Ember — Meta AI Research](https://research.meta.ai/blog/muse-ember) (raw: `raw/articles/research.meta.ai--blog-muse-ember--muse-ember.md`)
- [Simon Willison on Muse Ember](https://simonwillison.net/2026/Nov/10/muse-ember/) (raw: `raw/articles/simonwillison.net--2026-nov-10-muse-ember--7579b7c0.md`)
- [HN discussion 50429024](https://news.ycombinator.com/item?id=50429024)
