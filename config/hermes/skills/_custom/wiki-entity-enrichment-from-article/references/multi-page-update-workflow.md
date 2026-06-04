# Multi-Page Wiki Update Workflow

When an article touches multiple existing wiki pages (common for Hornet blog series, Karpathy posts, etc.), follow this sequence to avoid rework.

## Sequence (in order)

1. **Create raw article** → `wiki/raw/articles/YYYY-MM-DD_source_slug.md`
   - Frontmatter: `title`, `author`, `source`, `date`, `tags`
   - Body: Summary, Key Points (quoted data tables), Related links
   - Tags must already exist in `SCHEMA.md` — add new tags there first if needed

2. **Identify affected pages** — search `index.md` and `wiki/` for the entity/concept name
   - Typically: 1-2 concept pages + 1 entity page (author) + possibly comparisons

3. **Update each page** (use `patch` mode, NOT `execute_code` — execute_code may be blocked in cron/delegation contexts):
   - Add source to `sources:` frontmatter list
   - Bump `updated:` date
   - Add new tags if needed (also add to SCHEMA.md)
   - Add substantive content section with data tables and quotes
   - Add wikilinks to new/related pages

4. **Update `index.md`** — refresh description strings for changed pages with new data points

5. **Update `log.md`** — append entry with:
   - Source URL and author
   - Raw article path
   - Per-page changes (sections added, tags added)
   - Connection to related articles (e.g., "Part 3 of X series")

6. **Git commit + push** — single commit for the entire batch

## Pitfalls

### Markdown Table Formatting
When using `patch` to add rows to existing markdown tables, **match the exact pipe pattern** of the surrounding rows. Common mistake: introducing `||` (double pipe) when the table uses `|` (single pipe). This creates rendering bugs that are hard to spot in diff output.

**Bad** (accidentally introduced double-pipe):
```
|| May 2026 | Publishes "..." |
```

**Good** (matches existing table format):
```
| May 2026 | Publishes "..." |
```

**Fix**: After editing a table, re-read the affected lines to verify pipe consistency before moving on.

### execute_code Blocked in Cron Context
`execute_code` calls that use `from hermes_tools import patch` will be BLOCKED when running inside cron jobs or certain delegation contexts. Use direct `patch` tool calls instead — they work everywhere.

**Pattern**: Make individual `patch` calls for each edit. This is slower but reliable. Batch via `execute_code` only when running in normal interactive sessions.

### SCHEMA.md Tag Validation
Every tag on a page must exist in `SCHEMA.md`'s taxonomy. The pre-commit hook (`pre-commit-tag-validator.py`) will block commits with unknown tags. **Always add new tags to SCHEMA.md FIRST**, then use them in pages.

### CJK Character Detection
Wiki pages (excluding `raw/`) are English-only. The pre-commit hook blocks commits containing CJK characters. If you copy Japanese/CJK content from the user's request, translate it to English before writing to wiki pages.

### Tutorial / Framework Doc Scraping
When scraping tutorial or framework documentation pages (Qdrant, Neon, LangChain, etc.), the first curl often returns only navigation/sidebar content. The actual tutorial body is rendered client-side or lives deeper in the HTML.

**Pattern that works**: Extract the `<main>` tag content specifically:
```python
main = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
if main:
    html = main.group(1)
```
Then strip `<script>`, `<style>`, `<nav>`, `<header>`, `<footer>` tags before converting to text.

If the first attempt still returns mostly navigation (TOC links, breadcrumbs), try printing the middle third of the extracted text — tutorials often have their content body after a long navigation preamble.

### index.md Concurrent Edits
Multiple pipelines may edit `index.md` simultaneously (watchdog, blog-ingest, newsletter-ingest). After editing, check for `_warning` messages about sibling modifications. Re-read the file if warnings appear.
