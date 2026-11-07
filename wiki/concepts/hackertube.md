---
title: "HackerTube"
type: concept
created: 2026-11-01
updated: 2026-11-07
tags:
  - ai-agents
  - coding-agents
  - vibe-coding
  - recommendation-systems
  - hacker-news
  - youtube
confidence: high
sources:
  - raw/articles/2026-10-31_karpathy-hackertube.md
  - https://news.ycombinator.com/item?id=50319510
---

# HackerTube

HackerTube (hackertube.org) is a YouTube clone built by [[entities/andrej-karpathy|Andrej Karpathy]] in ~2 hours using Claude Opus 5.5 via Claude Code, announced 2026-10-31. It curates video recommendations from Hacker News comment history instead of YouTube's engagement-optimizing algorithm, as a direct response to what Karpathy called YouTube's "enshittified wall of slop."

## Overview

Motivated by frustration with YouTube's recommendation quality, Karpathy delegated the entire build to Opus 5.5 ("I don't actually do anything resembling traditional engineering anymore... I only talk to Claude and have it do everything"). The pipeline:

1. Opus downloaded all Hacker News comments (2007–2026)
2. Ran **Sonnet over them in a Claude Code Workflow** to filter spam and identify YouTube-video recommendations
3. Narrowed to 40K recommending comments → **6,454 YouTube videos across 150 topics**
4. Wrapped in a YouTube-like UI, deployed to a VPS with Claude handling deploy/secure/harden/optimize

Features: quality-curated content, 50%-crop thumbnails, account-free ForYou recommendations (state in local browser session), keyboard shortcuts, and a downloadable data export so users can have their own agent rebuild the site.

## Token Economics (from HN thread)

Karpathy disclosed the cost breakdown: **504M input tokens (90% cached), 7.6M output tokens** — over 90% of which was Sonnet calls labeling comments. The actual application + deploy work was only **~1M Opus 5.5 tokens**, with one context compaction. "Very small project by modern standards."

The manual work Karpathy retained: creating a Google Cloud YouTube-metadata API key, booting a VPS, buying the domain. The server code was not published ("a vibe coded mess") but the underlying dataset is downloadable.

## Significance

- **Flagship vibe-coding exemplar**: a production-deployed, publicly-used web app built end-to-end by an agent, by one of the field's most prominent engineers, at 1449 HN points — the strongest mainstream statement yet of the "agent does everything, human supervises" workflow (see [[concepts/agentic-engineering]]).
- **Batch-labeling cost pattern**: cheap-model (Sonnet) bulk classification + expensive-model (Opus) orchestration is a recurring agent cost-optimization design; the 90% cache hit rate on the input side is notable.
- **Community-curation counterpoint to algorithmic feeds**: top HN comments argued YouTube's recommendations are bad by any user-centric metric ("They're interested in getting you to watch ads, they couldn't care less what you want" — globular-toast), and requested the same treatment for social media feeds.

## Successor: TristanTube (Nov 7, 2026)

Six days after HackerTube, Karpathy shipped [[concepts/tristantube|TristanTube]] — the same move applied to a
single human curator ([[entities/tristan-hume|Tristan Hume]]'s refreshed YouTube tier list, ~47K videos, plus a
TV mode) instead of HN comment history. He described it as **"one-shotted with Claude Code in 3 minutes"**,
against HackerTube's ~2 hours. The gap is instructive: HackerTube's cost was dominated by Sonnet labeling ~40K
recommending comments, whereas a human-written tier list needs no labeling pass at all — i.e. **the
agent-build time is now proportional to how much curation work remains, not to app size**.

## Related

- [[entities/andrej-karpathy]] — creator
- [[concepts/agentic-engineering]] — supervisory agent workflow in practice
- [[concepts/vibe-coding]] — build style Karpathy himself coined (see [[entities/karpathy-writings]] MenuGen post-mortem)
- [[concepts/coding-agents/coding-agents]] — Claude Code as the build harness

## Sources

- Raw: `raw/articles/2026-10-31_karpathy-hackertube.md`
- HN discussion: https://news.ycombinator.com/item?id=50319510 (1449+ pts)
- Original post: https://karpathy.bearblog.dev/hacker-tube/
