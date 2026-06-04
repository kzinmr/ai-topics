# Periodic Wiki Enrichment — Full Reference

## Workflow
1. Scan recent raw articles by keywords and date
2. Read existing entity/concept pages for gaps
3. Identify new information (financials, product launches, incidents)
4. Patch existing pages with new sections (DO NOT rewrite entire pages)
5. Update index.md and log.md
6. Commit

## Quality Standards
- Incremental updates only (patch, not write_file)
- Source citations: every fact needs URL or file path
- No duplicates: search before creating
- Frontmatter accuracy: update dates and tags

## Stub-to-L3 Expansion
For `status: stub` pages:
1. Web search for recent developments
2. Search raw articles for related content
3. Read existing stub, identify gaps
4. Rewrite with write_file (OK for stubs)
5. Update index.md entry
6. Change `status: stub` → `status: L3`

## Common Patterns
| Scenario | Action |
|----------|--------|
| New fact about entity | Add section via patch |
| New concept from article | Create concept page, update index |
| Financial data | Add to Financials section |
| Incident | Add incident section with date |
