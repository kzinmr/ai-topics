---
title: Agent Memory Benchmark
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - agent-evaluation
sources:
  - https://letta.com/blog/benchmarking-ai-agent-memory
related_concepts:
  - agent-evaluation
  - ai-agents
---

# Agent Memory Benchmark

The Agent Memory Benchmark, developed by the Letta/MemGPT team, evaluates AI agent memory systems and explores whether a simple filesystem-based approach to agent memory is sufficient. It benchmarks different memory architectures and strategies for storing, retrieving, and utilizing information across agent interactions.

## What It Measures

The Agent Memory Benchmark measures:

- **Memory system effectiveness**: How well different memory architectures support agent task performance
- **Filesystem-as-memory**: Whether simple filesystem-based memory storage is sufficient for agent needs
- **Memory retrieval accuracy**: How correctly agents retrieve relevant stored information when needed
- **Memory coherence**: Whether agents maintain consistent and non-contradictory information across interactions
- **Memory scalability**: How memory systems perform as the volume of stored information grows
- **Cross-session persistence**: The ability to maintain and utilize information across multiple interaction sessions

## Data/Methodology

The benchmark uses a systematic evaluation of memory approaches:

- **Memory architecture comparison**: Tests multiple memory system designs including filesystem-based approaches
- **"Is a filesystem all you need?"**: A core research question exploring whether simple file-based memory can match more complex memory architectures
- **Task-based evaluation**: Memory systems are evaluated based on how well they support agent task completion
- **Letta/MemGPT expertise**: Leverages the team's deep experience with memory-augmented agents from the MemGPT project
- **Practical scenarios**: Tests based on realistic agent memory needs rather than synthetic memory challenges

## Key Results

- The benchmark tests the provocative hypothesis that a filesystem may be all that's needed for agent memory
- Results compare filesystem-based memory against more sophisticated memory management approaches
- Memory system design significantly impacts agent performance on tasks requiring long-term information retention
- The benchmark provides empirical evidence to guide memory architecture decisions for [[ai-agents]] development
- Findings inform the Letta team's approach to memory system design in their agent framework

## Related Benchmarks

- [[letta-leaderboard]] — Letta's benchmark for LLM agentic memory management capability
- [[hal-leaderboard]] — Princeton's aggregated agent evaluation leaderboard
- [[trail]] — Agent trace reasoning and issue localization
- [[skillsbench]] — BenchFlow's skill acquisition benchmark

## Connections to Other Wiki Concepts

The Agent Memory Benchmark directly connects to the [[letta-leaderboard]] as both come from the Letta/MemGPT team and focus on memory as a critical dimension of agent capability. Together, they explore both the model-side (how well LLMs manage memory) and system-side (what memory architecture works best) of the memory problem in [[ai-agents]]. This research contributes to [[agent-evaluation]] by establishing memory as a first-class evaluation dimension alongside task completion, reasoning, and tool use.
