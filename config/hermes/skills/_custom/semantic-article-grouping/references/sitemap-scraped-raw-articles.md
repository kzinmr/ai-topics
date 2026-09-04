# Sitemap-Scraped Raw Articles: Characteristics and Triage Patterns

**Observed**: June 2026 dreaming-group triage of 40 raw articles from June 3-4.

## Naming Convention

Sitemap-scraped articles follow a consistent pattern:
```
YYYY-MM-DD_{company-slug}_{article-slug}.md
```
Examples:
- `2026-06-04_fireworks-ai_open-source-agents-frontier-advisors.md`
- `2026-06-04_harvey_for-iain-telford-ai-success-depends-on-people.md`
- `2026-06-04_elevenlabs_ebury.md`
- `2026-06-04_hex-technologies_etl-pipeline.md`

These arrive via the `sitemap-monitor` cron job (06:00 UTC) which scrapes company blog sitemaps.

## Content Quality Distribution

Sitemap-scraped articles from company blogs have a **very low wiki-value yield** (~2-5% take rate). Typical composition of a 40-article batch:

| Category | % | Action |
|----------|---|--------|
| Enterprise marketing / product features | 60-70% | Skip |
| Customer case studies | 15-20% | Skip |
| Already captured by prior pipelines | 10-15% | Skip |
| Genuinely new technical content | 2-5% | Take/Reference |

## Contentless Large Files Pitfall

**Sitemap scrapes frequently produce files with no actual article body.** The file may be 10-20KB but contain only:
- Navigation chrome (menu items, breadcrumbs, footer links)
- Repeated CTA buttons ("Request a Demo", "Learn More", "Get Started")
- Cookie consent banners
- Related article lists
- No article text whatsoever

**Example**: `2026-06-04_glean_introducing-glean-mcp-gateway.md` — 445 lines, 17KB, but zero article content. The entire file was Glean's site navigation repeated twice.

**Detection**: Read the first 50 lines. If you see repeated product navigation, department lists, or "Sign in / Get a Demo" patterns with no paragraph text, the article body was not extracted. Skip with reason: "Sitemap scrape extracted navigation chrome only, no article body."

## Stub-Take Re-Fetch Pitfall (Sitemap Article With Summary But No Body)

**Distinct from the "too small to skip" case above.** A sitemap article can be a **thin but substantive extract** — short (24 lines / ~800B), frontmatter + title + author + a one-sentence summary that contains real claims (e.g. "58% cost cut without lowering quality"). The upstream dreaming-group (or blog-triage) will mark it a **★★★★★/★★★★☆ take** because the summary is promising, but the raw file has **no article body** — only the summary line.

**Concrete case (2026-08-25)**: `2026-08-25_factory_model-routing-belongs-in-the-harness.md` was 24 lines / 794B. The body was a single summary sentence: "Droid's model routing cut cost 58% without lowering quality. Only the harness can judge when a model switch is worth the cache miss..." The dreaming-group's triage rated it ★★★★★ with specific claims (58%, cache-miss judgment, feedback loop). Enriching `concepts/coding-agents/model-routing.md` **from that stub alone would have produced a thin, uncited entry with no supportable detail.**

**Fix — re-fetch the full article before enriching a stub take:**
1. After reading the raw file, if it is **< ~50 lines** or the body is **only a summary sentence** (no paragraphs, no section headings), treat it as a **stub extract**, not a full article.
2. Re-fetch the canonical URL from the frontmatter `url:` field via a `/tmp/` Python script (`urllib.request` + regex `<p>` extraction — the cron-safe pattern from the `daily-rss-triage` skill). For `factory.com`, a simple `urllib` GET + `<p>`-tag strip returned the full 8-minute article.
3. **Verify the triage's specific claims against the fetched body** before writing (the "58%" may be a rounded/paraphrased number; the fetched article gave the precise "58% aggregate, 76% median session, 2.12× at turns 61–150").
4. Enrich the wiki page from the **fetched full text**, citing the canonical URL + the raw article basename in `sources`.

**Why this matters**: The Deep Sleep verification gate ("read the article body") is only meaningful if the body is actually present. A stub extract silently passes the "read the body" check because the body *is* the summary — the gate gives false confidence. The discriminator is **line count / body depth**, not just "does a file exist".

**Heuristic for "is this a stub?"**: raw file < ~50 lines AND no section headings in the body AND the entire post-frontmatter content is one paragraph → re-fetch. If the file is 100+ lines with section structure, it's a full extract and no re-fetch is needed (the Harvey/ElevenLabs cases this session were 194–340 lines and enriched directly).

## High-Volume Company Blog Sources

These companies publish frequently via sitemap and typically produce low-wiki-value content:

