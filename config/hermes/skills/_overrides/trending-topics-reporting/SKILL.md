---
name: trending-topics-reporting
category: research
description: >-
  Regularly scan RSS feeds, blogwatcher DB, and raw articles for trending AI/ML
  topics. Synthesize findings into a Japanese-language report with top 5-8
  topics, source links, and wiki-action recommendations.
---

# Trending Topics Reporting

Scheduled research/reporting pipeline (12:00 UTC / 21:00 JST) that discovers, analyzes, and reports on trending AI/ML topics across all ingested sources.

## Pipeline Position

```
blog-ingest (07:00) → newsletter-ingest (07:10) → ... → active-crawl (11:00 UTC) → trending-topics (12:00 UTC)
```

The pipeline runs **after** all morning ingestion pipelines AND the `active-crawl` job (11:00 UTC), so it can reuse the active-crawl research note as a primary HN/X data source rather than running separate queries.

## Prerequisites

- Run `trending_topics.py` script first (`python3 ~/ai-topics/scripts/trending_topics.py --days N`)
- Query blogwatcher DB for recent article counts
- Read key raw articles for depth

## Workflow

### Phase 1: Data Collection (DB + Script + Optional HN)

1. **Run the trending script**:
   ```bash
   python3 ~/ai-topics/scripts/trending_topics.py --days 3
   ```
   Output: topic frequency table, new-page candidates, hot topics (4+ sources).

2. **Query blogwatcher DB for context** — use the exact queries from `references/blogwatcher-db-recipes.md`:
   - **Query 1**: Total articles in last 2-3 days
   - **Query 2**: Group by blog source to see distribution (top 20)
   - **Query 3**: Filter for AI-relevant titles — this is the **primary workhorse** that surfaces article titles, URLs, and source blogs for deep reading
   - **Query 4**: Unread article count by blog (health check)

   Run them with the full script from the reference file, or inline:
   ```bash
   python3 -c "
   import sqlite3
   db_path = '/opt/data/.blogwatcher/blogwatcher.db'
   conn = sqlite3.connect(db_path)
   cur = conn.cursor()

   # Total articles
   cur.execute(\"SELECT COUNT(*) FROM articles WHERE published_date >= date('now', '-3 days')\")
   print(f'Total articles (last 3 days): {cur.fetchone()[0]}')

   # Top 20 blogs
   cur.execute('''SELECT b.name, COUNT(*) as c FROM articles a JOIN blogs b ON a.blog_id = b.id
       WHERE a.published_date >= date('now', '-3 days')
       GROUP BY b.name ORDER BY c DESC LIMIT 20''')
   print('Top blogs:')
   for row in cur.fetchall():
       print(f'  {row[0]}: {row[1]}')

   # AI-relevant articles (see reference file for the definitive keyword list)
   ai_keywords = ['AI', 'LLM', 'agent', 'model', 'GPT', 'Claude', 'OpenAI', 'Anthropic',
       'RL', 'fine-tun', 'reasoning', 'safety', 'inference', 'multimodal',
       'embedding', 'transformer', 'diffusion', 'Llama', 'Gemini', 'Mistral',
       'coding', 'RAG', 'MCP', 'training', 'RLHF', 'alignment', 'open source',
       'synthetic', 'scale', 'evals', 'sandbox', 'prompt', 'Cursor',
       'Windsurf', 'memory', 'agentic', 'distillation', 'quantization',
       'Nemotron', 'Codex', 'augment', 'cosmos',
       'Hotz', 'Amodei', 'Nadella', 'Doctorow', 'Karp', 'Altman']
   conditions = ' OR '.join([f\"a.title LIKE '%{kw}%'\" for kw in ai_keywords])
   cur.execute(f'''SELECT a.title, b.name, a.url, a.published_date
       FROM articles a JOIN blogs b ON a.blog_id = b.id
       WHERE a.published_date >= date('now', '-3 days') AND ({conditions})
       ORDER BY a.published_date DESC LIMIT 50''')
   print('AI-relevant articles:')
   for row in cur.fetchall():
       print(f'  [{row[3]}] {row[1]}: {row[0]}')
   "
   ```

3. **Check active-crawl output** — see `references/active-crawl-output-reuse.md`:
   - The `active-crawl` job (11:00 UTC) produces a research note at
     `wiki/raw/articles/YYYY-MM-DD_active-crawl-trending-topics-research.md`
   - **⚠️ Dual naming convention**: The file may also be named
     `wiki/raw/articles/YYYY-MM-DD_trending-topics-research.md` (without `active-crawl` in
     the filename). Always search for BOTH patterns:
     ```bash
     find /opt/data/ai-topics/wiki/raw/articles/ -name '*trending-topics-research*' -mtime -1 2>/dev/null
     ```
   - **Also check the cron HOME fallback path**:
     ```bash
     find /opt/data/.hermes/home -path "*/raw/articles/*" -name '*trending-topics-research*' -mtime -1 2>/dev/null
     ```
     — in cron mode, the active-crawl output may only exist there
   - This note already contains HN Algolia point scores, X/Twitter engagement data,
     and wiki gap analysis — **use it as the primary HN/X data source**
   - If the file exists: extract HN point scores (for ★ rating), bookmark counts
     (for signal strength), and gap analysis (for wiki action recommendations)
   - **Volume-based fallback skip (amended 2026-07-31)**: If blogwatcher DB yields ≥20 AI-relevant articles
     with clear event clusters and Phase 1.5 cross-reference is satisfactory, skip the *full* HN discovery
     sweep — but still run 3-6 **targeted** HN Algolia point-score queries on the candidate clusters
     (curl-to-file, see the curl pitfall). Point scores are cheap and materially calibrate ★ ratings:
     585pts validated GPT-5.6 price-cut as ★★★★★, 190pts validated Anthropic cyber-evals as ★★★★★,
     3pts downgraded the Dwarkesh compute essay to analytical-merit-only ★★★★☆.
     See `references/cross-reference-2026-07-31.md`.
   - **Yesterday's note as intermediate fallback**: Even when today's active-crawl output
     is missing (pipeline failure / holiday), check if yesterday's (or the most recent
     ≤48h old) research note exists:
     ```bash
     find /opt/data/ai-topics/wiki/raw/articles/ -name '*trending-topics-research*' -mtime -2 2>/dev/null | head -1
     ```
     The most recent note's HN Algolia point scores, Dominant Theme, and gap analysis
     remain directional for stories under 48 hours old. Stories >400 pts from yesterday
     consistently validate as ★★★★☆+ topics. This check takes <5 seconds and can save
     10-15 minutes of manual Algolia queries. If the note contains topics that are
     still active (model launches, legal battles, safety research that crosses multiple
     days), extract those point scores to use as ★ rating input.
   - **No research-note file ≠ no active-crawl work** (observed 2026-08-11): active-crawl can run at 11:00, create 5 pages + 2 enrichments, and still NOT write a `*trending-topics-research*` note. The reliable "did active-crawl run" signal is the log.md head-scan (`head -80 wiki/log.md` shows the 11:00 active-crawl entry with pages created). When present, those created concept pages ARE the gap analysis — treat their topics as already wiki-covered and skip the full HN discovery sweep (only run the 3-6 targeted point-score queries for ★ calibration).
   - If the file does NOT exist AND yesterday's note is also absent AND blogwatcher
     volume is low (<20 AI-relevant articles): run Steps 3b and 3c manually

