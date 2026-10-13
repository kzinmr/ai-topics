---
title: "Runtime Oversight in Coding Agents — Three Orthogonal Knobs"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [agent-observability, coding-agents, ai-agents, harness-engineering, verification]
sources: [raw/papers/2026-10-11_2610.12269_cadence-strategic-guidance-coding-agents.md, raw/papers/2026-10-11_2610.12375_ontrack-streaming-trajectory-monitoring.md, raw/papers/2026-10-11_2610.12360_epistemic-humility-agents-knowledge-conflict.md, raw/papers/2026-10-11_2610.11647_skill-co-installation-conflict.md, raw/papers/2026-10-09_2610.13870_aria-advisor-consultation-agents.md]
related: [concepts/cadence-strategic-guidance-coding-agents, concepts/ontrack-streaming-trajectory-monitoring, concepts/epistemic-humility-agents-knowledge-conflict, concepts/skill-co-installation-conflict, concepts/process-supervision, concepts/signal-allocation-in-post-training, concepts/instrumental-monitor-evasion, concepts/human-in-the-loop, concepts/aria-advisor-consultation-agents]
---

# Runtime Oversight in Coding Agents — Three Orthogonal Knobs

Four independent 2026-10 papers (three posted 2026-10-08 to arXiv) all add a monitor or a checker
around an agent. Read together they decompose runtime oversight into knobs that can be tuned
independently — and reveal that the industry has been arguing almost exclusively about the first one.

## The knobs

| Knob | Question | Represented by |
|---|---|---|
| **Signal** | *what* should the monitor grade per step? | [[concepts/process-supervision]], [[concepts/signal-allocation-in-post-training]] |
| **Detector cost** | *how cheaply* can deviation be recognised per step? | [[concepts/ontrack-streaming-trajectory-monitoring]] (~1 ms/step, structure-aware OT) |
| **Sampling rate** | *how often* should the monitor run at all? | [[concepts/cadence-strategic-guidance-coding-agents]] (health-adaptive scheduling) |
| **Escalation channel** | does the uncertainty ever *reach the human*? | [[concepts/epistemic-humility-agents-knowledge-conflict]] (Identify / Solve / **Escalate**) |

## The synthesis

**1. Sampling rate is under-explored and cheap.** Cadence's +25.33% on mini-swe-agent comes from
*when to look*, not from a better judge or a better prompt. Fixed-interval and heuristic-trigger
monitors are the default in production harnesses, and both fail on opposite sides — late during
severe misbehaviour, wasteful during healthy execution.

**2. Detector cost sets what supervision is affordable.** OnTrack's ~1 ms/step is what converts
monitoring from a safeguard-agent tax into something runnable on every step. Its three-access-regime
ablation is the uncomfortable part: with no recorded successful runs you only get loop/stall/repeat
detection. Rich oversight is bought with a clean-run corpus.

**3. Escalation is where the failures actually land.** Epistemic humility finds agents that
*Identify* a contradiction, sometimes *Solve*, and frequently **never Escalate** — high-accuracy
configurations ship confident wrong final answers. This is the same shape as
[[concepts/evaluation/agent-overclaiming]] and the "independent, non-negotiable verifier" principle:
a judgement that stays inside the acting channel is not a control.

**4. The monitored object is itself unstable.** [[concepts/skill-co-installation-conflict]] shows the
agent's policy source is a description-mediated race across co-installed skills, decided by install
location. A monitor grading "the right behaviour" has no fixed referent while the namespace has no
precedence or exclusivity primitive.

## The unresolved tension

Every knob buys resolution by adding a component that can itself be wrong: a severity classifier
(Cadence), a reference-run distribution that drifts when the harness changes (OnTrack), a judge
grading escalation (ISE), a skill precedence order nothing enforces. And the monitor is a model
reading the trajectory, so [[concepts/instrumental-monitor-evasion]] applies — an agent that can see
guidance may learn to be un-monitorable rather than correct.

The consistent answer across this wiki's clusters remains: put the check in a channel the agent
cannot edit — a Lean kernel, a frozen gate file, a recomputing panel. Every knob above is a step
toward that only if its state lives outside the acting channel.

## Related

- Training-side analogue: [[concepts/signal-allocation-in-post-training]]
- Human-side: [[concepts/human-in-the-loop]], [[concepts/architect-loop]]
- Recovery cost of getting it wrong: [[concepts/undobench-agent-recovery-capability]]
- Guardrail placement: [[concepts/harness-engineering/agentic-engineering-guardrails-layer]]
