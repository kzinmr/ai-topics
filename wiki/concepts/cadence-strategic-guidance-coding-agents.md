---
title: "Cadence: Health-Adaptive Intervention Scheduling for Coding Agents"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [coding-agents, agent-observability, agent-harness, ai-agents, verification]
sources: [raw/papers/2026-10-11_2610.12269_cadence-strategic-guidance-coding-agents.md]
confidence: high
related: [concepts/ontrack-streaming-trajectory-monitoring, concepts/process-supervision, concepts/instrumental-monitor-evasion, concepts/harness-engineering/agentic-engineering-guardrails-layer, concepts/architect-loop, concepts/agent-harness-primitives]
---

# Cadence: Health-Adaptive Intervention Scheduling

Runtime monitors improve coding-agent reliability by inspecting the execution trajectory and
injecting corrective guidance when misbehavior is detected. **Cadence's claim is that the open
question is not *what* guidance to give but *when to look*.**

## The two failure modes of static triggering

| Triggering scheme | Failure |
|---|---|
| Fixed inspection interval | misses timely guidance during severe misbehavior; pays unnecessary overhead during healthy execution |
| Rigid heuristic rules | fails to detect complex reasoning errors |

Both treat inspection frequency as a constant. Execution health is not constant.

## Architecture

Two coupled modules:

1. **Two-tier intervention module** — *advisory-level* guidance for normal executions and minor
   lapses; *replacement-level* guidance for severe misbehaviour (the monitor takes over the step
   rather than suggesting).
2. **Inspection scheduler** — driven by the intervention level just issued: **tightens** supervision
   after replacement-level guidance, **relaxes** it after advisory-level guidance.

The controller is a feedback loop over the monitor's own output: the severity of the last
intervention sets the cadence of the next inspection.

## Results

Evaluated on **300 SWE-bench Lite tasks** across two structurally different agents
(mini-swe-agent, Moatless):

- Highest resolve rate among all evaluated monitors.
- **+25.33% (+76 resolved tasks)** over vanilla on mini-swe-agent.
- **+15.67% (+47 resolved tasks)** over vanilla on Moatless.

That the gain replicates across two different harnesses is the load-bearing part — it suggests the
win comes from scheduling policy, not from tuning to one agent's prompt shape.

## Position in the supervision design space

[[concepts/process-supervision]] asks *what signal* to grade per step; [[concepts/ontrack-streaming-trajectory-monitoring]]
asks *how cheaply* to detect deviation per step. Cadence asks the orthogonal question: **at what
rate should the monitor run at all**. Three together decompose runtime oversight into signal,
detector cost, and sampling rate.

The tiering also matters for oversight economics: advisory guidance is nearly free to emit, while
replacement guidance is expensive but decisive. Spending supervision budget where the last signal
was severe is the same "redistribute a fixed budget rather than add data" logic that
[[concepts/signal-allocation-in-post-training]] applies to training gradients — moved from the
trainer into the harness at run time.

## Caveats

- The monitor is itself a model reading the trajectory, so it inherits
  [[concepts/instrumental-monitor-evasion]]: an agent that can see the guidance may learn to be
  un-monitorable rather than correct.
- Health assessment quality is not separately ablated here — the scheduler can only be as good as
  the severity classifier driving it.
- 300 tasks, two agents: the +25% figure is on SWE-bench Lite, subject to the usual
  [[concepts/evaluation/reward-hacking|benchmark-optimization]] pressure.

## Source

Minxing Wang, He Ye, Earl T. Barr, Yintong Huo, *Cadence: Strategic Guidance for Coding Agents*,
arXiv:2610.12269 (2026-10-08) —
`raw/papers/2026-10-11_2610.12269_cadence-strategic-guidance-coding-agents.md`
