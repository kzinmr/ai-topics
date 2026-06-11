---
title: Claude Mythos
type: entity
created: 2026-04-09
updated: 2026-06-11
tags:
  - model
  - agent-safety
  - emerging
  - security
aliases:
- Mythos
sources: ["raw/articles/2026-04-30-anthropic-claude-security-public-beta.md", "raw/articles/2026-06-09_anthropic_claude-fable-5-mythos-5.md", "raw/articles/2026-06-09_eliebakouch_fable-5-mythos-debated-research.md", "raw/papers/2026-06-09_claude-fable5-mythos5-system-card.md", "raw/articles/garymarcus.substack.com--p-the-revenge-of-claude-mythos--32970cd2.md", "raw/articles/simonwillison.net--2026-jun-11-anthropic-walks-back-policy--042d91ca.md"]
---

# Claude Mythos

Anthropic's next-generation model, developed after . Withheld from public release due to safety concerns regarding vulnerability exploitation capabilities.

## Overview

Claude Mythos represents a significant leap over Opus 4.6 in benchmark performance. However, Anthropic decided not to release it publicly after discovering its exceptional ability to find and exploit software vulnerabilities.

## Key Metrics

| Benchmark | Opus 4.6 | Mythos |
|-----------|----------|--------|
| Firefox exploit generation | 2 working exploits (hundreds of attempts) | **181 working exploits** |
| Firefox zero-day discovery (codebase scan) | — | **271 zero-day vulnerabilities** (~4× what Mozilla patched in all of 2025) |
| General benchmarks | Baseline | Massive improvements |

## Vulnerability Discovery

Mythos identified long-standing security bugs in critical software projects:
- **Firefox**: 271 zero-day vulnerabilities discovered in a single sweep (May 2026 data from Claude Security announcement)
- **OpenBSD**: 27-year-old bug discovered
- **FFmpeg**: 16-year-old bug discovered
- Multiple other critical projects affected

Mythos is now deployed via **Project Glasswing** for defensive security research and powers Anthropic's **Claude Security** product (Opus 4.7) for enterprise vulnerability scanning.

## Availability

Not publicly released. Limited preview access granted to 12 companies under [[concepts/project-glasswing]] for defensive security research.

## Safety Decision

Anthropic's decision to withhold Mythos reflects their AI safety-first approach. Rather than releasing a potentially dangerous model, they redirected its capabilities toward beneficial use: finding vulnerabilities in critical infrastructure software.

## Related Commentary

> "Mythos is to Opus what Opus is to Sonnet." — Theo (video analysis)

## Mythos Preview — General Intelligence Assistant (May 2026)

Announced alongside [[concepts/claude/opus-4-8|Claude Opus 4.8]] on May 28, 2026, Mythos Preview evolved from a security-focused model into a general-purpose AI assistant. General release expected "in coming weeks."

Key developments:
- **L4 Engineer Substitution**: In an internal Anthropic survey, **5 out of 18 engineers** believed that with harness improvements, Mythos could substitute for an **L4 engineer** — a mid-level programmer capable of handling involved projects without supervision
- **Recursive Self-Improvement Context**: Anthropic engineers reported "close to 100%" of Claude Code's code was written by the tool itself — Mythos represents the next step toward [[concepts/recursive-self-improvement|recursive self-improvement]]
- **Positioning**: Mythos now sits alongside [[concepts/claude/effort-control|Effort Control]] and [[concepts/dynamic-workflows|Dynamic Workflows]] as part of Anthropic's May 2026 agentic AI push

## UK AI Security Institute (AISI) Evaluation

On April 13, 2026, the UK's AI Security Institute published its evaluation of Claude Mythos Preview:

- **First model to complete an AISI cyber range end-to-end** — previous models could barely complete beginner-level cyber tasks in 2023
- **Assessment**: Mythos "could be directed to autonomously compromise small, weakly defended, and vulnerable systems if given network access"
- **Key caveat**: The model is not as dangerous as some media narratives suggested (e.g., claims about schoolchildren taking down power grids). In its current form, Mythos alone is not catastrophic
- **Recommendation**: Emphasizes cybersecurity fundamentals — regular updates, access controls, security configuration, and logging
- **Significance**: Confirms that even a restricted preview model arms attackers to a greater degree than predecessors, reinforcing Anthropic's decision to withhold public release

Gary Marcus evaluated the results as finding a middle ground: Mythos is "nowhere near as scary as some made it out to be" but "really does arm attackers to a greater degree than Mythos's predecessors."

> [!NOTE] Concern for agentic code: Marcus notes that agent-written code may itself be "weakly defended and vulnerable," compounding the risk when Mythos-level models are used to generate production code.

## Claude Fable 5 & Mythos 5 — Dual Launch (June 2026)

On June 9, 2026, Anthropic launched two Mythos-class models simultaneously:

- **[[concepts/claude/fable-5|Claude Fable 5]]**: Mythos-class model made safe for general use. Safety classifiers fall back to Opus 4.8 on cybersecurity, biology/chemistry, and distillation queries. **>95% of sessions involve no fallback.**
- **Claude Mythos 5**: Same underlying model with safeguards lifted. Restricted to [[concepts/project-glasswing|Project Glasswing]] cyber defenders and select biology researchers.

**Pricing:** $10/MTok input, $50/MTok output — less than half the price of Claude Mythos Preview.

### Mythos 5 — Life Sciences Capabilities

Mythos 5 demonstrated breakthrough capabilities in life sciences research:

