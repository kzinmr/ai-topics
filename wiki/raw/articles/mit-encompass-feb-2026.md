---
title: MIT EnCompass - AI Agent Search Framework
date: 2026-02-05
source: MIT News / MIT CSAIL
url: https://news.mit.edu/2026/helping-ai-agents-search-to-get-best-results-from-llms-0205
---

# MIT EnCompass

**Published**: February 5, 2026

**Authors**: MIT CSAIL (Alex Shipps et al.)

EnCompass is a framework that executes AI agent programs by **backtracking** and making **multiple parallel attempts** to find the best solution paths through LLM-generated agent workflows.

## Key Features

- **Automatic backtracking**: When LLMs make mistakes during agent execution, EnCompass backtracks rather than requiring manual intervention
- **Parallel cloning**: Can clone the program runtime to make multiple attempts in parallel
- **Search over execution paths**: Searches over different possible paths an agent could take based on different LLM outputs
- **User annotations**: Developers annotate where backtracking or cloning may be useful
- **Custom search strategies**: Users can specify their own search strategies or use EnCompass defaults

## Significance

Addresses a fundamental challenge in agent engineering: **LLM non-determinism**. Instead of trying to make LLMs perfectly reliable (which is impossible), EnCompass embraces the uncertainty and searches for optimal execution paths.

## Related Concepts

- [[concepts/agent-loop-orchestration]]
- [[concepts/bitter-lesson-agent-harnesses]]
- [[concepts/agent-engineering-guide-2026]]
