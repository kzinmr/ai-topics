---
title: Claude Perfect Memory
type: concept
created: 2026-04-27
updated: 2026-05-26
status: L2
sources: [https://x.com/i/article/2044531930671288320, https://code.claude.com/docs/en/memory, https://milvus.io/blog/claude-code-memory-memsearch.md]
tags:
  - anthropic
  - memory-systems
  - context-engineering
  - architecture
aliases: [claude-memory, claude-code-memory]
---

# Claude Perfect Memory

A comprehensive guide to Claude Code's (Anthropic's AI coding agent) **multi-layer memory system**. Published by Gul Jabeen (@techwithgul.ai) on Medium in March 2026, with 8,194 bookmarks and 1.7 million impressions.

## Core Problem: Stateless AI

Claude's context window is like a **whiteboard** — it gets cleared every session. This is not a bug but a fundamental property of LLMs. The essence of a memory system is simple:

> Without building your own memory, cross-session context retention is impossible.

## 4-Layer Memory Architecture

Claude Code's memory system consists of 4 layers:

### 1. CLAUDE.md — Manual Rule File

| Scope | Path | Description |
|----------|------|------|
| **Managed Policy** | `/Library/.../CLAUDE.md` (macOS) | Organization-wide |
| **Project** | `./CLAUDE.md` | Repository-wide |
| **User** | `~/.claude/CLAUDE.md` | Personal (all projects) |
| **Local** | `./CLAUDE.local.md` | Personal (gitignored) |

**Best practices:**
- Keep under 150 lines (short but faithfully followed)
- Use bullet points (parsed faster than paragraphs)
- Specify important paths (50% search reduction for 500+ files)
- Include code examples (3-5, significantly reduces rewrite requests)
- State prohibitions explicitly (more effective than positive recommendations)

### 2. Auto Memory — Automatic Notes

| Setting | Value |
|------|------|
| **Location** | `~/.claude/projects/<project>/memory/` |
| **Entry point** | `MEMORY.md` |
| **Load limit** | First 200 lines or 25KB |
| **Categories** | user / feedback / project / reference |
| **Load method** | First 200 lines auto-loaded every session, topic files on-demand |

```
~/.claude/projects/<project>/memory/
├── MEMORY.md              ← index (1 line ≤150 chars)
├── feedback_testing.md
├── project_auth_rewrite.md
└── reference_linear.md
```

**Auto control:**
- Disable: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude`
- Enable: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=0 claude`

### 3. Auto Dream — Automatic Cleanup

- **Purpose**: Clean up stale memories
- **What it does**:
  - Replaces 'yesterday's deploy issue' → '2026-03-28 deploy issue'
  - Resolve contradictions (PostgreSQL → MySQL)
  - Remove references to deleted files
- **Trigger**: 24+ hours elapsed + MEMORY.md exceeds 200 lines
- **Limitation**: Handles a few days of clutter, cannot span months

### 4. KAIROS — Unreleased Always-On Daemon

- Found in leaked Claude Code source (v2.1.88 source map)
- **Always-on** memory daemon mode
- **Unreleased build** as of April 2026
- Potentially enables long-term memory spanning

## Modular Rules (`.claude/rules/`)

Specify path-specific rules via YAML frontmatter:

```yaml
---
paths: ["src/api/**/*.ts"]
---
# API Development Rules
- All API endpoints must include input validation
- Use Zod for schema validation
```

**Performance improvements:**
- Context tokens: 2,000 → 1,200 (-40%)
- Instruction relevance: +35%
- Rewrites: 5 → 3 (-40%)
- Response time: 45s → 30s (-33%)

## Key Commands

| Command | Purpose |
|----------|------|
| `/init` | Initialize project memory |
| `/memory` | Directly edit memory files |
| `/config` | Change settings (persisted in settings.json) |
| `@path/to/file` | Import external files (up to 5 levels recursion) |

## Limitations

1. **200-line limit**: MEMORY.md is only loaded up to 200 lines
2. **Exact keyword match**: Semantic search is not available ('port conflict' won't match 'docker-compose mapping')
3. **Local only**: Memories never leave Claude Code
4. **No cross-agent inheritance**: Switching agents means starting from zero

## External Solutions

- **claude-mem** ([thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)): Open standard AI agent memory — RAG + RAD (Retrieval Augmented Discovery)
- **Milvus Memsearch**: Cloud-based semantic search to fill Claude Code memory gaps

## Significance

Claude Perfect Memory became a **catalyst for widespread awareness of the importance of agent cross-session memory**. The 8,194 bookmarks demonstrate that 'context engineering' is becoming a core skill for solo founders and AI engineers.

## Related Concepts
- [[concepts/claude-perfect-memory]]

- [Solo Founder Stack](solo-founder-stack.md) — Context engineering is a core solo founder skill
- [CLAUDE.md](claude-md-pattern.md) — Structured memory file pattern
- [Context Engineering](context-engineering.md) — Information environment design

## References

- 2026-04-22-claude-perfect-memory-guide

