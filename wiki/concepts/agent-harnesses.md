---
title: "Agent Harnesses"
type: concept
created: 2026-04-24
updated: 2026-04-24
tags: [ai-agents, agent-frameworks, rl, minimalism, browser-agents]
aliases: ["The Bitter Lesson of Agent Harnesses", "Agent Frameworks Philosophy"]
sources: []
---

# Agent Harnesses

> **Core Thesis:** The less you build in your agent framework, the more it works. All the value is in the RL'd model, not your 10,000 lines of abstractions.

## Overview

The concept of **agent harnesses** represents a philosophical shift in how AI agents should be architected. Rather than building complex orchestration layers, planning modules, and verification systems, the minimal agent harness approach argues that modern RL-trained models are so capable that most framework abstractions are unnecessary — and often harmful.

## The Bitter Lesson Applied to Agents

Rich Sutton's **Bitter Lesson** from 70 years of AI research states: *"General methods that leverage computation beat hand-crafted human knowledge every time."*

Applied to agent architecture:

- **Hand-crafted abstractions** (planning modules, output parsers, verification layers) encode developer biases, not model capabilities.
- **Compute-centric approaches** (giving the model maximum freedom via complete action spaces) consistently outperform specification-heavy designs.
- The models themselves handle more than expected — Claude Code writes AppleScript directly; GPT-4 browses complex sites without specialized tools.

## Why Traditional Frameworks Fail

| Failure Mode | Description |
|---|---|
| **Abstractions freeze assumptions** | Planning, verification, and parsing modules lock in developer mental models that don't generalize. |
| **RL breaks constraints** | Models trained on millions of examples anticipate patterns developers can't predict. Over-specification prevents them from leveraging training. |
| **Incomplete action spaces** | Frameworks fail not because models are weak, but because the available tools/actions are insufficient. |

## Minimal Agent Architecture

### The Core Loop

The entire agent reduces to a for-loop:

```python
while True:
    response = model(messages, tools)
    if response.tool_calls:
        for tc in response.tool_calls:
            messages.append(tc.execute())
    else:
        break
```

> *"An agent is just a for-loop of messages. The only state an agent should have is: keep going until the model stops calling tools."*

### Complete Action Spaces

The key insight: instead of providing narrow primitives (`click`, `type`, `scroll`), provide **raw control surfaces**:

- **Chrome DevTools Protocol (CDP)** — Direct browser control
- **Browser Extension APIs** — Permissioned state & active window access

Together they create a nearly complete action space, enabling self-correction: *"As long as in principle everything is possible, LLMs are extremely good at fixing themselves on the fly."*

## Context Management Patterns

### Ephemeral Tools

Browser state snapshots easily exceed 50KB per request. After ~10 interactions, context hits 500KB+, causing hallucinations and crashes.

**Solution:** Limit retained outputs to the last N calls. Sacrifices cache slightly to prevent context overload.

```python
@tool("Get browser state", ephemeral=3)  # Keep last 3 only
async def get_state() -> str:
    return massive_dom_and_screenshot
```

### Explicit Termination

Naive "stop when no tool calls" causes premature exits. The solution: an explicit `done()` tool.

| Mode | Termination |
|---|---|
| CLI Mode | Stops on no tool calls (quick interactions) |
| Autonomous Mode | Stops only on explicit `done()` call |

```python
@tool('Signal that the current task is complete.')
async def done(message: str) -> str:
    raise TaskComplete(message)
```

## Inversion Strategy

> Start with maximal capability, then restrict.

Rather than building guardrails and constraints first, give the LLM near-human freedom, then layer on safety/structure based on evaluation data. This inverts the traditional approach of starting narrow and gradually expanding.

## Related Concepts

- [[concepts/agent-loop-orchestration]] — Patterns for managing the agent loop
- [[concepts/harness-engineering/agentic-engineering]] — Broader agent engineering practices
- [[concepts/ai-agent-traps]] — Common pitfalls in agent development
- [[concepts/chatgpt-memory-bitter-lesson]] — Bitter Lesson applied to memory systems
- [[concepts/ai-coding-agent-criticism]] — Criticisms of current agent approaches

## Key Sources

- [The Bitter Lesson of Agent Frameworks](https://browser-use.com/posts/bitter-lesson-agent-frameworks) — Gregor Zunic, Browser Use Blog, 2026-01-16
- [agent-sdk](https://github.com/browser-use/agent-sdk) — Browser Use's minimal agent architecture SDK
- [browser-harness](https://github.com/browser-use/browser-harness) — Self-healing browser harness
-  — Scraped article digest
