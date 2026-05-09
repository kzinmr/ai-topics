---
title: "Using Claude Code: The Unreasonable Effectiveness of HTML (X Article)"
source: "@trq212 / Thariq Shihipar"
date: 2026-05-08
scraped: 2026-05-09
type: metadata-only
url: https://x.com/i/article/2052796100608974848
note: "X native article behind auth wall — preserved as metadata. Author: Thariq Shihipar (Claude Code team, Anthropic). Companion site: https://thariqs.github.io/html-effectiveness/"
tags:
  - prompt-engineering
  - claude-code
  - html
  - markdown
---

# Using Claude Code: The Unreasonable Effectiveness of HTML

**Author**: Thariq Shihipar (@trq212) — Member of Technical Staff, Claude Code team, Anthropic
**Published**: 2026-05-08 on X
**Status**: Metadata-only (X native article behind auth wall)

## Summary (from Simon Willison's commentary)

Thariq Shihipar advocates for HTML over Markdown as an output format to request from Claude. Key arguments:

- HTML allows LLMs to embed SVG diagrams, interactive widgets, in-page navigation
- Modern large context windows make the token-efficiency advantage of Markdown negligible
- HTML artifacts render actual diffs with inline margin annotations, color-coded severity
- Companion site with 20 self-contained examples: https://thariqs.github.io/html-effectiveness/

## Example Prompt

```
Help me review this PR by creating an HTML artifact that describes it.
I'm not very familiar with the streaming/backpressure logic so focus on that.
Render the actual diff with inline margin annotations, color-code findings
by severity and whatever else might be needed to convey the concept well.
```

## Eight Categories of HTML Artifacts (from companion site)

1. **Exploration & Planning** (3 demos) — Side-by-side code approach comparisons, visual design directions, implementation plans with timelines
2. **Code Review & Understanding** (3 demos) — Annotated PRs with severity tags, PR writeups, module maps as boxes-and-arrows
3. **Design** (2 demos) — Living design system swatches, component variant contact sheets
4. **Prototyping** (2 demos) — Animation sandboxes with sliders, clickable interaction flows
5. **Illustrations & Diagrams** (2 demos) — SVG figure sheets, annotated flowcharts
6. **Decks** (1 demo) — Arrow-key slide decks from `<section>` tags + 20 lines of JS
7. **Research & Learning** (2 demos) — Feature explainers with collapsible sections, concept explainers with live rings
8. **Reports** (2 demos) — Weekly status with charts, incident timelines
