# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-09] rotate | Rotated log-2026.md (1158 lines → log-2026.md appended)
- Previous entries archived to log-2026.md
- Fresh log.md initialized

## [2026-05-09] watch | Watchdog fix — log.md duplicate header removed
- Removed duplicate header section (13 lines) from log.md rotation artifact
- Fixed extra blank line

## [2026-05-09] lint | Wiki health check — 3 CRITICAL, 12 WARNING issues found

### Fixes Applied
- **Index dedup**: Removed 2 duplicate entries (mitchell-hashimoto-ghostty, mitchell-hashimoto-hashicorp)
- **Index corruption**: Fixed pipe-table corruption (4 lines normalized)
- **Log rotation**: Rotated log.md (1158 lines → archived to log-2026.md, fresh log initialized)
- **Header counts**: Updated index.md header (Total: 1828, Entities: 531, Concepts: 1272, Comparisons: 13, Events: 2)

### Critical Issues
- 415 pages with broken outbound wikilinks
- 271 broken outbound wikilinks total (mostly concept/entity pages missing)
- 313 orphan pages (no inbound links)
- 128 stale pages (not updated in 90+ days)
- 734 pages (40%) with no sources field
- 349 tags not in SCHEMA.md taxonomy
- 16 composite kebab-case tags detected

### Warnings
- 1,828 total pages, only 762 indexed (58% index coverage gap)
- Concepts section: 1,272 files vs 209 index entries (84% unindexed)
- Subdirectory pages (fine-tuning/, harness-engineering/, etc.) not indexed

### Unactionable Broken Links
- 1 broken link in concepts/agentic-coding.md → `spec-driven-development` (no type prefix)
- Multiple back-links between paired pages (e.g., claris-filemaker ↔ agentic-coding)

### Tag Audit Summary
- Most common missing tags: coding-agents, software-development, workflow, testing
- Composite tags detected: agentic-engineering-patterns, context-window-management, fine-grained-authorization
- 349 unique tags not in SCHEMA.md taxonomy need reconciliation

## [2026-05-09] ingest | X accounts scan — 11 accounts, 4 new posts, 3 pages created
- **Scanned**: 11/79 accounts (68 skipped — budget)
- **New posts**: 4 (from @gm8xx8, @rlancemartin, @milksandmatcha)
- **Pages created**: 3
  - Created: entities/zyphra.md — Zyphra company entity (MoE models on AMD, $110M Series A)
  - Created: concepts/zaya1-vl-8b.md — ZAYA1-VL-8B: vision-language MoE (700M/8B), vision-specific LoRA, bidirectional image attention
  - Created: concepts/zaya1-74b-preview.md — ZAYA1-74B-preview: reasoning-base MoE (4B/74B), Mamba/CCA hybrid
- **Raw articles saved**: 2
  - raw/articles/2026-05-08-zyphra-zaya1-vl-8b.md
  - raw/articles/2026-05-08-zyphra-zaya1-74b-preview.md
- **Index updated**: Entities 541→542, Concepts 1272→1274, Total 1828→1831
