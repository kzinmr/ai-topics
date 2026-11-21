# Index Count Reconciliation & Stale-Report Verification (watchdog session 2026-11-09)

Commit `01ad7ca1`. Durable lessons for watchdog / health-fix runs.

## 1. Header section counts: INDEX LINES are authoritative, not filesystem files

The `## Concepts (N pages)` / `Total pages: N` headers in `index.md` count **indexed entries**, not files on disk. Recomputing from the filesystem — which the SKILL.md "Auto-correct during lint" line suggests — is systematically wrong in BOTH directions:

- **Top-level-only `find` under-counts**: nested subdir pages are each indexed as their own line. Observed 2026-11-09: `find wiki/concepts -maxdepth 1` = 1,718 files, but index contained 2,320 `- [[concepts/...]]` lines (606 nested pages under `concepts/ai-benchmarks/`, `concepts/claude/`, etc. are individually indexed, on top of the 21 `_index.md` hubs). Queries likewise had date-prefixed snapshot pages (`queries/2026-11-0X-skeleton-enrich-empty`) in the index that a naive scan misses.
- **Redirect-stub double-indexing inflates line counts legitimately**: a canonical slug may appear twice (canonical + stub entry). Always `[ -f wiki/<slug>.md ]` before calling a dup a bug (A4b / 2026-08-19). Observed: Entities header 966 = 958 top-level + 7 `entities/omar-khattab/*` subdir + 1 redirect-stub dup line. All 19 apparent duplicate entries had real files → 0 removed.

**Correct recipe** — count index lines per namespace (match BOTH `- ` and `|- ` prefixes); set headers to those numbers:

```python
import re
c = open('wiki/index.md').read()
for ns in ['entities','concepts','comparisons','events','queries']:
    n = len(re.findall(r'^\|?- \[\[' + ns + r'/', c, re.M))
    print(ns, n)   # numbers the headers should carry
```

Use the recursive filesystem scan ONLY as a **set-difference to find unindexed orphans**, never to set header numbers:

```python
import os, re
c = open('wiki/index.md').read()
indexed = set(re.findall(r'\[\[(?:entities|concepts|comparisons|events|queries)/([^\]|]+)', c))
for sub in ['concepts','queries','entities','comparisons','events']:
    for r,_,fs in os.walk(f'wiki/{sub}'):
        for f in fs:
            if not f.endswith('.md') or f.startswith('_index'): continue
            rel = os.path.relpath(os.path.join(r,f), f'wiki/{sub}')[:-3]
            if rel not in indexed and '/' not in rel:  # '/'-containing = hub-served, check individually
                print('UNINDEXED:', sub, rel)
```

(2026-11-09 result: exactly 1 real gap — `queries/2026-11-05-skeleton-enrich-empty`, a 29-line snapshot page — registered alphabetically between the 11-04 and 11-06 entries.)

After edits: `python3 scripts/validate_index.py` must exit 0; Total pages = sum of the five namespace counts.

## 2. Stale graph-report claims self-heal AND self-persist

- **Self-heal**: by watchdog time (17:35, after wiki-health-fix + sibling pipelines), the weekly graph report's actionable items are usually already applied. 2026-11-09: both "missing cross-ref" items (`concepts/qwen` → `[[entities/qwen]]`, `concepts/agent-harnesses` → `[[comparisons/agent-harnesses]]`) were already present in the target pages. Grep the actual page before "fixing" — the failure mode is adding a duplicate link line.
- **Self-persist**: mechanical typo-fix batches (the `[[concepts/ai-benchmarks/swe-bench\]]` backslash strip, 10 occurrences) MISS the graph report's own quoted example — the report file under `wiki/queries/` is often the LAST surviving carrier of the very typo it documents. When re-checking such batches, grep `wiki/queries/` too. Fix real link occurrences; LEAVE the annotations file's literal example text (`Mechanical: 10× ...`) intact — it documents the pattern, it doesn't link.

## 3. Watchdog-scoped staging (worked well)

The repo carried ~30 dirty files from sibling pipelines. Correct behavior: `git add` ONLY the files this run touched (`wiki/log.md wiki/index.md wiki/queries/<report>.md`), never `git add wiki/` wholesale — sibling edits belong to their owning pipelines. Pre-commit (validate_index + tag validator) passed with exactly the 3 staged files.

## 4. Log.md prepend pattern used (cron-safe)

`execute_code` blocked in cron mode → ran a `python3 - <<'PYEOF'` heredoc via terminal that asserts `content.startswith('# Wiki Log')` after the burial fix, rebuilds header+metadata+entry+remainder via `content.split('\n', 3)[3]`, and asserts exactly one header+metadata pair. The fix itself: `python3 config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py` (no args, backs up to .bak — delete the .bak before staging). Header was buried at line 11 by the same-day trending-topics prepend — recurring bug class; run the script first, it's idempotent (exits clean when header already at line 1).
