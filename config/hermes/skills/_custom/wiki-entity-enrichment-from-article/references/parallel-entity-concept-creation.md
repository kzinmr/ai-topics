# Parallel Entity + Concept Page Creation via delegate_task

When ingesting 2+ source articles that generate multiple entity pages AND multiple concept pages, use **parallel `delegate_task` subagents** to avoid sequential processing and context bloat.

## When to Use

- 2+ raw articles saved (e.g., X article + YouTube podcast transcript on same topic)
- Expected output: 3+ entity pages AND 2+ concept pages
- Both subagents can work independently from the same source files

## Pattern

### Subagent 1: Entity Pages
Creates all entity pages (`entities/name.md`) for people, companies, and organizations mentioned across the sources.

```text
Goal: Create wiki entity pages for these N people/orgs:
- entities/person-a.md
- entities/person-b.md
- entities/company-c.md

Source articles:
- raw/articles/YYYY-MM-DD_source_slug.md
- raw/articles/YYYY-MM-DD_source_slug2.md

Read both source articles and SCHEMA.md first. Create each entity page with full YAML frontmatter.
Use ONLY tags from the SCHEMA.md taxonomy. Each page must have 2+ wikilinks.
```

### Subagent 2: Concept Pages
Creates all concept pages (`concepts/topic.md`) covering frameworks, patterns, and insights from the sources.

```text
Goal: Create wiki concept pages for these N topics:
- concepts/topic-a.md
- concepts/topic-b.md

Source articles:
- raw/articles/YYYY-MM-DD_source_slug.md
- raw/articles/YYYY-MM-DD_source_slug2.md

Read both source articles and SCHEMA.md first. Create each concept page with full YAML frontmatter.
Use ONLY tags from the SCHEMA.md taxonomy. Each page must have 2+ wikilinks.
```

### Context Field Must-Haves
```
Working directory: /opt/data/wiki.
Source articles at raw/articles/.
SCHEMA.md at /opt/data/wiki/SCHEMA.md.
Use write_file to create pages.
All paths must be under /opt/data/wiki/.
Do NOT write to /opt/data/home/wiki/.
```

## Why This Works

- **No context pollution**: Each subagent has its own context window. The parent doesn't see intermediate tool outputs.
- **Parallel execution**: `max_concurrent_children=3` allows both to run simultaneously.
- **Independent work**: Entity and concept pages have zero coordination dependency — they just need the same source articles.
- **Subagents handle tag compliance**: They read SCHEMA.md and add missing tags before using them.

## Post-Subagent Verification

After subagents complete:
1. Verify created files exist: `search_files` on `entities/` and `concepts/` for today's date
2. Spot-check frontmatter on 1-2 pages from each subagent
3. Verify `index.md` and `log.md` were updated by subagents
4. Run `git add wiki/ && git commit` — pre-commit hook validates tags

## Time Savings

| Approach | Time |
|----------|------|
| Sequential (single agent, 6 pages) | ~15-20 min |
| Parallel subagents (3+3 pages each) | ~8-10 min |

## Pitfalls

- **Subagent race on SCHEMA.md**: Both may try to add new tags simultaneously. The `patch` tool handles merge conflicts well, but verify SCHEMA.md after both complete.
- **Wikilink cross-references**: Entity subagent may link to concepts that don't exist yet, and vice versa. This is fine — wikilinks are loose references, not hard constraints. They'll resolve when both pages exist.
- **don't forget the context field**: Subagents default to their own working directory. Always include path instructions.
