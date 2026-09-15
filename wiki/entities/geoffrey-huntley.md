---
title: "Geoffrey Huntley — The Anti-Hype Field Critic of Agent Engineering"
type: entity
created: 2026-09-15
updated: 2026-09-15
confidence: medium
tags:
  - person
  - blogger
  - ai-commentary
  - coding-agents
  - ai-agents
  - ai-skeptic
  - developer
aliases: ["gnubian", "ghuntley", "Geoffrey Huntley"]
sources:
  - raw/articles/2026-09-15_ghuntley_can-we-have-it-both.md
  - raw/articles/2026-09-14_ghuntley_a-featureless-world.md
related:
  - agent-slop
  - harness-engineering
  - ai-engineer-worlds-fair-2026
  - proxies-for-expertise
  - openclaw
---

# Geoffrey Huntley

Geoffrey Huntley (online handle **gnubian**) is an Australian software engineer and polemicist — founder of the gnub AI agent stack, former CTO, and self-described "extreme expert of the impossible" — who has become one of the most aggressive *internal* critics of the agentic-coding boom: he builds coding agents for a living and attacks the field's evidentiary standards from inside. His blog (ghuntley.com) mixes vulgarity, field reports from shipping agents, and occasionally rigorous critique that the more polite commentators avoid.

X: **@gnusoc** (also cross-posts at @gnubai). Substack: ghuntley.substack.com.

## Core Theses

### 1. The Real Coding Agent Is a Graph of Interacting Feedback Loops
Title of his **AI Engineer World's Fair SF talk** (see [[concepts/ai-engineer-worlds-fair-2026]]). The claim: what actually ships as a "coding agent" is not the model and not the prompt but a **directed graph of feedback loops** — compile errors, test runs, linters, human rejections — whose topology, not the model's raw capability, determines outcomes. Agents that can't *self-edit* their environment/context have "no agency at all."

### 2. The Featureless World
His AI Engineer talk/essay "**A Featureless World**" (2026): frontier labs are absorbing the outer harness — browser automation, memory, sandboxing, sub-agents — into the model and its official scaffold, so most third-party agent tooling is becoming **undifferentiated plumbing**. His sharpest exhibit: **OpenClaw** shipping "hundreds of thousands of lines of TypeScript" as a "giant pile of tech debt that no human being can read," which he calls *the biggest failure mode in agent engineering* — complexity that neither humans nor the agents using it can audit. ^[raw/articles/2026-09-14_ghuntley_a-featureless-world.md]

### 3. "Can We Have It Both Ways?" (Sep 2026)
His critique of the GPT-6 Astra / open-weight moment: labs want the **open-source PR benefit and proprietary pricing simultaneously** — ship open weights at the low end (Luna) while framing the closed flagship (Astra) as the "big" model, on top of a benchmark index that "can be gamed by a small nudge." The essay's famous line targets the field's evidentiary loop: **"we cite each other's talks at AI Engineer conferences as evidence enough."** Full argument filed at [[concepts/agent-slop]] and [[concepts/proxies-for-expertise]]. ^[raw/articles/2026-09-15_ghuntley_can-we-have-it-both.md]

### 4. The Test-Improve Loop
His standing prescription for agent teams, repeated across posts and talks: an unglamorous **test → measure → improve loop with adversarial, real-work evaluation at every step** — the opposite of demo-driven development. He claims most teams skip it because it makes demos worse in the short term.

## Reception & Style Notes

- Huntley is a **polarizing figure**: devoted readers value him precisely because he has shipping agents and no VC-funded incentive to soften claims; critics find the profanity-laden style ("go fuck yourself energy") drowns signal, and some of his quantitative claims are single-run anecdotes rather than benchmarks.
- Treat his capability claims as `confidence: medium` hypotheses worth testing, not measurements — an instance of his own point about evidence.
- He sits adjacent to but distinct from academic skeptics: his attacks come from a practitioner **selling agent infrastructure**, closer in function to a trade-insider whistleblower.

## Related

- [[concepts/agent-slop]] — synthesis of his reliability-gap critique
- [[concepts/harness-engineering]] — the layer his feedback-loop and featureless-world theses analyze
- [[concepts/ai-engineer-worlds-fair-2026]] — where two of his signature talks were given
- [[concepts/proxies-for-expertise]] — the conference-citation loop he attacks

## Sources

- Huntley, Geoffrey. ["Can we have it both ways?"](https://ghuntley.com) — Sep 2026. Raw: `raw/articles/2026-09-15_ghuntley_can-we-have-it-both.md`
- Huntley, Geoffrey. ["A Featureless World"](https://ghuntley.com) — Sep 2026. Raw: `raw/articles/2026-09-14_ghuntley_a-featureless-world.md`
