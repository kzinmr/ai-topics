---
title: "RE-Bench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - lab
sources:
  - title: "RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents"
    arxiv: "2411.15114"
    authors: ["METR"]
    year: 2024
related_concepts:
  - "[[paperbench]]"
  - "[[scienceagentbench]]"
  - "[[mle-bench]]"
  - "[[gaia-benchmark]]"
---

# RE-Bench

RE-Bench is an AI R&D evaluation benchmark developed by [METR](https://metr.org) that measures the ability of AI agents to perform machine learning research tasks. Rather than testing theoretical knowledge or coding ability in isolation, RE-Bench evaluates whether agents can carry out end-to-end research workflows that mirror what human ML researchers do in practice.

## What It Measures

RE-Bench assesses an agent's capacity to:

- **Optimize ML training pipelines**: Tune hyperparameters, adjust architectures, and improve model performance on defined objectives
- **Implement research papers**: Translate algorithmic descriptions from papers into working code
- **Debug and iterate on experiments**: Identify failures, propose fixes, and run experiments to validate improvements
- **Manage research compute budgets**: Make efficient use of computational resources under time and cost constraints

The benchmark specifically targets tasks that are representative of real AI R&D work, distinguishing it from benchmarks that test general coding or knowledge recall.

## Data/Methodology

RE-Bench presents agents with open-ended ML research tasks that have verifiable ground-truth answers or measurable performance metrics. Key methodological features include:

- **Structured task format**: Each task specifies a clear objective, baseline code, compute budget, and evaluation criteria
- **Sandboxed execution**: Agents operate in isolated environments with access to standard ML tooling (Python, PyTorch, etc.)
- **Automated scoring**: Performance is measured against objective metrics like model accuracy, loss values, or task completion
- **Cost tracking**: The benchmark tracks both the quality of solutions and the compute cost incurred by the agent during the process

Tasks span areas such as neural architecture search, training optimization, data preprocessing, and reproducing experimental results from published work.

## Key Results

- Frontier LLM-based agents demonstrate growing capability on RE-Bench tasks but remain well below expert human researcher performance
- Agent performance correlates strongly with the availability of tool use and the ability to iterate over multiple experiments
- Simple optimization tasks (e.g., hyperparameter tuning) are substantially easier for agents than creative research tasks requiring novel algorithmic insight
- The gap between agent and human performance narrows on tasks with clear evaluation signals and well-defined search spaces

## Related Benchmarks

- **[[paperbench]]**: Evaluates paper replication from scratch, complementing RE-Bench's focus on specific R&D subtasks
- **[[mle-bench]]**: Tests ML engineering through Kaggle competitions, focusing on applied ML rather than research methodology
- **[[scienceagentbench]]**: Assesses agents on scientific discovery tasks across broader scientific domains
- **[[gaia-benchmark]]**: Tests general AI assistant capabilities, some of which overlap with research-relevant skills

## Connections to Other Wiki Concepts

RE-Bench sits at the intersection of [[ai-agents]] and [[ai-research]] evaluation. As AI systems become more capable of autonomous research, RE-Bench provides a crucial yardstick for measuring progress toward [[automated-scientific-discovery]]. The benchmark's focus on ML research specifically connects to broader discussions about [[ai-safety]] — if agents can perform R&D tasks, understanding their capabilities and limitations becomes essential for managing risks from advanced AI systems. RE-Bench also relates to discussions of [[tool-use]] in language models, as effective agents must orchestrate complex multi-step workflows involving code execution, experimentation, and analysis.
