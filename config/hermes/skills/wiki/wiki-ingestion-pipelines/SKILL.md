---
name: wiki-ingestion-pipelines
category: wiki
description: >-
  Umbrella for all wiki ingestion pipelines — newsletter ingest, blog ingest,
  active knowledge crawl, arXiv paper pipeline, OpenAI blog ingestion,
  dreaming knowledge consolidation, and pipeline troubleshooting.
---

# Wiki Ingestion Pipelines (umbrella)

This umbrella skill covers all automated wiki ingestion pipelines — from external source to wiki page. Each section below covers one pipeline end-to-end, including cron configuration, checkpoint handling, and failure recovery.

All pipelines follow the same fundamental pattern:
```
fetch external content → checkpoint → triage → wiki-ingest (create/update pages) → commit
```

---

## Section A: Newsletter Pipeline (newsletter-wiki-ingest)

Consume a pre-triaged checkpoint JSON from the newsletter-triage cron job and create/update wiki pages autonomously.

### Pipeline Chain
```
newsletter-ingest (07:10 UTC) → newsletter-triage (07:20 UTC) → newsletter-wiki-ingest (07:40 UTC)
```

### Input Format
Triage checkpoint JSON is injected via `context_from` cron chaining, or available at:
- `${HERMES_HOME}/cron/data/newsletter/triage_latest.json`

### Workflow
1. **Orient** on wiki: read SCHEMA.md, index.md, recent log.md
2. **Load the checkpoint** — filter to `recommended_action === "take"` decisions
3. **Detect prior batch** — scan log.md for same source/newsletter title
4. **Process each take decision**:
   - ★★★★★ → New concept page
   - ★★★★☆ → Update existing page
   - ★★★☆☆ → Entity page update
5. **Create new pages first** (write_file), then update existing (patch), then index.md and log.md
6. **Commit and push**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: newsletter ingest ..." && git push`
7. If no take decisions, respond `[SILENT]`

### Triage Failure Recovery
When checkpoint is missing or failed (most common: `ok: false` with `output_path`):
1. Read the triage failure output file — it contains the embedded newsletter-ingest checkpoint with `candidates` array
2. Parse candidates for `open.substack.com/pub/{pub}/p/{slug}` canonical URLs (NOT tracking redirects)
3. Call `web_extract` on canonical URLs to get newsletter post body with real article links
4. Filter UI noise, assign star ratings, create/update wiki pages
5. Log: "newsletter-triage failed to produce valid JSON; wiki-ingest performed triage directly"

See `references/newsletter-wiki-ingest.md` for full Substack URL resolution patterns and State A/B/C handling.

### Key Pitfalls
- Detect follow-up batches before creating pages
- Subagents need explicit absolute paths (`/opt/data/ai-topics/wiki/...`)
- Japanese output is mandatory for cron reports
- Commit early for large batches to prevent data loss from tool call limits

See `references/newsletter-wiki-ingest.md` for full workflow details.

---

## Section B: Active Knowledge Crawl (active-knowledge-crawl)

Daily cron job that proactively researches and ingests new concepts based on `config/hot-topics.yaml`.

### Trigger
Scheduled cron job, or manual invocation by user.

### Workflow
1. **Select Topics**: Read hot-topics.yaml, extract topics with stale `last_crawled` (>3 days)
2. **Gap Discovery** (optional when few stale topics): Survey major AI domains not in hot-topics.yaml
3. **Research**: For each topic, crawl prerequisites, laterals, or deep-dives
4. **Create Wiki Pages**: Web search → save raw source → create concept page → update index/log
5. **Update hot-topics.yaml**: Set `last_crawled: YYYY-MM-DD`
6. **Commit**: `cd ~/ai-topics && git pull --rebase && git add wiki/ config/hot-topics.yaml && git commit && git push`

### Constraints
- Max 2 concepts per topic, max 6 total per run
- Source file in raw/articles/ REQUIRED before creating concept page
- Depth-1 only (grandchildren out of scope)
- arXiv-only (not peer-reviewed) papers FORBIDDEN as sources
- Git push may fail in cron — report status clearly

### Critical Lessons
- Files may already be committed (duplicate run detection): check `git ls-files` first
- Verify files exist after `delegate_task`: explicit file existence check
- `git pull --rebase` fails with unstaged changes: use `git stash && pull && stash pop`
- YAML via str.replace fragil — use sed with line numbers for hot-topics.yaml updates
- Avoid `git add -A` when sibling agents write to same repo — use selective `git add`

