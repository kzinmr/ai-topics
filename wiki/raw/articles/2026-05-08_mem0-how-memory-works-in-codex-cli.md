---
title: "How Memory Works in Codex CLI"
source: https://mem0.ai/blog/how-memory-works-in-codex-cli
author: Himanshu Sangshetti
author_handle: himanshutwtxs
date: 2026-05-08
scraped: 2026-05-14
type: raw_article
x_bookmark_id: "2054580022049198513"
x_article_id: "2054562106515804160"
tags: [codex, agent-memory, memory-systems, openai, agents, coding-agents]
---

# How Memory Works in Codex CLI

Himanshu Sangshetti (Mem0), May 8, 2026

## Codex's Three Surfaces

Codex is OpenAI's coding-agent product line with three surfaces in 2026:
- CLI
- IDE extension
- Cloud workspace inside ChatGPT

All share an engine and `~/.codex/` config directory.

## Two Memory Layers

### Layer 1: AGENTS.md (Static Instruction Layer)
- Cross-tool convention adopted by Codex, Cursor, Aider, Jules
- Spec now under Linux Foundation's Agentic AI Foundation (agents.md)
- Three-level hierarchy: Global (`~/.codex/AGENTS.md`) → Project walk (root to cwd) → Override files
- Size cap: 32 KiB (roughly 8,000 tokens)
- User-maintained, not agent-editable

### Layer 2: Memories (Generated Layer)
- Codex summarizes prior sessions in background, writes to `~/.codex/memories/`
- **Async generation**: sessions must be idle ~6 hours before consolidation
- **Two models**: one for extraction, one for consolidation (both configurable)
- **Caps and sweeps**: 256 rollouts max, 30-day unused = pruned, 30-day unrecalled = swept
- **Rate-limit-aware**: won't run consolidation when quota is low
- **Secret redaction**: built-in scrubbing for credentials
- **Two independent switches**: generate_memories (write) and use_memories (read)
- Geographic constraint: NOT available in EEA, UK, Switzerland at launch

## Inside the Pipeline

Two phases:
1. **Phase 1 (per-rollout)**: claims startup job, samples conversation against strict-schema extraction prompt, redacts secrets
2. **Phase 2 (merge)**: acquires global lock, prepares workspace, runs consolidation sub-agent, writes diff

Storage format: **markdown files**:
- `memory_summary.md` — consolidated view read at session start
- `MEMORY.md` — long-form merged memory file
- `raw_memories.md` — pre-consolidation extraction output
- `skills/<name>/SKILL.md` — skill-specific memories
- `rollout_summaries/<slug>.md` — per-session summaries

**Recall mechanism**: NOT vector search. Codex reads `memory_summary.md` whole (token-truncated), then instructs agent to `grep` over `MEMORY.md` for details.

## Where It Stops

- **No cross-machine sync**: `~/.codex/memories/` is local generated state
- **No team sharing**: per-user, no pooling across teammates
- **Generated state only, not editable**: user can read but hand-editing isn't the supported path
- **AGENTS.md fills gaps** for team conventions, cross-machine sharing

## Configuration Keys
- `memories.generate_memories` — allow new memories to be written
- `memories.use_memories` — inject existing memories into sessions
- `memories.disable_on_external_context` — exclude sessions with MCP/web search
- `memories.min_rate_limit_remaining_percent` — quota floor for consolidation
- `memories.extract_model` / `memories.consolidation_model` — model overrides
