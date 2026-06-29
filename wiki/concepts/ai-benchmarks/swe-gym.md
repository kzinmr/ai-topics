---
title: "SWE-Gym"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - software-engineering
sources:
  - title: "SWE-Gym: Training Software Engineering Agents"
    arxiv: "2412.21139"
    year: 2024
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/swe-lancer
  - concepts/ai-benchmarks/swe-rebench
  - concepts/evaluation/ai-benchmarks-and-evals
---

# SWE-Gym

SWE-Gym is a **training environment and benchmark** for software engineering agents. It provides executable environments where agents can practice SWE-bench-style tasks, bridging the gap between static benchmarks and real interactive development environments.

## What It Measures

SWE-Gym measures and enables:

- **Agent training effectiveness** — how well agents learn from interactive SWE environments
- **Task completion on executable SWE problems** — bugs and features in real codebases with runnable tests
- **Generalization from training to held-out evaluation tasks**
- **Agent scaffolding quality** — measuring how different agent architectures perform in interactive environments

The key innovation is that SWE-Gym is both a training dataset and an evaluation benchmark.

## Data/Methodology

- **Format**: Executable environments with real codebases, test suites, and issue descriptions
- **Task style**: SWE-bench-compatible — agents must resolve issues in real open-source projects
- **Environments**: Fully isolated Docker containers with working development setups
- **Evaluation**: Automated test-based verification (pass/fail on project test suites)
- **Training loop**: Agents can iteratively interact with environments — running tests, reading code, making changes
- **Scale**: Collection of SWE tasks suitable for both training and evaluation

## Key Results

- Training in SWE-Gym environments significantly improves agent performance on [[concepts/ai-benchmarks/swe-bench|SWE-bench]] tasks
- Smaller models trained in SWE-Gym can approach or match larger untuned models on SWE evaluation
- Interactive training environments are more effective than static code examples for agent learning
- Results demonstrate the value of environment-based learning for coding agents

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | SWE-Gym provides training environments for SWE-bench-style tasks |
| [[concepts/ai-benchmarks/swe-rebench\|SWE-rebench]] | Complementary — SWE-rebench refreshes evaluation while SWE-Gym focuses on training |
| [[concepts/ai-benchmarks/swe-lancer\|SWE-Lancer]] | Both advance SWE agent evaluation beyond basic bug-fixing |
| [[concepts/ai-benchmarks/terminal-bench\|Terminal-Bench]] | Both use Docker-based interactive environments for evaluation |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: SWE-Gym directly extends the SWE-bench paradigm by making tasks interactive and trainable
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Represents a shift from pure evaluation benchmarks to training-aware evaluation frameworks
- **[[concepts/ai-benchmarks/swe-rebench]]**: Together with SWE-rebench, SWE-Gym helps address contamination concerns by providing fresh training/evaluation splits
- SWE-Gym's interactive paradigm relates to [[concepts/ai-benchmarks/appworld|AppWorld]]'s approach of providing controllable, interactive environments for agent development
