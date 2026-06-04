# Wiki Wikilink Remediation

When you create a new wiki page, update existing pages that mention the topic as plain text to use `[[wikilink]]` references.

## Workflow
1. Identify files mentioning the topic as plain text via `search_files`
2. Filter out files that already have the wikilink
3. Prioritize: Tier 1 (entity pages) → Tier 2 (concept pages) → Tier 3 (comparison pages)
4. Add to index files: concepts/_index.md, entities/_index.md, main index.md
5. Update log.md and commit

## Wikilink Format
| Case | Format | Example |
|------|--------|---------|
| Entity page | `[[slug]]` | `[[anthropic]]` |
| Concept page | `[[slug]]` | `[[mcp]]` |
| First mention | `[[slug|Display Text]]` | `[[mcp|Model Context Protocol]]` |

## Pitfalls
- Don't over-link (only topic mentions, not casual word usage)
- Skip raw articles
- Use `patch`, not `sed`
- Check both paths: files may exist at `/opt/data/ai-topics/wiki/` or `~/wiki/`
