# Raw Article Discovery for Deep Reading

## Date-Range Discovery (3 days)

```bash
# Canonical path
find /opt/data/ai-topics/wiki/raw/articles -name "*.md" -mtime -3 2>/dev/null | sort | head -60

# Dual-path (canonical + cron HOME)
find /opt/data/ai-topics /opt/data/.hermes/home -path "*/raw/articles/*" -name "*.md" -mtime -3 2>/dev/null | sort | head -60
```

## By Keyword in Filename

```bash
find /opt/data/ai-topics/wiki/raw/articles -name "*microsoft*" -o -name "*gpt*" -o -name "*rosalind*" 2>/dev/null
```

## Reading Strategy

From the `trending_topics.py` output, you know which topics are trending (Claude, Google, GPT, OpenAI, etc.).
From the blogwatcher DB query 3, you have specific article titles and URLs.

To find the raw article file:
1. Guess the filename pattern from the source title/domain: `YYYY-MM-DD_source_slug.md`
2. Use `find` by date + partial keyword match
3. If no match, check the cron HOME fallback path (`/opt/data/.hermes/home/wiki/raw/articles/`)

## Articles to Prioritize (Heuristic)

- **Official blog posts from frontier labs** (OpenAI, Anthropic, Microsoft, Google, Meta) — always worth reading
- **X articles / megathreads from domain experts** — often contain deeper analysis than the official announcement
- **Simon Willison blog posts** — consistently high signal; he contextualizes and links to primary sources
- **AI Engineer YouTube talks** — conference presentations often include unreleased benchmarks or architecture details
- **Enterprise adoption case studies** (Harvey, Merge, Trilogy/Fireworks) — signal real-world usage patterns

## Raw Article File Naming Conventions: TWO PATTERNS

Articles come from two different pipelines, each with its own naming convention.

### Pattern A: Canonical (active-crawl / sitemap / manual scrape)

```
YYYY-MM-DD_source-slug_descriptive-slug.md
```

The source slug corresponds to the blog/outlet domain or author handle. For example:
- `2026-06-04_openai_gpt-rosalind-new-capabilities.md` → OpenAI blog about GPT-Rosalind
- `2026-06-04_arena-ai_agent-arena-methodology.md` → Arena blog
- `2026-06-05_cursor_cursor-3.md` → Cursor blog

### Pattern B: Blogwatcher-ingested (blog_ingest.py RSS/sitemap)

```
domain.com--path-segments-prefix--hash8.md
```

These come from `blogwatcher`/`blog_ingest.py` and use the source URL path with an 8-character hash suffix for dedup. For example:
- `simonwillison.net--2026-jun-6-micropython-in-a-sandbox--cfde862b.md`
- `eli.thegreenplace.net--2026-thoughts-on-starting-new-projects-with-llm-agents--7d421bbe.md`
- `garymarcus.substack.com--p-ais-black-friday--46e1b70c.md`
- `construction-physics.com--p-reading-list-060626--a83f7e7a.md`

### Finding Articles from Blogwatcher DB Output (CRITICAL)

When the blogwatcher DB query 3 returns article titles/URLs, **do NOT guess filenames** — Pattern B filenames are unpredictable due to hash suffixes. Instead, use keyword search across both wiki paths:

```bash
# From blogwatcher DB title → extract key unique word → search
find /opt/data/ai-topics /opt/data/.hermes/home -path "*/raw/articles/*" -name "*micropython*" 2>/dev/null

# Or use domain + date as broad search
find /opt/data/ai-topics /opt/data/.hermes/home -path "*/raw/articles/*" -name "*garymarcus*" 2>/dev/null
```

If a blogwatcher article has no matching raw file, it either wasn't fetched by blog_ingest yet, or was filtered out. Read the article directly from the URL in the DB output.
