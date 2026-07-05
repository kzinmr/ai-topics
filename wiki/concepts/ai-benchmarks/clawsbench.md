---
title: ClawsBench
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
sources:
  - https://github.com/benchflow-ai/ClawsBench
related_concepts:
  - agent-evaluation
  - ai-agents
---

# ClawsBench

ClawsBench is a benchmark developed by BenchFlow for testing agent clawback and recovery capabilities. It evaluates how well AI agents can recover from errors, undo mistakes, and adapt their approach when initial attempts fail — a critical capability for reliable agent deployment.

## What It Measures

ClawsBench measures an agent's ability to:

- **Error recovery**: How effectively agents can recover from mistakes and failed actions
- **Clawback capability**: The ability to undo or reverse incorrect actions and return to a valid state
- **Adaptive re-planning**: How well agents modify their approach when initial strategies fail
- **Resilience**: The ability to maintain goal-directed behavior despite encountering obstacles or errors
- **Self-correction**: Whether agents can identify their own mistakes and take corrective action without external guidance

## Data/Methodology

ClawsBench uses structured evaluation scenarios within the BenchFlow ecosystem:

- **Error injection**: Tasks where agents are deliberately placed in or led into error states
- **Recovery evaluation**: Assessment of how effectively agents return to productive states after failures
- **Dockerized execution**: Runs within the [[benchflow-tool]] framework for reproducible evaluation
- **Open-source**: Available on GitHub at benchflow-ai/ClawsBench for community contribution
- **Multi-step recovery tasks**: Scenarios that require multiple corrective actions rather than simple single-step fixes

## Key Results

- ClawsBench reveals that error recovery is a significant weakness in current [[concepts/ai-agents]] systems
- Agents that perform well on forward task completion often struggle with clawback and recovery scenarios
- The benchmark highlights the importance of resilience as a distinct evaluation dimension in [[agent-evaluation]]
- Results suggest that agents need better self-monitoring and self-correction capabilities
- Recovery performance varies significantly across different error types and agent architectures

## Related Benchmarks

- [[skillsbench]] — BenchFlow's benchmark for agent skill acquisition and application
- [[benchflow-tool]] — The BenchFlow evaluation framework that hosts ClawsBench
- [[trail]] — Agent trace reasoning and issue localization (also focused on agent failure modes)
- [[hal-leaderboard]] — Princeton's aggregated agent evaluation leaderboard

## Connections to Other Wiki Concepts

ClawsBench addresses a critical gap in [[agent-evaluation]]: the ability to recover from failures. While most benchmarks focus on task completion in ideal conditions, ClawsBench tests what happens when things go wrong — a common occurrence in real-world agent deployment. This connects to [[trail]]'s focus on agent error analysis and complements the forward-looking evaluation of [[skillsbench]] within the BenchFlow ecosystem. Together, these benchmarks contribute to a more complete picture of agent reliability for [[hal-leaderboard]] aggregation.
