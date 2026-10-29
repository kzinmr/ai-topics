# Dated triage pattern index (Oct 2026 additions)

Glob `references/newsletter-triage-2026-*.md` and `references/blog-triage-2026-*.md`
for the full set. This file indexes the October 2026 additions and the concrete
gap-detection recipes they established.

## newsletter triage 2026-10-29 (run_id 20261029T101049Z)

5 newsletters / 100 links -> 4 takes, 1 reference, 91 skips.

### Inbox pre-triage summary was accurate and saved ~15 tool calls

`wiki/raw/inbox/newsletter-ingest/{run_id}-triage.json` correctly identified all 5
publications (including disambiguating `source_name` = article title vs real
publication), assigned critical/high/low, and listed `existing_wiki_overlap`
candidates + `canonical_url` for the 4 Substack items. Trust its publication-id
and priority ordering; still resolve URLs for content verification. It also
correctly flagged the beehiiv item as "test ONE v2/c/ link before assuming
blocked" - the test returned a Cloudflare challenge, so that whole digest collapsed
to 1 reference decision instead of 20 resolution attempts.

### "Paywalled at para N" is still a take decision

The Signal (`thesignal.substack.com`, pub 293154) gated after 16 paragraphs. Those
16 carried every load-bearing number, so the item rated 4 stars as an
existing-page update. Gate location is not a proxy for value. Extract the full
public portion first, then decide.

### Gap-detection recipe: numeric-fact grep, not keyword grep

For financial/infrastructure claims, grep for the SPECIFIC figures, not the topic
word. Topic words exist everywhere in a mature wiki; the numbers do not.

```bash
cd ~/ai-topics/wiki
grep -rn "35.6bn\|10.6bn\|achilles\|railway" \
  concepts/subprime-data-center-crisis.md concepts/ai-bubble-financial-crisis.md entities/coreweave.md
grep -rin "culper\|electromigration\|short.sell\|arrhenius" entities/cerebras-systems.md
```

0 hits on the specific figures = genuine gap even when the umbrella topic page is
rich. This is what turned two would-be skips into takes:

- `entities/cerebras-systems.md` (164 lines, updated 2026-08-19) had zero mentions
  of the Culper Research short-seller report / electromigration dispute -> genuine
  contested-coverage gap, take as existing-page update.
- `concepts/subprime-data-center-crisis.md` covered the data-center-credit thesis
  but none of the bond/capex figures -> same treatment.

### Missing-page detection: enumerate the sub-index, don't trust the family page

`concepts/ai-benchmarks/aa-briefcase.md` existed (a v5 *component*), which is a
false-positive coverage signal for the umbrella index itself. Listing the whole
directory and grepping for "Intelligence Index" showed that after ~30 pages cite
"Artificial Analysis Intelligence Index v4.x" scores, no page *defines* the index.
When many pages reference a metric and none defines it, that is the strongest
possible new-page signal (5 stars).

### Same-author different-beat: raw article on disk but Layer 2 untouched

Simon Willison's vibe-game post was scraped by blog-ingest at 10:01 UTC
(`raw/articles/simonwillison.net--2026-oct-28-vibe-game-development--2fcae885.md`)
but his entity page's "Recent Notes" stopped at 10/26 and the vibe-coding concept
page had no game content. A raw article on disk is NOT coverage. Check:

1. does the author entity page's newest dated note precede the article date?
2. does the concept page actually contain the article's specific claims?

If both no -> take (existing-page update), and cite the existing `raw_path` so
downstream does not re-fetch.

### Stale blog-triage JSON: check `triage_timestamp` before using it as dedup

`${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json` was from
`20261026T100303Z` (3 days old) during the 10/29 run. Reference-only context, not
same-day dedup evidence. Always print and date-check it.

### Archive run shape

`python3 ~/ai-topics/scripts/archive_triage.py newsletter --keep-reference` returned
`{"candidates": 92, "new_archived": 50, "dedup_skipped": 42,
"total_archive_urls": 2954}`. A large `dedup_skipped` is expected for the
generated chrome/redirect placeholder URLs (they repeat across runs). Commit only
the archive file + `archive_index.json` with targeted `git add` - sibling wiki jobs
leave unrelated modified files in the tree the same hour.
