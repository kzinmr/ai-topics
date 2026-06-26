---
title: Letta Leaderboard
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - agent-evaluation
sources:
  - https://letta.com/blog/letta-leaderboard
related_concepts:
  - agent-evaluation
  - ai-agents
---

# Letta Leaderboard

The Letta Leaderboard benchmarks LLMs on their agentic memory capabilities, specifically testing how well models can manage, store, retrieve, and utilize information across multi-step agent interactions. Developed by the team behind MemGPT/Letta, it focuses on the memory management dimension of agent performance.

## What It Measures

The Letta Leaderboard measures LLM capabilities in agentic memory management:

- **Memory storage**: How effectively models encode and persist information from interactions
- **Memory retrieval**: The ability to recall relevant information when needed for subsequent tasks
- **Memory management decisions**: Whether models can determine what information to keep, update, or discard
- **Multi-session coherence**: Maintaining consistent knowledge across multiple interaction sessions
- **Information integration**: Combining new information with existing memory to make better decisions
- **Self-directed memory operations**: The model's ability to autonomously manage its own memory without explicit instructions

## Data/Methodology

The Letta Leaderboard uses memory-centric evaluation tasks:

- **Memory management scenarios**: Tasks that require agents to maintain and use information across extended interactions
- **Agentic memory operations**: Tests where models must decide when and how to store, update, or retrieve information
- **Multi-turn evaluation**: Assessments that span multiple interaction turns, testing memory persistence
- **Real-world memory patterns**: Scenarios that reflect practical memory management needs in agent applications
- **Letta framework integration**: Evaluations designed to work with the Letta/MemGPT memory-augmented agent architecture

## Key Results

- Models vary significantly in their ability to manage agentic memory, with performance not always correlating with general benchmark scores
- Strong reasoning models do not necessarily excel at memory management tasks
- The leaderboard reveals that memory management is a distinct capability axis that deserves dedicated evaluation
- Results have informed the Letta team's approach to memory-augmented agent design
- The benchmark demonstrates that [[agent-evaluation]] must include memory as a core dimension

## Related Benchmarks

- [[agent-memory-bench]] — Related benchmark from the same Letta/MemGPT team on agent memory
- [[hal-leaderboard]] — Princeton's aggregated agent leaderboard
- [[trail]] — Agent trace reasoning and issue localization
- [[skillsbench]] — BenchFlow's skill acquisition benchmark

## Connections to Other Wiki Concepts

The Letta Leaderboard highlights that memory is a critical but often overlooked dimension of [[ai-agents]] capability. It connects directly to the [[agent-memory-bench]] and the Letta team's broader thesis that effective memory management is essential for capable agents. This focus on memory as a distinct evaluation axis complements [[agent-evaluation]] frameworks like [[hal-leaderboard]] that aggregate across multiple capability dimensions.
