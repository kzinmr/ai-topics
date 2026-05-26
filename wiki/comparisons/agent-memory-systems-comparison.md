---
title: "Agent Memory Systems Comparison — OpenClaw vs Claude Code vs Codex vs Hermes"
type: comparison
aliases:
  - agent-memory-systems-comparison
  - harness-memory-comparison
created: 2026-05-17
updated: 2026-05-26
tags:
  - concept
  - memory-systems
  - architecture
  - context-engineering
  - comparison
sources:
  - https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive
  - https://mem0.ai/blog/how-memory-works-in-codex-cli
  - https://ianlpaterson.com/blog/claude-code-memory-architecture/
  - https://www.buildfastwithai.com/blogs/claude-managed-agents-memory-2026
  - https://code.claude.com/docs/en/memory
  - https://hermes-agent.nousresearch.com/docs/
  - raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering.md
---

# Agent Memory Systems Comparison — OpenClaw vs Claude Code vs Codex vs Hermes

An architectural comparison of memory systems across four major coding agent harnesses. While all harnesses share the **Markdown file-based memory strategy** as their most important commonality, their approaches to retrieval, embedding strategy, and context retention differ significantly.

---

## Common Ground: File-First Philosophy

All four harnesses share the design philosophy that **"files are the sole source of truth":**

| Harness | Primary Storage | Human-readable? | Version-controllable? |
|---------|----------------|-----------------|----------------------|
| **OpenClaw** | `memory/*.md`, `MEMORY.md`, `sessions/*.md` | ✅ Human-readable Markdown | ✅ git-manageable |
| **Claude Code** | `CLAUDE.md`, `MEMORY.md`, `.claude/rules/*.md`, auto-memory dir | ✅ Human-readable Markdown | ✅ git-manageable |
| **Codex CLI** | `~/.codex/memories/*.md`, `AGENTS.md` | ✅ Human-readable Markdown | ✅ Only AGENTS.md git-shareable |
| **Hermes Agent** | `~/.hermes/MEMORY.md`, `USER.md`, `SOUL.md`, SQLite DB + JSONL | ✅ Human-readable Markdown + SQLite | ✅ git-manageable |

This shared philosophy suggests a **"Bitter Lesson" convergence** in AI agent memory — simple, human-readable, auditable files win over complex retrieval architectures in the long run.

**Notable**: Hermes goes a step further by separating **SOUL.md** (agent persona and behavioral guidelines) as system prompt slot #1, clearly distinguishing memory from identity.

---

## Architecture Comparison

### Memory Hierarchy

