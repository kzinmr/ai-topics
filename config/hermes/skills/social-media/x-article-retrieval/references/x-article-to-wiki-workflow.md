# X Article to Wiki — Verified End-to-End Workflow

Complete workflow for ingesting an X Article into the wiki. Validated 2026-06-02 with article 2061850535708483585.

## Step 1: Fetch Article Body + Metadata (2 API calls)

```bash
# Call 1: Article body (plain_text, title, entities)
xurl --auth oauth2 "/2/tweets/<TWEET_ID>?tweet.fields=article"

# Call 2: Metadata (created_at, author_id) — SEPARATE call due to field incompatibility
xurl --auth oauth2 "/2/tweets/<TWEET_ID>?tweet.fields=created_at,author_id"
```

**Why two calls**: `note_tweet` and `article` fields cannot be mixed. `created_at` is not returned when `article` is requested (inconsistent behavior). Always make separate calls.

## Step 2: Fetch Author Info (optional but recommended for entity pages)

```bash
xurl --auth oauth2 "/2/users/<AUTHOR_ID>?user.fields=name,username,description,created_at"
```

## Step 3: Determine Filename

Follow `raw-article-filename-policy`:
- Pattern: `{YYYY-MM-DD}_{handle-no-at}_{content-slug}.md`
- Date = `created_at` from API (not today)
- Handle = X username without `@`, underscores stripped
- Example: `2026-06-02_trq212_dynamic-workflows-claude-code.md`

## Step 4: Create Raw Article

Save to `wiki/raw/articles/`. Frontmatter:
```yaml
---
title: "<article.title>"
author: <name> (@<handle>)
date: <created_at YYYY-MM-DD>
source: https://x.com/<handle>/status/<tweet_id>
source_type: x_article
url: https://x.com/i/article/<article_id>
tweet_id: "<tweet_id>"
article_id: "<article_id>"
author_id: "<author_id>"
---
```

Body = full `article.plain_text` from API response.

## Step 5: Create/Update Wiki Pages

From the article content, create:
1. **Concept page** (`wiki/concepts/`) — structured synthesis with patterns, use cases, comparisons. Must have ≥2 wikilinks.
2. **Entity page** (`wiki/entities/`) for the author — if not already existing. Mark `status: skeleton` if limited info.
3. **Update existing pages** — if the article extends an existing concept, update that page instead of creating new.

## Step 6: Update index.md + log.md

- Add new entity entries alphabetically in the Entities section
- Update/create concept entries in the Concepts section
- Append log entry to `wiki/log.md` with files created/updated and source URL

## Step 7: Commit + Push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push
```

## End-to-End Wiki Ingestion

See `references/x-article-to-wiki-workflow.md` for the full verified workflow: API fetch → raw article → concept page → entity page → index/log update → commit.

## Pitfalls

- **Mixing `note_tweet` + `article` in tweet.fields → silent data loss**
- **Field incompatibility**: Never combine `note_tweet` and `article` in one `tweet.fields` request. Always separate.
- **Entity page linking**: Even skeleton entity pages must have ≥2 outbound wikilinks. Link to the employer entity, the concept page, and any related concepts.
- **Tag validation**: All tags must exist in `SCHEMA.md` taxonomy. Pre-commit hook blocks unknown tags.
