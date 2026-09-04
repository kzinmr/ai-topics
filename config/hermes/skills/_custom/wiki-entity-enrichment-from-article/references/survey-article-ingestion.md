# Large Survey Article Ingestion

When ingesting a comprehensive technical survey (e.g., Lilian Weng's blog posts, Anthropic research reports), the article typically covers multiple distinct concepts that warrant separate wiki pages. This is a **multi-page ingestion** pattern, not a single-page enrichment.

## Workflow

### 1. Fetch & Save Raw Article
```bash
curl -sL "https://r.jina.ai/URL" -H "Accept: text/markdown" > /tmp/article.md
# Save to wiki/raw/articles/YYYY-MM-DD_source-slug.md
```

### 2. Identify Page Targets
Scan the article for distinct concepts/topics. Each major section (with its own bibliography, systems, or frameworks) is a candidate for a standalone concept page.

Decision criteria:
- **Standalone page**: Section covers a distinct concept with 3+ systems/papers/examples (e.g., "Recursive Self-Improvement" as a concept distinct from "Harness Engineering")
- **Append to existing page**: Section extends a concept already in the wiki (e.g., adding RSI perspective to existing harness-engineering.md)
- **Both**: Create standalone page AND add summary+link to existing related page

### 3. Check Existing Wiki (MANDATORY)
```
search_files(pattern="concept-name", target="files", path="~/wiki/concepts")
search_files(pattern="author-name", target="content", path="~/wiki")
```
- Existing entity page → update timeline, themes, sources, related concepts
- Existing concept page → append new section or create standalone + cross-reference
- No existing page → create new

### 4. Create/Update Pages
For each identified page target:
1. Save raw article (only once)
2. Create concept page(s) with full content
3. Update entity page (timeline entry, Recent Themes, Related Concepts, Sources)
4. Add bidirectional `[[wikilinks]]` between all related pages

### 5. Page Splitting Pattern
When a section within an existing concept page grows too large (>50 lines or covers a distinct subtopic):
1. Create standalone concept page with full content
2. Replace original section with **concise summary + `→ Full details: [[concepts/new-page]]`**
3. Add cross-reference in Related Concepts of both pages
4. Update index.md with new page entry

### 6. Cross-Entity Knowledge Linking
When creating a concept page for a major topic (e.g., RSI), search the wiki for related content from other entities:
```
search_files(pattern="keyword1|keyword2", target="content", path="~/wiki/entities")
search_files(pattern="keyword1|keyword2", target="content", path="~/wiki/concepts")
```
- Add sections referencing existing raw articles and entity pages
- Link to related safety/governance concept pages when applicable
- Add bidirectional references in both the new page and the referenced pages

### 7. Update index.md + log.md + Commit
Standard wiki update cycle, but with multiple pages:
1. Update/create entries in index.md for ALL modified/created pages
2. Append single log.md entry listing all changes
3. Commit with summary of all pages affected

## Pitfalls

- **Frontmatter YAML editing**: When adding new tags to frontmatter, be careful not to merge `tags:` and `aliases:` sections. Read the exact surrounding context before patching. Common error: adding tags after the last tag line but before `aliases:`, accidentally removing the `aliases:` key.
- **Tag taxonomy**: Always verify new tags exist in SCHEMA.md. Common mismatches: `auto-research` → `autoresearch`, `self-improvement` → `self-improving` or `recursive-self-improvement`. The pre-commit hook blocks unknown tags.
- **Rich page overwrite**: Never use `write_file` on existing concept/entity pages with >40 lines. Always `read_file` first, then `patch` to append/modify.
- **Duplicate raw articles**: Check `wiki/raw/articles/` before saving. The same URL may have been ingested via newsletter or blog pipeline.
- **Cross-reference completeness**: When adding a cross-reference from page A to page B, also add the reverse reference from B to A (bidirectional linking).

## Example: Lilian Weng "Harness Engineering for Self-Improvement" (July 2026)

**Pages created/modified:**
- `raw/articles/2026-07-04_lilianweng-harness-engineering-self-improvement.md` — raw article
- `concepts/recursive-self-improvement.md` — NEW standalone page (RSI concept, 21 references)
- `concepts/harness-engineering.md` — UPDATED: RSI section added (later split into standalone)
- `entities/lilian-weng.md` — UPDATED: timeline, themes, sources, related concepts
- `entities/anthropic.md` — UPDATED: cross-reference to RSI concept

**Key decision**: RSI was initially a section within harness-engineering.md, then split into its own page because it covered a distinct concept with its own bibliography and cross-cutting concerns (safety, evolutionary search, auto-research).
