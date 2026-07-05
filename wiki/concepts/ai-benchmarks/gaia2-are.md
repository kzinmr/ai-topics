---
title: "Gaia2 and ARE"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
sources:
  - title: "Gaia2 and ARE: Scaling Up Agent Environments and Evaluations"
    arxiv: "2509.17158"
    year: 2025
related_concepts:
  - "[[gaia-benchmark]]"
  - "[[theagentcompany]]"
  - "[[deepresearch-bench]]"
  - "[[crmarena-pro]]"
---

# Gaia2 and ARE

Gaia2 and ARE (Agent Runtime Environment) represent a significant scaling-up of agent evaluation infrastructure. Gaia2 is the successor to the [[gaia-benchmark|GAIA benchmark]], expanding both the number and diversity of tasks while ARE provides a unified runtime environment for executing and evaluating agents across diverse task types. Together, they aim to establish a more comprehensive and scalable standard for measuring AI agent capabilities.

## What It Measures

Gaia2 and ARE evaluate agents on:

- **Broad agent capabilities**: A wider range of tasks than the original GAIA benchmark, spanning research, analysis, tool use, multi-step reasoning, and real-world task execution
- **Scalable evaluation**: Ability to assess agents consistently across hundreds of diverse tasks with varying difficulty levels
- **Environment interaction**: How agents navigate and utilize complex digital environments including web browsers, file systems, APIs, and communication tools
- **Multi-step reasoning chains**: Tasks requiring long sequences of actions and decisions, testing sustained planning and execution
- **Cross-domain generalization**: Whether agents can apply capabilities learned in one domain to tasks in different domains
- **Real-world task complexity**: Tasks that reflect the complexity and ambiguity of real-world work rather than simplified academic problems

## Data/Methodology

Gaia2 and ARE introduce several methodological advances over the original GAIA benchmark:

- **Expanded task set**: Gaia2 significantly increases the number of evaluation tasks compared to GAIA, with broader coverage of difficulty levels and domains
- **ARE runtime**: The Agent Runtime Environment provides a standardized execution platform that supports diverse task types — web browsing, code execution, file manipulation, API calls, and more
- **Unified evaluation framework**: ARE defines consistent evaluation protocols across task types, enabling fair comparison of agents with different architectures and tool sets
- **Difficulty scaling**: Tasks are organized along multiple difficulty dimensions (number of steps, tool complexity, reasoning depth, domain expertise required)
- **Reproducible environments**: ARE provides sandboxed, reproducible execution environments that ensure consistent evaluation conditions
- **Community contribution**: The framework is designed to support community-contributed tasks, enabling the benchmark to grow over time

## Key Results

- Gaia2 confirms and extends the original GAIA findings — there remains a substantial gap between the best AI agents and human performance on complex real-world tasks
- The expanded task set reveals more nuanced capability profiles — agents that excel on some task types may struggle on others that require different skill combinations
- Multi-step tasks with more than 10 actions remain particularly challenging, with error rates compounding across steps
- Web-based tasks (navigating websites, extracting information, completing online forms) are a significant source of failures
- The ARE runtime enables more consistent evaluation than ad-hoc benchmark setups, reducing evaluation noise
- Performance improvements in frontier models are visible in Gaia2 scores, suggesting the benchmark has sufficient headroom to track future progress

## Related Benchmarks

- **[[gaia-benchmark]]**: The predecessor to Gaia2; Gaia2 expands on GAIA's task set and evaluation methodology
- **[[theagentcompany]]**: Tests agents in company simulation; Gaia2/ARE provides broader task coverage across diverse environments
- **[[deepresearch-bench]]**: Evaluates deep research capabilities; Gaia2 includes research tasks alongside many other task types
- **[[crmarena-pro]]**: Tests enterprise-specific tasks; Gaia2 covers enterprise tasks as part of its broader evaluation

## Connections to Other Wiki Concepts

Gaia2 and ARE are central to the [[agent-evaluation]] ecosystem, providing the infrastructure needed to track progress in [[concepts/ai-agents]] capabilities at scale. The benchmark connects to discussions of [[benchmark-saturation]] — as agents improve on existing benchmarks, new benchmarks like Gaia2 provide headroom for continued evaluation. ARE as a runtime environment relates to [[agent-infrastructure]] and the growing need for standardized platforms for developing, deploying, and evaluating AI agents. Gaia2 also connects to [[leaderboard-culture]] in AI and the question of how to design benchmarks that remain meaningful as capabilities advance. The benchmark's community contribution model relates to [[open-benchmark]] movements and collaborative evaluation efforts.
