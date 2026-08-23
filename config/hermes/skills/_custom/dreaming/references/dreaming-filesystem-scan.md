# Filesystem Scan for Enrichment Candidates

## When to Use
Checkpoint has `total_articles: 0` but `recent_raw_articles > 0`. The collect step found nothing from RSS/newsletter pipelines, but raw articles exist on disk from sitemap-monitor (06:00 UTC) and other pipelines.

## Validated Pattern (July 2026)

### Session 1: July 4, 2026 (original)
97 files in last 3 days. Found 2 enrichment candidates:
- Safari MCP server (★★★★★, Apple's first MCP entry) — page didn't exist
- Anthropic Fable 5 redeployment (★★★★☆, specific usage limits not in wiki)

### Session 2: July 5, 2026 (saturation + carry-forward)
176 raw articles on disk, 0 from pipeline. Prior 07/04 triage unconsumed.

**Same-day pipeline speed observed**: raw-backlog-ingest created 4 new concept pages on the same day:
- `concepts/better-models-worse-tools.md` (Armin Ronacher, 129 lines)
- `concepts/short-leash-ai-coding.md` (okTurtles, 75 lines)
- `concepts/ai-benchmarks/senior-swe-bench.md` (Snorkel AI, 105 lines)
- `concepts/pxpipe-code-to-image-cost-reduction.md` (teamchong, 90 lines)

Blog-wiki-ingest also updated `entities/simon-willison.md` with sqlite-utils Fable article.

**Cross-pipeline depth check result**: Prior 07/04 takes (Safari MCP, CurrentAI) were verified — Safari MCP page still didn't exist, CurrentAI still a stub. Both confirmed as takes. All other recent articles already captured by daily pipelines.

**Final triage**: Takes=2, Refs=5, Skips=5. Archive: 10 candidates, 3 new archived, 7 dedup'd.

### Session 3: July 17, 2026 (saturation, fresh triage)
193 raw articles on disk, 0 from pipeline. Prior triage had 11 decisions (10 skip, 1 reference from earlier cycle). Blog-wiki-ingest and newsletter-wiki-ingest both ran same day (Kimi K3, simonwillison updates). Active-crawl created 4 concept pages (ai-voice-fraud, gemini-notebook, llm-text-detection, soofi-s).

**Filesystem scan**: 30 recent files from Jul 15-17 scanned. Found 5 genuine references:
- Fireworks Series D ($1.5B, $17.5B valuation, $1B ARR) — entity page had zero funding data
- Pinecone Sparse V3 (term-major layout, 151× I/O reduction) — entity page had no V3 mention
- Pinecone Text Match Filters (lexical scoping for agents) — entity page had no FTS mention
- ElevenLabs Interaction Models (voice AI conversation architecture) — entity page had voice agent eval but not interaction model concept
- Harvey Benchmark acquisition ($100M+ Q2 ARR, 3rd acquisition) — entity page had LAB benchmark but not acquisition

**Already covered by same-day pipelines**: GPT-Red, Agentty, OpenWiki 0.2 OKF, Inkling/Modal DFlash, Cerebras Knowledge Base, Sierra Pinecone agent

**Batch entity coverage check technique**: Used `grep -l "EntityName" ~/ai-topics/wiki/entities/*.md` to quickly identify which entity pages exist, then `grep -i "specific-detail"` to check content depth. 4 grep calls instead of 12+ individual searches.

**Final triage**: Takes=0, Refs=5, Skips=14. Yield: ~17% reference rate from sitemap-heavy batches.

**Same-day pipeline saturation pattern**: By 18:00 UTC, all AI-relevant content from the day was already processed by blog-ingest (07:00), newsletter-ingest (07:10), active-crawl (11:00), and x-bookmarks (11:30). Dreaming's value was identifying entity page enrichment opportunities that the daily pipelines missed (funding data, technical features, acquisition milestones).

## Workflow

### Discovery
1. `ls -lt ~/wiki/raw/articles/ | head -15` — focus on files from today's date
2. `find ~/wiki/raw/articles -mtime -2 -type f | wc -l` — count recent files

### Prior Triage Recovery
1. Check if `triage_latest.json` exists: `read_file` first 5 lines
2. Check if consumed: `grep "Dreaming wiki-ingest\|dreaming.*consolidation" wiki/log.md | head -5`
3. If unconsumed → carry forward takes after cross-pipeline depth check
4. If consumed → create fresh triage from filesystem scan only

### Cross-Pipeline Depth Check (for carry-forward takes)
For each prior take, verify across ALL pipelines:
1. `find ~/ai-topics/wiki -name "*candidate_slug*" -type f 2>/dev/null`
2. If page exists → read `created` date and content sections
3. If created by daily pipeline after prior triage but with adequate coverage → downgrade
4. If still stub or missing → keep as take

### Coverage Check (for new filesystem articles)
For each AI-relevant file:
1. Read first 30-50 lines (title, frontmatter, opening)
2. **Batch entity check** (preferred for 3+ articles): `grep -l "EntityName" ~/ai-topics/wiki/entities/*.md` to identify which pages exist, then `grep -i "specific-detail" path/to/entity.md` to check content depth. This is faster than individual `search_files` calls.
3. **Individual check** (fallback): `grep -ri "topic-keyword" ~/ai-topics/wiki/concepts/ ~/ai-topics/wiki/entities/ | head -5`
4. If page exists → read the relevant section to check for specific detail gaps

### Consolidation Pattern
1. Prior unconsumed takes come FIRST (with fresh checkpoint_run_id)
2. Filesystem scan findings come AFTER
3. Batch skips by topic (non-AI, already-processed, prior-processed)
4. Save to `triage_latest.json` with current checkpoint_run_id
5. Run `archive_triage.py dreaming --keep-reference` AFTER all decisions finalized

## Source Field Normalization
Use `"dreaming"` for ALL articles triaged by the dreaming cycle, regardless of original pipeline. Do NOT use `"filesystem_scan"`, `"blog"`, or `"newsletter"`.

### Session 4: August 4, 2026 (full saturation, Takes=0)
205 raw articles on disk, 0 from pipeline. **All daily pipelines ran before dreaming**: blog-wiki-ingest (4 takes + 5 refs), newsletter-wiki-ingest (4 takes + 4 refs), active-crawl (3 new + 1 enrich), raw-backlog-ingest (3 rounds, 6 entity enrichments), X bookmarks ingest (Kimi K3 AMD MI355X), manual ingest (Gary Marcus Astra).

**Prior triage (Aug 3)**: 15 decisions (0 takes, 2 refs, 13 skips). Both refs already covered — Together AI autoscaling (entities/together-ai.md, Inference-Native Autoscaling section) and Browserbase harness (entities/browserbase.md, three-layer architecture + sources frontmatter).

**Filesystem scan**: 19 articles evaluated from Aug 4 sitemap batch + blog batch. 1 genuine reference found:
- **Warp software factory part 4** (computer use verification) — entity page had parts 1-3 but NOT part 4. Article adds verify-behavior skill (reproduce/verify modes), triage/implementation/review integration, cloud subagent fan-out, spec-driven debug loop.

**Already covered by same-day pipelines**: Micah Lee agentic coding (blog-wiki-ingest), WorkOS MCP vs REST (blog-wiki-ingest → concepts/mcp.md), OpenAI Astra (manual ingest), Qwen 3.8 (newsletter-wiki-ingest + active-crawl), Kimi K3 (X bookmarks + newsletter), Dwarkesh compute paradox (active-crawl).

**Thin sitemap article skip**: Factory AI "enterprise organization model" — 783 bytes / 26 lines, frontmatter + title only, no article body extracted. Consistent with known Factory sitemap pattern (see `sitemap-scraped-raw-articles.md` Factory pitfall). Skip with "no body to assess."

**Final triage**: Takes=0, Refs=1, Skips=19. Archive: 20 candidates, 12 new archived, 8 dedup'd. Total: 2,272 URLs.

**Lesson**: When all 6+ daily pipelines run before dreaming (07:00-18:00 UTC window complete), Takes=0 with 0-1 references is the expected outcome. Dreaming's value shifts to: (a) confirming prior triage completeness, (b) catching 1-2 entity enrichment gaps from sitemap batches, (c) archiving decisions for dedup.

## Expected Yield
| Scenario | Takes | References | Skips |
|----------|-------|------------|-------|
| Fresh scan (no prior triage) | 0-2 | 2-5 | 10-15 |
| Carry-forward + scan | 1-3 | 3-6 | 8-12 |
| Full saturation (all pipelines ran) | 0-1 | 0-2 | 15-20 |
| Sitemap-heavy batch (30 files) | 0 | 5 | 14+ |

## Common Pitfalls
- Don't scan all 200+ raw articles — focus on top 10-15 most recent
- Skip non-AI content immediately
- Check entity page `sources` frontmatter for prior captures
- `candidate_wiki_path` verification: `find` before assigning
- Source field must be `"dreaming"` (not `"filesystem_scan"`)
- Cross-pipeline depth check is mandatory for carry-forward takes
- raw-backlog-ingest runs 6×/day and can create concept pages between triage runs
