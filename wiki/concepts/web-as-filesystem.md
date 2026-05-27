---
title: "Web-as-Filesystem (Nia Docs)"
type: concept
aliases:
  - agentsearch
  - nia-docs
  - documentation-shell
tags:
  - concept
  - developer-tooling
  - tool
status: complete
description: "An abstraction that mounts all web documents as a Unix filesystem, enabling agents to naturally use tree/grep/cat/find and eliminating code hallucinations."
created: 2026-04-27
updated: 2026-04-27
sources:
  - "https://x.com/i/article/2041215978957389908"
related:
  - "[[concepts/rags]]"
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/mcp]]"
---

# Web-as-Filesystem (Nia Docs)

> **Definition:** An abstraction that mounts all web documentation as a Unix filesystem. Agents naturally use `tree`, `grep`, `cat`, `find`, eliminating code hallucinations.

## The Problem: Code Hallucination Is Not a Model Problem

- APIs change daily with breaking changes, deprecated endpoints, and parameter renames
- Model training data is months to years old
- Agents write seemingly perfect code that fails at runtime

## RAG Limitations
- Chunk documents, embed them, retrieve top-K
- Cannot handle answers spanning three pages or when exact function signatures are lost in chunking
- Retrieval only provides fragments, but agents need the full picture

## The Filesystem Abstraction Proposal

### Unix Wisdom
50 years ago Unix solved it: devices, processes, sockets — all files. `open`, `read`, `write`, `close`. One interface.

### Agents Are Pre-trained on Unix
- Billions of tokens of filesystem interaction baked into the weights
- `tree`, `grep`, `find` — not tools for agents to learn, but tools they already know
- Every coding model has learned millions of examples of `cat README.md`, `grep -r "auth" .`, `find . -name "*.md"`

### Comparison with MCP
- MCP: Each tool requires JSON schema, natural-language description, and careful argument construction
- Filesystem: None of that. Consumes no context window, no misuse surface area

> "@jerryjliu0: an agent with filesystem tools and a code interpreter is just as general, if not more general, than an agent with 100+ MCP tools."

## How It Works

### 1. Index
- When a URL is first accessed, the backend crawls the site
- Respects `llms.txt`, detects OpenAPI specs, handles redirects
- Each page becomes a file
- Example: `https://docs.stripe.com/api/charges/create` → `/api/charges/create.md`
- Path normalization: auto-detects and strips common path prefixes (absorbing inconsistent structures like `/docs/`, `/api/reference/`)

### 2. Serve
- Expose filesystem operations as API endpoints
- All responses gzip compressed
- `/load` endpoint returns status and all files in a single request
- cache: `Cache-Control: public, max-age=300`
- CLI maintains disk cache at `~/.cache/nia-docs/`
- Namespace is shared (unauthenticated by design)

### 3. Shell
- Runs on the client side (no container/sandbox/VM)
- just-bash (TypeScript reimplementation of bash)
- Supports grep, cat, ls, find, cd, tree, pipes, aliases
- Complete filesystem as an in-memory JavaScript object
- Large sites (1,000+ pages): load file tree upfront, lazy fetch via cat

## Why Not a Real Sandbox
- Boot time: ~100ms (cached), ~2s (already indexed), ~30-120s (cold index)
- Per-session compute: zero on the server side
- No need to borrow a micro-VM for a read-only static text workload

## Agent Setup
Just append to the agent's instruction file to use:
- Supports Claude Code, Cursor, Copilot, Codex, Gemini CLI, OpenCode
- `-c` flag for single command execution → exit. No interactive session needed

## Initial Data: Standard Agent Workflow
1. `tree` — Get oriented
2. `grep -rl` — Find relevant files
3. `cat` — Read

This is the same pattern a human developer follows. The filesystem abstraction isn't something agents need to learn — it's what they default to when available.

## Future Outlook
- API references as directories
- Changelogs as files
- OpenAPI specs as cat-able JSON
- Building infrastructure to make the entire web navigable like a codebase

## Sources
- [Turning the entire web into a filesystem](https://x.com/i/article/2041215978957389908) (2026-04-22, X article) — Arlan Rakhmetzhanov (Nozomio Labs CEO) — Nia's documentation shell
- [AgentSearch.sh](https://www.agentsearch.sh/) — live demo
