---
title: "Ido Pesok"
created: 2026-06-08
updated: 2026-06-08
type: entity
tags:
  - person
  - infrastructure
  - verification
  - agentic-engineering
  - coding-agents
sources:
  - https://www.linkedin.com/pulse/verifying-agentic-development-scale-ido-pesok-meohc
  - https://spice.ai/blog/verifying-agentic-development-at-scale
description: "Co-founder of Spice AI, later joined Cognition to build end-to-end verification for Devin. Focused on real-time verification of AI-generated code at scale."
status: stub
---

# Ido Pesok

**Ido Pesok** is an AI infrastructure entrepreneur focused on **verification of agentic code generation**. He co-founded [[entities/spice-ai]], where he built a multi-layered verification system for AI-generated code, and later joined [[entities/cognition-ai]] to develop end-to-end testing capabilities in [[entities/devin]]'s virtual machine.

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

## Related

- [[entities/spice-ai]] — company he co-founded
- [[entities/cognition-ai]] — company he joined for Devin work
- [[entities/devin]] — the AI software engineer he helped verify
- [[concepts/agentic-engineering]] — the discipline his work exemplifies
- [[concepts/code-review-agents]] — adjacent concept
