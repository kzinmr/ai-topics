---
title: "Ido Pesok"
created: 2026-06-08
updated: 2026-06-09
type: entity
tags:
  - person
  - infrastructure
  - verification
  - agentic-engineering
  - coding-agents
  - ai-agents
aliases:
  - ido-pesok
sources:
  - https://www.linkedin.com/pulse/verifying-agentic-development-scale-ido-pesok-meohc
  - https://spice.ai/blog/verifying-agentic-development-at-scale
  - raw/articles/2026-06-08_linkedin-ido-pesok_verifying-agentic-development-at-scale.md
description: "AI infrastructure engineer focused on real-time verification of agentic code generation. Built multi-layered verification stack at Spice AI, later joined Cognition to build Devin's autonomous verification system."
---

# Ido Pesok

**Ido Pesok** is an AI infrastructure engineer focused on **verification of agentic code generation**. He led the development of a multi-layered verification system for AI-generated code at [[entities/spice-ai]], and later joined [[entities/cognition-ai]] to build end-to-end testing capabilities in [[entities/devin]]'s virtual machine.

## Background

Pesok's work sits at the intersection of three converging trends: the explosion of AI-generated code volume, the inadequacy of traditional CI/CD pipelines for real-time verification, and the need for self-correcting agents. His core thesis — that verification, not generation, is the bottleneck in agentic development — has become a defining principle in the [[concepts/agentic-engineering]] discipline.

## Key Contributions

### Spice AI — Real-Time Verification Stack

At Spice AI, Pesok designed a three-layer verification system for agentic code:

1. **Syntax/type checking** — immediate compilation of generated code
2. **Semantic verification** — LLM-based intent matching (API correctness, data flows, pattern adherence)
3. **Architectural compliance** — enforcement of dependency policies, service boundaries, and approved patterns

Core insight: verification must happen **during generation, not after**, enabling agents to self-correct in real time. The system reported 94% catch rate with <3% false positives.

### Cognition / Devin — Cloud Agent Verification

After joining Cognition, Pesok focused on Devin's autonomous verification capabilities:

- End-to-end testing in cloud virtual machines
- Computer use (screenshots, mouse, keyboard) for validating UI integrations
- `devin review` — code review that closes the loop by fixing findings until the diff is clean
- Scaling verification for async-triggered agents (events, automations, schedules)

## Philosophy

> "The core challenge isn't generation. It's verification."

Pesok's work spans the transition from ad-hoc "vibe coding" to systematic [[concepts/agentic-engineering]], where the engineer's role shifts from writing code to **designing verification systems**.

## Graph Structure Query

```
[ido-pesok] ──author──→ [entity: spice-ai]  (verification system)
[ido-pesok] ──author──→ [entity: cognition-ai]  (Devin verification)
[ido-pesok] ──teaches──→ [concept: agentic-engineering]  (verification thesis)
[ido-pesok] ──contrasts──→ [concept: vibe-coding]  (systematic vs ad-hoc)
```

## Related

- [[entities/spice-ai]] — built verification system at this company
- [[entities/cognition-ai]] — company he joined for Devin work
- [[entities/devin]] — the AI software engineer he helped verify
- [[concepts/agentic-engineering]] — the discipline his work exemplifies
- [[concepts/coding-agents/code-review-agents]] — adjacent concept
- [[concepts/vibe-coding]] — contrast paradigm