---

## Section C: OpenAI Blog Ingestion (openai-blog-article-ingestion)

Simple workflow for ingesting openai.com/blog articles.

### Workflow
1. **Scrape & Save**: `web_extract(url)` → save to `wiki/raw/articles/{date}-{slug}.md`
2. **Check existing pages** → patch existing concept/entity or create new
3. **Update index.md and log.md**
4. **Commit**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest OpenAI blog article - {topic}" && git push`

### Pitfalls
- OpenAI blog URLs may have `/index/` path prefix
- Don't create duplicate pages
- Create minimal stub entity pages for newly mentioned people/organizations

---

## Section D: arXiv Paper Pipeline (arxiv-paper-pipeline)

Workflow for pulling arXiv papers, triaging by peer-review status, and ingesting into wiki.

### Save Path
Always save to `~/wiki/raw/papers/` (NOT `~/wiki/raw/articles/`).
Naming: `{YYYY-MM-DD}_{arxiv_id}_{short-title}.md`

### Triage Decision Matrix
| Paper Type | Action |
|---|---|
| Peer-reviewed conf/journal (NeurIPS, ICML, ICLR, ACL, CVPR, JMLR, TACL, Nature, Science) | ✅ Wiki-ingest OK |
| Tech company/industry research lab tech report (OpenAI, Meta, Google, MS, Anthropic, Huawei, Apple, Amazon, NVIDIA, and similar) | ✅ Wiki-ingest OK |
| arXiv-only (no venue) | ❌ BLOCK |
| User explicitly requests blocked paper | ✅ User override — ingest with blocked_reason note |

### Peer-Review Detection
1. Check abstract page for "Published in", "Accepted to"
2. Search Semantic Scholar for `publicationVenue`
3. If no venue found → mark as blocked

### Processing Steps
1. Search arXiv API or Semantic Scholar
2. For each candidate: fetch metadata → research peer-review → apply triage → save or block
3. If accepted: save to papers/ → create/update wiki page
4. Integrate user-provided context (tweets, discussions) alongside paper content

### Name Collision Handling (RLM and similar proliferating frameworks)

When a paper's framework name collides with an existing concept page (e.g., Huawei's lambda-RLM vs Galanos's Lambda-RLM):

1. **Detect collision early** — `search_files` for the framework name in existing concept slugs and content before creating pages
2. **Create a new concept page with a distinct, descriptive slug** (e.g., `typed-rlm` instead of reusing the conflicting `lambda-rlm`)
3. **Add frontmatter aliases** on the new page to capture the paper's name: `aliases: [original-name, Y-Combinator X, etc.]`
4. **Add a disambiguation warning** to the EXISTING page's top — brief note with wikilink to the new page
5. **Build a comparison table** on the new page showing control model, formal proofs, empirical scope, source lineage
6. **Update the parent concept page** (e.g., `rlm-recursive-language-models`) to list both as named variants
7. **Update log.md** — explain the collision, the resolution, and the comparison

See `references/arxiv-paper-pipeline.md` for further detail on blocked paper handling and JSON format.

---

## Section E: Blog Pipeline Troubleshooting (blog-ingest-troubleshooting)

Debug and fix the full blog/newsletter cron pipeline chain.

### Pipeline Architecture
```
ingest ──checkpoint──▶ triage ──checkpoint──▶ wiki-ingest
```

### Checkpoint File Locations
| Pipeline | Ingest checkpoint | Triage checkpoint |
|----------|-----------------|-------------------|
| Blog | `~/.hermes/cron/data/blog_ingest/latest.json` | `~/.hermes/cron/data/blog_ingest/triage_latest.json` |
| Newsletter | `~/.hermes/cron/data/newsletter/latest.json` | `~/.hermes/cron/data/newsletter/triage_latest.json` |

### Most Common Failure: "Checkpoint Cascade"
- Ingest script times out → checkpoint stays stale
- Triage reads old checkpoint → sees 0 articles → nothing output
- Wiki-ingest reads empty triage → `[SILENT]`

### Re-executing a Pipeline
1. Run ingest jobs first (blog + newsletter concurrently)
2. Then triage jobs
3. Then wiki-ingest jobs

