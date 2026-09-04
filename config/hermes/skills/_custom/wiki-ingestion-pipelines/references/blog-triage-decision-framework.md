# Blog Triage Decision Framework

Practical decision-making process for evaluating blog articles during the blog-ingest → blog-triage → blog-wiki-ingest pipeline.

## Decision Flow

```
Read saved article → Check existing wiki coverage → Evaluate AI-relevance → Assign action
```

### Step 0: Check for Unsaved High-Value Articles

The ingest checkpoint JSON includes an `unsaved_articles[]` array — articles the pre-run script identified but failed to save to `wiki/raw/articles/`. Before triaging saved articles, scan `unsaved_articles` for high-value AI-relevant titles:

```python
# In the checkpoint JSON, check:
unsaved = checkpoint.get("unsaved_articles", [])
for a in unsaved:
    # Score by title keywords: AI, LLM, inference, agent, model, chip, OpenAI, Anthropic, etc.
    if is_ai_relevant(a["title"]):
        # Fetch with curl (add User-Agent header for openai.com, etc.)
        # Save to wiki/raw/articles/ with standard naming
        # Add to triage decisions as a take
```

**Concrete example (June 2026)**: The OpenAI/Broadcom Jalapeño chip announcement was in `unsaved_articles` — a ★★★★★ take that would have been missed without this check. Fetched via `curl -A "Mozilla/5.0..."`, saved, and processed as a take.

**Why this matters**: The pre-run script sometimes fails to save articles from blogs with Cloudflare protection (openai.com returns 403 without User-Agent), rate-limited feeds, or timeout issues. The `unsaved_articles` array is the safety net — always check it.

### Step 1: Read Saved Articles

Read each saved article's raw file (50+ lines) from `wiki/raw/articles/`. Focus on:
- **Title signals**: AI/LLM/agent keywords in title
- **Author signals**: Known AI commentators (Simon Willison, Ed Zitron, Cory Doctorow, etc.)
- **Blog signals**: Some blogs are consistently AI-relevant (simonwillison.net, wheresyoured.at), others are mixed (idiallo.com)

### Step 2: Check Existing Wiki Coverage

Before making take/reference/skip decisions, verify what's already covered:

```bash
# Check entity pages for the author/blog
search_files(pattern="author-slug|blog-slug", path="~/wiki/entities", target="files")

# Check concept pages for the topic
search_files(pattern="topic-keyword", path="~/wiki/concepts", target="files")

# Check log.md for recent processing of same source
search_files(pattern="blog-domain", path="~/wiki/log.md", target="content")
```

**Key check**: Does the article introduce NEW information not already in existing pages?
- If entity page exists but lacks this article's content → enrichment candidate
- If concept page exists but is thin → update candidate
- If no relevant page exists AND topic is AI-relevant → new page candidate

### Step 3: Evaluate AI-Relevance

**Direct AI relevance** (TAKE candidates):
- AI/LLM products, features, launches (OpenAI, Anthropic, Google, etc.)
- AI agent frameworks, sandboxing, security
- ML infrastructure (JAX, PyTorch, training, inference)
- AI industry economics, pricing, enterprise adoption
- AI safety, alignment, policy
- Coding agents, developer tools for AI
- Token economics, model routing, optimization

**Indirect AI relevance** (REFERENCE candidates):
- AI impact on open source (PR flooding, contribution gaming)
- AI-generated content commentary
- AI career/industry commentary with substance
- Philosophical essays on AI and humanity
- AI productivity metrics and measurement

**Not AI-relevant** (SKIP):
- General programming (non-AI)
- Security (non-AI-specific)
- General career advice without AI angle
- Light opinion pieces without depth
- Non-tech content

### Step 3b: Verify a "take" isn't already covered (full-pipeline / State D)

When doing the full-pipeline State D path (blog-ingest → triage → wiki-ingest in one session, no separate `triage_latest.json`), do NOT use `grep "2026-XX-XX" log.md` to check whether today's content is already wiki-covered. At the time blog-ingest runs (~10:00 UTC) the other same-day pipelines (newsletter-wiki-ingest, raw-backlog-ingest, sitemap-monitor) have usually NOT committed yet, so the log shows no same-day entries — a false negative. The reliable check is to read the actual target page bodies (the "Decision by Coverage Level" matrix in `references/blog-wiki-ingest.md`): open the candidate `concepts/` / `entities/` page and look for the article's specific claims/data in the body, not just a URL in `sources`.

### Step 4: Star Rating & Action Assignment

| Rating | Criteria | Action |
|--------|----------|--------|
| ★★★★★ | Major new tool/technique, comprehensive coverage, fills wiki gap | TAKE — create new concept page |
| ★★★★☆ | Significant update to existing entity/concept, strong AI relevance | TAKE — update existing pages |
| ★★★☆☆ | Good AI content, enriches existing coverage, solid reference | REFERENCE — note for future enrichment |
| ★★☆☆☆ | AI-adjacent but light depth, opinion without substance | SKIP |
| ★☆☆☆☆ | Not AI-relevant | SKIP |

