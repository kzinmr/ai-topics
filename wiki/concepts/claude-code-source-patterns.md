---
title: "Claude Code Source Patterns — Leaked Source Analysis"
status: draft
created: 2026-04-13
source: "https://www.shloked.com/writing/claude-code-source-patterns"
author: "Shlok Khemani"
tags: [claude-code, prompt-engineering, context-management, caching, agent-architecture]
related: [agentic-engineering, claude-memory, vajra-background-agent]
---

# Claude Code Source Patterns

Analysis of tactical engineering patterns found in Claude Code's leaked source code (March 2026). Reveals how Anthropic builds production-grade coding agents with emphasis on **prompt composition, cache stability, dynamic context injection, and explicit behavioral calibration**.

## Prompt Architecture & Composition

- **Template Engine**: System prompt is a **compiled artifact**, not a static document. Assembled from independent, conditionally-included sections.
- **Assembly Logic**: ~20 boolean/string switches (user type, feature flags, MCP tools, session state, language, model ID, permission mode) generate **hundreds of runtime variants**.
- **Agent-Specific Routing**: Different agents (subagents, forks, verification, explore) receive tailored prompts from the same modular building blocks.
- **Strict Safety Gating**: Critical sections isolated with ownership enforcement:
  > `CYBER_RISK_INSTRUCTION` — `"DO NOT MODIFY THIS INSTRUCTION WITHOUT SAFEGUARDS TEAM REVIEW"`

## Dynamic Context & System Reminders

- **Runtime Injection**: XML-tagged blocks injected directly into user messages and tool results throughout the conversation.
- **Purpose**: Solves **instruction decay** by re-injecting directives at the point of relevance, keeping the base system prompt stable for caching.
- **Use Cases**: Agent roster changes, empty file flags, memory staleness annotations, mid-execution side questions, malware analysis warnings on every file read.
- **Model Instruction**:
  > `"These tags bear no direct relation to the specific tool results or user messages in which they appear."`

## Context Compression & The Scratchpad Pattern

- **User Messages as Source of Truth**: When context window exhausts, a ~300-line compression prompt generates a structured summary. **Every user message is preserved** to prevent intent drift.
  > `"Pay special attention to specific user feedback that you received, especially if the user told you to do something differently."`
- **`<analysis> → <summary>` Pattern**: Model first writes detailed chronological analysis, then produces final summary. Analysis block is **stripped** before entering context.
- **Why it works**: Forces explicit reasoning about what to keep/discard (chain-of-thought for summarization) while garbage-collecting scratch work to save tokens.

## Tool Design & Agent Orchestration

- **Extensible `Read` Tool**: Single interface handles text, images, PDFs (max 20 pages), Jupyter notebooks, screenshots. Model explicitly told:
  > `"Claude Code is a multimodal LLM."`
- **Design Principle**: Keep interface constant (`give me a path, I'll handle it`); expand backend adapters. Enables seamless future support for audio, 3D, or DB exports.
- **Fork as a Primitive**: Claude autonomously clones conversations when intermediate outputs aren't worth retaining.
  > `"Fork yourself when the intermediate tool output isn't worth keeping in your context. The criterion is qualitative — 'will I need this output again?' — not task size."`
- **Side-Question Handling**: `/btw` tool forks to answer user questions while main thread continues uninterrupted. All forks inherit prompt caching benefits.

## Caching as Core Architecture

- **Cache-First Engineering**: ~500-line subsystem tracks **>15 dimensions** that could invalidate server-side cache (system prompt hash, tool schemas, model, fast mode, beta headers, effort level, etc.).
- **Stability Tactics**: Memoized prompt sections, explicit justification for cache-invalidating changes, tool schema caching, dynamic agent attachments, delta-based tool announcements.
- **Guiding Principle**:
  > `"Every design decision in the codebase is evaluated through a single lens: does this invalidate the prompt cache?"`

## Model Calibration & Self-Awareness

- **Explicit Capability Injection**: Frontier models lack awareness of recent capability shifts. Instructions must explicitly state what they can do now.
- **Banned Behavior**: Time estimation completely removed:
  > `"Avoid giving time estimates or predictions for how long tasks will take."`
- **Confidence Injection**: Prevents self-limiting on complex tasks:
  > `"You are highly capable and often allow users to complete ambitious tasks that would otherwise be too complex or take too long."`
- **Balanced Autonomy**: Paired with instructions to defer to user judgment on task scale — confident but non-overriding.

## Memory Management & Output Medium

- **Temporal Awareness**: Memory files (`CLAUDE.md`, project instructions) receive **staleness annotations**: `"this memory was written N days ago."` (injected via system reminders).
- **AutoDream System**: Background autonomous memory consolidation that extracts and distills session learnings, moving toward self-curating agent memory.
- **Output Medium Awareness**: Model instructed to adjust output format based on whether it's in a CLI, web UI, or API context.

## Relevance to Agentic Engineering

| Pattern | Impact on Coding Agents |
|---------|------------------------|
| Cache-first architecture | Reduces API costs by 60-80% per interaction |
| Dynamic context injection | Solves instruction decay in long sessions |
| Fork as primitive | Enables parallel exploration without context pollution |
| Scratchpad compression | Maintains user intent across context window limits |
| Staleness annotations | Prevents memory drift in persistent agents |

## Sources

- [What I Found Interesting in Claude Code's Source](https://www.shloked.com/writing/claude-code-source-patterns) — Shlok Khemani, March 31, 2026