⚠️ `cronjob(run)` is async — run ingest scripts directly from terminal if cron scheduler fails:
| Pipeline | Script path |
|----------|-------------|
| Blog ingest | `python3 ~/.hermes/scripts/blog_ingest.py` |
| Newsletter ingest | `python3 ~/scripts/process_email.py` |

### Stage-Specific Issues
**Ingest:**
- Missing `daily_inbox_collect` module → create stub module
- Wrong DB path → use `~/.blogwatcher/blogwatcher.db`
- Pre-run script timeout → parallelize with ThreadPoolExecutor, write checkpoint before scraping
- **CRITICAL: SQLite `is_read` dedup pattern** — The blogwatcher DB (`~/.blogwatcher/blogwatcher.db`) has `articles` table with `is_read` (boolean) and `discovered_date` (date) columns. If `blog_ingest.py` times out at 120s, the most likely cause is `query_todays_articles()` in `daily_inbox_collect.py` lacking a date filter, causing it to fetch ALL articles (thousands of rows) instead of just today's. The fix:
  1. Ensure SQL query includes `WHERE discovered_date >= date('now', '-1 day') AND is_read = 0`
  2. After successful scrape+save in `blog_ingest.py`, call `mark_articles_as_read()` to set `is_read = 1`
  3. This prevents duplicate processing on subsequent cron runs
  4. The `daily_inbox_collect` module lives at `~/.hermes/scripts/daily_inbox_collect.py`
  5. After fixing scripts, re-run the pipeline and `cd ~/ai-topics && git add wiki/ && git commit && git push`

**Triage:** Reads from ingest checkpoint. Empty checkpoint → no output. May also produce markdown report instead of valid JSON — downstream wiki-ingest will fail with parse error. See `references/blog-ingest-troubleshooting.md` for recovery.

**Wiki-ingest:** Reads from triage checkpoint. No take decisions → [SILENT].

### Script Dual Location
Scripts live in TWO locations that must be kept in sync:
| Location | Purpose | Git-tracked? |
|----------|---------|-------------|
| `~/ai-topics/scripts/` | Source of truth | ✅ Yes |
| `~/.hermes/scripts/` | Cron execution copy | ❌ No |

When fixing: edit ai-topics/scripts, then cp to .hermes/scripts.

---

## Section F: Dreaming — Knowledge Consolidation Cycle (dreaming)

Automated consolidation process analyzing recently collected articles and folding significant findings into the wiki.

### Pipeline
- **Phase 1 (pre-run script)**: `~/ai-topics/scripts/dreaming.py` collects RSS scan articles, newsletters, existing wiki pages
- **Phase 2 (LLM processing)**: Analyzes, creates/updates wiki pages, commits

### Workflow
1. **Duplicate Check**: Review what adjacent scheduled jobs already completed (daily inbox update, active crawl, etc.)
2. **Light Sleep** (Screening): Review articles not already processed, group by semantic themes
3. **REM** (Flat Synthesis): Score each theme using weighted signals (relevance 0.30, frequency 0.25, query_diversity 0.15, recency 0.15, consolidation 0.10, conceptual_richness 0.05)
   - Score ≥ 0.65: Create or update wiki page
   - Score 0.45-0.65: Add to existing page or log for review
4. **NJ Delivery Filter**: Apply Newsjacking lens (0-5) to select what to deliver
   - NJ ≥ 4: Lead story; NJ = 3: Secondary; NJ ≤ 1: Omit from delivery
5. **Deep Sleep** (Replay-safe integration): Create/update wiki pages, cross-references, index/log, commit

### Sub-Patterns
- **Pattern A**: Existing coverage depth check — don't auto-update, check if page already covers the insight
- **Pattern B**: Newsletter noise filtering (Substack UI elements, redirect chains)
- **Pattern C**: Batch entity discovery — create missing entity pages for recurring people/companies
- **Pattern D**: Duplicate detection matrix (filename, index entry, content grep, session_search)

### Pitfalls
- Duplicate detection is MANDATORY
- Always check existing pages first
- Log.md corruption via patch (accidental `|` prefix from read_file format)
- Pre-run script may timeout — fall back to `grouped_themes_latest.json`

---

---

## Section G: Newsletter Triage (newsletter-triage)

### URL Resolution Patterns (CRITICAL — raw files contain tracking URLs, not canonical)

