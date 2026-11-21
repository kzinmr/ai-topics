# Digest-vs-Index Reconciliation Recipe (health-fix session 2026-11-09)

## The four-way count divergence problem

The daily health digest (`wiki_health.py` output), index.md section headers, actual index.md lines, and the filesystem all report DIFFERENT per-namespace page counts. Observed 2026-11-09:

| Source | Concepts | Comparisons | Events |
|--------|----------|-------------|--------|
| Digest (filesystem flat-ish) | 2325 | 35 | — |
| index.md header | 2321 ❌ | 39 ❌ | 55 ❌ |
| index.md actual lines | 2320 ✅ | 35 ✅ | 51 ✅ |
| Filesystem `.md` files | 2304 | 35 (+4 redirect entries in index) | 51 |

Why they diverge:
- **Nested subdir pages** (`concepts/ai-benchmarks/*`, `entities/omar-khattab/*`) are served by `_index.md` hub pages, NOT individually indexed → filesystem > index lines.
- **Redirect entries / `_index` hub links** can exist in index without a 1:1 file match.
- **Headers decay** — pipelines add/remove entries without bumping header counts; observed drift of 4 (Comparisons 39→35) and 4 (Events 55→51) in one day's worth of pipeline churn.
- **`> Total pages:` line** lags separately (was 3393 vs actual 3426).

## Authoritative reconciliation procedure

1. Count index lines per namespace — this is the ONLY ground truth for header counts:
   ```python
   import re, collections
   content = open('wiki/index.md').read()
   cnt = collections.Counter(m.group(1) for m in
       re.finditer(r'^\|?- \[\[(entities|concepts|comparisons|events|queries)/', content, re.M))
   ```
2. Patch each `## <Ns> (N pages)` header to the counter value (only if header has a count suffix).
3. Recompute and patch `> Total pages:` = sum of counter values.
4. Run `python3 scripts/validate_index.py` — **NOTE: it does NOT check header-vs-line-count drift**, only structural corruption. Header reconciliation must be an explicit step; a passing validate run is not evidence headers are correct.
5. Ghost check (recursive, before deleting anything): build slug set from index regex, walk filesystem, `s not in fs and not os.path.isdir(s)` → ghosts. Expect 0 after recursive scan (2026-11-09: 0 ghosts confirmed despite 4-way count divergence).

## Git working-tree contention (health-fix cron)

`git pull --rebase` fails with "Please commit or stash them" when a still-running/recently-finished enrichment pipeline leaves uncommitted wiki edits (2026-11-09: 51 files from a The Signal enrichment job). **Do NOT stash or commit other jobs' changes** — verify the diff is a legitimate enrichment append (updated: bump + section additions), leave it for that pipeline to commit, stage ONLY your own files (`git add wiki/index.md wiki/log.md`), and report the backlog in the 要手動対応 section of the report.

## High-sim graph pair triage (repeat false positives)

From `wiki_graph.py --format json` top pairs, these classes are NOT duplicates:
- `X` ↔ `X--core-ideas` / other `--subsection` slugs → page-split artifact (score up to 22).
- Pairs with `direct_link: True` and clearly distinct careers (karpathy/simon-willison, boris-cherny/ryan-lopopolo, alex-imas/phil-trammell) → genuinely different people who co-occur in concepts.
Before any merge: check `status: redirect`, aliases, `--subsection` suffix, and direct links (per watchdog-session-2026-08-13 false-positive checklist).

## SKILL.md size limit note (2026-11-09)

`skill_manage(action='patch')` on this skill fails with "content is 100,651 characters (limit: 100,000)". SKILL.md is over budget — new learnings must go into `references/` files. Consider splitting SKILL.md (e.g., move Sections H/K/M prose into references) at the next maintenance window.
