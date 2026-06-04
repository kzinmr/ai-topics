# Batch Company Entity Creation from Curated Lists

When processing a large curated company list (e.g., Paraform Talent Density Index, YC batches, startup rankings), use delegate_task subagents for parallel research + page creation.

## Workflow

### 1. Pre-check existing pages

```python
import os
entities_dir = "/opt/data/ai-topics/wiki/entities/"
def slug(name):
    return name.lower().replace(" ", "-").replace(".", "")

for company in companies:
    path = f"{entities_dir}{slug(company)}.md"
    status = "EXISTS" if os.path.exists(path) else "MISSING"
```

Split into existing (skip) and missing (create) lists.

### 2. Batch into groups of 13-14 for delegate_task

Each subagent handles ~13 companies. Provide:
- The exact list of company names and slugs
- A strict entity page template (YAML frontmatter + sections)
- The absolute path `/opt/data/ai-topics/wiki/entities/` (NOT `~/wiki/entities/`)
- Rules: minimum 2 wikilinks, 50-80 lines, blog URL discovery

### 3. Template for subagent context

The subagent prompt must include:

```
## Entity Page Format (STRICT - follow this template exactly)
```yaml
---
title: "Company Name"
type: entity
created: 2026-05-08
updated: 2026-05-08
tags:
  - company
  - [relevant tags: ai-agents, model, platform, infrastructure, product]
aliases: ["ShortName"]
sources:
  - https://company-website.com
---

# Company Name

Brief 1-2 sentence overview of what the company does.

| | |
|---|---|
| **Type** | [AI Research Lab / AI Infrastructure / AI Platform / etc.] |
| **Founded** | YYYY (City, Country if known) |
| **Leadership** | CEO Name (CEO), other key people |
| **Key Products** | Product1, Product2, Product3 |
| **Website** | [company.com](https://company.com) |
| **Tech Blog** | [blog.company.com](https://blog.company.com) (if found; otherwise omit this row) |

## Key Facts
- Fact 1

## Products & Technology
Brief section on key products and what they do.

## Related
- [[entities/openai]] — relationship note
- [[entities/anthropic]] — relationship note
```

## CRITICAL RULES
- Save to /opt/data/ai-topics/wiki/entities/ (absolute path, NOT ~/wiki/)
- File names: lowercase-hyphens
- Minimum 2 [[wikilinks]] per page
- Check /blog, /engineering, /rss.xml, /feed.xml for tech blogs
- Verify each file written with read_file or search_files
- Keep pages ~50-80 lines
```

### 4. Subagent output format

Each subagent should return a summary table:

| Company | File | Blog URL | Notes |
|---------|------|----------|-------|
| ... | entities/foo.md | https://foo.com/blog | ... |

### 5. Verify and integrate

After all subagents return:
1. Verify files exist: `os.path.exists()` for each expected path
2. Handle timeouts (subagent may exit with "timeout" but files may still be written — check filesystem first)
3. Collect all blog URLs for RSS/sitemap monitoring setup
4. Update `index.md` — append all new entity entries at end of Entities section via `patch`
5. Update `log.md` — single batch entry listing all created files
6. Commit: `git add wiki/entities/ wiki/index.md wiki/log.md && git commit && git push`

### 6. Pitfalls

- **Subagent timeouts**: Group C of 14 may timeout on slow websites. Check filesystem anyway — files are often written before timeout occurs.
- **Template drift**: Subagents may deviate from the template (add extra sections, omit frontmatter). Spot-check 2-3 pages per batch.
- **Wikilink quality**: Subagents may link to non-existent pages. Patch broken links after verification.
- **Index insertion**: The Entities section at scale is NOT strictly alphabetical. Append all entries at the section end rather than trying to compute alphabetical insertion points.
- **Blog URL accuracy**: Subagents may guess blog URLs rather than verify. Cross-check against actual website navigation.
