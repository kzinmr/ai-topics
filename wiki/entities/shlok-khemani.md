---
title: Shlok Khemani
type: entity
entity_type: person
status: L2
created: 2026-04-13
updated: 2026-04-13
sources:
  - https://www.shloked.com/
  - https://www.shloked.com/writing/chatgpt-memory-bitter-lesson
  - https://www.shloked.com/writing/claude-memory
  - https://www.shloked.com/writing/claude-memory-tool
  - https://www.shloked.com/writing/claude-code-source-patterns
  - https://www.shloked.com/writing/openpoke
  - https://www.shloked.com/writing/vajra
  - https://github.com/shlokkhemani
tags:
  - person
  - ai-agents
  - coding-agents
  - prompt-engineering
  - memory-systems
  - background-agents
  - multi-agent-orchestration
  - personal-ai
---


# Shlok Khemani

Writer and programmer based in Gurgaon, India. Currently researching **personal AI** and **memory systems for AI agents**. Previously at Decentralised.co, building products for the crypto space. Author of **OpenPoke** (open-source multi-agent assistant), **Vajra** (background coding agent), and the widely-read **ChatGPT Memory reverse-engineering** analysis.

## Bio

Shlok Khemani works at the intersection of AI agent architecture and practical developer tooling. His writing focuses on the engineering of personal AI assistants — how agents should remember, orchestrate, and execute tasks autonomously. Unlike researchers who work at the model level, Khemani operates at the **application layer**: he reverse-engineers existing AI products (ChatGPT Memory, Poke's architecture, Claude Code internals) and publishes both analysis and open-source implementations.

## Timeline

| Period | Activity | Key Events |
|--------|----------|------------|
| Pre-2025 | Decentralised.co | Built products for the crypto space; wrote stories |
| ~2023 | STREAKS | Created blockchain accountability tool |
| ~2024 | Sentient Market | Community tool tracking Crypto×AI intersection (70k+ users) |
| Sep 2025 | Claude Memory analysis | Published "Claude Memory: A Different Philosophy" vs. ChatGPT's approach |
| Sep 2025 | OpenPoke | Open-sourced Poke multi-agent architecture replica (465+ GitHub stars) |
| Sep 2025 | ChatGPT Memory reverse-engineering | "ChatGPT Memory and the Bitter Lesson" — widely cited analysis |
| Oct 2025 | Anthropic Memory Bet | Analysis of Anthropic's opinionated approach to AI memory |
| Nov 2025 | Google Memory critique | "Google Has Your Data. Gemini Barely Uses It." |
| 2025 | Claude Memory Tools | Published reference implementations for Claude's Memory API (53 stars) |
| Apr 2026 | Vajra | Open-sourced background coding agent with graph-based workflows |
| Apr 2026 | Claude Code source analysis | "What I Found Interesting in Claude Code's Source" |
| Apr 2026 | Conjure | Headless AI agents from terminal — skill for Codex, Claude Code, and pi |

## Core Ideas

### The Bitter Lesson Applied to AI Memory
> "The bitter lesson strikes again. While others build sophisticated scaffolding around models, OpenAI is betting that stronger models with more compute will obviate the need for clever engineering."

Khemani's analysis of ChatGPT Memory identified a deliberate architectural choice: **no RAG, no vector DBs, no knowledge graphs**. Instead, all memory is injected directly into the context window. This reflects Rich Sutton's Bitter Lesson — that raw scale and model capability eventually outperform hand-engineered solutions.

**ChatGPT's 4 Memory Layers:**

| Layer | Function | LLM Training Equivalent |
|-------|----------|------------------------|
| **User Knowledge Memories** | Dense AI-generated user profiles | Pretrained Base Model |
| **Model Set Context** | Explicit user corrections/facts | RLHF |
| **Recent Conversation Context** | ~40 most recent conversations | In-Context Learning |
| **Interaction Metadata** | Environmental/usage data | System Defaults |

His insight: users are essentially **curating their own training data** and providing RLHF-style corrections to a personal model.

### Filesystem-First Memory (Claude vs. ChatGPT)
Khemani contrasts two philosophies:

- **ChatGPT**: Hidden, opaque memory profiles managed by the platform
- **Claude**: File-based memory (CLAUDE.md, `.agent/` directories) where the user has full visibility and control

He argues Claude's approach is superior for developers because:
1. **Version control** — Git provides native diffing, branching, and history
2. **Transparency** — You can see exactly what the agent knows
3. **Portability** — Files move between environments; vector DBs don't

> "Every design decision in agent codebases should be evaluated through: 'does this invalidate the prompt cache?'"

### Multi-Agent Orchestration Architecture (OpenPoke)
From reverse-engineering Poke's system prompts, Khemani identified a critical design pattern: **personality separated from execution**.

- **Interaction Agent**: The conductor — maintains personality, context, and delegates work
- **Execution Agents**: Specialized LLM instances with their own prompts, history, and toolsets
- **Background Workers**: Continuously monitor inboxes, calendars, and external services

> "Most AI agents conflate personality with task completion—a single agent trying to be charming while also managing complex workflows. Poke separates these completely."

This insight became the basis for **OpenPoke** (465+ GitHub stars) — a stripped-down, locally-runnable implementation that mirrors Poke's email triage and reminder automation.

### Background Coding Agents (Vajra)
Vajra represents Khemani's practical implementation of **asynchronous agent workflows** for software development:

- **Graph-based workflows** using Graphviz DOT syntax
- **Linear integration** for issue tracking and PR automation
- **Filesystem-only architecture** — state persists in files, not proprietary databases
- **Background execution** — agents work on well-scoped async tasks while the developer focuses elsewhere

His observation: production background agents are already delivering measurable PR velocity at companies like Coinbase, Ramp, and Stripe.

### Cache-First Engineering
> "Every design decision in agent codebases should be evaluated through: 'does this invalidate the prompt cache?'"

Khemani's analysis of Claude Code's source code revealed a **cache-first architecture** where prompt composition, context compression, and fork primitives are all optimized around preserving the LLM's cached context. This has major cost and latency implications for agent development.

### Why Cognition Copied Claude's Memory
When Cognition released their memory tool, Khemani analyzed it and found they had essentially replicated Anthropic's approach:

- Same context management patterns
- Same filesystem-based state persistence
- Same rejection of proprietary vector stores

This validated his thesis that **file-based memory is the natural architecture for developer-facing AI agents**.

## Contributions

| Project | Description | Stars |
|---------|-------------|-------|
| **OpenPoke** | Multi-agent assistant with email triage, reminders, persistent agents | 465 |
| **Claude Memory Tools** | Reference implementations of Claude's Memory Tool API | 53 |
| **Vajra** | Background coding agent with graph-based workflows | — |
| **ChatFerry** | Terminal client for ChatGPT and Claude (no API keys, | 3 |
| **Conjure** | Headless AI agents from terminal | 3 |
| **Sentient Market** | Crypto×AI community tracking tool | 70k+ users |
| **STREAKS** | Blockchain accountability commitments | — |

## Writing (Selected 2025-2026)

| Date | Title | Key Themes |
|------|-------|------------|
| 2026-04-13 | What I Found Interesting in Claude Code's Source | Prompt composition, cache-first, context compression, fork primitives |
| 2026-04-12 | Why Cognition is Copying Claude's Memory | Memory tool analysis, context management, agentic engineering |
| 2026-04-12 | Claude's Memory | File-based memory, CLAUDE.md, filesystem as single source of truth |
| 2026-04-09 | ChatGPT's Memory Problem | Ephemeral memory, Bitter Lesson, stateless agents |
| 2026-04-06 | Open-Sourcing Vajra | Graph workflows, Linear integration, background agents |
| 2025-11-19 | Google Has Your Data. Gemini Barely Uses It. | Google's unused data advantage |
| 2025-10-14 | Anthropic's Opinionated Memory Bet | Anthropic's file-based memory philosophy |
| 2025-09-22 | OpenPoke: Recreating Poke's Architecture | Multi-agent orchestration, personality/execution separation |
| 2025-09-11 | Claude Memory: A Different Philosophy | File-based vs. hidden memory approaches |

## Philosophy

1. **Personality ≠ Execution** — Separate the agent's "voice" from its work
2. **Filesystem over Database** — Git-native version control beats proprietary vector stores
3. **Cache-First Design** — Every agent decision should optimize for prompt cache preservation
4. **Background Execution** — Well-scoped async agents are already production-ready
5. **Transparency over Opacity** — Users should see and control what agents remember

## Related

- [[peter-steinberger]] — Also builds personal AI agents (OpenClaw/Claudbot)
- [[claude-memory]] — File-based memory architecture
- [[chatgpt-memory-bitter-lesson]] — ChatGPT's memory system analysis
- [[multi-agent-orchestration]] — Patterns for coordinating multiple agents
-  — Async agent workflows
-  — Optimizing for prompt cache preservation
- [[concepts/harness-engineering/agentic-workflows/vibe-coding.md]] — The approach Khemani's work supports and critiques
- [[anthropic]] — Creator of Claude, Claude Code, and the memory philosophy Khemani analyzes
