---
name: wiki-daily-report
description: Generate a Japanese-language daily wiki change report summarizing today's modifications. Handles the case where wiki_report.py doesn't exist by using find-based fallback.
version: 1.1.0
author: Hermes Agent
tags: [wiki, report, cron, japanese]
category: wiki
---

# Wiki Daily Report

## Description

Generate a Japanese Discord-format daily wiki change report. Leads with high-newsjacking-signal stories (NJ ≥ 4), then lists all changes sorted by NJ score, ending with stats.

## Prerequisites

- Wiki at `~/wiki/` (resolves to `~/ai-topics/wiki/`)
- Log files: `wiki/log.md` or `wiki/log-2026.md`

## Primary Approach: Read log.md (Most Efficient)

The upstream cron jobs (newsletter-ingest, blog-ingest, active-crawl) write detailed structured entries to `wiki/log.md`. **This is the best source of change data** — far more efficient than file-system discovery.

### Step 1: Extract Today's log.md Entries

```bash
# Find all section lines for today's date
grep -n '^## \[' ~/ai-topics/wiki/log.md | grep "$TODAY"

# Read the full log entry sections for today (adjust filename if rotated)
# log.md is preferred; check log-2026.md if the current year's log is rotated
```

Read the full log.md file — it's typically <200 lines and gives you structured entries per ingest job:
- `## [DATE] newsletter ingest` — newsletter batch results
- `## [DATE] blog-triage ingest` — blog processing results
- `## [DATE] Active Crawl` — knowledge crawl results
- `## [DATE] Symphony blog article ingestion` — direct blog ingestion

### Step 2: Identify Top NJ Stories from log.md

From the log entries, identify the most impactful stories. For each:

1. **Read the corresponding concept/entity page** (not raw articles) — these already have structured content
2. **Apply NJ scoring** based on the page's summary + known industry context
3. Top scorer becomes the 🔥 lead; NJ 2-3 go to 📊 summary

No need to read raw articles unless the concept page is too sparse.

### Step 3: Aggregate Stats from log.md Headers

Grep log.md entries for counts:

```bash
# Count new concepts — look for "Created:" or "New Concept Pages" or "Created: concepts/"
grep -c "Created: concepts/" ~/ai-topics/wiki/log.md

# Count new entities
grep -c "Created: entities/" ~/ai-topics/wiki/log.md  

# Count updated — "Updated:"
grep -c "Updated:" ~/ai-topics/wiki/log.md

# Get total page count from last index.md update line
grep "total" ~/ai-topics/wiki/log.md | tail -1
```

### Fallback: Script Not Found + No log.md Entry

If the script doesn't exist AND log.md has no entry for today (rare — happens when the upstream ingest pipeline missed a tick), use file-system discovery:

```bash
# Files modified today (adjust date as needed)
find ~/ai-topics/wiki/ -type f -name "*.md" -newermt "$TODAY" 2>/dev/null

# Raw articles
find ~/ai-topics/wiki/raw/articles/ -name "*.md" -newermt "$TODAY" 2>/dev/null

# Get timestamps for sorting
find ~/ai-topics/wiki/ -type f -name "*.md" -newermt "$TODAY" -exec stat --format='%y %n' {} \; | cut -d'.' -f1 | sort
```

If 50+ raw articles, prioritize reading raw articles linked from new concept pages, then the 3-5 newest by timestamp, then any named after known authors.

## Newsjacking (NJ) Scoring Framework

Score each article/concept on a 0-5 scale:

- **5/5**: Trending wave + contrarian take + debate potential
- **4/5**: Riding viral momentum + in-group resonance
- **3/5**: Pattern interrupt + novelty from trusted source
- **2/5**: Standard insight, well-executed
- **1/5**: Incremental update
- **0/5**: Noise or link dump

## Report Structure (Japanese)

```
🔥 Top NJ Story (only if NJ ≥ 4 exists)
[NJ: X/5] タイトル — 1行サマリー
→ [[wiki/path]]

📊 Wiki Changes Summary — NJ score order (high → low)
[NJ: X/5] タイトル — 1行サマリー
→ [[wiki/path]]

📊 Stats
- 新規概念ページ: N件
- 新規エンティティページ: N件
- 新規比較ページ: N件
- 概念ページ更新: N件
- 新規Raw記事: N件
- 総更新数: N件
- NJ≥4ストーリー: N件
```

If **no NJ ≥ 4 articles exist**, lead with `📊 Today's Wiki Updates` instead of `🔥 Top NJ Story`.

## Edge Cases

- **log.md already has the day's entry**: Check `log-2026.md` — the "dreaming" consolidation job often writes to log.md before this report job runs. Don't duplicate content.
- **Raw articles without wiki pages**: Include raw articles in the report even if no concept/entity page was created yet.
- **Files modified but not new**: If a file was modified from a previous job's run (e.g., dreaming updated frontmatter), note it as "updated" not "new".
- **Git push may fail in cron**: Report git status clearly but don't retry.

## Writing Quality Techniques (Gwern-inspired)

The daily report pipeline can be improved using techniques from [[concepts/llm-creative-writing]] (Gwern's methodology):

### Anti-Examples Trick — Strip Generic Report Tone

After generating the first draft of a report, apply a "de-ChatGPTese" pass:

1. Ask the model to identify generic/platitudinous phrases in the report draft
2. Reverse those patterns — strip "notably," "importantly," "it's worth noting," "in the rapidly evolving landscape"
3. Force meta-cognition: ask *why* the generic pattern is bad and what the specific replacement should be

### Generate-Rank-Select — Report Iteration

For high-importance reports (NJ ≥ 4 lead stories):

1. Generate 2-3 variants of the lead section with different framing
2. Select the variant with the strongest specific claim, not the most general-sounding one
3. Use the rejected variants' best specific details to cross-enrich the chosen variant

### Manual of Style Enforcement

Maintain an implicit style contract for all reports:
- Japanese for Discord cron outputs, English for technical wiki content
- First sentence must be the most specific claim (not scene-setting)
- No filler transitions between bullet points
- Each bullet must advance a distinct idea — merge bullets that repeat

### Pitch: Anti-Examples Quality Gate in Cron Reports

When the daily-report cron detects NJ ≥ 4 stories, it should run an additional "anti-examples quality gate" pass on the lead section to strip generic framing before delivery.

## Related Skills

- `active-knowledge-crawl` — Related wiki operations
- `wiki-entity-enrichment-from-article` — Article processing workflow
- `concepts/llm-creative-writing` — Gwern's writing quality methodology (Anti-Examples, MoS, Generate-Rank-Select)