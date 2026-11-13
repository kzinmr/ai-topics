# Dreaming-group triage recipe — 2026-11-13 (0-article checkpoint, Takes=0 / Refs=3)

## Situation

- Checkpoint `20261113T180045Z`: `total_articles: 0`, `recent_raw_articles: 222`, injected `articles: []` → Pattern E trigger.
- `triage_latest.json` was STALE (`20261111T180052Z`, 4 takes + 10 skips) — confirmed consumed by the 11-11 dreaming wiki-ingest log entry (log.md L181: "1 new page + 3 enrichments" all committed). No carry-forward takes.
- No 11-12 dreaming entry exists (the 11-12 cycle appears to have been skipped/failed) → the 3-day absence-list (52 never-archived) includes 11-12 items, but those were largely consumed by the 11-12/11-13 blog-triage.

## Duplicate check (all confirmed via git log + log.md before triaging)

Same-day jobs that had already consumed the 10:01/06:00/12:05 batches:
- `c6436410` blog-wiki-ingest (NVIDIA CEO transition, Gemini 4 Hydrogen, Modal burst pricing, Hotz First Strike, Pluralistic)
- `cf8be8c3` trending-topics (checkpoint forensics/Blackwell fingerprint, Edge0-145B, x402, Nvidia petition, Anthropic IPO front page)
- `89a6d22f` night hot-post (checkpoint forensics), `b41fa679` morning hot-post
- `events/nvidia-ceo-transition-2026.md` verified to contain the Wired petition section (L58) — skip despite absence-list hit.
- `entities/george-hotz.md` L122 verified to contain the Nov 13 First Strike entry — skip despite absence-list hit.

## Probe

`config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py` → 52 never-archived across 3 days (index at 3,183 URLs). The absence list correctly flagged the NVIDIA-petition and Hotz articles even though they were same-day covered — line-level grep verification, not the absence list alone, was the decisive signal for those skips.

## Outcome

Takes=0, References=3, Skips=27 (30 decisions, run_id-keyed file, archived 26 + 4 dedup, total_archive_urls → 3,209).

Reference candidates (gaps verified by grep returning 0 hits on the target page):
1. **Hex "working with robots to rewrite Hex"** → `entities/hex-technologies.md`. Substantive agent-collaboration methodology (TODO-skeleton PRs, DAMP-not-DRY, statically verifiable exit criteria, robots produce "production code immediately" not code that ladders). Hex DOES publish real engineering posts alongside marketing (matches the 2026-08-14 DataBench counter-example) — never batch-skip Hex.
2. **Pinecone integrated embedding + Gemini Embedding 2** → `entities/pinecone.md` (extends the Oct 2026 Integrated Embedding section L179-189, vendor-extension only).
3. **Cohere first CISO (Jaya Baloo, AISLE co-founder)** → `entities/cohere.md`. Scraped from the /de/ locale — content identical to the English post; do not treat the German text as a different article.

## Notes

- ElevenLabs `customer-service-skills` raw is a 462B brotli-decoder scrape-failure stub — skip, cannot judge from body.
- Factory `cyber-defense-network` is a 511B bodyless shell (same pattern as the 11-11 `security-factory` shell).
- Harvey ×3 author-profile pages + ×2 nav-chrome product posts batch-skipped per Pattern E.
- This job is GROUPING ONLY — enrichments deferred to dreaming-wiki-ingest. The triage JSON at `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` carries `source: "dreaming"` and `recommended_action` on every decision with `body_excerpt`.
