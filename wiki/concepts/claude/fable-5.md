---
title: Claude Fable 5
type: entity
created: 2026-06-10
updated: 2026-06-10
tags:
  - model
  - claude-fable-5
  - anthropic
  - frontier-models
  - ai-safety
  - cybersecurity
  - alignment
  - benchmark
aliases:
  - Fable 5
  - Claude Fable
status: active
description: "Anthropic's Mythos-class model released for general use in June 2026. State-of-the-art on nearly all benchmarks. Safety classifiers fall back to Opus 4.8 on cyber/bio/distillation queries. $10/$50 per MTok."
sources:
  - raw/articles/2026-06-09_anthropic_claude-fable-5-mythos-5.md
  - raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md
  - raw/articles/2026-06-09_eliebakouch_fable-5-mythos-debated-research.md
  - raw/papers/2026-06-09_claude-fable5-mythos5-system-card.md
  - https://x.com/claudeai/status/2064394146916229443
  - raw/articles/simonwillison.net--2026-jun-9-claude-fable-5--6a315a85.md
---

# Claude Fable 5

Anthropic's Mythos-class model released for general use on June 9, 2026. State-of-the-art on nearly all tested benchmarks of AI capability, with safety classifiers that fall back to [[concepts/claude/opus-4-8|Claude Opus 4.8]] on sensitive queries. The same underlying model as [[concepts/claude/mythos|Claude Mythos 5]], differentiated by safeguards.

> "Fable is from the Latin *fabula*, 'that which is told,' akin to the Greek *mythos*. The safeguards are what distinguish the two models." — Anthropic

## Overview

Claude Fable 5 was announced on June 9, 2026 as "a Mythos-class model that we've made safe for general use." It represents the public release of Mythos-class capabilities, which Anthropic had previously restricted through [[concepts/project-glasswing|Project Glasswing]] due to safety concerns (particularly cybersecurity and dual-use biology capabilities).

The longer and more complex the task, the larger Fable 5's lead over other Claude models. It was simultaneously launched with **Claude Mythos 5** — the same model with safeguards lifted, restricted to Glasswing cyber defenders and select biology researchers.

**Pricing:** $10/MTok input, $50/MTok output — less than half the price of Claude Mythos Preview.

## Key Capabilities

### Software Engineering

| Benchmark/Eval | Result | Source |
|---------------|--------|--------|
| **Stripe** (50M-line Ruby codebase) | Codebase-wide migration in 1 day (team: 2+ months) | Customer feedback |
| **FrontierCode** (Cognition) | Highest score among frontier models at medium effort | Official eval |
| **CursorBench** | State-of-the-art | Michael Truell, Cursor CEO |
| **FrontierBench** (Cognition) | Highest-scoring model | Scott Wu, Cognition CEO |

> "Claude Fable 5 is the state of the art model on CursorBench. It's opened up a class of long-horizon problems that were out of reach for earlier models." — Michael Truell, Cursor CEO

### Knowledge Work

| Benchmark/Eval | Result | Source |
|---------------|--------|--------|
| **Hebbia Finance Benchmark** | Highest score of any model; gains in document reasoning, charts, tables | Official eval |
| **IMC trading analysis** | Aced nearly all categories (factual lookup, reasoning, root-cause, EV) | Customer feedback |
| **Replit ViBench** | Highest-performing — "nearly saturating base use cases" | Michele Catasta |
| **Genspark analytics** | First to break 90% — 10-point jump over Opus | Izzy Miller |

### Vision

- **State-of-the-art** on vision tasks
- Extracts precise numbers from detailed scientific figures
- Rebuilds web app source code from screenshots alone
- **Pokémon FireRed**: Beat the game with a minimal, vision-only harness — previous Claude models needed complex helper harnesses with maps, navigation aids, and game-state information

### Memory and Long-Context

- Stays focused across millions of tokens in long-running tasks
- Improves outputs using its own notes
- **Slay the Spire**: Persistent file-based memory improved performance **3× more** than for Opus 4.8; reached final act **3× more often**

### Life Sciences (Mythos 5)

| Capability | Result |
|-----------|--------|
| **Drug design** | Accelerated ~10×; matches/beats skilled human operators; 9/14 protein targets yielded strong candidates |
| **Novel hypotheses** | Scientists preferred Mythos hypotheses ~80% over Opus-class in blinded comparisons; one hypothesis independently corroborated |
| **Genomics research** | Week-long autonomous work; assembled single-cell data for millions of cells (138 species); model outperformed Science publication while being 100× smaller |

