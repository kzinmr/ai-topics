---
title: "Workspace-Bench 1.0"
created: 2026-05-07
updated: 2026-05-07
type: concept
tags: [benchmark, evaluation, ai-agents, coding-agents, multi-file, workspace]
aliases: ["workspace-bench", "Workspace-Bench"]
sources: [raw/papers/2026-05-05_arXiv_2605.03596_workspace-bench.md]
---

# Workspace-Bench 1.0

Workspace-Bench 1.0 is a comprehensive benchmark created by **OpenDataBox** (Zirui Tang et al.) that evaluates AI agents on "Workspace Learning" — the ability to navigate, reason over, and exploit complex dependencies in large-scale, heterogeneous file environments.

**arXiv**: [2605.03596](https://arxiv.org/abs/2605.03596) (May 5, 2026) | **GitHub**: [OpenDataBox/Workspace-Bench](https://github.com/OpenDataBox/Workspace-Bench) | **License**: MIT

## Core Concept: Workspace Learning

> "Whether an agent can identify, reason over, exploit, and update explicit and implicit dependencies among heterogeneous files in a real worker's workspace."

Unlike single-file or small-bundle benchmarks, Workspace-Bench requires agents to:
1. **Identify** relevant files in a massive directory
2. **Reason** about cross-file relationships (e.g., config → script output)
3. **Exploit** dependency graphs to solve tasks
4. **Update** files while maintaining system integrity

## Key Statistics

| Metric | Value |
|--------|-------|
| Worker Profiles | 5 (Operations Manager, Logistics Manager, AI Product Manager, Researcher, Backend Developer) |
| File Types | 74 |
| Total Files | 20,476 |
| Workspace Size | Up to 20GB |
| Tasks | 388 |
| Evaluation Rubrics | 7,399 |
| Lite Version | 100 tasks (~70% cost savings, preserves distribution) |

## Performance

| Agent | Score |
|-------|-------|
| Human (baseline) | **80.7%** |
| Best AI (OpenClaw + Claude Opus 4.7) | **68.7%** |
| Average AI (across 7 models × 4 harnesses) | **47.4%** |

The 12% gap between best AI and human, and 33.3% gap between average AI and human, shows substantial room for improvement.

## Key Findings

### Harness Design Matters
The architecture of the agent harness (how it interacts with the environment) is a major factor in cost, efficiency, and final success rates — consistent with findings from [[concepts/frontier-swe-benchmark]].

### Scale Is the Differentiator
Existing benchmarks fail to capture real-world complexity because they lack the "large-scale file dependencies" present here. The 74 file types and 20GB workspace create retrieval challenges that single-file benchmarks don't test.

### Cross-File Reasoning Gap
Agents struggle with implicit links between heterogeneous data formats (spreadsheets → configs → scripts → docs). This is a distinct capability gap from pure code generation.

## Five-Stage Evolution Model

The paper defines a 5-level progression for workspace learning capability:
- **L0**: Single-file, single-format
- **L1**: Multi-file, homogeneous format
- **L2**: Multi-file, heterogeneous formats, explicit dependencies
- **L3**: Multi-file, heterogeneous formats, implicit dependencies
- **L4**: Adaptive workspace learning (human-level)

## Agent-as-a-Judge Evaluation

Uses a rubric-based evaluation framework with 7,399 rubrics covering both final output correctness and navigation efficiency — a more granular approach than binary pass/fail.

## Relationship to Other Benchmarks

| Benchmark | Focus | Scale |
|-----------|-------|-------|
| [[concepts/swe-bench]] | PR-level code fixes | Small scope |
| [[concepts/frontier-swe-benchmark]] | Ultra-long-horizon engineering (20h) | 17 difficult tasks |
| **Workspace-Bench** | Multi-file workspace navigation | 20,476 files, 74 types |
| [[concepts/kernelbench]] | Kernel-level optimization | Specialized |
| [[concepts/agent-survival-benchmark]] | Human-normalized agent capability | Diverse tasks |

## Key Significance

Workspace-Bench shifts evaluation focus from "can the model write code" to "can the agent navigate and reason across a realistic professional environment." The 74-file-type heterogeneity and explicit dependency graphs make it the benchmark that most closely mirrors real knowledge-worker environments. Combined with [[concepts/frontier-swe-benchmark]]'s ultra-long-horizon perspective, these benchmarks together define the 2026 frontier of coding agent evaluation.

## See Also

- [[concepts/frontier-swe-benchmark]] — Ultra-long-horizon coding benchmark (20h tasks)
- [[concepts/swe-bench]] — Standard PR-level coding benchmark
- [[concepts/harness-engineering]] — Agent execution environment design
- [[concepts/ai-evals]] — AI evaluation landscape
- [[concepts/evals-for-ai-agents]] — Agent-specific evaluation approaches
