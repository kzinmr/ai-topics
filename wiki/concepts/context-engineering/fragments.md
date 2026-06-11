---
title: Context Fragments
type: concept
created: 2026-04-16
updated: 2026-04-16
status: active
depth: L2
tags:
  - harness-engineering
  - memory-systems
  - context-management
  - agentic-engineering
source: https://x.com/vtrivedy10/status/... (Vivek Trivedy, Apr 2026)
related:
  - harness-engineering
  - chatgpt-memory-bitter-lesson
  - claude-memory
  - ai-agent-memory-middleware
  - memory-systems-design-patterns
  - rlm-recursive-language-models
  - experiential-memory
sources: []
---

# Context Fragments

A concept proposed by Vivek Trivedy (@vtrivedy10) in April 2026. A framework that views the context window as "a collection of objects selectively loaded by the harness."

## Core Definition

> *"the context window is a precious artifact. Harnesses make decisions on how to populate, manage, edit, and organize it so agents can do work. Each loaded object can be thought of as a Context Fragment and represents an explicit decision by the user and harness designer of what needs a model needs to do work at any given time."*

### What Is a Context Fragment

Each Context Fragment:
- **Product of explicit decision-making** — an object loaded because the user or harness designer determined "this data is needed for the task"
- **Self-contained semantic unit** — files, documents, memories, tool definitions, etc.
- **Dynamically managed** — the harness adds, edits, deletes, and prioritizes them

## Origins: RLM and Externalized Objects

This idea originates from Alex Zhang's (@a1zhang) concept of "externalizing objects + loading into the context window" in [[concepts/rlm-recursive-language-models]]. RLM presents the paradigm that "language models are modules within a program, not final products," and Context Fragments is its concrete implementation.

## Harness Role

Viv's redefinition of the harness:

| Traditional harness definition | Context Fragments extension |
|-----------------|---------------------|
| Model + Tool routing | Model + Context Fragment routing + Memory retrieval |
| Managing tool calls | Which objects to load into context |
| Controlling agent behavior | "Editing, organizing, prioritizing" context |

## Relationship with Experiential Memory

> *"agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans)."*

Context Fragments are loaded into the context window as search results from **Experiential Memory** ([[concepts/experiential-memory]]). Because agents can share, fork, and accumulate memories, individual agents' experiences are reused as collective knowledge.

## Connection to The Bitter Lesson

Viv applies Rich Sutton's "Bitter Lesson" to agent memory:

- **compute leveraged search > human-curated knowledge**
- The ability to search, distill, and organize from large volumes of experiential data becomes a competitive advantage
- Open ecosystems matter — data ownership and utilization

## Open Questions

Open questions raised by Viv:

1. **Traces → Memory Primitives** — How to efficiently distill experiences (traces) into long-term memory primitives
2. **JIT Search vs Weight Integration** — Should search be just-in-time, or integrated into model weights?
3. **Self-Managing Context** — How models can self-manage their own context windows. Reducing error rates during recursive external object manipulation.

## Implementation Implications

### Harness Design

1. **Fragment selection policy** — Which objects to load
2. **Fragment lifecycle** — Add, edit, delete, compress
3. **Cross-fragment reasoning** — Reasoning across multiple fragments
4. **Error recovery** — Recovery from fragment operation failures

### Memory Architecture

- **L1: In-Context Fragments** — Objects needed for the current task
- **L2: Local Memory Store** — Fragments persisted across sessions
- **L3: Shared Memory Pool** — Accumulated memory shareable and forkable across agents

## Related Concepts

- [[concepts/harness-engineering]] — Extended version of Harness Design
- [[concepts/experiential-memory]] — Agent experience accumulation memory
- [[concepts/gpt/chatgpt-memory-bitter-lesson]] — Bitter Lesson and memory
- [[concepts/claude/memory]] — File-based memory (L2 implementation)
- [[concepts/ai-agent-memory-middleware]] — Cloud-scale memory (L3 implementation)
- [[concepts/memory-systems-design-patterns]] — Cross-cutting memory design pattern analysis
- [[concepts/rlm-recursive-language-models]] — The originating RLM/Externalized Objects
