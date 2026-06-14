---
name: wiki-maintenance
description: >-
  Comprehensive wiki maintenance: daily structural health checks (index reconciliation,
  log separator fixes, pipeline watchdog alerts), comparison page updates (adding items
  to multi-section comparison tables), and page relocation (moving/renaming pages while
  maintaining link integrity).
category: wiki
tags: [wiki, maintenance, index, comparison, relocation, watchdog]
triggers:
  - "wiki maintenance"
  - "wiki structural health"
  - "wiki watchdog"
  - "wiki auto-fix"
  - "update comparison page"
  - "add to comparison table"
  - "move wiki page"
  - "rename wiki page"
  - "relocate wiki page"
  - "wiki directory restructuring"
---

# Wiki Maintenance

Comprehensive wiki maintenance covering three domains: daily structural health, content updates, and structural reorganization.

## Quick Reference

| Task | Trigger | Section |
|------|---------|---------|
| Daily structural health | Watchdog cron / broken links | §1 Daily Structural Health |
| Add item to comparison | "Add X to pricing page" | §2 Comparison Page Updates |
| Move/rename pages | "Move wiki page" | §3 Page Relocation |

## Common Constraints

### execute_code Blocked in Cron
`execute_code` is blocked in cron mode. Use `patch()` and `terminal()` (shell commands) instead.

