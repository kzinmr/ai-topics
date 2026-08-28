# Cross-Reference Worked Example — 2026-07-11 (Company Monoculture Day)

## Day Profile

**Date**: 2026-07-11 (Saturday)
**Volume**: 101 RSS articles in 3 days, trending_topics.py detected 31 topics, 49 AI-relevant titles from blogwatcher DB
**Character**: Company monoculture — a single company (OpenAI) produced 5 spotlight-level events in the analysis window
**Active-crawl output**: Not found (last available: June 28 — consistent two-week gap)

## What Made This Day Unusual

This was a **company monoculture day** — one company dominated the news cycle with multiple genuinely distinct major events that each affected different domains:

| Event | Domain | Date | Sources | Signal |
|-------|--------|------|---------|--------|
| GPT-5.6 launch (Sol/Terra/Luna) | Model capability | Jul 9 | 11+ raw + RSS | ★★★★★ |
| GPT-Live (real-time voice) | Voice interaction | Jul 8 | 10 raw + RSS | ★★★★☆ |
| SWE-Bench Pro critique | Evaluation | Jul 8 | 5+ OpenAI + HN (219pts) | ★★★★☆ |
| Apple sues OpenAI | Legal/Hardware | Jul 10 | 5+ cross-source | ★★★★☆ |
| Fidji Simo steps down | Corporate | Jul 10 | WSJ + DF | ★★★☆☆ |

Total OpenAI-related: **5 of 7 report slots** at full strength.

## Curation Decisions Made

### 1. Coordinated Campaign Rule (Violation Detected and Corrected)

**Problem**: The GPT-5.6 launch (topic #1) and SWE-Bench Pro critique (topic #4) were kept as SEPARATE topics in this report. The July 10 reference explicitly states they should be a SINGLE coordinated topic.

**Root cause**: OpenAPI published the SWE-Bench critique on July 8 and GPT-5.6 on July 9 — 24 hours apart. The SWE-Bench critique explicitly shields GPT-5.6's weaker SWE-Bench score (Sol 64.6% vs Fable 80%). The July 10 reference correctly treated these as one topic. The July 11 run incorrectly split them.

**Correction**: Future runs MUST apply the coordinated campaign rule. SWE-Bench + GPT-5.6 is ONE topic at ★★★★★.

**Mitigation for this report**: The report already has 7 strong topics. Next time, merge them and fill the freed slot with a lower-ranked topic (Thinking Machines Lab essay, Cory Doctorow essay, or Meta Instagram AI training default).

### 2. Company Monoculture Heuristic Applied

After correction (SWE-Bench merged into GPT-5.6), OpenAI still occupies 4 of 7 slots (GPT-5.6, GPT-Live, Apple lawsuit, Fidji departure). This is valid because:

- **Domain diversity**: Each event affects a different domain (model, voice, legal, corporate)
- **Source diversity**: Apple lawsuit covered by WSJ, 9to5Mac, DF, Simon Willison — not just OpenAI's own blog
- **Independent narrative**: No single event is context for another (except SWE-Bench/GPT-5.6 which is now corrected)

**Heuristic applied**: Company monoculture is OK when domains diverge and cross-source coverage validates each event independently. The report intro should call this out explicitly.

### 3. Fire Hose Continuation

This day is a continuation of the July 10 fire hose — many of the same events are still in the 3-day window. The key difference: active-crawl was absent on July 10 and also absent on July 11. The two active-crawl failures in a row suggest the pipeline may have an issue, but the blogwatcher fallback handles it adequately on high-volume days.

### 4. AI Engineer Conference Cluster Applied Correctly

14 AI Engineer talks appeared in the DB. Per the conference cluster rule, these were treated as ONE topic (rank 6, ★★★☆☆). Read 3 talks in depth (sandbox cloud, ACP, deception monitor), synthesized as "agent implementation patterns."

### 5. Opinion Piece Threshold

Cory Doctorow essay (pluralistic.net) and Thinking Machines Lab manifesto were both strong pieces but dropped below the 7-topic line due to the sheer volume of newsworthy events. On a normal day either would be ★★★★☆.

### 6. Memory Crisis Article (wheresyoured.at) Survival

The "Hater's Guide to the Memory Crisis" at wheresyoured.at made the cut at ★★★★☆ because:
- It's a data-driven original analysis (not opinion on events)
- It covers a unique angle (consumer electronics price impact) that no other source addressed
- It provides concrete numbers ($1.894B HBM per 1GW DC, $316K HBM per NVL72 rack)

## Raw Article Discovery Pattern

**49 AI-relevant articles** found via blogwatcher DB. Raw article files found for most key sources:

- **Simon Willison**: 3 raw files (GPT-5.6, GPT-Live, OpenAI quote) — all substantive
- **9to5Mac/DF**: Apple lawsuit raw file — full article extracted
- **Sierra Blog**: AI-pilling raw file — full article (53 lines excellent content)
- **Thinking Machines Lab**: Full manifesto raw file (94 lines)
- **Pluralistic.net**: Cory Doctorow essay raw file (168 lines)
- **wheresyoured.at**: Memory crisis raw file (157 lines)
- **OpenAI official blog (GPT-5.6)**: No raw file found (likely JS-rendered)
- **Merge Blog (Kimi K2.6)**: No raw file found (SPA content gap)

**Pattern**: SPA gap affects Merge Blog and the OpenAI blog post. Content-rich articles from Simon Willison, Sierra, Pluralistic, wheresyoured.at, and Thinking Machines Lab all had full raw files. Prioritize these for deep reading.

## Newsletter Pipeline Status

0 newsletters scanned. This is a recurring gap — the `trending_topics.py` output consistently shows 0 newsletter sources. On high-volume RSS days this is irrelevant, but on slow days it would be a material gap.

## Score Distribution Tension

The 7-topic report had:
- 2 × ★★★★★ (GPT-5.6, GPT-Live)
- 3 × ★★★★☆ (Apple lawsuit, SWE-Bench, memory crisis)
- 2 × ★★★☆☆ (AI Engineer Conf, Sierra Pinecone)

This compression (5 of 7 at ★★★★☆+) is unusual but justified by the fire hose volume. The July 10 reference also noted the same compression pattern.

## Key Takeaway

The most important lesson from this day: **apply the coordinated campaign rule consistently**. The July 10 reference already documented the rule; the July 11 run violated it by splitting SWE-Bench and GPT-5.6. Future runs should load the July 10 reference before making curation decisions. The company monoculture heuristic is new — add it to the skill's curation section.
