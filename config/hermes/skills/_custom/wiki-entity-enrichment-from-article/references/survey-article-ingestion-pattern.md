# Survey Article Ingestion Pattern

When a comprehensive blog post (e.g., Lilian Weng's surveys, Karpathy's tutorials) introduces many new research systems under one umbrella topic, the ingestion strategy depends on whether an existing concept page covers the umbrella.

## Decision Tree

1. **Does an existing concept page cover the umbrella topic?**
   - YES → Add a focused section to the existing page (preferred)
   - NO → Create ONE new concept page for the umbrella

2. **For each individual system mentioned in the survey:**
   - Does it have ≥3 distinct conceptual subsections as a standalone topic?
   - Does it appear in ≥2 independent sources outside this survey?
   - Both YES → Consider a standalone concept page
   - Otherwise → Keep as a row in a table or bullet in the survey section

3. **Never create thin stub pages** for each system mentioned in a survey — they become orphans with no independent substance.

## Workflow

1. Extract article content (Jina Reader for blogs, pymupdf for PDFs)
2. Check existing wiki: `search_files` in `wiki/index.md` for umbrella topic
3. Save raw article to `wiki/raw/articles/YYYY-MM-DD_slug.md`
4. Update existing concept page:
   - Add `## <Author>'s <Topic> (<Date>)` section before `## References` or `## Related Concepts`
   - Summarize key contributions in structured format (tables for comparisons, bullets for systems)
   - Update frontmatter: `updated`, `tags` (add new tags if needed), `sources`
5. Update entity page (author):
   - Add timeline entry
   - Add new theme to Recent Themes
   - Add related concept wikilink
   - Add source URL
6. Update `index.md` — enrich descriptions of updated entries
7. Update `log.md` — single log entry covering all files touched
8. Commit atomically: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push`

## Example: Lilian Weng "Harness Engineering for RSI" (Jul 2026)

- Existing page: `concepts/harness-engineering.md` (508 lines, production-focused)
- Action: Added ~60-line RSI section covering design patterns, optimization progression, self-improving harnesses, evolutionary search, auto-research, open challenges
- Did NOT create: `alphaevolve.md`, `self-harness.md`, `darwin-godel-machine.md`, `stop.md`, etc.
- Updated: `entities/lilian-weng.md` (timeline, themes, sources, related concepts)

## Pitfalls

- **Tag taxonomy**: Always verify new tags exist in SCHEMA.md before committing. Use `grep "tag-name" wiki/SCHEMA.md`. The pre-commit hook blocks unknown tags — `auto-research` is NOT canonical (use `autoresearch`).
- **Section placement**: Add new sections before `## References` or `## Related Concepts`, not at the very end of the file.
- **Frontmatter discipline**: Always bump `updated` date and add the raw article to `sources` on every touched page.
- **Rich page protection**: If the existing concept page is >40 lines, use `patch` to add sections, never `write_file` to overwrite.
- **One commit, not N**: Commit all related changes together so the atomicity reflects the conceptual unit.
