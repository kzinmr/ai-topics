---
title: Claude Mythos
type: entity
created: 2026-04-09
updated: 2026-06-01
tags:
  - model
  - agent-safety
  - emerging
  - security
aliases:
- Mythos
sources: ["raw/articles/2026-04-30-anthropic-claude-security-public-beta.md"]
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

Announced alongside [[concepts/claude-opus-4-8|Claude Opus 4.8]] on May 28, 2026, Mythos Preview evolved from a security-focused model into a general-purpose AI assistant. General release expected "in coming weeks."

Key developments:
- **L4 Engineer Substitution**: In an internal Anthropic survey, **5 out of 18 engineers** believed that with harness improvements, Mythos could substitute for an **L4 engineer** — a mid-level programmer capable of handling involved projects without supervision
- **Recursive Self-Improvement Context**: Anthropic engineers reported "close to 100%" of Claude Code's code was written by the tool itself — Mythos represents the next step toward [[concepts/recursive-self-improvement|recursive self-improvement]]
- **Positioning**: Mythos now sits alongside [[concepts/effort-control|Effort Control]] and [[concepts/dynamic-workflows|Dynamic Workflows]] as part of Anthropic's May 2026 agentic AI push

## UK AI Security Institute (AISI) Evaluation

On April 13, 2026, the UK's AI Security Institute published its evaluation of Claude Mythos Preview:

- **First model to complete an AISI cyber range end-to-end** — previous models could barely complete beginner-level cyber tasks in 2023
- **Assessment**: Mythos "could be directed to autonomously compromise small, weakly defended, and vulnerable systems if given network access"
- **Key caveat**: The model is not as dangerous as some media narratives suggested (e.g., claims about schoolchildren taking down power grids). In its current form, Mythos alone is not catastrophic
- **Recommendation**: Emphasizes cybersecurity fundamentals — regular updates, access controls, security configuration, and logging
- **Significance**: Confirms that even a restricted preview model arms attackers to a greater degree than predecessors, reinforcing Anthropic's decision to withhold public release

Gary Marcus evaluated the results as finding a middle ground: Mythos is "nowhere near as scary as some made it out to be" but "really does arm attackers to a greater degree than Mythos's predecessors."

> [!NOTE] Concern for agentic code: Marcus notes that agent-written code may itself be "weakly defended and vulnerable," compounding the risk when Mythos-level models are used to generate production code.

## Sources
-  (Ben's Bites, 2026-04-09)
-  (scraped article)

## Related
- [[entities/anthropic]]
- 
- [[concepts/project-glasswing]]
- [[concepts/ai-safety]]

## References

- 2026-04-13-claude-mythos-preview-red-team
