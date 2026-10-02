---
title: Weekly Wiki Graph Analysis
created: 2026-10-02
updated: 2026-10-02
type: query
tags: []
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-10-02 15:02 UTC

## Verified Findings (manual cross-check)

The raw script output overstates several categories. Independent verification:

- **Broken links (script: 5312, verified: 2851)** — inflated by the script not resolving directory-hub pages (`concepts/context-engineering`, `concepts/security-and-governance`, etc. are directories with `_index.md`, not `path.md`). A resolver that recognizes dir-hubs cuts the count to ~2851. Most common *real* broken targets are **bare wikilinks** (`[[agent-evaluation]]`, `[[rag]]`, `[[cursor]]`) that need namespacing.
- **Index entries not on disk (script: 596)** — **FALSE POSITIVE.** An independent resolver matching index `[[wikilinks]]` against disk finds **0** genuinely missing entries. The script compares bare basenames against nested dir-hub paths (`concepts/x/y`) and miscounts. Do NOT "remove 596 index entries" — that would delete valid navigation.
- **Duplicate groups (script: 16)** — most are intentional `status: redirect` stubs (22 exist wiki-wide). Only **2 are genuine same-person dual-rich pages needing merge**:
  - `entities/deliberate-coder` (130) vs `entities/deliberatecoder` (139)
  - `entities/giles-thomas` (92) vs `entities/gilesthomas` (228)
  - Cross-type pairs (`entities/qwen`+`concepts/qwen`, `entities/cline`+`concepts/cline`) are an entity/product split, not dupes.
- **Orphans** — script 484 / verified-resolver 461 (~315 content-rich ≥50 lines). Consistent ~460–484. Top rich orphans: `concepts/ai-energy`, `concepts/multi-objective-policy-distillation`, `entities/openenv`.
- **Stale (>90d)** — script 1760, but many are **static reference content** (person bios, evergreen concepts, benchmark pages). This is not uniformly actionable; treat as a review queue, not a defect backlog.

## Genuine action items (this week)

1. **[HIGH] Fix 2 pages with non-canonical tags** (pre-commit would block any re-save):
   - `entities/dimillian.md`: `ai-agent`→`ai-agents`; drop `devtools`, `ai-coding-tools`, `ai-timeline`
   - `entities/odyssey-ml.md`: drop `genai`, `ai-timeline`
   - Note: `ai-timeline` appears on **both** — likely a recent seed added a non-taxonomy tag. Add to SCHEMA.md taxonomy *or* remove; do not leave both.
2. **[MEDIUM] Merge 2 real duplicate person pages** (deliberatecoder, giles-thomas) — pick canonical, convert other to `status: redirect`.
3. **[MEDIUM] Namescape ~high-frequency bare wikilinks** (`agent-evaluation`×25, `concepts/rag`, `entities/cursor`, …) and fix cross-namespace links (`[[concepts/claude-code]]`→`entities/`).
4. **[MEDIUM] Reconcile 4 unindexed concept pages** into index.md — but they are part of a **sibling active-crawl batch still uncommitted** (192 wiki files dirty in working tree); defer the index edit to that pipeline to avoid a competing commit.
5. **[LOW] Link the ~10 top content-rich orphans** from related MOCs/hubs.

## NOT real problems (do not act)

- "Remove 596 stale index entries" — false positive (0 actually missing).
- "Consolidate 16 duplicate groups" — 14 are redirect stubs / entity-product splits.
- "1760 stale pages" — mostly static reference content, not defects.

## Summary

- Total pages: 2542
- Orphans: 484 (content-rich: 476)
- Broken links: 5312
- Duplicate groups: 16
- Index gaps: 4
- Tag violations: 2
- Stale pages: 1760

## Recommended Actions

- [MEDIUM]  Fix 163 cross-namespace / bare wikilinks
- [MEDIUM]  Add inbound links to 476 content-rich orphan pages
- [LOW]     8 skeleton orphans exist - enrich or clean up
- [HIGH]    Review and consolidate 16 potential duplicate groups
- [LOW]     Consider splitting 242 oversized pages (>200 lines)
- [HIGH]    Fix 2 pages with non-canonical tags (pre-commit blocks)
- [MEDIUM]  Remove 596 stale index entries (files missing)
- [LOW]     1760 pages stale >90 days - review/revision needed

