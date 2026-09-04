# Daily RSS Triage — Extended Reference

This file was renamed from `daily-rss-triage.md` to `daily-rss-triage-reference.md` to resolve a skill name collision with the standalone `daily-rss-triage` skill. See the original content in the standalone skill at `config/hermes/skills/_custom/daily-rss-triage/SKILL.md`.

## Key Workflow Additions (from 2026-08-08 blog-triage session)

### Cron Mode Limitations
- `execute_code` is **blocked** in cron jobs (no user present to approve)
- Use `search_files(target='files', pattern='entity-name*', path='~/ai-topics/wiki/entities')` for entity existence checks instead
- `search_files` works correctly for specific filename patterns in known directories; it only fails for recursive globs like `**/*.md`

### Triage Priority Pattern
When blog ingest yields 15-20 articles:
1. First pass: delegate subagent to read all articles and score AI relevance (high/medium/low/none)
2. Second pass: check existing wiki pages for duplicates (search_files on entities, concepts, events)
3. Third pass: update existing pages with new information (patch, not write_file)
4. Fourth pass: update log.md and commit

### Article-to-Wiki Mapping
- High-relevance articles → update or create wiki pages immediately
- Medium-relevance → note in log.md, skip page creation unless existing page exists
- Low/none → save raw article only, no wiki action
