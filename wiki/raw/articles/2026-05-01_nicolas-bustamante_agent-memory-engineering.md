---
title: "Agent Memory Engineering"
author: "Nicolas Bustamante (@nicbstme)"
date: 2026-05-01
scraped: 2026-05-11
url: "https://nicolasbustamante.com/blog/agent-memory-engineering"
source: "nicolasbustamante.com"
type: blog-post
length: "34 min read (~69K chars)"
tags: [agent-memory, memory-systems, harness-engineering, claude-code, codex, hermes-agent]
---

# Agent Memory Engineering

How do agents actually remember me and my instructions? And why is moving from one agent's memory to another's so much harder than just copying files?

Nicolas Bustamante (Microsoft, ex-Fintool CEO) digs into the memory architectures of three production agent harnesses: **Hermes** (Nous Research), **Codex CLI** (OpenAI), and **Claude Code** (Anthropic).

## Core Thesis

**Models are post-trained on their harness.** Claude was post-trained against Claude Code's memory layer. GPT-5 was post-trained against Codex's memory layer. The model's instinct for "remember this for next time" is shaped by the exact UI it saw during post-training. → Switching harnesses means memory doesn't transfer.

## Key Findings

### 1. Every Clever Architecture Lost
Vector DBs, knowledge graphs, dedicated memory agents — all came in second to **LLM + markdown + bash tool**. The interesting question is not "what data structure" but "what discipline does the agent follow when reading and writing it."

### 2. Three Memory Architectures
- **Bounded Snapshot** (Hermes): Fixed-size memory snapshot frozen at session start
- **Two-Phase Async Pipeline**: Cron job extracts → small model summarizes → big model consolidates
- **Typed Live Writes** (Claude Code): Agent writes typed markdown files, always-load MEMORY.md index

### 3. Storage Layer Comparison
- **Codex**: Strict block schema with required frontmatter
- **Claude Code**: Typed markdown files with MEMORY.md index + age-aware reminders
- **Hermes**: Snapshot at session start, frozen for prefix cache

### 4. The Prefix Cache Problem
Hermes freezes the snapshot for prefix cache efficiency — but sacrifices the ability to update memory mid-session.

### 5. The Signal Gate
Telling the agent when NOT to remember — preventing memory pollution from one-off interactions.

Full article: https://nicolasbustamante.com/blog/agent-memory-engineering
