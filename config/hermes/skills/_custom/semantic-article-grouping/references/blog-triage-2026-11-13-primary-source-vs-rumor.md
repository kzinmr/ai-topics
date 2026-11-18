# Primary-source-vs-rumor cross-pipeline dedup (blog-triage, Nov 2026)

## Pattern: newsletter-triage ran first, blog batch carries the official primary source

When newsletter-triage has already committed for the same day (verify: `git log --oneline` shows a `wiki: newsletter triage <run_id>` commit today; grep log.md for the event keyword), do NOT auto-skip blog candidates covering the same event. The blog batch often carries the **official primary source** (company press release, canonical announcement page) that the newsletter cycle only had secondary coverage of.

**Concrete validation (2026-11-13, run 20261113T100036Z):**
- Newsletter triage (`f05f8d17`, 5 digests) covered the Jensen Huang resignation via newsletter digests.
- `entities/jensen-huang.md` carried a "Board preparing to oust him (Nov 11)" section explicitly caveated as *reported preparation, rumor-level*.
- Blog-ingest delivered `nvidianews.nvidia.com--news-nvidia-announces-ceo-transition--d22abd9c.md` — the official NVIDIA press release establishing: immediate resignation as President/CEO/board member, CFO Colette Kress as Interim CEO (retaining CFO role), Harvey C. Jones appointed first-ever Board Chair, permanent CEO search initiated.
- None of these confirmed facts existed anywhere in the wiki → **take ★★★★★** (events/nvidia-ceo-transition-2026.md + jensen-huang.md status-caveat update), while the TechCrunch "agrees to testify" follow-up was reference (absorb into the same event page).

## Decision test

For each same-event blog candidate after a newsletter cycle:
1. Read the existing page's actual content sections + `updated:` date — not just topic presence.
2. Ask: does the page contain the SPECIFIC facts this raw article establishes (names, titles, effective dates, official quotes)?
3. If the raw article is an official/primary source that CONFIRMS or SUPERSEDES a rumor-stage page → `take` (existing-page update, optionally a new `events/` page). Rumor→confirmed transitions are exactly the high-value updates triage exists to catch.
4. Secondary follow-up coverage of the same confirmed event (news aggregating the release) → `reference`, note it folds into the take's page.

## Companion yield observations from this run (14 candidates + 6 unsaved → 5/3/7+1)

- Company press releases swept in via Daring Fireball's `source_name` (daringfireball.net) are still primary sources — judge by URL/domain (`nvidianews.nvidia.com`), not the aggregator's source_name.
- A Simon Willison plugin-release post can be a ★4 take when it is the **first primary source for a new model tier** (Gemini 4 Hydrogen pricing table absent from `concepts/gemini/`) — do not batch-skip all `Release:` posts.
- Large Pluralistic posts (20KB) can still be reference: check whether the entity page already has recent same-author sections covering the same thesis (Doctorow's Uber-AI-replacement theme already in a June 19 section).
- unsaved_articles batch entry worked cleanly as a single skip decision with `body_excerpt: "（unsaved_articles — 抽出不可）"` and a durable-lead note for the one re-evaluation candidate (paywalled Reuters/WSJ pieces + Gary Marcus/Eli Lilly un-read).
