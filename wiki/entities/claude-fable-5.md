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
aliases:
  - Fable 5
  - Claude Fable
status: draft
description: "Anthropic's Mythos-class model released for general use in June 2026. Derived from the Claude Mythos architecture with safety-driven capability restrictions."
sources:
  - raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md
  - raw/articles/2026-06-09_eliebakouch_fable-5-mythos-debated-research.md
  - https://x.com/claudeai/status/2064394146916229443
---

# Claude Fable 5

Anthropic's Mythos-class model released for general use on June 9, 2026. Derived from the [[entities/claude-mythos|Claude Mythos]] architecture with safety-driven capability restrictions.

## Overview

Claude Fable 5 was announced by [@claudeai](https://x.com/claudeai) as "a Mythos-class model that we've made safe for general use" with capabilities that "exceed those of any model we've ever made generally available." It represents the public release of Mythos-class capabilities, which Anthropic had previously restricted due to safety concerns (particularly vulnerability discovery capabilities).

Fable 5 sits at the intersection of Anthropic's safety-first deployment philosophy and the research community's desire for access to frontier capabilities.

## Key Characteristics

### Mythos-Class Architecture
Fable 5 is derived from the Mythos architecture, which demonstrated exceptional capabilities:
- 181 working Firefox exploit generations
- 271 zero-day vulnerabilities discovered in a single sweep
- Discovery of 27-year-old OpenBSD bug and 16-year-old FFmpeg bug

### Safety Restrictions
As a "safe for general use" model, Fable 5 includes deliberate capability restrictions:
- **Research task limitations**: Deliberately weakened on "frontier LLM research" tasks (per [[entities/elie-bakouch]]'s critique)
- **Hidden restrictions**: Capability limitations are not visible to end users
- **Security-sensitive tasks**: Reduced vulnerability discovery capabilities compared to raw Mythos

### Performance Characteristics

#### Parameter Golf Benchmark (vs Opus 4.7)
| Model | Behavior | Result |
|-------|----------|--------|
| **Fable 5** | Bet on larger structural changes (architecture, quantization), showed resilience through regressions | ~6x more improvement than Opus 4.7 |
| **Opus 4.7** | First experiment produced a small win, then followed the same template: adjust scalar → measure → keep if positive | Incremental improvements only |

#### Memory Progression (Continual Learning Bench 1.0)
| Model | Memory Progression | Verification Coverage |
|-------|-------------------|----------------------|
| **Sonnet 4.6** | Exits at step 1: stores failure notes and open guesses, rarely consults prior notes | Low |
| **Opus 4.7** | Exits at step 3: creates schema reference with uncertainty flagged | 7-33% (median ~17%) |
| **Fable 5** | Completes full progression: distills learnings into general rules | Up to 73% (22 of 30 questions) |

## Design Patterns

Lance Martin (@rlancemartin) articulated two core patterns for maximizing Fable 5's capabilities (see [[concepts/designing-loops-with-fable-5]]):

1. **Self-Correction Loops**: Let the model iterate on environment feedback rather than direct prompting. Use `/goal` in Claude Code or Outcomes in Claude Managed Agents.
2. **Memory as Outer Loop**: Use memory to create cross-session learning. The optimal progression: Fail → Investigate → Verify → Distill → Consult.

Key finding: A **verifier sub-agent** outperforms self-critique because grading happens in an independent context window.

## Controversy: Capability Limitation Debate

The release of Fable 5 sparked debate about the transparency and scope of safety-driven capability restrictions:

- **[[entities/elie-bakouch]]** (Prime Intellect) criticized that Mythos-class models will be "bad ON PURPOSE on ai 'frontier llm research' tasks" and that the hidden nature of these restrictions is "crazy" (3,800+ likes, 1.2M impressions)
- **Research community concerns**: The deliberate weakening of frontier models on research tasks creates an artificial ceiling for AI research
- **Transparency gap**: Users cannot tell whether poor performance on research tasks is due to model limitations or intentional restrictions

## Availability

Released June 9, 2026 for general use. The announcement received significant engagement: 80,000+ likes, 15,500+ bookmarks, 21.4M impressions on the @claudeai announcement tweet.

## Related

- [[entities/anthropic]] — The company behind Fable 5
- [[entities/claude-mythos]] — The underlying Mythos architecture
- [[concepts/designing-loops-with-fable-5]] — Lance Martin's design patterns
- [[concepts/claude-mythos-glasswing]] — Mythos security capabilities
- [[entities/rlancemartin]] — Author of Fable 5 design patterns
- [[entities/elie-bakouch]] — Critic of capability limitation transparency
- [[concepts/claude-opus-4-8]] — Announced alongside Mythos Preview (May 2026)