## Safety Architecture

### Safety Classifiers

Fable 5 introduces new classifiers — separate AI systems that detect potential misuse and route responses to Opus 4.8:

1. **Cybersecurity**: Covers exploitation and offensive cyber tasks broadly. External bug bounty (1,000+ hours) produced **zero universal jailbreaks**. External red-teaming also failed on long-form agentic tasks
2. **Biology and chemistry**: Extended beyond narrow bioweapons blocking. Mythos 5 outperformed dedicated protein language models on AAV shell assembly prediction (Dyno Therapeutics evaluation)
3. **Distillation**: Blocks large-scale capability extraction attempts (identified in authoritarian countries)

**>95% of Fable sessions involve no fallback at all** — for those sessions, performance is effectively identical to Mythos 5.

### Jailbreak Robustness

- External partner: Fable 5's cyber safeguards were the **most robust of any model tested** (including Opus 4.8 and 4.7)
- **Zero** harmful single-turn requests complied with across 30 different public jailbreak techniques
- UK AISI made progress towards a universal jailbreak within a brief initial testing window

### Data Retention Policy

New **30-day retention** for all traffic on Mythos-class models:
- Not used for model training or non-safety purposes
- All human access logged; deletion after 30 days
- Purpose: defend against novel attacks, identify and reduce false positives

### Alignment Assessment

- Level of misaligned behavior (deception, cooperation with misuse) was **low and similar to Opus 4.8**
- Same underlying model → Fable 5 alignment level similar

## Safeguards Philosophy

> "Without safeguards, Fable 5's capabilities in areas like cybersecurity could be misused to cause serious damage."

- Safeguards tuned **conservatively** — sometimes catch harmless requests, trigger on average in **<5% of sessions**
- Working to improve safeguards and reduce false positives as quickly as possible
- With more capable models arriving in coming months, prioritizing safeguard refinement

## Design Patterns

Lance Martin (@rlancemartin) articulated two core patterns for maximizing Fable 5's capabilities (see [[concepts/claude/designing-loops-with-fable-5]]):

1. **Self-Correction Loops**: Let the model iterate on environment feedback rather than direct prompting. Use `/goal` in Claude Code or Outcomes in Claude Managed Agents.
2. **Memory as Outer Loop**: Use memory to create cross-session learning. The optimal progression: Fail → Investigate → Verify → Distill → Consult.

Key finding: A **verifier sub-agent** outperforms self-critique because grading happens in an independent context window.

### Parameter Golf Benchmark (vs Opus 4.7)

| Model | Behavior | Result |
|-------|----------|--------|
| **Fable 5** | Bet on larger structural changes (architecture, quantization), showed resilience through regressions | ~6× more improvement than Opus 4.7 |
| **Opus 4.7** | First experiment produced a small win, then followed the same template: adjust scalar → measure → keep if positive | Incremental improvements only |

### Memory Progression (Continual Learning Bench 1.0)

| Model | Memory Progression | Verification Coverage |
|-------|-------------------|----------------------|
| **Sonnet 4.6** | Exits at step 1: stores failure notes and open guesses | Low |
| **Opus 4.7** | Exits at step 3: creates schema reference with uncertainty flagged | 7-33% (median ~17%) |
| **Fable 5** | Completes full progression: distills learnings into general rules | Up to 73% (22 of 30 questions) |

## Independent Review: Simon Willison

Simon Willison published detailed initial impressions after ~5.5 hours of testing Fable 5 on June 9, 2026.

Key observations:
- **The 'big model smell'**: Fable 5 feels notably larger in knowledge scope than Opus 4.8. When asked to list Simon Willison's open source projects, Opus 4.8 listed ~5 projects cautiously; Fable 5 produced a comprehensive list with dates, recognizing the typo 'Simon Willion' and covering files-to-prompt, datasette-extract, LLM, Datasette, sqlite-utils, Django, shot-scraper, and more.
- **Speed and cost tradeoff**: $10/MTok input, $50/MTok output — twice the price of Opus 4.5-4.8. The model is slower but handles everything thrown at it.
- **Context window**: 1 million tokens input, 128,000 maximum output tokens, January 2026 knowledge cutoff.
- **Safety classifiers**: New mechanisms for indicating when guardrails trigger, with automatic fallback option to another model.
- **Mythos 5 parallel launch**: Same model without safety classifiers, restricted to select researchers.

