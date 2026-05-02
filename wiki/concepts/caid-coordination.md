---
title: "CAID (Centralized Asynchronous Isolated Delegation)"
type: concept
created: 2026-04-09
updated: 2026-04-09
tags:
  - concept
  - multi-agent
  - coding-agents
  - cmu
  - coordination
related: [multi-agent-systems, coding-agents, parallelism]
sources: []
---

# CAID (Centralized Asynchronous Isolated Delegation)

A coordination framework from CMU (2026) for running multiple coding agents in parallel on complex software engineering tasks. Uses git operations as the core coordination primitive.

## Key Design

### Branch-and-Merge Coordination
- Each agent isolated in its own workspace branch
- Git operations (worktree, commit, merge) serve as coordination mechanism
- Structured integration with test verification prevents conflicts
- Avoids interference that plagues naive parallelism

## Results

| Task Type | Improvement vs Single-Agent |
|-----------|----------------------------|
| Paper reproduction | **+26.7%** absolute |
| Python library development | **+14.3%** absolute |

### Optimal Parallelism
- Performance improves: 2 → 4 agents
- Performance decreases: → 8 agents
- **Not monotonic** — coordination overhead eventually dominates
- Overly fine-grained delegation causes integration costs

### Failure Modes
Primary coordination failures:
1. Imprecise task handoffs
2. Underspecified subgoals
3. Coarse-grained delegation misaligned with task dependency structure
4. Locally correct outputs that are globally inefficient to integrate

## When to Use
- Sustained, multi-step reasoning across large codebases
- Tasks where coordination overhead is manageable
- Team sizes of 2-4 agents (optimal range)

## When NOT to Use
- Simple tasks that don't benefit from parallelism
- Tasks requiring tight coupling between agents
- Beyond 4 agents without improved coordination strategy

## Sources
-  (NLP News coverage)
- CMU research paper (2026)

## Related
- 
- [[concepts/long-context-coding-agents]]
- [[concepts/harness-engineering]]
- 