**Substack newsletters:**
- Look for `open.substack.com/pub/{publication}/p/{slug}` (usually Link 7 or 9)
- Canonical form: `https://www.{publication}.com/p/{slug}` or use the open.substack URL directly with web_extract
- IGNORE: `substack.com/redirect/2/...` (resolves to app download), `substack.com/app-link/post?...` (email tracking)
- For author attribution: extract from the raw file's `substack.com/@authorname` links

**Beehiiv newsletters:**
- URLs are wrapped as `link.mail.beehiiv.com/v1/c/...` 
- Resolution: `web_search` with subject line + date to find canonical article URL
- The raw beehiiv newsletter digest file is saved in wiki/raw/newsletters/ but individual links need external resolution

**Cron pipeline context:** The newsletter-ingest cron job saves raw digests to wiki/raw/newsletters/ — this is the source data. Each digest contains 16-20 links, most of which are tracking/redirect URLs requiring resolution.

### Classification Criteria

| Level | Criteria | Action |
|-------|----------|--------|
| **Critical** | Direct AI agent/LLM relevance, comprehensive landscape updates, major product launches | Create new concept/entity pages, major enrichments |
| **High** | Specific tooling/workflow coverage, industry context with wiki actionability | Enrich existing entities, create concept pages |
| **Medium** | Weekly roundups with 1-2 relevant items | Selective entity enrichment |
| **Low** | No wiki actionability | Skip |

### Triage Output Format

Save JSON with: `triage_timestamp`, `run_id`, `newsletters[]` (each with `message_id`, `subject`, `source`, `date`, `canonical_url`, `classification`, `summary`, `wiki_relevance`, `recommended_action`), and `summary` (counts, `key_themes[]`, `recommended_wiki_updates[]`).

### Save Locations
- `/opt/data/.hermes/cron/data/triage/newsletter-triage-{timestamp}.json` (for downstream `newsletter-wiki-ingest`)
- `/opt/data/ai-topics/wiki/raw/inbox/newsletter-ingest/{timestamp}.json` (wiki inbox copy)

### Key Pitfalls
- Raw newsletter files in wiki/raw/newsletters/ contain ONLY tracking/redirect URLs — you MUST resolve to canonical URLs before content extraction
- The beehiiv newsletter digest is saved but the source file may not appear in the raw directory listing (it IS there, just needs reading)
- Substack redirect chains: `substack.com/redirect/...` → app download page, NOT the article. Always use `open.substack.com/pub/...` pattern
- Multiple newsletters can arrive in the same batch — classify each independently

See `references/newsletter-triage.md` for detailed URL resolution patterns, classification criteria, and output format.

---

## Section H: Daily RSS Triage (daily-rss-triage)

See `references/daily-rss-triage.md` for full workflow.

End-to-end pipeline for processing daily RSS scans: scan blogs → triage → ingest → commit.

### Pipeline Position
Pre-run script executes blogwatcher scan, queries DB, reads newsletter, lists existing topics.
The daily RSS triage is the **triage + ingest** stage of the blog pipeline.

### Workflow
1. Parse script JSON output for scan results
2. Generate Japanese summary report → save to `~/ai-topics/inbox/rss-scans/daily-scan-YYYY-MM-DD.md`
3. If article_total == 0 AND no newsletter → `[SILENT]`
4. Apply Newsjacking Triage Filter (0-5 score):
   - Trend Surfing, Polarizing Promise, Contrarian Insight, Pattern Interrupt, In-Group Signal
   - Score ≥ 3: Priority triage; 1-2: Standard; 0: Low priority
5. For each article: check existing wiki topics, evaluate relevance, scrape content
6. Create/update wiki pages, update index/log, commit
7. All reports in **Japanese**

### Key Pitfalls
- `search_files` unreliable for wiki directory discovery — use Python `os.walk()`
- RSS 429 rate limits — log failures, don't retry immediately
- Reddit URLs fail with web_extract — use browser tools as fallback
- Pre-staged files from previous runs — check `git diff --staged` before committing

---

## Section H: Raw Article Curation (wiki-raw-article-curation)

See `references/wiki-raw-article-curation.md` for full workflow.

Systematically reduce the "unprocessed raw articles" count reported by `wiki_health.py`.

### Detection
```bash
python3 ~/ai-topics/scripts/wiki_health.py | grep -A 3 "Unprocessed Raw Articles"
```

