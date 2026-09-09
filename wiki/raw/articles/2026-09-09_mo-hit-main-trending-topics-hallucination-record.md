---
title: "Trending-topics hallucination record: entities/mo-hit-main"
source_url: https://news.ycombinator.com/item?id=49505310
created: 2026-09-03
updated: 2026-09-09
note: |
  Provenance and verification record for a hallucinated entity injected into wiki/index.md
  by the trending-topics run of 2026-08-31. This file exists so the false claim stays
  quarantined with its disproof attached, and so future lint runs can recognize the pattern.
confidence: none
---

# Trending-topics hallucination record: "Mo Hit Main"

## The claim that was injected

The `trending-topics` run of **2026-08-31** (commit `d0b026bf`) added this line to `wiki/index.md`:

> `[[entities/mo-hit-main]]` — Mo Hit Main — Takumi Handa's Japanese LLM/generative-AI publishing hub (52k+ X followers, 5,600+ note writers, 1,000+ articles, weekly AI news 300+ issues)

The accompanying log line read only: `index.md: added entities/mo-hit-main`.

## Why it is a hallucination

1. **No source in the report itself.** The report that commit also wrote — `inbox/rss-scans/trending-topics-2026-08-31.md` — contains **zero** occurrences of `mohe`, `handaline`, `Handa`, `半田`, `52k`, `5,600`, "hub", or "unicorn". Every one of the report's eight items is a real, HN/newsletter-sourced story (OpenClaw 2.0 + Summer Yue inbox deletion, Auto Mode exploit ASR, Debian GR vote, Willison's ChatGPT Work teardown, moz:fest talk, NanoGPT speedrun, Meta Muse Glimmer, context-compaction safety trend). The index line has **no antecedent anywhere** — not in the report, not in any raw article, newsletter, transcript, or X bookmark in the repo.
2. **The name resolves to nothing.** "Mo Hit Main" is not a plausible rendering of any real handle. `entities/mo-hit-main.md` did not exist until wiki-health auto-fix created a stub for the ghost index entry (commit `0026a3d6`) — i.e. the stub was reconstructed **from the hallucinated claim itself**, not from a source.
3. **The nearest real accounts don't match** (verified 2026-09-03 and again 2026-09-09).

## Verification performed

### 2026-09-03 (skeleton-enrich-daily) — see [[raw/articles/2026-09-03_note-mohejapan-profile-scrape]]

- `note.com/mohejapan` = **もへじのお部屋** ("Moheji's Room"). Content is the **楽々古事記** ("Easy Kojiki") mythology-commentary series — **not** LLM/generative-AI content, and no hub branding.
- X `@handaline` (plausible handle for "Handarin" / Takumi Handa): **does not exist** (X API v2 resource-not-found).
- X `@moheji1`: exists, but belongs to **茂木秀樹 (Hideki Motegi)** — a different person.
- Japanese-language web searches (もへじ + LLM / ハンダリン / Takumi Handa / 半田匠): no corroborating results.

### 2026-09-09 (skeleton-enrich-daily, fresh re-check)

- X API `users/by/username/mohejapan` → empty result (`{}`; no such user).
- `r.jina.ai/https://note.com/mohejapan` → live scrape confirms 楽々古事記 series still current (entries 48–50 in the last 10 days, newest "楽々古事記【50】神武天皇の建国"), pinned article "もへじのプロフィール" from ~2022. Still **no AI/LLM content**, no follower/article statistics, no connection to anyone named Handa.
- Re-read of `inbox/rss-scans/trending-topics-2026-08-31.md`: still zero matching terms.

## Conclusion

The entity is a **generation-step hallucination**: the trending-topics agent emitted an index entry with specific quantitative claims (52k+ followers, 5,600+ writers, 1,000+ articles, 300+ issues) that were never present in its own collected data. This is the second confirmed hallucinated person in this wiki, alongside the [[entities/adam-rosenthal]] forename artifact.

## Disposition

- The claim is **not repeated as fact anywhere** in wiki prose outside this quarantine record.
- The stub page is kept only so the index wikilink resolves. Deletion (page + index entry) requires a **manual decision by kzinmr** and is deferred rather than executed by cron, so the hallucination-cleanup pattern stays auditable.
- **Follow-up for trending-topics hygiene**: the run should be constrained so index entries are only added when the report body contains a matching named entity + URL. See [[config/hermes/skills/_overrides/trending-topics-reporting/SKILL]] (candidate-viability-gate reference).
