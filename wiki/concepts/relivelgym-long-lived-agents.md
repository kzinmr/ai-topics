---
title: "ReLiveGym — Evaluating Long-Lived Agents over Weeks of Replayed Reality"
created: 2026-10-04
updated: 2026-10-04
type: concept
tags:
  - agent-evaluation
  - long-horizon
  - benchmark
  - ambient-agents
  - harness-engineering
  - agent-memory
aliases:
  - ReLiveGym
  - long-lived agents benchmark
  - action timing
sources:
  - raw/articles/arxiv-2610.00710-relivelgym-long-lived-agents-weeks-replayed-reality.md
confidence: medium
related:
  - concepts/long-horizon-agents
  - concepts/dayjob-benchmark
  - concepts/harness-engineering
  - concepts/ambient-agents
---

# ReLiveGym — Evaluating Long-Lived Agents over Weeks of Replayed Reality

**ReLiveGym** (Jin et al., arXiv:2610.00710, Sep 30 2026; Sahara Labs) is a diagnostic evaluation environment for **long-lived agents** — the class expected to run unattended for days or weeks, act *at the right time*, and adapt to a **temporally changing** environment. Its thesis: existing long-horizon agent benchmarks miss the *time* dimension because they assume a static environment.

## The gap: long-horizon ≠ long-lived

Prior long-horizon work ([[concepts/long-horizon-agents]], [[concepts/dayjob-benchmark]]) mostly measures *how much* work an agent completes in one continuous session, over a static world. Real recurring deployments — market monitoring, ecosystem watching, periodic analysis — instead require:
- operating unattended for **days or weeks**,
- **acting at the right timing** (not just acting well),
- **adapting** as the environment drifts under the agent.

ReLiveGym operationalizes this as **chronologically replayed real-world news, market, and social-media streams** over simulated weeks, with agents acting **sparsely**. Tasks span three axes: time sensitivity, reasoning intensity, and recurrence.

## Headline finding: "when to act" is a first-class harness-design axis

Across **eight base language models**, the authors vary model choice **and** harness design. The central result: **how an agent decides *when* to act** emerges as its own harness-design axis for long-lived tasks — and the optimal choice **varies across tasks and sometimes across models** (no single timing policy wins). They also evaluate **continuous learning from hindsight feedback** (reviewing what happened after the fact) and its effect on the observed failure modes.

This is a notable counterpoint to the [[concepts/harness-tax]] finding that harness choice moves cost 5× but success only ±2–5%: for *long-lived* tasks, the timing/hindsight loop is a place where harness design *does* move the needle — and moves it differently per task.

## Design axes it isolates
1. **Model choice** — baseline capability.
2. **Action-timing mechanism** — the scheduler/trigger policy for *when* to act (the paper's novel axis).
3. **Use of hindsight feedback** — whether/how the agent learns across the replayed timeline.

## Open questions
- "Optimal design varies per task" is a hedge that complicates productization — is there a meta-policy, or does every long-lived agent need a bespoke timing harness?
- Hindsight learning over weeks flirts with the memory-drift and identity issues in [[concepts/latent-identity-reversion]] — does accumulated hindsight feedback destabilize long-run behavior?
- Replayed streams are frozen history; true prospective deployment adds a distribution-shift the replay can't measure.

## Related
- [[concepts/long-horizon-agents]] — the static-environment sibling ReLiveGym extends to time-varying worlds
- [[concepts/dayjob-benchmark]] — hour-scale single-session work; ReLiveGym = week-scale recurring work
- [[concepts/harness-engineering]] / [[concepts/harness-tax]] — timing/hindsight as a harness axis with real success impact
- [[concepts/ambient-agents]] — the deployment class this benchmark targets
