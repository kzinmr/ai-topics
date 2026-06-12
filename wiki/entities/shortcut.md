---
title: Shortcut (AI Spreadsheet Agent)
created: 2026-06-12
updated: 2026-06-12
type: entity
tags: [product, vertical-agent, ai-agents, agent-architecture, context-engineering, domain-specific]
sources:
  - raw/articles/2026-06-11_peterwang_building-good-vertical-agent.md
---

# Shortcut

Shortcut is a vertical AI agent focused on spreadsheet tasks, widely considered the most accurate spreadsheet agent. Deployed inside three of the four largest multistrategy hedge funds, where being wrong is expensive.

## Key Facts

- **Co-founders**: [[entities/peter-wang|Peter Wang]] and others
- **Domain**: Spreadsheet operations (Excel/SpreadJS)
- **Differentiator**: Agent accuracy — "the agent is right more often, and in this domain that has been the single most compelling reason customers pick us"
- **Customers**: 3 of top 4 multistrategy hedge funds

## Architecture

### Single execute_code Tool

All capabilities (read, write, chart, pivot, conditional formatting) routed through one `execute_code` tool — no separate read_range, write_range, make_chart tools. The API lives inside the code the model writes.

### L1/L2/L3 Context Hierarchy

- **L1** (always in prompt): Core read/write operations with formula aliasing, style compression, free row/column context, and write diffs with built-in linting
- **L2** (on-demand specs): Curated English specs for pivot tables, conditional formatting, charts, data validation — fetched via `console.log(getXInfo())`
- **L3** (escape hatch): Full raw API reference (70k lines Office.js/SpreadJS) on disk, accessible via ~100-line grep skill

### Compression Techniques

- **Formula aliasing**: 500 identical formulas → one legend line (normalize to R1C1, count patterns, collapse)
- **Style compression**: Group cells by identical style, print one line per group
- **Write diff triage**: Changed cells grouped by sheet/row, suspicious cells (invalid formulas, hardcoded numbers) surfaced under "MUST FIX"

### Deferred Tool Loading

Additional tools (web_search, web_crawl, create_website) have schemas not in the prompt. Instead, a meta-tool wall allows the model to load tool schemas on demand — session-scoped cache pattern.

## Related

- [[entities/peter-wang|Peter Wang]] — co-founder and primary author of the architecture design
- [[concepts/context-as-memory-hierarchy|Context as Memory Hierarchy]] — the L1/L2/L3 framework
- [[concepts/vertical-agent-design|Vertical Agent Design]] — domain-specific agent engineering principles
