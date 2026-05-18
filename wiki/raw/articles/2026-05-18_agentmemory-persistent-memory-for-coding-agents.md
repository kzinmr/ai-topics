---
title: "agentmemory — Persistent Memory for AI Coding Agents"
source: https://github.com/rohitg00/agentmemory
author: Rohit Ghumare (rohitg00)
date: 2026-05-18
publication: GitHub / AlphaSignal
tags: [memory-systems, coding-agents, agent-memory, ai-agents, iii-engine, mcp, hybrid-search, open-source]
saved: 2026-05-18
---

# agentmemory — Persistent Memory for AI Coding Agents

> "Your coding agent remembers everything. No more re-explaining."
> Built on iii engine
> 12K+ GitHub stars, Apache-2.0, TypeScript (81.4%)

agentmemory is a persistent memory system for AI coding agents, built on iii-engine's three primitives (Worker/Function/Trigger). It silently captures every action your coding agent takes, compresses it into searchable memory, and injects the most relevant context into future sessions.

Works with Claude Code, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, pi, OpenCode, and any MCP client.

## Architecture

### Three Layers

1. **Capture**: 12 Claude Code lifecycle hooks fire automatically (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PreCompact, SubagentStart, SubagentStop, Notification, TaskCompleted, Stop, SessionEnd). Each hook reads JSON from stdin, POSTs to local REST API. Non-Claude agents use `memory_save` MCP tool or `/agentmemory/observe` endpoint.

2. **Pipeline**: Every observation passes through SHA-256 dedup (5-min window), privacy filter (strips API keys, tokens, secrets), BM25 indexing (always on, no LLM needed), and optional LLM compression (off by default since v0.8.8).

3. **Retrieval**: Three parallel streams — BM25 (Porter stemming, synonym expansion), Vector (cosine similarity over all-MiniLM-L6-v2 384-dim, free local or hosted), Graph (entity-relationship traversal). Results fused with Reciprocal Rank Fusion (k=60), diversified max 3 per session.

### 4-Tier Memory Consolidation

Memories progress through tiers (Ebbinghaus-style decay):
- **Working**: Raw observations
- **Episodic**: Compressed session summaries
- **Semantic**: Extracted facts and patterns
- **Procedural**: Workflows and decision patterns

Frequently accessed memories strengthen; stale ones auto-evict; contradictions detected and resolved on write.

### Context Assembly

`mem::context` assembles pinned slots, project profile, recent summaries, and high-importance observations into a ~1,900 token block. SessionStart context injection is off by default.

## Benchmarks

### LongMemEval-S (ICLR 2025)
- R@5: 95.2% (vs BM25-only: 86.2%)
- R@10: 98.6%
- MRR: 88.2%

### Token Efficiency
- agentmemory: ~170K tokens/year, ~$10/year
- LLM-summarized: ~650K, ~$500/year
- Paste full context: 19.5M+, impossible

## Integration

51 MCP tools, 6 resources, 4 slash commands (/recall, /remember, /session-history, /forget), 127 REST endpoints. Claude Code: 12 hooks + MCP via plugin marketplace. Codex CLI: 6 hooks + MCP plugin. Cursor/Cline/Windsurf/Gemini CLI: MCP config block.
