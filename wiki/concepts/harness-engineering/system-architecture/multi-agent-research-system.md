---
title: "Multi-Agent Research System"
type: concept
aliases:
  - multi-agent-research
  - orchestrator-worker-research
  - parallel-subagents
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
  - multi-agent
status: draft
sources:
  - "https://www.anthropic.com/engineering/built-multi-agent-research-system"
---

# Multi-Agent Research System

A research system built by Anthropic that operates multiple Claude agents in parallel.

## Core Insight

> "Multi-agent systems work mainly because they help spend enough tokens to solve the problem."

> "Token usage alone explains 80% of the performance variance in research tasks."

**The primary reason multi-agent systems work is that they enable spending enough tokens to solve the problem.**

## Architecture

**Pattern**: Orchestrator-Worker (parallel sub-agents)

```
User Query → LeadResearcher (planning, saved to Memory at 200k+ tokens)
  → Sub-agent generation (parallel search + interleaved thinking)
  → Integrate findings → CitationAgent (source integrity verification)
  → Final Output
```

**Separation of concerns**: Each sub-agent has its own tools, prompts, and exploration trajectories, reducing path dependency.

## Performance Metrics

| Metric | Value |
|--------|-------|
| **Single Opus 4 vs Multi-agent** | Opus 4 (lead) + Sonnet 4 (subagents) outperforms single Opus 4 by **90.2%** |
| **Token variance** | On BrowseComp evaluation, token usage explains **80%** of performance variance |
| **Cost reality** | Single-agent uses ~4× chat tokens, multi-agent uses ~15× |
| **Applicability** | High-value, highly parallelizable tasks. Information exceeding single context window |

**Unsuitable cases**: Tightly coupled / sequential workflows (e.g., most coding tasks)

## 8 Prompt Engineering Principles

1. **Simulate step-by-step**: Run prompts/tools in sandbox, identify failure modes (endless search, redundant queries, incorrect tool selection)
2. **Explicit delegation**: Provide sub-agents with clear objectives, output formats, tool boundaries, and source guidance to prevent overlap
3. **Scale effort to complexity**:
   - *Simple*: 1 agent, 3-10 tool calls
   - *Medium*: 2-4 agents, 10-15 calls each
   - *Complex*: 10+ agents with strictly divided responsibilities
4. **Optimize tool design**: Match tools to user intent. Poor descriptions cause catastrophic path divergence. Use explicit heuristics (e.g., "prefer specialized tools over general ones")
5. **Self-improvement loop**: Claude 4 can debug its own prompts/tools. Dedicated tool-testing agents reduce future task completion time by **40%**
6. **Broad to narrow search**: Start with short, broad queries → evaluate results → gradually narrow focus
7. **Leverage Extended Thinking**: Use thinking tokens as controllable scratchpad for planning, tool selection, and post-result gap analysis
8. **Maximize parallelism**: Lead generates 3-5 sub-agents simultaneously. Sub-agents use 3+ tools in parallel. Reduces research time by up to **90%**

## Evaluation Strategy

**Challenge**: Non-deterministic paths make step-by-step verification impossible

- **Start small**: ~20 real queries provide rapid, high-impact feedback in early development
- **LLM-as-Judge**: Single-prompt scoring from 0.0 to 1.0 (factual accuracy, citation accuracy, completeness, source quality, tool efficiency). Scalable and consistent with human judgment
- **Human monitoring**: Catch edge cases and systematic biases (e.g., early agent prioritizing SEO content farms over academic PDFs → resolved with source quality heuristics)
- **Focus on emergence**: Optimize not just individual agent prompts but interaction frameworks and division of labor

## Production Reliability

- **Stateful execution**: Long-running processes require fault-tolerant execution, retry logic, and periodic checkpoints. Agents resume from failure points
- **Graceful degradation**: Notify agents of tool failures. Let them adapt autonomously. Combine AI flexibility with deterministic safeguards
- **Debugging**: Full production tracing + monitoring of decision patterns/interaction structures (privacy-preserving, no content logging)
- **Deployment**: Rainbow deployments to gradually shift traffic without breaking active agents mid-flight
- **Current bottleneck**: Synchronous sub-agent execution blocks information flow. Future: asynchronous execution for higher parallelism (adding coordination/state complexity)

## Advanced Multi-Agent Patterns

- **End-state evaluation**: For state-changing agents, judge final results rather than intermediate steps. Use discrete checkpoints for complex workflows
- **Long-running context management**: Summarize phases → save to external memory → spawn new sub-agents with clean context → retrieve plan when approaching limits
- **Filesystem artifacts**: Sub-agents write structured outputs (code, reports, data) directly to external storage, passing lightweight references to coordinator. Eliminates "telephone game," reduces token overhead

## Related Concepts

- [[concepts/harness-engineering]] — Top-level index
- [[concepts/building-effective-agents]] — Fundamental principles of agent construction
- — Orchestrator-worker pattern
- [[concepts/context-engineering|Context Engineering]] — Context engineering
