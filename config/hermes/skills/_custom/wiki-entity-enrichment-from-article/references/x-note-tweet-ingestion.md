# X/Twitter Note Tweet → Wiki Ingestion Workflow

> End-to-end workflow for ingesting a single X/Twitter post (Note Tweet) into the wiki.
> Bridges `x-article-retrieval` skill (fetch mechanics) with wiki page creation.

## Trigger

User provides an X/Twitter URL like `https://x.com/username/status/TWEET_ID` and says "wikiに取り込んで" or equivalent.

## Step-by-Step

### 1. Extract Tweet ID from URL

Regex: `x\.com/.+/status/(\d+)` → capture group 1 is the tweet ID.

### 2. Fetch Basic Tweet + Metadata

```bash
xurl read <TWEET_ID>
```

Check if `text` is truncated (ends with `...` or `https://t.co/`). If so, it's likely a Note Tweet.

### 3. Fetch Full Note Tweet Content

```bash
xurl "/2/tweets/<TWEET_ID>?tweet.fields=note_tweet,created_at,author_id"
```

- `note_tweet.text` contains the full untruncated text
- `created_at` for the raw article date
- `author_id` for cross-referencing

**Pitfall**: Do NOT mix `note_tweet` and `article` in the same `tweet.fields` — `article.plain_text` is silently dropped. Use separate requests for each. (See `x-article-retrieval` skill.)

### 4. Fetch Author Info (if new entity)

```bash
xurl user @<username>
```

Get: `name`, `username`, `description` (bio), `public_metrics.followers_count`, `id`.

### 5. Save Raw Article

Path: `wiki/raw/articles/YYYY-MM-DD_<username>-<short-slug>.md`

Frontmatter:
```yaml
---
title: "Author Name on Topic"
author: Name (@username)
date: YYYY-MM-DD
source_url: https://x.com/username/status/TWEET_ID
type: x-note-tweet
tags: [relevant, tags, from-schema]
---
```

Body: Full tweet text verbatim. Include engagement metrics (likes, bookmarks, impressions) if notable.

**Pitfall**: Tags in raw/ frontmatter are informational — the pre-commit hook only validates `wiki/entities/`, `wiki/concepts/`, etc. But use SCHEMA-compliant tags anyway for consistency.

### 6. Check for Existing Entity Pages

```bash
search_files(pattern="username|Author Name", path="wiki/entities/")
```

If exists → update it with a new section referencing this post.
If not → create new entity page.

### 7. Create/Update Entity Page

For new person entities:
- Research the author (bio, affiliations, follower count, notable work)
- Structure: overview, key perspectives (from this tweet), related links
- Minimum 2 outbound `[[wikilinks]]` — link to existing concept/entity pages mentioned in the tweet

**Quality target**: Match depth of `entities/alex-cheema.md` or better. Include specific technical claims from the tweet, not just a summary.

### 8. Update Related Pages

If the tweet discusses an existing entity/concept (e.g., NVIDIA DGX Spark):
- Add a perspective section or quote to that page
- Update `sources:` and `updated:` in frontmatter
- Add cross-reference back to the new entity page

### 9. Update index.md and log.md

- Insert entity entry alphabetically in `index.md`
- Append log entry to `log.md`

### 10. Commit and Push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest Author topic summary (X post #TWEET_ID)" && git push
```

If tag violation → remove offending tag or add to SCHEMA.md, retry.

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Truncated tweet text | Always fetch with `tweet.fields=note_tweet` — `xurl read` returns truncated text |
| `exolabs`-style org tags not in SCHEMA | Don't include org names as tags unless they're in the taxonomy. Use broader tags like `ai-researcher`, `founder` |
| Missing wikilinks | Before writing entity page, search for related pages to link to |
| Alphabetical index insertion | Match exact surrounding lines for unique patch context |
| Log.md `|` prefix typo | `# Wiki Log` not `|# Wiki Log` — check patch doesn't introduce stray chars |
| Tags like `scaling-laws`, `pre-training`, `data-curation` | Use `scaling`, `training`, `datasets` instead — see precommit-pitfalls.md |

---

## X Megathread Ingestion (Multi-Tweet Threads)

When the source URL is the **head tweet of a multi-tweet thread** (megathread), the workflow differs from single-note-tweet ingestion. Megathreads typically have 10-60 tweets from the same author, all replying to each other.

### Detection

If `xurl read <TWEET_ID>` shows a short text and the author is known for long-form analysis, check for thread replies before assuming it's a single tweet.

### Step 1: Fetch All Thread Tweets

```bash
xurl search "from:<HANDLE> conversation_id:<HEAD_TWEET_ID>" --max-results 100 > /tmp/thread_raw.json
```

This returns all tweets by the author in the conversation thread. Sort by `created_at`.

**Pitfall**: The search endpoint may return `{}` (empty) if the query format is wrong. Use `from:HANDLE conversation_id:ID` (space-separated, not URL-encoded). The `xurl search` command handles encoding.

### Step 2: Fetch Full Text for Each Tweet

The search results have truncated `text` only. For each tweet ID, fetch the full content:

```python
import subprocess, json
for tid in tweet_ids:
    r = subprocess.run(['xurl', f'/2/tweets/{tid}?tweet.fields=note_tweet,created_at,author_id'],
                       capture_output=True, text=True, timeout=15)
    resp = json.loads(r.stdout)
    td = resp.get('data', {})
    note = td.get('note_tweet', {}).get('text', '')
    text = td.get('text', '')
    full_text = note if note else text
```

**Pitfall**: Fetching `note_tweet` for ALL tweets in the thread is safe — regular tweets just return empty `note_tweet`, falling back to `text`. Don't try to pre-filter which tweets need it.

### Step 3: Assemble Thread into Raw Article

Number each tweet `[1/N]` and concatenate. Save as a single raw article:

```
raw/articles/YYYY-MM-DD_<username>-<short-slug>.md
```

Use `type: x-thread` in frontmatter (not `x-note-tweet`).

### Step 4: Content Extraction Strategy

Megathreads contain a mix of:
- **Core analysis tweets**: The main technical content — these become the concept page
- **Casual replies**: "@user thanks for the catch", "it took me ~4 hours 😭" — include in raw for completeness but exclude from concept page
- **Wrap-up tweets**: "done!", "check out @other's recap" — include as context

### Step 5: Wiki Page Creation

For technical megathreads (e.g., model analysis, architecture deep dives):
- Create a **concept page** for the technical content (not an entity page)
- Update the **author's entity page** with a timeline entry referencing the thread
- If the thread discusses an existing concept/model, add a cross-link to that concept page

### Example (2026-06-03 Elie Bakouch MAI Thread)

- 57 tweets total, ~47 substantive analysis tweets
- Created `concepts/mai-thinking-1-tech-report.md` for the technical content
- Updated `entities/elie-bakouch.md` with timeline entry
- Updated `concepts/microsoft-mai-models.md` with deep-dive cross-link
