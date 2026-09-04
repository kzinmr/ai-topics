# Project Evolution Timeline Enrichment

When multiple provided sources span a project's history (precursor article → current release), the enrichment should surface the **evolutionary arc**, not just append new facts.

## Pattern: Historical Evolution Table

When sources reveal a project went through name changes, architectural shifts, or major redesigns, add an explicit evolution table:

```markdown
## Historical Evolution

| Date | Milestone | Key Difference |
|------|-----------|----------------|
| Jul 2025 | `datasette-llm-agent` (Substack post) | Claude-only, tool-use based (4 hardcoded tools) |
| May 2026 | `datasette-agent` 0.1a1–0.1a3 (public launch) | Multi-model, plugin architecture, LLM library integration |
```

This is more useful than scattered mentions across sections because:
- Readers can immediately see the timeline
- Name changes / architectural pivots are explicit
- The "why" of the current design becomes clear from the diff

## Workflow

1. **Date-check sources**: When sources span 6+ months, suspect evolution. Sort by date.
2. **Identify pivots**: Name changes, architecture shifts, scope changes, new dependencies.
3. **Add evolution table** near the top of the page (after Overview), before detailed feature sections.
4. **Cross-reference precursor**: Add precursor article to `sources` frontmatter, but note it describes the earlier incarnation.
5. **Update description**: The entity description should reflect the current state, with evolution context in the body.

## Pitfalls

- **Don't overwrite**: The existing page may have months of accumulated detail. Use `patch` to add the evolution table and new sections, never `write_file` on a rich page.
- **GitHub URL verification**: User-provided GitHub URLs may differ from actual repos. Blog posts link to the canonical repo (e.g., `simonw/datasette-agent`), while users may provide an org URL (`datasette/datasette-agent`). Always use the URL from the authoritative source (blog/docs), not the user's guess.
- **Precursor vs current**: Don't let precursor architecture details (e.g., "4 hardcoded tools") appear in the main feature list. Put them in the evolution table or a "Historical" section only.