> "It's slow, expensive and has been quite happily churning through everything I've thrown at it so far. As is frequently the case with current frontier models the challenge is finding tasks that it can't do." — Simon Willison

## Controversy: Capability Limitation Debate

The release of Fable 5 sparked debate about the transparency and scope of safety-driven capability restrictions:

- **[[entities/elie-bakouch]]** (Prime Intellect) criticized that Mythos-class models will be "bad ON PURPOSE on ai 'frontier llm research' tasks" and that the hidden nature of these restrictions is "crazy" (3,800+ likes, 1.2M impressions)
- **Research community concerns**: The deliberate weakening of frontier models on research tasks creates an artificial ceiling for AI research
- **Transparency gap**: Users cannot tell whether poor performance on research tasks is due to model limitations or intentional restrictions

### System Card Evidence: Frontier LLM Development Restrictions

The [[raw/papers/2026-06-09_claude-fable5-mythos5-system-card|System Card]] confirms these restrictions are intentional and documents their implementation:

> "We've implemented new interventions that limit Claude's effectiveness for requests targeting frontier LLM development (for example, on building pretraining pipelines, distributed training infrastructure, or ML accelerator design). Using Claude to develop competing models already violates our Terms of Service, but enforcing this restriction through our safeguards avoids accelerating the actors most willing to violate these terms."

Critical details from the System Card:
- **Invisible safeguards**: Unlike cyber/bio/distillation classifiers (which fall back to Opus 4.8), these restrictions are NOT visible to users — no model switch, no error message
- **Mechanisms**: Prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT)
- **Estimated impact**: ~0.03% of traffic, concentrated in <0.1% of organizations
- **Rationale**: Preventing acceleration of AI development without commensurate safeguards — Anthropic's concern from their February 2026 Risk Report about "accelerating other AI developers in building powerful AI systems that pose similar risks"
- **User experience**: Claude still responds helpfully; effectiveness is silently limited only for frontier LLM development tasks

## Availability

### Subscription Rollout
- **June 9–22**: Included on Pro, Max, Team, seat-based Enterprise at no extra cost
- **June 23**: Removed from subscription plans; requires usage credits
- Goal: restore as standard subscription feature when capacity allows

### Trusted Access Programs
- **Cybersecurity**: Expanding Glasswing partners, pursuing systematic application process
- **Biology**: Opening program for select researchers — Fable 5 with biology/chemistry safeguards removed (cyber safeguards still in place)

## Early Customer Feedback

| Company | Person | Quote |
|---------|--------|-------|
| Cursor | Michael Truell, CEO | "State of the art on CursorBench. Opened up a class of long-horizon problems." |
| GitHub | Mario Rodriguez, CPO | "Complex, long-horizon coding tasks with autonomy and reliability exceeding previous benchmarks." |
| Cognition | Scott Wu, CEO | "Highest-scoring on FrontierBench. Excels at long-horizon reasoning." |
| Replit | Michele Catasta, President | "Highest-performing on ViBench — nearly saturating base use cases." |
| Hebbia | Izzy Miller, AI Research Lead | "First to break 90% on core analytics — 10-point jump over Opus." |
| Genesis Therapeutics | Sean Ward, CEO | "Works at senior research scientist grade." |
| Vercel | Fabian Hedin, CTO | "Apps that took a hundred prompts a year ago, it now one-shots." |
| Luminance | Aveek Duttagupta, MTS | "In blind review, redlines matched or beat current model every time." |
| Rakuten | Yusuke Kaji, GM | "At highest effort, reflects on and validates its own work." |
| Augment | Luke Anderson, CTO | "More capable engineering in fewer turns." |
| Replit | Michele Catasta | "Strongest model on frontier physics research while using 1/3 reasoning tokens." |

## Related

- [[entities/anthropic]] — The company behind Fable 5
- [[concepts/claude/mythos]] — The underlying Mythos architecture and Mythos 5
- [[concepts/claude/designing-loops-with-fable-5]] — Lance Martin's design patterns
- [[concepts/claude/mythos-glasswing]] — Mythos security capabilities
- [[concepts/project-glasswing]] — Trusted access program
- [[entities/rlancemartin]] — Author of Fable 5 design patterns
- [[entities/elie-bakouch]] — Critic of capability limitation transparency
- [[concepts/claude/opus-4-8]] — Fallback model for classifier-triggered queries
