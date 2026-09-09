---
title: "Mo Hit Main (hallucinated entity — quarantine)"
created: 2026-08-31
updated: 2026-09-09
type: entity
aliases: [mo-hit-main]
tags: [person, content-creator, blogger]
sources:
  - raw/articles/2026-09-03_note-mohejapan-profile-scrape.md
  - raw/articles/2026-09-09_mo-hit-main-trending-topics-hallucination-record.md
confidence: none
status: hallucination-quarantine
---

# Mo Hit Main — hallucinated entity (quarantined)

> **⚠️ This entity does not exist.** The page was reconstructed as a stub from a broken `index.md` entry that the `trending-topics` run of 2026-08-31 emitted with **no supporting source in its own report**. Three verification passes (2026-09-03, 2026-09-09 ×2) found nothing. Full provenance and disproof: [[raw/articles/2026-09-09_mo-hit-main-trending-topics-hallucination-record]].

## What was claimed (and why none of it is usable)

The 2026-08-31 index line asserted a "Takumi Handa" Japanese LLM/generative-AI publishing hub with 52k+ X followers, 5,600+ note writers, 1,000+ articles, and a 300+-issue weekly AI news series. **No figure in that sentence has a traceable source**, and the report the same commit wrote contains no mention of the entity at all. Treat every number as fabricated.

## Verification history

| Date | Check | Result |
|---|---|---|
| 2026-09-03 | `note.com/mohejapan` scrape | "Rara Kojiki" Kojiki mythology series — no AI content, no hub branding |
| 2026-09-03 | X `@handaline` | user does not exist (API resource-not-found) |
| 2026-09-03 | X `@moheji1` | exists but is Hideki Motegi (茂木秀樹) — different person |
| 2026-09-03 | Japanese-language web searches (moheji+LLM, "Handarin", Takumi Handa) | no corroboration |
| 2026-09-09 | X API `users/by/username/mohejapan` | empty result |
| 2026-09-09 | live re-scrape of note profile | still Kojiki series only (entries 48–50); no stats, no AI content |
| 2026-09-09 | re-read of trending-topics 2026-08-31 report | zero matching terms |

## Disposition

- Kept as a **quarantine stub** so the index wikilink resolves; the false claims live only in the raw-article record above, with their disproof attached.
- **Do not enrich.** If kzinmr approves cleanup, delete this page and its `index.md` entry — cron deliberately does not delete entity pages.
- This is the wiki's second confirmed hallucinated-person artifact (see [[entities/adam-rosenthal]], a mis-prefixed forename for [[entities/dshr]]). Both point at the same class of failure: **index entries created without a source-backed antecedent**.

## Related

- [[raw/articles/2026-09-09_mo-hit-main-trending-topics-hallucination-record]] — full provenance/disproof
- [[entities/adam-rosenthal]] — the other confirmed identity artifact (resolved, unlike this one)
