---
title: "Terminal-Bench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - coding-agents
  - ai-agents
sources:
  - title: "Terminal-Bench"
    url: "https://github.com/harbor-framework/terminal-bench"
    stars: "2.4k"
    affiliation: "Stanford / Harbor"
    year: 2025
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/appworld
  - concepts/ai-benchmarks/gta-benchmark
  - concepts/evaluation/ai-benchmarks-and-evals
---

# Terminal-Bench

Terminal-Bench is a benchmark featuring **hard, realistic tasks in command-line interfaces**, developed by Stanford and the Harbor framework. It provides Docker-based environments with programmatic verification, targeting the intersection of AI agents and terminal/CLI proficiency.

## What It Measures

Terminal-Bench evaluates:

- **Command-line proficiency** — agents must navigate, manipulate, and reason in terminal environments
- **Realistic system administration tasks** — file management, process control, networking, configuration
- **Tool use in CLI contexts** — using shell commands, CLI tools, and scripting effectively
- **Problem-solving in constrained environments** — completing tasks with limited information and tool access
- **Programmatic task completion** — verifiable, deterministic outcomes for objective evaluation

## Data/Methodology

- **Environment**: Docker containers providing isolated, reproducible terminal environments
- **Tasks**: Hard, realistic CLI tasks covering system administration, DevOps, and general terminal workflows
- **Verification**: Programmatic verification — tasks have deterministic success criteria checked by automated evaluators
- **Difficulty**: Significantly harder than simple command-line tasks — requiring multi-step reasoning and planning
- **Scale**: Collection of tasks with varying complexity and domain coverage
- **Open source**: Available on GitHub with ~2.4k stars (harbor-framework/terminal-bench)
- **Affiliation**: Developed by Stanford University in collaboration with the Harbor framework

## Key Results

- Current AI agents show significant limitations in terminal-based task completion
- Multi-step CLI tasks with dependencies between steps are particularly challenging
- Agents frequently make errors in command syntax, flag usage, and tool invocation order
- The benchmark reveals important gaps in agents' understanding of system-level concepts
- Performance varies significantly by task complexity and domain

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | Terminal-Bench tests CLI skills; SWE-bench tests code patching |
| [[concepts/ai-benchmarks/appworld\|AppWorld]] | Both provide interactive environments — CLI vs. app APIs |
| [[concepts/ai-benchmarks/gta-benchmark\|GTA]] | Both evaluate agent tool use in realistic settings |
| [[concepts/ai-benchmarks/swe-gym\|SWE-Gym]] | Both use Docker-based interactive environments |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/swe-bench]]**: Terminal-Bench complements SWE-bench by testing the "shell side" of software engineering — many real SWE tasks involve significant terminal interaction
- **[[concepts/ai-benchmarks/appworld]]**: Both test interactive agent capabilities, but in different modalities (CLI vs. API)
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: Terminal-Bench exemplifies the trend toward realistic, environment-based evaluation with programmatic verification
- **[[concepts/ai-benchmarks/gta-benchmark]]**: Terminal-Bench's CLI focus is a natural subset of general tool-agent evaluation — terminal proficiency is a core tool-use skill
