---
title: MIT EnCompass - AI Agent Search Framework
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [agent, search, mit, orchestration, backtracking]
sources:
  - raw/articles/mit-encompass-feb-2026.md
---

# MIT EnCompass

**Published**: February 5, 2026
**Authors**: MIT CSAIL (Alex Shipps, Zhening Li, Armando Solar-Lezama) + Asari AI (Stephan Zheng)

EnCompass is a programming framework that **executes AI agent programs by backtracking and making multiple parallel attempts** to find the best solution paths through LLM-generated agent workflows.

## Key Features

- **Automatic backtracking**: When LLMs make mistakes during agent execution, EnCompass backtracks rather than requiring manual intervention
- **Parallel cloning**: Can clone the program runtime to make multiple attempts in parallel
- **Search over execution paths**: Searches over different possible paths an agent could take based on different LLM outputs
- **User annotations**: Developers annotate where backtracking or cloning may be useful
- **Custom search strategies**: Users can specify their own search strategies or use EnCompass defaults

## Performance

| Metric | Result |
|--------|--------|
| **Coding Effort Reduction** | Up to **80%** (348 fewer lines of code in one test case) |
| **Accuracy Boost** | **15% to 40%** improvement across five repositories |
| **Search Budget** | Achieved results at 16x the LLM calls of a non-search agent |

## Significance

Addresses a fundamental challenge in agent engineering: **LLM non-determinism**. Instead of trying to make LLMs perfectly reliable (which is impossible), EnCompass embraces the uncertainty and searches for optimal execution paths.

The framework demonstrates that **search strategies** (like Monte Carlo Tree Search, Beam Search) can be cleanly separated from agent workflow logic — a powerful pattern for building robust agentic systems.

## Related

- [[concepts/agent-loop-orchestration]] — Agent loop orchestration patterns
- [[concepts/bitter-lesson-agent-harnesses]] — Search-based improvement of agent harnesses
- [[concepts/agent-engineering-guide-2026]] — Agentic engineering patterns
- [[entities/mit-ibm-computing-research-lab]] — MIT research context
