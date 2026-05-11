---
title: "Agent Memory Engineering"
created: 2026-05-11
updated: 2026-05-11
type: concept
status: L2
tags: [agent-memory, memory-systems, harness-engineering, claude-code, codex, agents]
aliases: ["Agent Memory", "Memory Layer Design"]
sources: [raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering.md]
related: [entities/nicolas-bustamante, concepts/harness-engineering, concepts/model-harness-fit]
---

# Agent Memory Engineering

The discipline of designing how AI coding agents remember user preferences, learned workflows, and session history across invocations. Coined and comprehensively analyzed by Nicolas Bustamante (Microsoft, ex-Fintool CEO) in May 2026.

## Core Insight

> **Models are post-trained on their harness.** Claude was post-trained against Claude Code's memory layer. GPT-5 was post-trained against Codex's memory layer. The model's instinct for "remember this for next time" is shaped by the exact UI it saw during post-training.

This means memory is not portable between harnesses. A user with 64 well-loved memory entries built against Claude Code cannot drop them into Codex and expect the same behavior — the bytes land but the behavior differs.

## The Winning Architecture: Simple Won

Every clever architecture lost to **LLM + markdown + bash tool**:

| Architecture | Example | Verdict |
|-------------|---------|---------|
| Vector DB + semantic retrieval | Early memory startups | Lost — retrieval noise, stale embeddings |
| Knowledge graphs | Dedicated memory agents | Lost — maintenance overhead, fragile schemas |
| **Markdown files + bash tool** | Claude Code, Codex, Hermes | **Won** — simple, debuggable, model-native |

The interesting question is not "what data structure" but **"what discipline does the agent follow when reading and writing it."**

## Three Memory Architectures

### 1. Bounded Snapshot (Hermes)
- Memory snapshot frozen at session start
- Optimized for **prefix cache** — all memory bytes are in the first prompt
- Trade-off: cannot update memory mid-session, stale if user edits files between sessions

### 2. Two-Phase Async Pipeline
- **Phase 1 (extract)**: Cron job runs a small model to extract memory-worthy events
- **Phase 2 (consolidate)**: Big model synthesizes into structured memory
- Advantage: separation of concerns, batch processing
- Disadvantage: latency between event and memory update

### 3. Typed Live Writes (Claude Code)
- Agent writes typed markdown files directly during session
- `MEMORY.md` index always loaded
- Age-aware `<system-reminder>` wrapping on every file read
- Most sophisticated model-native approach

## Storage Layer Comparison

| Dimension | Claude Code | Codex CLI | Hermes |
|-----------|------------|-----------|--------|
| **Format** | Typed markdown files | Strict block schema + YAML frontmatter | Snapshot markdown |
| **Index** | `MEMORY.md` always loaded | `memory_summary.md` always loaded | Frozen at session start |
| **Write discipline** | Live writes during session | Task-group block format | External (cron/manual) |
| **Age tracking** | `<system-reminder>` age warnings | Implicit via timestamps | Snapshot timestamp |
| **Verification** | Age warning on every read | Citation blocks (`<oai-mem-citation>`) | N/A (frozen) |

## Key Design Questions

Bustamante identifies five questions every memory system must answer:

1. **Storage Format**: Typed files? Block schema? Snapshot?
2. **Load Strategy**: Always-load index? On-demand grep? Frozen snapshot?
3. **Write Discipline**: Live writes? Async pipeline? Manual?
4. **The Signal Gate**: When should the agent NOT remember? (Preventing memory pollution)
5. **Cold Start**: Day 1 bootstrap — what does a new user's memory look like? (Unsolved)

## The Signal Gate

One of the most important but least discussed aspects. Without a signal gate, the agent remembers every interaction — polluting memory with one-off queries, failed experiments, and noise. Claude Code's approach: prefix cache optimization means frequently-used memories survive; infrequent ones naturally decay.

## Memory Limits and Eviction

| Harness | Strategy |
|---------|----------|
| Claude Code | No hard cap — age-aware, natural decay |
| Codex | Character cap on `memory_summary.md` |
| Hermes | Snapshot size bounded by context window |

## Verification Discipline

Claude Code wraps every memory file read with an age warning in `<system-reminder>` — e.g., "This memory is 23 days old. Verify before applying." This creates a discipline where the model knows to treat older memories with appropriate skepticism.

## The Day 1 Bootstrap Problem

**Nobody has solved the cold start problem.** A new agent has zero memory. The user must manually bootstrap — write CLAUDE.md, AGENTS.md, configure rules. There's no standard for "initialize my agent from my GitHub activity, past PRs, and Slack history." This is Bustamante's identified frontier.

## Key Quotes

> "Memory is the layer where the model and the harness fuse, and once that fusion is cooked into your daily flow, going back is unbearable."

> "With memory, I outsource the persona of 'what the user wants' to the agent. Without memory, I am the persona, every single turn, forever."

> "Every clever architecture lost. The simple thing won. LLM plus markdown plus a bash tool."

## See Also
- [[entities/nicolas-bustamante]]
- [[concepts/harness-engineering]]
- [[concepts/model-harness-fit]]
- [[concepts/claude-md-rules]]
- [[concepts/memory-systems]]
