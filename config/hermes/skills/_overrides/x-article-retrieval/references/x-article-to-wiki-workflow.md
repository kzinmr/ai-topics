# X Article → Wiki Integration Workflow

End-to-end workflow for ingesting an X Article or Note Tweet into the wiki knowledge base. The main SKILL.md covers retrieval; this covers what happens after you have the content.

## Prerequisites
- `xurl` CLI on PATH
- `raw-article-filename-policy` skill for naming
- `wiki-entity-enrichment-from-article` skill for page creation/enrichment

## Step-by-Step

### 1. Retrieve Tweet Metadata
```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=note_tweet,created_at,author_id,public_metrics,entities&expansions=author_id&user.fields=name,username,description"
```
- Check response: does it have `article.title`? → X Article. Does it have `note_tweet.text`? → Note Tweet.
- Extract: `created_at`, `author_id`, author `username`/`name`, `public_metrics` (bookmark_count is a quality signal).

### 2. Fetch Full Content
- **X Article**: Separate call `xurl "/2/tweets/<TWEET_ID>?tweet.fields=article"` → `article.plain_text`
- **Note Tweet**: Already inline in step 1's `note_tweet.text`. Apply `strip_mathematical()` if needed.

### 3. Save Raw Article
Filename: `YYYY-MM-DD_{handle-without-at}_{short-slug}.md`

```
---
title: "<article title>"
author: <name> (@<handle>)
date: <created_at YYYY-MM-DD>
type: x_article          # or x_note_tweet
source_url: https://x.com/<handle>/status/<TWEET_ID>
article_url: https://x.com/i/article/<ARTICLE_ID>   # X Articles only
ingested: <today>
tags: [relevant, tags, from, SCHEMA]
---

# <Title>

<Full article text, cleaned of invisible unicode>
```

### 4. Check Existing Wiki Pages (BEFORE creating any new page)
Before creating new pages, search:
- `search_files` for author handle/name in `wiki/entities/`
- `search_files` for key concepts in `wiki/concepts/` and `wiki/entities/`
- **If `search_files` returns 0 results for a concept you KNOW should exist** — cross-check `wiki/index.md` directly. GPT model pages live in `concepts/gpt/`, OpenAI system cards in `concepts/gpt/`, and other topics may be nested in subdirectories that `search_files` can miss (path/glob edge cases).
- If the article is by/about an existing entity → update that entity page
- If it introduces a new concept → consider a concept page
- **Never create a duplicate page** — if index.md lists a matching page, read and update it instead

### 5. Update Entity/Concept Pages
For existing entity pages (most common pattern):
- **Do NOT overwrite** rich pages (>40 lines). Use `patch` to add a new section.
- Add a `##` section with date and source attribution
- Include a blockquote source reference at section top
- Update frontmatter: `updated`, `sources` (add raw article path), `tags` if new tags apply
- Add `[[wikilinks]]` to related pages (minimum 2 external wikilinks)

### 6. Update Index & Log
- `wiki/index.md`: Update the entity's entry in the recently-updated section
- `wiki/log.md`: Append entry with created/updated files and summary

### 7. Commit & Push
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: <summary>" && git push
```

## Pitfalls
- **Don't mix note_tweet and article in tweet.fields** — see main SKILL.md
- **Don't use today's date for raw article filename** — use `created_at` from the API
- **X Article plain_text may contain invisible unicode** (U+200B, U+200C, U+FEFF) — strip before saving if the content will be used in cron jobs
- **Author may not have an entity page yet** — search before assuming. Create a skeleton if the person is notable (OpenAI/Codex team, well-known AI practitioner)
- **Bookmark count >500 = high-quality signal** — prioritize these for richer wiki treatment
- **`search_files` may miss nested pages** — `concepts/gpt/`, `concepts/openclaw/`, and other subdirectories can return 0 on `search_files` even when matching files exist. Always cross-check `wiki/index.md` for the topic keyword before creating a new concept page. Caught in session: nearly duplicated `concepts/gpt/gpt-5-6.md` (209-line rich page) because `search_files(pattern="gpt-5-6")` returned 0.
- **Tag taxonomy violations block commits** — The pre-commit hook validates all tags against `wiki/SCHEMA.md`. Common mistakes: `reasoning-models` (not valid) → `reasoning-model` (valid); `api-abuse` (not valid) → `vulnerability` or `security` (valid). **Always check SCHEMA.md tag taxonomy before setting frontmatter tags.** The error message lists valid alternatives — read it and fix, don't retry blindly. Run `grep -i "<tag>" wiki/SCHEMA.md` to verify before committing.
- **Japanese in log.md blocks commits** — The pre-commit hook enforces English-only for all non-`raw/` wiki content. When the user communicates in Japanese, it's tempting to write the log header in Japanese (e.g. `## [2026-08-12] X Article取込: ...`). The hook catches this: `BLOCKED: Japanese content introduced to previously clean files`. **Always write log.md entries in English**, regardless of the conversation language. Fix: `patch` the header to English, re-stage, re-commit.
