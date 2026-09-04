# Blog Triage — Entity Enrichment from Blog Post

When a triaged blog post is **from an existing tracked entity** (e.g., antirez publishing a new essay, Simon Willison linking to a tool), the enrichment follows a lighter, more focused pattern than the full `wiki-entity-enrichment-from-article` workflow. The entity page already exists and is rich; the goal is to **add the new content incrementally**.

## When to Use This Pattern

- Blog post is from an author/org that already has a wiki entity page
- The post contains substantive new ideas, not just a link or version bump
- The post is relevant to the wiki's AI/LLM domain

## Workflow (6 steps)

### 1. Bump `updated` date in frontmatter
```yaml
updated: YYYY-MM-DD  # today's date
```

### 2. Add raw article to `sources:` list
```yaml
sources:
  - raw/articles/existing-source.md
  - raw/articles/new-blog-post--hash.md  # ← add
```

### 3. Add timeline entry
Insert a new row in the Timeline table, maintaining reverse-chronological order:
```markdown
| YYYY | Published "Title" — one-line description of key insight |
```

### 4. Add detailed section
Place after the most recent section (often before "Related" or "Influence Metrics"). Structure:
- **Section heading**: `### Title — Subtitle (Month YYYY)`
- **Context**: 1-2 sentences on what the post is and why it matters
- **Key points**: Subsections with `####` for major ideas
- **Quotes**: Use `>` blockquotes for the author's most memorable lines
- **Connection to existing themes**: Explicit `[[wikilink]]` to related concept pages
- **Related links**: Link to original post, YouTube video if applicable

### 5. Update Recent Themes bullet
If the post extends an existing theme, update the bullet description. If it introduces a new theme, add a new bullet.

### 6. Cross-link from new section to concept pages
Every new section should have at least one `[[wikilink]]` to a concept page. If the concept doesn't exist yet, consider creating it as a separate triage action.

## Example (antirez "Being Linux Torvalds", July 2026)

Source: `antirez.com/news/171` — essay on Linus Torvalds as metaphor for AI agent orchestration

**Steps performed:**
1. `updated: 2026-07-26`
2. Added `raw/articles/antirez.com--news-171--99acb946.md` to sources
3. Added timeline row: `| 2026 | Published "Being Linux Torvalds" — ... |`
4. Added section `### Being Linux Torvalds: The Programmer as Orchestra Director (July 2026)` with subsections on Core Analogy, Vibe Coding vs Automatic Programming, Key Insight, Connection to concepts
5. Updated Recent Themes bullet for "AI-assisted programming" to mention "orchestrator" framing
6. Cross-linked to `[[concepts/ai-assisted-development]]` and `[[concepts/vibe-coding]]`

## Pitfalls

- **Don't overwrite rich pages**: Always use `patch`, never `write_file` on entity pages with >40 lines
- **Don't create duplicate sections**: If the entity page already covers the topic (e.g., antirez already has a "Vibe Coding" section), reference it rather than restating
- **Timeline entries go BEFORE the most recent entry**, not at the end — maintain reverse-chronological order
- **Sources list**: Append to the END of the sources list, don't reorder existing entries
- **Commit with raw articles**: The raw article file should be part of the same git commit as the entity page update

## Practical Patch Sequence (Cron-Safe)

When running as a cron job, `execute_code` is blocked. Use individual `patch` calls in this order:

```
1. patch: updated: YYYY-MM-DD  (frontmatter date)
2. patch: sources: list         (append new raw article path)
3. patch: new section           (insert before "## Related" or at end of body)
   - If article corrects outdated info on the SAME page, patch those spots too
4. patch: log.md                (prepend triage summary entry)
5. terminal: git add wiki/ && git commit && git push
```

For **multi-article triage** (common in blog-ingest): read all raw articles first, identify which need wiki updates, then batch all patches for the same file before moving to the next file. This minimizes context switches.

If an article provides updated information that contradicts existing page content (e.g., a spec field changed from "max-only" to "low/high/max"), patch the spec table AND scan the full page for all prose references to the outdated value — caveats, benchmark notes, and comparison tables often contain stale references.
