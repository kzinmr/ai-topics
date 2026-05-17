---
title: "Deep Dive: How OpenClaw's Memory System Works"
source: https://snowan.gitbook.io/study-notes/ai-blogs/openclaw-memory-system-deep-dive
author: snowan (GitBook)
date: 2026-01-25
scraped: 2026-05-17
type: raw_article
tags: [openclaw, memory-systems, agent-architecture, context-engineering, vector-search, bm25, embedding, sqlite]
---

# Deep Dive: How OpenClaw's Memory System Works

## Introduction

OpenClaw is an open-source AI agent framework that stands out for its sophisticated memory system. Unlike traditional RAG (Retrieval-Augmented Generation) systems that rely on vector databases, OpenClaw takes a **file-first approach**: Markdown files are the source of truth, and the memory system is designed to help AI agents remember context across conversations.

## Architecture Overview

OpenClaw implements a **file-based, Markdown-driven memory system** with semantic search capabilities. The core philosophy: **files are the source of truth** — the AI agent only retains what gets written to disk.

### Key Components

1. **Markdown Storage Layer**: Plain text files in the workspace directory
2. **Vector Search Engine**: SQLite-based with hybrid (BM25 + vector) retrieval
3. **Embedding Providers**: Auto-selection between local/OpenAI/Gemini
4. **Automatic Memory Flush**: Pre-compaction trigger to persist context

## Memory Types & Storage Structure

### 1. Ephemeral Memory (Daily Logs)
**Location**: `memory/YYYY-MM-DD.md` — append-only files capturing day-to-day activities. Auto-creates new file each day, loads today + yesterday at session start.

### 2. Durable Memory (Curated Knowledge)
**Location**: `MEMORY.md` — curated long-term memory containing important decisions, project conventions, long-term todos. ONLY loaded in private sessions (never group contexts).

### 3. Session Memory
**Location**: `sessions/YYYY-MM-DD-<slug>.md` — automatically saves conversation transcripts with LLM-generated descriptive slugs. Indexed and searchable.

## Core Implementation: MemoryIndexManager

Central class managing all memory operations. Features: singleton pattern with caching, per-agent isolation (separate SQLite stores), file watching with debounced sync, provider fallback chain, session integration.

## Markdown Chunking Algorithm

Sliding window with overlap preservation:
- Target: ~400 tokens per chunk (~1600 chars)
- Overlap: 80 tokens (~320 chars) between consecutive chunks
- Line-aware with line numbers
- SHA-256 hash-based deduplication for cache lookup

Why: overlap prevents context loss at boundaries, line numbers enable precise source attribution, hash stability enables cache hits.

## Hybrid Search: BM25 + Vector

Weighted score fusion (default: 70% vector + 30% text):
1. **Vector Search** (semantic similarity): cosine similarity via sqlite-vec extension
2. **BM25 Search** (lexical matching): SQLite FTS5 for exact terms/IDs/error codes

BM25 rank normalization converts rank to [0,1] score for fusion.

## Embedding Provider System

Auto-selection chain with graceful degradation:
1. **Local** (node-llama-cpp, ~600MB model, privacy, offline)
2. **OpenAI** (text-embedding-3-small, 1536 dim, fast, Batch API support)
3. **Gemini** (gemini-embedding-001, 768 dim, free tier)

## Batch Embedding Optimization

Cache-first strategy with SHA-256 dedup. OpenAI Batch API: 50% cost reduction. Cost example for 10,000 chunks: Sync $0.20 → Batch $0.10 → 50% cache hit $0.05.

## SQLite Schema & Vector Storage

Core tables for files, chunks, embeddings, sessions. Uses sqlite-vec extension for in-database vector similarity. Falls back to JavaScript if extension unavailable.

## Automatic Memory Flush (Pre-Compaction)

When session approaches auto-compaction threshold, OpenClaw triggers a **silent, agentic turn** that reminds the model to write durable memory BEFORE context is compacted. Usually silent (NO_REPLY), one flush per compaction cycle, skipped in read-only sandbox mode.

For a 200K context window: triggers when context usage reaches ~80%.

## Session Memory Integration

Auto-saves and indexes past conversations with:
- JSONL parsing for user/assistant messages
- Delta-based incremental indexing (100KB or 50 messages threshold)
- Debounced background sync
- LLM-generated slugs for descriptive filenames

## Memory Search Tools

Two tools exposed to agents:
- **memory_search**: Returns snippets (~700 chars) with file path, line range, relevance score
- **memory_get**: Reads specific memory files with optional line range filtering

Both only enabled when `memorySearch.enabled` resolves to true.

## Key Innovations

1. **File-First Philosophy**: No database as source of truth — human-readable, version-controllable, no vendor lock-in
2. **Hybrid Retrieval**: BM25 + vector gives balanced precision/recall
3. **Provider Auto-Selection**: Local → OpenAI → Gemini fallback with graceful degradation
4. **Batch Optimization**: 50% cost reduction via Batch APIs
5. **Cache-First Embedding**: SHA-256 dedup prevents re-embedding
6. **Delta-Based Sync**: Incremental session indexing
7. **Pre-Compaction Flush**: Automatic context → memory transfer before truncation
8. **Per-Agent Isolation**: Separate SQLite stores per agent ID

## Performance

- Local embedding: ~50 tokens/sec (node-llama-cpp on M1 Mac)
- OpenAI embedding: ~1000 tokens/sec (with batching)
- Search latency: <100ms for 10K chunks (hybrid search)
- Index size: ~5KB per 1K tokens (1536-dim embeddings)

## Comparison with Traditional RAG

| Aspect | Traditional RAG | OpenClaw Memory |
|--------|----------------|-----------------|
| Source of truth | Vector database | Markdown files |
| Search method | Vector only | Hybrid (BM25 + vector) |
| Storage | Pinecone/Weaviate/Chroma | SQLite |
| Embedding | Always remote API | Local-first with fallback |
| Chunking | Fixed-size | Line-aware with overlap |
| Caching | Usually none | SHA-256 hash-based |
| Updates | Full reindex | Delta-based incremental |
| Context preservation | Manual | Automatic pre-compaction flush |
| Human-readable | No | Yes (plain Markdown) |
| Cost optimization | Limited | Batch API + caching |

## Limitations

- **Storage Growth**: ~365 daily logs + ~1000 session files/year → ~500MB SQLite index
- **Embedding Drift**: Different providers use different dimensions; switching requires reindexing
- **FTS5 Limitations**: No fuzzy matching, typo tolerance, or advanced ranking signals
- **No Cross-File Context**: Each chunk embedded independently

## References

- OpenClaw GitHub Repository (commit f99e3dd, January 2026)
- sqlite-vec Extension
- node-llama-cpp
