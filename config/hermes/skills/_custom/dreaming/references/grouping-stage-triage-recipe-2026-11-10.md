# Grouping-Stage Triage Recipe — 2026-11-10 (Takes=0, Refs=2)

Rules specific to the **dreaming-group** (triage-only) stage that the main SKILL.md doesn't
carry cleanly. The group job produces `triage_latest.json` for the 18:20 `dreaming-wiki-ingest`
downstream; it does NOT edit wiki pages. Validated 2026-11-10.

## Checkpoint shape (re-confirmed)
`latest.json` → `p["payload"]["articles"]: []`, `recent_raw_articles: 229`,
`existing_wiki_pages: 3366` = Pattern-E trigger. The cron-injected `<data>` block matches the
on-disk checkpoint here, but when they disagree TRUST THE CHECKPOINT (see main SKILL).

## Decisive probe
`python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py`
→ this run: "Recent files (3d): 85 / Archive index urls: 3128 / Total never-archived: 67".
The 06:00 UTC sitemap batch + the 12:15 UTC trending batch were all absent = never triaged.
This is the ground-truth untriaged pool; the upstream candidate list is not.

## RULE A — trending-topics 'Raw:'-saved batch is NOT a dreaming take
trending-topics runs 12:00 UTC, ~6h before dreaming. When its log.md entry lists files under
`Raw:` + `SCHEMA: minted ...` but created NO concept page for a hot item, that is still the
sibling job's output to finish — NOT a gap dreaming should take. Re-taking it in the night
cycle = duplicate creation of a page the 12:00 job deliberately left as raw+SCHEMA-mint.
Concrete 2026-11-10: Strands Decider (Amazon replacing Sonnet 4.6), H100 pricing spread,
Gemini human annotators — raw saved + `strands-agents` SCHEMA-minted by commit `1d0cffa4` /
log.md L44-50, no concept page → **skip**, not take. Detection: `grep -n "Raw:" wiki/log.md`
on today's trending-topics entry; if your candidate's filename appears there, skip it.
Do NOT conclude the item is unhandled just because `find wiki -iname "*keyword*"` returns
only the raw file — trending saved it on purpose.

## RULE B — brotli scrape-fail stubs are bodyless → batch-skip + archive
Sitemap scrape of some vendor blogs (parallel.ai confirmed) yields a file whose entire body is
`Scrape failed: brotli: decoder process called with data when
'can_accept_more_data()' is False` (hundreds of bytes, `wc -c` ~400). No article body, not
rescuable at this stage. Batch-skip these alongside genuine marketing posts; still archive
so the URL enters `archive_index.json` and future cycles stop re-surfacing them. Do NOT
attempt a take from a title alone (BODY-READING MANDATE). Same class as the "stub-raw"
2026-11-09 note (bodyless index pages) — different cause (decoder fail vs index page), same
disposition.

## RULE C — triple-target safety incident (extends dual-enrichment)
A single vendor-breach article can warrant THREE pages, not the one `candidate_wiki_path`
the triage engine picks. 2026-11-10: Fireworks AI inference-provider breach leaking Notion AI
customer conversations (HN 64pts, item 50437106) → all three were zero-coverage:
  1. `concepts/ai-agent-safety-incidents.md` — the new incident class (inference-API-vendor
     compromise propagating to SaaS-customer conversation logs)
  2. `concepts/ai-supply-chain-security.md` — the third-party-vendor exposure-surface angle
  3. `entities/fireworks-ai.md` — provider-side incident record (page existed, updated
     2026-10-23, no breach section)
Detection: when an incident names a vendor + a downstream SaaS customer, grep BOTH safety
concept pages AND the vendor entity page for the vendor/customer names. Hand the ingest job
all three paths with per-side framing (safety-incident class / supply-chain exposure /
provider incident log) and add the raw source to each frontmatter. The reusable durable
analysis angles from this class: ZDR-by-default vs customer-side retention config ("how is
there anything to leak unless the customer configured retention?"), Enterprise-plan-gated
affected-member visibility as an ops failure, undisclosed compromise scope.

## Verified-smooth mechanics (no change needed, just confirmed)
- Builder script via `write_file`→`terminal python3` (CJK reasons), `ast`-clean, 6 decisions,
  `Takes=0 Ref=2 Skip=4`, field-completeness self-check passed.
- `archive_triage.py dreaming --keep-reference` → 6 candidates / 6 new / 0 dedup / index
  3128→3132; `archive_path` printed under the `/opt/data/.hermes/home/ai-topics` symlink
  prefix (Pitfall — readlink resolves to canonical, file is in the right place).
- Wide sibling-dirty tree (64 files from other jobs) → staged ONLY archive JSON +
  archive_index.json; commit `67b6083d` hooks green, no `--no-verify`. Plain `git push`
  (skipped `pull --rebase` per Pitfall #26).
