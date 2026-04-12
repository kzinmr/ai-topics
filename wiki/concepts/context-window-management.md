---
title: "Context Window Management"
aliases:
  - context-engineering
  - context window management
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agent-architecture
status: L2
sources:
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/"
---

# Context Window Management

Managing the finite context window of LLMs as a critical engineering resource. Anthropic views this as the natural progression from prompt engineering to "context engineering" — curating and maintaining the optimal set of tokens during LLM inference.

## Core Problem

- Context is a **finite resource** — as context windows fill with conversation history, tool outputs, and retrieved data, model attention degrades ("context rot")
- Agents operating across multiple turns generate ever-growing data that must be cyclically refined
- The engineering challenge: find the smallest, most informative context set that produces reliable outputs

## Key Strategies

### Just-in-Time Context Loading
- Rather than pre-loading all relevant data, retrieve context dynamically at runtime
- Agents use tools to fetch data on-demand, keeping working memory lean
- Metadata (file sizes, naming conventions, timestamps) helps agents prioritize what to load

### Progressive Disclosure (Multi-Level Loading)
1. **Level 1**: Lightweight system prompt + tool metadata
2. **Level 2**: Full instructions loaded when task is identified
3. **Level 3+**: Detailed reference materials loaded only when specific sub-tasks require them

### Context Compression
- **Compaction**: Summarize conversation history while preserving key decisions and facts
- **File-native approach**: Store state in files (git history, progress logs) rather than context window
- Agents read structured files (e.g., `claude-progress.txt`) to recover context without re-reading full history

### Self-Managed Context
- Agents assemble understanding layer-by-layer, maintaining only what's necessary in working memory
- Note-taking strategies provide additional persistence beyond the context window
- Trade-off: runtime latency for token efficiency and focused attention

## Simon Willison's Perspective

> *"I've found that the biggest challenge with coding agents is context management. As the agent works on a task, the conversation grows and the model starts to lose track of earlier decisions. The solution is to write things down — use files, git commits, and progress logs as external memory."*

Willison advocates for:
- **Git commits as memory**: Each commit documents what was done and why
- **Progress files**: Explicit files tracking completed and pending work
- **CLAUDE.md pattern**: Project-level instructions that persist across sessions

## Anthropic's Guidance

> *"Our overall guidance across the different components of context (system prompts, tools, examples, message history, etc) is to be thoughtful and keep your context informative, yet tight."*

Anthropic identifies several patterns:
- **Hybrid model**: Claude Code uses `CLAUDE.md` (persistent) + dynamic retrieval (just-in-time)
- **Long-horizon tasks**: Require structured handoff mechanisms between context windows
- **Context rot**: All models exhibit degradation as context window fills; some more gracefully than others

## Practical Techniques

| Technique | Description | Use Case |
|-----------|-------------|----------|
| File-based state | Store progress in files rather than context | Long-running coding tasks |
| Structured handoff | Explicit progress logs for next session | Multi-session workflows |
| Dynamic retrieval | Load data on-demand via tools | Large codebases, databases |
| Context pruning | Remove stale/irrelevant history | Extended conversations |
| Metadata signals | Use file sizes, names, timestamps for prioritization | Initial context triage |

## Related Concepts
- [[agentic-engineering]]
- [[long-running-agents]]
- [[agent-skills]]
- [[building-effective-agents]]

## Sources
- [Effective Context Engineering for AI Agents (Anthropic)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Context Window Management (Simon Willison)](https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/)
