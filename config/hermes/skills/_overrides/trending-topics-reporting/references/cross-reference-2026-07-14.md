# Cross-Reference Worked Example — 2026-07-14

**Pattern**: CEO essay cluster + conference cluster + model competition — normal volume, no coordinated campaign, no company monoculture.

## Data Snapshot

- **Blogwatcher DB**: 89 articles in 3 days, 35 AI-relevant
- **Raw articles**: 70+ files across canonical + cron HOME paths
- **Newsletters**: 0 (no newsletter digest this window)
- **Active-crawl**: Not found (pipeline skipped)
- **trending_topics.py** output: 28 trending topics, 17 hot (4+ sources)

## Top Source Distribution

| Source | Articles | Notes |
|--------|---------|-------|
| AI Engineer | 22 | Conference cluster — treated as 1 topic |
| daringfireball.net | 21 | Apple-focused, mostly non-AI |
| simonwillison.net | 8 | High signal-per-article ratio |
| Merge Blog | 4 | 3 of 4 were AI governance/model comparison |

## Signal Discovery Path

### 1. CEO/Thought-Leader Essay Cluster (novel pattern this week)

Three independent thought-leader essays in the same 3-day window:

| Author | Article | Raw Source Count | Engagement | Signal Weight |
|--------|---------|:----------------:|:----------:|:-------------:|
| Satya Nadella | "Reverse Information Paradox" | 1 (X article) | 22K bookmarks, 10M impressions | ★★★★☆ |
| George Hotz | "I love LLMs, I hate hype" + "AI 2040" | 5 (2 raw articles + blogwatcher) | 3 geohot posts | ★★★★☆ |
| Cory Doctorow | "Why aren't AI companies competing..." | 2 (blogwatcher + raw) | Discussion across tech media | ★★★★☆ |

**Takeaway**: CEO essays with X bookmark counts >5,000 can be top-tier topics even from a single source. The blogwatcher DB Query 3a caught Hotz (via 'Hotz' keyword) but missed Nadella's X article entirely (not in RSS DB). Nadella was discovered via the `find` raw articles scan (X article scraper caught it). Without the raw article fallback, this topic would have been invisible to RSS-only analysis.

### 2. Conference Cluster (standard pattern)

AI Engineer Conference (22 talks) → treated as ONE topic covering:
- Agent production patterns (Machinecraft 39 agents, CI/CD reinvention)
- Security (bugpocalypse, approval spoofing)
- RL/reward hacking (Unsloth)
- Enterprise knowledge (Microsoft)

**Takeaway**: Standard conference cluster handling worked correctly. Picked 3-5 representative talks for deep reading, used the dominant themes for the report entry.

### 3. Model Competition (normal pattern)

GPT-5.6 Terra vs Claude Sonnet 5: Merge Blog benchmark + Simon Willison Fable extension commentary. No coordinated campaign — Merge Blog is a third-party comparison platform, not a lab publication.

**Takeaway**: The coordinated campaign rule (benchmark critique + model launch = 1 topic) was NOT triggered because the benchmark came from Merge, not from a competing lab. This is the correct application — the rule only applies when the same lab publishes a benchmark critique AND their own model launch within 48h.

### 4. Apple SpeechAnalyzer Benchmark (single-article-heavy topic)

One article from get-inscribe.com with comprehensive data. Was accepted as a fourth topic despite single-source status because:
- First independent benchmark of Apple's new API
- Had concrete cross-validation publishing raw transcripts
- Generated discussion across developer channels
- Connected to broader Apple AI ecosystem (TwoMillionKit, Private Cloud Compute)

**Takeaway**: Single-source topics can qualify if they have: (a) first-of-its-kind data, (b) methodological rigor with public datasets, (c) ecosystem relevance beyond the single article.

## Heuristics Applied

| Heuristic | Applied? | Outcome |
|-----------|:--------:|---------|
| Conference cluster | ✅ | AI Engineer 22 talks → 1 topic |
| Slow-week heuristic | ❌ | Not needed — 17 hot topics |
| Coordinated campaign rule | ❌ | Not triggered (benchmark from third party) |
| Company monoculture | ❌ | No single company dominated |
| Thematic clustering | ✅ | Agent governance (Merge Blog) + security (AI Engineer) → merged into 1 agent-governance topic |
| CEO essay weighting | ✅ | All three CEO essays got +1★ boost over raw count |
| X bookmark tiebreaker | ✅ | Nadella 22K → ★★★★☆, Doctorow lower engagement → still warranted inclusion |

## Key Improvements from This Session

1. **CEO essay detection** is now institutionalized in the keyword list (Nadella, Doctorow, Karp, Altman added to Query 3a)
2. **X bookmark tiebreaker** added as explicit heuristic alongside HN score
3. **CEO/Thought-Leader essay weighting** heuristic added to SKILL.md Curation section
