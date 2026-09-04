---
title: "David Rosenthal (DSHR)"
description: "David S. H. Rosenthal (DSHR) — Google Chrome OS/Chromebook co-creator and co-leader; digital preservationist behind the 'long archive' thesis — AI can't read the data you can't open, and cheap storage's promise dies without storage economics"
type: entity
created: 2026-09-04
updated: 2026-09-04
tags:
  - person
  - blogger
  - ai-commentary
  - digital-preservation
  - storage-economics
  - user-rights
  - session-portability
  - culture
  - google
sources:
  - https://dshr.io/
  - https://blog.dshr.org/
  - raw/articles/2026-09-04_dshr-david-rosenthal-bio-verification.md
  - raw/articles/2026-09-04_dshr-you-cant-read-the-databits-you-cant-afford-to-store.md
  - raw/articles/2026-08-23_dshr-the-sad-near-death-experience-of-a-google-profile.md
  - raw/articles/2026-06-23_dshr-ais-affordability-crisis.md
  - raw/articles/2026-06-15_dshr-vibe-coding-for-fun-and-profit.md
---

# David Rosenthal (DSHR)

**David S. H. Rosenthal** (online handle **DSHR**, blog at [blog.dshr.org](https://blog.dshr.org)) is a longtime systems engineer best known as a co-creator and co-leader of **Google Chrome OS / Chromebook**, and — since leaving that world — a sharp, dryly funny commentator on **digital preservation, storage economics, and the practical limits of AI**. His central throughline: *the bits you can't open, or can't afford to keep, don't exist* — a claim that turns out to constrain AI as much as it constrains archives.

## Professional Background

- **Google Chrome OS / Chromebook**: Rosenthal was a co-creator and co-leader of the Chrome OS project (the Linux-based, browser-centric operating system that shipped first on Chromebooks in 2011). This is the credential most sources cite when identifying him; it grounds his systems-level credibility on operating systems, browsers, portability of user environments, and platform lock-in.
- **Long systems career**: a researcher/engineer whose interests span operating systems, storage systems, distributed systems, and the economics of keeping data alive. His blog (active since ~2003, per the archive structure) reflects this breadth — from deep storage/RAID/disk topics to AI policy to personal computing culture.

> *Verification note:* Wikipedia blocks crawling (403 for robots) and `dshr.io/about` returns a 404, so the Chrome OS co-creator/co-leader attribution above is corroborated by the bio text surfaced via search snippets rather than a directly scraped authoritative bio page. Treat finer claims (exact titles, tenure dates) as unverified until a primary source is reachable. See [[raw/articles/2026-09-04_dshr-david-rosenthal-bio-verification.md]].

## Core Thesis: The "Long Archive"

Rosenthal's defining intellectual project is the **long archive** — an archive meant to remain readable for centuries, not years. Two ideas carry it:

1. **The format trap.** Proprietary, app-bound formats rot fast; when the app dies or changes, the data becomes unrecoverable. His recurring advice — "choose your own document formats carefully" — is a preservation argument that doubles as a **user-rights / session-portability** argument (see [[concepts/google-profile-sunset]], [[concepts/session-portability]]).
2. **Storage is not free.** "It's the storage, stupid." Cheap storage is *necessary but not sufficient* — the promise of "store everything forever" dies on storage **economics**, not physics. His proposed fix is **"sustainable free storage"** as a new business model, with three conditions:
   - **Charge for work** — free capacity is fine; free *processing* (egress, compute) is the killer.
   - **Data dies unless someone cares** — free storage needs an "heir" to pay when the owner stops.
   - **Sustainable** — a model that doesn't collapse under its own maintenance cost.

### Why this matters for AI

The long archive reframes data as **the AI economy's non-renewable resource**. As AI models commoditize, proprietary data becomes the scarce asset — and if the AI industry keeps degrading data accessibility (login walls, ToS bans on scraping, proprietary app silos, "the user is the product"), the **absorption frontier** hits a **preservation wall**: *AI can't read the databits we can't open.* See [[concepts/ai-affordability-crisis]] and [[concepts/absorption-frontier]].

```
Bits exist = (you can open them) AND (you can afford to keep them)
   format trap  ─────────► you can't open them
   economics    ─────────► you can't keep them
                both bite AI
```

## Key Ideas

- **AI Affordability Crisis** — platforms subsidized intelligence to buy adoption; prices are now snapping back to real cost; the gap between platform revenue and compute cost is the core business challenge. See [[concepts/ai-affordability-crisis]].
- **The absorption frontier & the preservation wall** — data as AI's non-renewable input; accessibility decay (login walls, format rot) is a slow brake on AI capability. See [[concepts/absorption-frontier]].
- **Google Profile near-death experience** — a concrete preservation story: Google's "My Activity" redesign removed export capability for 20 years of location/voice history, violating Google's own 2011 "Download Your Data" promise. A case study in platform lock-in vs. user rights. See [[concepts/google-profile-sunset]].
- **Vibe coding is not new** — "coding by talking to it" has been the right approach to *hobbies* forever. His hobby-COBOL project (a grammar school report-card generator on IBM AS/400, ChatGPT-bridged RPG→COBOL→RPG) is a love letter to hobby programming and against the "everything must be monetized" mindset.

## Writing Style

Dry, self-deprecating, systems-engineer voice. Frames sweeping industry claims through concrete, personal, often nostalgic anecdotes (a 1975 report card; 20 years of pings; a dead spreadsheet). Numbers up front, punchlines at the end. Anti-hype: repeatedly grounds AI talk in *costs* and *bits you can actually read* rather than capabilities.

## Related Concepts

- [[concepts/ai-affordability-crisis]] — his platform-economics diagnosis of AI
- [[concepts/absorption-frontier]] — data as AI's non-renewable resource; the preservation wall
- [[concepts/google-profile-sunset]] — Google Profile / "Download Your Data" case study
- [[concepts/session-portability]] — "choose your own document formats carefully"
- [[concepts/vibe-coding]] — "not new" hobby-programming reframing

## Sources

- [DSHR blog](https://blog.dshr.org/) — primary source
- [dshr.io](https://dshr.io/) — personal site
- "AI's Affordability Crisis" (2026-06-23) — [[raw/articles/2026-06-23_dshr-ais-affordability-crisis.md]]
- "Vibe Coding is Not New" (2026-06-15) — [[raw/articles/2026-06-15_dshr-vibe-coding-for-fun-and-profit.md]]
- "The Sad Near-Death Experience of a Google Profile" (2026-08-23) — [[raw/articles/2026-08-23_dshr-the-sad-near-death-experience-of-a-google-profile.md]]
- "You Can't Read the Databits You Can't Afford to Store" (2026-09-01) — [[raw/articles/2026-09-04_dshr-you-cant-read-the-databits-you-cant-afford-to-store.md]]
