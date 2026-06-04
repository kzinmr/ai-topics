---
name: daily-rss-triage
description: Daily RSS scan triage workflow — scan blogs, triage articles, ingest into wiki, commit changes
category: research
---

# Daily RSS Triage Workflow

End-to-end pipeline for processing daily RSS scans, triaging articles, and ingesting wiki-worthy content.

## Prerequisites

- `blogwatcher-db` skill loaded (database queries)
- `semantic-article-grouping` skill loaded (triage criteria)
- Pre-run script has already executed blogwatcher scan, queried DB, read newsletter, listed existing topics

## Workflow

### Phase 1: Report Generation

1. Parse script JSON output for scan results
2. Generate Japanese summary report (scan stats, failed blogs, articles list, Reddit highlights, newsletter info)
3. Save to `~/ai-topics/inbox/rss-scans/daily-scan-YYYY-MM-DD.md`
4. If article_total > 0 but ≤3 are AI-relevant, supplement with web_search (see Low-Article Day Fallback below)
5. If article_total == 0 AND no newsletter → `[SILENT]`

### Phase 1b: Low-Article Day Fallback (web_search supplementation)

When RSS scan yields few AI-relevant articles, the blog scan alone is insufficient. Supplement proactively:

1. **Web search** for recent AI headlines: `AI ML trending news May 2026` or specific domains (model releases, security incidents, robotics, geopolitical AI chip news)
2. **Cross-reference newsletter triage** — may have processed substantive content that RSS missed
3. **Score discovered topics** with Newsjacking filter — top 5-7 become the report's lead stories
4. **Save raw articles** from official sources (NIST reports, Reuters exclusives, company blogs)
5. **Create/update wiki pages** prioritizing highest wiki-actionability topics

**Effective search queries (discovered in production):**
- `"CAISI evaluation" DeepSeek V4` — NIST government evaluations
- `US officials weigh cutting deadlines fix digital flaws AI-powered hacking` — CISA/Reuters exclusives
- `exodus Boston Dynamics executives humanoid delivery` — Semafor/Business Insider scoops
- `Richard Dawkins Claude consciousness delusion` — AI culture war debates
   - All blog articles list
   - Reddit highlights (top 5 per subreddit)
   - Newsletter info (if exists)
3. Save to `~/ai-topics/inbox/rss-scans/daily-scan-YYYY-MM-DD.md`
4. **If article_total == 0 AND newsletter.exists == false → respond `[SILENT]` and stop**

### Phase 1.5: Newsjacking Triage Filter (READER perspective)

