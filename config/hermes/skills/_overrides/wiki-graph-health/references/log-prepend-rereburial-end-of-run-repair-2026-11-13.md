# log.md prepend → header re-burial: end-of-run repair (2026-11-13 health-fix session)

## What happened
During the 2026-11-13 `wiki-health-fix` cron run:

1. At session start, `git show HEAD:wiki/log.md` showed `# Wiki Log` at **line 9** — a sibling job (17:35 watchdog, committed minutes earlier) had prepended its entry ABOVE the header, re-burying it even though earlier sessions had repaired this same bug repeatedly.
2. I prepended my own health-fix entry via the canonical `open()`+write method (correct approach).
3. After the prepend, `grep -c '^# Wiki Log'` returned 1 but the header sat at **line 19** — my entry plus the sibling's prepend stack sat above it.
4. Fixed with the ready-made script:
   ```bash
   cd ~/ai-topics && python3 config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py wiki/log.md
   # Output: "Header buried at line 19; restoring to line 1" / "OK — header restored, 215 entries preserved, 0 pipe corruption"
   ```
5. Only THEN committed (`git diff --name-only -- wiki/ | xargs git add --` → commit → push, both pre-commit hooks passed).

## Durable lessons

### 1. Re-burial is a RACE, not a one-time bug
Multiple cron jobs (watchdog, trending-topics, health-fix) prepend to log.md within minutes of each other. Any repair done EARLY in a run gets undone by a later sibling prepend, and any prepend — even a well-behaved one that preserves the header below it — lands ABOVE it. Therefore:

- **Order of operations for any log.md-writing run**:
  1. Do all page/index edits.
  2. Prepend your own entry (open()+write, per skill's canonical recipe).
  3. **Immediately before `git add`/`commit`**, run `fix_log_header_burial.py wiki/log.md` unconditionally — it is idempotent (no-op when header already at line 1) and cheap.
  4. Verify `head -1 wiki/log.md` == `# Wiki Log` AND `grep -c '^# Wiki Log'` == 1, then commit in the same terminal invocation so no sibling can interleave.

### 2. Script location (verified 2026-11-13)
`~/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py` — NOT in `~/ai-topics/scripts/`. Invoke with the path as positional arg (`... .py wiki/log.md`); it auto-detects the buried-header line and reports entries preserved.

### 3. The sibling-modified warning is a hint to re-verify, not to redo
`patch` on index.md returned `_warning: modified by sibling subagent ... but this agent never read it`. In practice the sibling's changes (watchdog's own header reconcile) had already been committed; `git diff --stat` showed only MY 2 lines. Trust `git diff`, not the warning.

### 4. Header-count drift recipe (this run's actual fix)
`## Queries (57 pages)` vs 58 actual entries, `Total pages: 3452` vs sum 3453. Recipe:
- Count actual entries per section: `grep -c '^- \[\[queries/' wiki/index.md` (also `|-` variant if the section uses it).
- Verify all wikilinks for a section live between its header and the next `## ` header (`grep -n` line numbers) before bumping the count — rules out entries misplaced under a neighbor section.
- Recompute `Total pages` as the SUM of section headers, not a filesystem count (redirect-stub dups are legit).

### 5. Full clean-run checklist confirmed working (baseline for future health-fix runs)
All of these verified 0/clean in one pass, ~14 tool calls total:
- index.md: pipe_prefix / line-number / triple-bracket / space-prefix (Python count, not grep BRE)
- `validate_index.py` EXIT=0
- Recursive ghost scan (index wikilinks → file or `_index.md`), skipping `raw/` and handling `|display` syntax
- Recursive orphan scan filtered to top-level (`'/' not in slug[len(sub):]`) — nested pages served by `_index` hubs are by design
- no-frontmatter scan + `sources:` gap scan over entities/concepts/comparisons/queries/events (both were 0 as of 2026-11-13 — Section L's 770-gap state is fully remediated; don't pre-assume it, but don't budget hours for it either)
- L2 pipe-prefix: scope to `wiki/entities wiki/concepts` only (recursive `wiki/` hits log archives → 300K FPs)
- log.md: 1× `# Wiki Log`, 0 orphan `### 2026-` timestamps

Digest's stale/orphan/unprocessed numbers need no action in a clean run — report them, fix only the header drift + log header.

### 6. SKILL.md is at the 100K char cap
Net-growing patches to this SKILL.md fail at ≥100,008 chars. Keep SKILL.md edits net-neutral or net-shrinking; put new detail in `references/` and add only a short pointer line.
