---
source: https://www.antoinebuteau.com/automation-series-9-failure-modes-security-and-blast-radius/
title: "Automation Series #9: Failure Modes, Security, and Blast Radius"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, failure-modes, blast-radius, security, least-privilege]
---

# Automation Series #9: Failure Modes, Security, and Blast Radius

**Core Thesis:** The useful question is not how to prevent every failure, but how much damage a failure can do, how quickly you can detect it, and how cleanly you can recover.

## Failure Taxonomy (10 types)
Misclassification, Bad Extraction, Hallucinated Draft, Duplicate Side Effect, Unauthorized Action, Prompt Injection, Data Exfiltration, Irreversible Write, Silent Queue Backlog, Policy/Model Drift, API Change.

## Principle of Least Privilege
Automation should operate with absolute minimum permissions. Read only what's needed; separate drafting from sending; use scoped tokens.

## Launch Strategy: Stages of Autonomy
1. Shadow Mode (AI recommends, humans act)
2. Draft Mode (AI creates, humans send)
3. Assisted Mode (AI acts on low-risk, humans review rest)
4. Full Automation (low-risk, reversible, well-observed work only)

**The Operator's Rule:** "Build automation with failure containment from the start."