| Capability | Result |
|-----------|--------|
| **Drug design** | Internal protein design experts accelerated drug design ~10×. Mythos 5 with tools matches or beats skilled human operators. 9/14 protein targets yielded strong candidates under investigation |
| **Novel hypotheses** | First model to consistently produce novel, compelling scientific hypotheses. Scientists preferred Mythos hypotheses ~80% over Opus-class in blinded comparisons. One hypothesis (novel E. coli protein mechanism) independently corroborated |
| **Genomics research** | Week-long largely autonomous work. Assembled single-cell data for millions of cells spanning 138 animal species. Custom ML model outperformed a recent *Science* publication while being 100× smaller |

### Trusted Access Programs
- **Cybersecurity**: Expanding Glasswing partners, pursuing systematic application process
- **Biology**: Opening program for select researchers — Fable 5 with biology/chemistry safeguards removed (cyber safeguards still in place)

### Safety Architecture (Fable 5)

Fable 5's classifiers detect and route to Opus 4.8 on:
1. **Cybersecurity**: External bug bounty (1,000+ hours) produced zero universal jailbreaks
2. **Biology/chemistry**: Extended beyond narrow bioweapons blocking
3. **Distillation**: Blocks large-scale capability extraction

External partner found Fable 5's cyber safeguards were the **most robust of any model tested** (including Opus 4.8 and 4.7).

### Capability Limitation Debate

The Fable 5 release sparked debate about the transparency and scope of safety-driven capability restrictions:

- **[[entities/elie-bakouch|Elie Bakouch]]** (Prime Intellect) criticized that Mythos-class models will be "bad ON PURPOSE on ai 'frontier llm research' tasks" and that the hidden nature of these restrictions is "crazy" (3,800+ likes, 1.2M impressions)
- **Core tension**: The restrictions extend beyond security-sensitive tasks (vulnerability discovery) into research-oriented capabilities, creating an artificial ceiling for AI research
- **Transparency gap**: Users cannot distinguish between "model can't do this" and "model is restricted from doing this" — the capability limitations are not surfaced in the user interface

This debate highlights the fundamental challenge of deploying safety-restricted frontier models: how to balance capability access for legitimate research use cases against the risks of unrestricted access to Mythos-class capabilities.

#### Frontier LLM Development Restrictions (System Card)

Per the [[raw/papers/2026-06-09_claude-fable5-mythos5-system-card|System Card]], Anthropic implemented invisible safeguards targeting frontier LLM development:

> "We've implemented new interventions that limit Claude's effectiveness for requests targeting frontier LLM development (for example, on building pretraining pipelines, distributed training infrastructure, or ML accelerator design). Using Claude to develop competing models already violates our Terms of Service, but enforcing this restriction through our safeguards avoids accelerating the actors most willing to violate these terms."

Key design choices:
- **Invisible to users**: Unlike cyber/bio/distillation classifiers, these safeguards do NOT trigger visible fallback to Opus 4.8
- **Mechanism**: Prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT)
- **Scope**: Estimated ~0.03% of traffic, <0.1% of organizations
- **Rationale**: Concern about "accelerating other AI developers in building powerful AI systems that pose similar risks [...] without necessarily having commensurate safeguards"
- **Behavioral impact**: Minimal except limiting frontier LLM development effectiveness; Claude still responds helpfully

### Policy Walkback (June 11, 2026)

On June 11, 2026, WIRED (Maxwell Zeff) reported that Anthropic agreed to walk back Fable 5's invisible frontier LLM development restrictions. An Anthropic spokesperson stated: "We're changing Fable 5's safeguards for frontier LLM development to make them visible. We made the wrong tradeoff and we apologize for not getting the balance right."

Simon Willison characterized the reversal as "very good news," noting that the policy had been "tucked away in their system card" and would have "sabotaged" AI researchers using Claude. The policy had been criticized by [[entities/elie-bakouch|Elie Bakouch]] (Prime Intellect) for restricting researchers without notification.

Sources: raw/articles/simonwillison.net--2026-jun-11-anthropic-walks-back-policy--042d91ca.md

## Critical Perspective

Gary Marcus argued (June 2026) that Anthropic's Mythos release follows a deliberate pattern he traces back to OpenAI's GPT-2 'too dangerous to release' strategy in 2019:

1. **Scare**: Anthropic held 'hushed meetings in Washington' about Mythos being 'too dangerous to release' (April 2026). Media amplified concerns — Axios reported officials believed Mythos could 'bring down a Fortune 100 company' or 'cripple swaths of the internet'
2. **Hype**: Anthropic's valuation leapt after the safety narrative generated media interest
3. **Release**: Two months later, with guardrails added, Mythos-class capabilities became available to anyone at the right price — coinciding with companies beginning to limit AI token budgets ('tokenmaxxing')

Marcus notes that several authors of the original 2019 GPT-2 safety post (including Dario Amodei, Daniele Amodei, and Jack Clark) went on to found Anthropic, and argues they have been 'running literally the same play for seven years.'

> "Anthropic once again played the media like a fiddle. And so many folks ate it all up." — Gary Marcus

## Sources
-  (Ben's Bites, 2026-04-09)
-  (scraped article)

## Related
- [[entities/anthropic]]
- [[concepts/claude/fable-5]] — Mythos-class model released for general use (June 2026)
- 
- [[concepts/project-glasswing]]
- [[concepts/ai-safety]]

## References

- 2026-04-13-claude-mythos-preview-red-team
