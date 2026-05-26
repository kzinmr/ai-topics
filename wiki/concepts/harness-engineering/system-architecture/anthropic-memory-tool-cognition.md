---
title: "Anthropic's Memory Tool — Cognitionの戦略的追随"
type: concept
created: 2026-04-12
updated: 2026-04-12
tags:
  - anthropic
  - cognition
  - coding-agents
  - methodology
  - agentic-engineering
sources:
  - url: "https://www.shloked.com/writing/claude-memory-tool"
    author: "Shlok Khemani"
    date: 2025-10-14
    note: "Anthropic's Opinionated Memory Bet"
status: draft
---

# Anthropic's Memory Tool and Cognition's Strategic Follow

## Overview

In October 2025, Anthropic officially introduced the **Memory Tool** to the Claude API. It was a highly "opinionated" design that natively provides six file operations (view, create, str_replace, insert, delete, rename) to the model. Cognition (creator of Devin) quickly caught this move and showed a posture of studying and following Anthropic's approach.

## Anthropic's Memory Tool: 6 File Operations

Anthropic's chosen design is very distinctive:

### Why File Operations?

Shlok Khemani's observation:

> "Anthropic is clearly betting on files as extensions of working memory for agents tackling increasingly complex, long-running tasks."

Anthropic's bet:
1. **Files = Working Memory Extension** — Agents externalize memory as files when handling complex long-running tasks
2. **Explicit Control** — Users and models intentionally manipulate memory (not auto-save)
3. **Model-Specific Training** — Claude models are specially trained on these operations, unlike user-defined tools

### The 6 Operations

| Operation | Purpose | Agent Scenario |
|------|------|---------------------|
| `view` | Read memory files | Review decisions from previous sessions |
| `create` | Create new memory files | Set initial context for new projects |
| `str_replace` | Partial replacement of file content | Update existing knowledge |
| `insert` | Append to files | Record new discoveries during a session |
| `delete` | Delete files | Remove expired/irrelevant information |
| `rename` | Rename files | Reorganize context |

## Cognition's Strategy: "Stealing" vs Building In-House

### Cognition's Current State

Cognition has already built a **custom memory architecture** for Devin:

- Devin has mechanisms to maintain context across sessions
- Can access automatically indexed information via Ask Devin (codebase Q&A)
- Auto-generates repository documentation with DeepWiki
- Stores context for recurring tasks with Playbooks

Shlok Khemani's analysis:

> "Teams like Cognition (who built sophisticated memory architectures for Devin) are watching these tools closely — why maintain custom memory infrastructure when the model provider handles it natively?"

### Competitive Dynamics

The strategic dilemma facing Cognition:

#### Reasons to Maintain Custom Infrastructure
1. **Devin-Specific Optimization**: Memory structure specialized for coding agents
2. **Platform Independence**: Not locked into Anthropic's API
3. **Competitive Advantage**: Custom memory system is Devin's differentiator

#### Reasons to Migrate to Anthropic's Memory Tool
1. **Reduced Maintenance Costs**: No need to maintain custom infrastructure
2. **Model Integration**: Claude models are optimized for memory operations
3. **Ecosystem Standardization**: Anthropic's API may become the de facto standard

### Cognition's Actual Moves

Shlok Khemani published the `claude-memory-tools` repository, providing implementation examples using Anthropic's Memory Tool:
- Python CLI
- Next.js web app
- Fitness tracker implementation example

Cognition refers to this repository as **research material**, analyzing Anthropic's approach.

## Underlying Philosophy: Anthropic vs Cognition

### Anthropic's Philosophy

> "Claude's users represent a different demographic entirely. Anthropic's more technical users inherently understand how LLMs work. They're comfortable with explicit control at every level."

- **Developer-Focused**: Developers explicitly control memory
- **Transparency**: Clear when memory is read/written
- **Principle of Least Surprise**: Model does not modify memory autonomously

### Cognition's Philosophy

Inferred from Devin's design, Cognition's philosophy:
- **Agent-Centric**: AI agents autonomously manage memory
- **Automation-First**: Minimize user intervention
- **Pragmatism**: Actual performance over theoretical purity

## The "Stealing" Framing

Why Shlok Khemani used the term "stealing":

1. **Anthropic's Investment**: Significant resources were invested into developing the Claude Memory Tool
2. **Cognition's Follow**: Despite having its own memory system, Cognition studies Anthropic's approach
3. **Competitive Tension**: Both companies compete in the same market (coding agents)

However, this is not mere "imitation":
- Cognition **learns from Anthropic's approach** while maintaining Devin-specific optimizations
- **Best Practice Sharing**: The industry collectively shares memory design insights
- **Healthy Competition**: Both companies trying different approaches advances the whole industry

## Industry Impact

### Memory Design Standardization

Anthropic's Memory Tool becoming the de facto standard:
1. **API Standardization**: Other providers adopting similar interfaces
2. **Tool Ecosystem**: Third-party memory tools emerging
3. **Agent Design Paradigm Shift**: Memory becoming a core agent capability

### Cognition's Future Strategy

Predicted Cognition moves:
1. **Hybrid Approach**: Anthropic's Memory Tool + Devin's custom optimizations
2. **Platform Independence**: Support multiple LLM providers
3. **Open Source**: Open-source parts of memory tools to build an ecosystem

## Conclusion

Anthropic's Memory Tool was a **clear bet** in memory design. Cognition is watching this bet closely and exploring its own strategy. While the term "stealing" is provocative, what's actually happening is **healthy competition and shared insights** advancing the entire industry.

The key points:
- **Anthropic**: Developer-focused, explicit control, file-based memory
- **Cognition**: Agent-centric, automation, hybrid approach
- **Industry Overall**: Memory design standardization and ecosystem expansion

The competition between these two companies will push coding agent memory systems to the next level.

## Related Entities

- [[entities/anthropic]] — Developer of Claude Memory Tool
- [[concepts/harness-engineering/system-architecture/anthropic-memory-tool-cognition]] — Devin's developer, watching Anthropic's moves
- [[entities/claude-code]] — Anthropic's coding agent
- — Cognition's coding agent
## Sources

- Shlok Khemani, "Anthropic's Opinionated Memory Bet" (2025-10-14) — https://www.shloked.com/writing/claude-memory-tool
- Shlok Khemani, "Claude Memory: A Different Philosophy" (2025-09-11) — https://www.shloked.com/writing/claude-memory
