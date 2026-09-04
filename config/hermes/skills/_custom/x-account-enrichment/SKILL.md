---
name: x-account-enrichment
description: Enrich skeleton X/Twitter account entity pages to full quality (8-15KB), matching antirez-com.md / simon-willison.md depth.
category: wiki
---

# X Account Enrichment

Enrich skeleton entity pages for X/Twitter accounts tracked in `~/x-accounts.yaml`.

## Workflow

> **⚠️ CRITICAL: Git History Check First**
> Before enriching ANY page, check if a richer version exists in git history. Use `bash config/hermes/skills/wiki/wiki-entity-enrichment-from-article/references/find-richest-version.sh wiki/entities/<handle>.md 3`. If the richest version has >50 more lines than current, restore it first, then enrich on top. See `wiki-entity-enrichment-from-article` → `references/pre-write-verification.md` → "Git History Enrichment" for the full pattern.

1. **Audit current state:**
   ```bash
   python3 -c "
   import os, yaml
   with open(os.path.expanduser('~/x-accounts.yaml')) as f:
       accounts = [a['handle'].lstrip('@') for a in yaml.safe_load(f)['accounts']]
   entity_dir = os.path.expanduser('~/wiki/entities')
   for handle in accounts:
       path = os.path.join(entity_dir, f'{handle}.md')
       if os.path.exists(path):
           with open(path) as f: content = f.read()
           skeleton = 'status: skeleton' in content
           enriched = 'Core Ideas' in content
           print(f'  {handle}: skeleton={skeleton}, enriched={enriched}')
       else:
           print(f'  {handle}: MISSING')
   "
   ```

2. **Prioritize by tiers:**
   - Tier 1: High-impact AI researchers, open-source leaders, known bloggers
   - Tier 2: ML engineers, startup founders, educators
   - Tier 3: Contributors, emerging voices

## Batch process 2 per subagent (4 parallel max):
   - Split entities across 4 parallel subagents, 2 per subagent
   - Provide exact filenames in the goal (absolute paths: `/home/exedev/wiki/entities/{name}.md`)
   - Include the format template in the prompt
   - 8 entities processed this way = ~6 minutes total (vs 15+ minutes sequential)

4. **Post-batch verification:**
   ```bash
   # Check file sizes
   ls -la ~/wiki/entities/*.md | sort -k5 -n -r | head -30
   
   # Find remaining skeletons
   grep -l 'status: skeleton' ~/wiki/entities/*.md
   
   # Find duplicates (skeleton + enriched for same person)
   # Common pattern: full-name-slug.md vs handle.md
   ```

5. **Cleanup duplicates:**
   ```bash
   # Delete skeleton duplicates after confirming enriched version exists
   rm ~/wiki/entities/ethan-mollick.md      # → emollick.md
   rm ~/wiki/entities/chip-huyen.md          # → chipro.md
   rm ~/wiki/entities/lilian-weng.md         # → lilianweng.md
   rm ~/wiki/entities/eugene-yan.md          # → eugeneyan.md
   rm ~/wiki/entities/samuel-colvin.md       # → samuelcolvin.md (also empty)
   rm ~/wiki/entities/benjamin-clavi.md      # → bclavie.md
   rm ~/wiki/entities/cl-mentine-fourrier.md # → clefourrier.md
   rm ~/wiki/entities/late-interaction.md    # concept, not person
   ```

6. **Commit and push:**
   ```bash
   cd ~/ai-topics && git add wiki/ && git commit -m "wiki: enrich X accounts (batch N)" && git push
   ```

## Enrichment Format Template

```yaml
---
title: "Full Name"
handle: "@twitter_handle"
created: 2026-04-10
updated: 2026-04-10
tags: [person, topic1, topic2]
aliases: ["handle", "alt-name"]
---

# Full Name (@handle)

| | |
|---|---|
| **X** | [@handle](https://x.com/handle) |
| **Blog** | [URL](URL) |
| **GitHub** | [username](https://github.com/username) |
| **Role** | Job title |
| **Known for** | Key contributions |
| **Bio** | 2-3 sentence background |

## Overview

2-3 paragraph introduction of who they are, their background, and why they matter in AI.

## Core Ideas

Their key viewpoints, theories, and opinions on LLM/AI Agent technologies. Use subsections for each major theme. Quote their actual posts/articles where possible.

## Key Work

- Project/tool/library they created
- Papers published
- Notable blog posts
- Talks and presentations

## Blog / Recent Posts

Key articles they've written with dates and summaries.

## Related People

Connections to other wiki entities.

## X Activity Themes

What they tweet about most frequently.
```

