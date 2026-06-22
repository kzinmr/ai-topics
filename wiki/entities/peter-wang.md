---
title: Peter Wang
created: 2026-06-12
updated: 2026-06-12
type: entity
tags:
  - person
  - ai-agents
  - vertical-agent
  - architecture
  - context-engineering
sources:
  - raw/articles/2026-06-11_peterwang_building-good-vertical-agent.md
---

# Peter Wang (@BrainsAndTennis)

Co-founder of [[entities/shortcut|Shortcut]] and author of "Building a Good Vertical Agent" (Jun 2026), one of the most bookmarked X Articles on practical agent design (972 bookmarks). Also described as "Founding scientist @fundamental" in his X bio.

## Background

- X handle: @BrainsAndTennis (~10K followers)
- Focus: vertical AI agent engineering, spreadsheet AI, domain-specific agent design
- Production experience: built Shortcut agent deployed inside 3 of the 4 largest multistrategy hedge funds

## Core Ideas

### Context as Memory Hierarchy (L1/L2/L3)

Wang's central framework: agent context should mirror CPU memory hierarchy — a small always-resident cache (L1), on-demand curated specs (L2), and a raw escape hatch with a grep skill (L3). The objective is to minimize context spent per task, averaged over the task distribution.

> "A good agent is a faithful compression of its task distribution."

### One Tool, Not Thirty

Advocates a single `execute_code` tool rather than many specific tools. Model accuracy degrades with tool count; one tool lets the model compose capabilities via code.

### Domain Understanding Over Cleverness

What separates a good agent from a toy: "a real understanding of your domain and the patience to do some tedious, careful work in the few places that matter." The 99%-accurate task is worth 10× more than the 95%-accurate one.

## Notable Contributions

- L1/L2/L3 context hierarchy pattern for agents
- Formula aliasing and style compression for spreadsheet token efficiency
- Write diff with built-in linter (MUST FIX categorization)
- Deferred tool loading as session-scoped cache

## Sources

- [[raw/articles/2026-06-11_peterwang_building-good-vertical-agent|Building a Good Vertical Agent]] (X Article, Jun 2026, 972 bookmarks)
