---
title: "AI Memory Systems — Design Philosophy Comparison: Chat vs Coding Agents"
type: concept
created: 2026-04-12
updated: 2026-04-27
tags:
  - memory-systems
  - agentic-engineering
  - openai
  - anthropic
  - cognition
  - coding-agents
  - ai-agents
sources:
  - url: "https://www.shloked.com/writing/chatgpt-memory-bitter-lesson"
    author: "Shlok Khemani"
    date: 2026-04-12
    note: "ChatGPT's Memory isn't learning The Bitter Lesson"
  - url: "https://www.shloked.com/writing/claude-memory"
    author: "Shlok Khemani"
    date: 2026-04-12
    note: "Why Anthropic should give Claude memory"
  - url: "https://www.shloked.com/writing/claude-memory-tool"
    author: "Shlok Khemani"
    date: 2026-04-12
    note: "Cognition is trying to steal Claude Code's memory tool"
  - url: "raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md"
    author: "Alex Banks"
    date: 2026-04-26
    note: "Anthropic Managed Agents file-based memory"
status: draft
---

# AI Memory Systems — Comparative Analysis of Design Philosophy

## Overview

OpenAI's ChatGPT Memory, Anthropic's Claude Memory (in development), and Cognition's Devin Memory are each based on different design philosophies. This page compares the three approaches and explores optimal memory system design for coding agents.

## Three Approaches

### 1. OpenAI ChatGPT Memory — The "Not Learning The Bitter Lesson" Approach

Rich Sutton's "The Bitter Lesson" is a lesson from AI history: **leveraging scalable computation and learning succeeds in the long run more than hard-coding human knowledge**.

ChatGPT Memory's problems:

- **Explicit Memory**: Only stores information the user explicitly says "remember"
- **User-centric**: Remembers personal preferences, names, fragments of past conversations
- **Non-scalable**: Must manually build memory each interaction session
- **Context-unoptimized**: Low-relevance information easily contaminates memory

Shlok Khemani's observation:

> "ChatGPT's Memory is the anti-Bitter Lesson — it's trying to hard-code user preferences instead of learning from computation and search."

### 2. Anthropic Claude Memory — Agentic Working Memory

Claude's memory is designed as **agent working memory**:

- **Implicit Memory**: Automatically extracts important parts from conversations and code work
- **Project-centric**: Remembers code structure, technical decisions, dependencies
- **Scalable**: Summarization and retrieval mechanisms for efficiently managing large contexts
- **Context-optimized**: Only loads information relevant to the current task

This approach aligns with "The Bitter Lesson":
- Leverages computation (summarization algorithms) and search (relevant memory retrieval)
- Automatically learns and extracts without hard-coding human knowledge

### 3. Cognition Devin Memory — Hybrid Approach

Cognition has built a unique position between Anthropic and OpenAI:

- **Agent-specialized**: Memory structure optimized for coding tasks
- **Context anxiety resolution**: External memory prevents model over-scanning
- **Pragmatism**: Prioritizes actual performance over theoretical purity

## Analysis Through "The Bitter Lesson" Lens

### Rich Sutton's Lesson

Rich Sutton (2019): "The Bitter Lesson"
> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective."

### Contrast with ChatGPT Memory

ChatGPT Memory contradicts "The Bitter Lesson":
- **Hard-coding human knowledge**: Users explicitly say "remember this"
- **Non-scalable**: Manually built per session
- **Storage, not computation**: Simple storage rather than search or summarization algorithms

Meanwhile, Claude Memory aligns with "The Bitter Lesson":
- **Leveraging computation**: Automatic summarization, relevance scoring, search optimization
- **Scalable**: Efficiently manages large contexts
- **Learning-based**: Automatically extracts important information from user behavior patterns

## Memory Design Best Practices

### Separation of Concerns

```
┌─────────────────────────────────────┐
│           Agent Memory              │
├──────────────┬──────────────────────┤
│ Short-term   │ Long-term            │
│ (Working)    │ (Persistent)         │
│              │                      │
│ • Current    │ • Project structure  │
│   session    │ • Technical decisions│
│ • Task-      │ • User preferences   │
│   specific   │ • Past errors        │
│              │ • Solutions          │
└──────────────┴──────────────────────┘
```