## Quality Targets

- **Size**: 8-15KB per page minimum
- **Content**: Actual quotes, specific examples, real blog post links
- **Sections**: Core Ideas (with subsections), Key Work, Blog/Recent Posts, Related People, X Activity Themes
- **Frontmatter**: No `status: skeleton` tag
- **Cross-references**: Link to other wiki entities using `[[entity-name]]` format

## Related References

- `references/scan-naming-conventions.md` — Filename conventions for scan-sourced pages
- `references/tweet-content-extraction.md` — Extracting full content from tweets
- `references/x-accounts-scan-json-structure.md` — JSON structure of `x_accounts_latest_full.json`
- `references/x-scan-discord-report-template.md` — Japanese Discord report format template for x-accounts-scan cron job

## Known Subagent Pitfalls

1. **Filename aliasing**: Subagents create files with different names than specified (e.g., `hynek-schlawack.md` instead of `hynek.md`). Always audit post-batch for duplicates.

2. **Budget exhaustion**: 50-iteration budget per subagent. When processing 5 entities, subagent may hit limit and skip writing some files. Check `exit_reason: max_iterations` in results.

3. **Path discipline**: delegate_task subagents must always target `~/wiki/entities/`. If a delegated context shows `~/.hermes/home/...`, treat it as a runtime artifact and keep writing to the canonical wiki path only.

4. **Status cleanup needed**: Even when subagents write content successfully, `status: skeleton` in frontmatter is often NOT removed. Always verify and manually replace with `status: complete` if needed.

5. **Successful pattern confirmed (2026-04-10)**: 8 entities enriched in 4 parallel batches of 2 each, completed in ~6 minutes with file sizes 12.5-18.7KB (exceeding 8-15KB target). This confirms the 2-per-subagent batching strategy works well.

6. **Handle ≠ filename during scan ingest**: When processing scan results, the X handle (e.g., `dbreunig`) often does NOT match the entity page filename (e.g., `drew-breunig.md`). Always search for the entity page by content/grep before concluding it's MISSING:
   ```bash
   grep -rl 'dbreunig' ~/wiki/entities/ 2>/dev/null
   ```

## Research Strategy

For each person:
1. Search X/Twitter for their recent activity and key opinions
2. Check their blog/personal site for articles
3. Look up GitHub repositories they've created
4. Find interviews, talks, or presentations
5. Search for mentions in AI community discussions
6. Cross-reference with other wiki entities for related connections

## x-accounts Scan → Wiki Ingest (different workflow)

This skill covers **enriching skeleton entity pages** for tracked X accounts. A separate workflow exists for **processing new posts from x-accounts scans** into wiki pages (creating concept pages from shared links, updating entity pages with new blog posts, etc.).

For the scan→ingest workflow, see `wiki-ingestion-pipelines` → `references/x-accounts-scan-ingest-workflow.md`.

**Key distinction**:
- **This skill**: Take a `status: skeleton` entity page → research the person → write 8-15KB full page
- **Scan ingest**: Take `new_posts` from `x_accounts_latest_full.json` → evaluate each post's external URLs → create concept pages or update existing entity pages

**Post evaluation quick reference**:
| Signal | Action |
|--------|--------|
| Reply without standalone value | Skip |
| Multiple replies from same account forming coherent thread (same topic, consecutive timestamps) | Evaluate as group — may have standalone value together |
| Non-AI domain link | Skip |
| Link to own blog post (entity exists) | Update entity's Blog/Recent Posts |
| arXiv paper (no existing page) | Create concept page |
| Official docs link | Add to relevant entity sources |
| Conference appearance | Add to entity's Speaking Engagements |
