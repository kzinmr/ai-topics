# Cross-Reference Worked Example — 2026-06-21

> A "slow-but-rich" week with 69 RSS articles and 144 raw articles.
> No single launch dominated but 7 distinct thematic clusters emerged.

## Source Situation

| Metric | Value |
|--------|-------|
| RSS articles (3 days) | 69 |
| Raw articles (3 days) | 144 |
| trending_topics.py sources | 90 raw articles (no newsletters this run) |
| Trending topics found | 30 |
| Hot topics (4+ sources) | 21 |
| Selected for report | 7 |

## Background Noise (filtered out)

The trending_topics.py output was dominated by these generic entities that appeared as **background noise**, not signal:

| Entity | Sources | Real signal? | Why |
|--------|---------|-------------|-----|
| Claude | 21 | ❌ | No single event — spread across many articles mentioning Claude Code features |
| Anthropic | 12 | ❌ | Corporate mention background noise |
| OpenAI | 11 | ❌ | No single event |
| Google | 13 | ❌ | No single event |
| Meta | 9 | ❌ | No single event |
| MCP | 8 | ❌ (partial) | Not one unified topic but: enterprise auth + general mentions |
| Simon Willison | 8 | ❌ | His consistent blog output, not a new development |
| Cory Doctorow | 5 | ❌ | Consistent output from Pluralistic |

**Lesson**: In a slow week, entity names that normally correspond to launches (like "Cursor" at 6 or "Qwen" at 5) may still lack a single anchoring event. Check db article titles.

## Signal Identification

### Signal 1: Major M&A (Easy — single event, high impact)
**Cluster**: SpaceX × Cursor $60B
**Sources**: CNBC (1), Daring Fireball (1), HN discussion (1 raw article)
**Detection**: CNBC article title "SpaceX to acquire the AI coding startup Cursor for $60 billion" — unambiguous M&A event.
**Curation**: ★★★★★. Novelty + impact both extreme.
**Takeaway**: Major M&A always takes top slot regardless of source count.

### Signal 2: Cross-Source Economic Theme (Hard — needed to connect 4+ pieces)
**Cluster**: AI Industry Economics
**Sources**:
- Ars Technica: Leaked OpenAI financials (billions in losses)
- Where's Your Ed At: "Herbalife Moment" — AI as MLM
- George Hotz: "prices can't go down" — AI economics from ex-Googler perspective
- Uber spending caps ($1,500/mo/developer) — referenced in Alex Ellis article
**Detection challenge**: Each source has different keywords ("leaked", "Herbalife", "prices can't go down", "spending caps") so none would cluster via keyword matching alone.
**Curation**: ★★★★★. High controversy + wiki impact (new page needed).
**Takeaway**: Economic critique pieces often cross keyword boundaries. Read *all* non-technical opinion pieces — not just those matching technical keywords.

### Signal 3: Infrastructure Maturation (Thematic — 4 separate announcements, same theme)
**Cluster**: Agent Infrastructure Maturation
**Sources**:
- Cloudflare: Temporary Accounts (zero-friction agent deployment)
- MCP Blog: Enterprise Managed Auth (OAuth 2.0 for MCP)
- Anthropic Blog: Steering Claude Code (7 customization methods)
- Martin Fowler: Reliable Agentic AI Systems (Bayer PRINCE case study)
**Detection challenge**: These are 4 distinct announcements from 4 sources. They don't share a keyword or reference each other. The connection is *thematic* — all make production agent deployment easier.
**Curation**: ★★★★☆. Individually each is incremental; together they signal ecosystem maturation.
**Takeaway**: For infrastructure topics, group complementary announcements into one theme-synthesis topic rather than treating them as separate entries. The combined strength justifies ★★★★☆ where any single item would be ★★★☆☆.

