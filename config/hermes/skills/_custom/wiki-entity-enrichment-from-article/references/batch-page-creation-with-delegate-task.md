# Batch Wiki Page Creation with delegate_task

When creating 5+ concept pages from a structured source (e.g., a hub page linking to 20 individual documents), use parallel delegate_task subagents to fetch and create pages simultaneously.

## Pattern

### 1. Define the Batch

Group pages into batches of 3-5 (delegate_task limit per user). Each batch runs as parallel subagents.

```python
delegate_task(tasks=[
    {"goal": "Create wiki concept page for X. Fetch URL, extract content, write to ~/wiki/concepts/gpt/gpt-x-system-card.md. Include frontmatter with tags from SCHEMA.md. DO NOT modify index.md or log.md.", "toolsets": ["web", "browser", "file", "terminal"]},
    {"goal": "Create wiki concept page for Y...", "toolsets": ["web", "browser", "file", "terminal"]},
    {"goal": "Create wiki concept page for Z...", "toolsets": ["web", "browser", "file", "terminal"]},
])
```

### 2. Critical: Tell Subagents NOT to Touch index.md/log.md

Subagents running in parallel will create merge conflicts if they all try to update index.md. Explicitly instruct:
- "DO NOT modify index.md or log.md"
- Each subagent only creates its assigned page file(s)

### 3. Consolidate After All Batches Complete

After all batches finish, update index.md, log.md, and hub pages in a single pass:
- Add all new entries to index.md at the correct alphabetical position
- Update hub/MOC pages with links to all new pages
- Append to log.md
- Commit and push

## Subagent Goal Template

```
Create a wiki concept page for {NAME}. Write the file to ~/wiki/concepts/{dir}/{slug}.md

Use this frontmatter:
---
title: {FULL TITLE}
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [tag1, tag2, ...]
sources: [URL]
---

Key facts to include:
- {bullet points of key data}
- Include tables where appropriate
- Add [[wikilinks]] to related pages
- Make it ~{N} lines

DO NOT modify index.md or log.md.
```

## Pitfalls

- **Subagent save path**: Subagents default to the session working directory. Always specify absolute paths (`~/wiki/concepts/...`) in the goal.
- **Tag violations**: Subagents may invent tags not in SCHEMA.md. Pre-specify valid tags in the goal or include "tags must be from SCHEMA.md taxonomy" in instructions.
- **Subagent timeout**: Large pages from complex sites may timeout. If a batch of 3 times out, retry individual pages as separate subagents.
- **Content quality**: Subagent-extracted content varies. Review key pages after creation; fix obvious errors before committing.
- **Hub page updates**: Don't let subagents update hub pages either — they'll conflict. Do hub updates in the consolidation pass.
