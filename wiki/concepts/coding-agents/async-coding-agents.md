---
title: Async Coding Agents
created: 2026-06-09
updated: 2026-06-09
type: concept
tags: [coding-agents, async-agents, cloud-agents, agentic-engineering, multi-agent, autonomous-agents]
sources: [raw/articles/2026-04-12_aman-sanger-cursor-self-driving-codebases-gtc.md]
---

# Async Coding Agents

Cloud-hosted AI coding agents that run independently on their own compute, report results back to the engineer, and can work for hours or days on tasks — analogous to asynchronous colleagues rather than synchronous coding assistants.

## From Sync to Async

The shift from synchronous to asynchronous coding agents represents the third era of AI coding:

| Era | Mode | Interaction | Resource Use |
|-----|------|-------------|-------------|
| Autocomplete | Tab complete | Per-keystroke | Minimal |
| Sync agents | Prompt → response | Turn-based, local | Local machine |
| **Async agents** | Background tasks | Fire-and-forget | Cloud VMs |

## Why Async?

1. **Scale**: Can't run tens of agents on a local machine — need cloud environments
2. **Long-running tasks**: Agents need to run tests, use computers, iterate for hours
3. **Resource intensity**: Testing, video recording, compute-heavy verification require dedicated VMs
4. **Throughput**: Async agents produce 2-4x more code than synchronous local agents

## Architecture

### Multi-Agent Hierarchy
```
Planner (outer agent, ~100K tokens)
├── Sub-planner → Workers
├── Sub-planner → Workers
└── Sub-planner → Sub-planner → Workers
```

Each level bounds its token budget, preventing the train-time/test-time mismatch.

### Model Specialization
- **Planner**: Best reasoning model (e.g., OpenAI)
- **Computer use**: Multi-modal models (Gemini, Anthropic)
- **UI work**: Models with strong design capability (Anthropic)
- **Simple subtasks**: Faster, cheaper models

### Artifacts
Async agents produce reviewable outputs beyond code:
- **Video recordings** of features working
- **Research reports** summarizing experiments
- **Architecture diagrams**
- **Disposable tests** (not checked into codebase)

## Key Insight: Artifacts > Code Review

When agents produce 2-4x more code than you could review manually, reviewing raw diffs becomes intractable. The solution: trust the artifacts. Watch a video of the feature working. Read the research report. Only dive into code when you have high confidence the agent did the right thing.

## Current State (2026)

- **Cursor Cloud Agent**: 30% of merged PRs from cloud agents
- **Automations**: Event-triggered agents (issues, on-call, security)
- **Training monitoring**: Agents watching training runs, flagging anomalies
- Limitations: outer agent still hits token limits on very long tasks; orchestrator models need improvement

## Related Concepts

- [[concepts/self-driving-codebases]] — The end-state vision: fully autonomous codebases
- [[concepts/multi-agents/multi-agent]] — Planner/worker hierarchy
- [[concepts/context-engineering|Context Engineering]] — Spec writing for async agents
- [[concepts/agentic-engineering]] — Broader engineering with agents