### Git Commit Conventions
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: <summary>" && git push
```
**Shell variable trap**: If the commit message contains `$` (e.g., `$10/$50`), use single quotes or escape: `\$10/\$50`.

### Index.md Maintenance
- Section headers use **filesystem count** (including `_index.md`)
- Summary line `Indexed entries:` uses **index entry count** (all `- [[...]]` lines)
- Always verify both after any index modification
- Concepts section drifts the most — always check first

### NEVER use `write_file` for log.md
`write_file` overwrites the entire file. log.md is append-only — always use `terminal("cat >> wiki/log.md")` or `patch()`.

---

## 1. Daily Structural Health (Watchdog)

### When to Use
- Daily watchdog cron job (`wiki_watchdog_fix_context.py`) at 17:35 UTC
- User reports of broken links or index inconsistencies
- Any task involving wiki structure health checks

### Auto-Fixable Issues

**Index.md Corruption:**
- Pipe table corruption: `|- [[` → `- [[`
- Line number prefix corruption: `\d+|` patterns
- Duplicate entries: exact duplicate `- [[...]]` lines
- Header count mismatch: section headers vs filesystem

**Log.md Missing Separators:**
Consecutive `## [YYYY-MM-DD]` headers without `---`. Pre-flight: verify ALL `## ` lines are date-stamped before bulk fixing.

**Orphan Page Handling:**
1. Ghost entry detection (index.md → file existence)
2. Orphan addition (file existence → index.md)
3. Alphabetical insertion within correct section
4. Max 20 orphans per run; filter stubs (<30 lines, TODO marker)

### Pitfalls
- `rstrip(".md")` is a character set, not substring — use `re.sub(r'\.md$', '', target)`
- Schedule inversion: watchdog runs BEFORE health-fix (17:35 vs 17:50 UTC)
- `wiki_snapshot` counts may be stale — verify against filesystem
- Summary line `Indexed entries:` must count ALL `- [[...]]` lines, not just one section
- **Tag taxonomy**: Pre-commit validates tags against SCHEMA.md. Common misses: `exploration`, `interview`, `llm-training`, `rl` (use `reinforcement-learning`). Verify with `grep -o "tagname" wiki/SCHEMA.md`.
- **Language enforcement**: Non-raw pages must be in English. Japanese content blocks commit — translate before committing.
- **Symlink + git add**: Changes made through `~/wiki` symlink may not stage with `git add wiki/`. Use `git add -A wiki/` and verify with `git show --stat HEAD`.

→ **Full detail**: `references/daily-structural-health.md`
→ **Scripts**: `scripts/build-orphan-sed.py`, `scripts/misplaced-entries-detection.py`
→ **Reference**: `references/misplaced-stub-cleanup.md`

---

## 2. Comparison Page Updates

### When to Use
- Adding a new item (model, provider, tool) to an existing multi-section comparison page
- "Add X to the pricing/comparison page"
- "Update comparison table with new model"

### Workflow
1. Read the FULL comparison page first
2. Identify ALL sections to update (typically 8+)
3. Gather all pricing/spec data before editing
4. Edit with `patch` tool
5. Verify no duplicate frontmatter fields
6. Update index.md and log.md
7. Commit and push

### Sections Typically Updated (8 total)
1. Main table — new row with tier classification
2. Cache pricing section
3. Batch pricing section
4. Tier analysis section
5. Cost comparison section (chat + code gen workloads)
6. Key Trends — if significant market shift
7. Changelog — always add entry
8. Related Pages — wikilink to entity/concept page

### Key Pitfalls
- **Duplicate frontmatter**: Always read lines 1-10 before patching
- **Non-unique patch context**: Include surrounding lines for uniqueness
- **Section numbering cascade**: Renumber ALL subsequent sections when inserting
- **execute_code blocked in cron**: Use `terminal` + `sed` for bulk edits

→ **Price verification**: `references/llm-api-pricing-verification.md`
→ **Case study**: `references/llm-api-pricing-fable5-update.md`

→ **Full detail**: `references/comparison-page-updates.md`
→ **Case study**: `references/llm-api-pricing-fable5-update.md`

---

## 3. Page Relocation & Restructuring

### When to Use
- Moving a page to a new directory
- Renaming a page
- Reorganizing directory structure
- Merging directories or splitting pages

### Workflow
1. Verify target and backlinks (`search_files`)
2. Create target directory if needed
3. Copy and transform
4. Remove original
5. Update backlinks (small: `patch` per file; bulk: Python regex script)
6. Update index.md
7. Update log.md
8. Commit and push

### Link Update Patterns
- `[[concepts/old/page]]`
- `[[concepts/old/page|Display Text]]`
- `[[concepts/old/_index]]`
- `[[old/page]]` (relative links)

### Decision Matrix: Subdirectory vs MOC Page

| Signal | Subdirectory | MOC Page |
|--------|--------------|----------|
| Pages share a concrete prefix (≥5) | ✅ | — |
| Pages form a coherent domain by tag (≥5) | ✅ | — |
| Theme is cross-cutting / universal | ❌ | ✅ |
| ≤4 pages in cluster | ❌ | ✅ or skip |

**Universal themes** (too generic for subdirs): `agent-*`, `agentic-*`, `llm-*`, `open-*`, `multi-*`, `software-*`

### Directory Restructuring Patterns
1. `_index.md` to descriptive name
2. Creating new hierarchy
3. Merging directories
4. Semantic classification move (by tags)
5. Directory rename
6. Product tool split (model vs tool pages)
7. Prefix restoration

### Pitfalls
- **Double-prefix display bug**: Ensure display name doesn't duplicate slug prefix
- **Missing relative links**: Search for and update relative links too
- **Prefix stripping**: User preference — keep prefix in filenames even inside subdirectories
- **Overlapping concepts**: Keep separate, add disambiguation blockquotes
- **Prefix suffix capture for directory renames**: Use `(?old-name(/?[^\\\\]|]*?)(?:\\\\|([^\\\\]]+))?\\\\]\\\\]` pattern
- **Symlink + git add**: `git add wiki/` from repo root may not stage changes made through `~/wiki` symlink. Use `git add -A wiki/` and verify with `git show --stat HEAD`.
- **Double-nesting in bulk sed**: If `post-training` is in the moved pages list AND the sed replaces `concepts/post-training` → `concepts/post-training/post-training`, you get triple-nesting. Always verify: `grep -rli "double-pattern/"` after bulk sed.
- **Tag taxonomy violations**: Pre-commit blocks unknown tags. Verify tags exist in SCHEMA.md before committing. Common misses: `exploration`, `interview`, `llm-training`, `rl`.
- **Language enforcement**: Non-raw pages must be in English. Japanese content blocks commit.
- **Scope estimation**: For N moved pages, expect ~2-3N files needing reference updates.

→ **Batch reorg checklist + pitfalls**: `references/batch-directory-reorganization-pitfalls.md`

→ **Full detail**: `references/page-relocation.md`
→ **Batch reorg pitfalls**: `references/batch-directory-reorganization-pitfalls.md` (symlink+git trap, double-nesting, tag validation, scope estimation)

---

## Support Files

### References
| File | Source | Content |
|------|--------|---------|
| `references/daily-structural-health.md` | wiki-watchdog-auto-fix | Full watchdog workflow with all auto-fix patterns |
| `references/comparison-page-updates.md` | wiki-comparison-page-update | Full comparison page update workflow |
| `references/page-relocation.md` | wiki-page-relocation | Full page relocation workflow with all patterns |
| `references/misplaced-stub-cleanup.md` | wiki-watchdog-auto-fix | Detection heuristics for misplaced concept stubs |
| `references/llm-api-pricing-fable5-update.md` | wiki-comparison-page-update | Case study: adding Fable5 to LLM API pricing |
| `references/llm-api-pricing-verification.md` | wiki-maintenance | SPA price verification via OpenRouter API, `~` removal workflow, model name change detection |
| `references/agent-semantic-classification-migration.md` | wiki-page-relocation | Semantic classification of 47 agent pages |
| `references/batch-hierarchy-reorganization.md` | wiki-page-relocation | Multiple sequential directory reorganizations |
| `references/context-engineering-hierarchy-migration.md` | wiki-page-relocation | 16 pages into subdirectory, prefix restoration |
| `references/death-of-browser-relocation-example.md` | wiki-page-relocation | Real-world page relocation example |
| `references/directory-rename-and-product-split.md` | wiki-page-relocation | Directory rename patterns and product splits |
| `references/evaluation-safety-benchmarks-separation.md` | wiki-page-relocation | Three-way taxonomy separation |
| `references/orphan-page-deletion-example.md` | wiki-page-relocation | Orphan page detection and deletion |
| `references/post-relocation-enrichment-pattern.md` | wiki-page-relocation | Enriching relocated pages from past sessions |
| `references/batch-directory-reorganization-pitfalls.md` | wiki-maintenance | Symlink+git trap, double-nesting, tag validation, scope estimation, checklist |

### Scripts
| File | Source | Content |
|------|--------|---------|
| `scripts/build-orphan-sed.py` | wiki-watchdog-auto-fix | Build sed script for orphan insertion |
| `scripts/misplaced-entries-detection.py` | wiki-watchdog-auto-fix | Detect misplaced entries between sections |
