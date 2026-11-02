---
title: "HackerBooks (HN-recommended book discovery)"
type: concept
created: 2026-11-02
updated: 2026-11-02
tags:
  - hacker-news
  - ai-agents
  - vibe-coding
  - community
  - content-creator
confidence: high
status: active
sources:
  - raw/articles/2026-11-01_tomshardware_minecraft-agent-swarms-bureaucracy.md
related:
  - concepts/hackertube
  - entities/andrej-karpathy
---

# HackerBooks

**HackerBooks** (hackerbooks.org) is a "HackerTube, but for books mentioned on HN" service: it mines Hacker News comment history for book mentions and recommendations, then surfaces them with community-sourced context. Launched as a Show HN on 2026-11-01 and hit **1404 points / 234 comments** — the largest Show HN of the day.

## Origin: the HackerTube lineage

HackerBooks is a direct derivative of [[concepts/hackertube]], Karpathy's 2-hour Claude-Code-built YouTube clone (2584 pts, 2026-10-31), which extracted video recommendations from HN comments. Within ~36 hours the pattern — "HN comments are an undervalued recommendation corpus; an agent-built scraper + LLM classifier can turn them into a discovery engine" — had spawned two clones: HackerBooks (books, 1404 pts) and Wikihack (Wikipedia articles mentioned on HN, 197 pts, 2026-11-02).

This 3-generation cluster (2584 → 1404 → 197 pts) is a clean sample of the current **vibe-coding clone wave**: a frontier-model-built demo is published, and the community immediately forks the *concept* (not the code) into adjacent domains, each clone a weekend-scale agent build.

## Method (as reported)

Same shape as HackerTube: bulk-fetch HN comment archive → LLM workflow extracts entities (books/videos/wiki articles) and topics → rank by community signal (points-weighted mentions) → static-ish frontend. Cost profile follows Karpathy's disclosed pattern: cheap-model batch classification dominates token spend; the frontier model does orchestration and app assembly.

## Why it matters

- Validates HN comments as a **structured-interest corpus** distinct from algorithmic recommendation — human-curated co-mention graph rather than engagement-optimized feed.
- Demonstrates the **clone-latency** metric for agent-driven development: idea → viable competitor in under 48 hours changes what (if anything) is defensible about such directories.
- Ongoing HN debate: comment-mining recommendation beats personalized feeds on *signal quality* but has no cold-start answer for topics HN never discussed.

## Related

- [[concepts/hackertube]] — parent project (Karpathy, Opus 5.5 + Claude Code)
- [[entities/andrej-karpathy]] — originator of the pattern
- [[concepts/vibe-coding]] — development mode behind the clone wave

## Sources

- https://hackerbooks.org · HN: https://news.ycombinator.com/item?id=50326821
- Wikihack: https://wikihack.netlify.app · HN: https://news.ycombinator.com/item?id=50333339
