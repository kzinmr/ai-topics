---
name: trending-topics-reporting
category: research
description: >-
  Regularly scan RSS feeds, blogwatcher DB, and raw articles for trending AI/ML
  topics. Synthesize findings into a Japanese-language report with top 5-8
  topics, source links, and wiki-action recommendations.
---

# Trending Topics Reporting

Scheduled research/reporting pipeline (12:00 UTC / 21:00 JST) that discovers, analyzes, and reports on trending AI/ML topics across all ingested sources.

## Pipeline Position

```
blog-ingest (07:00) → newsletter-ingest (07:10) → ... → trending-topics (12:00 UTC)
```

The pipeline runs **after** all morning ingestion pipelines have completed, so it sees the fullest picture of recent content.

## Prerequisites

- Run `trending_topics.py` script first (`python3 ~/ai-topics/scripts/trending_topics.py --days N`)
- Query blogwatcher DB for recent article counts
- Read key raw articles for depth

## Workflow

### Phase 1: Data Collection (DB + Script)

1. **Run the trending script**:
   ```bash
   python3 ~/ai-topics/scripts/trending_topics.py --days 3
   ```
   Output: topic frequency table, new-page candidates, hot topics (4+ sources).

2. **Query blogwatcher DB for context**:
   ```bash
   python3 -c "
   import sqlite3, os
   db_path = '/opt/data/.blogwatcher/blogwatcher.db'
   ...
   "
   ```
   - Get total articles in last 2-3 days
   - Group by blog source to see distribution
   - Filter for AI-relevant titles (containing: AI, LLM, agent, model, GPT, Claude, OpenAI, Anthropic, RL, fine-tun, reasoning, safety, inference, multimodal, embedding etc.)

3. **Discover raw article files**:
   - Primary path: `~/wiki/raw/articles/` (= `/opt/data/ai-topics/wiki/raw/articles/`)
   - Fallback path (cron HOME): `/opt/data/.hermes/home/wiki/raw/articles/`
   - Use `find` to locate key articles by name pattern or date

### Phase 2: Deep Reading

For each candidate trending topic (identified by frequency in Phase 1):

1. Read the article body content (at least first 30-50 lines)
2. Identify: key claims, entities mentioned, controversy/novelty level
3. Check if content aligns with wiki scope (LLM/AI Agent tech, tools, safety, infra)

### Phase 3: Topic Curation

Select the **top 5-8 topics** based on:
- **Frequency** — how many independent sources cover this topic
- **Novelty** — genuinely new development vs incremental update
- **Controversy** — debates/different viewpoints create discussion value
- **Wiki impact** — does this warrant new pages or page updates?

### Phase 4: Report Generation

Write a **Japanese-language report** with this structure:

```markdown
# 🔥 トレンドトピックレポート — YYYY-MM-DD

> 分析期間: YYYY-MM-DD → YYYY-MM-DD
> ソース: RSS N記事, blogwatcher DB + raw articles

## 1️⃣ 🛡️ [Topic Title] — [1-line subtitle]
**関連ソース:** source1, source2, ...
[3-5 sentence summary in Japanese with key facts]
- [Link description](url)
```

Each topic should have:
- **Ranked heading** with emoji indicator
- **Source attribution** (which blogs/outlets covered it)
- **Concrete summary** with specific facts, numbers, claims
- **Direct links** to source articles

### Final Table: Wiki Action Recommendations

```markdown
## 📊 ウィクション推奨アクション
| トピック | 強度 | アクション |
|---------|------|-----------|
| Topic | ★★★★★ | 既存ページ名 — 更新内容 |
```

### Save Path

Save to: `~/ai-topics/inbox/rss-scans/trending-topics-YYYY-MM-DD.md`

### Deliverable

Final response is auto-delivered. Format as clean markdown with the full report. Do NOT use `send_message` or deliver independently.

## Key Pitfalls

### Dual Article Storage Paths
The cron HOME mismatch means raw articles may be in **either** of two locations:
- `/opt/data/ai-topics/wiki/raw/articles/` — canonical (used by most pipelines)
- `/opt/data/.hermes/home/wiki/raw/articles/` — cron HOME (used by blog-ingest scripts)

Always use `find` to discover articles:
```bash
find /opt/data/ai-topics /opt/data/.hermes/home -path "*/raw/articles/*" -name "*keyword*" 2>/dev/null
```
`trending_topics.py` reads from **both** paths via the canonical wiki dir — but new articles from today's blog-ingest may only be in the cron HOME path until the next sync.

### Blogwatcher DB may not have recent data
If the DB scan or ingest scripts failed, the trending_topics.py output may show 0 sources. In this case:
- Check `~/.hermes/cron/data/blog_ingest/latest.json` for the latest checkpoint
- Scan `~/wiki/raw/articles/` and the cron HOME fallback directly for any recent `.md` files
- Fall back to `web_search` for broader context if needed

### Cron HOME != canonical HOME
In cron mode, `HOME=/opt/data/.hermes/home` not `/opt/data`. The `~` resolves differently. Always use absolute paths.

### `web_search` is NOT available in terminal
Use the search tool or browser tool for web searching. The terminal has no `web_search` command.

### Report content length
Keep the final report concise — 5-8 topics with 3-5 sentences each. The auto-delivery system has a character limit. A full report is typically 4-8KB.

## Cron Job Context

- **Schedule**: 12:00 UTC (21:00 JST) daily
- **No user present** — make all decisions autonomously
- **No asking questions** — reasonable interpretation wins
- **Japanese output** required as the user reads Japanese
- **Save to `inbox/rss-scans/`** for audit trail
- **No commit needed** — this is a report, not wiki content
