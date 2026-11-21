# Upstream dreaming-group output truncated → NO analysis to recover (validated 2026-11-11)

## Signature

Pre-run script:
```json
{"ok": false, "error": "failed to parse JSON response from dreaming-group output",
 "output_path": "/opt/data/.hermes/cron/output/<job-id>/<ts>.md"}
```

Output file is LARGE (5,347 lines here), which superficially matches Pitfall #12's
"2,000+ lines indicates the dreaming-group completed its analysis before the JSON render failed".
**It does not.** The final headings are:

```
## Script Output
# TOKEN USAGE TRACKING
## Error
RuntimeError: Response truncated due to output length limit
```

Nothing after `## Script Output` but the token line and the error. The upstream agent
generated **zero tokens of response** — the model hit the output-length ceiling while
still consuming the (huge) prompt. There is no `## Theme Clusters` section because none
was ever written.

## The grep trap

A naive `grep -n "^## \|Cluster\|Already Covered\|Action"` on the file returns hundreds
of matches and looks like an analysis exists. They come from the **injected checkpoint**:
`existing_wiki_pages` lists ~2,900 `concepts/...` paths, and the injected skill text
carries `## ` headings (`## Workflow`, `## Key Pitfalls`, `## Integration Points`...).
Those are prompt content, not triage output.

**Correct probe** — look at the tail headings only:

```bash
grep -n "^## \|^### \|^# " <output_path> | tail -12
tail -25 <output_path>
```

If the last headings are `## Script Output` / `# TOKEN USAGE TRACKING` / `## Error`,
the file is prompt-only. Stop looking for clusters.

## Also verify the other two sources before concluding

```bash
ls -la ~/.hermes/cron/data/dreaming/{triage_latest.json,grouped_themes_latest.json,latest.json}
readlink -f ~/.hermes/cron/data/dreaming/latest.json
```

Expect `triage_latest.json` + `grouped_themes_latest.json` to be **stale** (prior days —
their mtimes reveal it) while `latest.json` is today's. Confirm the prior triage was
consumed:

```bash
grep -n "dreaming" wiki/log.md | head -5
git log --oneline --grep="dreaming" -5
```

A prior triage whose run_id appears in a committed log entry is consumed → no carry-forward.

## What to do

Run Pattern E yourself, from scratch:

1. `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py`
   (full skill-dir path — NOT repo-root `scripts/`) → the never-triaged pool (66 here).
2. Cross-check same-day sibling decisions so you don't re-take their work:
   `~/.hermes/cron/data/blog_ingest/triage_latest.json`,
   `~/.hermes/cron/data/newsletter/triage_latest.json`, plus today's `git log --oneline`.
3. Read bodies of the sitemap (06:00) and trending (12:15) batches — the blog-ingest
   10:01 batch is usually already handled by blog-triage.
4. Coverage-verify each candidate by grepping the target page's **body** (not just
   filenames): `grep -n -i "<specific claim>" wiki/entities/<page>.md`.
5. Enrich / create; build the triage JSON (`source: "dreaming"`,
   `recommended_action` not `action`); `archive_triage.py dreaming --keep-reference`;
   log prepend via `repair_log_md_header.py` or the idempotent rebuild script;
   scoped `git add`; `git commit -m` (hooks pass when tags/wikilinks/CJK are clean).

## High-value discrimination found this run

- **Newsletter take ≠ wiki coverage.** Muse Ember was a `take` in newsletter-triage yet
  had **no concept page and no entity section** anywhere. Grep for the model name in
  `wiki/concepts`/`wiki/entities` before honoring "already taken by a sibling".
  Re-taking it as a page creation was correct.
- **Locale-duplicate sitemap scrapes.** `cohere.com/de/blog/...` is the German mirror of an
  English post already documented in `entities/cohere.md`. Check the URL path for a
  locale segment (`/de/`, `/fr/`, `/ja/`) before treating it as new.
- **Scrape-failure stubs**: `Parallel ... scale-plan` was 14 lines containing
  `Scrape failed: brotli: decoder process called with data when 'can_accept_more_data()' is False`.
  Also 23-line bodyless shells (Factory `security-factory`). Both archive as skip; no body = no claim.
- **Already-covered classics verified with line refs**: Goldman Claude Code pull →
  `concepts/ai-engineering-dekilling.md` L40; LoreKit OpenTelemetry-memory essay →
  `concepts/ai-agent-memory-two-camps.md` L162.

## Cost note

This variant is the most expensive dreaming path (~35 tool calls) because the triage
work is duplicated inside the ingest job. If it recurs, the fix belongs upstream:
the grouping prompt injects the full `existing_wiki_pages` list (~2,900 lines) which is
likely what blows the output budget. Trimming that list in `dreaming.py` (e.g. emit a
count + prefix index instead of every path) would restore upstream analysis generation.
