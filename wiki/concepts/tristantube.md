---
title: "TristanTube: Karpathy's Claude-Code One-Shot YouTube Curation Apps"
type: concept
created: 2026-11-07
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
  - https://karpathy.ai/tristan-tube/
  - https://thume.ca/2026-11-01/youtube-tier-list-2026/
  - https://x.com/karpathy/status/2119114537442189652
  - raw/articles/2026-10-31_karpathy-hackertube.md
---

# TristanTube

**TristanTube** (karpathy.ai/tristan-tube/) is a single-page YouTube viewer [[entities/andrej-karpathy|Andrej Karpathy]]
built **2026-11-07**, quoting [[concepts/hackertube|HackerTube]]. It renders **Tristan Hume's** curated YouTube
tier list as a browsable app: **~47,000 videos** across the tiered channel list, plus a **"TV mode"** for
hands-off/laid-back watching. Karpathy's headline claim: **"One-shotted with Claude Code in 3 minutes."**

## What it is

Source material is Tristan Hume's 2026-11-01 post "My YouTube tier list, six years later" — a refresh of his
2020 tier list, graded **S 5 / A 14 / B 12 / C 33 / D 92**. The S tier is the tell about the taste being
encoded: **Applied Science** (Ben Krasnow — electron microscopes, aerogel, plasma sputtering chambers),
**Clickspring** (clockmaking / Antikythera mechanism reconstruction), and **Stuff Made Here**. Hume's framing:
*"the best YouTube channels to be some of the most awesome content on the internet for learning interesting
things."*

Karpathy's build wraps that editorial judgment in a player UI: numbered keyboard jumps (`1–9`, `10–90%`),
`N`/`P` for next/previous, `Space` pause, arrow-key ±10 s seek, `M` mute, `Esc` to exit TV mode, and a
"Surprise me?" randomizer. It is a **viewer over someone else's curation**, not an algorithm.

## The pattern this establishes

Together with [[concepts/hackertube|HackerTube]] (2026-10-31, ~2 hours with Opus 5.5, 43M HN comments →
6,454 videos), TristanTube is the second instance of the same move:

> **Take a trusted human's explicit preference list and hand it to a coding agent as a curation corpus,
> rather than accepting an engagement-optimized feed.**

| | HackerTube | TristanTube |
|---|---|---|
| Curated by | Hacker News comment history (43M comments, 20 yrs) | Tristan Hume (one person's tier list) |
| Output | 6,454 videos, 150 topics | ~47K videos from 66 tiered channels |
| Build time | ~2 hours, Opus 5.5 | ~3 minutes, one-shot Claude Code |
| Hosted | hackertube.org (own VPS + domain) | karpathy.ai/tristan-tube/ |
| Mode | ForYou, account-free | TV mode + tier browsing |

The two-week drop from ~2 hours to 3 minutes on a comparable task is the more newsworthy datapoint — it is a
clean, self-reported measure of the **one-shot capability curve** for small web apps, and it matches
[[concepts/agentic-engineering]]: the human supplies taste and the target, the agent supplies the entire
implementation. Note the asymmetry with HackerTube's disclosed economics (504M input / 7.6M output tokens,
mostly Sonnet labeling) — TristanTube needed no labeling pass at all because the tier list was already curated
by a human, which is why it was ~3 minutes instead of hours.

## Skepticism / open questions

- **"One-shotted in 3 minutes" is self-reported** and unverified; no token count or repo was published, unlike
  the HackerTube HN thread where Karpathy did disclose numbers.
- These are **taste-filtered, not quality-filtered**: both apps encode the preferences of one person (Hume) or
  one community (HN), and both inherit that blind spot. See [[concepts/agent-native-tool-fallacy]] for the
  adjacent argument that bespoke curation tooling converges on generic tooling.
- Durability: HackerTube's server code was unpublished ("a vibe coded mess"); TristanTube appears to be a
  static page on an existing domain, i.e. near-zero maintenance — which is exactly Karpathy's own contrast
  with his earlier, sunset arXiv Sanity tool (see [[entities/andrej-karpathy]]).

## Related

- [[concepts/hackertube]] — the Oct 31 precursor this quotes
- [[entities/andrej-karpathy]] — builder
- [[concepts/vibe-coding]] — the build style
- [[concepts/coding-agents/coding-agents]] — Claude Code as harness

## Sources

- App: https://karpathy.ai/tristan-tube/
- Source tier list: https://thume.ca/2026-11-01/youtube-tier-list-2026/
- Announcement: https://x.com/karpathy/status/2119114537442189652 (4,477 likes / 364K impressions at scan time)
- HackerTube raw: `raw/articles/2026-10-31_karpathy-hackertube.md`
