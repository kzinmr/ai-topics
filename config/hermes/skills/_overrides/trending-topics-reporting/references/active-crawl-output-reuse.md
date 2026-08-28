# Reusing Active-Crawl Output in Trending-Topics

The `active-crawl` cron job runs at **11:00 UTC**, exactly 1 hour before `trending-topics` (12:00 UTC).
Its output file is a **synthesized research note** that already contains HN Algolia point scores,
X/Twitter engagement data, wiki gap analysis, and candidate topic prioritization.

**Always check this file before running separate HN/X queries.** The active-crawl research note
is richer and faster than running Algolia + xurl from scratch.

## Discovery Command

The active-crawl output follows a predictable naming pattern:

```bash
# Find today's active-crawl research note
find /opt/data/ai-topics/wiki/raw/articles/ -name '*active-crawl*' -mtime -1 2>/dev/null
```

Expected path: `wiki/raw/articles/YYYY-MM-DD_active-crawl-trending-topics-research.md`

## What It Contains (from the YAML frontmatter + sections)

The research note is structured as:

```
---
title: "Active Crawl Trending Topics Research — YYYY-MM-DD"
type: research_note
sources:
  - https://hn.algolia.com/api/v1/search (multiple queries)
  - https://news.ycombinator.com/
  - xurl search (6 queries, x.com/Twitter)
  - blogwatcher DB
tags: [trending-topics, active-crawl, research, wiki-gap-analysis]
---
```

**Key sections to extract:**

### Dominant Theme
A 1-3 sentence summary of the #1 story this week. Example:
> "The #1 story this week: US government will vet who gets GPT-5.6 (1,162 pts)"

### Top HN Stories (table)
Each entry has: **N pts** — Title (Source)
Use the **point scores for your ★ rating**:
- > 400 pts → ★★★★★ candidate
- > 100 pts → ★★★★☆ candidate  
- > 30 pts → ★★★☆☆ candidate
- < 30 pts → lower priority

### Top X/Twitter Topics
Each entry has: `@handle — Title (N bookmarks)`
- > 500 bookmarks → strong community signal
- < 50 bookmarks → weak signal, verify against other sources

### Wiki Gap Analysis
A section listing coverage status. Three buckets:
- **HIGH**: Topics with 0 files (create new wiki page recommended)
- **MODERATE**: Topics with partial coverage (update existing page)
- **ALREADY COVERED**: Skip — pipelines already handled it

## How to Integrate into the Report

1. Read the active-crawl output after running `trending_topics.py` + blogwatcher DB queries
2. Use HN point scores from active-crawl to **validate** trending_topics.py frequency counts
   — a topic with 8 raw sources but only 20 HN pts = lower signal than a topic with 4 sources and 1,100 HN pts
3. Use X bookmark counts to surface community-validated topics that RSS may have missed
4. Use the gap analysis to decide wiki action recommendations (already tells you HIGH/MODERATE/COVERED)
5. **Only run separate HN Algolia queries if no active-crawl output exists** (pipeline failure or holiday)

## Fallback: No Active-Crawl File

If the file doesn't exist (pipeline skip, day-1-after-setup, cron failure):

1. Run HN Algolia queries manually per `references/hn-algolia-discovery.md`
2. Run xurl search per active-crawl-wiki skill's parallel subagent prompts
3. Perform wiki gap analysis by searching concepts/ and entities/ directories