### Signal 4: Open-Source Model Launch (Standard)
**Cluster**: DeepSeek Vision
**Sources**: DeepSeek (1), HN discussion (473pt, 194 comments)
**Detection**: Direct title match — "DeepSeek Introduces Vision".
**Curation**: ★★★★☆. Standard model launch pattern.
**Takeaway**: Model launches with HN 400+ pt discussion are automatic ★★★★☆.

### Signal 5: Inference Optimization (Technical deep-dive)
**Cluster**: Speculative Decoding Revolution
**Sources**: Modal Blog (1 primary article + HF model release)
**Detection**: Modal "Speculation Is All You Need" + HF speculator releases.
**Curation**: ★★★★☆. First-principles technical claim ("only engine optimization that matters") warrants elevation.
**Takeaway**: A single strong technical essay with a bold claim can carry enough weight for ★★★★☆ if it provides data (benchmarks, speedup charts, concrete model releases).

### Signal 6: Analytical/Philosophical Cluster (Slow-week pattern)
**Cluster**: AI Data Efficiency Limits
**Sources**:
- Dwarkesh Patel: "The data black hole at the center of AI" — sample efficiency gap
- lcamtuf (Michal Zalewski): "The 100,000 whys of AI" — AI slop uniformity
- Alex Ellis: "Local Qwen isn't a worse Opus, it's a different tool" — local model realism
- Ian Barber: "LLMs are complicated now" — architecture complexity evolution
**Detection challenge**: These are analytical essays, not news. Only Dwarkesh has "AI" in title. They address different facets of the same underlying issue (scaling limits).
**Curation**: ★★★★☆. In a slow week, high-quality analytical pieces get elevated. In a busy launch week, some of these might get dropped.
**Takeaway**: **Slow-week heuristic** — when launches are absent (no new model from Anthropic/OpenAI, no major product release), increase the weight of analytical essays and policy debates. These are the "filler" that makes a slow report valuable.

### Signal 7: Policy/Debate (Low-frequency, high-relevance)
**Cluster**: AI Governance Tensions
**Sources**:
- Cory Doctorow: "AI digital sovereignty risk doesn't exist" — sovereignty critique
- Software Freedom Conservancy: LLM recommendations — FLOSS guidelines
- Reuters: Norway school AI ban — 691pt HN
**Detection**: Diverse keywords ("sovereignty", "conservancy", "ban"). Reuters article caught by broader event keyword list.
**Curation**: ★★★☆☆. Worth including but lower urgency.

## Curation Decisions Summary

| Topic | Why selected | Why this rank | Would it make a busy week? |
|-------|-------------|---------------|---------------------------|
| SpaceX × Cursor | Unambiguous major event | #1 | Yes, always top |
| AI Economics | Cross-source cluster, high controversy | #2 | Yes |
| Speculative Decoding | Bold technical claim with data | #3 | Maybe (drop to #5-6) |
| Agent Infrastructure | Thematic grouping of 4 announcements | #4 | Maybe (drop to #5-6) |
| DeepSeek Vision | Standard model launch | #5 | Yes |
| Data Limits | Analytical cluster, slow-week filler | #6 | Dropped in busy week |
| AI Governance | Policy discussion | #7 | Dropped in busy week |

## Techniques Discovered

1. **Thematic clustering**: When 4+ sources from different outlets publish about *different aspects of the same theme* (agent infra, AI economics), group them as one topic even though no single event binds them.

2. **Slow-week adjustment**: When trending_topics.py shows < 24 hot topics (this run had 21) and no entity has > 25 sources, increase weight of analytical essays and policy pieces to maintain 7-topic target.

3. **HN score heuristic**: HN submissions with > 400 pts consistently correlate with ★★★★☆+ curation level. Use raw HN score as tiebreaker between topics of similar source-count strength.

4. **Raw article count discrepancy**: 144 raw articles vs 69 RSS articles. The raw articles include: active-crawl results, HN discussion snapshots, and sitemap-scraped content. Always use both sources — RSS alone would miss DeepSeek Vision, SpaceX/Cursor HN coverage, and several opinion pieces.
