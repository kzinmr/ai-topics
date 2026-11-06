---
title: "AlphaEval (Production-Grounded Agent Benchmark)"
type: concept
created: 2026-11-06
updated: 2026-11-06
tags:
  - benchmark
  - evaluation
  - agent-evaluation
  - ai-agents
  - arxiv
sources:
  - raw/papers/2026-11-06_2604.12162_alphaeval-evaluating-agents-in-production.md
  - "https://arxiv.org/abs/2604.12162"
related_concepts:
  - "[[concepts/ai-benchmarks/gdpval]]"
  - "[[concepts/agents-last-exam]]"
  - "[[concepts/dayjob-benchmark]]"
  - "[[concepts/benchmark-ceiling]]"
  - "[[concepts/ai-benchmarks/blood-on-the-clocktower-dwarkesh]]"
---

# AlphaEval (Production-Grounded Agent Benchmark)

AlphaEval (arXiv:2604.12162, submitted April 14, 2026) is a **production-grounded agent benchmark of 94 tasks sourced from seven companies that actually deploy AI agents in their core business**, spanning six O*NET (Occupational Information Network) occupational domains. Lead authors: Pengrui Lu, Pengfei Liu et al. (27 authors).

## Why it exists: the production-reality gap

The paper's core thesis is that agent deployment in commercial settings has outpaced evaluation methodology. Existing benchmarks are **retrospectively curated tasks with well-specified requirements and deterministic metrics** — conditions that diverge from production environments in five specific ways:

1. Requirements contain **implicit constraints** (not fully specified up front)
2. Inputs are **heterogeneous multi-modal documents** with information fragmented across sources
3. Tasks demand **undeclared domain expertise**
4. Outputs are **long-horizon professional deliverables**
5. Success is judged by **domain experts whose standards evolve over time**

## What makes it different from GDPval/DayJob-style suites

- **Product-level, not model-level evaluation.** AlphaEval evaluates *complete agent products* — Claude Code, Codex, etc. — as commercial systems, capturing performance variations invisible to model-level evaluation (the same harness/model confound surfaced elsewhere, e.g. [[concepts/ai-benchmarks/blood-on-the-clocktower-dwarkesh]]'s Elo-vs-prompt sensitivity and the harness caveats in [[concepts/kimi-k3]]'s benchmark table).
- **Multi-paradigm judging framework.** Coverage spans LLM-as-a-Judge, reference-driven metrics, formal verification, rubric-based assessment, and automated UI testing — individual domains compose multiple paradigms rather than relying on a single oracle.
- **Requirement-to-benchmark construction framework.** Beyond the task suite itself, the paper contributes a systematic, reproducible, modular methodology that transforms authentic production requirements into executable evaluation tasks "in minimal time" — a pipeline any organization can adopt. This directly addresses the evaluation-scarcity problem described in [[concepts/benchmark-ceiling]]: rather than a static item pool that depreciates, the framework industrializes the production of fresh, contamination-resistant tasks from live business requirements.

## Position in the benchmark landscape

AlphaEval belongs to the wave of **ground-truth professional-work benchmarks** — alongside OpenAI's [[concepts/ai-benchmarks/gdpval]] (economically valuable tasks), the hour-scale [[concepts/dayjob-benchmark]], and [[concepts/agents-last-exam]] (economically valuable agent tasks at the hardest tier). Its distinguishing angle is *provenance*: tasks are not retrospectively curated by researchers but lifted from seven companies' real agent deployments, and judged by those companies' own domain experts on evolving standards.

## Caveats

- Single-snapshot paper (v1, April 2026) found during a November 2026 crawl; adoption, leaderboard activity, and whether the seven companies have remained anonymous have not been independently verified in this wiki yet.
- 94 tasks is small relative to DayJob's 582 or GDPval's 1,320; statistical power per O*NET domain is correspondingly limited.
- Expert-judged, evolving standards imply lower run-to-run reproducibility than deterministic-metric suites — a deliberate trade-off.

## See Also

- [[concepts/ai-benchmarks/gdpval]] — economically valuable real-world tasks (the lineage AlphaEval extends)
- [[concepts/dayjob-benchmark]] — hour-scale ground-truth work benchmark with premature-commitment failure mode
- [[concepts/agents-last-exam]] — hardest-tier economically valuable agent tasks
- [[concepts/benchmark-ceiling]] — evaluation scarcity / depreciation model that the construction framework targets
- [[concepts/benchmark-framing]] — how benchmark design choices shape reported capability
