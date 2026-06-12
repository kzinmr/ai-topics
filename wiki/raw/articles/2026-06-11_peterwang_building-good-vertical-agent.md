---
title: "Peter Wang — Building a Good Vertical Agent"
date: 2026-06-11
date_ingested: 2026-06-12
source: https://x.com/BrainsAndTennis/status/2065190286519906657
author: Peter Wang (@BrainsAndTennis)
type: x_article
tags: [vertical-agent, agent-architecture, context-engineering, context-management, tool-use, agent-harness, ai-agents, domain-specific]
related:
  - entities/peter-wang
  - entities/shortcut
  - concepts/context-as-memory-hierarchy
engagement:
  likes: 274
  bookmarks: 972
  retweets: 24
  impressions: 86705
---

# Building a Good Vertical Agent

**Author**: Peter Wang (@BrainsAndTennis)
**Date**: 2026-06-11
**Source**: [X Article](https://x.com/BrainsAndTennis/status/2065190286519906657)

## Overview

Peter Wang, co-founder of Shortcut (widely considered the most accurate spreadsheet agent, deployed inside three of the four largest multistrategy hedge funds), shares principles from a year of building a production vertical agent. The core thesis: **a good agent is a faithful compression of its task distribution**.

## Key Arguments

### The Gap
- Plenty is written about building agents, but few about building *good* ones
- Tool count varies 4× across popular agents (Codex/Claude Code ~30 tools, Pi ~7) — no agreed principle
- What separates a good agent from a toy isn't cleverness — it's domain understanding and careful work in the few places that matter

### Context as a Layered Cache (L1/L2/L3)

The central metaphor: **agent context = CPU memory hierarchy**. With the model fixed, accuracy is a function of context quality. Bloated context buries signal; missing context forces guessing. The objective: minimize context spent per task, averaged over the task distribution.

```
+---------------------------------------------+
  L1   |  ALWAYS RESIDENT - tiny, instant.           |
       |  The 80%. Lives in the system prompt.       |
       +---------------------------------------------+
                  |  miss -> one cheap call
                  v
       +---------------------------------------------+
  L2   |  ON DEMAND - curated English specs.         |
       |  The next ~15%. One discovery step to load. |
       +---------------------------------------------+
                  |  miss -> read the skill, then search
                  v
       +---------------------------------------------+
  L3   |  ESCAPE HATCH - the raw API tome.           |
       |  The long tail. 3-6 grep calls to mine.     |
       +---------------------------------------------+
```

### One Tool, Not Thirty

Every spreadsheet capability (read, write, chart, pivot) is code executed under a **single `execute_code` tool**. No read_range, no write_range, no make_chart — one tool, API lives inside the code. Why? Model accuracy degrades as you add tools. A single tool collapses everything into one decision: write code.

### L1 — The Bread and Butter (Reading/Writing Cells)

The 80% case, where disproportionate effort goes:

- **Formula aliasing**: 500 near-identical formulas → normalize to R1C1, count patterns, collapse to aliases (F1, F2...). Big token savings, zero information loss.
- **Free row/column context**: Read C5:E20, scan leftward/upward for labels → model gets `Region | Q1 | Q2` for free.
- **Style compression**: Group cells by identical style, print one line per group.
- **Write diff with linter**: After code runs, return structured diff grouped by sheet/row with suspicious cells (invalid formulas, hardcoded numbers) pulled into a "Cells that need review — MUST FIX" section.

### L2 — Curated English, On Demand

Important-but-occasional capabilities (conditional formatting, pivot tables, charts) written as curated prose specs (~few hundred lines each), fetched via `console.log(getPivotTableInfo())`. Also applied to deferred tools (web_search, web_crawl) — their schemas aren't in the prompt; a meta-tool wall loads them on demand as a session-scoped cache.

### L3 — The Raw Tome + Skill

The complete raw API (70k lines for Office.js/SpreadJS) on disk, with a ~100-line skill teaching the agent to mine it with grep recipes. The system prompt makes the escape hatch explicit: "If the wrapped API can't do it, use the raw API — don't compromise."

### Prompt Budget Split

- **L1**: A few hundred lines (core read/write, execute_code contract, safety guidelines)
- **L2**: ~50 lines (curated allowlist of blessed methods + pointers to specs)
- **L3**: ~5 lines (skill.md name/description + references)

### The Recipe, Ported to Any Domain

Three questions for any domain:
1. **What do you wrap into L1?** Bread-and-butter operations. Make them token-efficient and consequence-reporting.
2. **What do you defer to L2?** Important-but-occasional. Curated, gotcha-aware specs.
3. **What is your escape hatch (L3)?** Raw complete substrate + a skill to mine it.

### The Hierarchy Moves But Never Disappears

As models improve, yesterday's L3 becomes tomorrow's L2, and yesterday's L2 collapses into L1. But the hierarchy itself never vanishes — context will always be scarce relative to everything you could put in it.

> Bigger context windows tempt people to paste in more. The better instinct is the one CPUs settled on decades ago: summaries in cache, details on demand, the raw substrate as the last resort.

## Key Quotes

- "A good agent is a faithful compression of its task distribution."
- "The relationship isn't linear — a task that scores 99% is worth 10x more than one that scores 95%."
- "What separates a good one from a toy isn't cleverness; it's a real understanding of your domain and the patience to do some tedious, careful work in the few places that matter."

## Tags & Relevance

This article is one of the clearest articulations of practical vertical agent design, grounded in production experience (hedge fund deployment). The L1/L2/L3 context hierarchy framework is directly applicable to any agent builder's context engineering decisions.
