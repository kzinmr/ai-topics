# Cross-Reference Workflow: Signal from Noise

> A worked example from the 2026-06-13 run, codified as a repeatable pattern.

## The Problem

`trending_topics.py --days 3` returns a ranked topic list where generic entity names
(Claude: 51, Anthropic: 39, OpenAI: 26) dominate the top by raw count.
These are **background noise** — the expected baseline, not specific new developments.

The blogwatcher DB query for AI-relevant titles (Query 3) returns **article titles**,
which contain the actual signal. You need to map the topic-count table against the
title list to find real stories.

## The 3-Column Cross-Reference Technique

Run these three outputs **side by side** (or sequentially, keeping them in context):

| Source | What it gives you | Purpose |
|--------|------------------|---------|
| `trending_topics.py` | Topic → count table | Broad landscape, identifies what people are talking about generically |
| Blogwatcher DB Query 3 | Article titles + URLs + source blogs | Specific stories behind the counts |
| `find` on raw articles | Filenames by keyword | Articles from active crawl (not just RSS) |

## Worked Example (2026-06-13)

### Step 1: Scan trending_topics.py hot topics

```
Claude (51), Anthropic (39), evals (36), Google (28), OpenAI (26), MCP (20),
Simon Willison (18), fine-tuning (12), Qwen (11), RAG (10), Gemini (9),
coding agents (9), Cursor (8), agentic engineering (8), long context (8),
red teaming (8), Dario Amodei (7), Gemma (7), Cognition (6)...
```

**Obvious noise**: Claude (51), Anthropic (39), OpenAI (26), Google (28), evals (36)
→ these are the default background. Skip.

**Potential signals** (lower count but topic = specific noun phrase):
- Dario Amodei (7) → person who published a policy essay
- MCP (20) → high count for a protocol, worth checking
- RAG (10) → new page recommended, check for specific development
- Gemma (7) → new model release?
- fine-tuning (12) → concept but high count = possible new technique

### Step 2: Map against blogwatcher DB titles

Look at the Query 3 output and group articles by **event cluster**:

| Cluster | Articles | Verdict |
|---------|----------|---------|
| Claude Fable guardrails | 4+ articles: Simon Willison "relentlessly proactive", Jon Ready "hidden guardrails", The Verge "apologizes", Gary Marcus "Section 230 & Fable" | **REAL SIGNAL** — controversy, multiple sources, specific event |
| Dario Amodei policy essay | darioamodei.com essay, cross-referenced by Simon Willison | **REAL SIGNAL** — first-of-its-kind regulatory proposal |
| OpenAI price cuts | WSJ scoop via Gary Marcus, George Hotz deflation essay | **REAL SIGNAL** — major economic implication |
| MCP ecosystem | Merge Blog 6× MCP+Codex guides, AI Engineer WebMCP talk | **REAL SIGNAL** — ecosystem expansion, new Google standard |
| MiniMax M3 / K2.7 Code | Fireworks AI blog posts | **REAL SIGNAL** — new model releases |
| Botsitting | Business Insider, Glean report | **MODERATE SIGNAL** — survey/report, good wiki material |
| Warp Oz / Rex | Warp blog | **MODERATE SIGNAL** — case study, shows pattern |

### Step 3: Find raw article files for each cluster

Use `find` to locate the full articles, not just RSS titles:

```bash
# By keyword
find /opt/data/ai-topics/wiki/raw/articles/ -name "*fable*" -o -name "*guardrail*" 2>/dev/null

# By date (last 2 days)
find /opt/data/ai-topics/wiki/raw/articles/ -name "*.md" -mtime -2 | sort

# Blogwatcher hash-suffixed files (RSS-ingested)
find /opt/data/ai-topics/wiki/raw/articles/ -name "*simonwillison*" -mtime -3 2>/dev/null
```

**Critical discrepancy note**: The blogwatcher DB (`SELECT COUNT(*)`) may report fewer
articles than `find` on raw articles. In the 2026-06-13 run: DB had 98 articles in 3 days
but raw articles directory had 135. The gap is **active crawl articles** (not RSS-ingested).
Always use `find` as a secondary discovery path — don't rely solely on the DB query.

### Step 4: Deep read → signal verdict

For each cluster, read 1-2 representative articles (30-60 lines). Ask:
- Is this a **first-of-its-kind** claim? → high novelty
- Is there **controversy or debate**? → high discussion value
- Does it have **wiki impact** (new page or major update)? → actionable
- Is it a **new model release** with specific metrics? → always include

### Step 5: Finalise top 5-8

Drop clusters that fail the test:
- RAG (10): After reading, likely incremental RAG technique articles, no single event
- fine-tuning (12): Noise — default background concept
- evals (36): Noise — default background
- Gemma (7): Checked titles → likely incremental update, no major release

## Common Failure Modes

| Pattern | Symptom | Fix |
|---------|---------|-----|
| Aggregator excerpt | Gary Marcus substack posts: 20 lines, no article body | Check if it's just a link post before including |
| Conference talk w/o transcript | WebMCP: YouTube link, minimal text content | Decide based on significance of the announcement itself |
| Dual-storage blindspot | Article in `~/.hermes/home/wiki/raw/articles/` but NOT in canonical path | Always search both paths |
| Short social post masquerading as article | Brief X thread or Bluesky post saved as .md | Filter out articles under 50 lines unless the author is the primary source |
