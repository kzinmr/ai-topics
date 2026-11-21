# Grouping-Stage Triage Recipe — 2026-11-04 (dreaming-group, validated)

Context: dreaming-group cron (18:10 UTC). Checkpoint `total_articles: 0`, `recent_raw_articles: 257`.
Earlier jobs that day had failed with HTTP 503 / response truncation (blog-triage, dreaming-wiki-ingest,
newsletter-wiki-ingest per the watchdog diagnosis entry), which left a never-archived, never-triaged pool
plus one orphaned raw article (SemiAnalysis SpaceX) untracked in git. The group job recovered cleanly.

## Working sequence (the run that produced Takes=3 Ref=3 Skip=4 in ~15 tool calls)

1. **Duplicate check first** (cheap, one batch): `git log --oneline -15` + `grep "$(date +%F)" wiki/log.md | head`.
   Read the day's trending-topics / active-crawl / blog-ingest / manual-backfill entries — anything their log
   lines explicitly claim covered ("sibling WIP", "skipped as covered") is a skip, no re-verification needed.
2. **Archive-index absence probe as the decisive pool**: `python3 config/hermes/skills/_custom/dreaming/scripts/check_archive_index_absence.py`.
   The output's "Never archived" list IS the triage pool. Read only the top AI-relevant files from it.
3. **Per-candidate coverage check**: grep the raw's specific claims (numbers, product names) in the candidate page —
   a `grep -n "<product name>" wiki/entities/<page>.md` miss plus a stale `updated:` date = genuine gap → take.
   Same-day sibling log mention = skip. Sources-frontmatter presence ≠ content (unchanged rule).
4. **Triage JSON**: write builder to `/tmp/` via write_file (CJK reasons — never heredoc),
   `compile()` pre-check, then `python3 /tmp/x.py`. Field is `recommended_action`. source: "dreaming".
5. **Archive**: `python3 scripts/archive_triage.py dreaming --keep-reference`.
6. **Log prepend with header normalization** (see below), then selective `git add` of exactly your files:
   log.md + dated archive JSON + archive_index.json + any orphaned raw you commit on behalf of a failed sibling job.

## Log.md header states seen (all handled by ONE normalize-then-prepend script)

Healthy file: L1 `# Wiki Log`, L3 italic. A sibling (watchdog) prepend can leave **single header at L1 but the
italic line buried at L24** — the header-count check (`grep -c '^# Wiki Log'` == 1) looks clean and only the
italic line's position reveals it. Anchoring a prepend on the italic line would then insert at the buried
position. Canonical script shape:

```python
lines = open(LOG).read().split("\n")
drop = {i for i,l in enumerate(lines) if l.strip()=="# Wiki Log" or l.strip().startswith("_Log of all wiki changes")}
body = [l for i,l in enumerate(lines) if i not in drop]
while body and body[0].strip()=="": body.pop(0)
entry = open(ENTRY).read().rstrip("\n")
new = ["# Wiki Log","", "_Log of all wiki changes. Newest entries at top._","", entry,""] + body
open(LOG,"w").write("\n".join(new))
```

Post-verify (cheap, no full read): `grep -c "^# Wiki Log"` == 1, italic at line 3, your `## [date]` heading at ~L6,
`git diff --staged --stat` shows a small insertion (a ~20-line entry ≈ +17/-2).

## Grouping-stage scope reminder

dreaming-group is TRIAGE ONLY — takes/references land in triage_latest.json for dreaming-wiki-ingest; do not
edit entity/concept pages from this job. What the group DOES commit: log.md entry + archive JSON + archive_index.json
(+ orphaned raw left by failed siblings). Commit message convention that passed both hooks:
`dreaming: group triage YYYY-MM-DD — Takes=N refs=N skip=N, archive M (Pattern E saturation)`.

## Yield benchmark

257 recent raw / ~30 never-archived candidates → 3 takes + 3 references + 4 batch-skips; archive 7 new URLs
(3,019 total). Typical when the day's pipelines partially failed: backlog probes find real gaps the saturated
daily runs would miss.
