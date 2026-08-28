# Direct-Patch Ingestion — Manual Trending Report → Wiki

> Faster alternative to the delegation-based `wiki-ingestion-workflow.md` when processing
> 3-8 updates manually (not via cron). Works directly in the current session without
> spawning subagents.

## When to Use This vs. Delegation

| Criterion | Direct-Patch (this) | Delegation (wiki-ingestion-workflow) |
|-----------|---------------------|--------------------------------------|
| Update count | 3-8 pages | 10+ pages |
| Session type | Interactive (user present) | Cron (no user) |
| Complexity | Enrichment from report data | Deep article reading + synthesis |
| Speed | Faster (no subagent overhead) | Parallel, but context setup cost |

## Workflow

### Step 1: Gap Analysis via Index + Search

Instead of checking each recommended action individually, do a **batch existence check**:

```
1. Read wiki/index.md (first 30-40 lines) — see what's in the "Updated" sections
2. search_files for key entity/concept names from the report across wiki/
3. Compare report recommendations against found pages
```

This is faster than the `find` + `grep` approach in the standard workflow because
index.md already tells you what was recently updated and by what pipeline.

### Step 2: Classify Each Recommendation

For each item in the report's recommendation table:

| Status | Action |
|--------|--------|
| Page exists + already has the content | **Skip** — other pipeline handled it |
| Page exists + missing this specific data | **Patch** — add section with `patch` tool |
| Page doesn't exist + raw articles available | **Create** — write new page from report + raw articles |
| Page doesn't exist + no raw articles | **Create from report** — use report summary as source |

Most sessions find 50-80% of recommendations already done (the report's own pitfall
section warns about this). Focus on the genuine gaps.

### Step 3: Enrich Entity Pages with Targeted Patches

For entity page updates from trending report data:

1. Read the existing entity page (full content if <200 lines)
2. Find the `## Related` section (or last content section)
3. Patch in a new section **before** `## Related` with:
   - Section header with date: `## Topic Name (Month Year)`
   - Key facts from the report (bullet points)
   - Source link to original article
   - Brief significance statement
4. Update `updated:` date in frontmatter

**Pattern**: The trending report's summary paragraphs are already well-synthesized.
You can often use them nearly verbatim as the wiki section content, adjusting only
formatting (add wikilinks, convert to bullet points, add source attribution).

### Step 4: Create Missing Concept Pages

For new concept pages recommended by the report:

1. Check if a related concept already exists (e.g., `voice-agent-evaluation` might
   be covered under a broader `voice-ai` page)
2. Use the report's summary + any available raw articles as source
3. Follow SCHEMA.md page thresholds (minimum content requirements)
4. Add at least 2 wikilinks to existing pages
5. Include YAML frontmatter with proper tags from taxonomy

### Step 5: Update Index + Log + Commit

Same as standard workflow:
1. Patch `index.md` — add entries to "Updated" sections
2. Patch `log.md` — prepend log entry with summary
3. `git add wiki/ && git commit && git push`

## Pitfalls

1. **Don't re-fetch articles the report already summarized**: The trending report
   is a curated synthesis. For simple enrichments (adding a product launch section,
   a case study, a benchmark result), the report summary is sufficient source material.
   Only fetch the original article if you need detailed technical specs or direct quotes.

2. **Patch order matters**: Update `updated:` date first, then content. If you patch
   content first and the date patch fails, you have stale metadata.

3. **Don't create stub pages**: If the report recommends a page but you don't have
   enough content for a meaningful page (30+ lines), skip it or merge the info into
   an existing related page. A 15-line stub page is worse than a well-placed paragraph
   in an existing page.

4. **Check for "already enriched" signals**: If an entity page's `updated:` date is
   within 2 days of the report date, and the report mentions the same topic, it was
   likely already processed by another pipeline. Search for key terms in the page body
   before adding duplicate content.
