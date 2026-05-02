---
title: "Supermemory (SMFS)"
type: entity
created: 2026-04-30
updated: 2026-04-30
tags:
  - company
  - memory-systems
  - filesystem
  - ai-agents
sources:
  - raw/articles/2026-04-29_introducing-smfs.md
---

# Supermemory (SMFS)

**Supermemory** is a company building the **Supermemory Filesystem (SMFS)** — a mountable filesystem designed specifically for AI agents.

## Product: SMFS
- Mountable filesystem replacing traditional UNIX operations with agent-optimized alternatives
- Aims to combine RAG and filesystem paradigms
- GitHub: https://github.com/supermemoryai/smfs
- Website: https://smfs.ai

## Core Thesis
- RAG isn't dead, but managing embeddings and vector databases has become too painful for modern agents
- Traditional filesystems fail for non-code content (PDFs, meeting transcripts, diagrams)
- SMFS makes the filesystem itself the storage and retrieval layer

## April 2026 Launch
- Article received 620 bookmarks, 304 likes, 136K impressions
- Positioned as fixing both "RAG sucks and filesystems are broken"

## SMFS Architecture Details

### Core Design
- **Rust-based single binary** — no kernel extensions
- **FUSE on Linux**, **NFSv3 on macOS** (pure-Rust localhost server, no macFUSE/kext/security prompts, shows in Finder natively)
- **Works with Daytona, E2B, Cloudflare, Vercel** and pretty much all sandboxes
- **Local-first sync** — reads never block on network; writes commit to local SQLite and drain to Supermemory Cloud with exponential backoff; survives restarts; offline reads keep working

### 4 Key Features

**1. Semantic Grep**
- `grep` without flags = semantic (vector query scoped to current path)
- `grep -F` = literal (traditional)
- Same Unix muscle memory, but matching function is a vector query
- Results land back on real paths; agent can `cat`, `ls`, re-grep with narrower scope

**2. User Profiles**
- `cat profile.md` returns a live digest of every memory in the container
- Not stored — synthesized on read from the supermemory graph
- Always fresh: if a fact updates in the graph, it automatically updates in the profile

**3. Multi-Agent Sync Engine**
- Multiple agents can mount the same container
- Agent A writes a memory → Agent B sees it on next pull
- Operations are instant (local SQLite) and incrementally synchronize with the cloud

**4. Auto Extraction**
- Drop raw files (PDFs, videos, screenshots, audio, docs) — no OCR, no transcription, no chunking needed
- `grep` works across every format natively
- Example: `grep "action items" ~/smfs/` returns matches across contract.pdf, standup.mp4, screenshot.png, handbook.docx, interview.m4a

### Benchmark Results (Claude & Codex, 20 tasks)

| Metric | Without SMFS | With SMFS | Change |
|---|---|---|---|
| **Codex token usage** | 1.2M | 203K | **-83%** |
| **Claude tool calls** | 116 | 42 | **-64%** |
| **Claude token usage** | — | — | **-36%** |
| **Answer found** | 19/20 (Codex), 16/20 (Claude) | 19/20, 18/20 | Claude +2 |
| **Internal benchmark** | — | — | Beats agentic search by >50% |

### Why It Works
> "Codebases are special. Filenames mean what they say. Function names are designed to be searchable. Your notes folder is not a codebase. Drop a thousand PDFs, meeting transcripts, and design docs in there and watch it fall apart."

SMFS solves the fundamental mismatch between agentic search (designed for code) and general document retrieval (where filenames are unreliable and content is multimodal).

## Related
- [[concepts/smfs]] — The filesystem concept page
- [[concepts/filesystem-memory]] — Alternative approach to agent memory

## References

- 2026-04-28_x-article-introducing-smfs-supermemory-filesystems
