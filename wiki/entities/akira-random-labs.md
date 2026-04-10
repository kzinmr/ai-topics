---
title: "Akira (Random Labs)"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai-coding-agents, swarm-intelligence, rlm, open-source, y-combinator]
aliases: ["@realmcore_", "realmcore_", "Kiran Chintawar"]
source: x-account
---

# Akira (@realmcore_) — Random Labs

| | |
|---|---|
| **X/Twitter** | [@realmcore_](https://x.com/realmcore_) |
| **GitHub** | [github.com/random-labs](https://github.com/random-labs) |
| **Company** | Random Labs (co-founder, YC S24) |
| **Flagship Product** | Slate — swarm-native coding agent |
| **Location** | San Francisco, CA |

## Overview

**Akira** (known on X as @realmcore_) is co-founder of **Random Labs**, a Y Combinator S24 startup building **Slate**, described as the industry's first "swarm-native" autonomous coding agent. Random Labs was founded in 2024 by **Kiran Chintawar** and **Mihir Chintawar** (brothers). Akira serves as the public-facing technical voice and architect for the project, operating under the @realmcore_ handle.

The company's mission is to build "LLM-based systems for end-to-end software engineering" — creating general-purpose software agents and interfaces that allow engineers to maximally leverage AI models.

## Slate — Swarm-Native Coding Agent

Launched in open beta in March 2026, **Slate** (`npm i -g @randomlabs/slate`) represents a fundamentally different architectural approach compared to existing coding agents like Cursor, Claude Code, or Devin.

### Core Architecture: Thread Weaving

Slate introduces **Thread Weaving**, a novel agent architecture pattern designed to overcome the limitations of both **ReAct** (Reasoning + Acting) and **RLM** (Recursive Language Models):

- **ReAct agents** interleave reasoning traces with action steps but suffer from context window limitations and performance degradation during long sessions
- **RLM agents** externalize data into a Python REPL and recursively call operations, but execute "blind" — committing to full execution paths without intermediate feedback
- **Slate's approach** uses a central orchestrator thread that dispatches bounded worker threads, each executing a single action and returning a compressed "episode" (not a full trace)

The orchestrator manages **strategy** (planning, decomposition), while worker threads handle **tactics** (code execution, file operations). This separation mirrors Karpathy's "LLM OS" concept — the context window is treated as scarce RAM, actively managed rather than exhausted.

### Episodic Memory

When a worker thread completes a task, it returns an **episode** — a compressed representation of important results, not the sprawling transcript of every step. This enables:

- **Composable context**: One thread's episode becomes another thread's input
- **No lossy compaction**: Episodes share context directly with the orchestrator, avoiding brittle message passing
- **Adaptive strategy updates**: The orchestrator can change course when new information arrives mid-task

### Swarm Multi-Model Orchestration

Slate dynamically selects the best model for each subtask:
- **Planning/strategy**: Claude Sonnet
- **Research/search**: GLM 5 (noted for agentic search capabilities)
- **Code execution**: OpenAI Codex

This is similar to Perplexity's Computer multi-model agent. Slate can run all three simultaneously in parallel, ensuring users aren't overspending on intelligence for simple tasks.

### Real-World Performance

A documented porting task (migrating an open-source library to TypeScript) cost **$58.32** with:
- 311 requests
- 583 tool calls
- 15.5 million input tokens

This demonstrates Slate's transparency in token economics — a key differentiator from competitors.

## Random Labs History

- **Early 2025 (May)**: Built one of the first sliding-window-based agents capable of running for up to 2 days in continuous sessions (deprecated, but available as `npm i -g @randomlabs/slatecli`)
- **2024**: Company founded by Kiran and Mihir Chintawar
- **March 2026**: Slate V1 launched as open beta with full technical report published at [randomlabs.ai/blog/slate](https://randomlabs.ai/blog/slate)

## Core Ideas

### "The Bottleneck is Context Architecture, Not Model Capability"
Random Labs argues that models already possess enough knowledge ("Knowledge Overhang") to solve far more tasks than they currently succeed at. The limiting factor is **context management** — how to structure, compress, and route information across long-horizon engineering sessions.

### Beyond ReAct and RLM
In their March 2026 technical report, Random Labs critiqued both dominant paradigms:
- **ReAct**: Good for short tasks but degrades in long sessions due to context window exhaustion
- **RLM**: Expressive but executes blind — no intermediate tactile feedback means failures aren't discovered until the entire plan completes
- **Slate**: Combines the expressivity of ReAct with the context isolation of RLM through thread-based episodic memory

### LLM as Operating System
Slate maps directly onto Karpathy's "LLM OS" framing: the orchestrator is the kernel (schedules tasks), threads are processes (execute operations), and the context window is RAM (scarce, must be managed).

### Open Beta Philosophy
Random Labs ships Slate as an open beta with full transparency on costs, architecture, and limitations. The company explicitly states they're building a "research beta, not an enterprise product" — prioritizing architectural exploration over polish.

## X/Twitter Activity

@realmcore_ is active on X/Twitter where Akira shares:
- Slate architecture explanations and technical deep-dives
- Commentary on ReAct, RLM, and competing agent paradigms
- "Knowledge Overhang" concept — the gap between what models know and what they can effectively use
- Thread Weaving demonstrations and episode examples
- Comparisons between Slate and other coding agents (Cursor, Devin, Claude Code)

## Related

- [[andrej-karpathy]] — "LLM OS" concept that inspired Slate's architectural framing
- [[rlm]] — Recursive Language Models (critiqued by Slate's architecture)
- [[coding-agents]] — AI-powered software development tools
- [[agentic-engineering]] — Multi-agent orchestration patterns
- [[entities/simon-willison]] — Open-source tooling philosophy

## Sources

- [VentureBeat: YC-backed Random Labs launches Slate V1](https://venturebeat.com/orchestration/y-combinator-backed-random-labs-launches-slate-v1-claiming-the-first-swarm) — March 13, 2026
- [Random Labs Blog: Slate](https://randomlabs.ai/blog/slate) — "Moving beyond ReAct and RLM" technical report
- [Techstrong.ai: Random Labs Says Bottleneck is Memory Management](https://techstrong.ai/features/random-labs-says-the-bottleneck-in-ai-agents-isnt-intelligence-its-memory-management) — March 16, 2026
- [ComputerTech: Slate V1 Review](https://computertech.co/slate-v1-review/) — Real-world cost analysis
- [Agent Wars: Random Labs critique of RLM/ReAct](https://agent-wars.com/news/2026-03-13-moving-beyond-rlm-and-react-based-coding-agents)
- [YouTube: Slate Agent Architecture (Vinh Nguyen)](https://www.youtube.com/watch?v=xcWzLcQ4jjc) — Technical breakdown
- [Random Labs About](https://randomlabs.ai/about) — Company mission
- [Docs: Slate](https://docs.randomlabs.ai/) — Installation and usage guide
