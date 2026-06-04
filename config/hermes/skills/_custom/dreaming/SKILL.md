---
name: dreaming
description: Knowledge consolidation cycle that analyzes collected articles and updates the wiki with significant findings while enforcing duplicate checks.
category: research
version: 2.0.0
author: Hermes Agent
---

# Dreaming — Knowledge Consolidation Cycle

Automated consolidation process that analyzes recently collected articles and folds significant findings into the wiki knowledge base. Includes mandatory duplicate-check against adjacent scheduled jobs.

Based on the "context substrate" philosophy (Camp 2, per @witcheer 2026-04-16): memory isn't fact storage, it's structured context that compounds over time. Camp 2 tools solve compounding via read-context→work→write-back loops. This dreaming cycle follows Camp 2: wiki files are the source of truth, not hidden vector state.

## Architecture

### Pipeline

**Phase 1: Data Collection** (pre-run script)
- Script: `~/ai-topics/scripts/dreaming.py`
- Collects RSS scan articles, newsletter articles, existing wiki pages
- Outputs structured JSON to stdout
- Injected into cron prompt as context

**Phase 2: Knowledge Consolidation** (LLM processing)
- Runs on the configured cron schedule
- Receives collected data via prompt injection
- Analyzes, creates/updates wiki pages
- Commits changes to git

## Step 0: Duplicate Check (MANDATORY — runs first every time)
Before processing, review what adjacent scheduled jobs have already completed:
1. **Daily Inbox Update (23:00 JST)** — RSS scan + Newsletter triage + Wiki ingest
2. **Daily Wiki Update Report (20:00 JST)** — Wiki update summary
3. **Daily Active Knowledge Crawl (00:00 JST)** — Hot topic concept discovery
4. **Skill Inventory Check (01:00 JST)** — New skill assessment

Duplicate-check rules:
- If an article was already processed by Daily Inbox Update, do NOT re-process it
- If a concept page was already created by Daily Active Knowledge Crawl, do NOT duplicate — only enrich if you have significant new insights
- If a skill was already assessed by Skill Inventory Check, reference that assessment rather than re-doing it
- If a wiki page was already updated and reported by Daily Wiki Update Report, skip redundant updates
- Only proceed with wiki consolidation for items NOT already handled by adjacent scheduled jobs
- If you find gaps or missed items from other jobs, fill them and note it in the report

## Dream Cycle Phases

### 1. Light Sleep — Screening & Grouping
- Review articles NOT already processed by adjacent scheduled jobs
- Group by semantic themes (shared entities, related concepts, events)
- Identify recurring patterns across multiple sources
- Flag articles that appear in multiple sources (higher significance)

### 2. REM — Flat Synthesis (Writer Phase A: unbiased consolidation)
Score each theme/group using weighted signals **WITHOUT newsjacking bias**:
- **relevance (0.30)**: Direct AI/LLM/agent relevance
- **frequency (0.25)**: Number of mentions across sources
- **query_diversity (0.15)**: Different sources discussing similar concepts
- **recency (0.15)**: How recent the discussion is
- **consolidation (0.10)**: How well it fits existing knowledge
- **conceptual_richness (0.05)**: Depth and novelty of insights

Promotion thresholds:
- Score ≥ 0.65: Create or update wiki page
- Score 0.45-0.65: Add to existing page or log for review
- Score < 0.45: Skip (minor mention)

**CRITICAL**: This phase is for knowledge consolidation, not distribution selection.
Do NOT apply newsjacking filtering here — capture everything that meets the threshold.

### 3. NJ Delivery Filter (Writer Phase B: distribution selection)
After flat synthesis, apply Newsjacking lens to select what to **deliver/report**:

**Newsjacking Signal Scoring (0-5):**
- 5/5: Trending topic + contrarian take + high debate potential (e.g., "X is dead" backed by data)
- 4/5: Riding viral wave + in-group resonance (e.g., Claude Code patterns, local LLM breakthroughs)
- 3/5: Pattern interrupt + novelty (unusual topic from trusted source)
- 2/5: Standard insight, well-executed but not debate-generating
- 1/5: Incremental update, low engagement potential
- 0/5: Noise, link dump, or already saturated topic

**Delivery prioritization**:
- NJ Score ≥ 4: **Lead story** — featured prominently in report, detailed analysis
- NJ Score 3: **Secondary** — included with context and cross-references
- NJ Score 2: **Brief mention** — one-liner in summary section
- NJ Score ≤ 1: **Omit from delivery** — wiki updated but not highlighted in report

This two-stage approach ensures:
1. Wiki receives comprehensive, unbiased knowledge consolidation (Phase A)
2. Reports are curated for maximum engagement and signal (Phase B)

### 3. Deep Sleep — Replay-Safe Integration
For each promoted theme:
1. **Check existing pages**: Search wiki for related content
2. **Create new pages** if significant enough:
   - Follow wiki format: frontmatter + content + cross-references
   - Link to at least 2 existing pages
   - Add to appropriate category (entities, concepts, comparisons, queries)
3. **Update existing pages** with new information:
   - Append new findings with dates
   - Note contradictions if present
   - Bump `updated` date in frontmatter
4. **Update navigation**:
   - Add new pages to `wiki/index.md`
   - Update total page count
   - Append to `wiki/log.md`
5. **Git commit & push**: `cd ~/ai-topics && git add wiki/ && git commit -m "dreaming: consolidation YYYY-MM-DD" && git push`

## Workflow

### Cron Job Configuration
```yaml
name: Dreaming
schedule: "<configured cron schedule>"
script: dreaming.py
skill: dreaming
deliver: "discord:1233771389367095377:1491801814222504169"
```

