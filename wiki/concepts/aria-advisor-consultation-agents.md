---
title: "ARIA — Learning When to Consult a Stronger Advisor Model"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [model-routing, token-economics, ai-agents, ai-agent-engineering, cost-optimization]
sources: [raw/papers/2026-10-09_2610.13870_aria-advisor-consultation-agents.md]
confidence: high
related: [concepts/model-routing, concepts/token-economics, concepts/epistemic-humility-agents-knowledge-conflict]
---

# ARIA — Learning When to Consult a Stronger Advisor Model

Executor–advisor (a.k.a. small-model-executes / big-model-advises) workflows trade task success
against compute cost by having a cheap model run the task and selectively escalate to a stronger
model. The classic failure: escalation is triggered by the executor's **self-assessment**, and
current LLMs are poor at detecting where their own reasoning breaks. Sowietzki et al.
(arXiv:2610.13870, Oct 2026) introduce **ARIA**, a meta-controller that learns *when* to consult
rather than trusting the executor to know.

## Method

Consultation is formulated as a **sequential resource-allocation problem**, not a per-step
confidence threshold:

- At "workflow contact points," ARIA maps execution evidence to a compact state abstraction.
- It picks one of two actions: `SILENT` (continue alone) or `CONSULT` (pay to consult the
  advisor).
- Action values are learned by **Monte Carlo control from cost-penalized outcomes** — the
  reward is task success minus a consultation price.
- A single **consultation-price parameter** governs the entire success–cost trade-off, so tuning
  cost vs. quality does **not require retraining** either underlying model.

## Results

Across SWE-bench Verified, Terminal-Bench 2.1, and $\tau^2$-bench, ARIA:

- recovers **44–81% of the executor–advisor success gap at less than half the advisor model's
  cost**;
- achieves the **best observed success–cost trade-off** among ten other conditions, including
  routing and cascading methods, fixed and prompted consultation, and random placement at
  matched advice volume;
- yields compact, inspectable policies.

## Why it matters

Model cascades and routers (see [[concepts/model-routing]], [[concepts/token-economics]]) usually
decide *which model answers a query up front*. ARIA's contribution is deciding *mid-trajectory,
where to interrupt a running agent* — the need for stronger reasoning "emerges during execution
and varies across workflow phases." That makes it a sibling of the escalation literature rather
than a routing trick: like [[concepts/epistemic-humility-agents-knowledge-conflict]], it treats
"knowing when to ask for help" as the scarce skill, but replaces unreliable self-assessment with
a learned controller priced against real cost.

## Related

- [[concepts/model-routing]]
- [[concepts/token-economics]]
- [[concepts/epistemic-humility-agents-knowledge-conflict]]
- [[concepts/test-time-compute]]
