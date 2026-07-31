---
title: "Separation of Duties"
type: concept
created: 2026-06-18
updated: 2026-07-31
tags:
  - architecture
  - agent-safety
related:
  - [[entities/aakash-gupta]]
  - [[concepts/security-and-governance/agent-separation-of-duties]]
sources:
  - https://x.com/aakashgupta/status/2067550891843186980
  - raw/articles/2026-06-18_agent-safety-separation-of-duties.md
---

# Separation of Duties

> **Canonical page moved.** The comprehensive treatment of this topic (worker/evaluator split, Codex `/goal` April 2026, Claude Code 2.1.139 May 2026, Aakash Gupta's 31-turn experiment) lives at [[concepts/security-and-governance/agent-separation-of-duties|Agent Separation of Duties]]. This page is retained as a short-form entry and redirect.

In the context of AI agents, **separation of duties** is an architectural design pattern that divides responsibilities among components so that the model executing a task (the worker) is structurally prevented from evaluating its own completion. A separate evaluator model reads the transcript and judges whether the stated condition was met — an accountability structure borrowed from accounting fraud-prevention practice.

## Key Concepts

- **Worker ≠ Evaluator**: The worker never gets a vote on its own completion; the evaluator answers one yes/no question against observable evidence.
- **Structural, not capability-based**: The safety property comes from architecture (no single agent has unchecked authority over a critical operation), not from model intelligence.
- **Independent convergence**: OpenAI (Codex `/goal`, April 2026) and Anthropic (Claude Code 2.1.139, May 2026) shipped the identical pattern within 30 days after both hit the same failure mode: an agent asked to verify its own work passes half-built stubs and calls them shipped.

## Sources

- [Agent Safety Separation Of Duties (X post)](https://x.com/aakashgupta/status/2067550891843186980)
- Full analysis: [[concepts/security-and-governance/agent-separation-of-duties]]
