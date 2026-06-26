---
title: "GTA (General Tool Agents)"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - agent-evaluation
sources:
  - title: "GTA: A Benchmark for General Tool Agents"
    arxiv: "2407.08713"
    year: 2024
related_concepts:
  - concepts/ai-benchmarks/appworld
  - concepts/ai-benchmarks/terminal-bench
  - concepts/ai-benchmarks/swe-bench
  - concepts/evaluation/ai-benchmarks-and-evals
---

# GTA (General Tool Agents)

GTA is a benchmark for evaluating **General Tool Agents** — AI systems that must use diverse APIs and tools to accomplish tasks. It tests the fundamental ability of agents to discover, understand, and correctly invoke external tools.

## What It Measures

GTA evaluates:

- **Tool use proficiency** — correctly selecting and invoking tools from a diverse set of APIs
- **API understanding** — interpreting API documentation, parameters, and return formats
- **Multi-tool orchestration** — combining multiple tools to accomplish complex tasks
- **Tool discovery and selection** — identifying the right tool for a given task from a large tool library
- **Error handling and recovery** — dealing with API errors, unexpected outputs, and tool failures

## Data/Methodology

- **Tools**: Diverse set of APIs spanning multiple domains (search, computation, data processing, etc.)
- **Tasks**: Scenarios requiring agents to use one or more tools to produce correct outputs
- **Evaluation**: Accuracy of final task completion and correctness of tool invocation sequences
- **Difficulty levels**: Range from single-tool tasks to complex multi-tool orchestration scenarios
- **Realism**: Tasks model realistic tool-use scenarios that agents would encounter in production
- **Benchmark focus**: General-purpose tool use rather than domain-specific evaluation

## Key Results

- Tool selection accuracy decreases as the number of available tools increases
- Multi-tool orchestration is significantly harder than single-tool tasks
- Agents struggle with understanding API parameter semantics and constraints
- Error recovery after failed tool calls is a weak point for most models
- The benchmark reveals that tool use is a distinct capability from general language understanding

## Related Benchmarks

| Benchmark | Relationship |
|-----------|-------------|
| [[concepts/ai-benchmarks/appworld\|AppWorld]] | Both evaluate tool/API use — GTA is general-purpose, AppWorld is app-focused |
| [[concepts/ai-benchmarks/terminal-bench\|Terminal-Bench]] | Both test tool use — GTA for APIs, Terminal-Bench for CLI tools |
| [[concepts/ai-benchmarks/swe-bench\|SWE-bench]] | Both evaluate agents on task completion, different tool paradigms |
| [[concepts/ai-benchmarks/spider-2\|Spider 2.0]] | Spider 2.0 tests SQL as a tool; GTA tests diverse API tools |

## Connections to Other Wiki Concepts

- **[[concepts/ai-benchmarks/appworld]]**: GTA and AppWorld both test interactive tool use, but GTA provides a broader, more general tool evaluation while AppWorld focuses on interconnected app ecosystems
- **[[concepts/evaluation/ai-benchmarks-and-evals]]**: GTA highlights tool use as a critical, distinct dimension of agent evaluation — separate from pure reasoning or code generation
- **[[concepts/ai-benchmarks/terminal-bench]]**: Terminal-Bench's CLI tasks can be viewed as a specific instance of the general tool-use paradigm GTA evaluates
- GTA's focus on general tool agents connects to the broader trend of [[concepts/ai-benchmarks/swe-lancer|SWE-Lancer]] and similar benchmarks testing agents in realistic, tool-rich environments
