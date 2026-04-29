---
title: "Supermemory Filesystem (SMFS)"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags: [concept, memory-systems, ai-agents, filesystem, rag]
sources:
  - raw/articles/2026-04-29_introducing-smfs.md
---

# Supermemory Filesystem (SMFS)

**SMFS** (Supermemory Filesystem) is a mountable filesystem designed specifically for AI agents, replacing traditional UNIX operations with agent-optimized alternatives. It aims to combine the best of RAG and filesystem paradigms.

## Core Thesis
- **RAG isn't dead** — but managing embeddings and vector databases has become too painful for modern agents
- **MCP and grep seemed to make "fancy retrieval" unnecessary** — Claude Code popularized agentic search where the agent walks a codebase with grep
- **The filesystem paradigm breaks down for non-code content** — Drop PDFs, meeting transcripts, and design docs into a folder and grep fails:
  - Filenames stop being signposts
  - Agents searching for "OAuth refresh failure" miss docs that call it "token rotation issue"
  - Cannot grep diagrams inside PDFs at all

## Design
SMFS is a **mountable filesystem** that replaces UNIX operations with agent-aware alternatives. It makes the filesystem itself the storage and retrieval layer, eliminating the need for separate vector databases and RAG pipelines.

## GitHub
- https://github.com/supermemoryai/smfs
- Website: https://smfs.ai

## Relationship to Existing Concepts
- [[concepts/filesystem-memory]] — SMFS extends the filesystem-as-memory paradigm with agent-aware operations
- [[concepts/agentic-rag]] — SMFS aims to replace the RAG pipeline entirely
- [[concepts/agent-sandboxing]] — SMFS provides a filesystem layer for agent workspaces
