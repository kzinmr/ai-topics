---
title: "Elo-per-token Analysis — Diagnosing How Agents Spend Test-Time Compute"
created: 2026-09-23
updated: 2026-09-23
type: concept
tags: [test-time-scaling, agent-evaluation, token-economics, ai-agents, inference, benchmark, arxiv]
sources:
  - raw/articles/2026-09-23_arxiv_2609.15309_elo-per-token-test-time-strategies.md
related:
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/token-economics]]"
  - "[[concepts/agent-benchmarks]]"
  - "[[concepts/sleep-time-compute]]"
---

# Elo-per-token Analysis — Diagnosing How Agents Spend Test-Time Compute

## Definition

**Elo-per-token analysis** is an evaluation method that measures the *rate* at which an agent
converts spent tokens into rating gains, to classify agents into distinct **test-time
strategies**. Liu, Mang, et al. (arXiv:2609.15309, Sep 2026) use it to answer a question
standard benchmarks leave opaque: *why* an agent's performance degrades once its token budget
runs out.

## Core Findings

Across five LLMs on eight agent benchmarks, two robust patterns emerge:

- **Two phases.** Agents improve at high Elo-per-token rate, then plateau or **degrade** —
  the "agents slow down" phenomenon.
- **Three failure modes** for the post-peak regime: *self-contradiction*, *context loss*, and
  *misleading feedback*.
- **Strategy classification.** A four-quadrant taxonomy (pre-peak rate vs. post-peak drop)
  splits agents into **High Potential** and **Underpressure** profiles.
- **Model-specific remedies.** Context-preserving strategies help GPT-5; verification helps
  DeepSeek — there is no universal fix.

## Why It Matters

It turns test-time compute from a black-box budget into a *diagnostic instrument*. Rather than
reporting a single pass@k, Elo-per-token exposes **how** compute is spent, distinguishing an
agent that plateaus from one that actively gets worse under pressure — a distinction invisible
to aggregate accuracy and directly actionable for tuning [[concepts/test-time-scaling|test-time
scaling]]. Economically it is the agent analog of
[[concepts/token-economics|token economics]]: it prices marginal tokens, exposing the point
where they stop producing value.

## Relationship to Other Ideas

The "degrade after a peak" finding is a first-class evaluation signal for
[[concepts/agent-benchmarks|agent benchmarks]] — a benchmark that stops measuring once agents
are past peak is measuring the wrong thing. The three failure modes map onto
[[concepts/context-engineering|context-engineering]] concerns (context loss) and
[[concepts/agent-runtime-environments|runtime environments]] (misleading feedback from tools).
Where [[concepts/sleep-time-compute|sleep-time compute]] asks *when* to spend reasoning,
Elo-per-token asks *whether more spend still helps* — the two are complementary lenses on the
same compute-vs-accuracy frontier.

## Open Questions

- Are the three failure modes exhaustive, or do new strategies (e.g., multi-agent) produce new post-peak regimes?
- Can the pre-peak/post-peak quadrant predict an agent's real-world budget sensitivity, or is it benchmark-bound?
- Is a single optimal stopping-point detectable online, to auto-truncate a run before the degrade phase?

## Sources

- When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis — arXiv:2609.15309 (2026-09-14), Liu, Mang, Peng, Chai, Li, Pimpalgaonkar, Zettlemoyer, Dimakis, Cheung
