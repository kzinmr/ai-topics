# Wiki Health Remediation

Full procedure for decision-matrix-driven remediation of wiki health issues.

## Health Issue Categories

### 1. Duplicate Pages
**Decision matrix:**
- Partner is skeleton stub (<500 chars) → Delete stub, partner = canonical
- Partner has richer content → Merge unique content into richer partner, delete stub
- Both have comparable depth → Keep more specific path (subdirectory), redirect root-level

**Merge procedure:** Read both files, identify unique sections, create merged file at partner path, delete lesser file, verify no broken wikilinks.

### 2. Skeleton Pages (`status: skeleton`)
**Decision matrix (priority order):**
- Partner file exists with rich content → Replace with redirect
- Referenced by ≥3 pages → Expand with web search, set `status: complete`
- Has >200 chars but still skeleton → Check partner, then expand or redirect
- <100 chars, no real content → Delete

### 3. Thin Pages (No skeleton marker)
| Size | Action |
|------|--------|
| <300 chars | Check for partner → redirect, else delete |
| 300-1000 chars | Check if referenced → redirect if partner exists, else expand |
| >1000 chars | Keep, review frontmatter |

### 4. Tag Consolidation
- Malformed YAML: `- [[rag]]`, `- concepts/rag` → `- rag`
- Case variants: `rAG`, `Rag` → `rag`
- Mixed delimiter, wiki-style references, typos, whitespace issues
- Fix procedure: audit first with Python, fix malformed tags via regex, consolidate synonyms, update SCHEMA.md

### 5. Post-Bulk-Ingest Cleanup
**Part A: Generated File Cleanup**
- Read bulk record from `~/wiki/bulk-processing/bulk-*.md`
- Audit what exists
- Deduplicate against existing entities
- Fix malformed YAML frontmatter
- Delete empty concept stubs

**Part B: Resolving 「ファイル未作成」**
Categorize each:
- Already exists (different slug) → ✅ mapped
- Already exists as concept → ✅ concept exists
- News/media outlet → Skip
- Non-AI platform → Skip
- arXiv-only (no peer review) → Skip
- Genuinely needs creation → Create full page

### 6. Execution Order
1. Duplicate resolution first
2. Skeleton expansion/redirect
3. Thin page cleanup
4. Frontmatter batch update

## Large-Scale Patterns

### Pattern 1: Corrupted filenames with special characters
Use Python glob + file size to identify and remove corrupted variants.

### Pattern 2: Missing `type` field across many pages
Auto-detect from directory structure (entities/ → type: entity, concepts/ → type: concept).

### Pattern 3: Systematic broken wikilinks (missing directory prefix)
Build slug-to-path map, fix in bulk with regex.

### Pattern 4: Rebuilding index.md from scratch
Scan all pages, extract frontmatter, group by type, generate markdown.
