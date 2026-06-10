---
title: "Anthropic — Claude Fable 5 and Claude Mythos 5"
date: 2026-06-09
date_ingested: 2026-06-10
source: https://www.anthropic.com/news/claude-fable-5-mythos-5
author: Anthropic
type: article
tags:
  - claude-fable-5
  - anthropic
  - frontier-models
  - ai-safety
  - model
  - benchmark
  - cybersecurity
  - alignment
  - announcement
related:
  - entities/claude-fable-5
  - entities/claude-mythos
  - entities/anthropic
  - concepts/claude-mythos-glasswing
  - concepts/project-glasswing
---

# Claude Fable 5 and Claude Mythos 5 — Anthropic Official Announcement

> **Source:** https://www.anthropic.com/news/claude-fable-5-mythos-5
> **Date:** June 9, 2026

## Summary

Anthropic launched two Mythos-class models simultaneously:

- **Claude Fable 5** — A Mythos-class model made safe for general use, with safety classifiers that fall back to Opus 4.8 on cybersecurity, biology/chemistry, and distillation-related queries
- **Claude Mythos 5** — The same underlying model with safeguards lifted, restricted to Project Glasswing cyber defenders and select biology researchers

**Pricing:** $10/MTok input, $50/MTok output — less than half the price of Claude Mythos Preview.

---

## Key Capabilities

### Software Engineering
- **Stripe**: Compressed months of engineering into days. Codebase-wide migration in a day on a 50-million-line Ruby codebase (would have taken a team 2+ months manually)
- **FrontierCode** (Cognition): Highest score among frontier models at medium effort — tests difficult coding tasks meeting production codebase standards
- **CursorBench**: State-of-the-art — "opened up a class of long-horizon problems that were out of reach for earlier models" (Michael Truell, Cursor CEO)
- **FrontierBench** (Cognition): Highest-scoring model — "excels at long-horizon reasoning and generalizes to unfamiliar tools out of the box" (Scott Wu, Cognition CEO)

### Knowledge Work
- **Hebbia Finance Benchmark**: Highest score of any model for senior-level reasoning; substantial gains in document-based reasoning, chart/table interpretation, problem solving
- **IMC**: Aced trading-analysis evaluations (factual lookup, conceptual reasoning, root-cause analysis, expected-value analysis)
- **Replit ViBench**: Highest-performing model — "nearly saturating our base use cases and building apps in less time with fewer tokens" (Michele Catasta)
- **Genspark**: First to break 90% on core analytics benchmark — 10-point jump over Opus

### Vision
- New state-of-the-art for vision tasks
- Extracts precise numbers from detailed scientific figures
- Rebuilds web app source code from screenshots alone
- **Pokémon FireRed**: Beat the game with a minimal, vision-only harness (previous Claude models needed complex helper harnesses)

### Memory and Long-Context
- Stays focused across millions of tokens in long-running tasks
- Improves outputs using its own notes
- **Slay the Spire**: Persistent file-based memory improved performance 3× more than for Opus 4.8; reached final act 3× more often

### Life Sciences (Mythos 5)
- **Drug design**: Internal protein design experts accelerated drug design ~10×. Mythos 5 with tools matches or beats skilled human operators on protein design tasks. 9 of 14 protein targets yielded strong candidates under investigation
- **Novel hypotheses**: First model to consistently produce novel, compelling scientific hypotheses. Scientists preferred Mythos hypotheses ~80% of the time over Opus-class models in blinded comparisons. One hypothesis (novel mechanism for E. coli protein) independently corroborated
- **Genomics research**: Conducted novel genomics research over a week of largely autonomous work. Assembled single-cell data for millions of cells spanning 138 animal species. Trained model outperformed a recent Science publication while being 100× smaller

---

## Safety Architecture

### Safety Classifiers
Fable 5 introduces new classifiers — separate AI systems that detect potential misuse and prevent the main model from responding. When classifiers detect requests related to:

1. **Cybersecurity**: Covers exploitation and offensive cyber tasks broadly. External bug bounty (1,000+ hours) produced no universal jailbreaks. External red-teaming organizations also failed to find universal jailbreaks on long-form agentic tasks
2. **Biology and chemistry**: Extended beyond narrow bioweapons blocking. Mythos 5 outperformed dedicated protein language models on AAV shell assembly prediction (Dyno Therapeutics evaluation)
3. **Distillation**: Blocks attempts to extract Claude's capabilities to train competing models (identified large-scale attempts in authoritarian countries)

