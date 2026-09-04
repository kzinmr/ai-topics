# Watchdog Session 2026-08-13 — Script Locations, Index Scan False Positives, Dedup Triage

All three learnings from the 2026-08-13 wiki-watchdog-fix run (0 auto-fixes needed; pure verification + gap reporting). Kept in a reference file because the main SKILL.md is at the 100K char limit — fold pointers into SKILL.md only as net-negative edits.

## 1. Canonical locations for the empty-wikilink fixer scripts

Verified 2026-08-13: neither `fix_empty_wikilinks_safe.py` nor `fix_broken_wikilinks.py` exists in:
- `~/ai-topics/scripts/` (the repo scripts dir) — NOT there
- `~/.hermes/skills/wiki/wiki-graph-health/scripts/` (home skill dir) — the directory is EMPTY (no .py files at all)

Canonical location (repo-tracked overrides):
```
/opt/data/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_empty_wikilinks_safe.py
/opt/data/ai-topics/config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_broken_wikilinks.py
```

- Run with `/opt/data/.hermes/venv/bin/python` (system python3 lacks PyYAML, script exits with import error).
- The script's own docstring says its path "differs from the skill's implied scripts/ location" — the SKILL.md Support Files list paths are relative to the `_overrides` dir.
- Quick discovery command if locations drift again: `find /opt/data/ai-topics -name 'fix_empty*' -o -name 'fix_broken*'`
- Note: `scripts/tag_audit.py` and `tag_normalization.py` have the same split — canonical at `~/ai-topics/scripts/` for tag_audit.py, `_overrides/.../scripts/` for tag_normalization.py (see Section J notes).

## 2. Empty-wikilink residual is stable (279 → 0 fixable)

Dry-run output on 2026-08-13: `Total broken: 279`, `Fixed: 0`, `Skipped: 279`. Every line classified as `[no-match]` or `missing:<target>`. This matches the documented 279-residual baseline from 2026-08-05. Conclusion: do NOT spend cycles hunting per-page mappings for these — the anchor `[[slug]]` was lost and the description text does not uniquely resolve. Report the residual count and move on. Re-run the safe fixer dry-run each watchdog cycle to confirm the count stays flat (growth would indicate a new corruption source).

## 3. "Not indexed" filesystem scan: nested pages are false positives

A recursive `os.walk` scan comparing every `.md` relpath under entities/+concepts/ against index.md wikilink slugs reports **570 "missing" pages** — but 570/570 are nested subdirectory pages:

```
concepts/ai-benchmarks/agent-arena        concepts/claude/fable-5
concepts/coding-agents/agentic-coding     concepts/gpt/chatgpt-dreaming
concepts/evaluation/llm-as-judge          entities/omar-khattab/rlm
concepts/harness-engineering/...          concepts/post-training/grpo
... (hundreds more under ~15-20 hub dirs)
```

These are intentionally NOT in main index.md — they are served by `_index.md` hub pages (21 hubs observed). **Filter to top-level only**: `'/' not in relpath` collapses 570 → 0 real gaps. Never "fix" nested pages into index.md; subdirectory organization is by design.

Sanity check: `find wiki/concepts wiki/entities -name '_index.md' | wc -l` → 21 = number of hubs legitimately owning nested content.

## 4. Dedup triage: explicit cross-reference note = resolved disambiguation

High-similarity person pairs are NOT always duplicates. 2026-08-13 verification of the top `person_similarity` pairs:

| Pair | Score | Verdict | Evidence |
|---|---|---|---|
| `aakash-gupta` ↔ `akash-gupta` | 11.5 | **Distinct individuals** | Both pages carry explicit "Related researcher (separate individual with adjacent focus area)" notes and link each other in Related/Cross-Reference sections |
| `martin-fowler` ↔ `martinfowler` | 11.5 | Already merged | `martin-fowler` is a `status: redirect` stub → canonical |
| `koylan-ai` ↔ `muratcan-koylan` | 13.0 | Already merged | `koylan-ai` is redirect/alias; `muratcan-koylan` lists `koylan-ai` in frontmatter aliases |
| `han-lee` ↔ `hanchunglee` | 14.5 | Page-split, not dup | `hanchunglee` is a sub-page pointing to `[[entities/han-lee]]` as "Comprehensive profile" |
| `drew-breunig` ↔ `drew-breunig--core-ideas` | 22.0 | Page-split, not dup | `--subsection` naming = Section G splitting convention |

**Triage checklist before merging any high-score pair** (read BOTH pages):
1. `status: redirect` in frontmatter → already merged, stop
2. One slug listed as alias in the other's frontmatter → already merged, stop
3. `--subsection` or `--projects` suffix → page-split (Section G), not a duplicate
4. Each page links the other with a "distinct/separate individual" note → deliberate disambiguation, stop
5. Only merge when no such markers exist AND content overlaps (see Section B merge procedure)

## 5. Pipeline alert classification note

`x_accounts: stale(26h)` fired but is a FALSE POSITIVE for the every-2-days cadence (`30 22 */2 * *`). Verify via `~/.hermes/cron/jobs.json` (enabled, state=scheduled, next_run_at within 1 cycle) — same pattern as the documented 2026-07-19 case. See `references/stale-job-alert-analysis.md` — this is already covered; recorded here only as confirmation the pattern recurs.