| Layer | OpenClaw | Claude Code | Codex CLI | Hermes Agent |
|-------|----------|-------------|-----------|--------------|
| **Static instructions** | None (replaced by system prompt) | `CLAUDE.md` (Global → Project → `.claude/rules/*.md`) | `AGENTS.md` (Global → Project walk → Override, max 32KiB) | `SOUL.md` (slot #1, persona & behavioral guidelines) |
| **Persistent memory** | `MEMORY.md` (private sessions only) | `MEMORY.md` (always loaded) + auto-memory dir | `~/.codex/memories/MEMORY.md` | `MEMORY.md` (2,200 chars max) + `USER.md` (1,375 chars max) — **frozen snapshot** at session start |
| **Daily/temporal memory** | `memory/YYYY-MM-DD.md` (today + yesterday loaded) | None (session-only context) | `rollout_summaries/<slug>.md` (per session) | None (bounded snapshot model eliminates need for daily log separation) |
| **Conversation history** | `sessions/YYYY-MM-DD-<slug>.md` (full-text searchable, indexable) | Indirectly via CLAUDE.md | `memory_summary.md` (summary only) | SQLite FTS5 + JSONL (full-text search, summarization, retrieval) |
| **External memory** | ❌ | ❌ | ❌ | ✅ **8 pluggable providers** (Honcho etc.), only 1 active at a time |
| **Procedural memory** | ❌ | ❌ | ✅ `skills/<name>/SKILL.md` (Codex per-skill memory) | ✅ **Self-Evolving Skills** (`~/.hermes/skills/`, auto-generated + Curator-maintained) |

### Retrieval & Recall Methods

| Method | OpenClaw | Claude Code | Codex CLI | Hermes Agent |
|--------|----------|-------------|-----------|--------------|
| **Vector search** | ✅ sqlite-vec + cosine similarity | ❌ | ❌ | ❌ |
| **Full-text search** | ✅ SQLite FTS5 (BM25) | ❌ (direct file loading) | ✅ `grep`-based (grep MEMORY.md) | ✅ SQLite FTS5 (full conversation history search) |
| **Hybrid search** | ✅ BM25 + vector (70:30 weighting) | ❌ | ❌ | ❌ |
| **Recall method** | `memory_search` tool (~700 char snippets + relevance scores) | Full file loading | Full `memory_summary.md` load → `grep` as needed | **session_search** tool (SQLite FTS5 → LLM summary) + MEMORY.md injected every session |
| **Progressive Disclosure** | ❌ snippet-based | ❌ full file load | ❌ full file load | ✅ **3-level** (name only → full content → reference files) |

**Biggest difference**: Only OpenClaw implements vector search. Hermes and OpenClaw share FTS5 full-text search, but Hermes specializes in conversation history search while OpenClaw uses hybrid search across memory files + sessions.

### Embedding Strategy

| Item | OpenClaw | Claude Code | Codex CLI | Hermes Agent |
|------|----------|-------------|-----------|--------------|
| **Uses embeddings** | ✅ Yes (for search) | ❌ No | ❌ No | ❌ No (FTS5 only) |
| **Provider** | Local → OpenAI → Gemini auto-fallback | N/A | N/A | N/A (can be covered by external providers) |
| **Cache** | ✅ SHA-256 hash based | N/A | N/A | N/A |
| **Batch optimization** | ✅ OpenAI/Gemini Batch API (50% cost reduction) | N/A | N/A | N/A |

### Memory Generation & Updates

| Item | OpenClaw | Claude Code | Codex CLI | Hermes Agent |
|------|----------|-------------|-----------|--------------|
| **Generation timing** | Pre-compaction flush (auto) + user instruction | User instruction / manual CLAUDE.md update | Async background (~6 hours idle) | **Agent-driven**: After complex tasks (5+ tool calls), error breakthroughs, user corrections |
| **Generation model** | Running agent model | Running agent model | Dedicated extraction model + integration model (independently configurable) | Running agent model |
| **Auto-summary** | ✅ Triggered automatically during compaction | ❌ Manual instruction only | ✅ Session summary → periodic integration | ✅ **Auto-consolidation at ~80% capacity** (densely integrates related facts) |
| **Limits & pruning** | Unlimited (filesystem capacity dependent) | Unlimited (filesystem capacity dependent) | 256 rollout limit / 30 days unused → deleted | **Capacity limited** (MEMORY.md 2,200 chars / USER.md 1,375 chars) + **Curator** (30 days stale / 90 days archive) |
| **Sensitive info removal** | ❌ | ❌ | ✅ Built-in credential scrubbing | ❌ |
| **External verification** | ❌ | ❌ | ❌ | ✅ **GEPA** (offline optimization pipeline, via PR) |

### Context Retention & Compaction

| Item | OpenClaw | Claude Code | Codex CLI | Hermes Agent |
|------|----------|-------------|-----------|--------------|
| **Pre-compaction flush** | ✅ Auto (~80% context usage, silent turn) | ❌ (5-layer compaction pipeline but no pre-flush) | ❌ (not directly relevant due to async generation) | ✅ **Pre-compression memory flush** (flushes memory before context compression) |
| **Compaction method** | Appends Markdown summary to `memory/` | 5-layer pipeline (gradual summarization) | Extraction → integration 2-phase pipeline | Bounded snapshot + FTS5 search (triggers new skill generation and memory update after compression) |
| **Context injection** | Today + yesterday daily logs + search results | CLAUDE.md + MEMORY.md injected every session | `memory_summary.md` injected every session (token truncated) | MEMORY.md + USER.md frozen snapshot (**prefix cache optimized** — all memory bytes in the initial prompt) |

---

## Selection Guide: Which Memory System to Choose

### Best for OpenClaw

- **Long-running agents**: Daily logs + session history auto-accumulation ideal for multi-month projects
- **Advanced search needed**: Vector search for concept matching, BM25 for precise term search
- **Offline requirements**: Local embedding provider enables fully offline operation
- **Multi-agent**: Per-agent isolation prevents cross-agent memory contamination

### Best for Claude Code

- **Team development**: Git-managed CLAUDE.md enables team-wide memory sharing
- **Simplicity focused**: Direct file loading requires no complex search infrastructure
- **Session-based work**: Better suited for focused single-task execution than long-term projects
- **Enterprise management**: Integration with Managed Agents lifecycle management

### Best for Codex CLI

- **Automated memory management**: Async generation enables "set and forget" operation
- **Skill-based memory**: Independent memory files per skill
- **Cost management**: Rate-limit aware, usage-based integration suppression
- **Privacy focused**: Built-in credential scrubbing + geographic constraints

### Best for Hermes Agent

- **Self-evolving agent**: Closed-loop learning where skills and memory accumulate with use
- **Prefix cache optimization needed**: Bounded snapshot (MEMORY.md + USER.md) ensures all memory fits in the initial prompt, maximizing cache efficiency
- **Procedural knowledge accumulation**: Recurring workflow that auto-generates skills from complex tasks for reuse
- **Curator-driven autonomous maintenance**: Auto-inventory with 30-day stale / 90-day archive
- **Multi-profile isolation**: Completely separated memory, skills, and config per profile

---

## Design Philosophy Comparison

| Axis | OpenClaw | Claude Code | Codex CLI | Hermes Agent |
|------|----------|-------------|-----------|--------------|
| **Philosophy** | "Files are truth, search is intelligence" — leverages memory through hybrid search | "Simplicity is power" — removes unnecessary infrastructure, trusts model intelligence | "Automation is key" — humans set up, agents manage autonomously | "Smarter with use" — Capability Accumulation System, closed-loop learning |
| **Complexity** | High (vector DB + FTS + provider management) | Low (filesystem only) | Medium (async pipeline + dedicated models) | Medium (3-Tier + Curator + GEPA, but transparent to users) |
| **Operational burden** | Medium (SQLite management needed) | Low (file editing only) | Low (automated, with limits and pruning) | Low (Curator auto-maintenance + GEPA auto-optimization) |
| **Scalability** | High (search handles large memory) | Limited (depends on full file loading) | Medium (256 rollout limit, periodic pruning) | **Bounded**: Intentionally limited (2,200 chars) — precision over scale |
| **Portability** | High (Markdown files + SQLite) | High (Markdown files only) | Medium (depends on `~/.codex/`, no cross-machine sync) | High (Markdown + SQLite + JSONL, though model-dependent) |
| **Prefix Cache efficiency** | Medium (search results vary per turn) | Low (full file load introduces variability) | Low (summary regenerated every session) | **Highest** — all memory bytes in initial prompt, maximum cache hit rate |

---

## Memory Architecture Classification (Bustamante)

Mapping Nicolas Bustamante's (Microsoft) 3-type classification to the four harnesses:

| Architecture Type | Harness | Characteristics |
|------------------|---------|-----------------|
| **Bounded Snapshot** | **Hermes Agent** | Memory frozen at session start, prefix cache optimized, capacity-limited |
| **Typed Live Writes** | **Claude Code** | Directly writes typed Markdown during session, age-aware reminders |
| **Two-Phase Async Pipeline** | **Codex CLI** | Async 2-phase: extraction (small model) → integration (large model) |
| **Hybrid Search + Flush** | **OpenClaw** | Doesn't fully fit any of the above 3 types — hybrid search + Pre-Compaction Flush unique path |

---

## Common Limitations

Constraints shared by all four harnesses:

1. **Lack of cross-file context**: Concepts spanning multiple files are not connected without explicit cross-references
2. **Embedding drift**: Provider changes require reindexing (OpenClaw has tracking mechanism, others N/A)
3. **Storage growth**: Long-term use leads to linear increase in file count and index size (Hermes mitigates with bounded design)
4. **Multi-machine sync**: None have built-in cross-machine sync mechanisms (Codex explicitly states "none")
5. **Model dependence**: Bustamante notes — "models are post-trained on their harness," making memory behavior non-portable between harnesses

---

## Related

- [[entities/openclaw]] — OpenClaw entity page (with Memory System section)
- [[entities/claude-code]] — Claude Code entity page
- [[entities/claude-code--architecture]] — Claude Code 5-layer architecture details
- [[entities/hermes-agent]] — Hermes Agent entity page
- [[concepts/hermes-agent]] — Hermes Agent 3-Tier Memory System details
- [[concepts/hermes-agent-architecture]] — Hermes Agent architecture (Prompt Assembly, Persistent State)
- [[concepts/claude-perfect-memory]] — Claude Code file-based memory design philosophy
- [[concepts/agent-memory-engineering]] — Nicolas Bustamante's 3-type classification
- [[raw/articles/2026-05-08_mem0-how-memory-works-in-codex-cli]] — Codex CLI memory details
- [[raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive]] — OpenClaw memory details
- [[raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering]] — Bustamante primary source
- [[concepts/ai-memory-systems]] — ChatGPT vs Claude vs Cognition memory comparison
- [[concepts/context-compaction]] — Context compaction concept
- [[concepts/harness-engineering/system-architecture/ai-memory-systems]] — AI memory systems overview
- [[concepts/agent-harness-comparison]] — 9-harness comprehensive comparison
- [[comparisons/hermes-vs-openclaw-architecture]] — Hermes vs OpenClaw architecture comparison
