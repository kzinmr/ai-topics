---
title: "Agent-Native Architecture"
created: 2026-05-25
updated: 2026-05-25
type: concept
tags:
  - concept
  - architecture
  - agent-design-patterns
  - agent-native
  - ai-native
  - tool
sources:
  - "raw/articles/2026-01-17_every-to_agent-native-architectures.md"
  - "https://every.to/guides/agent-native"
  - "https://every.to/source-code/the-folder-is-the-agent"
---

# Agent-Native Architecture

**Origin**: Dan Shipper (co-authored with Claude), [[entities/every-inc|Every]], January 2026

Agent-Native Architecture is a software design philosophy where **agents are first-class citizens** rather than afterthoughts. The same architecture that powers coding agents (like [[claude-code]]) can be applied to any domain — email management, file organization, content creation, and more.

## Core Thesis

> "A really good coding agent is actually a really good general-purpose agent."

The breakthrough: once LLMs with tools operating in a loop can reliably accomplish complex multi-step tasks (as demonstrated by Claude Code), the same architecture works for any domain — you just change the tools and context.

## Five Core Principles

### 1. Parity
**Whatever the user can do through the UI, the agent should achieve through tools.**

This is the foundational principle. Without parity, the agent is a second-class citizen. The discipline: every new UI capability must be accompanied by agent-accessible tools.

**Test**: Pick any UI action. Can the agent accomplish it?

### 2. Granularity
**Tools = atomic primitives. Features = outcomes achieved by agent in a loop.**

A tool is a primitive capability (read_file, search_files, write_file). A feature is an outcome described in a prompt that the agent achieves by composing tools in a loop.

**Test**: To change behavior, do you edit prompts or refactor code? In agent-native apps, it should be prompts.

### 3. Composability
**With atomic tools + parity, new features are just new prompts.**

Example "weekly review" feature:
```
"Review files modified this week. Summarize key changes.
Based on incomplete items and approaching deadlines,
suggest three priorities for next week."
```
The agent uses `list_files`, `read_file`, and its judgment. No new code needed.

### 4. Emergent Capability
**The agent accomplishes things you didn't explicitly design for.**

The flywheel:
1. Build with atomic tools and parity
2. Users request unanticipated things
3. Agent composes tools to accomplish them (or fails, revealing a gap)
4. Observe patterns in what's being requested
5. Add domain tools/prompts to make common patterns efficient
6. Repeat

**Test**: Can it handle open-ended requests in your domain?

### 5. Improvement Over Time
**Agent-native apps get better without code changes.**

Three improvement vectors:
- **Accumulated context**: State persists across sessions via context files (CLAUDE.md, memory files)
- **Developer refinement**: Ship updated prompts for all users
- **User customization**: Users modify prompts for their individual workflow

This is fundamentally different from traditional software, which only improves through code releases.

## Implementation Patterns

### Agent-to-UI Communication
How agents surface their work to humans — not as raw tool outputs, but as formatted, contextual information.

### iOS Storage Architecture
How mobile apps structure filesystem access for agent compatibility.

### Checkpoint and Resume
Agent sessions can pause and resume with full context recovery.

### Dynamic Capability Discovery
Agents discover available tools/capabilities at runtime rather than having them hardcoded.

### CRUD Completeness
Ensuring agents can Create, Read, Update, and Delete all domain entities — not just read them.

## Success Criteria

| Criterion | What It Means |
|---|---|
| UI Parity | Agent achieves anything users can through UI |
| Granularity | Tools are atomic; features are prompts |
| Composability | New features = new prompts, not code |
| Emergence | Agent handles unanticipated requests |
| Improvement | Gets better through context + refinement |

## Relationship to Other Patterns

- **[[concepts/folder-is-the-agent|Folder Is the Agent]]** — The filesystem IS the agent's context layer, implementing all five principles
- **[[concepts/compound-engineering-every|Compound Engineering]]** — The iterative improvement loop that makes agent-native apps better over time
- **[[claude-code]]** — The proof-of-concept that coding agents can be general-purpose agents
- **[[openclaw]]** — The hosted implementation of agent-native architecture

## Industry Impact

This philosophy underpins:
- Every's product suite (Spiral, Cora, Sparkle, Monologue, Proof, Plus One)
- The shift from "AI features in apps" to "apps designed for agents from the start"
- Anthropic's Claude Managed Agents (hosted sandboxing + state management)
- The broader agent-native software movement

## Related Pages
- [[entities/every-inc]] — Origin company
- [[entities/dan-shipper]] — Philosophy author
- [[concepts/folder-is-the-agent]] — Implementation pattern
- [[concepts/compound-engineering-every]] — Iterative improvement methodology
- [[claude-code]] — Proof-of-concept coding agent
- [[openclaw]] — Hosted agent platform