### Mixed-Strategy Approach (< 100 unprocessed)
1. **"Already Consumed but Unlinked" check**: Search unique phrase from article in L2 pages
2. **Tier 1 (High-Value)**: Deep-read and enrich existing wiki pages
3. **Tier 2 (Bulk-Associate)**: Add filename to existing page's References section

### Association Targets
| Article Type | Best Target |
|---|---|
| Author blog | Their entity page |
| Technical concept | Relevant concept page |
| Newsletter tracking pixel | `wiki/concepts/blogwatcher.md` |
| Metadata-only artifacts | `wiki/concepts/blogwatcher.md` |

### Bulk-Associate Workflow (>100 unprocessed)
1. Domain analysis — group by domain/author
2. Keyword-to-entity mapping
3. Batch update entity pages
4. Handle remaining unmatched articles

### Pitfalls
- Substring matching quirk: filename stem must appear verbatim in L2 content
- Escape-drift on YAML frontmatter patches — use markdown References section instead

## Section I: X Bookmarks Ingest (x-bookmarks-ingest)

Cron pipeline triggered by `fetch_x_bookmarks.py` that processes incoming X/Twitter bookmarks and ingests external articles into the wiki.

### Pipeline Chain
```
fetch_x_bookmarks.py (pre-run script, every 6h) → x-bookmarks-ingest (agent cron)
```

### Input Format
The agent cron job receives a JSON payload with `new_bookmarks[]` array. Each bookmark contains:
- `id`, `author_id`, `created_at`, `text`, `public_metrics` (bookmark_count, like_count, etc.)
- `entities.urls[]` — each URL has `expanded_url`, `display_url`, `status` (HTTP), and optionally `title`/`description`
- `external_urls[]` — URLs with `status: 200` that are NOT X article links
- `article` — for X Articles (`x.com/i/article/...`), contains `title` field

### Workflow

1. **Extract actionable URLs**: Filter bookmarks for `external_urls[]` with `status: 200`. These are direct article links (OpenAI blog, Substack, arXiv, etc.). X Articles (`x.com/i/article/...`) with `status: 500` require the fallback path.

2. **Scrape external articles**: `web_extract()` each external URL. Save to `wiki/raw/articles/{YYYY-MM-DD}_{source}_{slug}.md`. The OpenAI blog and Meta/FAIR research blogs typically return full content.

3. **X Article fallback**: For bookmarks where the only URL is an X Article behind the auth wall:
   - Extract `article.title` from bookmark metadata
   - Run `web_search` with: `"<article title>" 2026` (add author name or domain keywords)
   - Common mirrors: LangChain blog (`blog.langchain.com/...`), Substack, arXiv, personal blogs
   - If found → scrape and save. If not → mark as metadata-only, skip wiki creation.
   - Notable authors often cross-post: check `blog.langchain.com`, `substack.com`, author's personal site.

4. **Check for existing entity pages BEFORE creating new ones**: This is the most common pitfall. Before creating any person/org entity page:
   - `search_files(pattern="firstname.*lastname|@handle", path="~/wiki/entities", target="files")`
   - Also check `search_files(target="content")` for aliases referencing the same person under different slugs (e.g., Varun Trivedy = Vivek Trivedy = @Vtrivedy10)
   - If an existing page is found (even with a slightly different slug), update THAT page — do NOT create a duplicate.

5. **Prioritize by engagement**: Process highest-bookmark-count articles first (signal of importance).

6. **Create/update wiki pages**: Follow `wiki-entity-enrichment-from-article` skill for entity/concept creation. For multi-article batches by the same author (e.g., two LangChain blog posts by Vivek Trivedy), use the Multi-Source Same-Author Sequential Enrichment pattern.

7. **Update index.md and log.md**: One log entry summarizing the entire batch. Update index.md entry count. Patch existing concept page descriptions if significantly changed.

8. **Commit and push**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: X bookmarks ingest — <summary>" && git push`

### Key Pitfalls

