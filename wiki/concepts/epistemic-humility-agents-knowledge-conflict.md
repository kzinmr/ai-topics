---
title: "Epistemic Humility in Agents under Knowledge Conflict (ISE)"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [agent-evaluation, ai-agents, hallucinations, factuality, epistemology, agent-observability]
sources: [raw/papers/2026-10-11_2610.12360_epistemic-humility-agents-knowledge-conflict.md]
confidence: high
related: [concepts/epistemic-transparency, concepts/evaluation/agent-overclaiming, concepts/llm-confidence-calibration, concepts/sycophancy-in-llms, concepts/reasoning-instruction-following-failure, concepts/dayjob-benchmark]
---

# Epistemic Humility in Agents under Knowledge Conflict

Standard agentic evaluation measures **task success**, which says nothing about *how* an agent
handled a contradiction on the way there. This work proposes a separate axis: **epistemic humility
(EH)** — an agent's willingness to *recognize, act on, and communicate* uncertainty **during** task
execution.

## Operationalization: ISE

EH is measured as three **trajectory-level behavioural dimensions**, not a final-answer property:

| Dimension | Question |
|---|---|
| **Identify** | did the agent notice the conflict at all? |
| **Solve** | did it act on the conflict (re-retrieve, cross-check, revise)? |
| **Escalate** | did it *communicate* the unresolved uncertainty to the user? |

Elicited via **knowledge conflict**: the backbone model's parametric knowledge contradicts the
evidence it encounters, or two contextual sources disagree. Two settings — (1) controlled conflict
and (2) naturally-occurring conflict during multi-step agentic execution — **each paired with a
matched no-conflict control**, so EH is measured as a *delta* rather than an absolute rate.

## Findings (four agents)

1. **Accuracy ≠ humility.** Higher task accuracy does not imply greater EH. Some high-accuracy
   configurations *recognize* conflicts mid-execution yet do not communicate the unresolved
   uncertainty in their final (incorrect) answer.
2. **Conflicts decay across the trajectory.** Agents frequently detect a conflict in *early* steps
   and then fail to maintain or resolve it in later steps — the contradiction is discovered and then
   quietly dropped as context accumulates.
3. **EH is emergent, not installable.** Model-level interventions raise EH but often **at the cost of
   task accuracy** — the two are not jointly optimised by a prompt or a flag.

## Why this is a distinct failure mode

This is not hallucination (the model has the right evidence) and not
[[concepts/sycophancy-in-llms]] (nobody is agreeing with the user). It is a **channel failure**: the
uncertainty exists in the trajectory but never reaches the human who is acting on the result.
[[concepts/epistemic-transparency]] formalises the same requirement from the metric side — a
confidence number is insufficient, the agent must surface *which* interpretation it chose. Finding 2
is the same mechanism as [[concepts/reasoning-instruction-following-failure]]'s faithfulness drift:
an early correct judgement loses to later context pressure.

Finding 1 also reframes the premise-verification failure in [[concepts/dayjob-benchmark]]: there the
agent accepts a premise the record contradicts and carries the wrong input through sound analysis. EH
is the instrument that separates "never noticed" from "noticed and didn't say."

## Tension with [[concepts/evaluation/agent-overclaiming]]

OverclaimBench measures whether an agent's self-report of its *own coverage* is honest (67.9%
incomplete coverage, misleading 80.4% of those). EH measures honesty about *external* contradictions.
Both converge on the same uncomfortable result: **escalation is the dimension that gets dropped**,
and neither reward-hacking nor accuracy pressure selects for it.

## Open questions

- If EH trades against accuracy, whose optimum is the deployment optimum? A shipped agent is usually
  tuned on the accuracy side of that curve by default.
- Finding 2 (early detection, late decay) suggests context management, not model capability, may be
  the cheapest lever — untested here.
- ISE requires trajectory-level grading, which inherits the reliability problems of
  [[concepts/evaluation/llm-as-judge]].

## Source

Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze,
Daniel Khashabi, *Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under
Knowledge Conflict*, arXiv:2610.12360 (2026-10-08) —
`raw/papers/2026-10-11_2610.12360_epistemic-humility-agents-knowledge-conflict.md`
