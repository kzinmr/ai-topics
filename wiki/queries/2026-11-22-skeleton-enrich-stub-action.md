---
title: "Skeleton enrichment run — 2026-11-22 (speedrun contributor cluster)"
type: query
created: 2026-11-22
updated: 2026-11-22
tags:
  - query
  - knowledge-management
sources: []
---

# Skeleton enrichment run — 2026-11-22

> Snapshot note from the `skeleton-enrich-daily` cron run (2026-11-22 19:0x UTC).
> The `status: skeleton` backlog remains **empty** (streak since 2026-10-17). As in the
> 2026-11-11/12/13/15/18/19/21 runs, productive action was taken on the `status: stub`
> backlog — this time the **nanoGPT speedrun contributor cluster** deferred by the
> 2026-11-21 run: `jxbz`, `brendanh0gan`, plus two new entities surfaced during
> research: `leloykun`, `you-jiacheng`.

## Actions this run (2 enriched, 2 new pages)

| Page | Before | After |
|------|--------|-------|
| `concepts/jxbz.md` | 252 B stub | ~4.9 KB — **Jeremy Bernstein**, Muon co-creator; identity verified via GitHub API (jxbz = jeremybernste.in = Thinking Machines Lab); "Deriving Muon" theory section; record #3 credit; Bernstein & Newhouse draft-origin story |
| `concepts/brendanh0gan.md` | 252 B stub | ~2.8 KB — record #11 sole credit (U-net + double LR); #20 first-sub-3-min team; "Brendan Rappazzo" via project citation (flagged inference); GitHub 404 negative finding; `status: stub` retained (identity unverified) |
| `entities/leloykun.md` | (new) | ~2 KB — Franz Louis Cesista; #15/#20/#21 records; Muon co-author |
| `entities/you-jiacheng.md` | (new) | ~2 KB — You Jiacheng (IIIS Tsinghua); solo #15–#17, #19 value-embedding streak; Muon co-author |

## Method notes

- **web_search tool unavailable** in this session; DuckDuckGo/Google endpoints
  bot-blocked. Fell back to **GitHub REST API + Jina Reader + arXiv API**, which turned
  out to be strictly better sources (primary attribution data).
- The modded-nanogpt **README record table** is the authoritative attribution source —
  it names the credited contributor per record and includes the formal citation with
  real names ("Brendan Rappazzo", "Braden Koszarsky", "Boza Vlado", "Franz Cesista",
  "Jiacheng You") — a reusable cross-reference between handles and names.
- Suggested SCHEMA tag check: all tags pre-registered; no SCHEMA edits needed.

## Remaining backlog

~384 `status: stub` pages. Next-run candidates: org/tool-shaped stubs in `concepts/`
(`cyd`, `genie`, `synth`, `quepid`, `spegel`, `botnet`, `prodng`, `katerra`, `dingcad`,
`pallets`, `placeiq`) — the same GitHub/registry-first pattern applies.
`KoszarskyB` (Braden Koszarsky, records #12/#14/#18) is a promising full-entity candidate.