### Summarization

- Store **summarized knowledge**, not raw data
- Extract only important information, eliminate noise
- Update periodically to maintain freshness

### Retrievability

- Fetch only needed information when needed
- Filter via relevance scoring
- Save context window space

### Freshness Management

- Mechanism for automatic expiration of old information
- Periodic memory inventory
- Mechanisms for correcting/deleting incorrect information

## Cognition's Strategic Positioning

Cognition combines:

1. **Learning from Anthropic**: Actually observed Claude's context anxiety problem
2. **Proprietary implementation**: Built agent-specialized memory in Devin
3. **Relationship with OpenAI**: Potential for competition/cooperation with Codex

Shlok Khemani's analysis:

> "Cognition is essentially trying to steal the best parts of both companies' approaches — Anthropic's deep technical understanding and OpenAI's product vision — and combine them into something new."

## Anthropic Managed Agents: File-Based Memory (2026-04)

The memory approach adopted by Anthropic Managed Agents breaks from traditional vector stores:

- **File-based**: Editable, exportable, auditable, version-controllable, rollback-able via API — not a black-box vector store
- **Mount path**: `/mnt/memory/<store-name>/` — directly mounted into the agent container
- **Real-time sync**: Multiple agents can simultaneously access the same memory store
- **Interpretability**: Files are human-readable, easy to share and audit

This approach fully aligns with the spirit of "The Bitter Lesson":
- Leverages general-purpose filesystem rather than specialized vector DB
- Format readable/writable by both humans and agents
- Uses computational resources (the model itself) to extract and organize needed information

### Design Philosophy Comparison (Extended)

| Aspect | ChatGPT Memory | Claude Memory (in dev) | Managed Agents Memory | Devin Memory |
|------|---------------|----------------------|---------------------|-------------|
| Storage format | Black box | Unknown | **Editable files** | Database |
| Auditability | Low | Low | **High (file audit)** | Medium |
| Export | Not possible | Unknown | **Possible via API** | Limited |
| Version control | None | None | **Git-compatible** | Internal |
| Rollback | Not possible | Unknown | **Possible via API** | Limited |
| Multi-agent sharing | Not possible | Not possible | **Real-time sync** | Limited |

## Impact on Coding Agents

### Claude Code vs Codex Memory Strategy Differences

| Aspect | Claude Code | Codex |
|------|-------------|-------|
| Memory type | Working memory (project context) | User profile |
| Optimization target | Coding performance | Conversational consistency |
| Scalability | High (auto-summarization/search) | Low (manual memory) |
| Context anxiety | Resolved (external memory) | Unresolved (relies on long context) |

### How Memory Affects Agent Design

1. **Context management**: Long context vs external memory
2. **Cross-session continuity**: Reusing past knowledge
3. **Performance**: Search efficiency and decision speed
4. **Scalability**: Handling large numbers of projects

## Conclusion

AI memory system design is not just a technical issue — it reflects an **AI philosophical approach**:

- **OpenAI**: Consumer-centric, explicit memory, conversational consistency focus
- **Anthropic**: Developer-centric, implicit memory, computational scalability focus
- **Cognition**: Pragmatic, hybrid approach, agent-specialized

Claude's memory design aligning with "The Bitter Lesson" gives it a long-term scalability advantage. That Cognition is learning from this approach and chasing it with their own implementation shows memory systems are becoming a core competitive advantage for coding agents.

## Related Entities

- [[entities/openai]] — ChatGPT memory, Codex development
- [[entities/anthropic]] — Claude Memory, Claude Code
- [[concepts/harness-engineering/system-architecture/anthropic-memory-tool-cognition]] — Devin, agent-specialized memory
-  — "The Bitter Lesson" proponent
## Sources

- Rich Sutton, "The Bitter Lesson" (2019)
- Shlok Khemani, "ChatGPT's Memory Isn't Learning the Bitter Lesson" (2026-04-12)
- Shlok Khemani, "Why Anthropic Should Give Claude Memory" (2026-04-12)
- Shlok Khemani, "Cognition is Stealing Claude Code's Memory Tool" (2026-04-12)
