---
source: https://www.antoinebuteau.com/automation-series-10-the-automation-architecture-worksheet/
title: "Automation Series #10: The Automation Architecture Worksheet"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, architecture-worksheet, staging, ownership]
---

# Automation Series #10: The Automation Architecture Worksheet

**Core Thesis:** The point of automation architecture is to make better decisions before the workflow is in production.

## 8-Step Worksheet
1. **Workflow Definition** — Name, outcome, trigger, out-of-scope
2. **Boundary Mapping** — Code vs Model vs Human per step
3. **Risk & Reversibility** — Score each action
4. **Narrow Model Jobs** — Strict contracts with schemas
5. **Decision Gates & State** — Idempotency, state machine
6. **Observability & Evaluation** — Gold sets, review cadence
7. **Security & Ownership** — Named owner, least privilege
8. **Launch Strategy** — Earn autonomy through stages

## Final Operator Checklist
Deterministic parts by code? AI steps bounded by schemas? Side effects idempotent? Confidence gates change behavior? Named human owner?
