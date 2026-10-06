---
title: Practitioner Permission Decisions in Agentic AI Assistants
created: 2026-10-06
updated: 2026-10-06
type: concept
tags: [human-in-the-loop, agent-safety, agent-observability, developer-tooling, ai-agents]
sources: [raw/articles/arxiv-2610.06047-practitioner-permission-decisions-agentic-assistants.md]
confidence: medium
related: [concepts/human-in-the-loop, concepts/overact-proactive-over-authorization, concepts/pace-provenance-aware-capability-enforcement]
---

# Practitioner Permission Decisions in Agentic AI Assistants

A sequential mixed-methods study (18 interviews → 115-practitioner survey) of how software
practitioners actually decide whether to grant an AI agent permission to modify files, run
commands, or reach external resources — and how they preserve autonomy benefits while doing so.

## What practitioners observe (and don't)

People understand agent behaviour through what they can **directly observe and review**.
Decisions, data use, and behind-the-scenes activity stay opaque. That uncertainty directly
shapes permission choices.

## What drives a permission decision

Grant/deny depends on: (1) the **scope and risk** of the action, (2) whether it **fits the
task**, (3) **familiarity** with the agent, and (4) the **environment**. Practitioners then
dial oversight — from setting limits in advance, to monitoring execution, to reviewing work
afterwards. How much scrutiny is applied hinges on trust, task importance, time pressure,
and the consequence of an action.

## Design implications (the paper's core contribution)

Permission systems should:
- make **consequential actions easier to review**;
- **separate what an agent is *allowed* to do from what the user *intended***;
- make **reversibility** clearer;
- **avoid treating repeated approvals as stable preferences** (a repeated "yes" is not consent);
- **distinguish rejecting one action from rejecting the entire approach**.

## Implication

This is the empirical, human-factors counterpart to the enforcement-mechanism literature.
Where [[concepts/pace-provenance-aware-capability-enforcement]] and
[[concepts/overact-proactive-over-authorization]] propose technical gates at the tool-call
boundary, this study documents that the human on the other side of the prompt is a noisy,
context-dependent approver whose fatigue and inference can't be assumed reliable — arguing
for permission UX grounded in observability and reversibility, see [[concepts/human-in-the-loop]].

## Related

- [[concepts/human-in-the-loop]] — the oversight model this study empirically grounds
- [[concepts/overact-proactive-over-authorization]] — the failures humans are asked to catch
- [[concepts/pace-provenance-aware-capability-enforcement]] — enforcement at the tool boundary
