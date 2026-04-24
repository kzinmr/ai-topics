---
title: "Cognition's Memory Tool — Copying Claude's Approach"
type: concept
status: draft
created: 2026-04-13
source: "https://www.shloked.com/writing/claude-memory-tool"
author: "Shlok Khemani"
tags: [cognition, devin, memory-tool, claude-code, competitive-analysis, context-management]
related: [claude-memory, claude-code-source-patterns, agentic-engineering]
sources: []
---

# Why Cognition is Copying Claude's Memory Tool

Analysis of how Cognition (makers of Devin) is adopting Claude's memory approach — and what this reveals about competitive dynamics in the coding agent space.

## The Core Observation

Cognition is implementing a **memory tool** that closely mirrors Claude's file-based memory system. This is notable because:

1. **Validation of approach**: A major competitor is copying, not innovating differently
2. **Convergence on filesystem**: Industry moving toward file-based context management
3. **Implicit admission**: Their previous approach wasn't working

## What Cognition is Copying

| Claude Feature | Cognition's Implementation |
|----------------|---------------------------|
| **CLAUDE.md** | Similar markdown-based project context files |
| **File system as memory** | Reading/writing to project files for persistence |
| **Human-editable context** | Transparent, version-controlled memory |
| **Auto-discovery** | Scanning project root for context files |

## What Cognition is Doing Differently

- **Memory tool API**: Explicit tool call vs. Claude's auto-discovery
- **Integration with Devin's workflow**: Tied to their specific agent architecture
- **Competitive positioning**: Framed as innovation, not emulation

## Why This Matters for the Industry

### Convergence on Best Practices

The fact that Cognition is copying suggests:
- **File-based memory is winning** over database/vector store approaches
- **Transparency matters** — users want to see and edit agent memory
- **Git integration is essential** — version control for agent context

### Competitive Dynamics

- Cognition raised significant funding but is now following Anthropic's design
- Suggests **Anthropic has the superior architecture** for coding agent memory
- May indicate Cognition's previous approach had fundamental limitations

## Implications for Agentic Engineering

1. **Standardization likely**: File-based memory may become industry standard
2. **Tool convergence**: Memory tools will look increasingly similar
3. **Focus shifts**: From "how to store memory" to "how to use memory effectively"

## Sources

- [Why Cognition is Copying Claude's Memory](https://www.shloked.com/writing/claude-memory-tool) — Shlok Khemani, April 12, 2026

## See Also

- [[concepts/_index.md]]
- [[concepts/ai-agent-memory-middleware.md]]
- [[concepts/memory-systems-design-patterns.md]]
- [[concepts/knowledge-graph-memory-agents.md]]
- [[concepts/ai-agent-memory-two-camps.md]]
