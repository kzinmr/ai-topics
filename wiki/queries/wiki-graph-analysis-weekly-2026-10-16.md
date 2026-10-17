---
title: Weekly Wiki Graph Analysis
created: 2026-10-16
updated: 2026-10-16
type: query
tags: [knowledge-management]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-10-16 15:00 UTC
**Method**: Recursive scan of all Layer-2 pages (`entities/ concepts/ comparisons/ queries/ events/`), Obsidian-style wikilink resolution (basename across all subfolders). Code fences stripped before link extraction.

> ⚠️ The built-in `scripts/wiki_graph_analysis_weekly.py` reports lower orphan counts and ~6,000 "broken links" because it (a) scans only the *top level* of each folder (`os.listdir`) and (b) mis-parses nested `[[[[...]]]]` brackets into phantom links. The numbers below are recomputed with a recursive, bracket-safe resolver and are the accurate graph picture.

## Summary

| Metric | Count | Notes |
|---|---|---|
| Total L2 pages (recursive) | **3,258** | script top-level-only saw 2,656 (misses 596 nested concepts) |
| Pages with ≥1 inbound link | 197 | graph is star-shaped around hubs |
| **Orphans (no inbound)** | **3,039 (93%)** | 2,580 content-rich · 29 skeleton · 430 minimal |
| Broken wikilink targets (true) | 1,840 slugs / 3,507 instances | 649 more links are *reachable but need path normalization* |
| Real duplicate groups | 15 (14 actionable) | confirmed, not false positives |
| Stale pages (>90d) | 2,364 | see caveat below |
| Oversized pages (>200 lines) | 318 | |
| Tag violations | 1 (`quant`) | pre-commit would block |
| Index not-indexed pages | 3 | WIP snapshots + one report |
| Index entries pointing nowhere | 1 | `_meta/rss-scans/2026-10-13` (script's "601" is an artifact) |
| Missing frontmatter | 3 | all `queries/*uncommitted-wip-snapshot` / annotations |

## 1. Orphan pages — the dominant problem (93%)

Only 197 of 3,258 pages receive any inbound link. The remaining ~3,039 are content with no way in — invisible to navigation and to Obsidian's graph view. This is the single biggest structural issue and is far worse than the weekly script's "493" headline suggests, because the script never sees the 596 nested concept pages and never resolves namespace-relative links.

Top content-rich orphans (worth linking first):
- `concepts/ai-energy` (329L, 34 outbound links — rich but nobody links *to* it)
- `concepts/exhaustive-agentic-search` (295L)
- `concepts/multi-objective-policy-distillation` (279L)
- `entities/openenv` (234L) · `entities/ibrahim-diallo` (227L)
- `concepts/symphony` (208L) · `concepts/autonomous-agent-marketplace-stack` (199L)
- `concepts/mistral-ocr-4` (188L) · `concepts/hegel-property-based-testing` (187L)

**Recommendation**: This is not a "link every page" job. The fix is *hub density* — MOC / index pages that fan out to each thematic cluster (the openclaw/, harness-engineering/, evaluation/, post-training/ sub-clusters already have `_index.md` hubs; the ~2,000 loose top-level concepts mostly do not). Prioritize the content-rich orphans above, and audit the `_index.md` hub coverage per theme.

## 2. Missing cross-references / broken links

True broken targets (no page resolves) — these are the highest-leverage to fix because they are *heavily-referenced* hubs whose links are mis-pathed:

| Broken slug | refs | Likely reality |
|---|---|---|
| `context-engineering` | 201 | file lives at `concepts/harness-engineering/context-engineering.md` — bare/prefixed link never resolves in Obsidian |
| `claude-code` | 47 | entity `claude-code` exists; concept-prefixed links (`[[concepts/claude-code]]`) are wrong namespace |
| `agent-evaluation` | 45 | check for nested `evaluation/` path |
| `coding-agents` | 28 | nested `concepts/coding-agents/…` |
| `gemini` / `cursor` / `sglang` / `rag` | 17–24 | namespace / nesting mismatches |

Plus **649 links are reachable only after normalization** (wrong subfolder prefix or bare-vs-namespaced). Obsidian can't follow `[[concepts/context-engineering]]` when the file is `concepts/harness-engineering/context-engineering.md`. A one-time path-normalization pass over these would reconnect a large slice of the graph cheaply.

**Recommendation**: Run a normalization pass (repoint to real basenames) — highest ROI. 87 cross-namespace links (e.g. `[[concepts/claude-code]]` → `entities/claude-code`) are mechanical fixes.

## 3. Duplicate entity pages — 15 groups (all confirmed real)

Person pages duplicated under both `name-surname` and `namesurname` slugs — one is a rich page, the other a 14–22 line stub (redirect candidates):

- `eugene-yan` (353L) vs `eugeneyan` (16L stub)
- `lilian-weng` (203L) vs `lilianweng` (16L stub)
- `samuel-colvin` (227L) vs `samuelcolvin` (14L stub)
- `martin-fowler` (17L stub) vs `martinfowler` (142L)
- `giles-thomas` (92L) vs `gilesthomas` (228L)
- `deliberate-coder` (130L) vs `deliberatecoder` (139L) — both substantial, needs merge

Same-name-different-type / slug variants:
- `entities/cline` (128L) vs `concepts/cline` (98L)
- `entities/qwen` (145L) vs `concepts/qwen` (88L)
- `concepts/agent-harnesses` (157L) vs `comparisons/agent-harnesses` (412L)
- `concepts/dspy-rlm` (697L) vs `concepts/dspyrlm` (25L stub)
- `concepts/deer-flow` (92L) vs `concepts/deerflow` (51L)
- `concepts/alpha-proof-nexus` (142L) vs `concepts/alphaproof-nexus` (52L)
- `concepts/open-claw-ecosystem` (25L stub) vs `concepts/openclaw-ecosystem` (138L)
- `concepts/evals-skills` (25L stub) vs `comparisons/evals-skills` (69L)
- `concepts/llm-integration-patterns` (25L stub) vs `comparisons/llm-integration-patterns` (275L)

**Recommendation**: For the 5 clear person-page pairs, keep the rich page and convert the stub into a redirect (per the `redirect` tag in SCHEMA.md). For the cross-type pairs (cline/qwen), decide the canonical home and redirect the other. `deliberate-coder`/`deliberatecoder` needs a manual content merge.

## 4. Stale concepts — 2,364 (>90 days)

Largest cluster is a 2026-04-10 bulk-ingest wave of HN-popular *blogger* entity pages (abacaj, adam-mastroianni, chipro, derek-thompson, jxmo, …) plus April concept seeds. **Caveat**: staleness here means "frontmatter `updated` not bumped", not necessarily "wrong". Person/blog entity pages are inherently low-churn — their content isn't false, just untouched. Do **not** mass-edit; treat as a review backlog, not a defect. The genuinely worth-rechecking ones are fast-moving concepts (model/capability claims) older than ~90d, not person pages.

## 5. Other health items

- **Oversized (>200 lines): 318.** Worst offenders: `queries/2026-10-04-uncommitted-wip-snapshot` (3,668L — a WIP snapshot that should arguably be archived), `concepts/agentic-search` (1,191L), `entities/simon-willison` (993L), `entities/harvey` (960L), `entities/ed-zitron` (918L). Split the concept pages; leave rich person pages (they legitimately accumulate).
- **Tag violation:** 1 page uses `quant` (invalid → use `quantization`).
- **Missing frontmatter:** `queries/2026-10-04-uncommitted-wip-snapshot`, `queries/2026-10-11-uncommitted-wip-snapshot`, `queries/wiki-graph-analysis-weekly-2026-08-28-annotations`.
- **855 pages have empty `sources:`** — mostly generated blog-entity / timeline pages. Low severity but worth defaulting to `[]` explicitly for lintability.
- **Index:** only 3 pages unindexed (all WIP/report artifacts); only 1 true dangling index entry (`_meta/rss-scans/2026-10-13`). The script's "601" is a basename-resolution bug, not real drift.

## Prioritized recommendations

1. **[HIGH] Path-normalization pass on broken links** — repoint the top mis-pathed hubs (`context-engineering` ×201, `claude-code` ×47, `agent-evaluation`, `coding-agents`) and the 87 cross-namespace links. Cheap, reconnects the most-referenced pages.
2. **[HIGH] Consolidate 14 duplicate groups** — redirect the 5 person-stub pairs; merge `deliberate-coder`/`deliberatecoder`; pick canonical homes for `cline`/`qwen`.
3. **[MED] Hub/MOC coverage for orphan clusters** — the ~2,000 loose top-level concepts need thematic hub fan-out (extend existing `_index.md` pattern); link the 10 richest orphans first.
4. **[MED] Fix `quant`→`quantization`** tag + add frontmatter to the 3 WIP query pages (or archive the WIP snapshots).
5. **[LOW] Archive stale report/WIP snapshots** (`queries/2026-10-04-uncommitted-wip-snapshot` etc.) and fix the `_meta/rss-scans/2026-10-13` dangling index line.
6. **[LOW] Treat "stale" as a review backlog**, not a defect — don't mass-edit low-churn person/blog pages.
7. **[TOOLING] Fix `scripts/wiki_graph_analysis_weekly.py`** — switch `os.listdir`→`os.walk` (recursive), dedup the `[[[[…]]]]` nested-bracket regex, and make index reconciliation basename-aware. Current output (493 orphans / 6,269 broken / 601 index gaps) is materially misleading.
