---
title: "MirrorCode"
type: concept
created: 2026-07-28
updated: 2026-07-28
tags:
  - benchmark
  - evaluation
  - coding-agents
  - ai-agents
  - long-horizon
sources:
  - raw/newsletters/2026-07-27-import-ai-466-the-bitter-lesson-for-robotics-ais-complete-week-long-programming-.md
  - "https://epoch.ai/MirrorCode"
related_concepts:
  - "[[concepts/ai-benchmarks/_index]]"
  - "[[concepts/agent-evaluation]]"
  - "[[concepts/swe-bench]]"
  - "[[entities/epoch-ai]]"
---

# MirrorCode

MirrorCode is a benchmark for evaluating AI systems on **long-horizon programming tasks** — tasks that take humans weeks to complete. Developed jointly by **Epoch AI** and **METR** (Model Evaluation and Threat Research), it was announced in April 2026 and released with additional tests in July 2026.

## What It Measures

MirrorCode assesses AI systems' ability to perform programming tasks that require sustained effort over extended periods. Unlike conventional coding benchmarks that measure single-turn or short-session performance, MirrorCode focuses on:

- **Long-horizon task completion**: Tasks designed to take humans multiple days or weeks
- **Sustained reasoning**: Maintaining coherent problem-solving across extended sessions
- **Autonomous progress tracking**: Self-directed task decomposition and execution
- **Robustness to context accumulation**: Handling growing context without performance degradation

## Key Results

The most striking finding from early MirrorCode evaluations:

- **Claude Opus 4.7** solved a task in **14 minutes** that would take a human multiple weeks
- However, **AI systems could not solve the hardest tasks yet**, suggesting meaningful headroom remains
- The benchmark designers noted this gap as a positive signal — the hardest tasks provide a clear frontier for improvement

## Methodology

MirrorCode was first described in Import AI #453 (April 2026) and subsequently fleshed out with additional test cases. The benchmark is designed to:

1. **Mirror** realistic software engineering workflows by decomposing large tasks into verifiable subtasks
2. **Measure** sustained performance over multiple hours or days of autonomous agent operation
3. **Identify** specific failure modes that emerge only in extended duration tasks

## Significance

MirrorCode fills an important gap in the AI evaluation landscape. Most coding benchmarks (e.g., [[concepts/swe-bench]], HumanEval, MBPP) test short-duration, isolated coding tasks. MirrorCode addresses the question: *how well do AI systems perform when the task requires sustained, multi-day effort?*

The finding that Opus 4.7 can complete a multi-week human task in minutes — but still fails on the hardest problems — suggests that long-horizon capability is improving rapidly but not yet saturated.

## Related Benchmarks

- [[concepts/swe-bench]] — Software engineering benchmark for AI agents (shorter tasks)
- [[concepts/ai-benchmarks/agentdojo]] — Dynamic evaluation for agent security
- [[concepts/ai-benchmarks/benchmaxxing]] — Notes on benchmark over-optimization

## Connections to Other Wiki Concepts

MirrorCode connects to the broader [[concepts/agent-evaluation]] landscape by testing a dimension — sustained long-horizon performance — that existing benchmarks do not adequately cover. Its findings inform discussions of [[concepts/recursive-self-improvement]] and [[concepts/test-time-scaling]] by demonstrating that AI systems can maintain coherent problem-solving over extended periods.
