---
title: "Context Compaction"
type: concept
aliases:
  - context-compaction
  - pre-compaction-flush
created: 2026-04-25
updated: 2026-05-26
tags:
  - concept
  - context-engineering
  - memory-systems
  - architecture
status: complete
sources:
  - https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive
  - https://github.com/openclaw/openclaw/blob/f99e3ddd6d6fc59173f7260c5d2ae0cffa4e30e0/docs/concepts/memory.md
---

# Context Compaction

The process by which AI agents summarize and trim old messages to free up space in the context window during extended conversations, ensuring room for new dialogue.

---

## Basic Mechanism

Context compaction operates through the following pattern:

1. Conversation reaches the context window threshold (e.g., 80%)
2. System summarizes old messages via LLM
3. Summary is injected as a "compressed representation" of context, freeing raw messages
4. Space is cleared for new messages

**Fundamental Problem**: Information not captured during compaction is **permanently lost**. To address this, some harnesses trigger memory persistence **before** compaction.

---

## Pre-Compaction Flush

An innovative approach implemented by OpenClaw. As the conversation approaches the context limit, it triggers a **silent agent turn** to prompt writing to persistent memory **before** compaction.

### Trigger Conditions

- When context usage reaches approximately 80%
- Once per compaction cycle (anti-spam)
- Skipped in read-only sandbox mode

### Behavior

- Normally **`NO_REPLY`** (passes silently if nothing important to save)
- Only writes to `memory/` or `MEMORY.md` when there is significant context
- Operates automatically without human intervention

### Design Intent

> "Compaction is inevitable. But by giving the agent one last word **before** compaction, valuable context can be rescued." — OpenClaw Memory Docs

---

## Compaction Approaches by Harness

| Harness | Compaction Method | Pre-Compaction Flush | Post-Compaction Memory |
|---|---|---|---|
| **OpenClaw** | Appends Markdown summary to `memory/` | ✅ Auto (~80% usage) | Reads today + yesterday daily logs |
| **Claude Code** | 5-layer compaction pipeline (progressive summarization) | ❌ | Reloads CLAUDE.md + MEMORY.md |
| **Codex CLI** | 2-phase async pipeline (extract → consolidate) | ❌ (unnecessary due to async generation) | Loads `memory_summary.md` |

---

## Related

- [[concepts/context-engineering/context-compression|Context Compression Techniques]] — Compression algorithms (summarization, retrieval, structural, learned) that Compaction processes use
- [[comparisons/agent-memory-systems-comparison]] — OpenClaw/Claude Code/Codex memory system comparison
- [[entities/openclaw]] — OpenClaw entity (Pre-Compaction Flush details in Memory System section)
- [[entities/claude-code--architecture]] — Claude Code 5-layer compaction pipeline
- [[concepts/claude/perfect-memory]] — Claude Code's memory design philosophy
- [[raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive]] — Original article