Before detailed triage, apply Newsjacking lens (from Elvis Sun's framework) to identify high-signal articles:

1. **Trend Surfing**: Does the article ride an existing wave? (e.g., Claude Code launch, new model release, viral AI tool)
2. **Polarizing Promise**: Does it make a bold, debatable claim that creates curiosity? ("X is dead", "Everyone is wrong about Y")
3. **Contrarian Insight**: Does it challenge conventional wisdom with data-backed arguments?
4. **Pattern Interrupt**: Is it structurally or topically unusual for its source? (e.g., Karpathy writing about biology, Simon Willison on non-web topics)
5. **In-Group Signal**: Does it use specialized knowledge that creates an "insider" resonance for the target audience (r/LocalLLaMA, AI agent developers)?

**Scoring**: Assign each article a `newsjacking_score` (0-5) based on how many criteria it meets.
- Score ≥ 3: **Priority triage** — flag for immediate wiki ingestion
- Score 1-2: **Standard triage** — normal evaluation
- Score 0: **Low priority** — only ingest if highly relevant to core interests

### Phase 2: Triage

For each article, evaluate:
1. **Already covered?** Check `existing_wiki_topics` list
2. **Substantive?** Not a link dump, not Reddit noise
3. **Relevant?** LLMs, AI agents, coding agents, developer tooling, inference/training, prompt engineering, AI safety, open-source AI
4. **Newsjacking score?** (from Phase 1.5) — higher scores get priority placement

Output triage table:
```
| ソース | タイトル | NJスコア | アクション | 対象 |
|--------|----------|----------|------------|------|
| simonwillison.net | タイトル | 4/5 | wikiエントリ作成 | entities/simon-willison.md |
| blog.example.com | タイトル | 1/5 | スキップ（既存） | — |
```

### Phase 3: Wiki Ingestion

For each "wikiエントリ作成" article:

1. **CRITICAL: Check existing entity pages FIRST**
   ```bash
   # Check if file exists with ANY name variation
   search_files(pattern="entity-name", path="~/ai-topics/wiki/entities", target="files")
   ```
   - The `wiki/index.md` may reference entities with different filenames than expected (e.g., `[[entities/gpjt]]` for "Giles Thomas")
   - Always verify file existence before creating new pages

2. **Scrape content**: `web_extract([article_url])`

3. **Determine category**:
   - `entities/` — people, companies, blogs, tools
   - `concepts/` — techniques, patterns, ideas
   - `comparisons/` — head-to-head analyses
   - `queries/` — research questions

4. **Create or update page**:
   - If updating: read existing file, append new content under appropriate section, update `updated:` frontmatter
   - If creating: follow existing entity page format (frontmatter + overview + core ideas + related + sources)

5. **Update index and log**:
   - `wiki/index.md` — add/update entity reference (match the filename convention used in index)
   - `wiki/log.md` — add dated entry with changes summary

6. **Commit and push**:
   ```bash
   cd ~/ai-topics && git add wiki/ inbox/rss-scans/ && git status
   # CRITICAL: Check for pre-staged files from previous runs
   git diff --staged --stat
   git commit -m "wiki: daily scan YYYY-MM-DD — [summary]" && git push
   ```

## Key Pitfalls
- **Index stub detection**: `search_files("firstname.*lastname")` on the index may miss existing stubs if the index entry uses a different format (e.g., `**Role** | Professor Emeritus` instead of the person's name). Always also check `search_files(target="content")` for the person's name in the entities directory before creating a new entity page. stubs created by `build_x_wiki.py` or `build_blog_wiki.py` may exist even when `search_files` returns nothing.
- Index filename mismatches: short handles vs full names
1. **Index filename mismatches**: `wiki/index.md` may use short handles (`gpjt`) while you'd expect full names (`gilesthomas-com`). Always check the index first.

2. **Pre-staged files**: Previous cron runs or sessions may have already staged files. Use `git diff --staged` before committing to understand what's changed.

3. **Duplicate entity creation**: Always search for existing entity files before creating new ones. The same person/company may already have a page under a different name.

4. **No content to report**: If `article_total == 0` AND no newsletter exists, respond `[SILENT]` — don't generate empty reports.

5. **Category field is JSON**: In blogwatcher DB, `categories` is a JSON array. Use `LIKE '%\"tag\"%'` for SQL filtering or `json.loads()` in Python.

6. **Published vs discovered dates**: Use `discovered_date` for "when blogwatcher found it", `published_date` for "when article was published" (can be NULL).

7. **`search_files` is unreliable for wiki directory discovery**: It returns `{"total_count": 0}` for `~/ai-topics/wiki/**/*.md` patterns. Use `execute_code` with Python `os.walk()` or `pathlib` for directory traversal and file existence checks instead.

8. **RSS 429 rate limits**: `r/LocalLLM` and `r/LocalLLaMA` frequently hit HTTP 429. Log failures but do NOT retry immediately — wait for next scan cycle to avoid exacerbating rate limits.

9. **Substack redirect URLs**: Newsletter articles use tracking-heavy Substack redirect URLs (e.g., `substack.com/redirect/UUID`). `web_extract` handles these natively — pass the full redirect URL, do not strip tracking parameters.

10. **Batch file creation before git commit**: When creating multiple wiki pages (6+), create all files first using `execute_code` with Python `open()/write()`, then do a single `git add wiki/ && git commit && git push`. Multiple small commits are fine for updates to existing files, but batch new file creation.

11. **Context window management**: When running as a cron job with many articles (90+), tool outputs may fill the context window. Use `[Old tool output cleared to save context space]` pattern mid-run and reconstruct state via targeted `read_file` with `offset` + `execute_code` directory checks.

12. **Entity update vs create decision**: For established entity files (e.g., `antirez-com.md`, `pluralistic-net.md`), append new sections under existing headers rather than rewriting. Preserve historical continuity and frontmatter integrity. For new entities, follow the existing frontmatter format with `title`, `created`, `updated`, `tags`, `related`.

13. **Reddit URL extraction failures**: `web_extract` consistently fails on Reddit URLs with "Content was inaccessible or not found". Reddit uses Cloudflare protection and dynamic content loading that defeats simple HTTP extraction. For Reddit articles, skip scraping and only record the URL/title in triage. If content is needed, use `browser_navigate` + `browser_snapshot` as a fallback (higher resource cost).

14. **Git rebase in headless cron environment**: When running as a cron job, `wiki/log.md` can be modified concurrently (e.g., by another scheduled run or external process), causing git push rejections that require `git pull --rebase`. In headless environments with no `EDITOR` set, `git rebase --continue` hangs. Always use `GIT_EDITOR=true git rebase --continue` to bypass interactive editor prompts. If conflicts occur, `git checkout --theirs <file>` accepts the remote version, then continue.

## Output Language

All reports, triage tables, and wiki content should be in **Japanese** unless the source material is explicitly English-only and the user has not requested Japanese output.