| Company | Typical Content | Usual Action |
|---------|----------------|--------------|
| Harvey (harvey.ai) | Legal workflow guides, customer stories, product features | Skip unless new technical benchmark data |
| ElevenLabs (elevenlabs.io) | Customer stories (ElevenAgents Stories, ElevenCreative Stories) | Skip unless new architecture/capability |
| Hex Technologies (hex.tech) | Data analytics guides, ETL tutorials | Skip (content marketing) |
| Glean (glean.com) | Enterprise AI platform features, chatbot guides | Skip unless new MCP/integration architecture |
| Pinecone (pinecone.io) | Vector DB use cases, integration guides | Skip unless new benchmark/architecture data |
| Factory (factory.ai) | Product feature snippets (often <1KB) | Skip — too small for wiki value |
| Cohere (cohere.com) | Product announcements, partnership news | Skip unless new model/architecture details |

**Factory pitfall**: Factory blog articles via sitemap are frequently **extremely small** (500-600B) — just a product feature name and one-liner. These fail the body-reading mandate (no substantive body to assess). Skip with "too small for wiki value."

**Exception**: When these companies publish benchmark data, architecture details, or integration specifications (e.g., Fireworks AI's LAB harness engineering results), the content is wiki-worthy regardless of source.

**Fireworks AI exception (June 2026)**: Two sitemap articles from Fireworks were genuine enrichment takes:
1. "Frontier-lab training infrastructure as a service" — zero-KLD train/serve alignment, batch invariance for large MoEs, DeepSeek DeepGEMM integration (14KB)
2. "Open-source worker + closed-source advisor" — GLM 5.2 + Opus 4.8 benchmark data: SWE-bench Pro +7pp, Terminal-Bench +4pp, Legal Agent Benchmark +4pp (11KB)

Both enriched `entities/fireworks-ai.md` which already had a Hybrid Harness section but lacked these specific technical details. Key lesson: even when the entity page covers the broader topic, sitemap articles can contain specific benchmark data or architecture details that represent genuine wiki gaps.

## Yield Expectations for Dreaming-Group (Sitemap-Heavy Batches)

When the dreaming-group checkpoint is in 0-article recovery mode and scans recent raw articles:

- **40 sitemap articles** → expect 1-3 takes, 1-2 references, 35-38 skips
- **200+ raw articles** (mixed sitemap + RSS + newsletter + X bookmarks) → expect 3-8 takes, 3-8 references, rest skip
- **281 raw articles (June 2026 validated)** → 4 takes, 7 references, 20 skips (after removing ~240 already processed by other pipelines). The 0-article recovery mode's primary value is catching **late-arriving sitemap articles** with genuine technical content that other pipelines missed and **entity page enrichment opportunities** that the blog pipeline's 5% take rate missed

## Cross-Pipeline Dedup for Sitemap Articles

Sitemap articles may overlap with:
1. **Blog-ingest pipeline** (RSS-based) — same article may arrive via RSS feed earlier
2. **Newsletter pipeline** — the same company blog post may be linked from a newsletter
3. **Active-crawl pipeline** — hot-topics.yaml may target the same company

Always check `wiki/log.md` for same-day processing before triaging sitemap articles. The blog-ingest pipeline (07:00 UTC) typically runs before sitemap-monitor (06:00 UTC) delivers to dreaming-group (18:00 UTC), so most genuinely valuable content is already captured.

## Cross-Reference Technique for Sitemap Articles

When checking if sitemap articles are already wiki-processed, use `grep -rl` for reliable filename-content matching:

```bash
# Check if article topic is in any wiki page
grep -rl "fireworks-ai\|zero-KLD\|batch invariance" ~/wiki/entities/ ~/wiki/concepts/ 2>/dev/null

# Check entity page for specific content
grep -n "GLM 5.2\|Opus 4.8\|SWE-bench Pro" ~/wiki/entities/fireworks-ai.md 2>/dev/null
```

**Why `grep -rl` over `search_files`**: The `search_files` tool with `target='files'` searches file *content* using regex, not filenames. Plain keywords work but glob-like patterns (`*keyword*`) fail. For true filename matching, use `find ~/wiki/entities -name "*keyword*"` in terminal.

**Entity page gap detection**: If the entity page exists but lacks the article's specific technical details (benchmark numbers, architecture patterns), it's a genuine enrichment opportunity even though the entity covers the broader topic. Always read the entity page's actual content sections — don't assume "entity page exists for company X" means "article about company X is already covered."

## Content Structure: Navigation Chrome

Sitemap-scraped articles typically have 30-40 lines of navigation chrome before article content:
- Lines 1-8: YAML frontmatter
- Lines 9-13: Source URL, title
- Lines 14-40: Navigation chrome (menus, CTAs, breadcrumbs)
- Lines 41+: Article body content (if extracted)

Start reading at line 40+. If lines 40-100 are still navigation chrome, the article body was not extracted — skip.
