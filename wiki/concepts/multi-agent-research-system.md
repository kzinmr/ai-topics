---
title: "Multi-Agent Research System (Anthropic)"
type: concept
created: 2026-04-25
updated: 2026-05-26
tags:
  - multi-agent
  - orchestration
  - lab
  - evaluation
aliases:
  - Claude Research multi-agent
  - orchestrator-worker research
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_multi-agent-research-system.md
  - https://www.anthropic.com/engineering/multi-agent-research-system
related:
  - multi-agent-orchestration-architecture
  - agent-team-swarm
  - building-effective-agents
  - managed-agents
---

# Multi-Agent Research System (Anthropic)

A multi-agent system built by Anthropic for the Claude Research feature. Uses the orchestrator-worker pattern, where a lead agent dynamically spawns and coordinates parallel sub-agents.

## Performance

> Multi-agent system with Claude Opus 4 lead + Claude Sonnet 4 subagents **outperformed single-agent Claude Opus 4 by 90.2%** on internal research eval.

### Token Efficiency Analysis on BrowseComp

- **Token usage alone explains 80% of the variance**
- Tool call count + model selection explains 95%
- Multi-agent: consumes **15x** the tokens of a chat (economically viable only for high-value tasks)

## Architecture

```
User Query → Lead Agent  (planning & strategy)
                ├── Subagent 1  (independent search)
                ├── Subagent 2  (independent search)
                └── Subagent N  (independent search)
                          ↓
                Lead Agent  (result synthesis)
                          ↓
                CitationAgent  (citation verification)
                          ↓
                Final Answer
```

### Key Components
- **Lead Agent**: Query analysis → strategy formulation → sub-agent generation → result synthesis. Persists plans in Memory (to work around 200K token limit)
- **Subagents**: Parallel independent search. Evaluate tool results with Interleaved Thinking
- **CitationAgent**: Verifies sources for all claims
- **Memory**: Holds plans when context limit is exceeded

## Prompt Engineering Lessons

### 1. Think like your agents
Observe agents' step-by-step behavior in simulation → directly discover failure modes

### 2. Teach the orchestrator how to delegate
Each sub-agent needs: objective, output format, tool/source instructions, and clear task boundaries
""Research semiconductor shortage"" → too vague, 3 agents duplicate work

### 3. Scale effort to query complexity
- Simple fact-check: 1 agent, 3-10 tool calls
- Direct comparison: 2-4 subagents, 10-15 calls
- Complex research: 10+ subagents (clear role specialization)

### 4. Let agents improve themselves
Tool testing agent uses MCP tools dozens of times → rewrites descriptions → **40% reduction in task completion time**

### 5. Start wide, then narrow down
Start with short, broad queries and gradually narrow down (same as human expert research)

### 6. Parallel tool calling
- Lead agent: spawns 3-5 subagents in parallel
- Subagents: use 3+ tools in parallel
- **Reduces research time for complex queries by up to 90%**

## Evaluation Methodology

### LLM-as-Judge Rubric
| Dimension | Evaluation |
|------|---------|
| Factual accuracy | Do claims match sources? |
| Citation accuracy | Do citations support the claims? |
| Completeness | Are all requested aspects covered? |
| Source quality | Are primary sources used? |
| Tool efficiency | Were tools used appropriately and enough times? |

A single LLM call producing a 0.0-1.0 score with pass-fail judgment showed the highest consistency.

### Value of Human Evaluation
- Detects hallucinated answers, system failures, and subtle source selection bias
- Early: prioritized SEO-optimized content farms over academic PDFs → added source quality heuristics

## Production Reliability Challenges

- **State Management Complexity**: Minor failures derail the entire agent
- **Rainbow deployments**: Gradually migrate traffic without breaking running agents
- **Synchronous Execution Bottleneck**: Lead agent waits for sub-agent completion (room for improvement with async)

## Sub-agent Filesystem Output

> Sub-agents call tools to save artifacts to external systems, returning only lightweight references to the coordinator. Prevents the "telephone game" and avoids token copying of large outputs.

## See Also

- [[multi-agent-orchestration-architecture]] — Multi-agent orchestration patterns
- [[concepts/multi-agents/agent-team-swarm]] — Agent team/swarm architecture
- [[concepts/managed-agents]] — Managed Agents platform
- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
- [[concepts/eval-awareness-browsecomp]] — BrowseComp eval awareness
