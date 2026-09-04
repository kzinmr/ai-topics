# Sitemap-Monitor Articles as Dreaming Backlog

**Observed**: June 2026 dreaming-group triage — checkpoint had 0 articles, but 5 unprocessed sitemap articles found on disk.

## Pattern

When the dreaming checkpoint shows `total_articles: 0` and `articles: []`, the dreaming-collect step found nothing new from newsletter/RSS sources. But the sitemap-monitor pipeline (06:00 UTC) may have scraped company blog articles that escaped ALL downstream processing:

- **sitemap-monitor** (06:00) → scrapes company blog sitemaps → saves to `raw/articles/`
- **blog-ingest** (07:00) → scrapes RSS feeds → may miss sitemap-only articles
- **newsletter-triage** (07:20) → processes newsletter links → different source
- **active-crawl** (11:00) → hot-topics.yaml targets → may or may not catch same companies
- **dreaming-group** (18:10) → checks all unprocessed → catches the gaps

## Detection

```bash
# Step 1: Find today's sitemap-scraped articles
ls -lt ~/wiki/raw/articles/ | grep "$(date +%b\ %d).*06:00"
# Or for a specific date:
ls -lt ~/wiki/raw/articles/ | grep "Jun 25.*06:00"

# Step 2: Check if already wiki-processed
for f in "keyword1" "keyword2"; do
  grep -rl "$f" ~/wiki/entities/ ~/wiki/concepts/ 2>/dev/null
done

# Step 3: For articles NOT in wiki pages, read body (skip first 40 lines of nav chrome)
```

## Sitemap Article Content Structure

Sitemap-scraped articles typically have 30-40 lines of navigation chrome before article content:

```
Lines 1-8:   YAML frontmatter
Lines 9-13:  Source URL, title
Lines 14-40: Navigation chrome (menus, CTAs, breadcrumbs)
Lines 41+:   Article body content (if extracted)
```

**Assessment**: Start reading at line 40+. If lines 40-100 are still navigation chrome (repeated menus, "Sign in", "Get Started"), the article body was not extracted — skip.

## Verified Example (June 25, 2026)

5 sitemap articles from 06:00 UTC, none referenced in wiki pages:

| Article | Size | Content | Action |
|---------|------|---------|--------|
| Fireworks AI: Frontier-lab training infra | 14KB | Zero-KLD alignment, batch invariance for MoEs, DeepSeek DeepGEMM | ★★★★☆ take |
| Fireworks AI: Worker + advisor | 11KB | GLM 5.2 + Opus 4.8 benchmarks (SWE-bench Pro +7pp) | ★★★★☆ take |
| Harvey: Caryn Sandler case study | 18KB | Customer spotlight, marketing | ★★☆☆☆ skip |
| Cohere: Aston Martin F1 | 5KB | Partnership announcement, thin | ★☆☆☆☆ skip |
| ElevenLabs: API auth docs | 23KB | API reference documentation | ★☆☆☆☆ skip |

**Yield**: 2 takes (40%), 3 skips (60%) — higher than typical sitemap batch (~2-5%) because the 0-article checkpoint means other pipelines already filtered the easy wins.

## Cross-Reference Technique

Use `grep -rl` for filename-content matching (not `search_files` with regex which can miss):

```bash
# Check if article topic is in any wiki page
grep -rl "fireworks-ai\|zero-KLD\|batch invariance" ~/wiki/entities/ ~/wiki/concepts/ 2>/dev/null

# Check entity page for specific content
grep -n "GLM 5.2\|Opus 4.8\|SWE-bench Pro" ~/wiki/entities/fireworks-ai.md 2>/dev/null
```

If the entity page exists but lacks the article's specific technical details (benchmark numbers, architecture patterns), it's a genuine enrichment opportunity even though the entity covers the broader topic.

## Key Insight

The sitemap-monitor pipeline (06:00 UTC) is the ONLY pipeline guaranteed to run before dreaming-group (18:10 UTC) without any intermediate processing. Articles from company blogs that aren't in RSS feeds and aren't linked from newsletters will ONLY appear in sitemap output. This is a genuine gap source for the dreaming pipeline.
