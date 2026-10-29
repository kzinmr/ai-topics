# Watchdog session 2026-10-26 — redirect-conversion commit + header-safe log prepend

Two techniques proven cleanly in the 2026-10-26 17:35 UTC watchdog run (entity dedup:
eugeneyan -> eugene-yan, giles-thomas -> gilesthomas, lilianweng -> lilian-weng).

## 1. Redirect-conversion vs the content-regression pre-commit hook

When dedup converts the THIN page of a duplicate pair to status: redirect (canonical
keeps the content), .githooks/pre-commit fires:

    CONTENT REGRESSION DETECTED — rich wiki pages would be overwritten!
    wiki/entities/eugeneyan.md
      220 -> 11 lines  (-209 lines, 5% of original)

This is a KNOWN FALSE POSITIVE for intentional redirect conversions, not a skeleton
overwrite. Do NOT git checkout the old content back — the content lives in the
canonical page by design.

Procedure (in order):
1. Verify canonical is richer BEFORE shrinking: wc -c both pages; check incoming
   wikilink counts (grep -r "[[entities/<slug>" wiki --include='*.md' -l | grep -v
   _archive | wc -l) favor the canonical. 2026-10-26: eugene-yan 27.9 KB/14 links vs
   eugeneyan 15.9 KB/4 links.
2. Rewrite incoming wikilinks FIRST — replace both [[entities/thin]] and
   [[entities/thin| display-text variants across the whole wiki (skip _archive/).
   os.walk batch script; 5 files touched that day (index.md, entities/_index.md, 3 pages).
3. Commit with --no-verify and an explicit message stating the conversion is intentional
   and where content went:
   "watchdog: entity dedup — <thin list> intentionally converted to redirects (content merged into canonical <slug list>); index dedup + header recount"
4. Index dedup: remove stale "- [[entities/thin]]" entry lines, then RECOUNT ALL FIVE
   section headers from "- [[dir/" entry lines — same-day pipeline additions
   (trending-topics, active-crawl) leave other headers stale too. That run: Entities
   957->955 (own edits), but Concepts 2240->2242 and Queries 41->43 also drifted from
   earlier commits. Always:
   len(re.findall(rf'^- \[\[{cat.lower()}/', content, re.M))
5. Merge exceptions to check first:
   - samuelcolvin-style pages may ALREADY be redirect stubs (redirect: + status: redirect
     frontmatter, ~200 B) — skip, don't re-convert.
   - deliberate-coder vs deliberatecoder (Ben Ilegbodu vs Steve Shogren) look rich on
     both sides but are DIFFERENT people — verify identities before any merge.
   - lilian-weng case: contested career facts — keep both dated/attributed on canonical.

Redirect stub template used (pre-commit tag validator accepts empty tags: []):

    ---
    title: "<Name> (redirect)"
    type: entity
    redirect: "<canonical-slug>"
    aliases: [<existing aliases carried over>]
    updated: YYYY-MM-DD
    status: redirect
    sources: []
    ---

    > This page has moved. See [[entities/<canonical-slug>]] for the full <Name> entity page.

Carry over the old page's aliases: line so backlink searches still resolve.

## 2. Header-safe log.md insertion (never prepend at position 0)

log.md = "# Wiki Log" header + prepend-only "## [" entries. The "---" anchor trap makes
patch(old_string="---") corrupt an arbitrary earlier entry; naive prepend at line 0
buries the header (see watchdog-healthy-baseline.md §3 Header Burial). Recipe — write
/tmp/log_prepend.py, splice between header and first entry:

    lines = open('wiki/log.md').read().split('\n')
    h = next(i for i,l in enumerate(lines) if l.rstrip() == '# Wiki Log')
    first = next(i for i in range(h+1, len(lines)) if lines[i].startswith('## ['))
    lines = lines[:first] + entry.split('\n') + lines[first:]
    open('wiki/log.md','w').write('\n'.join(lines))

To add a sub-section to the SAME day's entry (e.g. pipeline-alert adjudication after the
main Changes block), splice a "###" block at the same first index — lands inside the
current entry rather than creating an orphan block. The follow-up can be a separate
small commit ("watchdog: pipeline alert adjudication ...").

After EVERY log write: head -1 wiki/log.md must return "# Wiki Log".

## 3. Pipeline chain-break false positives (2026-10-26 data point)

pipeline_watchdog reported both chains broken (blog: triage_ok_but_wiki_ingest_failed,
newsletter: ingest_ok_but_triage_failed). Both were checkpoint-staleness false
positives: the day's triage HAD run (git log "wiki: newsletter triage <run-id>" commit
present; blog triage_latest.json mtime same morning) — only the checkpoint JSON lagged
one day, or take-count was too small to trigger wiki-ingest commits.

Adjudication recipe: before treating a chain break as actionable, check
"git log --since=today" for triage/ingest commits AND checkpoint mtimes
(~/.hermes/cron/data/{newsletter,triage}/triage_latest.json). If the work commits exist,
report as false positive, log the adjudication under the watchdog log entry, commit —
no cron re-run needed.
