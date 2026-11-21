# Archive-only dreaming commit with NO log.md entry — downstream recipe (validated 2026-11-13)

## The detection gap

The SKILL.md "archive-only commit" variant relies on a **wording discriminator** in the
upstream log.md entry ("Reference candidate for enrichment" = future tense ⇒ not executed).
Degenerate case: the upstream dreaming-group commits `triage JSON + archive JSON +
archive_index.json + a skill recipe reference` and touches **no log.md at all**. Then
`grep "$(date +%F)" wiki/log.md | grep dreaming` returns nothing, which naively reads as
"nothing happened upstream, saturation, nothing to do."

Detection is one tool call and never ambiguous:

```bash
cd ~/ai-topics && git log --oneline -3 --format="%h %ci %s"   # find today's dreaming commit
git show --stat <sha>
```

Verdict table:

| `git show --stat` touches | Meaning | Downstream action |
|---|---|---|
| archive JSON + `archive_index.json` only | archive-only | **Execute the references** in `triage_latest.json` |
| archive JSON + `archive_index.json` + skill `references/*.md` | archive-only (this variant) | **Execute the references** |
| archive JSON + log.md + entity/concept pages | fully enriched | Skip enrichment, log + commit only |
| log.md only | stale earlier pass | Compare mtimes, see SKILL.md "log-only commit" variant |
| nothing today | upstream never ran | Run Pattern E yourself |

## Two consequences that look like failures but aren't

1. **`archive_triage.py dreaming --keep-reference` → `archived: 0, "All items already archived (dedup)"`.**
   Expected: upstream already pushed every decision URL into `archive_index.json`. Do NOT
   re-run expecting yield and do NOT conclude the triage was never archived. This is the
   SKILL.md Pitfall #23 absolute-saturation row, reached via a different path.
2. **The downstream log entry must itself name the upstream SHA and the `git show --stat`
   verdict.** Otherwise the next cycle sees a log entry describing enrichments and assumes
   the upstream also performed them (it didn't — it only triaged and archived).

## Session details (2026-11-13, commit `d1af70ad`, 4 files +79/-2, both hooks green first try)

- Upstream `6895a275` "dreaming: grouping triage … Takes=0/Refs=3/Skips=27, archive + 11-13
  recipe reference" → 3 files: `dreaming-group-triage-recipe-2026-11-13.md`,
  `archive_index.json`, `dreaming/2026-11-13_20261113T180045Z.json`. Zero log.md, zero pages.
- Checkpoint read directly (not the injected cron summary): `payload.articles: 0`,
  `recent_raw_articles: 222`, `existing_wiki_pages: 3382`.
- `triage_latest.json` field is `recommended_action` (3 × `reference`, 27 × `skip`).
- All 3 references verified as genuine gaps after reading both the raw article body AND the
  full target page:
  - `entities/hex-technologies.md` — page carried the Oct 27 Hex 4.0 **architecture** post and
    the Hero observability post, but not the Nov 12 **review-practice playbook** (250K LoC /
    4 months, exported-signature freeze, "DAMP", the wrapper-string static-break exit-criteria
    trick, YOLO "black box" regions). The "same company already has a section" trap.
  - `entities/pinecone.md` — the Oct integrated-embedding section covered Pinecone-hosted
    models only; the Nov 12 third-party Gemini Embedding 2 (Vertex AI serving, Pinecone
    invoice at Google list price, Builder 20M-token promo) was absent. Appended INTO that
    section rather than creating a new heading — same-thesis continuation.
  - `entities/cohere.md` — had North×Wiz agent + Model Vault but no security *leadership* hire
    / AISLE background. Added after the C$4B Canada section, before `## Related`.
- Tag/language gates: existing pages carried only SCHEMA-valid tags, so the only pre-commit
  risk was CJK. Ran a Python re-scan over the 3 touched files (`[\u3040-\u30ff\u4e00-\u9fff
  \uff00-\uffef\uac00-\ud7af]` → 0 hits) before staging. Staged 4 files explicitly (3 pages +
  log.md) — never `git add wiki/` (sibling untracked `wiki/raw/newsletters/*` from other jobs).
- No index.md change needed: 0 new pages ⇒ index untouched, and the log entry says so
  explicitly so the health-fix job doesn't chase a phantom count drift.

## Vendor-blog German-locale source

`sitemap_monitor` scraped Cohere at `cohere.com/de/blog/...` (German body). The body was still
complete and fully readable, so the reference was executable — do NOT skip a sitemap article
because the scrape landed on a non-English locale path. Verify the body has full content, then
note the locale caveat in the page's Source line: `(official post scraped in German; content
verified from the full body)`. This keeps the claim honest without a `本文未取得`-style CJK
gloss (the wiki language hook blocks those).

## log.md prepend (this session's working shape)

Header was healthy (`# Wiki Log` at L1, italic L2). Script pattern that produced a clean
+17/-0 diff: strip ALL header/italic lines wherever they sit, drop leading blanks, rebuild head
as `# Wiki Log\n\n_italic_\n\n` + entry + `\n` + rest. Post-verify cheaply instead of reading
the 700KB file: `grep -c '^# Wiki Log'` == 1, `grep -n '^_Log of all'` == 3,
`git diff --stat` is +N/-0 (a deletion count means the entry text was accidentally rewritten).
Entry authored via `write_file` to a **time-stamped** `/tmp/dreaming_log_<pipeline>_<date>_<hhmm>.md`
so sibling jobs can't collide on the path.
