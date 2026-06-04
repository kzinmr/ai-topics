# Cheat at Search Lecture Transcript Ingestion Pattern

When ingesting a Doug Turnbull "Cheat at Search" Maven course lecture transcript, follow this cross-referencing cascade.

## File Naming

```
wiki/raw/transcripts/YYYY-MM-DD_softwaredoug_cheat-at-search-<topic-slug>-lecture.md
```

Existing transcripts follow this pattern:
- `2026-05-20_softwaredoug_cheat-at-search-llm-query-understanding-lecture.md`
- `2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents-lecture.md`
- `2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture.md`
- `2026-06-02_softwaredoug_cheat-at-search-long-running-search-lecture.md`
- `2026-06-04_softwaredoug_cheat-at-search-coding-agents-lecture.md`

## Cross-Referencing Cascade (4 pages minimum)

### 1. Entity page: `wiki/entities/doug-turnbull.md`
Add a wikilink under the "Cheat at Search (Maven Course)" section → "#### Lecture Transcripts (wiki)" subsection.
Format: `[[raw/transcripts/YYYY-MM-DD_...|Lesson N: Topic]]`

### 2. Concept pages mentioned in the lecture
Add the transcript path to the `sources:` frontmatter array of each relevant concept page.
Common patterns:
- RLM-related → `wiki/concepts/rlm-recursive-language-models.md`
- Auto-research → `wiki/concepts/karpathy-loop.md`, `wiki/concepts/pi-autoresearch.md`
- Agentic search → `wiki/concepts/agentic-search.md`

### 3. Slides article (if exists)
The companion slides article is usually at `wiki/raw/articles/YYYY-MM-DD_softwaredoug_search-with-agents-lessonN-<topic>.md`.
Add `related_transcript: raw/transcripts/YYYY-MM-DD_...` to its frontmatter.

### 4. Prior lectures
Add cross-references to prior lecture transcripts in the transcript's own frontmatter body (markdown links).

## Frontmatter Template

```yaml
---
title: "Cheat at Search — <Topic> (Lecture Transcript)"
author: Doug Turnbull (@softwaredoug)
date: YYYY-MM-DD
date_ingested: YYYY-MM-DD
related_article: articles/YYYY-MM-DD_softwaredoug_search-with-agents-lessonN-<topic>
type: transcript
tags:
  - agentic-search
  - <topic-specific-tags>
---
```

## Pitfall: Pre-commit Tag Validation on Staged Files

The pre-commit hook validates ALL staged files, not just the ones you changed.
If you `git add` an entity page (e.g., doug-turnbull.md) and that page has pre-existing
tags not in SCHEMA.md taxonomy, your commit will be blocked even though you didn't touch those tags.

**Fix**: Check tags on all staged files before committing. If blocked:
1. Read the error message — it lists the exact files and tags
2. Add the missing tags to `wiki/SCHEMA.md` under the appropriate category
3. `git add wiki/SCHEMA.md` and recommit

Common tags missing from SCHEMA.md that appear on older entity pages: `developer`, `relevance`, `author`, `consultant`.

## Pitfall: Shell Heredoc with `&`

When using `terminal()` with heredoc (`cat >> file << 'EOF'`), the `&` character gets
interpreted as shell backgrounding. Use `echo` chains or `write_file` instead.
