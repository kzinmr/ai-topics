---
title: "AppWorld"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - ai-agents
sources:
  - title: "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents"
    venue: "ACL 2024"
    year: 2024
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/terminal-bench
  - concepts/ai-benchmarks/gta-benchmark
  - concepts/evaluation/ai-benchmarks-and-evals
---

# AppWorld

AppWorld is a benchmark featuring a **controllable world of apps and people** for evaluating interactive coding agents. Published at ACL 2024, it provides a simulated ecosystem of **9 interconnected apps** and **458 tasks** that test an agent's ability to interact with APIs and manage complex multi-app workflows.

## What It Measures

AppWorld evaluates:

- **Interactive coding ability** — agents must write code that interacts with multiple app APIs
- **Multi-step reasoning** — tasks require chaining operations across apps and managing state
- **API understanding and usage** — agents must correctly discover, understand, and call APIs
- **Real-world task completion** — tasks model realistic user needs across social, productivity, and utility apps
- **State management** — tracking and managing information across app interactions over time

## Data/Methodology

- **Apps**: 9 interconnected applications covering social, productivity, and utility domains
- **Tasks**: 458 tasks of varying complexity, from simple single-app operations to complex multi-app workflows
- **Environment**: Controllable sandbox where apps have defined APIs, data models, and user populations
- **Evaluation**: Programmatic verification of task completion against expected outcomes
- **Interaction model**: Agents write and execute code to interact with app APIs
- **Controllability**: Full deterministic control over the simulated world state

## Key Results

- Current coding agents show significant struggles with multi-app coordination tasks
- Single-app tasks are substantially easier than cross-app workflows
- Error rates increase with the number of API calls and apps involved
- The benchmark reveals important gaps in agents' ability to reason about API semantics and data flow
- Results suggest that interactive coding requires different capabilities than static code generation

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | AppWorld focuses on API interaction rather than code patching |
| [[concepts/ai-benchmarks/terminal-bench\|Terminal-Bench]] | Both test agents in interactive, realistic environments |
| [[concepts/ai-benchmarks/gta-benchmark\|GTA]] | Both evaluate agent tool use and API interaction |
| [[concepts/ai-benchmarks/swe-lancer\|SWE-Lancer]] | Both test real-world task completion beyond simple code fixes |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: AppWorld complements SWE-bench by testing a different aspect of software engineering — API interaction and multi-app orchestration rather than code patching
- **[[concepts/ai-benchmarks/gta-benchmark]]**: Both evaluate tool use, but AppWorld provides a richer, more interconnected app ecosystem
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: AppWorld represents the interactive simulation approach to benchmarking, distinct from static code-based evaluation
- **[[concepts/ai-benchmarks/terminal-bench]]**: Both provide realistic interactive environments, but AppWorld focuses on app APIs while Terminal-Bench targets CLI environments
