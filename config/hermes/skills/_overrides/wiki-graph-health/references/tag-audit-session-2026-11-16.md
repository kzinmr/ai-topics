# Tag audit session — 2026-11-16 (clean audit, drifted normalization dict)

## Outcome
`scripts/tag_audit.py`: **0 violations** (3,525 pages scanned, 1,029 unique tags, 1,127 SCHEMA tags).
No composite kebab tags, no non-SCHEMA tags. No pages changed, no commit needed.

## Key finding: normalization dry-run said "would modify 612 pages" — correctly NOT applied
Reason (extends the 2026-08-10 lesson): the TAG_NORMALIZATION dict (627 mappings) has drifted
into a **preference-rewrite layer**. Most high-frequency mappings fire on tags that ARE valid
SCHEMA tags (e.g. `ai-safety`→`agent-safety` 85x, `agent-harness`→`harness-engineering` 38x,
`cybersecurity`→`security` 22x, `research`→`lab` 20x). Applying them would rewrite tag semantics
across 612 pages with zero audit violations to justify it.

### Classification procedure (reusable)
Load both scripts via importlib, run `ta.load_valid_tags()`, then for each page compute which
mappings fire. Bucket each fired `(src, target)`:
- `src-in-schema` + `target-SCHEMA` → **preference rewrite** — do NOT apply on a clean audit
- `src-not-schema` → real violation the audit missed (audit said 0, so none existed)
- `target-NOT-SCHEMA` → stale chain — fix BOTH sides (see 2026-08-17 ref)

Also run a **dedup-collision check**: pages where `src` and `MAP[src]` co-exist would be silently
rewritten by the dedup pass even when no mapping "violates" — 290 such collisions found
(e.g. `startup`+`vc`+`company` all collapsing to `company` on andrew-chen.md). Another reason
wholesale normalization is unsafe when the audit is clean.

## Stale chain check
Only 1 mapping had a nominally non-SCHEMA target: `'OAuth': 'oauth'` — lowercase `oauth` IS in
SCHEMA (verified via load_valid_tags), so it was a false alarm from the key/target comparison.

## Decision rule (for future runs)
Audit = 0 → do nothing beyond: (1) classify dry-run fired mappings, (2) check stale chains
(target in SCHEMA), (3) report. Never run `tag_normalization.py` without `--dry-run` when
`tag_audit.py` reports 0 — it WILL modify 600+ pages of preference rewrites.

## Housekeeping notes
- `SKILL.md` hit the ~100K char hard limit again (100,252) — a 2-line reference-list patch was
  REJECTED. This session note lives in references/ instead; SKILL.md needs a net-shrink pass
  before any new reference entries can be added.
- Tag normalization dict last touched: 3c678510. SCHEMA last touched 2026-11-15 (perplexity tag).
