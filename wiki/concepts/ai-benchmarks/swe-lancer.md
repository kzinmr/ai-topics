---
title: "SWE-Lancer"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
sources:
  - title: "SWE-Lancer: Can AI Agents Earn $1M from Real-World Freelance Software Engineering?"
    arxiv: "2502.12115"
    year: 2025
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/swe-gym
  - concepts/ai-benchmarks/swe-bench-pro
  - concepts/evaluation/ai-benchmarks-and-evals
---

# SWE-Lancer

SWE-Lancer is a benchmark that evaluates AI coding agents on **real-world freelance software engineering tasks** sourced from the Upwork freelancing platform. Unlike benchmarks that focus solely on bug-fixing or patch generation, SWE-Lancer tests end-to-end SWE capability including requirements understanding, solution design, and implementation.

## What It Measures

SWE-Lancer measures an AI agent's ability to:

- **Understand natural-language requirements** from real client job postings on Upwork
- **Perform end-to-end software engineering** — from interpreting vague specifications to delivering working solutions
- **Earn realistic compensation** — tasks are priced at their actual Upwork rates, giving a monetary performance metric
- **Handle diverse SWE tasks** including frontend, backend, full-stack, and DevOps work

The benchmark's central question: *Can AI agents earn meaningful income from real freelance work?*

## Data/Methodology

- **Source**: Tasks collected from Upwork, a major freelancing platform
- **Task types**: Full freelance engagements — not just code patches but complete deliverables
- **Evaluation**: Both automated testing and monetary valuation based on real Upwork pricing
- **Scope**: Covers a wide range of software engineering domains and difficulty levels
- **Realism**: Tasks reflect actual client needs, including ambiguous requirements and open-ended problem specifications

## Key Results

- Current frontier models and agents show limited ability to complete freelance-level tasks end-to-end
- The benchmark reveals significant gaps in requirements understanding compared to pure code generation
- Monetary scoring provides an interpretable performance metric — reported earnings are far below the $1M benchmark name
- Performance varies significantly by task domain (frontend vs. backend vs. full-stack)

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | SWE-Lancer extends beyond SWE-bench's bug-fixing to full freelance tasks |
| [[concepts/ai-benchmarks/swe-gym\|SWE-Gym]] | Complementary training environment for SWE agent development |
| [[concepts/ai-benchmarks/swe-bench-pro\|SWE-bench Pro]] | Both target professional-grade SWE evaluation |
| [[concepts/ai-benchmarks/appworld\|AppWorld]] | Both evaluate agents on realistic, multi-step tasks |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: SWE-Lancer builds on the SWE-bench paradigm but moves from bug-fixing to full feature development and freelance-style tasks
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Represents a new frontier in agent evaluation — testing practical economic viability rather than just technical correctness
- **[[concepts/ai-benchmarks/swe-gym]]**: SWE-Gym's training environments could help prepare agents for SWE-Lancer's evaluation tasks
- SWE-Lancer highlights that [[concepts/ai-benchmarks/swe-bench-agent-scaffolding|agent scaffolding]] quality matters greatly when tasks require end-to-end reasoning rather than focused patch generation
