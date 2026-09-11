# Skill Sync Pitfalls — Library Management

## Pitfall: Deleting repo-only skills breaks cron jobs

When syncing `~/.hermes/skills/` to `ai-topics/config/hermes/skills/`, a naive approach of "delete files that only exist in repo" will break cron jobs that reference skills loaded via `external_dirs`.

### Root cause
`config.yaml` has `external_dirs: ~/ai-topics/config/hermes/skills`. Skills that exist **only** in the repo (not in `~/.hermes/skills/`) are still loaded by Hermes and referenced by cron jobs.

### Safe sync procedure
1. **Before deleting**, check cron jobs for skill references:
   ```python
   # Extract all skills from ~/.hermes/cron/jobs.json
   with open('~/.hermes/cron/jobs.json') as f:
       data = json.load(f)
   cron_skills = set()
   for j in data['jobs']:
       for s in j.get('skills', []): cron_skills.add(s)
       if j.get('skill'): cron_skills.add(j['skill'])
   ```
2. **Categorize** repo-only files:
   - Referenced by cron jobs → **KEEP** (e.g., wiki-ingestion-pipelines, wiki-entity-enrichment-from-article, semantic-article-grouping, blogwatcher-db)
   - System-specific (not Hermes-bundled) → **KEEP** unless explicitly deprecated
   - Hermes-bundled duplicates → safe to remove from repo
3. **Never mass-delete** repo-only files. Always filter first.

### Skills that MUST exist in repo (cron-referenced, as of 2026-06)
- `wiki/wiki-ingestion-pipelines` — x-bookmarks-ingest
- `wiki/wiki-entity-enrichment-from-article` — x-bookmarks-ingest, skeleton-enrich-daily, raw-backlog-ingest
- `research/semantic-article-grouping` — blog-triage, newsletter-triage, raw-backlog-ingest
- `research/blogwatcher-db` — referenced by blogwatcher jobs

## Pitfall: Archiving vs deleting

Use `.archive/` directory (in ~/.hermes/skills/) to disable skills without losing them. For repo skills, use `git rm` only after confirming no cron dependencies. Git history allows recovery but is slower.

## Skill naming convention

Hermes-bundled skills use `category/skill-name` paths. System-specific skills should also follow this convention. Avoid top-level skills without category unless they are genuinely cross-cutting (e.g., `dogfood`).
