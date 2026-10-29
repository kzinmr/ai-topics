---
title: "ypi: a recursive coding agent"
source_url: https://raw.works/ypi-a-recursive-coding-agent/
author: Raymond Weitekamp (@raw_works)
published: 2026-02-12
ingested: 2026-10-28
source_type: blog
tags: [raw, blog, rlm, coding-agents, recursion, jj, pi, self-delegation]
---

# ypi: a recursive coding agent

**Author:** Raymond Weitekamp ([@raw_works](https://x.com/raw_works)) — RAW Works (raw.works)
**Published:** February 12, 2026
**URL:** https://raw.works/ypi-a-recursive-coding-agent/

I built **ypi** — a recursive coding agent. It's Pi that can call itself.

The name comes from the **Y combinator** in lambda calculus — the fixed-point combinator that enables recursion. ("rpi" has other connotations.)

The idea was inspired by Recursive Language Models (RLM), which showed that an LLM with a code REPL and a `llm_query()` function can recursively decompose problems, analyze massive contexts, and write code — all through self-delegation.

## The idea

Pi already has a bash REPL. I added one function — `rlm_query` — and a system prompt that teaches Pi to use it recursively. Each child gets its own **jj workspace** for file isolation. That's the whole trick.

```
┌──────────────────────────────────────────┐
│  ypi (depth 0)                           │
│  Tools: bash, rlm_query                  │
│  Workspace: default                      │
│                                          │
│  > grep -n "bug" src/*.py                │
│  > sed -n '50,80p' src/app.py \          │
│      | rlm_query "Fix this bug"          │
│            │                             │
│            ▼                             │
│    ┌────────────────────────────┐        │
│    │  ypi (depth 1)             │        │
│    │  Workspace: jj isolated    │        │
│    │  Edits files safely        │        │
│    │  Returns: patch on stdout  │        │
│    └────────────────────────────┘        │
│                                          │
│  > jj squash --from <child-change>       │
│  # absorb the fix into our working copy  │
└──────────────────────────────────────────┘
```

The recursion works like this: `rlm_query` spawns a child Pi process with the same system prompt and tools. The child can call `rlm_query` too:

```
Depth 0 (root)    → full Pi with bash + rlm_query
  Depth 1 (child) → full Pi with bash + rlm_query, own jj workspace
    Depth 2 (leaf) → full Pi with bash, but no rlm_query (max depth)
```

Each recursive child gets its own jj workspace, so the parent's working copy stays untouched. You review child work with `jj diff`, absorb it with `jj squash --from`.

## How it works

The architecture maps directly to the Python RLM library.

## Key takeaways

- Minimal recipe for "recursive coding agent": existing agent + one `rlm_query` tool + a recursion-teaching system prompt + per-child VCS workspace isolation.
- jj (Jujutsu) workspaces as the isolation primitive for recursive agents — child agents edit safely in isolated change contexts; parent absorbs via `jj squash --from`.
- Direct RLM-to-agent translation of the `llm_query()` self-delegation pattern.
