---
source: https://www.antoinebuteau.com/automation-series-4-the-automation-boundary-code-vs-model-vs-human/
title: "Automation Series #4: The Automation Boundary: Code vs Model vs Human"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, boundary-design, risk-reversibility, code-vs-model-vs-human]
---

# Automation Series #4: The Automation Boundary

**Core Thesis:** Without an intentional boundary map, responsibilities are assigned "by accident."

## The Boundary Map
- **Code owns exactness:** Required fields, permission checks, policy thresholds, idempotency, retries.
- **Models own ambiguity:** Classification, extraction, sentiment — with fixed contracts and output schemas.
- **Humans own accountability:** Low-confidence outputs, irreversible actions, sensitive communications.

## Decision Framework: Risk and Reversibility
Score actions by impact and reversibility. Low risk + easy reversal = auto with logs. High risk + hard reversal = human owns decision.

**The Operator's Rule:** "If you cannot say which decisions belong to code, model, and human, you are not designing automation. You are distributing risk randomly."
