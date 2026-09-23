# Weekly graph analysis — 2026-09-18 addendum

Learnings from the 2026-09-18 wiki-graph-analysis cron run. These supplement `references/weekly-graph-analysis.md` — read that file first.

## The wrong-script failure recurred despite prior guidance

The 2026-08 reference said `_weekly_graph_report.py` is canonical and `wiki_graph_analysis_weekly.py` is shallow/diagnostic. The 2026-09-18 run still invoked the shallow script. Consequences it produced (all real):

- Page count 2,486 vs actual 3,079 (missed 587 nested concepts + 7 nested entities).
- "5,252 broken links" vs 2,810 real (shallow scan mis-resolves nested-dir targets).
- "573 stale index entries" vs actual 0 ghosts (path-exact comparison vs mixed index forms).

**Mandatory verification step (add to the quick-start):** after any scan run, compare the report's total page count against
`find entities concepts comparisons queries events -name '*.md' ! -path '*_archive*' | wc -l`.
If they differ, redo the scan recursively (or run `scripts/wiki_graph_analysis_verified.py`) and report only verified numbers. Never publish shallow-script counts.

## Output-render bug: double-wrapped link targets

`wiki_graph_analysis_weekly.py` prints broken targets as `[[[[concepts/foo]]]]` (double-wrapped). Grepping the wiki for `[[[[` to "verify" returns 0 matches even when the refs genuinely exist in files. Do not use that grep as a verification; recompute with the recursive script.

## New in-repo tool: `scripts/wiki_graph_analysis_verified.py`

Committed 2026-09-18 (repo `~/ai-topics/scripts/`). Recursive walk; outputs: total pages, orphans (excludes `_index` hubs), content-rich orphan list sorted by size, and broken targets ranked by ref count with one sample source each. Use it for the adjudication pass. Implementation gotchas baked into it (re-implement elsewhere and you'll repeat these):
1. Strip fenced code blocks before wikilink extraction (example links in ``` fences inflate counts).
2. Resolve a target as alive if it matches a full key OR the basename of any page (basename map).
3. Skip `_archive` dirs; exclude `_index`/`index` pages from orphan counting (by-design unreferenced).

## Broken-link classification taxonomy (report this, not a flat count)

Classified 2,810 broken refs on 2026-09-18:
| Category | Refs | Fix |
|---|---|---|
| namespaced-missing (wrong-namespace guess or truly absent) | 1,280 | batch basename-resolution where unique |
| raw-ref-as-wikilink (`[[raw/...]]`, `[[transcripts/...]]`) | 919 | NOT page-creatable — policy: inline-link conversion or lint exemption |
| bare-missing (`[[windsurf]]` to nonexistent page) | 432 | create or unlink |
| deep-path-drift (renames, trailing `\` artifacts) | 121 | manual; `[[concepts/evaluation/petri-alignment\]]` shows trailing-backslash class |
| dir-hub-missing-index (target is a directory without `_index.md`) | 58 | create hub `_index.md` — `concepts/context-engineering` alone absorbed ~130 refs; single highest-ROI fix |

`[[[]]]` empty-target refs (31) also exist — usually `[[|alias]]` or truncated links.

## Duplicate-group adjudication, 2026-09-18 snapshot

16 flagged → 8 real: eugeneyan→eugene-yan, lilianweng→lilian-weng (fact conflict, contested), gilesthomas/giles-thomas, deliberate-coder/deliberatecoder, deerflow→deer-flow, alphaproof-nexus→alpha-proof-nexus, dspyrlm(stub)→dspy-rlm, open-claw-ecosystem(stub)→openclaw-ecosystem.

⚠️ **Contradicts the 2026-08-28 note** that called deliberate-coder/deliberatecoder different people (Ben Ilegbodu vs Steve Shogren). As of 2026-09-18 on disk: `entities/deliberate-coder` title = "Deliberate Coder" (130L), `entities/deliberatecoder` title = "Steve Shogren (Deliberate Software)" (139L); no `steve-shogren` page exists. The pair was NOT opened and read this run — the earlier session's "different people" warning stays in force until someone reads both Overviews. This is exactly why the "always read both pages before merging person pairs" rule exists; do not merge based on this addendum's listing alone.

Still-no-action confirmed 2026-09-18: samuelcolvin and martin-fowler are proper `redirect:` pages; cline/qwen entity+concept and agent-harnesses/evals-skills/llm-integration-patterns concept+comparison pairs are by-design.

## Index reconciliation by basename

Path-exact disk-vs-index comparison manufactured 573 fake ghosts. Correct method: map index wikilinks and disk paths to basenames, compare those, then inspect the small remainder. 2026-09-18 true result: 0 ghosts, 22 unindexed = all `_index` hubs (by-design) + the just-written report page.

## execute_code blocked again

execute_code was BLOCKED in this cron run (matches the 2026-08-28 note). Write analysis scripts to `/tmp/*.py` via terminal heredoc and run with `python3`. The skill's own SKILL.md already carries this pitfall — plan for it from the start of cron runs.
