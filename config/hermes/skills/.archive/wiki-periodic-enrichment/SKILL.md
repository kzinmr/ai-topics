---
name: wiki-periodic-enrichment
description: Periodic review of recent raw articles and incremental update of existing wiki entity pages with new information.
trigger: When asked to review recent articles, update existing wiki pages with new info, or periodic enrichment of entity pages.
---

# Periodic Wiki Page Enrichment

## Purpose
Scan recent raw articles for information gaps in existing wiki pages and fill them incrementally — without creating duplicate pages.

## Workflow

### 1. Scan for Relevant Articles
```python
import glob, os
raw_dir = os.path.expanduser('~/ai-topics/wiki/raw/articles/')
files = glob.glob(os.path.join(raw_dir, '*.md'))

# Filter by keywords and date
keywords = ['claude', 'anthropic', 'opus', 'sonnet', 'boris', 'cat-wu', 'glasswing', 'mythos']
```
- Filter by keyword matching filename
- Filter by date (past N days based on user request)
- List relevant files with sizes

### 2. Read Existing Entity Pages
- Load existing entity/concept pages that might need updates
- Identify what's already covered vs. new info in articles
- Check for gaps, outdated info, missing sections

### 3. Identify Gaps & New Information
- Compare article content against existing page content
- Note new facts: financial data, product launches, incidents, code names, strategy changes
- Prioritize: major developments first (e.g., $30B ARR, source code leak, model withholding)

### 4. Patch Existing Pages
- Use `patch` to add new sections to existing pages (DO NOT rewrite entire pages)
- Add new subsections with clear headers
- Include source citations in format: `[Article Title](URL) (Date)`

### 5. Update Index.md
- Add new concept/entity entries to `wiki/index.md` in appropriate section
- Update section counts if needed
- Use `patch` for targeted addition

### 6. Update Log.md
- Prepend new entry with today's date
- Summarize: entity pages updated, concepts added, articles processed
- Include processed article list with counts

### 7. Commit & Push
```bash
cd ~/ai-topics
git add wiki/entities/ wiki/index.md wiki/log.md
git commit -m "wiki: <summary> - processed N articles from past N days
- Updated: entity names
- Added: new concepts/entities to index"
git push
```

## Quality Standards
- **Incremental updates only**: Never rewrite existing pages; add sections via patch
- **Source citations**: Every new fact must have a URL or file path
- **No duplicates**: Always check if entity/concept already exists before creating
- **Consistent formatting**: Match existing page style (Japanese/English as appropriate)
- **Frontmatter accuracy**: Ensure dates and tags are updated on modified pages

## Stub-to-L3 Expansion Pattern
When a concept page has `status: stub`:
1. Run `web_search` for recent developments on the topic (2-3 queries with different keywords)
2. Run `search_files` in `wiki/raw/articles/` for related raw content
3. Read existing stub to identify what's already covered vs. missing
4. Rewrite with `write_file` (full replacement OK for stubs) including:
   - Overview section (what the concept is, why it matters)
   - Key players/models/tools with dates and specs
   - Architectural patterns or workflows
   - Competitive landscape table
   - Related wiki pages with `[[wikilinks]]`
   - Sources section with URLs
5. Update `index.md` entry from `> **TODO**: Enrich this page.` to actual description
6. Change frontmatter `status: stub` → `status: L3`

## Common Patterns
| Scenario | Action |
|----------|--------|
| New fact about existing entity | Add section to entity page via patch |
| New concept from article | Create concept page, update index.md |
| Code name / alias discovered | Add alias section to entity page |
| Financial data (ARR, valuation) | Add to Financials/Company Info section |
| Incident (leak, security) | Add incident section with date |
| Strategy/planning (summit, roadmap) | Add Corporate Strategy section |
| **Batch related-page update** | Update all related entity/concept pages in one session (e.g., OpenAI + Sam Altman + Anthropic + Claude Code), then single `git commit -m` covering all changes |
| **New entity creation** | Create entity page (L3 quality), add to `index.md` in alphabetical order, update `frontmatter.updated` to today |

## Pitfalls
- **Don't overwrite existing content**: Use patch with unique context strings
- **Don't skip log.md**: Always record changes for audit trail
- **Don't create pages that already exist**: Search `wiki/entities/` and `wiki/concepts/` first
- **Don't forget index.md**: New entries must be referenced in index
- **Date filtering**: Past "N days" means cutoff = today - N days; include articles from cutoff date onwards
- **Substack articles**: Often contain only placeholder text ("Introducing the Substack app"); fall back to original URL if content is missing

## Git Push Troubleshooting
Same as `wiki-entity-enrichment-from-article` skill — if push fails, save commits locally and notify user.