- **Duplicate entity detection is MANDATORY**: Before creating any person entity page, search for existing pages under different slugs (e.g., `vtrivedy10.md` vs `varun-trivedy.md` vs `vivek-trivedy.md`). Many tracked people already have pages created by `build_x_wiki.py`.
- **X Articles behind auth wall**: `web_extract()` on `x.com/i/article/...` returns JavaScript wall or login page. Don't waste time retrying — go straight to `web_search` for mirrors.
- **Image-only bookmarks**: Bookmarks where the only URLs are `pic.x.com/...` media links have no scrapable content. Skip them.
- **Thread-only bookmarks**: Bookmarks where the content is entirely in the tweet text with no external URL. Skip for article scraping (save as metadata-only).
- **LangChain blog mirror pattern**: When searching for X Article mirrors, `blog.langchain.com` is a common target — many agent/harness engineering articles are cross-posted there.
- **Don't create duplicate Vivek Trivedy pages**: He already has `vtrivedy10.md` (188 lines, canonical) + `varun-trivedy.md` (173 lines, duplicate waiting for dedup). Use `[[vtrivedy10]]` as the wikilink target.

### Deliverable Format (cron)
The final response is auto-delivered. Report findings concisely:
- ✅ Processed articles with wiki actions
- 🆕 New pages created
- ✏️ Updated pages
- ⏭️ Skipped/auth-walled articles
- 🔍 Notable discoveries (duplicates found, new entities identified)

If nothing was scrapable (all bookmarks are image-only, thread-only, or X Articles with no mirrors found), respond `[SILENT]`.

---\n\n## JS-Rendered Site Workaround (companion GitHub repo)

Many modern doc sites (Next.js SPAs) render sub-page content client-side, so `web_extract()` returns empty results on all pages except the SSR'd landing page.

**Solution**: Check the main landing page for a companion GitHub repo link (usually a "View on GitHub" badge or footer link). Clone the repo — it typically contains markdown READMEs and source code for each module/lesson.

See `references/js-rendered-docs-workarounds.md` for the full workflow, detection patterns, and the Braintrust Evals 101 case study.

## Manual Article Ingest Patterns

When ingesting a single URL (not batch pipeline), see `references/manual-article-ingest-patterns.md` for:
- **Author identification** via secondary search when `web_extract()` omits the byline
- **Related-concept detection** — checking existing pages before creating new ones
- **Author/org/product mapping** — which entities to create from a single article
- **MCP tool identification** — extracting tool names from article data source mentions
- **Pattern 6: Substack multi-part series batch discovery** — checking `/archive` to find all parts when given part 1 only

---

## General Pipeline Pitfalls

- **Always orient first** — read SCHEMA.md + index + recent log before any operation
- **Detect follow-up batches** — check log.md for same source before creating pages
- **Escape-drift on YAML frontmatter patches**: Add to markdown References section instead
- **Partial-match corruption on patch** — When `old_string` matches only a PREFIX of a target line (not the full content), the patch tool replaces only the matched portion and appends the REMAINING original text onto your new content. **Fix:** Always include enough trailing context in `old_string` to uniquely identify the ENTIRE line — preferably the full text of the line from the file. Verify by reading the file first with `read_file(offset, limit)` and using the exact bytes shown. After every patch on index files, immediately re-read the affected lines to check for appended garbage text. If corruption occurred, fix with a second patch that replaces the corrupted substring.
- **Context compaction can mask prior work** — review compaction summary for already-completed tasks
- **Commit message `&` trap**: The terminal tool interprets `&` as shell backgrounding. If your commit message contains `&` (e.g., `set_to_none=True`, `agents & tools`), use **single quotes**: `git commit -m 'wiki: safe message here'`. Double quotes fail silently. Also, `&&` chaining triggers the tool's backgrounding detection — split into separate `git add`, `git commit`, `git push` calls when `&&` chaining fails.
- **Total page count in index.md header must be correct**
- **concepts/_index.md drift**: Many wikis have a separate `concepts/_index.md` listing concepts by category. Creating or enriching concept pages without updating this causes index drift. Always update BOTH `wiki/index.md` (main index) and any sub-index files (`concepts/_index.md`, `entities/_index.md` if they exist) when adding new pages.
- **New files invisible to `git add` after auto-commit**: If a cron job or auto-sync mechanism committed your new wiki files before your batch commit, `git status` won't show them and `git add` won't stage them. Verify with `git ls-files | grep <new-file-name>`. If the file shows as tracked but `git diff HEAD --stat` doesn't include it, it was already committed — just commit the remaining modifications.
- **Subagents need explicit absolute paths** — don't rely on HOME resolution