When triggered, responses fall back to **Claude Opus 4.8** — users are informed when this occurs. **More than 95% of Fable sessions involve no fallback at all.**

### Jailbreak Robustness
- External partner found Fable 5's cyber safeguards were the most robust of any model tested (including Opus 4.8 and 4.7)
- Zero harmful single-turn requests complied with across 30 different public jailbreak techniques
- UK AISI made progress towards a universal jailbreak within a brief initial testing window

### Data Retention Policy
New 30-day retention requirement for all traffic on Mythos-class models (both first- and third-party surfaces):
- Not used for model training or non-safety purposes
- New privacy protections: all human access logged, deletion after 30 days in almost all cases
- Purpose: defend against complex/novel attacks, identify and reduce false positives

### Alignment Assessment
- Level of misaligned behavior (deception, cooperation with misuse) was low and similar to Opus 4.8
- Same underlying model, so Fable 5 alignment level similar

---

## Safeguards Philosophy

> "Without safeguards, Fable 5's capabilities in areas like cybersecurity could be misused to cause serious damage."

- Safeguards tuned **conservatively** — sometimes catch harmless requests, trigger on average in <5% of sessions
- Working to improve safeguards and reduce false positives as quickly as possible
- With more capable models arriving in coming months, prioritizing safeguard refinement

---

## Pricing and Availability

| | Fable 5 | Mythos 5 |
|---|---|---|
| **Access** | General availability | Glasswing partners + select biology researchers |
| **Input** | $10/MTok | $10/MTok |
| **Output** | $50/MTok | $50/MTok |
| **API** | claude-fable-5 | claude-mythos-5 |

### Subscription Rollout
- **June 9–22**: Included on Pro, Max, Team, seat-based Enterprise at no extra cost
- **June 23**: Removed from subscription plans; requires usage credits
- Goal: restore as standard subscription feature when capacity allows

### Trusted Access Programs
- **Cybersecurity**: Expanding Glasswing partners, pursuing systematic application process
- **Biology**: Opening program for select researchers — Fable 5 with biology/chemistry safeguards removed (cyber safeguards still in place)

---

## Naming

> "Fable is from the Latin *fabula*, 'that which is told,' akin to the Greek *mythos*. The safeguards are what distinguish the two models (Fable and Mythos) and are why we've given them different names."

---

## Early Customer Feedback

| Company | Person | Quote |
|---------|--------|-------|
| Cursor | Michael Truell, CEO | "State of the art on CursorBench. Opened up a class of long-horizon problems." |
| GitHub | Mario Rodriguez, CPO | "Took on complex, long-horizon coding tasks with autonomy and reliability exceeding previous benchmarks." |
| Cognition | Scott Wu, CEO | "Highest-scoring model on FrontierBench. Excels at long-horizon reasoning." |
| Replit | Michele Catasta, President | "Highest-performing on ViBench — nearly saturating base use cases." |
| Hebbia | Izzy Miller, AI Research Lead | "First to break 90% on core analytics benchmark — 10-point jump over Opus." |
| Genesis Therapeutics | Sean Ward, CEO | "Works at senior research scientist grade — picking directions, allocating resources, killing incorrect beliefs." |
| Vercel | Fabian Hedin, CTO | "Apps that took a hundred prompts a year ago, it now one-shots." |
| Luminance | Aveek Duttagupta, MTS | "In blind review, lawyers found its redlines matched or beat current model every time." |
| Rakuten | Yusuke Kaji, GM | "At highest effort, reflects on and validates its own work — makes highly autonomous operations possible." |
| Augment | Luke Anderson, CTO | "More capable engineering in fewer turns — handling complex multi-agent workflows." |

---

## Related

- [[entities/claude-fable-5]] — The general-access model
- [[entities/claude-mythos]] — The underlying Mythos architecture and Mythos 5
- [[entities/anthropic]] — The company
- [[concepts/project-glasswing]] — Trusted access program
- [[concepts/claude-mythos-glasswing]] — Mythos security capabilities
