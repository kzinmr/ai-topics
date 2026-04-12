---
name: wiki-entity-upgrade
description: Upgrade bio-only blogger entity pages to comprehensive thought analysis format
category: wiki
---

# Wiki Entity Page Upgrade

Upgrade bio-only entity pages to comprehensive thought analysis format following mitchellh-com.md as reference.

## Workflow

1. Read existing bio-only entity page in ~/wiki/entities/
2. Scrape author's blog (homepage + 3-5 recent articles)
3. Extract core ideas, philosophy, key quotes, recent themes
4. Write upgraded page following the format below
5. Update wiki/index.md and wiki/log.md
6. Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: upgrade <slug> to thought analysis" && git push`

## Page Format

```yaml
---
title: "Author Name"
type: entity
url: "blog.example.com"
category: blog-author
tags: [topic1, topic2]
---

| Field | Value |
|-------|-------|
| Name | Author Name |
| URL | blog.example.com |
| Known For | Key achievement |
| Themes | Primary writing topics |

## Overview
Brief biographical context + writing philosophy (2-3 paragraphs)

## Timeline
| Year | Milestone |
|------|-----------|

## Core Ideas
### Idea 1 Name
Analysis + supporting evidence from their writing

### Idea 2 Name
Analysis + supporting evidence

## Key Quotes
- "Notable quote 1" — [Source](url)
- "Notable quote 2" — [Source](url)

## Recent Themes (2024–2026)
- Theme 1 with explanation
- Theme 2 with explanation

## Related
- [[entities/related-author]] — connection explanation

## Sources
- URL 1
- URL 2
```

## Progress Tracking

After each batch, run this audit to separate completed vs remaining:

```python
import os
target = os.path.expanduser("~/wiki/entities/")
skip = {'agibot-10000-units', 'amazon-rivr', 'anthropic', 'claude-mythos', 'cursor-3',
        'gemma-4', 'glm-5-zai', 'glm-5v-turbo', 'meta', 'mistral-voxtral-tts',
        'muse-spark', 'openai-spud', 'qwen3-6-plus', 'zoox-expansion'}
bio_only, has_analysis = [], []
for f in sorted(os.listdir(target)):
    if not f.endswith('.md') or f.replace('.md','') in skip: continue
    with open(os.path.join(target, f)) as fh: content = fh.read()
    if "## Core Ideas" in content or "## Key Themes" in content:
        has_analysis.append(f)
    else:
        bio_only.append(f)
print(f"✅ Done: {len(has_analysis)}, 📋 Remaining: {len(bio_only)}")
for b in bio_only: print(f"  - {b}")
```

## Batch Processing Strategy

- **Budget awareness**: delegate_task has ~50 iteration budget per subagent. A batch of 5 entities can exhaust it, leaving some files unwritten. Always verify post-batch.
- Group by similar domains (AI researchers, security experts, infrastructure devs, etc.)
- Process 3-5 entities per subagent task using delegate_task
- Use 2-3 parallel subagent tasks per batch (don't exceed 4 — budget compounds)
- After each batch: audit → copy from wrong dir → commit → push → next batch
- For the final ~10 entities: consider running sequentially or in 2 parallel tasks to ensure completion
- Non-entity pages (companies, models, products) use different formats — skip them
- Target: ~69 blogger entities total (OPML has 84 feeds, but 14 are concepts/products)

## Critical Pitfalls

- **Subagent write_file path bug**: delegate_task subagents write files to `~/.hermes/hermes-agent/wiki/entities/` instead of the correct `~/wiki/entities/`. After subagent completion, ALWAYS check the wrong directory and copy upgraded files:
  ```bash
  cp ~/.hermes/hermes-agent/wiki/entities/*.md ~/wiki/entities/
  ```
- **Subagent filename aliasing**: Even when given exact filenames, subagents create files with DIFFERENT names (e.g., `benjamin-clavi.md` instead of `bclavie.md`, `ethan-mollick.md` instead of `emollick.md`, `hynek-schlawack.md` instead of `hynek.md`). After each batch:
  1. Check all new files: `ls -la ~/wiki/entities/*.md` (sort by time)
  2. Look for skeleton duplicates: files with `status: skeleton` in frontmatter
  3. Delete skeleton duplicates after confirming enriched version exists
  4. Common pattern: full-name-slug.md vs handle.md — both exist for same person
- **Subagent budget exhaustion**: Each delegate_task subagent has ~50 iteration budget. When processing 5+ entities, the subagent may hit the limit and complete without writing all files. ALWAYS verify:
  1. Check subagent summary for which files were actually written vs just researched
  2. If `exit_reason: max_iterations`, some files may be missing
  3. Run the progress tracking audit immediately after each batch
- **Non-entity page confusion**: OPML has 84 feeds but only ~69 are blogger entities. The rest are companies, products, or concepts. Use the skip set in progress tracking to avoid wasting time on these.
- **Hillel Wayne newsletter duplication**: Hillel Wayne has both `hillel-wayne.md` and `buttondown-com-hillelwayne.md`. The newsletter version should cross-reference the main page, not duplicate all content.

## X Account Enrichment Workflow

For X/Twitter accounts (from `~/x-accounts.yaml`), the enrichment process is similar but with format differences:

### X Account Page Format
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
## Core Ideas
## Key Work
## Blog / Recent Posts
## Related People
## X Activity Themes
```

### X Account Enrichment Steps
1. Check `~/x-accounts.yaml` for account list
2. Run `~/scripts/build_x_wiki.py` to create skeleton pages (if not already done)
3. Prioritize by importance: high-impact AI figures first
4. Batch process 5 accounts per delegate_task subagent
5. Use 3 parallel subagents per batch (don't exceed 4 — budget compounds)
6. After each batch: audit → cleanup duplicates → commit → push → next batch
7. Target quality: 8-15KB per page, matching `antirez-com.md` or `simon-willison.md` depth

### Known Duplicate Patterns (X Accounts)
- `benjamin-clavi.md` → keep `bclavie.md`
- `chip-huyen.md` → keep `chipro.md`
- `ethan-mollick.md` → keep `emollick.md`
- `eugene-yan.md` → keep `eugeneyan.md`
- `hynek-schlawack.md` → keep `hynek.md` (or vice versa, check which is enriched)
- `lilian-weng.md` → keep `lilianweng.md`
- `samuel-colvin.md` → keep `samuelcolvin.md`
- `peter-steinberger.md` → keep if enriched (no alternate)
- `karri-saarinen.md` → keep if enriched (no alternate)
- `daniel-han.md` → keep if enriched (no alternate)
- `cl-mentine-fourrier.md` → keep `clefourrier.md`
- `late-interaction.md` → concept page, not person (delete if in entities/)