---
title: "OnTrack: Streaming Structure-Aware Optimal Transport for Agent Trajectory Monitoring"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [agent-observability, ai-agents, agent-safety, token-economics, verification]
sources: [raw/papers/2026-10-11_2610.12375_ontrack-streaming-trajectory-monitoring.md]
confidence: medium
related: [concepts/cadence-strategic-guidance-coding-agents, concepts/process-supervision, concepts/token-economics, concepts/instrumental-monitor-evasion, concepts/human-in-the-loop, concepts/undobench-agent-recovery-capability]
---

# OnTrack: Streaming Structure-Aware Trajectory Monitoring

Agents are deployed in domains with **irreversible actions** — trip planning, stock trading, IT
incident triage — and are usually run autonomously with minimal rule-based safeguarding. The two
existing answers each fail structurally:

| Approach | Failure |
|---|---|
| Safeguard agent monitoring every step | adds cost + latency to **every** step |
| Post-hoc log evaluation | verdict arrives **after** the run, when tokens are burned and damage is done |

**OnTrack** is a streaming monitor that compares an agent's steps *and dependency structure* against
recorded successful runs, alerting or blocking in **~1 millisecond per step**.

## Method: structure-aware optimal transport

The comparison is not content similarity over step text. It is **optimal transport over the
trajectory's structure** — the steps and the dependencies between them — so a run that visits the
right actions in a wrong causal order is distinguishable from one that merely phrases things
differently. Streaming formulation means the distance is computed incrementally as steps arrive,
which is what makes the per-step cost millisecond-scale rather than a post-run batch job.

## Three access regimes

Detection capability degrades monotonically with data access — an explicit ablation rather than an
assumption:

1. **Full reference access** — historical runs *and* tool schemas.
2. **Intermediate access** — tool schemas only.
3. **No prior knowledge** — only step logs as they are generated.

Capability slides from *plan-violation detection* (regime 1) down to *loop, stall, and repeated-tool-call
detection* (regime 3). Practically: the valuable supervision is bought with recorded successful runs,
and an organisation that has never logged clean runs only gets the cheap failure signatures.

## Results

Evaluated on **SWE-bench trajectories**, judging from the **first 8 steps only**:

- Ranks failing trajectories below succeeding ones better than content-similarity approaches
  (**+0.057 AUROC**).
- With an abort policy: **~18% of compute saved** that would have been burned on failing runs.
- **83% of interrupted runs were actually heading to failure** — 5 of 6 aborts correct.

## Why early abort is the interesting result

An 8-step horizon on a task that may run for hundreds of steps is the only regime where aborting
recovers meaningful budget. This makes the metric that matters not accuracy but **precision at a
very early cut-off**, because a false abort destroys a run that would have succeeded — the asymmetric
cost [[concepts/undobench-agent-recovery-capability]] measures from the other side (naive retry
duplicates external effects in 53.33% of trials).

## Caveats

- 8-step / SWE-bench only; generalisation to long-horizon non-coding agents is asserted by the
  motivation, not measured. Confidence set to `medium` for that reason.
- Aborting is itself an irreversible action with an unrecoverable cost when wrong; the 5-of-6 figure
  is a small denominator.
- Reference-run dependence creates a drift problem: once the model or harness changes, "successful
  runs" from the previous version may mis-shape the transport cost.

## Source

Babak Barazandeh, Connor Swanson, Chinmay Kulkarni, Nikhil Mungel, *OnTrack: Real-Time Monitoring
and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport*,
arXiv:2610.12375 (2026-10-08) —
`raw/papers/2026-10-11_2610.12375_ontrack-streaming-trajectory-monitoring.md`
