# Tag Audit Session — 2026-08-17

## Outcome
5 non-SCHEMA tags → 0. Commit `3c678510` (7 files, +31/−11), pre-commit tag validator passed WITHOUT `--no-verify`.

## Violations and fixes
- **Mapped (2x multi-use)**: `wealth-concentration`→`economics`, `data-exfiltration`→`security`
- **Mapped via EXISTING dict entries (applied manually)**: `wiki-maintenance`→`wiki`, `graph-analysis`→`wiki` (both on `queries/wiki-graph-analysis-weekly-2026-08-14.md` — page created after the 2026-07-27 run, so the mappings existed but had never been applied to it)
- **Deleted (1x one-off)**: `incident` (event page already carried agent-safety/security/vulnerability)

## NEW pitfall — stale TAG_NORMALIZATION chain (mapping VALUE not in SCHEMA)
`'wealth-distribution': 'wealth-concentration'` was added 2026-08-10 with claimed
"every canonical target verified present in SCHEMA.md" — but `wealth-concentration`
was **never in SCHEMA**. The mapping silently converted one non-SCHEMA tag into
another non-SCHEMA tag. The audit caught it only because `wealth-concentration` was
in use on 2 pages; a stale chain whose target is unused rots silently.

- **Detection**: when a flagged tag appears as a dict VALUE (`': 'wealth-concentration'`),
  it's a chain target, not just a key. `grep -n "wealth-concentration" tag_normalization.py`
  shows BOTH the key `'wealth-concentration':` and the value `': 'wealth-concentration'` lines.
- **Fix**: map BOTH the source and the old target to the real canonical:
  `wealth-distribution`→`economics`, `wealth-concentration`→`economics`.
- **Prevention**: when adding mappings, verify the canonical target exists in SCHEMA.md
  (Phase 2.5), AND check that existing mapping values aren't themselves non-SCHEMA tags.
  `tag_normalization_diff_scan.py` classifies pages, not dict entries — the stale chain
  check must be a manual `grep` of the dict values.

## Process notes
- Cron pre-run script path failure again (`tag_audit.py` blocked outside scripts dir) →
  ran directly from `config/hermes/skills/_overrides/wiki-graph-health/scripts/` per
  documented workaround (Layer 3 / Section J).
- Diff-scan before deciding: **0 violation pages** after manual patches (156 preference-rewrite
  pages correctly left untouched) — confirms manual-patch playbook over wholesale normalization.
- **Bumped `updated:` on all 5 manually-patched pages** (SCHEMA convention "always bump updated" —
  easy to forget on tag-only edits; the 2026-08-10 session didn't mention it, this one did).
- **Sibling-subagent warnings on patched files** (concurrent pipelines active, e.g. raw-backlog-ingest):
  verified via the patch tool diffs that only tag lines changed — surgical patches are safe;
  the warnings are informational, not blockers.
- Committed with explicit pathspec (7 files) to avoid sweeping concurrent pipeline changes
  (untracked raw articles + sibling-modified concept files present in the same worktree).
- No SCHEMA.md additions needed — all targets were existing canonicals.
