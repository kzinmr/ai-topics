# Critical Article Ingestion Pattern (Controversy & Criticism)

When ingesting an article that **criticizes** an existing wiki entity (company, tool, person, project), do NOT create a separate "criticism" page. Instead, add a structured "Controversy & Criticism" section to the existing entity/concept page.

## When to Use This Pattern

- Article presents factual criticisms with sources (not just opinions)
- The target entity already has a wiki page
- The criticism is substantive enough to affect how someone evaluates the entity
- Examples: attribution disputes, license violations, misleading practices, security vulnerabilities, vendor lock-in

## Section Structure

```markdown
## Controversy & Criticism (YYYY–YYYY)

[Brief intro sentence with link to the primary source article]

### [Issue Category 1]
- Bullet points with specific claims and evidence
- Include dates, GitHub issue numbers, specific quotes where available
- **Bold key metrics** (e.g., "1.8x faster", "400+ days without response")

### [Issue Category 2]
- ...

### [Alternative/Recommended Tools]
| Tool | Type | Description |
|------|------|-------------|
| ... | ... | ... |
```

## Workflow

1. **Read the existing page** — `read_file` to understand current content and structure
2. **Save the critical article as raw source** — `wiki/raw/articles/{date}_{source}_{slug}.md`
3. **Identify the right insertion point** — typically after the main description/features, before "Related Pages" or "Sources"
4. **Add sources to frontmatter** — append the critical article URL to the `sources:` list
5. **Add tags** — `controversy` and `vendor-lock-in` (if applicable) are canonical SCHEMA.md tags
6. **Write the section** — use `patch` (never `write_file` on rich pages)
7. **Update the entity's "Related wikilinks"** — link to alternative tools mentioned
8. **Update index.md** — enhance the entity's description to mention the controversy
9. **Update log.md** — record the enrichment

## Example (Ollama, June 2026)

Source: "Friends Don't Let Friends Use Ollama" (Zetaphor, sleepingrobots.com)
Target: `wiki/concepts/local-llm/ollama.md` (129 lines, rich page)

**What was added:**
- "Controversy & Criticism (2024–2026)" section with 7 subsections
- Attribution & License Issues, ggml Fork, Misleading Model Naming, Closed-Source App, Modelfile & Registry Lock-in, Cloud Pivot, VC Pattern
- "Recommended Alternatives" table (llama.cpp, llamafile, Jan, koboldcpp, LM Studio, ramalama)
- Tags: added `controversy`, `vendor-lock-in`
- Sources: added the article URL and HN discussion link

**What was NOT done:**
- Did NOT create a separate "ollama-controversy.md" page
- Did NOT rewrite the existing architecture/features sections
- Did NOT remove positive content about Ollama

## Key Principles

1. **Preserve existing content** — criticism supplements, not replaces
2. **Source everything** — link to specific GitHub issues, commits, quotes
3. **Include community perspective** — HN comments add credibility
4. **Offer alternatives** — a criticism section without alternatives is incomplete
5. **Date the controversy** — "Controversy & Criticism (2024–2026)" sets time bounds
6. **Use `patch`, never `write_file`** — this is always an enrichment of an existing rich page

## Pitfalls

- **Don't be one-sided**: If the entity has responded to criticism or if there are valid counterpoints (e.g., "Ollama solved the UX problem"), note them
- **Don't create duplicate tags**: `controversy` is canonical; don't invent `criticism` or `anti-ollama`
- **HN comments as source**: HN comments are community perspective, not authoritative sources. Use them to illustrate community sentiment, not as primary evidence
- **GitHub issue numbers**: Always include specific issue numbers (#3185, #8557, etc.) — they're verifiable and permanent
