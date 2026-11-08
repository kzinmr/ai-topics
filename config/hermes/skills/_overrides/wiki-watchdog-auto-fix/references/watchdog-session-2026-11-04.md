# Watchdog Session — 2026-11-04 (17:35 UTC)

One auto-fix + a systemic pipeline-failure diagnosis worth keeping as a reusable classification.

## What happened

- Index corruption checks all 0 upstream (pipe/line-number/triple) → report-only, no action (healthy pipeline, as expected — watchdog value shifted to verification/gap reporting).
- Top-level unindexed scan found exactly ONE gap: `entities/metR` (METR, real ~25-line content page). Registered in index.md entities section between `merge` and `merge-dev`. validate_index.py clean (3,417 lines), tag validator passed, committed+pushed (`78e19703`).

## Reusable: classifying multi-job pipeline failures into root causes

Five jobs failed across blog/newsletter/dreaming/x-bookmarks chains. Read the **last 8-15 lines** of each job's latest `~/.hermes/cron/output/<job_id>/<run>.md` — the `## Error` block at the very bottom carries the root cause. Classification found TWO systemic causes, not five independent failures:

1. **`RuntimeError: HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider.`** → blog-triage (10:28), dreaming-wiki-ingest (11-03 18:20). The message itself says fallback *should* engage but didn't — this is a provider-fallback config issue, flag to human, don't retry blindly.
2. **`RuntimeError: Response truncated due to output length limit`** → blog-wiki-ingest, newsletter-wiki-ingest, x-bookmarks-ingest. Same error across 3 different jobs = an output/max-tokens cap too low for these agent prompts, not a one-off.

Cascade pattern confirmed: **newsletter-triage SUCCEEDED** (status `ok`, output ends with a proper `COST_REPORT:` line and human-readable Japanese report) yet its downstream wiki-ingest reported `failed to parse JSON response from newsletter-triage output`. Why: triage emitted a prose report, not the JSON the downstream expects. But note that `triage_latest.json` on disk WAS valid JSON (checked with `json.load` on `~/.hermes/cron/data/newsletter/triage_latest.json`) — the parse failure was reading the *markdown output file*, not the checkpoint. So the checkpoint-based handoff is fine; the failing step is the wrapper that re-parses the agent's chat output. Distinguish these before reporting.

## Verifying triage success despite downstream 'parse failed'

jobs.json `last_status` is the fastest truth source:
```python
python3 -c "
import json
jobs=json.load(open('/opt/data/.hermes/cron/jobs.json'))
jl=jobs if isinstance(jobs,list) else jobs.get('jobs',jobs)
for j in (jl if isinstance(jl,list) else jl.values()):
    n=j.get('name','')
    if any(k in n.lower() for k in ['blog','newsletter','x_bookmark','wiki']):
        print(n,'|',j.get('enabled',True),'|',j.get('last_status'),'|',str(j.get('last_run_at'))[:19])
"
```
(No `hermes` binary on PATH here — read jobs.json directly. 11-03 reference also documents `hermes cron list` returning empty-with-exit-0; this session `hermes: command not found` — same conclusion, use jobs.json.)

## Uncommitted raw articles left by failed wiki-ingest — do NOT just `git add`

`git status --short -- wiki/` showed today's `raw/newsletters/2026-11-03-*` (6 files) + 1 `raw/articles/` file staged as `??`. These were triaged (2 takes queued in `triage_latest.json`) but the wiki-ingest run that was supposed to commit them died on truncation. **Do not commit them yourself** — the take work (page creation) never happened; committing raws without the ingest makes the watchdog look like it processed them. Correct action: report them as deferred work, recommend force-running the failed ingest job after the LLM backend recovers (`hermes cron run <job-id>` or via `hermes cron`).

## metR capital-slug pitfall (minor)

My top-level-unindexed scanner used regex `\[\[(?:entities|concepts)/([a-z0-9@\.\-]+)` — lowercase-only character class. `entities/metR` (capital R in slug) was genuinely unindexed so the fix was correct, but the regex itself cannot match capital-letter slugs → it would FALSELY report any correctly-indexed capital-slug page as missing. When scanning for unindexed pages, add `re.IGNORECASE` or uppercase `A-Z` to the class, then verify each "missing" hit against a case-insensitive `grep -i` on index.md before registering (metR itself returned 35 grep hits — all in other pages' descriptions, none was an actual index entry, confirming it was a real gap).

## log.md prepend → H1 burial RECURRED (self-inflicted, fixed same-session)

Prepending via `open(); write(entry+content)` again left `# Wiki Log` stranded at line 13 (the entry went ABOVE the existing H1 because the file's H1 was already the first line and the prepend put content before it). Recovery that worked: read all lines, find every `# Wiki Log` line, pop the non-first occurrence, then `content = "# Wiki Log\n\n" + content.lstrip('\n')`, verify `content.count("# Wiki Log") == 1`. The canonical prepend in the parent skill assumes the file starts with content under an existing H1 — but the safest recipe is: strip the leading H1, prepend entry, then re-emit exactly one H1 at the very top. Always `git diff wiki/log.md` before commit to confirm the H1 is at line 1 and no body content vanished. (Sibling-subagent write warning appeared on the index patch — the `# Wiki Log` count of 4 after the strip was misleading because the string also occurs in body prose; trust `head -4` + git diff, not the substring count. The 11-03 reference already flagged the prose-mention substring-count trap — reconfirmed.)