## Output Format

After processing, deliver a summary like:

```
# Dreaming Report — YYYY-MM-DD

## Duplicate Check Summary
- Items skipped (already processed by other jobs): N
- Gaps filled: N
- Overlapping areas identified: [list]

## Consolidation Summary
- Articles processed: N
- Themes identified: N
- Pages created: N
- Pages updated: N

## New Wiki Pages
- [[concepts/new-page]]: Brief description

## Updated Pages
- [[entities/existing]]: What changed
```

## Sub-Patterns

### Pattern A (CORE): Existing Coverage Depth Check

After Phase A identifies themes meeting the promotion threshold (score ≥ 0.65), **do NOT automatically create/update wiki pages**. First perform a depth check:

1. **Read the existing page(s)** in full — not just check their existence
2. **Assess coverage depth**: Does the existing page already cover the theme's core insight? Compare against the dreaming theme's summary
3. **Search for raw articles** on disk (`~/wiki/raw/articles/`) matching the theme's URLs or titles to see if content was already ingested
4. **Only update if there are genuine gaps** — don't update "because the threshold says so"
5. **Document in the report** why each high-scoring theme was skipped (e.g., "Already covered comprehensively" vs "Minor detail gap filled")

Rationale: The dreaming checkpoint aggregates articles across 2+ day windows. By the time the dreaming cycle runs, the daily RSS pipeline or newsletter-ingest may have already processed many of these articles. The wiki's existing pages may already reflect the key insights.

### Pattern B (NEWSLETTER): Newsletter Noise Filtering
When processing articles from newsletters (substack, beehiiv, etc.), apply these filters BEFORE scoring:

| Signal Type | Pattern | Action |
|-------------|---------|--------|
| Substack UI | `play_audio=`, `post-comment`, `submitLike=`, `share=`, `redirect/app-store` | Skip |
| Substack UI | `utm_campaign=email-read-in-app`, `@username` mentions | Skip |
| Redirect chains | `substack.com/redirect/UUID` | Try web_extract or skip if no body |
| Beehiiv tracking | `link.mail.beehiiv.com/v1/c/...` | Extract destination via web_extract |
| Duplicate URLs | Same raw_article_path appearing multiple times | Deduplicate — process once |

### Pattern C (ENTITY): Batch Entity Discovery
When articles reference recurring people/companies without dedicated entity pages:

1. **Search existing entities first**: `search_files "name" path=~/wiki/entities target=files`
2. **Check index.md slug_lookup**: Verify if entity already catalogued under different name
3. **Create entity page** if missing: Use standard frontmatter (title, created, updated, tags, related, sources)
4. **Minimum entity page content**: Role/affiliation, key contributions, timeline highlights, 2+ cross-references, sources list
5. **Batch commit**: Create all new entity pages first, then update index.md/log.md in a single commit

### Pattern D (DEDUP): Duplicate Detection Matrix
Before creating or updating any page, check ALL sources:

| Check | Method | What it catches |
|-------|--------|-----------------|
| Filename | `search_files "name" path=~/wiki/entities` | Exact matches |
| Index entry | Read `wiki/index.md` slug_lookup | Catalogued under different name |
| Content grep | `search_files "name" target=content path=~/wiki` | Mentioned inside other pages |
| Recent sessions | `session_search "name"` | Processed in previous dreaming cycles |

## Pitfalls
1. **Duplicate detection is MANDATORY** — never re-process what other jobs handled
2. **Don't create pages for everything** — follow the scoring thresholds
3. **Always check existing pages first** — avoid duplicates
4. **Cross-references are mandatory** — isolated pages are useless
5. **Commit in the same session** — don't leave changes uncommitted
6. **Report what changed** — user needs to know what happened
7. **Handle contradictions explicitly** — don't silently overwrite
8. **Keep pages scannable** — split if over 200 lines
9. **Update index.md and log.md** — navigation backbone
10. **Database Schema Constraints**: `blogwatcher-cli.db` articles table uses `published_date` or `discovered_date`, `is_read` is integer 0/1, `categories` is JSON array
11. **Script Execution**: `dreaming.py` outputs JSON to stdout. If it times out, cron still fires but with missing context
12. **Pre-run Script JSON Parse Failure**: When the pre-run script outputs `{"ok": false, "error": "failed to parse JSON response from dreaming-group output"}`, the grouped themes are still available as a fallback at `/opt/data/.hermes/cron/data/dreaming/grouped_themes_latest.json`. Read this file directly to extract themes, articles, and run metadata. The checkpoint data is valid even when `ok` is false — it contains the same structure as a successful run. Do NOT stop processing; extract themes from the fallback file and proceed.

13. **Stale Dreaming Themes**: The dreaming checkpoint may be 2-3 days old by the time the cycle runs. Themes identified in the checkpoint may have been processed by the daily RSS pipeline, newsletter-ingest, or other adjacent jobs in the interim. Cross-reference raw article file dates (`~/wiki/raw/articles/`) and recent `log.md` entries to avoid re-processing. If a theme's key article was already fetched and corresponded to an existing wiki page with adequate coverage, skip the update.

14. **Log.md Corruption via Patch**: When using `patch` on `log.md`, the `read_file` output format (`LINE|content`) can cause accidental `|` prefix insertion. This happens because the patch `old_string` may include a pipe character from the read_file separator. **Fix**: Always verify log.md formatting after patching by re-reading the file. If `||-` appears instead of `-` at the start of a bullet line, run a corrective patch. To prevent: when reading log.md, mentally subtract the `LINE|` prefix before constructing old_string values.
