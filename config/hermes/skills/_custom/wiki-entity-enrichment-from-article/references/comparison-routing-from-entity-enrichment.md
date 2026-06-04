# Comparison Page Routing (from wiki-entity-enrichment sessions)

## Rule

When enriching an entity page and the user ALSO asks for a comparison across 3+ items (e.g., "compare OpenClaw, Claude Code, and Codex memory systems"), the comparison page MUST go to `wiki/comparisons/`, NOT `wiki/concepts/`.

## Litmus Test

If all comparison tables were removed from the page, would it still be a coherent concept page?

- **YES** → `wiki/concepts/` is correct
- **NO** → `wiki/comparisons/` is required

## Example Violation

**Session 2026-05-17**: Enriched OpenClaw entity page + created `concepts/agent-memory-systems-comparison.md` comparing 3 harnesses' memory systems. Should have been `comparisons/agent-memory-systems-comparison.md`. The page IS the comparison — removing all tables leaves no coherent concept.

## Fix Procedure

When a comparison page is discovered in `concepts/`:
1. `mv wiki/concepts/<name>.md wiki/comparisons/<name>.md`
2. Update frontmatter: `type: comparison`, add `moved_from: [concepts/<name>.md]`
3. Update all `[[concepts/<name>]]` wikilinks → `[[comparisons/<name>]]` across all wiki pages
4. Update `wiki/index.md` entry to point to `comparisons/`
5. Update `wiki/log.md` with correction note
6. `git add -A && git commit -m 'wiki: move <name> from concepts/ to comparisons/ (routing fix)'`

## Prevention

Always load `wiki-comparison-page-routing` skill before creating any new wiki page in an entity-enrichment session when the user asks for a comparison.
