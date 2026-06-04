---
name: wiki-wikilink-remediation
category: wiki
description: Add wikilinks to plain-text mentions of a newly-created page across the wiki
---

# Wiki Wikilink Remediation

When you create a new wiki page (concept, entity, comparison), update existing pages that mention the topic as plain text to use proper `[[wikilink]]` references.

## Workflow

### Step 1: Identify files mentioning the topic as plain text

```python3
from hermes_tools import search_files
results = search_files(pattern="MCP|mcp|Model Context Protocol", target="content", path="/opt/data/ai-topics/wiki", output_mode="content", limit=200)
```

Then filter out files that already have the wikilink:
```python3
need_update = []
for match in results.get("matches", []):
    path = match["path"]
    if "concepts/mcp.md" in path:  # skip the new page itself
        continue
    if "[[mcp" in match["content"].lower():
        continue  # already has wikilink
    if path not in need_update:
        need_update.append(path)
```

### Step 2: Prioritize updates

**Tier 1 — Must update (entity pages):**
- Entity pages that discuss or reference the concept (e.g., `philipp-schmid.md`, `claude-code.md`)
- Always use `[[mcp|Model Context Protocol]]` format with display text

**Tier 2 — Should update (concept pages):**
- `_index.md` files (add the new page to the concept index)
- Adjacent concept pages (e.g., `cli-over-mcp-pattern.md`, `code-execution-with-mcp.md`)

**Tier 3 — Nice to update:**
- Comparison pages
- Query pages
- Other concept pages that mention the topic

### Step 3: Add to index files

**For concepts:** Add to `concepts/_index.md`:
```markdown
## MCP (Model Context Protocol)
- [[mcp]] — One-line summary of the page.
```

**For entities:** Add to `entities/_index.md` similarly.

**For main index.md:** Add the one-line entry to the appropriate section (e.g., Networking & Protocols), and bump the page count header.

### Step 4: Update log.md

Add an entry at the top of `log.md`:
```markdown
## [YYYY-MM-DD] trending-topics | <topic> wiki update + wikilink remediation
- **New page**: [[slug]] (<file path>) — <one-line description>
- **Schema update**: <if any tags were added>
- **Wikilink remediation**: Added [[slug]] wikilinks to N entity pages and M concept pages
- **Index update**: Added <topic> to index.md, <section> count X→Y
- **Sources**: <list key source articles>
```

### Step 5: Commit and push

```bash
cd /opt/data/ai-topics && git add wiki/ && git commit -m "wiki: <topic> concept page + wikilink remediation" && git push
```

## Wikilink Format Guidelines

| Case | Format | Example |
|------|--------|---------|
| Entity page | `[[slug]]` | `[[anthropic]]` |
| Concept page | `[[slug]]` | `[[mcp]]` |
| Plain text first mention | `[[slug|Display Text]]` | `[[mcp|Model Context Protocol]]` |
| Already has display text | Keep it | `[[mcp|MCP]]` |

## Common Pitfalls

1. **Don't over-link**: Only link when the mention refers to the concept/page as a topic, not as a casual word usage
2. **Skip raw articles**: Raw articles in `wiki/raw/articles/` are transient — don't add wikilinks there
3. **Don't replace all occurrences**: A paragraph might mention "MCP" once as the topic and again casually — only link the meaningful mention
4. **Use `patch`, not `sed`**: The wiki uses fuzzy matching — `patch` handles indentation differences better
5. **Read before patching**: If a file was read with offset/limit, re-read it before patching to avoid stale context
6. **Check both paths**: Files may exist at `/opt/data/ai-topics/wiki/` or `~/wiki/` — use absolute paths

## Related Skills

- `wiki-bulk-link-fix` — Fix broken wikilinks (links that don't resolve)
- `wiki-graph-health` — Entity deduplication and concept link gap detection
- `wiki-entity-enrichment-from-article` — Create wiki pages from raw articles