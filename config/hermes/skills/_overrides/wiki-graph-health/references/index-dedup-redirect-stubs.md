# Index Dedup — Redirect-Stub Pre-Check & Count/Orphan Traps (2026-08-19 session)

Session detail backing the compact pre-check in §A4b of SKILL.md. Read this before doing any index.md dedup, header-count refresh, or orphan registration at scale.

## 1. Redirect stubs are legitimately indexed twice (dedup pre-check)

A slug appearing **twice** in `index.md` is NOT always a bulk-duplication bug. This wiki indexes **redirect stubs** as their own lines, so the canonical slug AND its redirect stub BOTH appear in the index.

**Pre-check before removing any "duplicate" line:** does the duplicate slug have its own `.md` file?
```bash
[ -f wiki/<slug>.md ] && echo KEEP-redirect || echo REMOVE-dup
```
- **File exists** → intentional redirect stub entry → **leave it**.
- **No file** → likely a genuine bulk-duplication artifact → remove the later occurrence.

**2026-08-19 data:** an audit flagged 6 apparent duplicate slugs:
`entities/fastino-labs`, `entities/kyle-corbett`, `concepts/gepa`, `concepts/mai-thinking-1-report`,
`concepts/separation-of-duties`, `concepts/gpt/image-2-vs-nano-banana-2`.
**All 6 had their own `.md` files** (redirect stubs) → all legitimate dual listings → **0 removed**.

## 2. Header counts: two distinct sources, use the right one

- **Section header counts** (`## Entities (904 pages)`) must equal the count of **actual `- [[namespace/...]]` entry lines in that section**, NOT the raw filesystem `.md` count.
- Filesystem count diverges from index entries because:
  - (a) redirect stubs are indexed but their canonical+stub **both** count as entries;
  - (b) some files exist on disk but are **NOT** index entries (`_index` hubs, `gpt/_archive/*` files, some redirect stubs).
- So `find wiki/entities -name '*.md' -not -name '_index.md' | wc -l` (e.g. 906) ≠ index entry count.
- **Fix**: recompute each section header by counting its own `- [[` lines in a single pass (single source of truth), not from the filesystem.

## 3. Orphan report mixes real orphans with intentional non-indexed pages

`wiki_health.py --json` `orphan_count` / `orphans` mixes genuine orphans with by-design unindexed pages.
At ~2,964 L2 pages, ~24 "orphans" break down as:
- ~21 `_index` hub files (subdirectory synthesis hubs — intentionally not in main index.md),
- ~2 `concepts/gpt/_archive/*` files (archived content — intentionally not indexed),
- ≤1 **genuine** orphan (a real page like `entities/tim-sherratt`, a redirect stub that is a real page and SHOULD be registered).

**Action**: filter the orphan list — drop every `_index` and every `_archive/*` entry; only the remainder is actionable. Register a genuine real-page orphan in index.md (alphabetical insertion); **do not delete** it.

## 4. Pipeline 503 busy — transient, not a defect (triage/ingest)

Downstream triage/ingest cron jobs can all fail in one window with:
`RuntimeError: HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider.`
This is **transient model-gate saturation**, not a data or pipeline defect.
- **No data loss** — ingest checkpoints (`blog_ingest/latest.json`, `newsletter/latest.json`) stay `ok:true`; the backlog is picked up automatically by the next day's scheduled runs.
- **Do not** treat as an actionable pipeline break; re-alert only if it persists 2+ consecutive days.

## 5. Index.md single-pass fix recipe (insert + dedup + recount)

Proven 2026-08-19: one Python pass that (a) inserts a new orphan entry alphabetically, (b) removes true duplicate slug lines, (c) recomputes each section header count from its own `- [[` lines. Avoids offset drift by rewriting header lines in place during the same pass (use a placeholder token like `(COUNT<section>)` then substitute). Always finish with `python3 scripts/validate_index.py`.
