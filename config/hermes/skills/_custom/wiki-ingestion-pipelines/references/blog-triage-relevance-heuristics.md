# Blog Triage Relevance Heuristics

Decision framework for determining which blog articles from the RSS ingest are worth wiki page updates vs. raw-save-only. Developed from repeated blog-triage sessions.

## Triage Decision Tree

For each article from the blog-ingest checkpoint:

### 1. Source Signal Weight (who wrote it?)

| Source Tier | Examples | Bias |
|-------------|----------|------|
| **Tier 1 — AI thought leaders** | Simon Willison, geohot, Andrej Karpathy, swyx | Almost always worth triage; even "link blog" posts reveal market dynamics |
| **Tier 2 — Tech commentators with AI coverage** | Daring Fireball (Gruber), John Gruber, lcamtuf | Worth scanning; AI content is intermittent but often high-signal |
| **Tier 3 — Domain blogs** | John Cook (math), Jim Nielsen (design), Terence Eden (travel) | Skip unless directly AI-relevant; save as raw only |

### 2. Content Relevance Filter

**Wiki-worthy (create/update pages):**
- New substantive information about an existing wiki entity or concept
- Market dynamics / competitive positioning between tracked products (e.g., Fable vs GPT-5.6)
- New product capabilities, usage metrics, or pricing changes
- First-person takes from AI practitioners on LLM usage patterns
- Cross-entity competitive intelligence (e.g., OpenAI removing usage limits pressures Anthropic)

**Raw-save only (no wiki action):**
- Tool version releases (shot-scraper 1.11, sqlite-utils 4.1.1) — unless major feature
- Organizational theory / management concepts (DRI) — unless directly about AI agent governance
- Domain-specific content from non-AI blogs (travel, cooking, hardware)
- Paywalled content with no extractable substance

### 3. Wiki Page Action Type

| Article Content | Action |
|----------------|--------|
| New info about existing entity | `patch` entity page — see `references/blog-triage-entity-enrichment-pattern.md` for the 6-step workflow |
| New market dynamics between tracked products | `patch` both entity pages + relevant concept page |
| New concept not yet in wiki | Consider creating concept page if >2 independent sources |
| Analytical essay describing systemic pattern | Create concept page — see `references/concept-page-from-analytical-essay.md` for template |
| Tool release with AI implications | `patch` tool entity page if exists; otherwise raw-save |
| Quote-post revealing author's AI philosophy | `patch` author entity page |

### 4. Common Patterns from Simon Willison's Blog

Willison's link blog posts are the single highest-yield source for wiki updates. His post structure:
- **Tool release posts** (shot-scraper, sqlite-utils, datasette) — usually raw-save only
- **"Bump" / competitive dynamics posts** — wiki-worthy, updates multiple pages
- **Quote posts with AI commentary** — patch the quoted person's entity page
- **Directly AI posts** (LLM coding, agent engineering) — always wiki-worthy

### 5. Batch Triage Workflow

```
1. Read checkpoint JSON from blog-ingest
2. For each article:
   a. Check source tier (Tier 1 → always read; Tier 2/3 → scan title)
   b. Read raw article if Tier 1 or title suggests AI relevance
   c. Check wiki/index.md for existing entity/concept pages
   d. ALSO check if the SOURCE (blog author) has an existing entity page
      → If yes and article is substantive: use entity enrichment pattern
         (see references/blog-triage-entity-enrichment-pattern.md)
   e. Decide: skip | raw-save-only | wiki-update | entity-enrich
3. For wiki-update articles:
   a. Read existing page(s) before patching
   b. Patch with new information (never overwrite rich pages)
   c. Update `updated` date, add source link
4. For entity-enrich articles (post from tracked author):
   a. Follow 6-step pattern: bump date → add source → timeline entry →
      detailed section → update themes → cross-link
   b. See references/blog-triage-entity-enrichment-pattern.md
5. Commit all changes in single git commit
6. Update log.md with triage summary
```

## Pitfalls

- **Over-triaging non-AI content**: A math blog post about Bayesian statistics is NOT AI-relevant just because ML uses Bayes. The threshold is "does this change our understanding of an AI entity, concept, or market?"
- **Under-triaging link blog posts**: Simon Willison's one-liner about Fable access extensions revealed competitive dynamics worth 3 wiki page updates. Don't skip link posts from Tier 1 sources.
- **Creating pages for single-source concepts**: Don't create a new concept page from a single blog post. Wait for corroborating sources unless it's a major product launch.
- **Missing cross-entity updates**: When an article mentions multiple tracked entities (e.g., "OpenAI removing limits pressures Anthropic"), update ALL relevant pages, not just the primary subject.
- **`execute_code` blocked in cron mode**: When blog-triage runs as a cron job, `execute_code` is blocked with `BLOCKED: execute_code runs arbitrary local Python`. Use individual `patch` tool calls instead. Do not try to batch patches in a Python script — call `patch` sequentially for each edit.
- **Stale spec fields in concept pages**: When a developer guide or update article contradicts an existing wiki page (e.g., "reasoning_effort: max-only" vs actual "low/high/max"), update the spec table AND any prose that references the old value (caveats, pelican benchmark notes, etc.). Search the full page for all mentions of the outdated detail.
- **Log entry as final step before commit**: Always add the log.md entry as the last wiki edit before `git add + commit + push`. This keeps the log accurately reflecting all changes in the batch.
- **Non-unique `patch` strings in large files**: Entity pages with many entries (e.g., Simon Willison at 780+ lines) will have repeated patterns like `Source: [[raw/articles/...]]`. The `patch` tool requires a unique match. **Fix**: re-read the target section with `read_file(offset=N, limit=30)` to find unique surrounding context (e.g., the preceding entry's last line + the target line). Never assume a `Source:` line is unique in a 500+ line file.
- **Sibling subagent file modification warnings**: When `patch` warns `"was modified by sibling subagent"`, this is informational — `patch` operations are additive and don't conflict with sibling edits to different sections. Safe to proceed. However, `write_file` would overwrite sibling changes, so always `read_file` before `write_file` in multi-agent contexts.
- **Multi-article same-entity batching**: When multiple articles in the same triage batch update the same entity page (e.g., 5 Willison posts → `entities/simon-willison.md`), batch all patches to that file in sequence rather than reading the file separately for each article. Read once, patch multiple times. The `patch` tool handles sequential edits correctly.
- **Event page creation for significant incidents**: When a batch contains multiple articles about the same incident (e.g., AISI unsanctioned behaviour + Irregular misconfiguration + Meta cyberattack), create a dedicated `events/` page for the incident and cross-reference it from all related entity/concept pages. This is more valuable than scattering incident details across entity pages.
- **Title mismatch between RSS and article content**: Some articles have different titles in the RSS feed vs the actual article (e.g., RSS says "Shawn Smucker: 'Please Use AI'" but article is titled "The Courage to Live It"). Use the article's actual title for the wiki, not the RSS title.