3b. **(Fallback) Scan HN Algolia for breaking AI stories** — see `references/hn-algolia-discovery.md`:
   - Only run if active-crawl output is absent
   - Use `search_by_date` endpoint (NOT `search` — that's relevance-ranked, not recency)
   - Run 8-15 keyword queries (AI+agent, LLM, OpenAI, Claude, DeepSeek, etc.), deduplicate by objectID
   - Filter: points ≥8 weekdays / ≥5 weekends, AI-relevance keyword check
   - **Watch for**: HN captures major model launches and policy stories that RSS may miss (e.g., GPT-5.6 Sol, Anthropic Mythos restricted release)
   - **Pitfall**: `/items/{id}` returns `num_comments=0` — use `search_by_date` with title keywords for accurate comment counts
   - Useful when: major AI events are unfolding and HN is the primary discussion venue

3c. **(Fallback) Scan X/Twitter** — only if active-crawl output is absent:
   - Use `xurl search` with targeted queries or check `xurl user` from tracked accounts
   - Filter by engagement (bookmarks > 50 = substantive thread signal)
   - Focus on: model release discussion, agent tooling announcements, policy commentary

4. **Discover raw article files** — see `references/raw-article-discovery.md` for exact `find` commands:
   - Primary path: `~/wiki/raw/articles/` (= `/opt/data/ai-topics/wiki/raw/articles/`)
   - Fallback path (cron HOME): `/opt/data/.hermes/home/wiki/raw/articles/`
   - Date-range discover: `find` with `-mtime -3`
   - Keyword discover: `find` with `-name \"*keyword*\"`
   - **Two filename conventions exist** (canonical `YYYY-MM-DD_source-slug.md` + blogwatcher hash-suffixed `domain.com--path--hash8.md`). See `references/raw-article-discovery.md` for both patterns and discovery commands.
   - **Do NOT guess filenames for blogwatcher-ingested articles**

### Phase 1.5: Cross-Reference (Signal from Noise)

The `trending_topics.py` output is noisy — generic entity names dominate raw counts.
Map the topic-frequency table against actual article titles **before** deep reading.

**Full workflow** with a worked example from the 2026-06-13 run:
see `references/cross-reference-workflow.md`.

**Quick steps**:
0. **Read yesterday's report first**: `~/ai-topics/inbox/rss-scans/trending-topics-*.md` (most recent). **The most recent daily report may NOT be yesterday** (observed 2026-08-05: no 08-04 file; anchor was 08-03 daily + 08-03 weekly digest). When a day is missing, the gap days' topics are fair game IF the wiki log head-scan shows no pipeline ingestion — run `head -80 wiki/log.md` before assuming a gap-day topic is unreported: on 2026-08-05 the morning pipelines had already ingested 7 of 9 candidate topics (Yegge, Zitron bubble, MiniMax H3, ChatGPT Work, MoK, cyber-evals, OpenAI×Apple PI), leaving only residuals (ai-economics 7/13, elevenlabs 8/1, warp missing).
   **Monday rule**: On Mondays the `weekly-ai-digest-YYYY-MM-DD.md` is created at 00:00 UTC, ~12h before this 12:00 UTC daily run. Read it BEFORE yesterday's daily report and treat it as the PRIMARY dedup anchor: the daily report must (a) focus on developments from the last ~12-24h (post-digest), and (b) actively hunt for **digest misses** — major stories inside the digest's 7-day window that the digest omitted. Observed 2026-08-03: OpenAI Astra math breakthrough (8/1, 8.4M X views + HN 459pts) was missed by BOTH the 8/2 daily report and the 8/3 weekly digest; the daily caught it as ★★★★★. Hunt technique: scan `find ... -mtime -2` raw articles on both paths — if a raw file exists for a big-point story (e.g. Gary Marcus Astra essay, Simon Willison ten-advances) but neither report covered it, that is a digest miss. Do NOT re-cover digest topics even if they look fresh (e.g. Sierra×Plaid was digest topic 7 — skip in daily).
   Note which topics were already reported so today's list focuses on genuinely NEW developments
   (2026-07-31: dropped Kimi K3, ARC-AGI-3, NVIDIA Blackwell, antirez debate — all covered 7/30;
   kept GPT-5.6 price cut, Anthropic cyber-evals, Dwarkesh compute essay, Merge Agent Handler).
   **Multi-report dedup grep** (observed 2026-08-11): when a report day is missing (e.g. no 08-10 file), grep candidate topic names across the last 4-5 reports, not just the previous one:
   `grep -n "Topic\|Keyword" inbox/rss-scans/trending-topics-2026-08-0{5,6,7,8,9}.md` — one pass excluded 5 pre-covered topics (Discovery Loop 8/6, Castform 8/6, Astra Critical + HF timeline 8/8, DOE Genesis 8/8, Oracle OpenJDK 8/9). Without it, GPT-5.6-Cyber risked being re-reported as the Astra story and Discovery Loop could have resurfaced as new.
   Also grep candidate wiki pages' frontmatter `updated:` dates to distinguish "already ingested by
   blog-wiki-ingest" (mark ✅ DONE) from "stale, needs update" before writing recommendations.
1. Scan trending_topics.py output. Flag generic entity names (Claude, OpenAI, Anthropic)
   as **background noise** — skip unless a specific article title reveals a real event.
2. Group blogwatcher DB titles into **event clusters** (e.g. "Fable guardrail controversy"
   = 4 articles from different sources about the same event).
3. Cross-reference against `find` results on raw articles to catch **active crawl**
   articles that don't appear in the RSS-only blogwatcher DB. Also check the active-crawl
   research note (see Step 3a) — its Dominant Theme and Top HN Stories sections validate
   which topic clusters are genuinely hot beyond RSS frequency counts.
4. Drop clusters that are incremental updates without controversy, novelty, or wiki impact.

**Key discrepancy**: The blogwatcher DB and `find` often disagree on article counts.
Blogwatcher is RSS-only; raw articles include active crawl. Always use both.

### Phase 2: Deep Reading

For each candidate trending topic (identified by frequency and cross-referenced in Phase 1.5):

1. **Read raw article files first**: Use `read_file` on the discovered `.md` files (at least first 30-50 lines).
2. **If no raw file exists** for a DB-discovered article (common — blog-ingest may not have fetched it, or the site is SPA-based):
   1. **Try `curl` + HTML stripping**: `curl -sL '<URL>' -o /tmp/article.html` then extract with `python3 -c "import re; ..."` using `re.sub(r'<[^>]+>', ' ', open('/tmp/file.html').read())`.
      - **Works for**: Ghost blogs, WordPress, Docusaurus, most static sites, Next.js pages WITH SSR.
      - **Fails for**: Pure React SPAs (Ramp Builders, Augment Code) — returns only "You need to enable JavaScript."
   2. **Fallback to `web_search`** (agent search tool, NOT terminal — unavailable there) with the article title as query. This works for SPA-only pages that have been indexed by search engines.
   3. **Last-resort fallback**: Use `delegate_task` with `web` toolset to fetch and summarize the URL via an isolated subagent.
3. Identify: key claims, entities mentioned, controversy/novelty level
4. Check if content aligns with wiki scope (LLM/AI Agent tech, tools, safety, infra)

**Known pattern**: Conference talk listings (AI Engineer YouTube playlist), opinion essays (wheresyoured.at), and product announcements (Modal, Voyage AI) almost always have raw files. Company engineering blogs on SPA frameworks (Ramp Builders, Augment Code) often don't — rely on `web_search` or delegate_task for those.

**New pattern — Anti-bot JS gate (Merge Blog, similar sites)**:
Some blogs (Merge Blog is the known example) use **fingerprint-based redirect anti-bot protection** (FingerprintJS) that blocks `curl` extraction entirely. Unlike SPAs where you get a "You need to enable JavaScript" message, these sites return a blank page with a redirect script and require real browser rendering. `web_search` or `delegate_task` with the `browser` toolset can bypass these. When multiple Merge Blog articles appear in Query 3 results but no raw files exist, assume they're behind this gate and skip direct curl extraction.

### Phase 3: Topic Curation

Select the **top 5-8 topics** based on:
- **Frequency** — how many independent sources cover this topic
- **Novelty** — genuinely new development vs incremental update
- **Controversy** — debates/different viewpoints create discussion value
- **Wiki impact** — does this warrant new pages or page updates?

### Curation: Signal vs Noise

The `trending_topics.py` output is noisy — generic entity names like "Claude" (38 sources), "OpenAI" (25 sources) often dominate raw counts but represent **background noise**, not specific new developments. Apply these heuristics:

- **Filter background noise**: Generic entity names (Claude, OpenAI, Google) appearing as raw counts → expected baseline, not signal.
- **Identify real signals**: Look for **launch clusters** — multiple articles about the same specific product/event (e.g., 5× Cursor articles = Cursor 3.0 launch; 3× MAI articles = Microsoft MAI release).
- **Cross-reference with blogwatcher DB**: Query 3 gives actual article titles. A "Claude" count of 38 means nothing; a specific title about "Claude Code feedback loops" or "Claude sandboxing" is genuine signal.
- **Novelty filter**: Prioritize: (a) first-of-its-kind claims, (b) controversy/debate (ROI, safety, governance), (c) new open-source model releases, (d) new evaluation methodologies, (e) ecosystem standards/consolidation.
- **Wiki impact test**: Ask "does this topic warrant a new wiki page or a significant update to an existing one?" If not, consider it a minor blip.
- **Slow-week heuristic**: When hot topics < 24 and no entity has > 25 sources, increase weight of analytical essays and policy pieces to maintain the 7-topic target. See `references/cross-reference-2026-06-21.md` for a worked example.
- **Thematic clustering**: Group complementary announcements (e.g., 4 agent-infrastructure items from different sources) into one theme-synthesis topic. Combined strength often justifies ★★★★☆ where individual items would be ★★★☆☆.
   - **Conference cluster treatment**: When a single source (e.g., AI Engineer Conference, WWDC, Google I/O) produces ≥10 articles in the analysis window, treat them as ONE conference-cluster topic, not N independent signals. Read 3-5 representative articles in depth and synthesize the conference's dominant themes into a single report entry. Do not inflate the count — conference articles from one source do not validate each other.
   - **Content-series cluster treatment**: When a single blog publishes 3+ related articles in the SAME thematic category within 3 days (e.g., 3 model comparison articles from Merge Blog comparing different vendor pairs; 5 "how to build" tutorials from the same engineering blog), treat them as ONE content-series cluster. Unlike conference clusters where articles validate each other's existence, content-series articles are individually useful data points that collectively strengthen a BROADER narrative (e.g., "model competition is intensifying" rather than "model X beats model Y"). Read 1-2 articles in depth for concrete numbers, cite the series as a grouped source, and use the remaining titles as supporting evidence. Do NOT split them into 3+ separate topics — but DO use their combined weight to justify ★★★★☆+ for the parent narrative topic. See `references/cross-reference-2026-07-16.md` for a worked example.
   - **Security incident cluster treatment**: When multiple independent companies have security/privacy incidents in the SAME thematic category within 3 days (e.g., 2026-07-16: Grok Build auto-upload privacy scandal + Codex $HOME deletion bug + Cursor 0day disclosure — three independent coding-agent security incidents), treat them as ONE thematic cluster. Unlike content-series clusters (same blog) or conference clusters (same source), security incidents from different companies VALIDATE each other — a pattern of industry-wide issues is stronger evidence than any single incident. Read all available articles for concrete details, score as ★★★★☆ if ≥2 companies are affected, and synthesize under a shared thematic heading (e.g.,「コーディングエージェントセキュリティ問題」).
   - **Multi-party governance open-letter cluster treatment**: When opposing camps publish open letters / position papers on the SAME policy question within ~1 week (e.g., 2026-07-24→28: "Open Weights and American AI Leadership" by Microsoft-shepherded 235 companies vs Anthropic's "Our position on open-weights models" vs "Pacing the Frontier" by 1,324 frontier-AI employees), treat the whole exchange as ONE topic — the debate itself is the story, not 3 separate letters. This applies to governance letters (open weights, regulation, pacing), NOT to product launches. The anchor piece is usually a same-week synthesis (Simon Willison's 8/2 "Open letters about AI development" was the perfect spine). Score ★★★★★ if both sides have substantive signatories (100+ orgs / 1,000+ individuals) and the policy question is live. Related frameworks published in the same window (e.g., Thinking Machines Lab "A Safe Path to Open Weights" staged-release post) fold into the same topic as supporting sources. See `references/cross-reference-2026-08-02.md`.
- **Frontier Model Day / multi-lab launch cluster**: When 3+ independent labs launch models within ~48h (e.g., 2026-08-12→13: Grok 4.6, Qwen3.8-Max open weights, DeepSeek V4 Pro GA, Microsoft MAI-Thinking-1), each launch CAN remain its own topic — unlike conference clusters, different companies' launches validate each other's existence and affect demonstrably different domains (model capability, pricing, open-weights, platform). But: (a) add a "Frontier Model Day" concentration note to the report intro naming the shared window; (b) calibrate EACH launch with its own HN point-score query — do not treat the cluster's combined volume as one signal; (c) expect morning pipelines (newsletter-wiki-ingest / blog-wiki-ingest) to have already ingested most launches since AINews covers them same-day — the residual wiki action is often a single page that got a reference but not a full event section. See `references/cross-reference-2026-08-13.md`.
- **Coordinated campaign rule**: When Lab A publishes a benchmark critique of Benchmark X AND Lab A's own model launch follows within 48 hours with the same model underperforming on Benchmark X, these MUST be treated as ONE coordinated topic (not separate). The benchmark critique is context for the launch, not an independent signal. The July 10 reference file (`cross-reference-2026-07-10.md`) documents this pattern — do not repeat the July 11 error of splitting them into rank 1 and rank 4.
- **Company monoculture heuristic**: When a single company produces 3+ genuinely independent major events in one analysis window (e.g., OpenAI week of July 8 — GPT-5.6 launch + GPT-Live + SWE-Bench critique + Apple lawsuit), each event CAN stand as its own topic IF they affect demonstrably different domains (model capability → one topic, voice product → another, legal action → another). However:
   * Add a **"Company Concentration" note** in the report intro: e.g., "今週はN社が全7トピック中X個を占める集中週"
   * Apply the coordinated campaign rule FIRST (benchmark critique + model launch = ONE topic)
   * If the monoculture pushes the report past 7 topics, de-prioritize lower-ranked topics from the dominant company before cutting topics from other companies
   * See `references/cross-reference-2026-07-11.md` for a worked example
- **HN score heuristic**: HN submissions > 400 pts consistently correlate with ★★★★☆+ curation level. Use as tiebreaker.
- **HN-low / X-engagement rescue heuristic** (observed 2026-08-11): major lab model launches can warrant ★★★★★ with near-zero HN points when X views + Reddit activity are exceptional — Muse Glimmer 30B: HN 4pts but X 944K views + r/LocalLLaMA 2141 activity → ★★★★★. HN front-page queries under-sample the r/LocalLLaMA audience; for open-weight model launches, calibrate with X/Reddit engagement from the AINews recap (AI Twitter Recap + Reddit Recap carry exact numbers) instead of treating low HN as a demotion.
- **X bookmark score tiebreaker**: X/Twitter bookmark counts are a viable signal strength indicator for content not on HN. Use as secondary tiebreaker: >5,000 bookmarks → ★★★★☆ candidate, >500 bookmarks → strong community signal (retain even if source count is low), <50 bookmarks → weak signal (verify against other sources). Treat 22K+ bookmarks (CEO essays) as ★★★★★ signal regardless of RSS source count — X engagement can validate content the RSS-only DB missed.
- **CEO/Thought-Leader essay weighting**: When a top executive (CEO, CTO, prominent figure) publishes a long-form original essay and it has exceptional engagement (>5,000 bookmarks or >1M impression count), it earns an automatic +1★ signal boost above what its raw source count suggests. The reverse information paradox essay by Satya Nadella (22K bookmarks, 10M impressions from a single source) is the canonical example — a single piece of content from one source can be a top-tier topic when the author's stature and engagement are both exceptional. Do NOT apply this boost to routine company blog posts or press releases — only to genuine thought-leader essays (manifesto, reflection, "why I...", policy position, open letter). Signals: (a) length > 2,000 words, (b) first-person reflective voice, (c) engagement spike across X, HN, or industry discussion within 24h of publication.

### Phase 4: Report Generation

Write a **Japanese-language report** with this structure:

```markdown
# 🔥 トレンドトピックレポート — YYYY-MM-DD

> 分析期間: YYYY-MM-DD → YYYY-MM-DD
> ソース: RSS N記事, blogwatcher DB + raw articles

## 1️⃣ 🛡️ [Topic Title] — [1-line subtitle]
**強度: ★★★★★** | **関連ソース:** source1, source2, ...
[3-5 sentence summary in Japanese with key facts]
- [Link description](url)
```

Each topic should have:
- **Ranked heading** with emoji indicator
- **Source attribution** (which blogs/outlets covered it)
- **Concrete summary** with specific facts, numbers, claims
- **Direct links** to source articles

### Final Table: Wiki Action Recommendations

```markdown
## 📊 ウィクション推奨アクション
| トピック | 強度 | アクション |
|---------|------|-----------|
| Topic | ★★★★★ | 既存ページ名 — 更新内容 |
```

### Save Path

Save to: `~/ai-topics/inbox/rss-scans/trending-topics-YYYY-MM-DD.md`

### Deliverable

Final response is auto-delivered. Format as clean markdown with the full report. Do NOT use `send_message` or deliver independently.

### Weekly Digest Mode (Monday 00:00 UTC)

A higher-quality variant of the daily trending-topics report. Runs every Monday 00:00 UTC via the `weekly-ai-digest` cron job. Covers 7 days instead of 3.

**Differences from daily mode:**
- **7-day window** instead of 3-day — `trending_topics.py --days 7`
- **Gwern quality techniques** (T1-T5 below) are **MANDATORY** — this is the user's highest-priority report
- **Section-level Atomic Snippets** with 3-layer structure (一言要約 / 詳細 / 深掘り)
- **Wikilink density**: minimum 2 wikilinks per topic (Engram Pathways)
- **Title selection**: generate 2-3 variants and rank-select the best (Generate-Rank-Select)
- **Save to** `~/ai-topics/inbox/rss-scans/weekly-ai-digest-YYYY-MM-DD.md`
- **Commit and push** after writing (unlike daily mode which skips commit)
- **Company monoculture note** in intro when one company dominates multiple topics

#### T1: Anti-Examples — Slop Removal

After generating the draft, self-review for ChatGPT-style generic expressions:
- 「画期的な」「革新的な」「注目すべき」→ replace with concrete statements
- 「〜と言えるでしょう」「〜ではないでしょうか」→ remove hedging entirely
- Generic transition phrases used as filler (一方で / さらに / しかしながら)
- Watered-down claims: 「高い性能を誇る」→「Sol 53.6% vs Fable 5 adaptive reasoning」
- Every qualitative claim gets a quantitative replacement or is deleted

**Firing order**: Apply T1 as the **final pass only** — after all other techniques are done. If applied during writing, you lose signal that the other techniques depend on.

**Mechanical verification (re-runnable)**: after the manual pass, run this grep to prove no slop tokens survive (used successfully 2026-08-03):
```bash
grep -nE "画期的|革新的|注目すべき|〜でしょう|ではないでしょうか|一方で|さらに、|しかしながら|高い性能を誇る|急速に進化" <digest-file> || echo NO_SLOP_FOUND
```
Treat any hit as a T1 failure and fix before delivery.

#### T2: Manual of Style

```
- Japanese, concise bullet structure
- Every claim must have a source (wikilink or URL)
- One insight per bullet. No padding.
- Major comparisons in table format
- No speculative claims without attribution
- Each section starts with the emoji + ranked heading
```

#### T3: Atomic Snippets

Every topic section uses a strict 3-layer structure:

```
**▶ 一言要約**: (15-30 tokens — the elevator pitch, self-contained for skimmers)
**詳細**: (bullet list, 100-300 tokens — key facts, numbers, concrete claims)
**深掘り**: (optional paragraph — technical detail, wikilinks, cross-references)
```

The **一言要約** MUST stand alone — a reader stopping after the first sentence should understand the topic's essence. The **詳細** contains all sourced claims. The **深掘り** connects to the wiki's durable knowledge via wikilinks.

#### T4: Generate-Rank-Select

For the report title and introductory paragraph:
1. Generate exactly 2-3 variants
2. Evaluate each by: information density, clarity, keyword coverage
3. Document which was selected and why (in the thinking trace, not the output)
4. Do NOT submit the first pass

#### T5: Engram Pathways

Before writing, search the wiki for related pages (git log, wiki/log.md, entity/concept pages). Each topic must embed **minimum 2 wikilinks** to existing entities, concepts, events, or raw sources. The links must be substantive (not decorative) — they connect the report's claims to the wiki's durable knowledge.

**Placement rules**: Wikilinks go in the 「詳細」 and 「深掘り」 sections. The 「一言要約」 stays link-free (optimized for skimmers and auto-delivery truncation).

**Verify every wikilink target exists on disk before committing** (2026-08-03): the wiki carries ~2,000 unresolved L2 links (7/31 graph analysis), so an unverified link is likely broken. Batch-check with:
```bash
cd ~/ai-topics && for f in <target1> <target2> ...; do [ -f "wiki/$f.md" ] && echo "OK $f" || echo "MISS $f"; done
```
Fix MISS lines (use the real page path from `wiki/index.md` or `find`) before writing the digest. Note `concepts/mcp.md` and `concepts/model-context-protocol-mcp.md` can both exist — prefer the path the log entries actually reference. **Directory-index pages report false MISS** (observed 2026-08-09): `concepts/coding-agents/` exists only as `concepts/coding-agents/_index.md`, so `[ -f wiki/concepts/coding-agents.md ]` fails while `[ -f wiki/concepts/coding-agents/_index.md ]` passes. Check the `_index` path for any MISS that looks like a category dir, and wikilink as `[[concepts/coding-agents/_index]]`.

#### Weekly Digest Pitfalls

- **7-day data = more noise**: Apply the signal-vs-noise heuristics (Curation: Signal vs Noise section) more aggressively. A topic appearing in 3-4 sources over 7 days is a slow burn, not an event cluster.
- **Monday cross-check**: The previous weekly digest (last Monday) wrote its own log entries. Cross-check against `git log --since` and `wiki/log.md` to avoid re-covering the same ground. **But the last weekly digest may NOT be last Monday** — observed 2026-08-03: the previous digest was 2026-07-13 (3 weeks prior; the 07-20 and 07-27 runs didn't produce files). `find inbox/rss-scans -name 'weekly-ai-digest-*.md'` first. Dedupe anchor = the most recent daily `trending-topics-*.md` report (they cover 7/31→8/2 well); format template = the most recent existing weekly digest.
- **Verify inferred dates/numbers against wiki pages before writing** (2026-08-03): draft claimed MCP RC was "2026-06-11" from inference — grep of `concepts/model-context-protocol-mcp.md` showed the stateless RC was actually "since May 2026". Any date/number you did not copy verbatim from a wiki page or raw article must be grepped before it ships. Wiki pages are the ground truth for the digest, not the LLM's prior.
- **`hermes-report-quality` dual-path collision**: the weekly-ai-digest cron job lists `hermes-report-quality` for loading, but it exists in BOTH `~/.hermes/skills/wiki-daily-report/hermes-report-quality/` and `~/ai-topics/config/hermes/skills/_overrides/wiki-daily-report/hermes-report-quality/` at the SAME categorized path → loader reports "skill not found / skipped". This is NOT a missing skill. The T1-T5 techniques are fully documented in this skill's Weekly Digest Mode, so the failure is non-blocking — proceed with this skill's guidance and note the warning is a known collision artifact. **Applies to daily runs too** (observed 2026-08-05): loading `wiki-daily-report/hermes-report-quality` ALSO returns ambiguous (2 matches), and the job listed `llm-wiki` / `daily-rss-triage` which were reported "not found and skipped" despite existing in the skills list — same loader-collision class, non-blocking.
- **Commit requirement**: Unlike daily reports, the weekly digest MUST be committed (`git add inbox/ && git commit -m "wiki: weekly AI digest YYYY-MM-DD"`) and pushed — the user relies on the audit trail.
- **Memory unavailable in cron**: The `memory` tool is blocked in cron mode. All cross-session context comes from wiki pages, git log, and raw articles — not memory.
- **Anti-Examples firing order**: T1 is the final polish pass for a reason. Applying it too early strips the draft of the concrete language that T4 and T5 need to evaluate and link.
- **Never invent URLs or identifiers — raw frontmatter is the source** (2026-08-17): the digest draft shipped `https://arxiv.org/abs/2608.0xxxx` for the reasoning-trace paper until the final review pass caught it. Raw article frontmatter carries canonical links (`source:`, `url:`, `paper_url:` fields — the stolen-thoughts.com/paper.pdf URL came straight from frontmatter). Grep `head -40 wiki/raw/articles/<file>.md` for `paper_url`/`url`/`source` before writing any link. Extend the 08-03 date-verification rule to URLs: a link you did not copy verbatim from a wiki page or raw article must not ship. Run URL/wikilink verification together with the T1 slop grep as the final gate.
- **Stats block enumeration via git diff-filter** (2026-08-17): count new L2 pages for the digest stats section with `git log --since="7 days ago" --name-status --diff-filter=A --format="" -- wiki/ | grep -E "^A" | awk '{print $2}' | sort -u`, then bucket by `concepts/` / `entities/` / `events/` prefix (ignore `raw/` + `archived/` noise). `git log --since --oneline -- wiki/ | wc -l` = 総コミット; `--diff-filter=M | grep -cE "^M"` = 更新ファイル数. This is more accurate than find-based discovery for the digest stats block.


## Pricing Monitoring

LLM API pricing monitoring is handled as a specialized sub-mode of this skill. See:
- `references/pricing-page-scraping.md` for provider-specific fetch commands and parsing strategies
- The archived `llm-pricing-monitor` skill (absorbed into this skill) for the complete standalone pricing workflow

## Linked Files

| File | Purpose |
|------|---------|
| `references/blogwatcher-db-recipes.md` | Exact SQL queries for blogwatcher DB (total articles, top blogs, AI-relevant articles, unread counts) |
| `references/raw-article-discovery.md` | `find` commands and filename convention for locating raw articles by date or keyword |
| `references/pricing-page-scraping.md` | Provider-specific curl commands for fetching live pricing data (OpenAI SPA pitfall, Anthropic, Google, DeepSeek) |
| `references/cross-reference-workflow.md` | Worked example from 2026-06-13: mapping trending_topics.py output against blogwatcher DB titles to separate signals from noise |
| `references/cross-reference-2026-06-21.md` | Worked example from 2026-06-21: slow-week heuristics, thematic clustering, HN score tiebreaker |
| `references/cross-reference-2026-07-01.md` | Worked example from 2026-07-01: normal-volume day with multiple launch events + economic debate + conference coverage + MCP ecosystem expansion. Shows SPA fallback gap for blogwatcher-only articles without raw files. |
| `references/wiki-ingestion-workflow.md` | Full workflow for ingesting report recommendations into wiki: deduplication, delegation, tag validation, git staging |
| `references/direct-patch-ingestion.md` | Faster manual alternative for 3-8 updates: gap analysis via index, targeted patches, no delegation overhead |
| `references/hn-algolia-discovery.md` | HN Algolia API as a fourth trending source: endpoint selection, multi-query dedup, /items/{id} num_comments=0 workaround, point thresholds by day type, wiki relevance tagging |\n| `references/active-crawl-output-reuse.md` | Reusing the 11:00 UTC active-crawl research note as primary HN/X/gap-analysis data source, avoiding duplicate queries |
| `references/cross-reference-2026-07-10.md` | Worked example from 2026-07-10: **fire hose day** with 5+ simultaneous megalaunches (GPT-5.6, GPT-Live, AI Engineer Conference, benchmark politicization, security incidents). Shows coordinated signal detection, security story pairing, opinion piece de-prioritization, and ranking compression heuristics. |
| `references/cross-reference-2026-07-11.md` | Worked example from 2026-07-11: **company monoculture day** (OpenAI dominates 5 of 7 topics). Documents the coordinated campaign rule violation (SWE-Bench + GPT-5.6 split when they should be one topic), the new company-monoculture heuristic, and memory crisis article survival patterns. |
| `references/cross-reference-2026-07-14.md` | Worked example from 2026-07-14: **CEO essay cluster + conference cluster + model competition** — normal volume week. Documents the CEO/thought-leader essay detection pattern, CEO essay weighting heuristic, X bookmark tiebreaker application, and conference cluster handling with agent governance thematic clustering. |
| `references/cross-reference-2026-07-16.md` | Worked example from 2026-07-16: **high-density multi-thematic week** with model launch + regulation + security + economics + hardware + extreme quantization. Documents the content-series cluster pattern (Merge Blog model comparisons), CEO essay heuristic confirmation, SPA vs timing-based raw-file availability, and the generic "GPT" false-positive page candidate. |
| `references/cross-reference-2026-07-17.md` | Worked example from 2026-07-17: **security incident cluster day** (Grok Build + Codex + Cursor incidents from 3 companies). Documents the multi-company security-cluster pattern, active-crawl research note filename quirk (`*trending-topics-research*` not `*active-crawl*`), Merge Blog anti-bot gate, and single-source novelty validation (Modal 1M sandboxes). |
| `references/cross-reference-2026-07-19.md` | Worked example from 2026-07-19: **multi-thematic weekend** — lawsuit cluster (Apple vs OpenAI, single-source authoritative depth), product reversal (Fable 5), conference cluster (AI Engineer, 14 talks), safety research (Agentic Misalignment). Documents the "yesterday's research note as fallback" pattern and the authoritative single-source depth heuristic. |
| `references/cross-reference-2026-07-31.md` | Worked example from 2026-07-31: high-volume day with NO active-crawl note. Amends the volume-based skip rule (targeted HN point-score queries still calibrate ★ ratings), documents reading yesterday's report first to dedupe topics, the `curl|python3` scanner block + WSJ bot-shell + plan-only delegate summaries, and wiki frontmatter `updated:` checks before recommendations. |
| `references/cross-reference-2026-08-01.md` | Worked example from 2026-08-01: second consecutive no-active-crawl day, volume-based skip with 6 targeted HN queries only. Documents the overnight price-war response pattern (OpenAI cut → DeepSeek reply), **newsletter subject-line validation** (filenames carry AINews subjects verbatim), future-dated blogwatcher DB articles, and frontmatter `updated:` checks marking 4 of 7 wiki actions already done. |
| `references/cross-reference-2026-08-02.md` | Worked example from 2026-08-02: third consecutive no-active-crawl day (volume-based skip now the stable default). Documents the **multi-party governance open-letter cluster** pattern (3 letters from opposing camps = ONE topic), the price-war cascade theme chain (cost → speed → router deprecation), and the `log.md`-tail technique for ✅ DONE detection complementing frontmatter checks. |
| `references/cross-reference-2026-08-03.md` | Worked example from 2026-08-03: **weekly digest mode**. Documents: previous weekly digest may be 3 weeks stale (not last Monday) — dedupe against daily reports instead; `hermes-report-quality` dual-path collision producing a false "skill not found" cron warning; date-verification catch (MCP RC "2026-06-11" → actually "since May 2026"); T1 slop grep; T5 wikilink existence batch-check. |
| `references/cross-reference-2026-08-03-daily.md` | Worked example from 2026-08-03 (Monday **daily** run, ~12h after the weekly digest): digest-as-dedup-anchor on Mondays; digest-miss hunt (OpenAI Astra missed by both prior reports); `head -80 wiki/log.md` head-scan as the fastest "already done" check (5/7 actions done); HN point growth between scrape and report. |
| `references/cross-reference-2026-08-05.md` | Worked example from 2026-08-05: missing previous-day report (anchor = 08-03); morning-pipeline dedup via log.md head-scan (7/9 actions already done); brotli scrape-failure stub pattern; OpenAI News JS gate; trending script 0-newsletter quirk; HN calibration table for 8 topics; T1 slop grep on a daily report. |
| `references/cross-reference-2026-08-06.md` | Worked example from 2026-08-06: no active-crawl note (volume-based skip + 9 targeted HN queries); DeepMind-exodus top story already ingested by newsletter-wiki-ingest; 4-org security cluster pre-ingested by morning pipelines; old-story re-surfacing → patch existing page not create (Anthropic cryptanalysis); Cloudflare tag-soup scrape pattern; WordPress.com body-anchor extraction. |
| `references/ainews-fulltext-extraction.md` | AINews full-text extraction via open.substack.com (dead redirect URLs are not a dead end); AI Twitter Recap as free X-scan substitute; HN Firebase topstories quick calibration. Worked example 2026-08-08 (Astra critical, Zawinski's Law, SWE-bench harness, Databricks cost controls). |
| `references/cross-reference-2026-08-09.md` | Worked example from 2026-08-09: **7th consecutive no-active-crawl day** (volume-based skip is now the stable default); "wiki-ingested ≠ reported" gap (Oracle/OpenJDK 530pts was wiki-covered but never reported); newsletter subject scan surfacing DeepSeek price reversal + ByteDance 10T (low-HN + high-authority overlap → ★★★★☆); `_index.md` wikilink false-MISS pitfall; AI Engineer conference second-wave cluster. |
| `references/cross-reference-2026-08-11.md` | Worked example from 2026-08-11: **8th consecutive no-active-crawl day**; KEY NUANCE — no research-note file ≠ no active-crawl work (log.md head-scan is the reliable signal; active-crawl ran, created 5 pages + 2 enrichments, wrote no note); **zero-residual wiki-action day** (all 7 topics pre-ingested by morning pipelines); HN-low/X-engagement rescue heuristic (Muse Glimmer HN 4pts → ★★★★★ via X 944K + Reddit 2141); multi-report dedup grep across 08-05→08-09; daily report git-untracked (save-only confirmed). |
| `references/cross-reference-2026-08-13.md` | Worked example from 2026-08-13: **Frontier Model Day / multi-lab launch cluster** (4 labs in 48h = 4 separate topics + intro concentration note); **HN date-mixing pitfall** (Qwen3.8-Max 546pts hit was 7 days old — check `created_at` before ★ calibration); residual-work detection (page `updated:` bumped ≠ event section present — grep content, e.g. qwen-3-8.md missing the weights-drop section); save-only confirmed. |
| `scripts/trending_db_query.py` | Combined 3a+3b keyword DB query (total, top blogs, 120 AI-relevant titles, unread health) — drop-in replacement for the hand-written /tmp query script, takes `days` arg (default 3, use 7 for weekly mode). |
| `scripts/hn_calibrate.py` | HN Algolia targeted point-score queries for ★ calibration — urllib direct-fetch, search_by_date, `%3E`-encoded numericFilters, default query list + argv override. Verified cron-safe 2026-08-15. |
| `references/cross-reference-2026-08-15.md` | Worked example from 2026-08-15: **report-miss ≠ wiki-miss** (4 stories missed by 8/13 report but wiki-covered → still report as NEW topics); residual carryover verification by keyword grep not frontmatter date; 3rd recurrence of active-crawl-runs-without-note. |
| `references/cross-reference-2026-08-17.md` | Worked example from 2026-08-17: **weekly digest mode**. Documents: fabricated-URL catch (arXiv ID placeholder replaced from raw frontmatter `paper_url:`), stats-block enumeration via `git log --diff-filter=A`, hermes-report-quality collision recurrence (non-blocking), skill bare-name ambiguity workaround (read_file either copy), T4 title selection rationale. |

## Key Pitfalls

### 1. Skill Name Collision (Dual-Path)

This skill exists in **two locations** with the same bare name `trending-topics-reporting`:
- `~/.hermes/skills/research/trending-topics-reporting/` (default)
- `~/ai-topics/config/hermes/skills/_overrides/trending-topics-reporting/` (repo override)

When loading with bare name `skill_view(name='trending-topics-reporting')`, Hermes returns an ambiguous error. **Always use the categorized path**: `skill_view(name='research/trending-topics-reporting')`. If editing, patch both copies or ensure the `_overrides/` version (repo-canonical) stays current.

### 2. Dual Article Storage Paths
The cron HOME mismatch means raw articles may be in **either** of two locations:
- `/opt/data/ai-topics/wiki/raw/articles/` — canonical (used by most pipelines)
- `/opt/data/.hermes/home/wiki/raw/articles/` — cron HOME (used by blog-ingest scripts)

Always use `find` to discover articles:
```bash
find /opt/data/ai-topics /opt/data/.hermes/home -path "*/raw/articles/*" -name "*keyword*" 2>/dev/null
```
`trending_topics.py` reads from **both** paths via the canonical wiki dir — but new articles from today's blog-ingest may only be in the cron HOME path until the next sync.

### Blogwatcher DB may not have recent data
If the DB scan or ingest scripts failed, the trending_topics.py output may show 0 sources. In this case:
- Check `~/.hermes/cron/data/blog_ingest/latest.json` for the latest checkpoint
- Scan `~/wiki/raw/articles/` and the cron HOME fallback directly for any recent `.md` files
- Fall back to `web_search` for broader context if needed

### Future-dated articles appear in DB range queries
`published_date >= date('now', '-3 days')` also returns articles whose published_date is in the **future** (observed 2026-08-01: a Sierra post dated 2026-08-03 showed up in the -2 days window; the post was live, just scheduled/dated ahead). Do not drop a topic just because its DB date looks ahead of today — verify the URL is live with curl. Conversely, don't treat the future date as a signal that the story is somehow bigger than it is; it's a scheduling artifact of the source blog.

### RSS-Discovered Articles Without Raw Files (SPA Content Gap)

Many articles appear in the blogwatcher DB (via RSS) but have **no corresponding raw article file** — the blog-ingest pipeline may not have fetched them, or the site returned empty HTML (SPA pattern).

This affects **company engineering blogs on SPA frameworks** disproportionately:
- **Ghost blog users** (Arena, Modal, Voyage AI) — almost always have SSR, `curl` extraction works
- **Static-site blogs** (Simon Willison, LWN, Pluralistic) — always have raw files
- **Pure React SPAs** (Ramp Builders, Augment Code, some Next.js sites) — `curl` returns only "You need to enable JavaScript"

**Procedure when an article has RSS entry but no raw file:**
1. `curl -sL <URL> -o /tmp/article.html` and attempt text extraction with `re.sub(r'<[^>]+>', ' ', html)`
2. If that yields < 100 meaningful characters → SPA → use `web_search` agent tool with the article title
3. If `web_search` unavailable in cron mode → use `delegate_task` with `web` toolset to fetch and summarize

**New failure modes for raw files that EXIST but contain no content** (observed 2026-08-05):
- **Brotli scrape-failure stub**: the sitemap scraper can write a raw file containing ONLY `Scrape failed: brotli: decoder process called with data when 'can_accept_more_data()' is False` (ElevenLabs ASR post — file was 14 lines, zero content). Treat as missing: grep `Scrape failed` / check file size (<1KB) before deep reading, retry `curl -sL --compressed <URL>` (the error indicates Content-Encoding: br mishandling), else fall back to web_search / secondary coverage.
- **OpenAI News JS gate**: `openai.com/index/*` pages return exactly `Enable JavaScript and cookies to continue` to curl (fingerprint-style gate, distinct from the SPA 'You need to enable JavaScript.' message). Don't retry curl variants — report the title + secondary coverage with attribution and mark `本文未取得` in the report (observed 2026-08-05 third-party-cyber-evaluations post; AISI report reference in the wiki carried the substance).
- **Cloudflare tag-soup scrape** (observed 2026-08-06): Cloudflare blog pages (`blog.cloudflare.com/cloudflare-os/` etc.) can scrape as ~25KB that looks healthy but is pure tag-cloud soup — frontmatter + title + a wall of tag names (Cloudflare Access, Workers, Durable Objects, ...) with NO article body. Distinct from the brotli stub (contains an error string) and the JS gate (contains a message). Detection: file size looks fine but grepping a distinctive article phrase fails. Workaround: read the active-crawl-created wiki concept page (e.g. `concepts/cloudflare-os.md` — contains the synthesis) instead of the raw file; Cloudflare blog is a tracked RSS source so expect this to recur.

**Track this pattern**: In AI Engineer Conference sessions, wheresyoured.at essays, and Modal/Voyage announcements, raw files almost always exist. Incompany engineering blogs on modern frameworks, they often don't. Prioritize raw-file-available articles for deep reading unless the missing article is clearly central to a hot topic.

### Cron HOME != canonical HOME
In cron mode, `HOME=/opt/data/.hermes/home` not `/opt/data`. The `~` resolves differently. Always use absolute paths.

### `web_search` is NOT available in terminal
Use the search tool or browser tool for web searching. The terminal has no `web_search` command.

### SPA Pages Return Stale Data via Browser Scraping
SPA pages (like OpenAI pricing at `developers.openai.com`) load data dynamically via JSON hydration. Browser-based scraping (`delegate_task` with `browser` toolset) often returns **stale cached HTML** with empty or outdated model data. The correct approach:

**OpenAI (Astro, not Next.js as of mid-2026)**: The page uses Astro v6.0.4+ and embeds pricing data as inline arrays in HTML, NOT as `__NEXT_DATA__`. Extract with:
```bash
curl -s 'https://developers.openai.com/api/docs/pricing' -o /tmp/openai_pricing.html
# Then parse the [0,&quot;model&quot;],[0,input],[0,cached],[0,output] tuples
```
See `references/pricing-page-scraping.md` for the full extraction regex.

**Anthropic (docs.anthropic.com)**: Use the developer docs page, not the consumer pricing page:
```bash
curl -sL 'https://docs.anthropic.com/en/docs/about-claude/models' -o /tmp/anthropic_docs.html
```

**Cross-provider check**: OpenRouter API at `openrouter.ai/api/v1/models` returns structured JSON for all providers — best single-source verification.

### Keyword List Has Blind Spots for Events and Product Launches

The `ai_keywords` list in `references/blogwatcher-db-recipes.md` Query 3a is tuned for technical AI/ML content (models, training, agents, safety) but systematically misses conference/event coverage (WWDC, Google I/O, GTC), product-specific names (Siri AI, North Mini Code), author opinion pieces (George Hotz essays, Dario Amodei policy posts), and socio-economic AI topics (deflation, regulation, national security).

**Fix**: Always run Query 3b (broader event/product catch-all) alongside Query 3a. The event keyword list covers platform names, announce verbs, conference names, and editorial formats (essay, interview, thoughts on). See the updated reference file for both keyword lists.

### Pricing Data Must Be Fetched Live
When updating `wiki/comparisons/llm-api-pricing.md`, **always fetch from the provider's official pricing page** at update time. Never use cached wiki data, raw articles, or previously scraped snapshots as the source of truth. See `references/pricing-page-scraping.md` for provider-specific fetch commands.

### `execute_code` blocked in cron mode
The `execute_code` tool is blocked in cron mode for security reasons. Do NOT attempt to use it for the DB query phase — it will fail with `BLOCKED: execute_code runs arbitrary local Python (not allowed in cron mode)`. Always run inline Python via `terminal` with `python3 -c "..."`, as shown in the Phase 1 queries above.

### `curl | python3` blocked by the security scanner — fetch to file first
`curl -s URL | python3 -c ...` is denied in cron mode (`tirith:curl_pipe_shell`, "pipe to interpreter"), even when the pipe only parses JSON. Always split into two steps:
```bash
curl -s --max-time 20 "https://hn.algolia.com/api/v1/search_by_date?query=GPT-5.6%20price&tags=story&hitsPerPage=8" -o /tmp/hn.json
# then parse /tmp/hn.json in a SEPARATE terminal call
```
Also beware `.dev`-TLD lookalike blocks (`tirith:lookalike_tld`, e.g. merge.dev) and paywalled bot-shell pages (WSJ returns ~767-byte shells to curl). Don't fight the scanner — fall back to blogwatcher-DB title/URL data or secondary coverage (HN titles, NYT/FT links) with attribution. Never fabricate content of a paywalled op-ed; report title + secondary coverage instead.

### Quick story verification: prefer HN Algolia curl-to-file over delegate web research
For existence/engagement checks (e.g. "is this op-ed real, what are its points?"), HN Algolia `search_by_date` via curl-to-file is fast and reliable. Observed 2026-07-31: `delegate_task` subagents with the `web` toolset twice returned plan-only summaries (no actual results) for the same verification question — treat such summaries as a failed result and fall back to Algolia, rather than retrying the delegate.

### Newsletter Digest URLs Are Often Unusable

AINews and other Substack-based newsletter digests use obfuscated redirect/tracking URLs. When a candidate topic appears only in newsletter sources (counted by `trending_topics.py`) without blogwatcher DB entries or raw article files, those newsletter URLs typically cannot be resolved to actual content — they are Substack redirects that don't expose the real article URL.

**Procedure when a candidate topic has only newsletter sources:**
1. Treat it as a **weak signal** — confirm via blogwatcher DB Query 3 (AI keywords) or Query 3b (event keywords). If 3+ distinct blogwatcher DB sources exist, the topic is real.
2. If blogwatcher DB also has no hits but the newsletter title reveals a specific event (e.g., "OpenAI launches GPT-5.6 Sol"), use `web_search` with the article title as query.
3. For **breaking stories** (model launch, security incident, policy change) that only appear in newsletters but not yet in blogwatcher DB — check the active-crawl research note. The 11:00 UTC active-crawl job often catches HN/X coverage before RSS cycles.
4. Topics supported solely by newsletter-substack-URL counts and not validated by blogwatcher DB, raw articles, or active-crawl research should be **dropped** from the report.
5. **Newsletter subject lines are valid event signals even when every URL is dead** (2026-08-01). AINews digest subjects act as a same-day event log: "🐋 DeepSeek Answered OpenAI's Price Cut Overnight" (7/31) confirmed the DeepSeek-V4-Flash-0731 launch narrative before the blogwatcher hits were cross-referenced, and "not much happened today" (8/1) correctly predicted a quiet day. The filenames in `wiki/raw/newsletters/` carry the subject verbatim (`2026-07-31-deepseek-answered-openai-s-price-cut-overnight.md`) — `ls -t` on that dir is a cheap subject-line signal scan. When a model-launch / price-war / policy story appears as a digest subject, treat it as weak-but-real confirmation: verify with HN Algolia curl-to-file for points, then keep the topic if the event is real.
6. **`trending_topics.py` can report 0 newsletters while newsletter files exist** (observed 2026-08-05: 11 digest files on disk in `wiki/raw/newsletters/`, script counted 0). Do NOT treat 0 as "no newsletter signal" — always run the `ls -t` subject scan regardless of the script's count; the 8/5 AINews subject "megakernels are so dead and so back" confirmed the MoK topic before cross-reference.
7. **AINews full-text IS extractable via open.substack.com** even when every redirect URL is dead (observed 2026-08-08). The digest filename slug maps to `https://open.substack.com/pub/swyx/p/<slug>`; curl it, strip tags, anchor on the subtitle text. The body includes the **AI Twitter Recap** — a curated scan of ~544 Twitters / 12 subreddits with engagement numbers that functions as a free daily X-scan substitute when the active-crawl note is absent. It surfaced 4 of 8 topics on 8/8 (Astra critical status, Claude Code cross-session messaging 554K views, SWE-bench harness analysis, Databricks cost controls). Full recipe + worked example: `references/ainews-fulltext-extraction.md`.

### HN point counts grow during the day
A raw article's embedded HN point count (captured at scrape time) can lag the live Algolia count by an hour of votes (observed 2026-08-03: Qwen3.8-Max raw file said 623 pts, live Algolia `search_by_date` showed 683pts/339c minutes later). For ★ calibration and the report, always re-query HN Algolia and cite the live number.

### HN Algolia model-name queries mix dates — check `created_at` before calibrating
For model-name queries (e.g. `Qwen3.8-Max`), `search_by_date` returns hits from MANY different days — the top hit may be an OLD high-point story (546pts agentic-index ranking from 8/6) that does NOT validate the current event (the 8/12-13 open-weights drop, which itself had no dedicated HN points). Before using a hit's points for ★ calibration, verify its `created_at` falls inside the analysis window. Otherwise cite the old story as context, not as validation of the current event. Observed 2026-08-13: Qwen3.8-Max weights-drop story had zero HN points in-window; the 546pts hit was 7 days old. Also note `query` with a dot (e.g. `Qwen3.8-Max`, `Grok 4.6`) still matches — no need to strip punctuation, but confirm the titles/URLs are actually about the current release.

### Report content length
Keep the final report concise — 5-8 topics with 3-5 sentences each. The auto-delivery system has a character limit. A full report is typically 4-8KB.

## Report → Wiki Ingestion

After the report is delivered, the recommended wiki actions need to be manually ingested. This is a **separate step** from report generation — the trending-topics job only generates the report, it doesn't modify the wiki.

**Two workflows available:**
- **Delegation-based** (10+ updates, cron): See `references/wiki-ingestion-workflow.md`
- **Direct-patch** (3-8 updates, interactive): See `references/direct-patch-ingestion.md` — faster for small batches, works inline without subagents

**Full workflow**: See `references/wiki-ingestion-workflow.md`

### Quick Steps

1. **Locate output**: `~/.hermes/cron/output/158a461eb520/YYYY-MM-DD_HH-MM-SS.md`
2. **Deduplicate**: Check if recommended pages already exist (blog-wiki-ingest, dreaming-wiki-ingest, and other pipelines may have already created them)
3. **Delegate**: Use `delegate_task` batch mode (up to 3 parallel) for independent page create/update operations
4. **Validate tags**: Subagents often introduce invalid SCHEMA.md tags — fix before committing
5. **Selective staging**: `git reset HEAD` + `git add` only relevant files (working directory usually has unrelated changes)
6. **Commit + push**: `cd ~/ai-topics && git commit -m "wiki: ingest trending-topics report YYYY-MM-DD" && git push`

### Key Pitfall: Most Actions Are Already Done

The trending-topics report runs at 12:00 UTC, **after** all morning ingestion pipelines (blog-wiki-ingest at 07:50, newsletter-wiki-ingest at 07:40, etc.). By the time you ingest the report, 50-80% of the recommended actions are typically already reflected in the wiki. Always check existing pages before creating new ones.
**Fastest completion check — `head -80 wiki/log.md`**: log.md has newest entries at top, so the first ~80 lines show today's full pipeline activity (active-crawl 11:03, newsletter-wiki-ingest 11:00, blog-wiki-ingest 10:35, blog-triage 10:24, llm-pricing-monitor 10:00 — all before trending-topics). This catches pages already created/updated AND "verified already executed (commit …)" entries in ONE read — faster and more complete than per-page frontmatter `updated:` checks. Observed 2026-08-03: 5 of 7 recommended actions were already done (openai-astra created, qwen-3-8 enriched, anyscale updated, boris-cherny verified, ai-music-copyright created); residuals were stale pages (`entities/qwen.md` 7/15, `entities/claude-code--capabilities.md` 5/26). Verify residual paths with `[ -f wiki/<path> ]` before recommending.
**Zero-residual day** (observed 2026-08-11): when active-crawl ran AND newsletters carried the same stories, morning pipelines fully pre-ingested ALL 7 candidate topics — the wiki-action table becomes an all-✅ statement (「残作業なし」) and no ingestion step follows. This is now the expected outcome when the log.md head-scan shows active-crawl 11:00 + newsletter-wiki-ingest 11:00 + blog-wiki-ingest 10:50 all firing; do not invent residual work to make the table non-empty.

**Report-miss ≠ wiki-miss (observed 2026-08-15)**: log.md head-scan tells you what the WIKI covered; the last report's topic list tells you what was REPORTED — these are independent artifacts. On 08-15 the 8/13 report (generated 12:19 UTC) had missed 4 major stories (Gemini 3.7 Flash 953pts, GLM-5.3 1103pts, GPT-5.6 Sol Ultrafast 701pts via Cerebras, OpenAI/Anthropic IPO wave) even though the wiki fully covered all of them. When the last report is a gap day (missing 08-14) or was generated early, check the pipelines' newly-created pages against the last report's topic list: if a wiki-covered story is absent from the last report AND has high HN points (>400), report it as a NEW topic — do NOT dedupe it away just because the wiki page exists. The report is the user-facing deliverable; the wiki is the durable layer. Recipe + worked example: `references/cross-reference-2026-08-15.md`; point scores via `scripts/hn_calibrate.py`.

**Residual carryover across reports (observed 2026-08-15)**: wiki-action residuals flagged in a prior report can stay pending for days. The 8/13 report's only residual (qwen-3-8.md missing the "open-weights actually released 8/12-13" section) was STILL un-done on 8/15. Verify residual state by keyword grep of the target page (`grep -niE "vllm|b300|unsloth|4bit" wiki/concepts/qwen-3-8.md`), NOT by frontmatter `updated:` date — a page can be touched without containing the required section. Carry genuine leftovers forward in the action table with the 「残作業（YYYY-MM-DD由来）」 label instead of silently dropping them.

## Cron Job Context

- **Schedule**: 12:00 UTC (21:00 JST) daily
- **No user present** — make all decisions autonomously
- **No asking questions** — reasonable interpretation wins
- **Japanese output** required as the user reads Japanese
- **Save to `inbox/rss-scans/`** for audit trail
- **No commit needed** — this is a report, not wiki content. Verified 2026-08-11: `git ls-files inbox/rss-scans/` shows daily reports (e.g. trending-topics-2026-08-09.md) are UNTRACKED; only weekly digests are tracked. This job is save-only. (daily-rss-triage's "commit and push" instruction belongs to the scan/triage/ingest pipeline, not this report-only job.)