### Step 5: Save Triage Checkpoint

Save JSON to `~/.hermes/cron/data/blog_ingest/triage_latest.json`:

```json
{
  "triage_timestamp": "ISO-8601",
  "run_id": "from ingest checkpoint",
  "source": "blog-ingest",
  "decisions": [
    {
      "title": "Article Title",
      "url": "https://...",
      "blog": "domain.com",
      "raw_path": "/opt/data/ai-topics/wiki/raw/articles/filename.md",
      "recommended_action": "take|reference|skip",
      "star_rating": 1-5,
      "reason": "Brief justification",
      "target_pages": ["entities/page-name", "concepts/page-name"]
    }
  ],
  "summary": {
    "total_decisions": 0,
    "takes": 0,
    "references": 0,
    "skips": 0,
    "key_themes": ["theme1", "theme2"]
  }
}
```

### Step 6: Process TAKE Articles

For each TAKE decision, process via parallel subagents (up to 3 concurrent):

**Batch strategy:**
- Group by update type: entity updates vs concept updates vs new pages
- Each subagent receives: article content, existing page content, exact insertion points
- Entity updates: add new section to existing entity page
- Concept updates: add subsection or cross-reference to existing concept page
- New pages: create new concept page with full content

**Subagent goal pattern:**
```
"Update the {entity/concept} page at /opt/data/ai-topics/wiki/{entities/concepts}/{name}.md 
to add information about {topic}. Read the file FIRST with read_file. Use patch to add 
content - DO NOT use write_file as the page is large ({N} lines). Add the new section 
after {existing section}. Bump the 'updated' date in frontmatter to {date}. Add 
{raw_article_path} to the sources list."
```

## Common Triage Patterns

### Pattern: Blog with mixed relevance (e.g., idiallo.com)
Some blogs post both AI and non-AI content. Read titles first, filter by keyword signals, only read full content for promising titles.

### Pattern: Series articles (e.g., "Hater's Guide to AI Bubble 3.0")
Check if previous installments are already in the wiki. If yes, the new version is an update to the existing entity page entry, not a new page.

### Pattern: Quote/link blog posts (e.g., Simon Willison link blog)
These are short — read the full content. The linked source may be more valuable than the blog post itself. Note the linked source for potential separate processing.

### Pattern: Multiple articles from same author
Group them for efficiency. Update the entity page once with all new content, not separately for each article.

## Pitfalls

- **Post-subagent index.md count verification (CRITICAL)**: After parallel subagents modify index.md, ALWAYS verify THREE things: (1) the top-level header count (`Total pages: N | Indexed entries: M | Concepts: X | Entities: Y`), (2) the section headers (`## Concepts (N pages)`, `## Entities (N pages)`), and (3) that the new entry actually appears in the correct alphabetical position. **Common failure mode observed June 2026**: Subagent adds the entry line to index.md but does NOT update any of the three counts — header, section header, or indexed entries. The parent must `grep -n "Total pages" index.md` and `grep -n "## Concepts" index.md` after every subagent batch and patch any stale counts before committing. This is distinct from the drift problem (counts mismatch each other) — it's a complete omission problem (counts never bumped at all). **Post-subagent verification checklist**: (1) `grep -n "Total pages" wiki/index.md` — header count correct? (2) `grep -n "## Concepts\|## Entities" wiki/index.md` — section counts correct? (3) `grep "new-page-slug" wiki/index.md` — entry present in correct position?
- **Paywalled content**: Some articles (wheresyoured.at premium) may be truncated. Use available content for triage; note if full content is needed for wiki update.
- **Duplicate detection**: Check `log.md` for same URL processed in previous runs before adding to triage decisions.
- **Entity page existence**: Don't assume entity pages exist for all blog authors. Some may only have skeleton pages from `build_x_wiki.py`.
- **Bot check pages saved as articles**: Some blogs use anti-bot protection (Anubis, Cloudflare challenge). The pre-run script may save the challenge page instead of actual content. Detection: file is very short (<500 bytes) and contains keywords like "Protected by", "Anubis", "Making sure you're not a bot", or "challenge". Action: skip the article — do not attempt to re-fetch (the bot protection will block the triage agent too). Note in triage decision with `raw_path: null` and reason "bot check page, not actual content".

- **Tag validation**: All new tags used in wiki updates must exist in SCHEMA.md. Check before committing.
- **`execute_code` blocked in cron mode**: When running as a cron job, `execute_code` is blocked (cron jobs run without a user present to approve). Use `write_file` to create the triage checkpoint JSON instead of building it programmatically with `execute_code`. This applies to Step 5 (Save Triage Checkpoint) — construct the JSON string directly and write it via `write_file` to `~/.hermes/cron/data/blog_ingest/triage_latest.json`.
