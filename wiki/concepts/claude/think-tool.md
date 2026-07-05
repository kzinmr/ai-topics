---
title: "Claude Think Tool"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - anthropic
  - tool
  - architecture
  - reasoning
  - evaluation
aliases:
  - think tool
  - Claude think tool
  - stop-and-think tool
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_claude-think-tool.md
  - https://www.anthropic.com/engineering/claude-think-tool
related:
  - claude-code
  - agent-skills
  - advanced-tool-use
---

# Claude Think Tool

Claude's "think" tool provides a dedicated space for structured thinking during complex tasks. In long tool-call chains or multi-step conversations, it allows Claude to process external information and stop to think before the next action.

## Comparison with Extended Thinking

| | Think Tool | Extended Thinking |
|---|---|---|
| **Timing** | **During** response generation (between tool calls) | **Before** response generation |
| **Target** | Processing external information (tool results) | Deep reasoning from a query alone |
| **Reasoning Depth** | Lightweight reasoning focused on new information | Comprehensive, deep pre-consideration |
| **Best For** | Complex tool chains, policy-focused environments | Coding, math, physics (non-tool) |

## Implementation

```json
{
  "name": "think",
  "description": "Use the tool to think about something...",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

It is built into the τ-Bench standard environment.

## Benchmark Results (τ-Bench)

**Evaluation metric**: pass^k (average across tasks of the probability that all k independent trials succeed) — measures consistency and reliability.

### Airline Domain (Claude 3.7 Sonnet)

| Setting | pass^1 | pass^2 | pass^3 |
|------|--------|--------|--------|
| Baseline | 0.332 | 0.206 | - |
| Extended Thinking | 0.412 | 0.290 | 0.232 |
| Think Tool | 0.404 | 0.254 | 0.186 |
| **Think Tool + Optimized Prompt** | **0.584** | **0.444** | **0.384** |

- Think tool + optimized prompt achieves **+54% over baseline**
- Standalone performance matches Extended Thinking

### Retail Domain

- Think tool standalone: 0.812 vs Baseline 0.783

## Recommended Use Cases

- **Complex tool calls**: When long tool chains require analyzing each result
- **Policy-focused environments**: Scenarios requiring consistent adherence to detailed guidelines (customer service, etc.)
- **Sequential decision-making**: When each step depends on the previous one and mistakes are costly

## Current Status

As of December 2025, Anthropic recommends using Extended Thinking over the think tool in most cases, due to improvements in Extended Thinking. However, the think tool retains its advantage in scenarios requiring sequential processing of tool results.

## See Also

- [[entities/claude-code]] — Claude Code agent harness
- [[concepts/agent-skills]] — Equipping agents with skills
- [[concepts/advanced-tool-use]] — Advanced tool use patterns
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
