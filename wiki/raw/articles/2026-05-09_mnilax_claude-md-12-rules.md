---
title: "Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more"
source: "X Article by @Mnilax"
date: 2026-05-09
scraped: 2026-05-11
type: x_article
url: https://x.com/i/article/2053106718226227203
authors: ["@Mnilax"]
tags: [claude-code, agentic-engineering, context-engineering, coding-agents]
status: metadata-only
---

# Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more

**Author**: @Mnilax
**Published**: 2026-05-09
**Original URL**: https://x.com/i/article/2053106718226227203
**X Post**: https://x.com/Mnilax/status/2053116311132155938

> NOTE: This is a metadata-only record. The full article is behind X's authentication wall and could not be scraped. A mirror was not found via web search. The content below is reconstructed from X.com search result snippets.

## Summary (from available metadata)

In late January 2026, Andrej Karpathy posted a thread complaining about how Claude writes code — three failure modes: silent wrong assumptions, over-complication, orthogonal damage to code it shouldn't have touched.

Forrest Chang read the thread, packaged the complaints into 4 behavioral rules in a single CLAUDE.md file, and dropped it on GitHub. It hit 5,828 stars in the first day, 60,000 bookmarks in two weeks, and 120,000+ stars by May 2026 — the fastest-growing single-file repo of 2026.

The author (@Mnilax) tested these 4 rules on 30 codebases over 6 weeks. Results: mistakes that used to happen ~40% of the time dropped to under 3% on tasks that played to their strengths. But the 4 rules were built for January 2026 code-writing problems — they don't cover May 2026 agent-orchestration problems (multi-step agents, hook cascades, skill loading, multi-codebase work).

The author added 8 more rules covering these new areas. The claim: 12 rules total, mistake rate from 41% → 3%.

Key insight: CLAUDE.md is "the most under-leveraged file in the entire AI coding stack." Most developers either bloat it to 4,000+ tokens (compliance drops to 30%), skip it entirely (5x token waste), or copy once and forget (breaks silently as codebase shifts). Anthropic docs say CLAUDE.md is advisory — Claude follows it ~80% of the time. Past 200 lines, compliance drops sharply.

## Related
- [[concepts/claude-md-rules]] — Karpathy's CLAUDE.md behavioral rules for coding agents
- [[entities/andrej-karpathy]] — Andrej Karpathy
- [[entities/claude-code]] — Claude Code
- [[entities/forrest-chang]] — Creator of the andrej-karpathy-skills repo
