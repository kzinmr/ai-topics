---
name: active-crawl-wiki
description: Scheduled autonomous wiki crawling to discover and document trending AI/ML developments
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [wiki, active-crawl, research, trending, ai-ml]
    category: research
    related_skills: [llm-wiki, web-extract, blogwatcher]
---

# Active Crawl for AI/LLM Knowledge Wiki

Systematic approach for scheduled autonomous wiki crawling to discover and document trending AI/ML developments.

## Trigger Conditions
- Scheduled cron job with no user-provided sources
- Wiki needs proactive gap discovery
- Emerging trends need documentation before they're widely covered
- Recurring "trending topics" report generation (e.g., daily or weekly)

## Process

### 1. Trend Discovery (Hybrid Scanning)

Two complementary approaches — use BOTH for richest coverage:

#### A) Blogwatcher DB Scan
```python
import sqlite3
# Discover articles in last 2-3 days
rows = conn.execute("""
    SELECT b.name, a.title, a.url, a.published_date
    FROM articles a JOIN blogs b ON a.blog_id = b.id
    WHERE DATE(a.discovered_date) >= date('now', '-2 days')
    ORDER BY a.discovered_date DESC
""").fetchall()
```
- Group by blog to spot clusters (same blog = same thought leader's hot topic)
- Check log.md to see if blog-ingest triage already processed today's batch — avoid re-analyzing
- If blogwatcher DB returns 0 results for today, the scan may not have run yet — use web_search as the primary source instead

#### B) Web Search (Broad Context)
- Run 3-5 targeted web_search queries: model releases, AI agent news, platform launches, research breakthroughs, Big Tech AI moves
- Use queries that triangulate from different angles:
  - `"AI ML trending topics <date>"` — broad discovery
  - `"latest AI agent developments news"` — agent ecosystem
  - `"LLM model release announcement <month>"` — model tracking
- Dedup results by topic (multiple queries may surface the same event)
- Supplement truncated web_search results with follow-up queries for specific topics

#### C) Cross-Reference Against Wiki (Coverage Gap Analysis)
```python
import os, glob
wiki = os.path.expanduser("~/wiki")
for slug, desc in topics.items():
    found = glob.glob(os.path.join(wiki, "concepts", f"*{slug}*"))
          + glob.glob(os.path.join(wiki, "entities", f"*{slug}*"))
    # Also check log.md for recent mentions
```
- Score each candidate topic: **FULL gap** (no page, no log mention) → highest priority; **PARTIAL gap** (page exists but missing recent info) → enrich; **COVERED** (fully documented) → skip
- Use `os.walk()` or `glob` not `search_files` — the tool can return false negatives on files that exist

### 1B. Trending Topics Report Workstream (Optional Variant)

When the goal is to produce a **summary report of what's trending** (not to create wiki pages immediately), use this dual-output variant instead of the standard create-pages flow:

#### Priority Scoring
Score each candidate topic 1-5 stars:
- ★★★★★ = New concept/page needed, major development, not in wiki at all
- ★★★★☆ = Existing page needs significant update, important new information
- ★★★☆☆ = Minor update worth noting, covered by entity page but new data exists
- ★★☆☆☆ = Mention only, low wiki value
- ★☆☆☆☆ = Skip entirely

#### Topic Tiers for Report Organization
Organize findings into visual priority tiers in the Japanese report:
- 🥇 **Tier 1** (2-3 topics): ★★★★★ gaps — newest, most impactful, not in wiki
- 🥈 **Tier 2** (2-3 topics): ★★★★☆ — important but partially covered or incremental
- 🥉 **Tier 3** (2-3 topics): ★★★☆☆ — interesting but lower urgency

#### Dual Output

**Output A — Human-readable Japanese report** (auto-delivered via cron):
- Title: `# 🚀 トレンドトピックレポート — YYYY-MM-DD`
- Each topic: emoji tier marker + **bold title** — 1-2 paragraph summary in Japanese
- Include concrete details: model names, paper URLs, company names, $ amounts
- End with: `📋 ウィクション推奨アクションサマリー` table (priority, action type, target)
- Include scan stats: RSS articles found today, how many already processed, newsletters pending

**Output B — Structured checkpoint JSON** (for downstream wiki-ingest pipelines):
```json
{
  "checkpoint_run_id": "YYYYMMDDTHHMMSSZ",
  "type": "trending-topics-daily",
  "summary_ja": "2-3 sentence Japanese summary of all topics",
  "topics": [
    {
      "priority": 1,
      "title": "Topic Title",
      "url": "https://...",
      "wiki_gap": "full|partial|covered",
      "recommended_action": "create|enrich|skip + path suggestion",
      "reason_ja": "★N 日本語理由"
    }
  ]
}
```
Save to: `${HERMES_HOME}/cron/data/trending/topics_latest.json`

### 1C. Save Raw Article

Before moving to page creation, save a comprehensive research note:
```
~/wiki/raw/articles/YYYY-MM-DD_trending-topics-research.md
```
- Include full YAML frontmatter with all source URLs
- One section per topic with key facts, source links, and preliminary wiki gap assessment
- This serves as the source material for any subsequent wiki page creation

### 2. Source Extraction
- Use `web_extract` on official sources only
- Skip aggregators and second-hand summaries
- Handle paywalled content: cross-reference with alternative sources, mark uncertain claims with qualifiers

### 3. Save Raw Articles First
```bash
# Naming convention: YYYY-MM-DD_source-topic.md
~/wiki/raw/articles/2026-05-06_cloudflare-llm-infrastructure.md
```

### 4. Create Wiki Pages
Each page must include:
- YAML frontmatter (title, created, updated, type, tags, sources)
- 4+ cross-references via [[wikilinks]]
- Tags from SCHEMA.md taxonomy
- Clear, scannable structure (headings, bullet points)

### 5. Update Navigation
- **Large index.md (>100KB):** Use programmatic Python approach
- **Small index.md (<100KB):** Use `patch` with exact anchor lines
- Update header counts (Total pages: N) — verify against filesystem
- Append to log.md with batch entry

### 6. Quality Verification
- Verify all new files exist
- Verify cross-references point to real pages
- Verify tag taxonomy compliance

### 7. Git Commit
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: active crawl — <count> new pages" && git push
```

## Pitfalls
- **Never modify raw/ files** — sources are immutable
- **Don't create pages for passing mentions** — follow Page Thresholds
- **Large files need programmatic approach** — read_file/patch fail silently on 200KB+ files
- **Always verify after operations** — check files exist before claiming success
- **Paywalled content needs qualifiers** — mark uncertain claims appropriately
- **Subagent iteration budgets are real** — max_iterations=20 allows ~5-7 page creations
- **Blogwatcher DB may have 0 results for today** if the scan hasn't run yet — fall back to web_search as primary source; don't report "[SILENT]" based on empty DB alone
- **Web_search queries may return overlapping results** — always dedup by topic across multiple queries; a single event (e.g., "OpenAI Daybreak") can appear in 3+ searches
- **Checkpoint JSON path must be consistent** — save to `${HERMES_HOME}/cron/data/trending/topics_latest.json` so downstream wiki-ingest pipelines can find it
- **Cross-referencing against wiki needs glob not search_files** — `search_files(target=files)` returns false negatives for files that exist on disk; use `os.walk()` or `glob.glob()` instead
- **Raw article for trending topics is a research note, not a source scrape** — it aggregates findings across multiple URLs with analysis, not a single extracted page. Use YAML frontmatter with a `sources:` list of all URLs referenced
