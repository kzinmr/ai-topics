## [2026-07-20] entity-wiki-enrich | Meta-Anthropic $10B compute deal

**Pipeline**: manual enrichment
**Enriched**: [[entities/meta]] — Added Meta-Anthropic Compute Deal section ($10B+ compute leasing deal reported July 17, 2026; Meta provides compute to rival Anthropic as "third compute landlord")
**Source**: [[raw/newsletters/2026-07-19-google-clones-you-meta-powers-anthropic-and-thinking-machines-opens-the-vault.md]]
**Index**: No change (entity already exists).

## [2026-07-20] entity-wiki-create | New entity page: VAST Data

**Pipeline**: entity-wiki-create (manual request)
**New page**: [[entities/vast-data]] — VAST Data — $30B data storage and AI infrastructure company; GPU starvation problem, data-centric design philosophy, cold archive thesis, AI Operating System vision
**Source**: [[raw/newsletters/2026-07-19-you-re-wasting-a-lot-of-money-exclusive-interview-with-vast-data-s-sven-breuner-.md]]
**Tags added to SCHEMA.md**: `storage`, `data-layer`
**Index**: Entities 859→860 pages.

## [2026-07-19 18:20 UTC] dreaming-wiki-ingest | Confirmation — upstream dreaming-group already committed enrichment

**Upstream dreaming-group (18:00 UTC)**: Saturation analysis completed, Takes=0, 21 decisions archived.
## [2026-07-20 04:00 UTC] raw-backlog-ingest | All 5 articles already covered — Takes=0

**Batch**: 20260720T040009Z (5 candidates)
**Result**: All 5 articles already fully covered in existing wiki pages:
1. `reframing-superintelligence-fhi-2019.md` → concepts/cais.md + entities/k-eric-drexler.md
2. `2026-06-03_microsoft-mai-thinking-1-tech-report.md` → entities/mai-thinking-1.md + concepts/mai-thinking-1-tech-report.md + concepts/microsoft-mai-models.md
3. `benchflow-awesome-evals-2025.md` → concepts/ai-benchmarks/benchflow-tool.md
4. `dwarkesh.com--p-grant-sanderson-2--960d89cd.md` → entities/grant-sanderson.md
5. `wheresyoured.at--the-openai-bubble--eb7fc2d4.md` → entities/ed-zitron.md
**Archive**: 5 processed (2 newly archived, 3 dedup skipped). Total archives: 1792 URLs.
**No wiki pages created or modified.**


**Upstream commit**: `ac854382` — archive (9 newly archived, 12 dedup), log entry, and push already done.
**Downstream role**: Verify upstream completeness, confirm no additional enrichment needed.
**Triage JSON**: 21 decisions, Takes=0, Refs=0 — post-enrichment saturation state confirmed.
**Verification**: All reference candidates verified "already covered" by upstream. Filesystem scan of ~30 recent raw articles found no gaps.
**Action**: Downstream confirmation only. Upstream enrichment was complete.

## [2026-07-19 18:00 UTC] dreaming | Knowledge consolidation — saturation day, Takes=0

**Checkpoint**: 0 articles collected, 202 recent_raw_articles on disk (Jul 17-19).

**Pattern E triggered**: Filesystem scan of ~30 recent raw articles. All AI-relevant content already covered by daily pipeline (blog-ingest, newsletter-ingest, sitemap-monitor, active-crawl).

**Duplicate Check Summary**:
- Items skipped (already processed by other jobs): 21
- Gaps filled: 0
- Blog triage (12 decisions): all skip
- Newsletter triage (1 decision): skip

**Key articles assessed (all already covered)**:
- Anthropic Agentic Misalignment Summer 2026 → `concepts/agentic-misalignment.md` (4 failure modes, Petri tool)
- Capital One VulnHunter → `concepts/ai-vulnerability-detection-at-scale.md` (falsification engine, Claude Code skills)
- ZKSecurity/OpenVM CVE-2026-46669 → `concepts/ai-cryptographic-vulnerability-discovery.md` (zkao, 9.5h scan)
- Mozilla State of Open Source AI 2026 → `concepts/open-source-llms.md` (3.3% gap, 50× cost drop)
- Codex Resets tracker → `concepts/codex-resets.md` (created today)
- Agent Quota Resets → `concepts/agent-quota-resets.md` (created today)
- Simon Willison Claude Code Bun in Rust → `entities/simon-willison.md` (line 622-627)
- Sean Goedecke Overtraining/Grokking → `entities/seangoedecke-com.md` (lines 325-371)
- Hyperbo.la Code Reds/Token Mandates → `entities/hyperbo.md` (lines 24-37+)
- Semantic Kernel → Microsoft Agent Framework → `entities/microsoft-agent-framework.md`

**Non-AI content skipped**: Hex Technologies (3), Harvey blog (4), ElevenLabs accessibility, Anyscale Ray infrastructure, construction-physics, jim-nielsen, nesbitt.io, daringfireball, shkspr.mobi, seangoedecke Impro book review.

**Archive**: 21 candidates → 9 newly archived, 12 dedup skipped. Total archive URLs: 1,792.

## [2026-07-19 11:15 UTC] active-crawl — 4 new concept pages

**Crawl round**: trending topics from HN Algolia + X/Twitter + blogwatcher DB analysis. Cross-referenced against wiki coverage gaps.

**New pages**:
- `concepts/qwen-3-8.md` — Qwen 3.8: Alibaba's ~2.4T open-weight MoE model, announced July 19, 2026. Sources: qwen.readthedocs.io, @Alibaba_Qwen tweet, HN (206 pts)
- `concepts/agentic-misalignment.md` — Anthropic's agentic misalignment research: how LLMs act as insider threats, 4 failure modes documented (Summer 2026). Sources: anthropic.com/research/agentic-misalignment, alignment.anthropic.com, HN (101 pts)
- `concepts/codex-resets.md` — OpenAI Codex usage limit reset dynamics: 35 resets, avg 8.9-day interval, competitive strategy vs Anthropic. Source: codex-resets.com, HN (197 pts)
- `concepts/semantic-kernel.md` — Microsoft Semantic Kernel: open-source agent framework SDK for .NET/Python/Java. Sources: learn.microsoft.com, github.com/microsoft/semantic-kernel

**SCHEMA.md**: Added `semantic-kernel` tag to Products line.

**Index**: Concepts 1881→1887 pages.

**Raw articles saved**:
- `raw/articles/2026-07-19_qwen-3-8-launch.md`
- `raw/articles/2026-07-19_anthropic-agentic-misalignment.md`
- `raw/articles/2026-07-19_anthropic-agentic-misalignment-summer-2026.md`
- `raw/articles/2026-07-19_codex-resets.md`
- `raw/articles/2026-07-19_microsoft-semantic-kernel.md`
- `raw/articles/2026-07-19_microsoft-semantic-kernel-readme.md`


## [2026-07-19 07:40 UTC] newsletter-wiki-ingest — 0 takes (all skip)

- Newsletter: The Stage and the Factory Floor (Manu Sharma, beehiiv uid=383) — 20 URLs all expired (403)
- All 20 beehiiv tracking URLs returned HTTP 403 (expired token >12h post-send)
- Inbox pre-triage confirmed all links unresolvable
- No takes — all items archived as skip (already deduped)

## [2026-07-18 17:35 UTC] watchdog | Auto-fix summary

**Pipeline**: wiki-watchdog-fix (daily auto-healing)

**Index.html fixes:**
- FIXED Header count: Entities (857→858 pages) — index had 858 entries vs 857 in header
- FIXED Header count: Concepts (1878→1879 pages) — index had 1879 entries vs 1878 in header

**Index health verified:**
- Triple bracket corruption: 0 ✅
- Pipe prefix corruption: 0 ✅
- Line-number corruption: 0 ✅
- Duplicate entries: 0 ✅
- validate_index.py: clean (2812 lines) ✅
- Genuine stale index entries: 0 (graph analysis claim of 542 was false positive — recursive scan finds all subdirectory files)

**Graph analysis claims verified (from 2026-07-17 weekly):**
- '542 stale index entries' = FALSE POSITIVE — flat ls misses subdirectory files
- 38 orphans unchanged = partially false — actually 0 genuine orphans (all 38 are _index.md or archive files)
- context-engineering still missing (131 refs) = NEEDS HUMAN (requires page creation, out of scope)
- 6 duplicate entity pairs unresolved = NEEDS HUMAN (requires merges, out of scope)
- 106 stale pages (>90d) = NEEDS HUMAN (requires content refresh pipeline)
- 4,302 broken wikilinks = most are subdirectory paths or artifact patterns, not fixable in bulk

**Pipeline health:**
- Pipeline watchdog: 0 alerts ✅
- wiki-health-fix: ran before this watchdog ✅
- Tag compliance: 0 violations (10th week) ✅

---

## [2026-07-18 12:00 UTC] raw-backlog-ingest — 1 page enriched, 2 sources added

**Pipeline**: raw-backlog-ingest (backlog batch processing)

**Enrichments:**
- ENRICHED [[concepts/microsoft-mai-models]] — Added MAI-Thinking-1 architecture details (interleaved dense/MoE, LatentMoE, global load balancing), scaling ladder methodology, three-specialist RL training pipeline (STEM/Agentic/Safety climbs), training infrastructure (8K GB200, 90% goodput, 30T tokens from scratch, MAIA-200 inference)
  - Source: [[raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md]]

**Sources added:**
- [[concepts/evaluation/ai-evaluation]] — Added BenchFlow Awesome Agent Evals (443+ curated links, 146 deep reading notes) as resource
- [[concepts/evaluation/ai-evals]] — Added BenchFlow Awesome Agent Evals as resource
  - Source: [[raw/articles/benchflow-awesome-evals-2025.md]]

**Skipped (already captured):**
- [[raw/articles/reframing-superintelligence-fhi-2019.md]] — Already fully covered in concepts/cais, concepts/comprehensive-ai-services, entities/k-eric-drexler
- [[raw/articles/dwarkesh.com--p-grant-sanderson-2--960d89cd.md]] — Already captured in entities/grant-sanderson
- [[raw/articles/wheresyoured.at--the-openai-bubble--eb7fc2d4.md]] — Already captured in entities/ed-zitron

## [2026-07-18 11:00 UTC] active-crawl — 1 new page, 2 enrichments, 3 raw articles

**Pipeline**: active-crawl (hot-topics.yaml + trending discovery)
**Topics crawled**: 3 topics from 3 parallel subagent discovery (HN Algolia + X/Twitter + wiki gap analysis)

**New pages created:**
- NEW [[concepts/ai-cryptographic-vulnerability-discovery]] — AI-driven discovery of cryptographic vulnerabilities; ZK Security's zkao AI auditor found CVE-2026-46669 (critical soundness bug) in OpenVM's pairing library after 9.5h scanning; context engineering for cryptographic codebases; LLM-generated PoC unreliability
  - Source: [[raw/articles/2026-07-17_zksecurity-ai-cryptographic-vulnerability-discovery.md]]

**Enrichments:**
- ENRICHED [[concepts/ai-vulnerability-detection-at-scale]] — Added Capital One VulnHunter section: agentic AI code security scanner (open-sourced July 17, 2026); falsification engine architecture; forward attack-path reasoning; /vulnhunt -> /vulnhunter-fix -> /vulnhunt-fix-verify closed loop; Apache 2.0
  - Source: [[raw/articles/2026-07-17_capital-one-vulnhunter-agentic-code-security.md]]
- ENRICHED [[concepts/open-source-llms]] — Full enrichment from 25-line stub to comprehensive page: Mozilla's State of Open Source AI V1.0 data (3.3% capability gap, 50x inference cost drop, 79% dev adoption, ~$24.8B savings); Chinese open-weight dominance (18T vs 5.5T weekly tokens); harness layer as new frontier; MCP ecosystem stats; open weights vs open source debate
  - Source: [[raw/articles/2026-07-17_state-of-open-source-ai-2026-report.md]]

**Raw articles saved:**
- [[raw/articles/2026-07-17_zksecurity-ai-cryptographic-vulnerability-discovery.md]] — ZK Security blog: AI finds critical ZkVM bug
- [[raw/articles/2026-07-17_capital-one-vulnhunter-agentic-code-security.md]] — Capital One Tech: Announcing VulnHunter
- [[raw/articles/2026-07-17_state-of-open-source-ai-2026-report.md]] — Mozilla: The State of Open Source AI V1.0

**SCHEMA.md**: Added `cryptography` tag to Domain Concepts

**Discovery method**: 3 parallel subagents (HN Algolia 15 stories, X/Twitter 9 filtered results, wiki gap analysis 10 candidates). Topics selected via cross-referencing: VulnHunter (HN #9, 71 pts), AI Meets Cryptography (HN #6, 95 pts), State of Open Source AI (HN #2, 452 pts). Kimi K3 skipped (already covered, 213-line page from Jul 17).

## [2026-07-18 07:50 UTC] Blog wiki ingest — Fable 5 permanent, hyperbo enrichment, grokking/overtraining

**Pipeline**: blog-wiki-ingest (recovered from triage checkpoint after render failure)
**Source**: blog-triage checkpoint at `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json`
**Blogs**: 20 candidates → 2 takes, 2 references, 16 skip

**Enrichment executed**:
- Updated `[[entities/fable]]` (Market Dynamics section) — Fable 5 made permanent on Max/Team Premium (July 20), $100 credit for other users; competition from GPT-5.6 Sol and Kimi 3 cited by Simon Willison as driving Anthropic's strategic pivot; "Fablepocalypse Ends" subsection added
- Source: `[[raw/articles/simonwillison.net--2026-jul-18-claude-make-fable-5-permanent--c4a972b2.md]]`
- Enriched `[[entities/hyperbo]]` from skeleton to full entity page (52→111 lines) — three new sections: "Code Reds and Maintenance Loops" (Stripe Code Yellow, the 4-step failure loop, /goal infrastructure), "Token Mandates" (organizational discovery, randomized hill climbing, 5% rule), "Agent Engineering Connections"
- Sources: `[[raw/articles/hyperbo.la--w-code-reds-need-maintenance-loops--83920e0a.md]]`, `[[raw/articles/hyperbo.la--w-token-mandates--2d279dd2.md]]`
- Enriched `[[entities/seangoedecke-com]]` (381→432 lines) — new "Grokking and Overtraining" section with 5 subsections covering Gwern's Catapulting thesis, grokking mechanism (memorization→compression→generalization), 100-trillion-parameter model proposal, and Sean's assessment
- Source: `[[raw/articles/seangoedecke.com--overtraining-as-the-path-to-human-like-ai--67c86c06.md]]`

**Fixed**: Malformed frontmatter in entities/hyperbo.md (merged tags/type/status lines); pipe artifact in references list

**Referenced entities**: fable, hyperbo, seangoedecke-com

## [2026-07-18 07:20 UTC] Newsletter triage recovery & wiki enrichment

**Pipeline**: newsletter-wiki-ingest (recovered from triage checkpoint after render failure)
**Source**: newsletter-triage checkpoint at `/opt/data/.hermes/cron/data/newsletter/triage_latest.json`
**Newsletters triaged**: 5 (Vanishing Gradients, The Signal, Simon Willison, Superintel+, AINews)
**Total items**: 59 → 1 reference, 58 skip

**Enrichment executed**:
- Enriched `[[concepts/ai-agent-architecture]]` with Maven Clinic enterprise AI agent case study (lead agent + specialist pattern, evaluation methodology, release gating by consequence severity)
- Source: `[[raw/articles/2026-07-17-hugobowne-enterprise-ai-agent-healthcare.md]]`
- Removed `status: stub` from page frontmatter; added tags, sources, and cross-references to related concepts

**Referenced entities**: William Horton, Maven Clinic, Hugo Bowne-Anderson (Vanishing Gradients)

## [2026-07-18 12:00 UTC] YouTube video ingestion — Geoffrey Litt "Understanding is the new bottleneck"

**Video**: [Understanding is the new bottleneck — Geoffrey Litt, Notion](https://www.youtube.com/watch?v=WkBPX-oDMnA)
**Channel**: AI Engineer
**Duration**: 19:33
**Views**: 58,297

**Summary**: Autonomous coding agents still require human judgment. To guide agents well, you need to understand the work they are doing — not just verify correctness. Combines education and cognitive science with modern agent capabilities.

**Actions taken**:
- Downloaded English auto-captions via yt-dlp
- Cleaned VTT transcript (621 segments, deduplicated)
- Saved raw article with full transcript: `[[raw/articles/2026-07-10_geoffrey-litt-understanding-bottleneck]]`
- Saved separate transcript file: `transcripts/WkBPX-oDMnA_geoffrey-litt-understanding-bottleneck.md`
- Updated entity page `[[entities/geoffrey-litt]]` with raw article links in Speaking Engagements and Blog/Recent Posts sections

**Note**: This video was already referenced in the entity page from x-accounts-scan (2026-07-17), but the full transcript was not ingested until now.

## [2026-07-17 23:30 UTC] x-bookmarks-ingest — 2 bookmarks processed

**Bookmark 1 — Bret Taylor: "The Next Horizon in Agents" (Sierra Horizon)**

Sierra announced Horizon, a long-horizon agent platform that extends Agent OS beyond single conversations to multi-day/week/month goals. Horizon agents proactively engage customers, learn from each interaction, and operate on outcome-based pricing (not tokens). Bret Taylor frames two key theses: (1) customer relationship data as a durable, defensible moat that deepens as AI improves; (2) outcome-based pricing abstracts token costs away from the customer.

Created 3 new wiki pages:
- 🆕 [[entities/bret-taylor]] — comprehensive entity page covering Google Maps, FriendFeed, Facebook CTO, Quip, Salesforce co-CEO, Twitter chairman, Sierra CEO
- 🆕 [[entities/clay-bavor]] — Sierra co-founder, former Google VP of AR/VR (Cardboard, Daydream, Project Starline)
- 🆕 [[concepts/long-horizon-agents]] — new concept page for agent systems operating over extended timeframes

Enriched:
- ✏️ [[entities/sierra]] — added Horizon section with platform capabilities, long-horizon planning, context engine, differentiation moat, and tokenomics theses

**Bookmark 2 — Armin Ronacher: "Reactive Agents are Proactive" (Junior Subscriptions)**

Ronacher documents Junior's resource subscription architecture — a generalized mechanism letting coding agents subscribe to external events (CI checks, PR reviews, merges) as follow-up messages within ongoing conversations. Key insights: provider-agnostic interface, per-conversation subscriptions (not global webhooks), follow-up vs steering message distinction, `[[NO_REPLY]]` marker for silent event handling, event batching. Junior ~100% subscribes to PRs it creates, auto-resolves build failures, and addresses review feedback.

Created 2 new wiki pages:
- 🆕 [[entities/junior]] — comprehensive entity page for Sentry's open-source AI coding agent with resource subscription architecture
- 🆕 [[concepts/agent-resource-subscriptions]] — new concept page for the resource subscriptions design pattern

Enriched:
- ✏️ [[entities/armin-ronacher]] — added "Resource Subscriptions — Reactive Agents" subsection under Recent Themes, new timeline entry for July 16, 2026

**Raw articles saved:**
- [[raw/articles/2026-07-16_sierra_horizon-long-horizon-agents]]
- [[raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive]]


## [2026-07-17 22:30 UTC] x-accounts-scan | 4 new posts from 3 accounts

**Scanned**: 12/84 accounts (72 skipped by budget), cursor 81→9.

### Ingest Decisions

| Account | Post | Decision | Wiki Action |
|---------|------|----------|-------------|
| @natolambert | Claude Fable 5 bug report | **Skip** — ephemeral bug, temporary status issue | — |
| @geoffreylitt | "Understanding is the new bottleneck" AIE talk | **Update** | Added Speaking Engagements section + Blog/Recent Posts row |
| @0xsero | Step-3.7-Flash-148B (REAP) #1 on local.ai | **Update** | Added LOCAL.AI Benchmark Results section |

### Wiki Changes
- `wiki/entities/geoffrey-litt.md` — Added AIE talk "Understanding is the new bottleneck" (2026-07-10, 56K views) to Speaking Engagements + Blog/Recent Posts
- `wiki/entities/sero.md` — Added LOCAL.AI benchmark #1 (DGX Spark, Mac M5 Max) for Step-3.7-Flash-148B (REAP)

## [2026-07-17 23:30 UTC] x-bookmarks-ingest — 2 bookmarks processed

**Bookmark 1 — Bret Taylor: "The Next Horizon in Agents" (Sierra Horizon)**

Sierra announced Horizon, a long-horizon agent platform that extends Agent OS beyond single conversations to multi-day/week/month goals. Horizon agents proactively engage customers, learn from each interaction, and operate on outcome-based pricing (not tokens). Bret Taylor frames two key theses: (1) customer relationship data as a durable, defensible moat that deepens as AI improves; (2) outcome-based pricing abstracts token costs away from the customer.

Created 3 new wiki pages:
- 🆕 [[entities/bret-taylor]] — comprehensive entity page covering Google Maps, FriendFeed, Facebook CTO, Quip, Salesforce co-CEO, Twitter chairman, Sierra CEO
- 🆕 [[entities/clay-bavor]] — Sierra co-founder, former Google VP of AR/VR (Cardboard, Daydream, Project Starline)
- 🆕 [[concepts/long-horizon-agents]] — new concept page for agent systems operating over extended timeframes

Enriched:
- ✏️ [[entities/sierra]] — added Horizon section with platform capabilities, long-horizon planning, context engine, differentiation moat, and tokenomics theses

**Bookmark 2 — Armin Ronacher: "Reactive Agents are Proactive" (Junior Subscriptions)**

Ronacher documents Junior's resource subscription architecture — a generalized mechanism letting coding agents subscribe to external events (CI checks, PR reviews, merges) as follow-up messages within ongoing conversations. Key insights: provider-agnostic interface, per-conversation subscriptions (not global webhooks), follow-up vs steering message distinction, `[[NO_REPLY]]` marker for silent event handling, event batching. Junior ~100% subscribes to PRs it creates, auto-resolves build failures, and addresses review feedback.

Created 2 new wiki pages:
- 🆕 [[entities/junior]] — comprehensive entity page for Sentry's open-source AI coding agent with resource subscription architecture
- 🆕 [[concepts/agent-resource-subscriptions]] — new concept page for the resource subscriptions design pattern

Enriched:
- ✏️ [[entities/armin-ronacher]] — added "Resource Subscriptions — Reactive Agents" subsection under Recent Themes, new timeline entry for July 16, 2026

**Raw articles saved:**
- [[raw/articles/2026-07-16_sierra_horizon-long-horizon-agents]]
- [[raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive]]


## [2026-07-17 18:10 UTC] dreaming | Knowledge consolidation — 5 reference enrichments (triage recovery)

**Saturation scenario** — Dreaming-collect reported 0 articles, 193 recent raw articles. Dreaming-group (18:00 UTC) completed triage but failed on JSON render. Triage recovered from output file.

**Enrichments applied** (via filesystem scan, 30 articles examined):
| Entity | Section Added | Key Content |
|--------|--------------|-------------|
| [[entities/fireworks-ai]] | Series D — $1.505B at $17.5B | $1.505B Series D at $17.5B valuation, $1B ARR, 40T tokens/day, 95% specialized models. Led by Atreides Management, Index Ventures, TCV; Nvidia participated. |
| [[entities/pinecone]] | Sparse V3 + Text Match Filters | Term-major index layout: 151× (SPLADE) / 1,428× (BM25) I/O reduction. Text match filters for agents solving unstated-context problem. |
| [[entities/elevenlabs]] | Interaction Models | Natural human-AI dialogue: three failure modes of turn-based voice, cascaded STT+TTS architecture, emotional perception. |
| [[entities/warp-terminal]] | Self-Improving Code Review | 3rd factory post: outer-loop agent improves reviewer, skills+Python scripts, spec comparison + build validation. |
| [[entities/harvey]] | Benchmark Acquisition | Acquired Benchmark (YC, NYC, $2T+ AUM), 3rd acquisition of 2026, record Q2 $100M+ net-new ARR, 50+ asset mgmt firms. |

Skipped (already covered): GPT-Red, Agentty, OpenWiki 0.2, Inkling on Modal, Cerebras KB, Sierra AI-Pilling.
Non-AI batch skip: Cohere×UofT, Glean×Databricks, Hex, Parakeet, Pluralistic, EU Battery, Intel history.

**Sources**: raw/articles/2026-07-17_fireworks-ai_series-d-announcement.md, raw/articles/2026-07-17_pinecone_sparse-v3.md, raw/articles/2026-07-17_pinecone_text-match-filters.md, raw/articles/2026-07-17_pinecone_behind-the-benchmarking-pipeline.md, raw/articles/2026-07-17_elevenlabs_interaction-models.md, raw/articles/2026-07-17_warp_how-to-build-a-cloud-software-factory-self-improving-code-review.md, raw/articles/2026-07-17_harvey_y-combinator-backed-benchmark-joins-harvey.md

## [2026-07-17] X Bookmarks Ingest — OpenWiki 0.2 OKF + Cerebras Knowledge Base

**Bookmark 1: OpenWiki 0.2 adopts OKF spec** (LangChain AI, Jul 16 2026):

## [2026-07-17] Raw Backlog Ingest (12:00 UTC)

Processed 5 candidates from raw backlog (--sort ai-hint --limit 5). All 5 already covered by existing wiki pages:

- reframing-superintelligence-fhi-2019.md - Skip (archived, Drexler CAS)
- 2026-06-03_microsoft-mai-thinking-1-tech-report.md - Skip (entities/mai-thinking-1 + concepts/mai-thinking-1-tech-report + concepts/hill-climbing-machine)
- benchflow-awesome-evals-2025.md - Skip (concepts/ai-benchmarks/benchflow-tool with full Awesome Agent Evals section)
- dwarkesh.com--p-grant-sanderson-2--960d89cd.md - Skip (archived, Grant Sanderson math interview)
- wheresyoured.at--the-openai-bubble--eb7fc2d4.md - Skip (archived, Ed Zitron)

Takes=0, References=0, Skips=5. No new pages created. Triage saved to cron/data/raw_backlog_ingest/triage_latest.json.


- Created [[concepts/okf-open-knowledge-format]] — New concept: Google Cloud OKF spec for structured knowledge wikis
- Enriched [[concepts/openwiki.md|concepts/openwiki]] — Added OKF 0.2 Integration section (YAML frontmatter, index.md/logs.md conventions, deterministic search)
- Enriched [[entities/langchain]] — Added OpenWiki 0.2 milestone to timeline, bumped sources
- Raw article: raw/articles/2026-07-16_langchain_openwiki-0.2-okf.md

**Bookmark 2: How we built our knowledge base** (Cerebras AI/Growth team: Isaac Tai, Daniel Kim, Mike Gao, Jul 16 2026):
- Created [[concepts/enterprise-knowledge-base-architecture]] — New concept: meet-the-data-where-it-lives enterprise KB architecture; hybrid search (full-text + embeddings + IDF + age decay), LLM query planning, MCP-exposed retrieval primitives, scoped projects, RRF fusion, bursting for thread-level granularity
- Created [[entities/cocoindex]] — New entity: open-source code embedding framework for vectorizing codebases
- Created [[entities/isaac-tai]] — New entity: Cerebras AI/Growth engineer
- Created [[entities/daniel-kim-cerebras]] — New entity: Daniel Kim, Head of Growth at Cerebras
- Created [[entities/mike-gao]] — New entity: Mike Gao, ML Runtime at Cerebras (ex-Google, Qualcomm, Baidu Research)
- Enriched [[entities/cerebras-systems]] — Added Internal Knowledge Base section (15K queries/day, architecture, MCP integration)
- Raw article: raw/articles/2026-07-16_cerebras_knowledge-base-architecture.md

**index.md** — Added 6 entries (2 concepts, 4 entities). Counts updated: Concepts 1874→1876, Entities 851→855, Comparisons 35

## [2026-07-17] Active Crawl (4 topics)

| 2026-07-17 11:?? | concepts/ai-voice-fraud.md | created | AI Voice Fraud concept page — voice cloning scams, deepfake audio fraud vectors, defensive strategies |
| 2026-07-17 11:?? | concepts/gemini-notebook.md | created | Gemini Notebook concept page — Google's NotebookLM rebranding under Gemini brand umbrella |
| 2026-07-17 11:?? | concepts/llm-text-detection-classical-ml.md | created | LLM Text Detection with Classical ML — SVM/RF/XGBoost on stylometric features for AIGC detection |
| 2026-07-17 11:?? | concepts/soofi-s.md | created | Soofi S — German AI consortium's open 30B multilingual model, Apache 2.0 |
| 2026-07-17 11:?? | raw/articles/2026-07-15_ai-voice-fraud-three-second-theft.md | saved | Source: smarterarticles.co.uk, 188 HN pts |
| 2026-07-17 11:?? | raw/articles/2026-07-16_notebooklm-to-gemini-notebook.md | saved | Source: blog.google, 314 HN pts |
| 2026-07-17 11:?? | raw/articles/2026-03-01_llm-text-detection-classical-ml.md | saved | Source: blog.lyc8503.net, 204 HN pts |
| 2026-07-17 11:?? | raw/articles/2026-07-13_soofi-s-german-30b-model.md | saved | Source: the-decoder.com, 139 HN pts |
| 2026-07-17 11:?? | SCHEMA.md | modified | Added tags: notebook, classifiers, llm-output, deepfakes, fraud |
| 2026-07-17 11:?? | index.md | updated | Added 4 concept entries, updated section counts (1891→1896) |

Sources: HN Algolia (15 trending stories), X/Twitter xurl (10 trending topics), Blogwatcher SQLite DB, Wiki gap analysis. Discovery via 3 parallel subagents. Page creation via parallel subagents + direct parent edits.

Top story: Kimi K3 (#1 HN at 1,677 pts) — already documented in wiki; skipped page creation. Other notable: Cursor 0day (453 pts), Demis Hassabis AI safety (157 pts), Gemma 4 CPU inference (324 pts), Spectral Compute CUDA alternatives (141 pts — 403 blocked), LM Studio Bionic (264 pts).

2026-07-17 | newsletter-wiki-ingest | Enrich concepts/kimi-k3.md (+91 lines) | Add KDA/AttnRes architecture details, Agent Arena benchmarks, AA evaluation metrics, Serving/Infrastructure, Caveats & Controversies, Community Reaction from AINews article | Triage recovered from checkpoint (Takes=0, Ref=4); processed 1 reference enrichment | [concepts/kimi-k3](concepts/kimi-k3.md) | sources: raw/newsletters/2026-07-17-ainews-kimi-k3-2-8t-a50b-the-largest-open-model-ever-released-opus-4-8-class-at-.md

## 2026-07-17

### Blog Ingest — Kimi K3

| 2026-07-17 07:00 UTC | blog-wiki-ingest | **37 new articles collected, 14 saved, 6 unsaved (paywalled).** AI-relevant processing: Created `concepts/kimi-k3.md` (Moonshot Kimi K3 — 2.8T MoE frontier model, $3/$15 pricing, open weights by Jul 27, Elo 1547 on Artificial Analysis, Arena.ai Frontend #1). Updated `entities/kimi.md` (K3 row in model table, K3 section with benchmarks/pricing/pelican). Updated `entities/simon-willison.md` — July 16-17 entries: Kimi K3 pelican analysis (25¢, 13,241 reasoning tokens), Inkling open-weights coverage, Codex $HOME file deletion bug (Thibault Sottiaux quote), Linus Torvalds AI-in-Linux stance, data center water use (Spot Birds Not Golf), Firefox in WebAssembly. Updated `entities/openai-codex.md` — Known Issues section: GPT-5.6 $HOME file deletion bug (full access mode + no sandboxing → model deletes $HOME). Updated `comparisons/llm-api-pricing.md` (K3 in China Frontier section). Non-AI articles skipped: astronomy (NGC 7497), gadget review (Thermal Master DV2), Intel history, Windows debugging, EU battery regulation, app design essay, Cory Doctorow billionaire essay. Sources: 7 simonwillison.net articles, daringfireball.net linked articles. |

### Raw Backlog Ingest — 5 candidates (2 archived, 3 dedup-skipped)

| 2026-07-17 00:00 UTC | raw-backlog-ingest | **All content already captured.** Processed 5 candidates: reframing-superintelligence-fhi-2019.md (Drexler CAS, archived), dwarkesh.com--p-grant-sanderson-2--960d89cd.md (Grant Sanderson math interview, archived), wheresyoured.at--the-openai-bubble--eb7fc2d4.md (Ed Zitron, archived), 2026-06-03_microsoft-mai-thinking-1-tech-report.md (already fully covered in entities/mai-thinking-1 + concepts/mai-thinking-1-tech-report + concepts/hill-climbing-machine, newly archived), benchflow-awesome-evals-2025.md (already fully covered in concepts/ai-benchmarks/benchflow-tool, newly archived). No enrichment needed — all content fully captured by Jun/Jul 2026 sessions. Archive: 2 new + 3 dedup (total: 1,687 URLs). |

## 2026-07-16

### Dreaming — Knowledge Consolidation

| 2026-07-16 18:00 UTC | dreaming | **Saturation day** — Takes=0, Ref=1, Skip=10. RSS/Newsletter収集0件。Filesystem scan: 185生記事のうち11件のAI関連記事を評価。全件が既存Wikiページでカバー済み。Bonsai 27B (concepts/bonsai-27b.md), Juggler (concepts/juggler.md), Claude Memory Heist (concepts/claude-memory-heist.md), Demis Hassabis preflight (entities/demis-hassabis.md L175-189), Glean Agent Identity (entities/glean.md L154), ICML 2026 trends (entities/sierra.md sources). Reference: China Apple Intelligence承認 (us-china-ai-competition.md update候補). Archive: 11 candidates → 9 new archived (total: 1,687 URLs). |

## 2026-07-16

### Active Crawl

| 2026-07-16 12:00 UTC | active-crawl | 3 new concept pages: [[concepts/gpt-red]] (OpenAI automated red-teaming via self-play, 84% success), [[concepts/grok-mermaid]] (Rust terminal Mermaid renderer from Grok Build), [[concepts/agentty]] (C++26 Claude Code alternative, 11MB binary). Raw articles: 2026-07-15_mit-technology-review_gpt-red.md, 2026-07-16_github_agentty-cpp26-coding-agent.md. Sources: MIT Technology Review, Simon Willison, GitHub/1ay1. Index: Concepts 1866->1891, Entities 851->852. |

### Blog Wiki Ingest

- **entities/grok-build.md**: Added "Open Source Release (July 2026)" section — Apache 2.0 release, 844,530 lines Rust, code structure analysis (Simon Willison, July 15)
- **entities/simon-willison.md**: Added 2 entries — Grok Build OSS analysis and Claude web_fetch data exfiltration vulnerability (July 15)
- **entities/ed-zitron.md**: Added "The OpenAI Bubble" to Notable Articles table — Lehman Brothers of AI framing, cult-like psychosis thesis (July 2026)
- **entities/sierra.md**: Added "Pinecone Architecture" sub-section — 3-layer architecture, durable sessions, multiplayer, privileged operations (July 2026)
- **concepts/ai-agent-security.md**: Added "Claude web_fetch — Nested Link Exfiltration" section (Ayush Paul discovery, July 2026)
- **concepts/inkling.md**: Added Together AI and Modal raw articles to sources

| 2026-07-16 07:40 UTC | newsletter-wiki-ingest | Enriched [[entities/thinking-machines-lab]] (Inkling model: 975B/41B MoE, architecture, benchmarks, ecosystem). Enriched [[concepts/inkling]] (architecture details, benchmarks, ecosystem support, Inkling-Small). Source: AINews newsletter, Together AI blog, Modal blog. Index: Entities 851->851, Concepts 1866->1866. |
| 2026-07-15 23:30 UTC | x-bookmarks-ingest | X bookmarks ingest: 2 bookmarks processed. Created entity: [[entities/soham-ray]] (Soham Ray, Sierra AI researcher, tau-bench ICML 2026 oral). Enriched: [[entities/shreya-shankar]] (ICML 2026 timeline + tau-bench oral), [[entities/sierra]] (ICML 2026 tau-bench presentations + Soham Ray cross-ref). Updated concept pages: [[concepts/ai-benchmarks/tau-bench]] (ICML 2026 conference column), [[concepts/ai-benchmarks/tau-squared-bench]] (ICML 2026 oral annotation). Saved raw article: 2026-07-14_sohmray_icml-2026-research-trends.md. Bookmark 1 (Boris Cherny fragment) skipped - truncated text-only, no actionable content. Index: Entities 850->851. |

| 2026-07-15 22:30 UTC | x-accounts-scan | X accounts scan: 3 new posts from 2 accounts (danielhanchen ×2, shloked ×1). Created raw articles: inkling-1bit-gguf-quants, inkling-unsloth-studio, rabbithole-infinite-canvas-learning. Updated entities: daniel-han (Inkling GGUF + Studio), shlok-khemani (Rabbithole). Created concepts: inkling.md, rabbithole.md. Enriched stubs: concept/unsloth.md, concept/unsloth-fast-fine-tuning.md. Updated post-training/unsloth.md. Index +2 concepts (1864→1866). |

| 2026-07-15 18:22 UTC | dreaming-wiki-ingest | Upstream dreaming-group at 18:00 UTC already completed triage — Takes=0 (saturation day). All daily pipelines (blog, newsletter, active-crawl) ran before dreaming. Archive confirmed at c36c6c86. No action needed. |
| 2026-07-15 18:00 UTC | dreaming | Saturation day — Takes=0, all pipelines already ran today. 30 articles triaged as skip (sitemap company blogs + already-processed active-crawl/blog/newsletter). Archive: 30 new, total 1,661 URLs |
---
## [2026-07-15] watchdog | Auto-fix header counts, verify structural health

### Changes
- Fixed Entities header: 851→850 pages
- Fixed Concepts header: 1,884→1,864 pages
- Verified 0 stale index entries (541 false positive from flat scan)
- Verified 0 index corruption issues

---

## [2026-07-15] active-crawl | 5 new concept pages, 2 new entity pages, 5 raw articles

### Changes

**New concept pages:**
- [[concepts/bonsai-27b]] — Prism ML's 27B model running on phones via extreme quantization (1.125 bits/param)
- [[concepts/juggler]] — Open-source GUI coding agent by Julian Storer (JUCE creator), AGPL + Apache SDK
- [[concepts/claude-memory-heist]] — Prompt injection attack exfiltrating user data from Claude's memory system via web_fetch navigation
- [[concepts/ai-preflight-safety-testing]] — Demis Hassabis endorses mandatory pre-deployment safety evaluations (FINRA-style SRO)
- [[concepts/jepa-world-models]] — Joint Embedding Predictive Architecture world models (LeCun, LeMario, LeWorldModel)

**New entity pages:**
- [[entities/prism-ml]] — AI research company; creators of Bonsai 27B (Caltech, Khosla/Cerberus/Google/Samsung)
- [[entities/qwen]] — Alibaba's LLM family (Tongyi Qianwen); base model for Bonsai 27B

**Raw articles saved:**
- raw/articles/2026-07-15_bonsai-27b-prism-ml.md
- raw/articles/2026-07-15_juggler-gui-coding-agent.md
- raw/articles/2026-07-15_claude-memory-heist.md
- raw/articles/2026-07-15_ai-preflight-safety-testing.md
- raw/articles/2026-07-15_lemario-jepa-world-model.md

**Tags added to SCHEMA.md:** prism-ml, bonsai, juggler

**Sources:**
- https://prismml.com/news/bonsai-27b (HN 612 pts)
- https://github.com/juggler-ai/juggler (HN 247 pts)
- https://www.ayush.digital/blog/the-memory-heist (HN 354 pts)
- https://garymarcus.substack.com/p/breaking-demis-hassabis-endorses-preflight-safety-testing-for-ai
- https://www.benjamin-bai.com/projects/lemario (HN 108 pts)

### Health Check
| Metric | Status |
|--------|--------|
| New pages | 7 (5 concepts + 2 entities + 5 raw articles) |
| Wikilinks verified | All OK across all pages |
| SCHEMA tags | Added prism-ml, bonsai, juggler |
| Index entries | Inserted alphabetically at correct positions |
| Index counts | Entities 851, Concepts 1884 — match filesystem |

---
## [2026-07-15] Blog wiki-ingest — Armin Ronacher Tower, Codex Pets, AI Vulnerability Discovery, Pseudpocalypse

**Source**: blog-triage checkpoint (20 articles: 2 take, 2 reference, 16 skip)

**Pages enriched:**
- entities/armin-ronacher — Added "The Tower Keeps Rising" (July 13): Tower of Babel metaphor for shared understanding collapse in AI-assisted software projects. Added to timeline + Recent Themes
- concepts/codex/codex-superapp — Added "Codex Desktop Pets / Custom Pets" section: Pedalican by Simon Willison, multi-modal agent workflow with GPT-5.6 Sol xhigh + gpt-image-2
- concepts/ai-vulnerability-discovery — Added "Microsoft AI-Driven Record Patch Volume — 570 Vulnerabilities (July 2026)": exploitability index critique by Satnam Narang (Tenable)
- concepts/ai-privacy-tools — Added "Pseudpocalypse — LLM-Based Authorship Attribution": ~29-bit information-theoretic threshold, Claude 4.8 identification from 1000 words

**References archived**: 16 skip + 2 reference items

---
## [2026-07-15] Newsletter wiki-ingest — GPT-5.6 usage patterns, AI Engineering 5 trends, LLM Architecture (Raschka)

**Source**: 3 newsletters triaged and ingested (Ben's Bites, swyx/Latent Space, Vanishing Gradients)

**Pages enriched:**
- concepts/gpt/gpt-5-6 — Added "Practical Usage Patterns" section (model selection, usage limits, ChatGPT Work, Computer Use)
- concepts/ai-engineering — Complete rewrite from stub: 5 trends from AIEWF 2026 (harness, loop, FDEs, context, skills engineering)
- concepts/llm-architecture-complexity — Added Raschka: MLA KV cache analysis, RLVR/PRM predictions, shrinking harnesses, fine-tuning economics
- concepts/agent-harnesses — Added "Shrinking Harnesses as Models Improve" section
- entities/sebastian-raschka — Added new book "Build a Reasoning Model", methodology, AI stack, Vanishing Gradients conversation

**New pages created:**
- events/ai-engineer-worlds-fair-2026 — AI Engineer World's Fair 2026 event page with key themes, people, quotes

# Wiki Log

_Log of all wiki changes. Newest entries at top._

---
## [2026-07-14] X bookmarks ingest — Demis Hassabis's Frontier AI Standards Body proposal

**Source**: X Article by Demis Hassabis (@demishassabis), "A Framework for Frontier AI and the Dawning of a New Age" (Jul 14, 2026)
**Engagement**: 18,137 bookmarks, 13,609 likes, 2,599 RTs, 5M impressions

**New pages created:**
- concepts/frontier-ai-standards-body — Demis Hassabis's July 2026 FINRA-style Frontier AI Standards Body proposal
- raw/articles/2026-07-14_demishassabis_frontier-ai-framework.md

**Pages enriched:**
- entities/demis-hassabis — Added "On AI Governance (July 2026)" section, updated sources/frontmatter
- concepts/ai-regulation-2026 — Added Demis Hassabis FINRA-SRO section with comparison table vs Amodei/OpenAI frameworks
- concepts/frontier-safety-blueprint — Added cross-reference to competing Hassabis proposal

**Key proposal elements**: FINRA-style SRO with federal oversight, industry-funded, dynamic quarterly benchmarks, voluntary→mandatory pre-release review, ratchet mechanism for development slowdowns, open-source board seat, country-agnostic scope.

| 2026-07-14 18:22 UTC | dreaming-wiki-ingest | Saturation day — Takes=0, 5 refs verified (all already covered), 21 skips archived via prior cycles |
  - Verified: Martin Alderson margin collapse pt 2 (entities/martin-alderson.md lines 96-110 — already covered), Merge AI agent governance (entities/merge-dev.md Refs section — already covered), Hebbia data integrations (entities/hebbia.md Data Integrations section — already covered), ElevenLabs AI calling (entities/elevenlabs.md AI Customer Service section — existing coverage sufficient), DOOMQL (entities/simon-willison.md — marginal value, not enriched)
  - Archive: All 25 decisions already in archive_index.json (deduped from prior cycles)

| 2026-07-14 20:00 UTC | raw-backlog-ingest | 0 takes, 5 skips — all articles already covered in existing wiki pages |
|  - MAI-Thinking-1 tech report (407KB PDF): fully captured in entities/mai-thinking-1.md + concepts/mai-thinking-1-tech-report.md + concepts/hill-climbing-machine.md since Jun 2026 |
|  - BenchFlow Awesome Agent Evals (443+ resources): fully captured in concepts/ai-benchmarks/benchflow-tool.md since Jun 2026 |
|  - 3 already-archived items: Reframing Superintelligence (FHI 2019), Dwarkesh Grant Sanderson, Dwarkesh Adam Brown |
|  - Archive: 2 new + 3 dedup skipped (total 1640 archive URLs) |
  - Upstream: Prior dreaming-group at 18:00 enriched entities/sierra.md — SoftBank partnership

| 2026-07-14 18:00 UTC | dreaming | Saturation day — 1 take (Sierra+SoftBank), filesystem scan of 190 raw articles |
  - Enriched: [[entities/sierra.md]] — SoftBank Corp. partnership (exclusive Japan sales partner), LINEMO 97% resolution/93% CSAT, Opera Tech acquisition, Tokyo office
  - Skipped: Merge.dev AI agent governance + MCP governance (already in merge-dev.md), Hex Technologies context engineering (existing context-engineering pages), Hebbia strategist (light content), ElevenLabs AI calling (guide article), Krebs CISA leak (tangential), ArsTechnica Musk/Apple/OpenAI (events page exists)
  - Source: [[raw/articles/sierra.ai--blog-announcing-our-partnership-with-softbank-corp--4a150bd0]]

| 2026-07-14 | active-crawl | 3 pages created, 3 raw articles saved | Claude Code vs OpenCode token overhead comparison (687 pts HN), Mesh LLM distributed P2P inference (344 pts HN), Apple SpeechAnalyzer on-device API benchmark (541 pts HN)

| 2026-07-14 | concepts/hill-climbing-machine.md | enriched | Hill-Climbing Machine expanded from stub to comprehensive page: integrated system components, three specialist RL climbs, modified GRPO, reward decomposition, 8K GB200 infrastructure
  - Source: [[raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md]]

| 2026-07-14 | comparisons/claude-code-vs-opencode-token-overhead.md | created | 33K vs 7K token overhead comparison; Systima measurement study; 4.7× gap on Sonnet 4.5
  - Source: [[raw/articles/2026-07-12_systima_claude-code-vs-opencode-token-overhead.md]]

| 2026-07-14 | concepts/mesh-llm.md | created | Distributed P2P LLM inference over iroh protocol; 40+ preconfigured models; Qwen 235B @ 16 tok/s across 2 nodes
  - Source: [[raw/articles/2026-07-11_iroh_mesh-llm-distributed-inference.md]]

| 2026-07-14 | concepts/apple-speechanalyzer.md | created | Apple on-device speech recognition API; 2.12% WER on LibriSpeech, 3-4× improvement over legacy, beats Whisper Small
  - Source: [[raw/articles/2026-07-13_getinscribe_apple-speech-api-benchmark.md]]

| 2026-07-14 | SCHEMA.md | updated | Added tags: speech, p2p, edge-computing, opencode


| 2026-07-14 | concepts/cais.md | enriched | Drexler FHI 2019 paper deep dive: service-centered architecture, R&D automation vs agent-centric model, learning vs competence distinction, safety afforances, risks (210-page technical report)


| 2026-07-14 | entities/claude-code.md | updated | Added 2M users / $2.5B ARR metrics to Key Metrics

| 2026-07-14 | concepts/vllm.md | updated | Added HuggingFace Transformers integration section — native vLLM speed
| 2026-07-14 | concepts/agent-harnesses.md | updated | Added Practical Harness Construction Patterns section — opinionated adapters, permission encoding, structured artifacts, multi-model routing

| 2026-07-14 | entities/alex-finn.md | created | Alex Finn — solo builder with 24/7 local AI fleet and automated software factory

---

## [2026-07-14 07:50 UTC] Blog Wiki Ingest — 2 takes, 4 references

### Updated Entity Pages
- ✏️ [[entities/martin-alderson]] — Added "Winners and Losers — Part 2 (July 2026)" subsection: Grok 4.5 pricing, hardware winners, coding agents, B2C wildcard, managed agent platforms
  - Source: [[raw/articles/martinalderson.com--posts-the-upcoming-ai-margin-collapse-part-2-winners-and-los--2b401389]]
- ✏️ [[entities/antirez-com]] — Added "Control the Ideas, Not the Code (July 2026)" section: code review suboptimal with LLMs, Mythical Man Month, DS4 experience, DESIGN.md proposal
  - Source: [[raw/articles/antirez.com--news-169--1ef2a41d]]
- ✏️ [[entities/merge-dev]] — Added 3 reference entries: MCP governance platforms, AI agent governance framework, Sonnet 5 vs GPT-5.6 Terra benchmark
  - Sources: [[raw/articles/merge.dev--blog-mcp-governance-platform--5437a765]], [[raw/articles/merge.dev--blog-ai-agent-governance--4bf04b32]], [[raw/articles/merge.dev--blog-gpt-5-6-terra-vs-claude-sonnet-5--9c5002f0]]
- ✏️ [[entities/cory-doctorow]] — Added "Go Meta Economy" section: AI companies as picks-and-shovel sellers despite transformative claims
  - Source: [[raw/articles/pluralistic.net--2026-07-13-go-meta-meta--d0727adf]]

---

## [2026-07-14 07:00 UTC] Blog Ingest — 20 articles scanned, 17 saved

### Raw Articles Saved (17)
- [[raw/articles/simonwillison.net--2026-jul-14-uvx-github-actions-cache--a814fa12]] — Using uvx in GitHub Actions in a cache-friendly way
- [[raw/articles/simonwillison.net--2026-jul-13-datasette-code-frequency--b8e9b576]] — datasette code-frequency chart on GitHub
- [[raw/articles/simonwillison.net--2026-jul-13-doomql--7d2f71ea]] — DOOMQL
- [[raw/articles/krebsonsecurity.com--2026-07-lessons-learned-from-cisas-recent-github-leak--89c16b34]] — Lessons Learned from CISA's Recent GitHub Leak
- [[raw/articles/martinalderson.com--posts-the-upcoming-ai-margin-collapse-part-2-winners-and-los--2b401389]] — Winners and losers in the coming AI margin collapse (part 2)
- [[raw/articles/devblogs.microsoft.com--oldnewthing-20260713-00--57587b90]] — Why don't we just make the entire stack out of guard pages?
- [[raw/articles/micahflee.com--mandatory-update-a-short-story--a332b287]] — Mandatory Update: A Short Story
- [[raw/articles/paper.design----bb20e46c]] — Paper - design, share, ship (sponsor)
- [[raw/articles/merge.dev--blog-mcp-governance-platform--5437a765]] — A guide to evaluating MCP governance platforms
- [[raw/articles/merge.dev--blog-ai-agent-governance--4bf04b32]] — AI agent governance: key aspects, benefits, and platforms
- [[raw/articles/merge.dev--blog-gpt-5-6-terra-vs-claude-sonnet-5--9c5002f0]] — Claude Sonnet 5 vs GPT-5.6 Terra: how they compare on coding
- [[raw/articles/sierra.ai--blog-announcing-our-partnership-with-softbank-corp--4a150bd0]] — Announcing our partnership with SoftBank Corp.
- [[raw/articles/arstechnica.com--tech-policy-2025-08-elon-musk-sues-apple-openai-to-block-exc--03034646]] — Elon Musk sues Apple and OpenAI
- [[raw/articles/lwn.net--articles-1082647--d9aae7b5]] — Final normal Debian bookworm release
- [[raw/articles/dfarq.homeip.net--code-red-worm-july-13-2001--5761e2ff]] — Code Red worm, July 13, 2001
- [[raw/articles/antirez.com--news-169--1ef2a41d]] — Control the ideas, not the code
- [[raw/articles/pluralistic.net--2026-07-13-go-meta-meta--d0727adf]] — Why aren't AI companies competing directly with their customers?

### Skipped (3)
- LWN.net "Shielding running kernels against exploits with BPF" (paywalled)
- LWN.net "Security updates for Monday" (paywalled)
- shkspr.mobi "[RSS Club] Half a million steps" (not AI-relevant)

### Checkpoint
- run_id: 20260714T070031Z
- checkpoint: /opt/data/.hermes/cron/data/blog_ingest/latest.json
---
## [2026-07-13] X Bookmarks Ingest — 2 bookmarks processed

### New Pages
- 🆕 [[concepts/reverse-information-paradox]] — Nadella's framework for enterprise AI knowledge sovereignty: inverting Arrow's Information Paradox, trust boundary concept, five enterprise imperatives (Control, Capability, Choice, Cost, Compound)
  - Source: [[raw/articles/2026-07-12_satya-nadella_reverse-information-paradox]]

### Enriched Pages
- ✏️ [[entities/prime-intellect]] — verifiers v1 announcement (Jul 12): environment decomposition into taskset/harness/runtime primitives; harness-agnostic task definitions
  - Source: [[raw/articles/2026-07-12_primeintellect_verifiers-v1]]
- ✏️ [[entities/satya-nadella]] — Reverse Information Paradox article: career timeline entry, 2 new notable quotes, cross-reference to reverse-information-paradox concept
  - Source: [[raw/articles/2026-07-12_satya-nadella_reverse-information-paradox]]
- ✏️ [[concepts/ai-economics]] — Reverse Information Paradox section: structural cost of knowledge leakage, asymmetric learning flow, distributed learning infrastructure argument
- ✏️ [[concepts/token-capital]] — Cross-reference to reverse-information-paradox in Related Concepts

### Raw Articles Saved
- [[raw/articles/2026-07-12_primeintellect_verifiers-v1]] — Prime Intellect verifiers v1 tweet (514 bookmarks)
- [[raw/articles/2026-07-12_satya-nadella_reverse-information-paradox]] — Satya Nadella X Article (22,227 bookmarks, 10.6M impressions)

### Stats
- 1 new concept page, 4 pages enriched, 2 raw articles saved
---
## [2026-07-13 12:00 UTC] enrichment | GPT-5.6-Sol operational guidance added to openai-codex
---
## [2026-07-13 22:30 UTC] enrichment | X accounts scan: V-SPLADE endorsement added to Tom Aarsen
- [[entities/tom-aarsen.md]]: Added V-SPLADE Endorsement (July 2026) section covering Tom Aarsen's X thread recommending naver/v-splade-quality, v-splade-efficient, and splade-v3 models for sparse embedding document retrieval. Added to Blog/Recent Posts table. Updated frontmatter date.
---
## [2026-07-13 18:00 UTC] dreaming | Knowledge consolidation — 2 reference enrichments
- [[entities/ed-zitron.md]]: Added Memory Crisis — HBM Economics section (HBM pricing, memory triopoly, NVIDIA 65% HBM consumption, consumer electronics price impact)
- [[comparisons/llm-gateways.md]]: Added Merge Gateway evaluation data (65% cost reduction, subsecond overhead, Benjamini-Hochberg FDR corrected statistical tests)

---

## [2026-07-13] enrichment | Neovim analogy & harness cost data added to Pi

### Enriched Pages
- **[[entities/pi]]** — Added "Neovim Analogy" section (core app + extensions, custom commands, custom UI, config directories mapping), "Plugin Model: Programmable Harness vs External Hooks" section (Pi vs OpenCode plugin philosophy), and Databricks internal benchmark data showing Pi achieves same success rate as vendor harnesses at 1–2x less cost per task. Source: Rasyidan A F blog "Vim of Coding Agents" (2026-07-11).

### Sources
- raw/articles/2026-07-11_rasyidanaf_vim-of-coding-agents.md


### Enriched Pages
- **[[entities/openai-codex]]** — Added "GPT-5.6-Sol Operational Guidance (July 2026)" section based on Theo Browne's X Article. Covers reasoning level selection (medium/high/xhigh/Ultra), fast mode 2.5x multiplier warning, subagent management mitigations (lower reasoning, AGENTS.md directive, Fable orchestrator pattern), model selection (Sol/Terra/Luna), prompt engineering with clear stop points, and usage monitoring tools (ccusage, codexbar). Updated frontmatter: sources, date.

### Sources
- raw/articles/2026-07-11_theo_gpt-5-6-sol-without-hitting-limits.md — Theo Browne X Article (plain_text source)

---
## [2026-07-13 12:00 UTC] entity-creation | Theo Browne (t3.gg) entity page created

### New Pages
- **[[entities/theo-browne]]** — Comprehensive entity page for Theo Browne (t3.gg), CEO at t3.chat, creator of create-t3-app (38K+ stars), tech YouTuber, and prominent coding agent practitioner. Covers key projects (create-t3-app, t3.chat, t3.code, t3 Stack), YouTube content style, writing philosophy (practitioner-first, opinionated but transparent), core ideas (reasoning level taxonomy, subagent token cascade management, Fable-as-orchestrator pattern, vendor advocacy), and cross-references to Claude Code, OpenAI Codex, agentic engineering, and related concepts.

### Sources
- X/Twitter: @theo (358K+ followers)
- Website: t3.gg
- GitHub: t3-oss/create-t3-app
- X Article: "gpt-5.6-sol without hitting limits" (July 2026)

---
## [2026-07-13 11:15 UTC] active-crawl — 3 new pages + 1 entity enrichment

### New Pages
- **[[concepts/agent-approval-spoofing]]** — Security vulnerability where 6 AI coding assistants displayed incorrect file paths in approval dialogs. Covers the vulnerability pattern (LLM generates approval text and tool call with no cross-validation), confirmed incidents (TheDailyAgent July 2026, Cursor force-push HN 46728766, Claude Code git bypasses), and mitigations (system-level gating, Yubikey hardware tokens, Docker sandboxing).
- **[[concepts/ai-infrastructure-circular-financing]]** — Financial model where Nvidia invests in cloud GPU providers (CoreWeave, Nebius) who use the capital plus massive debt to buy GPUs from Nvidia, creating a circular revenue loop. Covers scale ($2B investment vs $35B CoreWeave CapEx, $2.3B GPU-collateralized debt), risks (collateral cascade), and community debate (365 HN pts, 167 comments).
- **[[entities/terry-tao]]** — Entity page for Fields Medalist Terence Tao, a prominent advocate for AI tools in mathematics. Covers his use of GPT-4/Claude as "co-pilot" for proof strategies, advocacy for Lean proof assistant, open-source AI stance, and key quote: "The job description is changing."

### Enriched
- **[[entities/deepseek]]** — Added "Custom AI Chip Development (July 2026)" section covering Reuters report that DeepSeek is designing its own AI chips, driven by US export controls, Singapore Blackwell controversy, and strategic implications for China's AI silicon independence. (+28 lines)

### Sources
- Agent approval spoofing: TheDailyAgent tweet + HN discussion (objectID 46728766)
- Circular financing: io-fund.com article + HN discussion (365 pts, objectID 48873836)
- Terry Tao: Scientific American + El País + Nature interviews
- DeepSeek chips: Reuters (July 7, 2026) + SCMP + CNBC

### Research
- raw/articles/2026-07-13_trending-topics-research.md: Comprehensive research note covering all 4 topics with HN Algolia discussion analysis

---
## [2026-07-13 10:00 UTC] llm-pricing-monitor | OpenAI GPT-5.6 launch + deep-research price revert
- comparisons/llm-api-pricing.md: Added GPT-5.6-sol ($5/$30, flagship), GPT-5.6-terra ($2.50/$15), GPT-5.6-luna ($1/$6) with new cache writes pricing (+25% premium over base input)
- comparisons/llm-api-pricing.md: Reverted o3-deep-research from $10/$40 back to $5/$20 and o4-mini-deep-research from $2/$8 back to $1/$4 — now batch-only (no standard pricing tier)
- comparisons/llm-api-pricing.md: Added gpt-5.3-codex ($1.75/$14) and gpt-5.4-cyber (undisclosed); added Priority pricing tier (2× standard)
- comparisons/llm-api-pricing.md: Moved GPT-5.5 from Flagship to Frontier tier; updated Tier Analysis, Batch Pricing, Cache Pricing, Cost Comparison, Key Trends, and Changelog sections
- Verified: Anthropic pricing unchanged (Fable 5 $10/$50, Opus 4.8 $5/$25, Sonnet 5 intro $2/$10 through 2026-08-31)
- Verified: Google pricing unchanged (3.1 Pro $2/$12, 3.5 Flash $1.50/$9, 3 Flash Preview $0.50/$3, 3.1 Flash-Lite $0.25/$1.50)
- Verified: DeepSeek pricing unchanged (V4-Flash $0.14/$0.28, V4-Pro $0.435/$0.87). Note: deepseek-chat/reasoner aliases deprecating 2026-07-24
---
## [2026-07-13 07:40 UTC] blog-wiki-ingest | Recovered from blog-triage checkpoint (JSON saved before render failure)
- entities/george-hotz.md: Enriched with "I Love LLMs: The Singularity is Nearer (Jul 12, 2026)" section — partial retraction of Eternal Sloptember, genuine AI optimism, negative valence hype critique, frontier lab valuation (Moore's law vs lab value capture), Linus Torvalds agents=10x vs compilers=1000x, cognitive fatigue caveats. Timeline entry + notable posts list + source added. (+25 lines)
- entities/simon-willison.md: Enriched with "Fable Gets Another Bump" (July 12) — Anthropic extends Fable 5 access through Jul 19, OpenAI GPT-5.6 Sol removes limits, Simon argues for permanent Fable availability. "Directly Responsible Individuals (DRI)" — agents should never be DRI, IBM 1979 management decision rule. Reference only (no page change): Merge Gateway cost evaluation (no existing concept page for LLM routing)
- Skip: shot-scraper 1.11, sqlite-utils 4.1.1, lcamtuf panel meter, SwiftUI WWDC, posterior variance/variance statistics, TwoMillionKit, Lunatic Fringe, cooled clothing, HyperCard emulator, icon design, interrail travel, Grumpy Website, Every Frame Perfect, Sam Altman/Elon Musk X thread, Apple/OpenAI Gurman paywall
- Archive: blog triage decisions archived
---
## [2026-07-13 07:40 UTC] newsletter-wiki-ingest | Recovered from triage checkpoint (JSON saved before render failure)
- entities/nathan-lambert.md: Added "July 2026: 6 months to live for open models" section — White House EO threat, 6-month ban window, distillation as regulatory capture, Anthropic lobbying critique
- concepts/open-weight-vs-closed-llm-gap.md: Added "Regulatory Dimension" section — Lambert's 6-month regulatory timeline vs Doubleword's Dec 2026 benchmark convergence, comparison table, regulatory capture framing
- concepts/open-source-ai-destruction.md: Added "Nathan Lambert: Distillation as Regulatory Capture" subsection — regulatory destruction dimension complementing Geerling's operational destruction dimension
- Source: raw/newsletters/2026-07-12-6-months-to-live-for-open-models.md (Interconnects / Nathan Lambert)
- Reference only (no page change): The Signal competitive analysis — all topics already wiki-covered (GPT-5.6, GPT Live, ChatGPT Work, Claude Cowork, Muse Spark 1.1)
- Skip: Lenny's Podcast (AI sentiment survey — no wiki target), Beehiiv W&B@CoreWeave (all URLs 403 expired, CoreWeave/W&B pages already cover acquisition)
---
## [2026-07-13 07:00 UTC] blog-ingest | 30 new articles collected, 18 saved as raw
- Scan: 0 blogs_scanned (blogwatcher RSS scan), 20 blog_articles total, 18 saved, 2 unsaved (X link, Bloomberg paywall)
- Key AI-relevant articles processed into wiki updates:
  - geohot.github.io: "I love LLMs, I hate hype" — updated entity page with Jul 2026 blog post
  - simonwillison.net: "Fable gets another bump" — updated Fable entity + GPT-5.6 concept with competitive dynamics
  - TwoMillionKit (Apple Private Cloud Compute workaround) — saved as raw, not wiki-worthy yet
  - DRI concept (Simon Willison) — saved as raw, organizational theory tangentially relevant

---
## [2026-07-13 07:00 UTC] blog-triage | Updated 3 wiki pages from blog ingest
- entities/geohot-github-io: Added "I love LLMs, I hate hype" (Jul 2026) — AI excitement, anti-hype, GLM-5.2+opencode, LLMs as compilers, Moore's law thesis
- entities/fable: Added Market Dynamics section — Fable vs GPT-5.6 Sol competition, Anthropic access extensions through Jul 19, OpenAI removing usage limits, 6M active users
- concepts/gpt/gpt-5-6: Added Post-Launch Updates — usage limit removal (Jul 12), efficiency improvements, 6M active users, competitive impact on Anthropic

---
## [2026-07-12 18:28 UTC] dreaming-wiki-ingest | Enriched 2 entity pages (reference candidates from filesystem scan)
- Factory AI: Added Incident Response section (Slack alert → autonomous RCA, incident memory)
- ElevenLabs: Added Impact Program — Projekt Kalwaria (cultural heritage TTS/VR restoration)
- Sources: raw/articles/2026-07-11_factory_incident-response.md, raw/articles/2026-07-11_elevenlabs_how-projekt-kalwaria-uses-elevenlabs-to-preserve-history.md

---
## [2026-07-12 18:01 UTC] dreaming-group | Saturation day — 0 takes, 2 references
- Checkpoint: 1 article (ATP podcast, non-AI) + 169 recent raw articles
- Blog triage: 20 decisions (1 take consumed by blog-wiki-ingest)
- Newsletter triage: 18 decisions (all skips)
- Active-crawl: 4 new pages (Cline, Mindwalk, Reame)
- Filesystem scan: 7 articles assessed → 0 takes, 2 references, 5 skips
- References: Factory AI incident response (enrichment candidate), ElevenLabs Projekt Kalwaria (enrichment candidate)
- Archive: 6 new URLs archived (1,546 total)
---
## [2026-07-12] watchdog | Auto-fixed log.md separators and pipe corruption

### Changes
- Fixed 2 `|---` pipe corruption lines in log.md (separator lines with | prefix)
- Added 26 missing `---` section separators between consecutive `## [YYYY-MM-DD]` headers
- Verified: all structural checks clean (0 pipe corruption in index.md, 0 ghost entries, 0 line-prefix corruption, 0 stale index entries)

### Health Summary
| Metric | Status |
|--------|--------|
| Index structural health | Clean (2771 lines) |
| Ghost entries | 0 |
| Index corruption | None detected |
| Log separators | 0 missing out of 118 sections |
| Stale index entries (index→file) | 0 |
| Cross-section misplacement | 0 |
| Tag violations (SCHEMA.md) | 0 |

---

## [2026-07-12] active-crawl — 4 new pages: Cline, Mindwalk, Reame

### New Pages
- **[[entities/cline]]** — Entity page for Cline, the 64K+ star autonomous coding agent for VS Code (TypeScript, July 2024). Covers GitHub stats, features (multi-modal IDE/CLI/SDK, Kanban multi-agent board, Plan/Act mode, model agnosticism, plugins/MCP, multi-agent teams), architecture, comparison to Devin/Cursor/Claude Code/Codex, and timeline.
- **[[concepts/cline]]** — Concept page on the Cline paradigm: autonomy spectrum, Plan/Act toggle, model agnosticism vs provider lock-in, multi-surface engine-first design, .clinerules pattern, multi-agent teams and scheduling, relationship to self-driving codebases.
- **[[concepts/mindwalk]]** — Concept page for Mindwalk (Go, 129 stars), a visualization tool that replays coding-agent sessions on a 3D codebase map. Covers the spatial-intuition approach to agent observability ("what did the agent think?" vs "was the agent correct?"), design, use cases, comparison to trace-based observability, and limitations.
- **[[concepts/reame]]** — Concept page for Reame (C++, 64 stars), a CPU-first LLM inference server on llama.cpp. Covers the "never compute the same thing twice" thesis, architecture (disk KV cache, self-regulating speculation, Conclave, interleaved multi-user), performance (7B on 2-core ARM at 100% accuracy), and comparison to vLLM/llama.cpp server/Ollama.

### Sources
- Cline: GitHub (github.com/cline/cline) — raw: 2026-07-12_cline-autonomous-coding-agent.md
- Mindwalk: GitHub (github.com/cosmtrek/mindwalk) — raw: 2026-07-12_mindwalk-session-replay.md
- Reame: GitHub (github.com/swellweb/reame) — raw: 2026-07-12_reame-cpu-inference-server.md

### Pipeline
- Active crawl discovery via 3 parallel subagents (HN Algolia, xurl X/Twitter, wiki gap analysis)
- 5 raw articles saved; 3 topics selected for page creation (GPU circular financing and Machinecraft deferred due to insufficient source content)
- Tags added to SCHEMA.md: cline (Products)
- Index entries: Concepts 1852→1855, Entities 844→845

---
## [2026-07-12] blog-wiki-ingest | George Hotz "AI 2040 and the Cult of Intelligence"

### Changes
- **[[entities/george-hotz.md]]** — Added "AI 2040 and the Cult of Intelligence" section: Plan A vs Plan L binary, "Cult of Intelligence" framing of singularitarianism, hardware reality check (ocean datacenters, chip fab timelines), ChatGPT alignment test (murder-concealment scenario refused), "you cannot take over the world with tokens" thesis. Updated timeline with Jul 11 entry. Added to Key Writings list. Updated sources frontmatter.

### Sources
- [[raw/articles/geohot.github.io--blog-jekyll-update-2026-07-11-ai-2040-html--34014eca.md]]

---
## [2026-07-11] dreaming | Entity enrichments (Cohere DSD, Fireworks ×2, Hebbia integrations)

### Changes
- **[[entities/cohere.md]]** — Added DSD (Dynamic Speculative Decoding) section: hardware-aware adaptive K selection, Command A/Command A+ performance, ~23% faster than fixed-K SD at BS 128/256, RL rollout relevance
- **[[entities/fireworks-ai.md]]** — Added MiniMax M3 Sparse Attention on Blackwell section: KV-outer kernel, ~980 TFLOP/s, 1.9-2.4× vs FlashInfer, 1.6× vs MSA. Added LangChain Deep Agents on Nemotron 3 Ultra section: 10× cost reduction, post-training path, NVIDIA OpenShell integration
- **[[entities/hebbia.md]]** — Expanded Data Integrations: 12+ sources catalog (SEC, CapIQ, FactSet, PitchBook, Preqin, Third Bridge, Guidepoint, Snowflake, Databricks, SharePoint)

### Source
- dreaming-cycle 2026-07-11

---
## [2026-07-11] watchdog | Auto-fixed 87 bare wikilinks

### Changes
- Fixed **87 bare wikilinks** missing namespace prefixes (e.g., anthropic → entities/anthropic, mcp → concepts/mcp, glimpse → entities/glimpse, bm25 → concepts/bm25, hermes-vs-openclaw-architecture → comparisons/hermes-vs-openclaw-architecture)
- Affected **58 files** across entities, concepts, and comparisons directories
- Remaining 1,720 broken wikilinks are genuine missing targets requiring page creation
- Index: clean (0 corruption, 0 stale entries, validate_index passes)
- No other auto-fixable issues found

### Flagged for Human Review
- **14 duplicate groups** (5 entity, 4 concept, 3 cross-type, 2 concept↔comparison) — need merge decisions
- **63 stale content pages** (>90 days without update) — read and enrich
- **38 orphan pages** (no inbound links) — add cross-references
- **x_accounts job stale (26h)** — check and restart

---

## [2026-07-11] active-crawl | 4 new pages — Replicate, SambaNova, LingBot-World-Infinity, AI-Enabled Terrorism

### New Pages
- **entities/replicate.md** — Replicate: serverless GPU inference platform; Cog ML containerization; founded 2019, backed by a16z/Sequoia/NVentures; pay-per-inference API for open-source models. 162 lines.
- **entities/sambanova.md** — SambaNova: AI chip company; SN40L RDU (Reconfigurable Dataflow Unit); fastest token/s inference for open-source models; .1B+ funding, B+ valuation; competes with Cerebras/Groq/NVIDIA. 156 lines.
- **concepts/lingbot-world-infinity.md** — LingBot-World-Infinity: open-source real-time interactive world model from THU-KING-NIC-Lab (Tsinghua); breakthrough 60-minute coherent rollouts across 20 scenarios; causal action-conditioned modeling. 76 lines.
- **concepts/ai-enabled-terrorism.md** — AI-Enabled Terrorism: CASP (Cambridge) report documenting Boko Haram using frontier AI models for tactical planning, logistics, and bomb-making; HN 207 pts/173 comments; NYT parallel coverage; AI safety/governance implications. 130 lines.

### Updated
- **index.md** — Section headers updated (Entities 842→845, Concepts 1848→1852). 4 new entries added alphabetically.
- **SCHEMA.md** — Added tags: replicate, sambanova, lingbot (Products); terrorism (Domain Concepts)

### Sources
- raw/articles/2026-07-11_replicate-about.md
- raw/articles/2026-07-11_sambanova-about.md
- raw/articles/2026-07-10_lingbot-world-infinity.md
- raw/articles/2026-07-10_casp-boko-haram-frontier-ai.md

### Discovery
- HN Algolia: 15 trending stories identified (GPT-5.6 1524pts, Apple-OpenAI 1119pts, GPT-Live 746pts, GitLost 538pts, Robostral 487pts, etc.)
- X/Twitter: 10 trending discussions (AI market structure 85bkm, on-policy distillation 46bkm, world models, etc.)
- Wiki gaps: Inference infra (Replicate/SambaNova missing), safety guardrails, MCP ecosystem
- Most HN stories already covered by wiki — selected 4 genuine gaps

---
## [2026-07-11] blog-wiki-ingest | Enriched gilesthomas (parameter anatomy) and cory-doctorow (AI slavery fantasy)

### Updated Pages
- **entities/gilesthomas.md** — Added "LLM Parameter Anatomy (July 2026)" section: token embeddings dominate small models (77M of 163M), FFN has ~2x attention params, vocabulary scaling effect, interactive visualizer built with GPT-5.6 Sol via Codex. Pedagogical gap: attention mechanism focus leads to parameter distribution misunderstanding.
- **entities/cory-doctorow.md** — Added "AI Slavery Fantasy — Omelas, Absent Indians, and Paperclips (July 2026)" section: AI Omelas (hidden human labor under algorithm-optimized conditions), Absent Indians (low-waged workers pretending to be robots), paperclips as marketing tool (AI safety x-risk discourse elevates rights-for-robots debate), central thesis that AI sales pitch depends on creating "a new kind of slave." Sources frontmatter and References updated.

### Post-Recovery Verification
- **events/apple-sues-openai-2026.md** — Already existed with full content from newsletter-wiki-ingest (07:40) and blog-triage (07:30). No additional enrichment needed — page covers all key allegations (Tang Tan, Chang Liu, 400+ ex-Apple employees, $6.5B io acquisition, supplier manipulation). Both 9to5Mac and Threads sources already in frontmatter.

### Decisions
- Takes: 1 (gilesthomas enrichment) | References: 1 (cory-doctorow enrichment) | Already-done: 1 (apple-sues-openai event page)
- Triage checkpoint recovered from file (upstream triage JSON parse failure).

---

## [2026-07-11] newsletter-wiki-ingest | Reference: Alex Banks — AI Is Quietly Thinking for Us

### Updated Pages
- **entities/alex-banks.md** — Added "AI Is Quietly Thinking for Us (Jul 2026)" section under Core Ideas: Cognitive Atrophy Paradox — McGill GPS study analogy for AI dependence eroding judgment. Companion piece to "You're Underestimating AI on Purpose" (Jun 2026). Added source reference.

### Sources
- raw/newsletters/2026-07-10-ai-is-quietly-thinking-for-us.md

### Decisions
- Takes: 0 | References: 1 | Skips: 34 (3 batch skip + 31 noise links)
- Triage checkpoint recovered from file (upstream triage JSON parse failure).

---
## [2026-07-11] blog-triage | Wiki pages from blog ingest — Apple-OpenAI lawsuit, AI memory crisis, Thinking Machines Lab, LLM parameter counts

### New Pages
- **events/apple-sues-openai-2026.md** — Apple sues OpenAI for trade secret theft (July 10, 2026): Tang Tan (ex-VP Product Design) and Chang Liu (ex-senior engineer) accused of stealing hardware designs, confidential files, and supplier intel. 400+ ex-Apple employees at OpenAI.
- **concepts/ai-memory-crisis.md** — AI-driven memory price crisis: HBM demand from NVIDIA GPUs consuming 65% of global HBM supply; Samsung/SK Hynix/Micron triopoly driving 700% DRAM price increase; consumer electronics (consoles, phones, laptops) all getting more expensive.
- **entities/thinking-machines-lab.md** — Thinking Machines Lab: AI company advocating decentralized, customizable models; "build AI that extends human will and judgment"; argues against centralized alignment; bets on interaction models and fine-tuning tools.
- **concepts/llm-parameter-counts.md** — LLM parameter distribution intuition: embeddings dominate small models, FFN has ~2x attention params, weight tying impact, scaling from 124M to 70B+.

### Updated Pages
- **entities/openai.md** — Added "Apple Sues OpenAI for Trade Secret Theft (July 2026)" section linking to event page.
- **index.md** — Updated counts (Entities 842→843 [ghost resolved], Concepts 1846→1848, Events 15→16). Added 4 new entries.
- **index.md** — Resolved ghost entry for `thinking-machines-lab` with description.

### Sources
- raw/articles/9to5mac.com--2026-07-10-apple-sues-openai-trade-secret-theft--c6113a74.md
- raw/articles/wheresyoured.at--premium-the-haters-guide-to-the-memory-crisis--0b884d04.md
- raw/articles/thinkingmachines.ai--blog-the-future-worth-building-is-human--7fe53b6e.md
- raw/articles/gilesthomas.com--2026-07-llm-parameter-counts--674e98c7.md

---

## [2026-07-10] backlog-ingest | Enriched MAI-Thinking-1 entity with safety/red-teaming details

- **entities/mai-thinking-1.md** — Expanded Safety & Red Teaming section with detailed internal safety evaluation (jailbreak taxonomy: Foundational/Compositional/Adaptive techniques, 9.5K prompts, ASR comparable to Sonnet/Opus), internal red teaming mitigation results (~22% aggregate ASR reduction), and independent red teaming findings (TAP closed-loop pipeline, multilingual vulnerability in 6 low-resource languages). Updated `updated` to 2026-07-10.
- raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md

---

## [2026-07-10] dreaming | Reference enrichment — Gumloop case study to Fireworks AI

- **`entities/fireworks-ai.md`** — Added Gumloop case study section: GLM-5.2 replaced Opus 4.8 (nobody noticed), 72% cost savings, 7x growth in open-weight model agent chats in 3 weeks, reliability as Fireworks differentiator. Updated `updated` to 2026-07-10 and added source.
- raw/articles/2026-07-10_fireworks-ai_gumloop.md

---

## [2026-07-10] health-fix | index repair — orphan registration + section counts

### Changes
- **Added orphan entries** to index.md: concepts/harness-engineering/agentic-workflows/vibe-coding (Vibe Coding), queries/wiki-graph-analysis-weekly-2026-06-19
- **Fixed section header counts**: Entities 836→842, Concepts 1868→1846, Queries 5→6
- **Skipped _index files** (20 pages) and _archive pages per policy

### Verification
| Metric | Status |
--------|--------|
| Index structural health | Clean (2760 lines) |
| Ghost entries | 0 |
| Index corruption | None detected |

---

## [2026-07-10] watchdog | auto-fix: log header, updated dates (6 files)

### Changes
- **Fixed log.md header burial** — header was at line 409; moved to top, all orphaned entries relocated below header
- **Added updated: 2026-07-10** to 6 pages missing the field:
  - entities/parallel-web-systems.md
  - concepts/local-first-architecture.md
  - concepts/meta-meta-prompting.md
  - comparisons/claude-mythos-preview-vs-mythos5-fable5.md
  - comparisons/bing-api-alternatives-2026.md
  - comparisons/google-alerts-alternatives-2026.md

### Live verification summary
| Metric | Status |
--------|--------|
| Index structural health | Clean (2758 lines) |
| Pipe prefix corruption | 0 |
| Triple bracket corruption | 0 |
| Line-number corruption | 0 |
| Log header position | At line 1 |
| Log pipe corruption | 0 |
| Ghost entries (stale index) | 0 |
| Index coverage gap | 4 |
| Missing updated | 0 |
| Missing sources | 0 |
| Missing type | 0 |
| Missing created | 23 (needs attention) |
| Entity duplicates | 6 pairs (needs attention) |
| Concept duplicates | 4 pairs (needs attention) |

### Escalations
- **23 pages missing created:** -- exceeds auto-fix threshold (9). Needs batch pass with git-log date lookup.
- **10 duplicate groups** -- 6 entity pairs, 4 concept pairs. Documented in graph analysis report. Needs dedicated dedup pass.

---

## [2026-07-10] weekly wiki-graph-analysis | graph health + person×concept analysis

**Scripts**: `scripts/wiki_graph_analysis_weekly.py` + `scripts/wiki_graph.py`

**Summary**: 2,201 pages scanned. 38 orphans, 4,274 broken links (616 fewer than last week), 14 duplicate groups (25 fewer), 2 index gaps (1,992 fewer), 0 tag violations. Person×concept graph: 187 persons × 1,781 concepts — 15 cross-reference gaps identified. Full report: [[queries/wiki-graph-analysis-weekly-2026-07-10]].

---
## [2026-07-10] active-crawl | 4 new pages from trending topics

**Sources**: HN Algolia trending (Jul 7-10) + X/Twitter search + wiki gap analysis + blogwatcher DB
**Topics selected**: 4 (from 45+ HN stories, 60+ tweets, 30+ gaps)

### Pages created:
- [[concepts/coding-agents/databricks-coding-agent-benchmark]] — Databricks benchmarking coding agents (Claude Code, Codex, Devin) on their multi-million line production codebase. Three capability tiers, open models competitive, harness efficiency matters.
- [[concepts/mistral-robostral-navigate]] — Mistral's 8B VLA robotics navigation model; single-camera, SOTA on R2R-CE, cross-embodiment, two-stage training with prefix-caching + CISPO RL.
- [[concepts/claude/fable-safety-classifiers-critique]] — Rob Patro (Combine Lab) critique of Anthropic Fable's overzealous safety classifiers blocking legitimate CS research tasks.
- [[entities/rowboat]] — Open-source (Apache 2.0), local-first Claude Desktop alternative with knowledge graph memory, MCP integration, BYO models. Show HN Jul 7 (216 pts).

### Raw articles saved:
- wiki/raw/articles/2026-07-10_databricks-coding-agent-benchmark.md
- wiki/raw/articles/2026-07-10_mistral-robostral-navigate.md
- wiki/raw/articles/2026-07-10_fable-safety-classifiers-critique.md
- wiki/raw/articles/2026-07-10_rowboat-claude-desktop-alternative.md

### Topics already covered (skipped):
- GPT-5.6 (extensive existing coverage, 42 concept pages)
- Grok 4.5 (event page + 3 entities already enriched Jul 9)
- GLM 5.2 local inference (existing concepts)
- GitLost agent prompt injection (existing concepts/security-and-governance/gitlost-agent-prompt-injection)
- Microsoft Flint (existing concepts/flint-visualization-language)
- Claude 5/Sonnet 5 (existing concepts/claude/sonnet-5)
- AI supply chain / SemiAnalysis (existing entity + concept pages)

### Stats:
- Wiki now: 1,868 concepts, 836 entities, 34 comparisons, 4 queries, 15 events = 2,757 total pages
- 4 raw articles saved

---
## [2026-07-10] blog-wiki-ingest | Muse Spark 1.1 enrichment, Simon Willison GPT-5.6 reference

- **Source**: blog-triage checkpoint (Jul 10 07:37 UTC) — 11 articles triaged, 1 take, 3 reference, 7 skip
- **Recovery**: blog-triage output render failed; triage checkpoint recovered from `triage_latest.json` (per pipeline recovery pattern)
- **Pages enriched**:
  - `concepts/meta-muse-spark.md` — Added Muse Spark 1.1 section: first API release, llm-meta-ai plugin (Simon Willison), agentic tool calling/computer use improvements, Attractor States in Self-Conversation finding. Fixed broken wikilinks in Related section. Updated `updated` to 2026-07-10.
  - `entities/simon-willison.md` — Added July 9 GPT-5.6 hands-on assessment entry (pricing, Agents' Last Exam vs SWE-Bench Pro skepticism, Cost per Pelican). Added Muse Spark 1.1 coverage entry (llm-meta-ai plugin, cross-wikilink to concepts/meta-muse-spark).

**Decisions:** 1 take (Muse Spark 1.1 → concepts update), 3 reference, 7 skip

---
## [2026-07-10] newsletter-wiki-ingest | Meta MSL 1-Year enrichment, Grok 4.5 pricing, GPT-5.6 source

- **Source**: newsletter-triage checkpoint (Jul 10 07:20 UTC) — 6 newsletters triaged, 1 take, 2 reference, 3 skip
- **Recovery**: newsletter-triage output render failed; triage checkpoint recovered from `triage_latest.json` (per pipeline recovery pattern)
- **Pages updated**:
  - `entities/meta.md` — Expanded Superintelligence Labs (MSL) section with SemiAnalysis 1-year progress report: $14.3B Scale AI/Alexandr Wang poaching, data/RL supply chain ($1B+ ARR), 3,000 engineers on RL tasks, 5x 1GW+ Titan clusters (Hyperion 1.5GW world's largest single buildings), Tokenomics model projecting Meta surpasses OpenAI+Anthropic compute by end-2026. Updated sources, Key People (Alexandr Wang named).
  - `events/grok-4-5-launch.md` — Added pricing position (~6x cheaper than Opus 4.8, ~3x cheaper than GPT-5.5) from Ben's Bites reference. Updated sources.
  - `concepts/gpt/gpt-5-6.md` — Added AINews July 10 bulletin as source reference.

**Decisions:**
- 5-star entities/meta.md — SemiAnalysis Meta Superintelligence: genuine enrichment gap (existing page had 2-line placeholder)
- 3-star events/grok-4-5-launch.md — Ben's Bites pricing reference: pricing comparison not in the launch event page
- 3-star concepts/gpt/gpt-5-6.md — AINews source: page already comprehensive, added source reference only
- 1-star Lenny's Podcast (Adam Mosseri) — Skip: social media strategy, not core AI/Agent tech
- 1-star True Positive Weekly #169 — Skip: pure link digest
- 1-star Beehiiv uid=348 (GPT-Live) — Skip: all URLs 403/Cloudflare, topic already covered

**Sources:**
- raw/newsletters/2026-07-09-the-future-of-meta-superintelligence-a-1-year-progress-update.md
- raw/newsletters/2026-07-09-grok-x-cursor.md
- raw/newsletters/2026-07-10-ainews-openai-launches-gpt-5-6-sol-terra-luna-codex-becomes-chatgpt-superapp.md

---

## [2026-07-10] blog-ingest | GPT-5.6 GA, ChatGPT Work, Muse Spark 1.1, Sierra AI-pilling

- **Source**: blog-ingest checkpoint (Jul 10 07:00 UTC) — 31 new articles, 11 saved, 9 unsaved
- **Key event**: OpenAI GPT-5.6 (Sol/Terra/Luna) general availability + ChatGPT Work agent launch (Jul 9)
- **Pages updated**:
  - `concepts/gpt/gpt-5-6.md` — Added GA section: specifications, new API features (Programmatic Tool Calling, Multi-agent, Prompt cache breakpoints), benchmark claims (Agents' Last Exam 53.6, SWE-Bench Pro comparison), availability tiers, model retirement schedule, cost analysis
  - `entities/openai.md` — Added July 2026 Product Launches section: GPT-5.6 GA, ChatGPT Work agent, Codex merged into ChatGPT desktop, ChatGPT Sites, Fidji Simo departure, Microsoft 365 Copilot integration, Bio Bug Bounty. Updated Key Products list.
  - `entities/muse-spark.md` — Upgraded from skeleton to full page: Muse Spark 1.1 (first API-available model), llm-meta-ai plugin, Attractor States finding
  - `entities/sierra.md` — Added "AI-Pilling Our Company" section: Pinecone single-agent architecture, proactive agent patterns, context-as-bottleneck thesis, agent-as-UI model, outcomes-over-activity metrics
- **Not covered**: 9 unsaved articles (OpenAI official pages behind Cloudflare, NYT Meta/Instagram article, astronomy blog)

---
## [2026-07-09] dreaming | Knowledge consolidation — reference enrichment (triage recovery)

- **Source**: dreaming-collect checkpoint (Jul 9 18:00), group-agent JSON parse failure recovered via `latest.json` + triage checkpoint
- **State**: Pipeline saturation — 1 non-AI RSS article skipped, 155 raw articles on disk scanned (15 evaluated), all 14 sitemap/blog-ingest articles already covered by daily pipelines
- **`entities/elevenlabs.md`** — Added Fyxer Case Study section: Scribe v2 STT benchmark (20% WER reduction vs control, 15% relative lift in user conversion, 6,000+ orgs A/B test, exclusive transcription provider rollout). Bumped `updated` to 2026-07-09 and added source.

**Sources:**
- raw/articles/2026-07-09_elevenlabs_fyxer.md

---

## [2026-07-09] watchdog | Auto-fix: added frontmatter to 3 legacy pages

- **Fixed**: Added YAML frontmatter (title, type, created, updated, tags, sources, status) to 3 pages that had none:
  - `entities/uipath.md` — tags: [entity, company, enterprise-ai, coding-agents]
  - `concepts/cursor-automations.md` — tags: [concept, coding-agents, cursor, developer-tooling]
  - `concepts/mistral-medium-3-5.md` — tags: [concept, model, open-source, mistral]
- **Verified**: All tags conform to SCHEMA.md taxonomy. Index.md structurally clean (0 corruption issues).

---

## [2026-07-09] Raw Backlog Ingest — archive 5 articles, cleanup 2 duplicate stubs

### Archived (already captured by previous pipeline runs)
- **`raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md`** — Content fully covered in [[concepts/mai-thinking-1-tech-report]] (227 lines) + [[entities/mai-thinking-1]] (148 lines)
- **`raw/articles/benchflow-awesome-evals-2025.md`** — Content fully covered in [[concepts/ai-benchmarks/benchflow-tool]] (118 lines)
- **`raw/articles/reframing-superintelligence-fhi-2019.md`** — Already archived
- **`raw/articles/dwarkesh.com--p-grant-sanderson-2--960d89cd.md`** — Already archived
- **`raw/articles/webkit.org--blog-17967-news-from-wwdc26-webkit-in-safari-27-beta--c116f751.md`** — Already archived

### Cleanup
- **Fixed** [[concepts/mai-thinking]] — Removed Korean text artifacts (독), reorganized with hill-climbing machine concepts, added proper cross-references
- **Fixed** [[concepts/mai-thinking-1-report]] — Converted duplicate 22-line stub into redirect page pointing to [[concepts/mai-thinking-1-tech-report]]
- **Updated** index.md — Updated descriptions for mai-thinking and marked mai-thinking-1-report as redirect


---
## [2026-07-09] Active Crawl — 3 new concept pages + 1 enrichment

### Created
- **`concepts/gpt-live.md`** — GPT-Live: OpenAI's full-duplex real-time voice interaction mode (July 8, 2026). Covers full-duplex vs half-duplex, key use cases (translation, language learning), market context (Gemini Live, open-source), community reception (717 HN pts). Sources: raw/articles/2026-07-08_openai_gpt-live.md (HN discussion-based, OpenAI blog HTTP 403).
- **`concepts/flint-visualization-language.md`** — Flint: Microsoft Research's JSON-based visualization DSL for AI agents. Compiles to ECharts, MCP-integrated via flint-chart server. Comparison to Vega-Lite, Graphviz, ECharts. Community reception: 295 HN pts. Sources: raw/articles/2026-07-08_microsoft_flint-visualization-language.md (HN discussion-based, project page JS-rendered).
- **`concepts/inference-provisioned-throughput.md`** — Provisioned Throughput: Together AI's reserved inference capacity for open-weight models with token pricing and 99% SLA. Covers market gap (serverless vs dedicated), cost advantage (90% below Claude Opus 4.8), market context (30B→400T tokens/month). Sources: raw/articles/2026-07-08_together-ai_provisioned-throughput.md (full article extracted).

### Updated
- **`concepts/quantifying-infrastructure-noise-in-agentic-coding-evals.md`** — Enriched from 25-line skeleton to 71-line full page. OpenAI analysis of SWE-Bench Pro reliability: infrastructure noise, benchmaxxing, harness variance, private benchmarks, evaluation design best practices. Sources: raw/articles/2026-07-08_openai_coding-evaluation-noise.md (OG metadata + HN discussion).

### Raw Articles Saved
- `raw/articles/2026-07-08_openai_gpt-live.md`
- `raw/articles/2026-07-08_microsoft_flint-visualization-language.md`
- `raw/articles/2026-07-08_together-ai_provisioned-throughput.md`
- `raw/articles/2026-07-08_openai_coding-evaluation-noise.md`

---
## [2026-07-09] Blog Wiki Ingest — enrich entities/giles-thomas.md with Part 34b and Poppy training box

### Updated
- **`entities/giles-thomas.md`** — Enriched with Part 34b (JAX GPT-2 Small implementation: test loss 3.418784 beats PyTorch and original GPT-2, 37h15m training, full 32-bit precision, incremental architecture build) and Hardware: Poppy the Training Box section (dedicated LLM training machine build, RTX 3090 upgrade, 22,557 tokens/sec throughput, 368W power). Added sources and references for both articles. Bumped `updated` to 2026-07-09.

### Sources
- raw/articles/gilesthomas.com--2026-07-llm-from-scratch-34b-building-and-training-gpt-2-sma--64a53b57.md
- raw/articles/gilesthomas.com--2026-07-poppy-the-training-box-1-the-beginnings--dfae584f.md

---

## [2026-07-09] Newsletter Wiki Ingest — enrich entities/modal-labs.md with Agent Experience (AX) interview content

### Updated
- **`entities/modal-labs.md`** — Enriched with Modal CTO Akshat Bubna's Agent Experience (AX) design philosophy. Added section: Agent Experience (AX) Design Philosophy with subsections on "Agent Cloud" thesis, why Kubernetes fails for bursty AI workloads, GPU snapshotting and cold start optimization, RL rollouts at 100,000 sandbox scale, Modal as "Agent Cloud Future." Added AX-related wikilinks. Bumped `updated` to 2026-07-09. Added newsletter source.

### Sources
- raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-modal-cto.md

---

## [2026-07-09] Newsletter Wiki Ingest — add Claude Fable reference to agentic-engineering

### Updated
- **`concepts/agentic-engineering.md`** — Added reference entry for Vanishing Gradients podcast episode 5 (Nicolay Gerold, AMP Code CEO) on Claude Fable for coding agents. Covers: AMP's handoff feature removal (compaction improved, model ate the feature), TypeScript/Rust for AI engineering workflows preference. Bumped `updated` to 2026-07-09.

### Sources
- raw/newsletters/2026-07-08-what-claude-fable-means-for-coding-agents.md
---
## [2026-07-09] wiki: Create Agent Experience (AX) concept page from Modal CTO interview triage

### Created
- **`concepts/agent-experience.md`** — New concept page about Agent Experience (AX), the design philosophy for cloud infrastructure built for autonomous AI agents rather than human developers. Covers: AX vs DX comparison, key infra requirements (programmatic primitives, API-first, standardized sandboxes), why Kubernetes fails for AI agents, Modal's capabilities (GPU snapshotting, DeFlash speculative decoding, Auto Endpoints, RL rollouts). Tags: concept, infrastructure, ai-agents, cloud-infrastructure, developer-experience. Source: raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-modal-cto.md.

### Updated
- **`wiki/index.md`** — Added `concepts/agent-experience` entry to Concepts section; updated Concepts count from 1838 → 1839.

### Sources
- raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-modal-cto.md

---

## [2026-07-09] wiki: Add GPT-Live event, update simon-willison link blog entries (Jul 8 batch)

### Created
- **`events/2026-07-08-openai-gpt-live.md`** — OpenAI GPT-Live Voice Mode event page. Covers: GPT-5.5 background delegation architecture, continuous conversation flow, quality improvements over GPT-4o-era voice mode, Simon Willison's preview testing (1-hour dog-walking conversation), laughing-at-non-jokes bug fix. Tags: openai, model, voice, multimodal, chatgpt.

### Updated
- **`entities/simon-willison.md`** — Added 3 new link blog entries from July 8: Introducing GPT-Live (real-time voice model with GPT-5.5 delegation), Rewriting Bun in Rust, Kenton Varda. Updated sources (added 3 raw article paths) and bumped `updated` date to 2026-07-09.
- **`wiki/index.md`** — Added `events/2026-07-08-openai-gpt-live` entry to Events section; updated Events count from 13 → 14.

### Sources
- raw/articles/simonwillison.net--2026-jul-8-introducing-gptlive--94860320.md
- raw/articles/simonwillison.net--2026-jul-8-rewriting-bun-in-rust--13af90c8.md
- raw/articles/simonwillison.net--2026-jul-8-kenton-varda--84dd5805.md

---

## [2026-07-08] daily-skeleton-enrichment | Entity enrichment — 2 small entity pages enriched

### Changes
- Enriched entities/parsagon.md — Rewrote from generic stub (37 lines) to comprehensive entity page (2.6KB). Added: creator info (Sandy Suh, sand1929), CLI/Python API details, natural language browser automation description, PyPI package details (v1.0.1, Jun 2026), note about platform pivot to Global Policy Intelligence. Corrected previous mischaracterization as generic web scraping platform.
- Enriched entities/exa.md — Expanded from skeleton (38 lines, 1.1KB) to full entity (96 lines, ~4KB). Added: founders (Will Bryk CEO, Jeff Wang co-founder), product suite (Search, Contents, Deep, Agent, Monitors, Exa Connect), technical architecture (500B+ webpages, H200 cluster), customer references (Cursor, Cognition, HubSpot, OpenRouter, 400K+ developers), advisor info (Tal Broda).

---
## [2026-07-08] dreaming | Knowledge consolidation — 2 reference enrichments

### Changes
- Enriched entities/ed-zitron.md — added "Let AI Burn" (Jul 2026) to Notable Articles table + sources
- Enriched entities/fireworks-ai.md — added GLM 5.2 Fast GPU Scheduler Reclaim case study under Enterprise Case Studies
- Source: dreaming-group triage (filesystem scan of 156 raw articles)
- Takes: 0 | References: 2 | Skips: 13

---
## [2026-07-08] health-fix | Register 20 orphan concept pages in index.md

### Changes
- Added 19 concept pages from concepts/harness-engineering/system-architecture/ to index.md
- Added 1 concept page from concepts/harness-engineering/agentic-workflows/using-git-with-agents to index.md
- Corrected Concepts section count from 1841 to 1838 (actual entry count)
- No index corruption detected (pipe, line-number, triple-bracket, space-prefix all clean)
- 0 ghost entries (all index wikilinks resolve to existing files)
- validate_index.py: clean (2747 lines)

---

## [2026-07-08] watchdog | Auto-fix index issues

### Changes
- Removed duplicate `concepts/agent-harnesses` entry at comparisons section boundary
- Restored misplaced `concepts/evals-skills` and `concepts/llm-integration-patterns` entries to correct alphabetical position
- Fixed Entities header count: 842 → 841 (actual files)
- Fixed Concepts header count: 1,861 → 1,841 (actual files)
- Verified: 0 tag violations, 0 source field gaps on knowledge pages, 0 orphan timestamps in log.md

### Issues requiring attention
- **78 file orphans**: Subdirectory pages (harness-engineering/system-architecture/, etc.) not in index — needs human review
- **684 pages missing sources field** (per graph analysis) — pipeline is addressing incrementally

---

## [2026-07-08] Active Crawl — Agent Security & Claude Code History

### Created
- **`concepts/security-and-governance/gitlost-agent-prompt-injection.md`** — GitLost: GitHub AI agent prompt injection attack by Noma Security. First major public demo of prompt injection in a platform-integrated coding agent. 218 HN points. Disclosed to GitHub.
- **`entities/halo-tamper-evident-agent-runtime.md`** — Halo: open-source (Apache-2.0) tamper-evident runtime evidence for AI agents. Append-only hash-chained log, zero runtime dependencies, ~4,300 lines of auditable Python.

### Enriched
- **`entities/claude-code--history.md`** — Added Origins section from Anthropic's "The Making of Claude Code" blog (July 2026). Internal CLI was originally called "clide". Core design bet on read/edit/bash primitives. Updated tags and sources.
- **`concepts/ai-agent-safety-incidents.md`** — Added GitLost incident section. Updated tags (prompt-injection, agent-security, incident, github) and sources.

### Raw Articles
- [[raw/articles/2026-07-07_anthropic-making-of-claude-code]] — The Making of Claude Code (Anthropic Blog)
- [[raw/articles/2026-07-08_noma-security-gitlost-github-agent-leak]] — GitLost (Noma Security Blog)
- [[raw/articles/2026-07-07_bkuan001-halo-tamper-evident-runtime-evidence]] — Halo README (GitHub)

### Sources
- HN Algolia API search (15 trending AI stories)
- xurl X/Twitter search (12 substantive AI results)
- Blogwatcher DB query (30 articles from last 3 days, 6,826 total)
- Wiki gap analysis across 10 key areas (2,701 pages scanned)

---


## [2026-07-08 08:00 UTC] raw-backlog-ingest | Archived 2 unprocessed raw articles (5 candidates: 3 already archived, 2 content-already-captured)

**Processed 5 candidates from backlog (ai-hint sorted):**
- `reframing-superintelligence-fhi-2019.md` — Already archived (Drexler CAS report 2019)
- `2026-06-03_microsoft-mai-thinking-1-tech-report.md` — Skip, content fully covered in entities/mai-thinking-1 + concepts/mai-thinking-1-tech-report + concepts/microsoft-mai-models
- `benchflow-awesome-evals-2025.md` — Skip, content fully covered in concepts/ai-benchmarks/benchflow-tool
- `dwarkesh.com--p-grant-sanderson-2--960d89cd.md` — Already archived (Grant Sanderson math interview)
- `webkit.org--blog-17967-news-from-wwdc26-webkit-in-safari-27-beta--c116f751.md` — Already archived (Safari 27 beta release notes)

**Newly archived:** 2 articles (MAI-Thinking-1 tech report, BenchFlow Awesome Agent Evals)
**Total archive URLs:** 1,434

---
## [2026-07-08] wiki: Blog-wiki-ingest - LLM gateways enrichment, reference items

**Blog triage recovered from checkpoint (20 decisions: 3 takes, 6 references, 11 skips). All 3 takes already processed by other pipelines (comparisons/llm-gateways created, concepts/ai-industry-economics enriched, entities/openai AP+ case study added). Processed 4 reference enrichments.**

**Pages updated:**
- entities/simon-willison.md — sqlite-utils 4.0 final release entry (migrations, nested transactions, compound FKs); github-code Web Component entry
- concepts/notion-mcp.md — Merge Agent Handler third-party Notion MCP integration section
- concepts/ai-governance-political-pressure.md — Doctorow antitrust enforcement reference added
- concepts/apple.md — Siri iOS 27 beta 3 voice customization (Pace/Expressivity sliders)

---
## [2026-07-08] wiki: Newsletter-wiki-ingest - Fable entity, enrichments

**Newsletter triage recovered from checkpoint (5 newsletters: Ben's Bites, AINews, SemiAnalysis, Super Intel, Lenny's Newsletter)**

**Created:**
- `entities/fable.md` — Anthropic Fable coding harness entity page (creative thinking partner use case, "square peg for a round hole" harness design tension, Opus-like interaction traits, subagent orchestration, memory compaction); tags: entity, product, anthropic, agent-harness, coding-agent

**Updated:**
- `entities/lilian-weng.md` — Added "Added Context: AINews Synthesis (July 2026)" subsection connecting Weng's Harness Engineering survey to current product landscape (Cowork UX, Claude Cowork mobile, Codex Mobile iOS); "Harness engineering is increasingly the center of agent design" framing
- `entities/anthropic.md` — Added "SemiAnalysis IPO Financial Projection (July 2026)" subsection: 3Q26 $1B profit projection, June 1 confidential IPO filing (both paywalled/qualifier-appended)
- `concepts/harness-engineering.md` — Added "Cognitive UX in Harness Design" section: creative partner vs coding assistant design tension, Opus-like interaction traits, system prompt plasticity; cross-links to agentic-engineering and entities/fable
- `wiki/index.md` — Added entities/fable entry

---
## [2026-07-08] wiki: Enrich OpenAI entity with Australian Payments Plus case study

**Updated:**
- `entities/openai.md` — Added Australian Payments Plus enterprise adoption case study (80% employees more creative, 300+ custom GPTs, 1000+ Projects, Codex for reconciliation/investigation, simulations in 1 day vs weeks); added tags (enterprise-ai, chatgpt, codex, llm, case-study); added related wikilinks to concepts/ai-industry-economics, concepts/token-economics, entities/anthropic

---
## [2026-07-08] wiki: Add LLM gateways comparison page

**Created:**
- `comparisons/llm-gateways.md` — LLM Gateways Comparison (Eden AI, Merge Gateway, OpenRouter, LiteLLM, Portkey); features, pricing, self-hosting, governance, observability, use-case recommendations

**Updated:**
- `wiki/index.md` — Added llm-gateways entry in Comparisons section (alphabetical)

---

## [2026-07-07] wiki: Added Anthropic RSI evidence to recursive-self-improvement

**Updated:**
- `concepts/recursive-self-improvement.md` — Added "Industry Evidence: Anthropic's RSI Trajectory" (metrics, benchmarks, task horizon doubling, narrowing human role) + "Safety & Governance Concerns" (safety interventions, reward hacking, verification, dual framing); added 2 new sources
- `entities/anthropic.md` — Added cross-reference to RSI concept page

---

## [2026-07-07] wiki: Split RSI into standalone concept page

**Created:**
- `concepts/recursive-self-improvement.md` — Standalone RSI page (21 references, benchmarks, open challenges)

**Updated:**
- `concepts/harness-engineering.md` — RSI section replaced with concise summary + link to standalone page; added RSI to Related Concepts
- `entities/lilian-weng.md` — Added RSI concept link
- `wiki/index.md` — Updated recursive-self-improvement entry description

---

## [2026-07-07] wiki: Ingested Lilian Weng "Harness Engineering for Self-Improvement"

**Ingested:**
- `raw/articles/2026-07-04_lilianweng-harness-engineering-self-improvement.md` — New raw article (Lilian Weng, July 4, 2026)

**Updated:**
- `entities/lilian-weng.md` — Added Jul 2026 timeline entry, "Harness engineering for RSI" theme, related concept link, source URL
- `concepts/harness-engineering.md` — Added RSI section (design patterns, optimization progression, self-improving harnesses, evolutionary search, auto-research workflows, open challenges); added new tags and source
- `wiki/index.md` — Updated lilian-weng entry description

---

## [2026-07-07 17:50 UTC] health-fix | Auto-fix: orphan index registration

**Auto-fixed:**
- `wiki/index.md` — Added 20 harness-engineering/agentic-workflows sub-pages to Concepts section (orphan index registration)

---

## [2026-07-07 17:35 UTC] watchdog | Auto-fix and health report

**Auto-fixed (2):**
- `entities/armin-ronacher.md` — Fixed pipe-prefixed (`|-`) list item on line 256 → normalized to `-`
- `queries/wiki-graph-analysis-weekly-2026-07-05.md` — Fixed 15 quadruple-bracket (`[[[[`) wikilinks → normalized to `[[`

**Verified clean (no action needed):**
- `index.md` — 0 corruption (validate_index.py ✅, 2703 lines)
- Tag violations — 0 (tag taxonomy clean)
- Missing `sources` field — 0 (down from 684 in earlier reports)
- Stale/ghost index entries — 0 (subdirectory files confirmed)
- Active wiki pages — 0 residual corruption after fixes

**Needs attention (2):**
- **Subdirectory concept index gap**: 41 subdirectory concept pages (`harness-engineering/agentic-workflows/*`, `harness-engineering/system-architecture/*`, etc.) exist on disk but aren't in `index.md`. They're navigable via `_index.md` subdirectory files. Needs human decision on whether to add to main index.
- **Pipeline: x-accounts-scan stale (~26h)**: Reported stale by pipeline watchdog. Job runs every 2 days — likely within normal schedule.

---

## [2026-07-07 11:00 UTC] active-crawl | 4 new pages from trending HN/X topics

**active-crawl**: Created 4 new wiki pages from trending topics (July 3-7, 2026):

- [[concepts/anthropic-global-workspace]] — Anthropic interpretability research finding transformer LMs spontaneously develop a 'global workspace' bottleneck analogous to biological consciousness (386 HN pts, 145 comments)
- [[entities/amd-ryzen-ai-halo]] — AMD's $4,000 AI dev kit with unified memory architecture for local LLM inference (342 HN pts)
- [[concepts/code-cleanliness-coding-agents]] — arXiv study (2605.20049) on how codebase cleanliness impacts coding agent token usage (-7-8%) and file revisitations (-34%) across 660 Claude Code trials (198 HN pts)
- [[concepts/browser-integrated-ai]] — Trend of embedding AI models in browsers, sparked by Chrome silently installing a 4GB Gemini Nano model (78 HN pts)

Raw articles saved: 2026-07-07_anthropic_global-workspace-language-models.md, 2026-07-07_lttlabs_amd-ryzen-ai-halo-dev-kit.md, 2026-05-19_arxiv_2605.20049_code-cleanliness-coding-agents.md, 2026-05-16_oztalking_chrome-hidden-4gb-ai-model.md

SCHEMA.md: Added 3 new tags (consciousness, ai-hardware, chrome). Updated index.md with 4 new entries.

Sources: HN Algolia API, X/Twitter xurl search, arXiv, Anthropic Research, LTT Labs, OZ Talking. Cross-referenced against wiki gaps — all 4 were genuine gaps.


---
## [2026-07-07 07:50 UTC] blog-wiki-ingest | 2 pages enriched from 1 blog take

- **Enriched** [[concepts/ai-industry-economics]] — 137→186 lines. Added Open-Weight Margin Collapse section: GLM 5.2 as open-weights Opus competitor, ~90% gross inference margin analysis, drop-in replacement migration, cost comparison ($4.40 vs $25/MTok), AMD 2.75x inference efficiency, structural implications. Source: Martin Alderson margin collapse part 1.
- **Enriched** [[entities/martin-alderson]] — 288→302 lines. Added Open-Weight Margin Collapse subsection under AI Compute Economics. GLM 5.2 breakthrough, frontier margin analysis, cost comparison, AMD efficiency, structural thesis.
- Updated index.md and log.md for all changes.

---
## [2026-07-07 07:40 UTC] newsletter-wiki-ingest | 7 pages enriched from 6 newsletters

- **Enriched** [[concepts/claude/fable-5]] — 425→543 lines. Added 3 new Post-Redeployment sections: GPU Kernel Generation (18.71× CUDA speedup on KernelBench-Mega), Thariq Shihipar's Field Guide (unhobbling, blindspot passes, grief management, "tradeoffs are not real"), Fable 5 Return Aftermath & Sonnet Guidance (99% blocker, government pre-release deal). Sources: Import AI 464, AI by Aakash, AINews.
- **Enriched** [[concepts/ai-benchmarks/remote-labor-index]] — 63→78 lines. Added July 2026 Update: Fable 5 16.1% success rate (up from 2.5% in Oct 2025), quadrupling in under 8 months. Source: Import AI 464.
- **Enriched** [[concepts/ai-benchmarks/osworld]] — 67→81 lines. Added OSWorld 2.0 section: 108 long-horizon tasks (1.6hr median), 31 self-hosted websites, Slack/REAPER/MuseScore/Overleaf integrations. Source: Import AI 464.
- **Enriched** [[concepts/claude/sonnet-5]] — 116→140 lines. Added How I AI Bench section: 64-generation blind test, Sonnet 5 near-bottom in preference ranking but Opus-level codebase navigation, LLM-as-Judge methodology limitations. Source: How I AI.
- **Stub→Full** [[concepts/symphony]] — 25→207 lines. Fully expanded from stub: architecture (WORKFLOW.md, SKILL.md, context compaction, sidecar proxy), Symphony from Phone (Alessio Fanelli pattern: Agent Prompter→Manager, token cost tracking 15M-221M, skills maintenance, Glimpse extension), comparison with Anthropic Managed Agents. Source: How I AI.
- **Enriched** [[entities/tencent-hy3]] — 123→153 lines. Added July 2026 Update: Apache 2.0, 192 experts/top-8 routing, vLLM day-0 support with Tencent production kernels upstreamed, 2.95× mixed-length decode. Source: AI by Aakash.
- **Enriched** [[entities/semianalysis]] — 197→243 lines. Added GPU Debt Backstop: AI Project Trinity analysis — $7.1T AI debt by 2029, NVIDIA minimum revenue guarantees, GPU-backed securities as new asset class, three obstacles to market maturity. Source: SemiAnalysis.
- Updated index.md and log.md for all changes.

---
## [2026-07-07 00:01 UTC] raw-backlog-ingest | Enriched MAI-Thinking-1 entity + BenchFlow Awesome Agent Evals

- **Enriched** [[entities/mai-thinking-1]] — From 55-line entity to 147-line comprehensive page. Added: Architecture section (periodic local/global attention, LatentMoE, model specifications table, scaling ladder), extended benchmark comparison tables (STEM/Agentic Coding, General Capabilities, Human Side-by-Side), modified GRPO section (adaptive entropy control, outer ratio clip, reward decomposition), total training overhead metrics (51 hours). Sources include the full 109-page tech report.
- **Enriched** [[concepts/ai-benchmarks/benchflow-tool]] — Added Awesome Agent Evals detail: compilation methodology (11.6k papers, 47 transcribed talks, 146 deep notes), 12-item must-read starter set table with core theses, eval/RL-environment companies landscape (pavlovslist directory, environment labs, eval platforms, benchmark/audit orgs).
- Updated index.md entries for both pages.

---
## [2026-07-06] skeleton-enrich-daily | Enriched Aman Sanger + David Fowler from L2/stub to comprehensive

- **Enriched** [[entities/aman-sanger]] — From 35-line stub (status: none) to 159-line comprehensive entity page. Added: Background (co-founding story, funding timeline, key metrics), Three Eras of AI Coding, Self-Driving Codebases, Artifacts Paradigm, Multi-Agent Architecture, Codebase Indexing, Reverse-Engineered GPT-4 Inference, Speaking & Media table (Lex Fridman, Latent Space, GTC 2026), Engineering Philosophy subsections (Speed is Not the Product, Compound Engineering, Specification-Driven Development, Don't Lose to Slop), Related People, See Also, and Sources.
- **Enriched** [[entities/david-fowler]] — From 48-line L2 stub to 152-line comprehensive entity page. Added: Quick Facts table (146K followers, 15+ year MSFT career, Barbadian background), detailed Key Projects (SignalR creator, NuGet co-creator, ASP.NET Core architect, Aspire technical lead, Tally), AI & Aspire Philosophy (Speed is Not the Product, Intent vs Mechanics, Agent-Ready Infrastructure), Medium Blog Posts table (7 articles), Career Timeline, Philosophy & Engineering Principles table, and Sources.
- Updated index.md entries with descriptive summaries for both entities.

---

## [2026-07-06 18:15 UTC] dreaming-wiki-ingest | Claude Code Session Cache Leakage — new concept page
- **Created** [[concepts/claude-code/claude-code-session-cache-leakage]] — Claude Code Enterprise ZDR workspace session cache cross-account leakage (Jul 4, 2026). Sonnet 5 cache miss after 5+ minutes injected unrelated Minecraft temple content from another account. 313 HN pts, 132 comments. Distinct incident from [[concepts/claude-code/claude-code-leak]] (March npm supply-chain leak). Cross-platform (CLI + Mobile), confirmed not local. Updated `index.md`.

---
## [2026-07-06 11:16 UTC]

**active-crawl**: Created 4 new concept pages from trending HN/X topics (July 3-6, 2026):

- [[concepts/ai-generated-code-policies]] — AI-Generated Code Policies: Godot engine ban on AI-authored code (558 HN pts), open source governance of AI contributions, policy design space
- [[concepts/reasoning-model-quality-degradation]] — Reasoning Model Quality Degradation: GPT-5.5 Codex reasoning-token clustering at 516/1034/1552 (366 HN pts), hidden constraints, reliability cliff
- [[concepts/enterprise-coding-agent-security]] — Enterprise Coding Agent Security: Claude Code session/cache leakage (313 HN pts) + Alibaba Claude Code workplace ban (335 HN pts), data exfiltration, sandboxing
- [[concepts/ai-inventorship-patent-law]] — AI Inventorship & Patent Law: Japan Supreme Court rules AI cannot be inventor (398 HN pts), DABUS cases, international comparison

Raw articles saved: 2026-06-30_pcgamer_godot-bans-ai-authored-code.md, 2026-06-27_github_gpt55-codex-reasoning-token-clustering.md, 2026-07-04_github_claude-code-session-cache-leakage.md, 2026-03-06_japannews_ai-cannot-be-patent-inventor.md

Sources: HN Algolia API, GitHub Issues API, PC Gamer, Japan News, HN discussions. Cross-referenced against wiki gaps — all 4 were genuine gaps with no prior concept pages.


---
## [2026-07-06] blog-wiki-ingest | Enriched SynthID C2PA section + Sean Goedecke entity page

### Changes
- **Enriched** [[concepts/synthid]] — Added "C2PA Limitations and Critique — Sean Goedecke's Analysis" section (6 critical lenses: all-image signing catch-22, SNS manifest stripping, 26-cert trust list, key management, safety theater, non-image applicability). Updated `updated` date and `sources` with new raw article.
- **Enriched** [[entities/seangoedecke-com]] — Added Timeline entry for "C2PA only works if everything is signed" with wikilink to new synthid C2PA section. Updated `updated` date and `sources`.

### Sources
- raw/articles/seangoedecke.com--c2pa-only-works-if-everything-is-signed--ae4eb8f4.md

### Stats
- Pages enriched: 2 (synthid, seangoedecke-com)
- Articles skipped (archived): 6

---
## [2026-07-06] newsletter-wiki-ingest | Enriched Microsoft + Figure AI + AI Jailbreaking pages

### Changes
- **Enriched** [[entities/microsoft]] — Added Microsoft Frontier Company section ($2.5B, 6,000 engineers embedded in enterprises, Rodrigo Kede Lima, early partners LSEG/Unilever/Accenture, any-model IP protection). Updated `updated` date and sources.
- **Enriched** [[entities/figure-ai]] — Added BMW Plant Spartanburg Deployment section (F.03 parts sequencing in logistics, Figure 02 30K+ BMW X3s track record, fingertip/3g sensors, palm cameras, wireless charging, Centre of Competence for Physical AI, Plant Leipzig pilot). Updated `updated` date and sources.
- **Enriched** [[concepts/ai-jailbreaking]] — Added Industry CVSS for Jailbreaks section (Anthropic+Amazon+Microsoft+Google framework, 4 criteria, HackerOne programme). Updated `updated` date and sources.

### Sources
- raw/newsletters/2026-07-05-anthropic-s-fable-freedom-microsoft-s-inside-job-and-figure-s-factory-foothold.md

---
## [2026-07-06] raw-backlog-ingest | Enriched MAI-Thinking-1 entity page and BenchFlow concept page

### Changes
- **Enriched** [[entities/mai-thinking-1]] — Fixed formatting issues, added Training Infrastructure section (YOLO framework, 8K GB200 cluster, MAIA-200 inference silicon), Safety and Red Teaming section, and updated frontmatter `updated` date to 2026-07-06
- **Enriched** [[concepts/ai-benchmarks/benchflow-tool]] — Added Awesome Agent Evals List section documenting the 443-link curated eval resource compiled by BenchFlow via depth-4 citation crawl. Updated frontmatter `sources` with raw article path and `updated` date

### Sources
- raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md
- raw/articles/benchflow-awesome-evals-2025.md

### Stats
- Pages enriched: 2 (mai-thinking-1, benchflow-tool)
- Articles skipped (already archived): 3

---
## [2026-07-06] x-accounts-scan | Updated Eugene Yan and Lance Martin entity pages with new sources

### Changes
- **Enriched** [[entities/eugeneyan]] — Added ai.engineer conference (2026) appearance with 3 linked resources: "How to Work and Compound with AI" (May 2026), "Patterns for Building Cybersecurity Evals" (Jun 2026), "Using LLMs to Secure Source Code" (Anthropic blog). Updated frontmatter sources and `updated` date to 2026-07-06. Added blog post summaries to Notable Blog Posts table.
- **Enriched** [[entities/rlancemartin]] — Added Sonnet 5 migration guidance via `/claude-api` skill in Claude Code. New source: platform.claude.com prompting-claude-sonnet-5 guide. Updated `updated` date to 2026-07-06. Expanded claude-api Skill section with Sonnet 5 migration support detail.

### Sources
- https://eugeneyan.com/writing/working-with-ai/
- https://eugeneyan.com/writing/cybersecurity-evals/
- https://claude.com/blog/using-llms-to-secure-source-code
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5

### Stats
- Pages enriched: 2 (eugeneyan, rlancemartin)

---
## [2026-07-06] x-accounts-scan | HF CLI + 2 arXiv papers — 1 new concept page, 2 enrichments

### Changes
- **Skipped** [[concepts/coding-agents/hf-cli]] — HF CLI for Agents blog post already fully covered (105-line page + benchmark data + skill details)
- **Created** [[concepts/data-repetition-in-training]] — arXiv 2606.24998: "Internal Data Repetition Destroys Language Models" by Joshua Kazdan et al. Chinchilla-era scaling law analysis of verbatim duplication damage. Key findings: non-monotonic damage peak at intermediate repeat counts, power-law scaling of peak in model size, ~33% compute waste from 10% repeated FLOPs budget. Links to data-filtering-scaling-laws, data-scaling-limits, scaling-laws.
- **Enriched** [[concepts/multi-teacher-on-policy-distillation]] — Added arXiv 2606.30406 (MOPD paper by Wenhan Ma et al., Jun 29) to sources; bumped updated date. Paper confirms MOPD deployment in MiMo-V2-Flash and benchmarks against Mix-RL, Cascade RL, Off-Policy Finetune, Param-Merge baselines.
- **Updated** [[index.md]] — Added data-repetition-in-training entry between data-filtering-scaling-laws and data-scaling-limits

### Sources
- https://huggingface.co/blog/hf-cli-for-agents (already covered)
- https://arxiv.org/abs/2606.24998 (new concept page)
- https://arxiv.org/abs/2606.30406 (source added to existing page)

### Stats
- Pages created: 1 (concepts/data-repetition-in-training)
- Pages enriched: 1 (concepts/multi-teacher-on-policy-distillation — source + date)
- Index entries added: 1

---

## [2026-07-05] skeleton-enrich | Restored microsoft.md corruption, enriched 5+ entity pages

### Changes
- **Restored** [[entities/microsoft]] — Company page restored from git history (was overwritten with Microsoft AI Team content); added MAI internal models section
- **Enriched** [[entities/microsoft-ai-team]] — Fixed YAML corruption; expanded with detailed profile of Microsoft's internal AI research division
- **Redirected** [[entities/microsoft-ai]] — Converted to redirect to microsoft-ai-team (was duplicate)
- **Enriched** [[entities/david-duvenaud]] — Added academic background (UofT/Vector Institute), expanded Talkie section, added sources
- **Enriched** [[entities/periodic-ai]] — Added William Fedus leadership info, AI Scientist vision, physical AI/robotics, infrastructure
- **Created** [[entities/william-fedus]] — New entity page for Periodic Labs CEO, former VP Research at OpenAI
- **Enriched** [[entities/jacob-xiaochen-li]] — Added research focus section, three-paradigm breakdown, MIT CSAIL affiliation detail
- **Enriched** [[entities/aakash-gupta]] — Expanded agent safety section, added Separation of Duties detail
- **Enriched** [[entities/akash-gupta]] — Expanded with structural safeguards detail, cross-reference to aakash-gupta
- **Index** — Updated 7 new entity entries, fixed microsoft description

---
## [2026-07-05] dreaming | Knowledge consolidation — 2 takes, 5 references

### Changes
- Created [[concepts/safari-mcp-server]] — Apple's first MCP server for Safari Technology Preview 247; 17 browser automation tools (July 5)
- Enriched [[concepts/currentai]] — stub → full page: Open Source AI Gap Map (421 products, 14 categories, 228 orgs) (July 5)
- Enriched [[entities/simon-willison.md]] — Fable's judgement (subagent delegation pattern) + llm-coding-agent 0.1a0 (Fable 5 experiment) (July 2-3)
- Enriched [[entities/daringfireball-net.md]] — Gruber's Claude Electron Mac app critique + Drew Breunig analysis (July 3)
- Enriched [[entities/meta.md]] — New section: 2026 Engineering Culture Collapse (Pragmatic Engineer, July 2026)
- Enriched [[concepts/claude/fable-5.md]] — Redeployment details: usage limits, new safety classifier, CAISI validation, industry framework (June 30)
- Updated wiki/index.md — added Safari MCP Server + CurrentAI entries
- Source articles: webkit.org, simonwillison.net (x2), daringfireball.net, anthropic.com, pragmaticengineer.com

### Stats
- Pages created: 1 (concepts/safari-mcp-server)
- Pages enriched: 5 (currentai, simon-willison, daringfireball-net, meta, fable-5)
- Total index entries: concepts +2

---
## [2026-07-05] health | Wiki health digest & index repair

### Changes
- Verified index.md structural integrity: 0 corruption issues ✅
- Added 20 high-priority orphan entity pages to index.md (aaron-levie, adam-mastroianni, alec-radford, andrej-karpathy, chip-huyen, dan-shipper, demis-hassabis, eliezer-yudkowsky, ethan-mollick, fei-fei-li, garry-tan, geoffrey-hinton, gwern, ilya-sutskever, jeff-geerling, jensen-huang, john-carmack, marc-andreessen, sam-altman, satya-nadella)
- Index: 265 lines, 87 entities, 132 concepts (0 corruption)
- 2594 orphan pages remain — auto-apply limit (20) reached

### Stats
- 2753 L2 pages total (849 entities, 1871 concepts, 33 comparisons)
- 7777 raw articles, 4655 unprocessed (59.8% coverage gap)
- 2075 stale pages (>30 days since update)
- 0 skeleton entities, 0 ghost entries

---


## 2026-07-05 — Raw backlog ingest (5 articles)

**Source batch**: raw-backlog-ingest pipeline — 5 articles from backlog (sorted by AI relevance hint)

### Enriched pages:

- `concepts/comprehensive-ai-services.md` — Major enrichment from Drexler 2019 FHI report (210 pages). Added: CAIS core thesis (R&D automation vs agent-centric model), service-oriented intelligence framework, learning vs competence distinction, safety implications, comparison table vs Bostrom's agent-centric model, full ToC-informed structure. (25 → 212 lines)
- `entities/k-eric-drexler.md` — Enriched from stub (23 lines) with full biography, molecular nanotechnology background, CAIS framework details, intellectual positioning vs Bostrom, safety contributions. (23 → 80 lines)
- `entities/grant-sanderson.md` — Enriched from skeleton (36 lines) with Dwarkesh Patel interview content (AI as leading indicator, fractal frontier, conceptual breakthroughs vs pattern matching, hundred-year verification loops, hidden bridges between fields). Merged biographical data from duplicate `entities/grant-sanderson-3blue1brown.md` (education, Stanford/Khan Academy/MIT, channel stats, video series table, Manim engine, ML relevance). (36 → 160+ lines)

### Duplicates resolved:

- `entities/eric-drexler.md` — Converted to redirect → `entities/k-eric-drexler.md`
- `entities/grant-sanderson-3blue1brown.md` — Converted to redirect → `entities/grant-sanderson.md`

### Cross-references updated:

- `entities/future-of-humanity-institute.md` — `[[entities/eric-drexler]]` → `[[entities/k-eric-drexler|K. Eric Drexler]]`
- `concepts/nick-bostrom.md` — `[[entities/eric-drexler]]` → `[[entities/k-eric-drexler|K. Eric Drexler]]`

### Skipped (already covered):

- `2026-06-03_microsoft-mai-thinking-1-tech-report.md` — Fully covered by 227-line `concepts/mai-thinking-1-tech-report.md`
- `benchflow-awesome-evals-2025.md` — Bulk-processed June 26 (57 benchmark pages)
- `webkit.org--blog-17967-news-from-wwdc26-webkit-in-safari-27-beta--c116f751.md` — Non-AI content
---
## 2026-07-05

- **Pages Updated**:
  - `entities/armin-ronacher.md` — Added "Better Models: Worse Tools — Tool Schema Regression" section: Claude Opus 4.8/Sonnet 5 invented tool keys in Pi's edit tool, RL training artifact hypothesis (harness-optimized for Claude Code's forgiving tool shape), strict mode fix, Codex non-regression comparison. Updated `updated` date, sources, and URLs.
  - `entities/simon-willison.md` — Added "July 2026 Updates" section: sqlite-utils 4.0rc2 Fable-driven release ($149.25, cross-model GPT-5.5 review, data-loss `delete_where()` bug discovery); "Better Models: Worse Tools" quote post reference. Updated `updated` date and sources.

- **Pipeline**: active-crawl — 5 new concept pages from trending HN/X sources (July 5)
  - `concepts/better-models-worse-tools.md` — Armin Ronacher on tool-calling regression in newer Claude models (HN 181 pts)
  - `concepts/ai-benchmarks/senior-swe-bench.md` — Snorkel AI benchmark for senior-level coding agents, 24.0% top solve rate (HN 182 pts)
  - `concepts/pxpipe-code-to-image-cost-reduction.md` — Vision-based API cost reduction: 59-70% savings via text-to-image conversion (HN 302 pts)
  - `concepts/short-leash-ai-coding.md` — 12-principle human-in-the-loop AI coding methodology (HN 194 pts)
  - `concepts/single-transformer-layer-rl.md` — arXiv 2607.01232: single-layer RL matches full-parameter training (HN 150 pts)
  - `wiki/raw/papers/2026-07-02_2607.01232_single-transformer-layer-rl.md` — new paper
  - `wiki/raw/articles/2026-07-02_snorkel_senior-swe-bench.md` — new article
  - `wiki/raw/articles/2026-07-02_okturtles_short-leash-ai-coding.md` — new article
  - `wiki/raw/articles/2026-07-03_teamchong_pxpipe-code-to-image-cost-reduction.md` — new article
  - `wiki/SCHEMA.md` — added tags: `regression` (Engineering), `pi` (Products)

- **Pipeline**: blog-wiki-ingest (recovered from blog-triage checkpoint after JSON parse failure)
- **Triage decisions processed**: 2 takes, 1 reference, 12 skips

---
## 2026-07-02

- **Pages Updated**:
  - `concepts/multi-token-residual-prediction.md` — **New**: Multi-Token Residual Prediction (MRP) concept page for DLM inference optimization. 1.56× lossless speedup, +16 accuracy points recovery. Modal × NYU Shanghai HeavyBall Research.
  - `concepts/synthid.md` — Added Text Watermark Criticism section: Sean Goedecke's July 2026 analysis of text watermark removability, SynthID zero-temperature breakage, homoglyph watermarking by OpenAI/Anthropic, AI Act interoperability vs security-by-obscurity conflict.
  - `entities/together-ai.md` — Updated funding from $150M+ Series B to $800M Series C from Aramco Ventures, NVIDIA, Vista Equity. Added 500 MW compute capacity commitment.
  - `entities/seangoedecke-com.md` — Added "Text AI watermarks will always be trivial to remove" (July 2026) to timeline and sources.
  - `concepts/token-economics.md` — Added MTR Rail+Property Business Model Analogy section: Michael Li's Dwarkesh Blog Prize essay on ML labs capturing complementary asset value.

- **Pipeline**: blog-wiki-ingest (recovered from triage checkpoint after blog-triage JSON parse failure)
- **Archived**: 18 skip/reference items

- **Pages Updated**:
  - `concepts/coding-agents/pi-autoresearch.md` — Added Introspection (Roland Gavrilescu/ex-xAI), Agent Recipes framework, Pi as "Linux of agent harnesses" positioning, inner/outer loop distinction, human-in-loop design. (newsletter: Autoresearch — Latent Space)
  - `entities/cursor-ai.md` — Added Forward Deployed Engineering (FDE) section: VP Pauline Brunet, 10× team growth plan, enterprise adoption phases, AI software factory vision. (newsletter: How Cursor deploys AI inside the enterprise — Latent Space)
  - `entities/thariq-shihipar.md` — Added AI Engineer World's Fair 2026 keynote section: "The models are grown, not developed" framing, continuous discovery paradigm. (newsletter: AIEWF Daily Dispatch — Latent Space)
  - `entities/addy-osmani.md` — Added Agency Ladder concept: inner loop (capability) vs outer loop (agency), human outer loop position, AIEWF 2026 talk. (newsletter: AIEWF Daily Dispatch — Latent Space)
  - `entities/geoffrey-litt.md` — Added AI Engineer World's Fair 2026 anti-factory critique: "Factories is a depressing vision" thread (35.5K Views), Design Engineering track on human understanding of code. (newsletter: AIEWF Daily Dispatch — Latent Space)

- **Pipeline**: newsletter-wiki-ingest (recovered from triage checkpoint after newsletter-triage JSON parse failure)
---
## [2026-07-02] Ornith-1.0 Official Release Page Import — Major Wiki Update

### Changes
- **raw/articles/deep-reinforce.com--ornith-1-0--official-release.md** — New: DeepReinforce official release page saved
- **concepts/ornith-self-scaffolding-llm.md** — Updated: Self-Improving Training Framework (2-stage RL loop, Reward Hacking Defense 3-layer defense, Pipeline-RL), detailed benchmark numbers (397B/35B/9B), References expanded
- **comparisons/self-scaffolding-approaches.md** — Updated: Ornith entry updated with self-improving training framework details

### Sources
- https://deep-reinforce.com/ornith_1_0.html

---

## [2026-07-02] Self-Scaffolding Approaches — RLM / Dynamic Workflows / Ornith Comparison Page Created

### Changes
- **comparisons/self-scaffolding-approaches.md** — New: Comprehensive comparison page for 3 self-scaffolding approaches (RLM, Dynamic Workflows, Ornith). Covers implementation layers, training, parallelism, and decision frameworks.
- **concepts/ornith-self-scaffolding-llm.md** — Updated: Added RLM/Dynamic Workflows related sections, expanded Related Pages
- **concepts/dynamic-workflows.md** — Updated: Added links to RLM, Ornith, comparison page in Related Concepts
- **concepts/rlm-recursive-language-models.md** — Updated: Added links to Ornith, comparison page in Related Concepts
- **index.md** — Updated: Added comparisons/self-scaffolding-approaches

### Sources
- Simon Willison: https://simonwillison.net/2026/Jun/29/ornith/
- RLM: arXiv:2512.24601, Alex Zhang clarification (May 2026)
- Dynamic Workflows: Anthropic blog (June 2026)

---

## [2026-07-02] Pioneer AI & GLiNER Model Family — New Entity & Concept Pages Created

### Changes
- **entities/fastino-labs.md** — New: Fastino Labs company page — SLM applied research lab; Pioneer platform, GLiNER model family
- **entities/pioneer-ai.md** — New: Pioneer AI product page — SLM fine-tuning & inference agent; Agent Mode, Research Mode, Adaptive Inference; AdaptFT-Bench
- **concepts/gliner-model-family.md** — New: GLiNER model family concept — GLiNER→GLiNER2→GLiGuard→GLiNER2-PII; bidirectional encoder architecture; 42 PII types; OpenAI Privacy Filter comparison
- **raw/articles/pioneer-ai-blog-*.md** — New: 6 Pioneer AI blog articles saved as raw
- **SCHEMA.md** — Tags added: `encoder-model`, `small-language-model`, `named-entity-recognition`, `pii-detection`

### Sources
- https://pioneer.ai/blog/introducing-pioneer
- https://pioneer.ai/blog/behind-pioneer
- https://pioneer.ai/blog/gliner-modern-named-entity-recognition
- https://pioneer.ai/blog/gliner2
- https://pioneer.ai/blog/gliguard-16x-faster-safety-moderation-with-a-small-language-model
- https://pioneer.ai/blog/gliner2-pii-open-source-privacy-filtering-with-pii-detection

---

## [2026-07-02] X Article ingest — OpenWiki by Brace Sproul

### Changes
- **raw/articles/2026-07-01_bracesproul_openwiki-langchain.md** — New: X article "Introducing OpenWiki, an open source agent for repo documentation" by Brace Sproul (LangChain)
- **concepts/openwiki.md** — New: OpenWiki concept page — LangChain's open-source agent/CLI for codebase documentation wikis; wiki-as-context pattern, DeepAgents integration, GitHub Action for updates
- **entities/brace-sproul.md** — New: Brace Sproul entity page — Head of Applied AI at LangChain, led OpenWiki release
- **index.md** — Added brace-sproul entity + openwiki concept entries
- **log.md** — This entry

### Sources
- https://x.com/bracesproul/status/2072375136368660515 (X article, 394 bookmarks, 69.5K impressions)

---

## [2026-07-01] Dreaming wiki-ingest — 2 takes + 2 references enriched

### Changes
- **entities/fireworks-ai.md** — Added GLM 5.2 Fast section: 2-3x speed tier, agent loop optimization, 77.8% SWE-bench, $2.80/$0.28/$8.80 pricing
- **entities/glean.md** — Added Independent Agents section: 4 characteristics (Identity, Memory, Proactivity, Accountability), OnCall Assistant
- **entities/harvey.md** — Added Model Partnerships section: Claude Sonnet 5 integration, 5.8% LAB, 91.3% BigLaw Bench
- **entities/elevenlabs.md** — Added Procedures in ElevenAgents section: Structured/Free-form procedures, SOP import, Alpha
- Coverage verification: 3 takes (Mythos export, Voyage Context-4, Modal Auto Endpoints) already covered by existing pages — skipped

---
## [2026-07-01] wiki-health | Auto-fix: 14 orphan concept pages added to index.md

### Changes
- Added 14 orphan concept pages to wiki/index.md:
  - agent-harnesses, agentic-rag, ai-alignment, chain-of-thought
  - cpu-inference-llm, deep-research, durable-execution
  - kv-cache, llm-security, model-context-protocol-mcp
  - prompt-caching, rag-systems, sandbox
  - speculative-decoding, test-time-scaling
- Index validation passed (229 lines, 0 issues)
- Total indexed entries: 219 (up from 205)

---

---
## [2026-07-01 11:15] — Active crawl — 4 new pages + 1 enrichment

**Discovery:** Parallel subagent trend scan (HN Algolia + X/Twitter + wiki gap analysis)

### New pages created (4):
- `concepts/claude-code/steganographic-watermarking.md` — Claude Code Steganographic Request Watermarking: Anthropic's anti-distillation/anti-reseller measure using regex-based steganographic fingerprinting in API requests (2100 HN pts, Jun 30)
- `concepts/claude-science.md` — Claude Science: Anthropic's AI workbench for life sciences; reproducible computational biology with native visualization, compute management, and Modal GPU integration (503 HN pts, Jun 30)
- `concepts/edge-ai.md` — Edge AI (On-Device AI Inference): Running AI inference locally on devices via NPU accelerators; Apple Intelligence (WWDC 2026), Gemini Nano, llama.cpp; confirmed wiki coverage gap (170 lines)
- `concepts/together-ai-icml-2026.md` — Together AI at ICML 2026: 9 papers across full AI stack — DSGym (data-science agent eval/training), ThunderAgent (1.5–3.6× agent throughput), TTT-Discover, RARO (25% vs 5.9% SFT win rate)

### Existing pages enriched (1):
- `concepts/token-economics.md` — Added "The Economy of Tokens — A New Economic Paradigm" section: tokens as currency framework (supply/demand/velocity), pricing optimization strategies, market structure, and industry implications; based on @vipulved (Vipul Ved Prakash, Together AI CEO) X article (1004 bookmarks, Jun 2026)

### Raw articles saved (4):
- `raw/articles/2026-06-30_claude-code-steganographic-watermarking.md` — HN discussion (thereallo.dev blocked)
- `raw/articles/2026-06-30_claude-science-product.md` — Claude Science product page + Modal integration blog
- `raw/articles/2026-06-09_apple-intelligence-edge-ai.md` — Apple Intelligence WWDC 2026 announcement
- `raw/articles/2026-06-30_together-ai-icml-2026.md` — Together AI ICML 2026 blog post

### Coverage gap filled:
- **Edge AI** was the top wiki gap (completely missing) identified by the gap analysis subagent. Now filled with comprehensive coverage of hardware, software, model optimization, deployments, and use cases.

---
## [2026-07-01 07:45] — Blog wiki-ingest — 2 takes, 4 references from 19 blog candidates (recovered from triage checkpoint after JSON parse error)

**Source:** blog-triage checkpoint (saved before response render failure)

### New pages created (2):
- `entities/giles-thomas.md` — Giles Thomas; "Writing an LLM from scratch" series (part 34a), JAX/NNX/Optax training loop, outside-in methodology
- `entities/grant-sanderson.md` — Grant Sanderson (3Blue1Brown); skeleton entity, AI as leading indicator in mathematics, Dwarkesh Patel podcast

### Existing pages enriched (3):
- `entities/ed-zitron.md` — Added "June 2026: BIS Systemic Risk Warning" section: BIS annual report $1T+ hyperscaler capex warning, Oracle $129.5B debt/$38B lease/$260B future lease, Exponential View report critique, "The Four Losers" framing
- `entities/simon-willison.md` — Added June 30 entries: Claude Sonnet 5 tokenizer analysis (1.42× English, sampling params deprecated, 30% effective price increase, Adaptive Thinking default ON) and shot-scraper video feature (agent self-recorded demos via storyboard.yml/Playwright)
- `concepts/claude/fable-5.md` — Added Export Controls Lift (June 30, 2026) section: Commerce Department lifted restrictions on Fable 5/Mythos 5 after ~18-day suspension
---
## [2026-07-01 07:40] — Newsletter wiki-ingest — 4 takes, 3 references from 8 newsletters (recovered from triage checkpoint after JSON parse error)

**Source:** newsletter-triage checkpoint (saved before response render failure)

### New pages created (1):
- `concepts/claude/sonnet-5.md` — Claude Sonnet 5 (Jul 2026): most agentic Sonnet yet; new tokenizer (+30% tokens), adaptive thinking, 1M context, 128K output, $3/$15M pricing; Harvey LAB 5.8% all-pass, BigLaw Bench 91.3%

### Existing pages enriched (3):
- `concepts/token-economics.md` — Added "Enterprise TokenBudgeting (SemiAnalysis, June 2026)" section: enterprise budget ranges ($250-$10,000+/month), model downgrade strategies, M365 Copilot gaming, coding spend dominance, 50+ enterprise interviews, the tokenmaxxing→tokenbudgeting shift
- `concepts/local-llm/local-ai.md` — Added "AIEWF Workshop: Ahmad Osman on Local AI (June 2026)" section: Osmantic's hardware arena demo, open-source LLMs catching up to frontier (4-8 month lag), the "local AI is just running a model" misconception, 22× RTX 3090 setup, enterprise concerns (model routing, sandboxing, latency)
- `concepts/agentic-engineering.md` — Added "AIEWF 2026 Day 2: Loops, Software Factories & FDEs" section: swyx loop agenda, Allie Howe Software Factories, Microsoft Foundry learning loop, OpenAI Codex multi-agent loops, Peter Steinberger agent orchestration, Tereza Tížková software factory definition, Zach Lloyd "factory engineering," Natalie Meurer FDE evolution, Zixuan Li ZCode, MiniMax M3 release

### Reference items (3):
- **GPT-5.6 Preview** (Ben's Bites) — already covered by concepts/gpt/gpt-5-6.md
- **Sebastian Raschka Reasoning Book** — reference for concepts/inference-time-compute.md
- **FDE article** (AIEWF) — incorporated into agentic-engineering.md enrichment above

---



## [2026-06-30 11:15] — Active crawl — 4 new pages + 1 enriched

**Discovery:** Parallel subagent trend scan (HN Algolia + X/Twitter + wiki gap analysis)

### New pages created (4):
- `concepts/gpu-bubble-ai-inference.md` — GPU Bubble in AI inference: CPU-GPU round-trip idle cycles during autoregressive decode; Moondream Photon pipelined decoding (ping-pong slots, forward-now-sample-later, zombies) achieves up to 35% higher throughput on NVIDIA B200
- `concepts/wayfinder-router.md` — Wayfinder Router: deterministic, offline LLM query router; scores prompt structural complexity (0.0–1.0) without model calls; sub-millisecond routing decisions; PyPI package by @itsthelore
- `entities/moondream.md` — Moondream: VLM company building small vision-language models and the Photon inference engine; GPU bubble elimination research
- `entities/hp-inc.md` — HP Inc.: hardware company; launched OpenAI Frontier strategic partnership (June 2026) for enterprise AI deployment

### Existing pages enriched (1):
- `entities/openai.md` — Added HP Frontier Partnership section (June 2026): HP scaling OpenAI Frontier across customer experiences, software dev, and enterprise operations

### Raw articles saved (3):
- `raw/articles/2026-06-04_moondream_gpu-bubble.md` — Moondream "Popping the GPU Bubble" (Photon inference engine)
- `raw/articles/2026-06-25_wayfinder-router_deterministic-llm-routing.md` — Wayfinder Router GitHub README
- `raw/articles/2026-06-28_openai_hp-frontier-partnership.md` — OpenAI HP Frontier Partnership blog

### SCHEMA.md updated:
- Added `moondream`, `hp` to People/Orgs tag taxonomy


---
## [2026-06-30 07:50] — Blog wiki-ingest — Ornith-1.0, voyage-context-4, Cory Doctorow enriched

**Source:** blog-triage (recovered from checkpoint after JSON parse error)

### New pages created (1):
- `concepts/ornith-self-scaffolding-llm.md` — DeepReinforce Ornith-1.0: self-scaffolding LLMs for agentic coding; 4 variants (9B~397B) on Gemma 4/Qwen 3.5; MIT licensed; Simon Willison verified with LM Studio + Pi

### Existing pages enriched (3):
- `entities/voyage-ai.md` — Added voyage-context-4: MoE backbone contextualized chunk embeddings; auto-chunking; no 32K limit; $0.12/1M tokens; 2.08% chunk retrieval improvement
- `entities/cory-doctorow.md` — Added "Google Search Enshittification → Gemini" section: Google's intentional search degradation, Jedi Blue collusion, Gresham's Law of the web, parasitic AI summaries
- `entities/john-d-cook-applied-mathematics-consulting.md` — Added "LLM Output Verification: Grok vs Man Page" section: empirical LLM verification methodology, Grok correct despite man page bug

---
## [2026-06-30 07:40] — Newsletter wiki-ingest — 8 takes, 3 references from 4 newsletters

**Source checkpoint:** newsletter-triage (recovered from checkpoint after JSON parse error)
**Newsletters processed:** AINews (swyx), How I AI (Lenny Rachitsky), Import AI #463, Monday Template (skip)

### New pages created (3):
- `concepts/brain2qwerty.md` — Meta Brain2Qwerty v2 non-invasive brain-to-text decoder; ~61% accuracy; Auto Research coding-agent workflow
- `entities/meituan-longcat.md` — Meituan LongCat 2.0 / Owl Alpha; 1.6T/48B MoE, 1M context, trained on 50k domestic accelerators; first near-frontier model on fully domestic Chinese hardware
- `concepts/snowflake-arctic-rl.md` — Snowflake Arctic RL; VeRL+SkyRL; ZoRRo 6x actor-update acceleration; 36h Text2SQL training beats Gemini 3.1 Pro

### Existing pages enriched (5 takes):
- `entities/fernando-borretti.md` — Added "AI and the Permanent Underclass" section: structural inevitability of human disempowerment, three-strata society (AI base, permanent overclass, permanent underclass)
- `entities/glm-5-zai.md` — Added Claire's hands-on review: 45-min autonomous bug triage, $3.36/6M tokens, TypeScript/React weakness under agentic pressure
- `concepts/coding-agents/coding-agents.md` — Added Gusto Cofounder case study: 5-person team, 10 weeks, zero PM/Jira/docs, Claude Code as primary contributor
- `entities/deepseek.md` — Added DSpark speculative decoding: 30.9% higher accepted length vs Eagle3, deployed in V4-Flash/V4-Pro
- `entities/arena-ai.md` — Added $100M ARR in 8 months, 700M+ conversations, 82M+ votes, 10M+ monthly visitors, agent-mode CI/CD

### Reference enrichments (3):
- `entities/tencent.md` — Added ARGUS GPU cluster telemetry (10k GPU tracing)
- `entities/cursor-ai.md` — Added Cursor for iOS (always-on cloud agents, PR diff notifications)
- `concepts/nemotron-3-ultra.md` — Added Nemotron-TwoTower (98.7% AR quality, 2.42x throughput) + vLLM multi-node inference guide


---
## [2026-06-30 12:00] — New concept page: Brain2Qwerty v2 (Meta)

**New wiki page:**
- `concepts/brain2qwerty.md` — Meta Brain2Qwerty v2 non-invasive EEG-based brain-to-text decoder; ~61% accuracy; Auto Research coding-agent workflow improved word error rate

**Source:** raw/newsletters/2026-06-30-ainews-not-much-happened-today.md (triage decision: new concept)

---
## [2026-06-29 22:30] — X accounts scan — 4 raw articles + 3 wiki pages from 8 posts

**Scan summary**: 84 tracked accounts, 12 scanned, 8 new substantive posts from 4 accounts (simonw, tomaarsen, emollick, ashpreetbedi).

**Raw articles saved**:
- `raw/articles/2026-06-26_openai_gpt-5-6-sol-preview.md` — OpenAI GPT-5.6 Sol preview (simonw tweet)
- `raw/articles/2026-06-18_liquid_lfm2-5-retrievers.md` — Liquid AI LFM2.5 Retrievers blog post (tomaarsen tweets)
- `raw/articles/2026-06-29_artificial-analysis_aa-briefcase-benchmark.md` — AA-Briefcase agentic knowledge work benchmark (emollick tweet)
- `raw/articles/2026-06-29_agno_welcome-docs.md` — Agno agent platform documentation (ashpreetbedi tweets)

**New wiki pages**:
- `entities/liquid-ai-lfm2-5-retrievers.md` — LFM2.5-ColBERT-350M / LFM2.5-Embedding-350M multilingual retrieval models
- `concepts/ai-benchmarks/aa-briefcase.md` — AA-Briefcase: agentic knowledge work benchmark by Artificial Analysis
- `entities/agno.md` — Agno: open-source agent platform SDK and AgentOS runtime

**Already existed/not duplicated**:
- `events/2026-06-27-openai-gpt-5-6-sol` — GPT-5.6 Sol event already exists
- `concepts/gpt/gpt-5-6` — GPT-5.6 concept page already exists
- `concepts/claude/mythos` — Claude Mythos concept page already exists

**Not ingested (paywall/no access)**:
- WSJ: "China Has Matched Anthropic in Cybersecurity" (emollick tweet) — paywalled, 51-byte JS-block page
- Agno Demo AgentOS (ashpreetbedi tweet) — demo link, no substantive content to scrape

---
## [2026-06-29 18:20] — dreaming: consolidation — 1 enrichment

**Enriched**:
- `entities/seangoedecke-com.md` — Added AI Inference Is Obviously Profitable section: A100 cost calculations ($1/M tokens at 400W), 70-80% gross margin analysis, DeepSeek 87¢/M tokens comparison, rebuttal to VC-subsidy thesis. Bumped updated to 2026-06-29.

**Skipped/reference (pipeline saturation)**: RLVR Generalization (Dwarkesh: 222-line entity covers fully), GPT-5.6/Mythos (events + concepts pages), AI Bubble (GM 310-line Fizzle section, Zitron 528-line Cargo Culture), DeepSpec/DSpark (active-crawl created concept), Prompt Injection (concept page has 80+ line Role Confusion section), jax-js (below threshold), AI Liability (110-line concept page), Non-AI batch (17 articles).

**Summary**: 9 themes / 27 articles from fallback file. 1 genuine gap identified and enriched.



---


## [2026-06-29] Watchdog auto-fix

### Auto-fixed
- **Log.md**: Added 8 missing `---` section separators between consecutive `## [DATE]` entries (June 28-29 entries)

### Verified (index.md — Format B)
- **Pipe corruption**: 0 instances
- **Line prefix corruption**: 0 instances
- **Triple brackets**: 0 instances
- **Space prefix**: 0 instances
- **Duplicate entries**: 0 instances
- **Ghost entries**: 0 instances
- **Cross-section misplacement**: 0 instances

### Pipeline Watchdog
- **x_accounts**: Stale (26h) — known pattern, reported for monitoring
- **wiki-health-report**: OK — total_l2=2722, entities=839, concepts=1851
- **wiki-graph-analysis**: 74.4h old — stale, not acted upon

---

## [2026-06-29] — active-crawl | 3 new concept pages

**Sources**: HN Algolia + X/Twitter trending + blogwatcher DB gap analysis (June 29, 2026)
**Topics**: Mixture of Agents (arXiv papers), Model Training as Code (Aleph Alpha blog), CPU Inference for LLMs (compiled research)

### [[concepts/cpu-inference-llm]]
**Action**: Created concept page `concepts/cpu-inference-llm.md`
**Source**: Research compilation from llama.cpp README, ZSE project, HN discussions
**Tags**: cpu-inference, inference, quantization, local-llm, hardware
**Coverage gap**: wiki had 0 pages on CPU-specific LLM inference despite 15 GPU inference pages

### [[concepts/mixture-of-agents]]
**Action**: Created concept page `concepts/mixture-of-agents.md`
**Source**: arXiv:2409.07487 (MoA is All You Need, 2024) + arXiv:2605.29116 (Beyond Consensus, 2026)
**Tags**: mixture-of-agents, multi-agent, agents, llm, model, ensemble
**Coverage gap**: No prior MoA coverage despite mixture-of-experts being well-documented

### [[concepts/model-training-as-code]]
**Action**: Created concept page `concepts/model-training-as-code.md`
**Source**: https://aleph-alpha.com/en/blog/model-training-as-code/ (165 HN pts, June 2026)
**Tags**: model-training-as-code, training, mlops, workflow, experiment-tracking
**Coverage gap**: MTaC paradigm not documented despite strong HN signal

**Raw articles created**: 2024-09-04_2409.07487_mixture-of-agents.md, 2026-05-27_2605.29116_beyond-consensus-moa.md, 2026-05-22_aleph-alpha_model-training-as-code.md, 2026-06-29_cpu-inference-llm-trend.md
**SCHEMA.md tags added**: mixture-of-agents, model-training-as-code, flyte, weights-and-biases, cpu-inference
---
## [2026-06-29] llm-pricing-monitor — pricing correction

Live pricing fetch from all 4 providers (OpenAI, Anthropic, Google, DeepSeek). 1 change detected:

- **comparisons/llm-api-pricing.md** — Corrected Gemini 3.1 Flash Lite output: $0.50 → $1.50/M (Global). The 06-22 changelog had erroneously "corrected" this from $1.50 to $0.50; live Vertex AI page confirms $1.50/M. Added cached input $0.025/M. Added to cache pricing table. Removed incorrect Google reference from 06-22 changelog.

All other provider prices verified unchanged:
- OpenAI: GPT-5.5 ($5/$30), GPT-5.4 ($2.50/$15), GPT-5.4-mini ($0.75/$4.50), GPT-5.4-nano ($0.20/$1.25) ✅
- Anthropic: Opus 4.8 ($5/$25), Sonnet 4.6 ($3/$15), Haiku 4.5 ($1/$5), Fable 5 ($10/$50) ✅
- Google: 3.1 Pro ($2/$12), 3.5 Flash ($1.50/$9), 3 Flash Preview ($0.50/$3) ✅
- DeepSeek: V4-Flash ($0.14/$0.28), V4-Pro ($0.435/$0.87) ✅

---
## [2026-06-29] blog-wiki-ingest — blog triage enrichment (Case C2 recovery)

Blog-triage output parse failed but checkpoint valid (today's date). No take decisions. Processed 2 reference enrichments:

- **entities/simon-willison.md** — Added "Jon Udell on Agent in the Loop" (Jun 28, 2026) entry to June 2026 Updates. Philosophical reframing of "human in the loop" → "agent in the loop" complements Simon's agentic engineering philosophy.
- **entities/jim-nielsen.md** — Added "Intelligence Is Not Enough" Core Ideas section. Bryan Cantrill's Oxide talk on human values (resilience, teamwork, rigor, optimism) being irreplaceable in solving company-destroying bugs. Reinforces Jim's "People Are Not Friction" thesis.

Skipped: 9 non-AI or already-covered articles (security breach, Om Malik tributes, LLVM optimization, book review, etc.). Archived via archive_triage.py.

---
## [2026-06-29] Newsletter Wiki Ingest — Poolside and Open-Source AI Strategy

**Source**: Interconnects / Robotic (Nathan Lambert) — "Latest open artifacts (#22): Zyphra, Cohere, and Poolside are expanding the breadth of the ecosystem"

**Updated**:
- `entities/poolside.md` — Laguna M.1 license corrected from "Proprietary (API preview)" to "Apache 2.0"; added Poolside's public commitment to open releases ("Open weights are now our default."); updated frontmatter date and sources
- `concepts/open-source-ai.md` — Added "Open Model Makers Ecosystem (June 2026)" section with Nathan Lambert's 3-category framework (Pure Model Makers, Big Tech, Product Companies); updated frontmatter date and sources

**Index updates**:
- Added `[[entities/poolside]]` entry to Entities section
- Added `[[concepts/open-source-ai]]` entry to Concepts section

**Analysis**: The triage checkpoint was valid (Case C — cron output parse failed but checkpoint JSON intact). 2 take decisions processed (poolside license update + open model makers framework enrichment). 1 reference decision (open model categories) also executed as enrichment. All other items correctly skipped (already covered by existing pages or non-AI content).
---
## [2026-06-29] Lambda MicroVMs vs AgentCore — Comparison Page

**Created**: `comparisons/lambda-microvms-vs-agentcore.md` — Comparison analysis of AWS Lambda MicroVMs and Amazon Bedrock AgentCore. Organized as different stack layers (isolation primitives vs managed platform), analyzing architectural positioning, usage conditions, and competitive landscape.

**Updated**:
- `concepts/aws-lambda-microvms.md` — Added link to comparison page
- `entities/amazon-bedrock-agentcore.md` — Added link to comparison page
- `index.md` — Added comparison page to Comparisons section

---
## [2026-06-29] AWS Lambda MicroVMs — Wiki Ingestion

**Source**: AWS News Blog (2026-06-22) — "Run isolated sandboxes with full lifecycle control: AWS Lambda introduces MicroVMs"

**Created**:
- `raw/articles/2026-06-22_aws-lambda-microvms-announcement.md` — raw article
- `concepts/aws-lambda-microvms.md` — full concept page; Firecracker-based serverless sandbox primitive for isolated/stateful execution; 3 core capabilities (VM isolation, rapid launch/resume, stateful execution), comparison table with Lambda Functions, Agent Sandbox ecosystem positioning, workflow diagram

**Enriched**:
- `concepts/firecracker.md` — added 2026-06-22 history entry for Lambda MicroVMs launch, added wikilink to related pages
- `entities/amazon-bedrock-agentcore.md` — added Lambda MicroVMs to related pages (low-level sandbox primitive complement to AgentCore Code Interpreter)
- `concepts/sandbox.md` — added Lambda MicroVMs product page to sources
- `index.md` — added concepts/aws-lambda-microvms entry

**Analysis**: Lambda MicroVMs vs AgentCore — see concept page for detailed comparison table

---
## [2026-06-28] X Bookmarks Ingest — Vercel Eve Framework

**Source**: X Article (June 27, 2026) — "Building Agents with Vercel's Eve Framework"

**Created**:
- `entities/vercel-eve.md` — Vercel Eve: Open-source filesystem-first agent framework (Apache 2.0). Core idea: agent = directory of files. Tools, skills, subagents, evals, connections, and channels auto-discovered by name. Built-in durable sessions (Vercel Workflows), sandbox isolation, HITL, MCP connections, Slack/Discord channels. Vercel runs 100+ Eve agents in production (d0: 30K questions/month, Vertex: 92% ticket resolution, Athena: 6-week build with no engineers). GitHub: 2,857 ★, 214 forks, 116 open issues.

**Enriched**:
- `entities/vercel.md` — Added Eve: Filesystem-First Agent Framework section, updated AI Ecosystem Role with Eve, added Eve to related/sources, bumped updated date to 2026-06-28

**Index**:
- Added entities/vercel, entities/vercel-eve, entities/vercel-sandbox to index.md (all were missing — wiki drift correction)

**Raw article**: [[raw/articles/2026-06-27_vercel-building-agents-with-eve-framework.md]]

---
## [2026-06-28 18:20] — dreaming: consolidation — 2 takes, 4 reference enrichments

### Duplicate Check
- Pipeline saturation: blog-triage Takes=0, newsletter-triage Takes=0, active-crawl 4 pages created
- 222 raw articles → 82 unprocessed → 2 takes, 7 references, rest skip
- No same-day dreaming commit found (Case C2 — triage produced decisions only)

### Takes (2)
1. **concepts/dark-factory-software-factory.md** — Added Warp Factory Engineering section (92 lines): Zach Lloyd's memo redefining engineers as "factory engineers", Factory Efficiency metric = shipped product / (inference cost + human time cost), meta-engineering concept, Oz platform, automation-first mandate, self-improvement agents, recursive self-improvement goal. Includes Key Paradigm Shift comparison table (Product Engineering → Factory Engineering) and Relationship to Other Approaches (StrongDM, sairahul1, Factory.ai, Warp).
2. **concepts/open-source-vs-closed.md** — Rewrote 24-line stub to 77-line comprehensive concept page: Doubleword benchmark-by-benchmark analysis across 18 benchmarks, Dec 3 2026 convergence prediction, coding gap at 1-2 months, overall ~5 months flat, interpretation challenges section, HN 299pt reception.

### Reference Enrichments (4)
3. **concepts/anthropic/dod-dispute.md** — Added NSA Mythos access loss event (June 23 NYT): classified contract for intelligence analysis failed to finalize (HN 248pt).
4. **concepts/codex/codex-knowledge-work.md** — Added OpenAI Internal Adoption Trajectory subsection: <10% Codex tokens (Aug 2025) → full deployment across every department including Legal/Recruiting (Jun 2026).
5. **concepts/ai-and-authenticity.md** — Added AI Companion Dependency section: OpenAI/MIT Media Lab RCT (~1000 participants, 4 weeks) — heaviest users loneliest and most emotionally dependent.
6. **concepts/agent-skills.md** — Added Warp Self-Improvement Loop subsection: context window scaling problem, composable executable skills, Execute→Evaluate→Revise loop.

### Skipped References (already covered)
- Sakana Fugu — Already in entities/sakana-ai.md (Fugu section)
- MCPorter — Has dedicated concepts/mcporter.md page
- Gemini Android — Already in concepts/gemini-computer-use.md
- Warp Skills (old ref on line 113) — Expanded, not skipped

### Batch Skips
- Marketing (Decagon, Harvey, Hex, Glean, Cohere) — 13 articles
- Non-AI (Tedium, vintage computing, math, music, general tech) — 10+ articles
- Already processed (Fable 5 newsletter, active-crawl OpenKnowledge/Self-Harness/Cursor) — 6 articles
- ElevenLabs product docs (7 articles)
- Sitemap non-substantive (shkspr.mobi, MacRumors, Seán Goedecke, Xbox)
- Other low-value (CVE, events, Maven, HN acquisitions)

### Archive
- Skip/Reference items archived via archive_triage.py

---
## [2026-06-28] health-fix | Auto-fix orphan pages in index.md

### Changes
- Added 9 orphan concept pages to index.md: after-automation, ag2-autogen, agent-account-provisioning, agent-communication-standards, agent-distillation, agent-driven-ranker-optimization, agent-economics, agent-first-design, agent-harness-primitives
- Added 9 orphan comparison pages to index.md: llm-api-pricing, llm-integration-patterns, local-llm-models-april-2026, open-harness-vs-agent-framework, open-source-rl-libraries-comparison, openai-vs-sierra-agent-simulation, openclaw-pi-hermes-state-management, palantir-platform-family, palantir-vs-competitors
- Skipped: concepts/_index (_index.md), concepts/agent-memory (redirect stub), concepts/agent-documentation (empty stub <300B), concepts/agent-first-codebase-design (empty stub <300B)
- No index corruption detected (0 pipe, 0 line-number, 0 triple-bracket issues)

### Validation
- validate_index.py: clean (181 lines)
- All section headers intact
- All 18 entries verified present
- Fixed comparison section alphabetical ordering (31 entries resorted)

---## [2026-06-28 11:03] — Active Crawl: 4 new wiki pages from trending topics

### Discovery
- HN Algolia: 630 stories scanned, 15 AI-relevant, cross-referenced against wiki
- X/Twitter (xurl): 58 tweets scanned across 6 queries, 10 substantive results
- Blogwatcher DB: 100+ articles from 30 blogs in last 3 days
- Wiki gap analysis: checked 1,322 concepts + 829 entities across 10 key areas

### Selected Topics
1. **entities/openknowledge.md** — OpenKnowledge, open-source AI-native markdown editor (373 HN pts, GitHub README)
2. **concepts/self-harness.md** — Self-Harness paradigm from Shanghai AI Lab (arXiv:2606.09498, Terminal-Bench-2.0 improvements)
3. **concepts/ai-executive-orders.md** — U.S. AI executive orders and government gatekeeping of frontier models
4. **concepts/open-weight-vs-closed-llm-gap.md** — Open-weight vs closed LLM performance gap analysis (Doubleword, 299 HN pts)

### Raw Articles Saved
- raw/articles/2026-06-28_active-crawl-trending-topics-research.md (research note)
- raw/articles/2026-06-28_inkeep-openknowledge-ai-knowledge-tool.md
- raw/articles/2026-06-08_arxiv-2606.09498_self-harness.md
- raw/articles/2026-06-22_doubleword-open-source-vs-closed-llm-gap.md

### Key Content
- **OpenKnowledge**: GPL-3.0 licensed, macOS + web UI, native Claude/Codex/Cursor integration, MCP-first architecture, git-native sync
- **Self-Harness**: 3-stage loop (Weakness Mining → Harness Proposal → Proposal Validation), +14-21pp across MiniMax/Qwen/GLM on Terminal-Bench-2.0
- **AI Executive Orders**: Timeline from Biden 2023 EO through Trump 2025 rescind to current government gatekeeping (GPT-5.6 and Mythos restricted access)
- **Open-weight gap**: Single-benchmark projection shows Dec 2026 convergence; multi-benchmark average shows persistent ~5-month gap

### Statistics
- 8 files staged for commit: 4 wiki pages + 3 raw articles + index.md + log.md


---
## [2026-06-28 07:22] — Newsletter Triage (Recovery): Super Intel Fable 5, all skip

### Triage Summary
- **Source**: Super Intel (Kim Isenberg)
- **Newsletter**: "The Fable 5 Kill-Switch, Two Weeks On"
- **Decisions**: 6 items, all skip (Takes=0)
- **Outcome**: Main article content already captured in `concepts/claude/fable-5.md` (362 lines, updated 2026-06-28). Full raw article saved to `raw/newsletters/`. Remaining links: banner images, tracking pixels, beehiiv UI noise.
- **Recovery**: Newsletter-triage upstream failed response render; checkpoint JSON recovered per pipeline-recovery protocol.
- **Archive**: All items already in archive (dedup from prior pass).

---
## [2026-06-28 07:00] — Blog Ingest: 20 new articles, 15 saved, 2 wiki pages updated

### Collection Summary
- 20 blog articles collected from RSS feeds
- 15 saved as raw articles to `wiki/raw/articles/`
- 5 unsaved (paywalled: WSJ, FT, The Information, openai.com, Senate.gov)

### AI-Relevant Articles
- **Anthropic Mythos released to 100+ US institutions** (Semafor, via Daring Fireball) — Government lifts block on Claude Mythos 5; Commerce Secretary Lutnick cites "significant progress"; same-day as GPT-5.6 release
- **OpenAI GPT-5.6 blocked from broad release** (openai.com, via Daring Fireball) — paywalled, already tracked in `events/2026-06-27-openai-gpt-5-6-sol.md`
- **Grok content moderation controversy** (The Information, via Daring Fireball) — paywalled
- **Meta AI bet flops, layoffs** (Pluralistic) — Meta's giant AI bet described as a flop, leading to massive layoffs
- **Apple/Micron RAM shortage** (Tedium, Daring Fireball) — Apple faces RAM supply constraints, bipartisan opposition to Chinese chip purchases

### Wiki Updates
- Updated `concepts/claude/mythos.md` — added Government De-escalation section (Mythos 5 released to 100+ US institutions, June 27)
- Updated `events/2026-06-27-openai-gpt-5-6-sol.md` — added cross-reference to Anthropic de-escalation
- Updated `index.md` — Mythos entry updated with government de-escalation info

### Checkpoint
- `~/.hermes/cron/data/blog_ingest/latest.json` — ready for `blog-triage` at 07:30

---

## [2026-06-27 22:30] — X Accounts Scan: 12 new posts from 5 tracked accounts, 10 raw articles scraped, 8 wiki pages created

### Scanned
- 84 tracked accounts → 12 selected (budget limit) → 12 new posts found
- Contributors: Eric Zhang (@ekzhang1), Hugo Bowne-Anderson (@hugobowne), Peter Steinberger (@steipete), Boaz Barak (@boazbaraktcs), Jo Bergum (@jobergum)

### Raw Articles Saved (10)
- `raw/articles/2026-06-26_openclaw_mcporter-mcp-typescript-tool.md` — mcporter MCP TypeScript toolkit (4.7k★)
- `raw/articles/2026-03-31_hugobowne_top-questions-about-ai-assisted-software.md` — 10 Q&A on AI-assisted dev (Hugo + Eleanor Berger)
- `raw/articles/2026-01-05_hugobowne_how-to-build-ai-agent.md` — Building AI agents with AI-assisted coding
- `raw/articles/2026-06-23_hugobowne_show-us-your-agent-skills.md` — Show Us Your Agent Skills landing (22 guests, 51 skills)
- `raw/articles/2026-06-23_hugobowne_bryan-bischof-agent-skills.md` — Bryan Bischof's BBPlot agent skill
- `raw/articles/2026-06-26_noema_how-ai-will-change-us.md` — Noema essay by Houda Nait El Barj
- `raw/articles/2026-06-22_maven_elite-ai-assisted-coding.md` — Maven course by Eleanor Berger
- `raw/articles/2026-06-23_hugobowne_claude-code-8bit-video-skill.md` — YouTube: Claude Code 8-bit video skill demo
- `raw/articles/2026-06-29_luma_retrieval-for-agents-sf.md` — Luma event: Retrieval for Agents SF
- `raw/articles/2026-06-26_ekzhang_jax-js-web-ml-framework.md` — jax-js web ML framework (845★)

### Entity Pages Created (6)
- `entities/hugo-bowne-anderson.md` — AI educator, Vanishing Gradients host
- `entities/peter-steinberger.md` — PSPDFKit creator, MCP tooling explorer
- `entities/boaz-barak.md` — Harvard CS professor, AI safety
- `entities/jo-bergum.md` — Hornet CEO, vector search expert
- `entities/eric-zhang.md` — jax-js creator, web ML
- `entities/bryan-bischof.md` — Theory Ventures, BBPlot eval-driven charts

### Concept Pages Created (2)
- `concepts/mcporter.md` — MCP TypeScript runtime toolkit (4.7k★, 42 releases)
- `concepts/show-us-your-agent-skills.md` — YouTube series: 22 builders × 51 skills × 79 workflows

### Skipped
- Eric Zhang: graphon (Zig graph DB — non-AI), NY Systems Reading Group event (announcement), jax-js WASM matmul PR (merged into main project page), jax-js Whisper demo (merged into main project page)

---
## [2026-06-27 22:34] — Raw article scrape: Noema Magazine "How AI Will Change Us"
### Added
- **raw/articles/2026-06-26_noema_how-ai-will-change-us.md** — Houda Nait El Barj (OpenAI researcher). Key thesis: as AI becomes the most patient, emotionally responsive conversationalist always available, what humans need shifts from information to presence, embodiment, and participation in shared vulnerability. Covers AI companionship, interpretation vs participation, meaning-on-demand risks. 16.5K chars.
---
## [2026-06-27] — Dreaming wiki ingest: 6 enrichments (Takes=0, pipeline saturation)
### Enriched
- **[[entities/cohere]]** — Added AI Agent Fork Maintenance section: control theory framework for vLLM fork management (5 open-sourced skills, cohere-ai/vllm-skills), upstream absorption compressed weeks→days. Added Security Agent with North & Wiz section: 8 MCP tools, toxic combination analysis (20s vs half morning), autonomous weekly posture brief. Sources: cohere.com/blog Jun 26.
- **[[entities/warp-terminal]]** — Added Factory Engineering Shift section: Zach Lloyd internal memo declaring shift from product engineering to cloud software factory, COGS vs R&D framing, automation mandate, recursive self-improvement goal. Source: warp.dev/blog Jun 18.
- **[[entities/fireworks-ai]]** — Added Cursor Composer 2 Partnership section: Fireworks provides distributed RL inference infrastructure (3-4 global clusters) for Cursor's Composer 2 (Kimi 2.5-based), 6-10x lower inference cost. Source: fireworks.ai/blog Jun 26.
- **[[concepts/open-source-ai-must-win]]** — Added Anil Dash Platform War Strategy section: 4-tactic playbook (disintermediate, model switching, commoditize open weights, channel anger) complementing the manifesto. Source: anildash.com Jun 23.
- **[[entities/glean]]** — Added No-Code Automation Guide section: Trever Gile's comprehensive guide, Agent Builder position for business user AI workflows. Source: glean.com/blog Jun 22.
### Notes
- 2 verified-false enrichment gaps skipped: entities/modal-labs.md (speculative decoding already covered), entities/cloudflare.md (temporary accounts already covered)
- Triage checkpoint recovered from file (upstream failing-group agent failed JSON render, saved checkpoint before response failure)
---
## [2026-06-27] — Active crawl: 4 new pages (Qualcomm-Modular, DeepSpec, CVE-2026-55607, Modular entity)

### Created
- **[[events/2026-06-24-qualcomm-acquires-modular]]** — Qualcomm acquires Modular (~$4B); chipmaker consolidates AI software stack; implications for Mojo language and MAX platform. Source: HN discussion (238 pts, 125 comments) on Reuters report.
- **[[entities/modular]]** — Modular — AI infrastructure startup co-founded by Chris Lattner (LLVM, Swift, MLIR) and Tim Davis; Mojo programming language, MAX AI platform; acquired by Qualcomm June 2026.
- **[[concepts/deepspec-dspark]]** — DeepSpec & DSpark — DeepSeek open-source speculative decoding inference framework; DSpark distributed engine, 60–85% faster generation, MIT license. Source: HN discussion (254 pts) on deepseek-ai/DeepSpec GitHub.
- **[[concepts/cve-2026-55607-claude-code-sandbox-escape]]** — CVE-2026-55607 — Claude Code sandbox escape via .git worktree naming, symlink manipulation, git fsmonitor execution rewrites; disclosed by Prasenjit Sarkar (@stretchcloud) June 26. Source: X/Twitter thread.
- **[[wiki/raw/articles/2026-06-24_hn-discussion_qualcomm-acquires-modular]]** — Raw article (69 lines, HN discussion highlights)
- **[[wiki/raw/articles/2026-06-26_hn-discussion_deepseek-deepspec-inference-optimizations]]** — Raw article (133 lines, HN discussion + GitHub README)
- **[[wiki/raw/articles/2026-06-26_x-stretchcloud_cve-2026-55607-claude-code-sandbox-escape]]** — Raw article (23 lines, X/Twitter disclosure)

### Updated
- **[[index]]** — Added 4 entries across Concepts (+2), Entities (+1), Events (+1) sections.

### Scan stats
- HN Algolia: 147 stories scanned (June 23–27), 15 AI-relevant; 145 pre-existing pages filtered; 3 true gaps selected
- X/Twitter (xurl): 10 substantive results from 5 queries; filtering removed promotional/non-English content
- Blogwatcher DB: 24 AI-relevant articles in last 3 days (50 total); most already triaged by blog-wiki-ingest
- Topics skipped (already covered): GPT-5.6 Sol, Mythos, GLM-5.2, Claude Tag, Gemini 3.5 Flash CU, OpenAI Daybreak, OpenAI Jalapeño, agentic engineering/harness patterns

---
## [2026-06-27] — Blog wiki ingest: 5 enrichments
### Enriched
- **[[concepts/ai-economics]]** — Added Inference Economics section: A100 cost breakdown ($1/MTok), 70-80% gross margins, DeepSeek validation, inference-subsidizes-training thesis. Source: Sean Goedecke (seangoedecke.com) Jun 26.
- **[[concepts/gpt/gpt-5-6]]** — Added Prompt Caching features: explicit cache breakpoints, 30-min minimum cache life, 1.25x cache write billing, 90% cache read discount. Source: OpenAI via Simon Willison Jun 26.
- **[[concepts/claude/fable-5]]** — Added Economic Recoupment Impact (Dean W. Ball): narrow post-release recoupment window, $100B+ datacenter buildout vs 100-company market. Source: Simon Willison quoting Dean W. Ball Jun 26.
- **[[entities/simon-willison]]** — Added hackmyclaw.com Prompt Injection Challenge: Fernando Irarrázaval's 6,000-attempt challenge, 0 injection successes, Opus 4.6 Anti-Prompt-Injection Rules. Source: simonwillison.net Jun 26.
- **[[concepts/continual-learning]]** — Added Advanced Frameworks (Dwarkesh Patel): RLVR generalization limits (Dario Amodei short→long horizon gap), OPSD (On-Policy Self-Distillation), Dreaming as 4th scaling axis, KV cache vs weight density (35M×), 2027 vision. Source: dwarkesh.com Jun 26.
- **[[entities/dwarkesh-patel]]** — Added "The next big breakthrough" to career timeline and blog posts: RLVR limits, OPSD, dreaming, computer use grindability. Source: dwarkesh.com Jun 26.

---
## [2026-06-27] — Newsletter wiki ingest: GPT-5.6 pages + entity enrichment

### Created
- **[[concepts/gpt/gpt-5-6]]** — GPT-5.6 (Sol/Terra/Luna) — OpenAI's three-model family. First government-mediated restricted preview (~20 trusted partners). Key specs: Sol Ultra 91.9% Terminal-Bench 2.1, $5/$30 per 1M tokens; Terra $2.50/$15; Luna $1/$6. METR evaluation: highest cheating rate detected, 11.3h 50%-horizon (cheating-adjusted). Cerebras launch via @scaling01 (July, 750 tokens/sec). Sources: AINews Jun 27.
- **[[events/2026-06-27-openai-gpt-5-6-sol]]** — Event page for the GPT-5.6 Sol restricted preview. First U.S. government-mediated frontier model release. Sources: AINews, Superintel (beehiiv 403-expired).

### Enriched
- **[[entities/dean-ball]]** — Added "What Should Be Done (Jun 2026)" section: EO as de facto licensing, administration knowledge gap, default denial pattern, IVO proposal for frontier labs, Obernolte-Trahan Great American AI Act endorsement. Source: Hyperdimensional Jun 26.
- **[[entities/alex-banks]]** — Added "You're Underestimating AI on Purpose (Jun 2026)" — AI Perception Paradox, Amara's Law, systematic underestimation of AI progress. Source: The Signal Jun 26.


---
## [2026-06-26] — Active Crawl: 3 new concept pages + 1 entity enrichment

### Created
- **[[concepts/ai-gateway]]** — AI Gateway concept (LLM API routing, cost control, governance). Sources: LangChain LLM Gateway, Glean MCP Gateway. Triggers: HN 287pts (OpenKnowledge), Merge Blog, wiki gap analysis.
- **[[concepts/agent-integration-platforms]]** — Agent Integration Platforms (Nango, Composio, Arcade). Emerging "Zapier for AI agents" subsector. Sources: Merge Blog composio-vs-arcade, composio-alternatives.
- **[[concepts/llm-cost-crisis]]** — LLM Cost Crisis / Tokenpocalypse. Synthesizes HN cost crisis articles (89+pts), ties to token-economics and outcome-based pricing.

### Enriched
- **[[entities/deepseek]]** — Added $7.4B funding round (June 2026, WSJ), doubling staff, US enterprise adoption shift. 

### Ingested (Manual)
- **[[raw/articles/2026-06-24_lilianweng_scaling-laws-carefully]]** — Lilian Weng "Scaling Laws, Carefully" (Jun 2026). Comprehensive survey: Kaplan (2020) vs Chinchilla (2022) reconciliation, data-limited scaling (Muennighoff 2023, Lovelace 2026), practical fitting pitfalls (Besiroglu 2024).
- **[[concepts/scaling-laws]]** — New concept page synthesizing scaling law research history, formulations, and practical implications.
- **[[entities/lilian-weng]]** — New entity page for Lilian Weng (OpenAI researcher, Lil'Log author).

### Discovery
- HN Algolia: OpenAI Broadcom chip (810pts), Anthropic-Alibaba distillation (762pts), VibeThinker (395pts), Claude Code Extended Thinking (325pts), OpenAI DayBreak (220pts)
- X/Twitter: 30 Core Agentic Engineering Concepts (1570 bookmarks), Loop Engineering = Software Engineering (442 bookmarks), Kareem Carr on AI's uneven effectiveness
- Wiki gaps filled: AI Gateway (FULL), Agent Integration Platforms (FULL), LLM Cost Crisis (PARTIAL→NEW)

---
## [2026-06-26] Blog Wiki Ingest — Supplement Batch

- **Take**: Andrew Nesbitt "Incident Report: CVE-2026-LGTM" — satirical AI supply chain security gate failure piece. Added as new Core Ideas subsection to `entities/andrew-nesbitt.md` (+31 lines, 7-gate failure mapping, satire analysis). Added to `concepts/ai-supply-chain-security.md` as 5th case study (satirical stress test).
- **Reference**: Michal Zalewski "AI children's books, body horror edition" — purchased and inspected AI-generated Amazon bestseller encyclopedia. Enriched `entities/lcamtuf.md` with supplement paragraph, recent theme entry, and reference.
- **Skips**: 14 articles — non-AI topics (math, Windows internals, Apple pricing, Anubis-gated, unsaved_articles).
- **Archived**: 15 skip+reference items via archive_triage.py.

---
## [2026-06-26] Blog Ingest Triage — 2026-06-26

**Source:** blog-ingest pipeline (blogwatcher RSS scan)
**Articles scanned:** 32 new (20 shown)
**Articles saved:** 17 raw articles to wiki/raw/articles/

### Triage Decisions

**Takes (★★★★):**
- Gary Marcus "The Generative AI Fizzle™" → enriched `gary-marcus.md` — coined term for slow AI valuation decline, LLM commoditization validated, Chinese open-source threat, OpenAI $21B losses, AI stocks down for month
- Simon Willison "AI and Liability" → enriched `simon-willison.md` — linked Bruce Schneier on German ruling holding Google liable for AI overview errors

**References (★★★):**
- Andrew Nesbitt "Scrutineer" → enriched `simon-willison.md` + created `andrew-nesbitt.md` entity — LLM-powered open source security scanning for Alpha-Omega, addresses maintainer burnout bottleneck
- Cory Doctorow "Jailbreaking isn't theft" → skipped (primarily about digital sovereignty/copyright, minimal AI content)

**Skipped (★★):**
- 13 articles: math (johndcook.com × 3), Apple pricing (daringfireball.net), Windows internals (devblogs.microsoft.com × 2), ffmpeg color grading (jeffgeerling.com), VA Linux history (dfarq.homeip.net), subway engineering (construction-physics.com), Raymond Chen food take (devblogs.microsoft.com), Om Malik obituary (daringfireball.net), xeiaso.net bot-check page

### Pages Modified
- `entities/gary-marcus.md` — added "Generative AI Fizzle™" section + source
- `entities/simon-willison.md` — added AI liability + Scrutineer link blog entries + sources
- `entities/andrew-nesbitt.md` — NEW entity page (open source security researcher)
- `wiki/index.md` — added andrew-nesbitt entry

---
## [2026-06-25] OpenAI "How Agents Are Transforming Work" + Research Paper Ingestion

**Source**:
- Blog: https://openai.com/index/how-agents-are-transforming-work/ (June 25, 2026)
- Paper: https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf
- Authors: Drew Johnston, David Holtz, Alex Martin Richmond, Christopher Ong, Prasanna Tambe, Aaron Chatterji (OpenAI, Columbia, Wharton, Duke)

**Raw paper saved**: `raw/papers/2026-06-25_openai-shift-to-agentic-ai.md` (50-page research paper with 4 stylized facts, task taxonomy, job title classifier, 15 figures)

**Raw article saved**: `raw/articles/2026-06-25_openai-agents-transforming-work.md`

**New concept page**: [[concepts/agentic-knowledge-work]] — Agentic Knowledge Work paradigm shift. Enriched with paper's four stylized facts:
1. Rapid but uneven shift (Codex output share: Individual 16.5%, Org 63.3%, OpenAI 99.8%)
2. Delegated production, not consultation
3. Anchored in software, broader where adoption deepest
4. Large, repeatable, parallel workflows (3+ concurrent agents, 26.6% skill use)

Key data: 80.6% users >30min tasks, non-developer growth 137×/189×, every department majority Codex by Apr 2026, median researcher output 50× higher.

**Updated**:
- [[entities/openai-codex]] — Added paper + article source references + concept link
- `index.md` — Added agentic-knowledge-work concept entry

---

## [2026-06-25] X Bookmarks Ingest — Codex Agent Development Methodology

**Bookmark batch**: 1 bookmark processed

**Enriched**:
- [[entities/openai-codex]] — Added "Agent Development Methodology — Production Agent Workflow" section based on @gengdaJ's June 23 Note Tweet. Documents a structured five-phase development cycle (Product Alignment -> Decomposition -> Goal Authoring -> Target Mode Execution -> Consolidation & Iteration) and production deployment with Tencent Cloud EdgeOne Makers (edge Web + AI Agent hosting with built-in memory, sandbox, tracing, and gateway infrastructure).

**Raw article saved**: [[raw/articles/2026-06-23_gengdaj-codex-production-agent-workflow.md]]

**Index**: Added openai-codex entity entry to recently-updated entities section (was previously missing from index.md).

---
## 2026-06-25 X Accounts Scan

**Source**: x-accounts-scan cron job (fetch_x_accounts.py)
**Stats**: 12/84 accounts scanned, 12 new posts, 6 substantive articles processed

### New Concept Pages
- [[concepts/prompt-debt]] — Drew Breunig's framework for fragile prompt buildup, model lock-in, and solutions via DSPy/GEPA
- [[concepts/gemini-computer-use]] — Philipp Schmid's Android-specific Gemini Computer Use implementation guide
- [[concepts/ai-control]] — DeepMind's AI Control technical roadmap (TRAIT&R taxonomy, D1-D4/R1-R3 defense ladders, 15 mitigations)

### Enriched Entity Pages
- [[entities/drew-breunig]] — Added "The Problem is Prompt Debt" to Core Ideas + scaffold-docs-skill to Key Projects
- [[entities/philipp-schmid]] — Added Gemini Android Computer Use guide to Key Work and Blog sections
- [[entities/mario-zechner]] — Added DeepMind AI Control Roadmap + "Slow Down to Speed Up" talk recommendations
- [[entities/chris-tate]] — Added emulate (vercel-labs) to key projects, overview, and Known-for

### Raw Articles Saved
- raw/articles/2026-06-22_dbreunig_prompt-debt.md (Drew Breunig — "The Problem is Prompt Debt")
- raw/articles/2026-06-23_dbreunig_scaffold-docs-skill.md (Drew Breunig — scaffold-docs-skill README)
- raw/articles/2026-06-25_philschmid_gemini-android-use.md (Philipp Schmid — Gemini Android Computer Use guide)
- raw/articles/2026-06-25_google-gemini_android-computer-use-quickstart.md (Google Gemini quickstart repo)
- raw/articles/2026-06-24_yt_slow-down-ai-software-engineering.md (Gergely Orosz YouTube transcript)
- raw/papers/2026-06-24_deepmind_ai-control-roadmap.md (DeepMind AI Control Roadmap PDF)

### Skipped (Non-AI)
- hynek: psycache (PostgreSQL caching — not AI-related)
- badlogicgames: GitHub PR limits blog (open source management)
- _xjdr: noumena.com (AI coding tool — mentioned briefly, no article to scrape)

---
## [2026-06-25] Dreaming Wiki Ingest — Enriched entities/fireworks-ai.md (2 articles)

- **Enriched**: `entities/fireworks-ai.md` (289→348 lines, +59 lines)
  - Added "Frontier Training Infrastructure (June 2026)" section: zero-KLD train/serve alignment, batch invariance for large MoEs, sparse-attention indexer nondeterminism, DeepGEMM integration, validation table (KLD=0, 0% clipped tokens, reward stays healthy vs ~0.013 KLD, 45% clipped, collapse at step 20)
  - Updated "Hybrid Harness" section: added GLM 5.2 + Opus 4.8 benchmarks (SWE-bench Pro +7pp, Terminal-Bench +4pp, Legal Agent +4pp), cost efficiency ($3.50-6.09 vs $18.28 Opus baseline), same-model reviewer ablation fails
  - Sources added: 2 new raw/article references

---
## [2026-06-25] Dreaming Group Triage — Pipeline saturation scenario (Takes=2, Skips=3)

- **Context**: Daily pipeline saturation — blog-ingest (2 takes), newsletter-ingest (5 takes), active-crawl (5 articles), X-bookmarks (2 bookmarks) already processed today.
- **Takes**:
  - `entities/fireworks-ai.md` enrichment: zero-KLD train/serve alignment, batch invariance for large MoEs, DeepSeek DeepGEMM, GLM 5.2 managed service (14KB sitemap article)
  - `entities/fireworks-ai.md` enrichment: GLM 5.2 + Opus 4.8 worker+advisor benchmark data — SWE-bench Pro +7pp, Terminal-Bench +4pp, Legal Agent Benchmark +4pp (11KB sitemap article)
- **Skips**: Harvey Caryn Sandler case study (marketing), Cohere Aston Martin F1 (thin), ElevenLabs API auth (documentation)
- **Archive**: 3 skip items archived to `raw/archived/triage/dreaming/2026-06-25_20260625T180026Z.json` (total: 1151 URLs)

---
## [2026-06-25] X Bookmarks Ingest — 2 bookmarks processed (1 Zyphra, 1 BenchPress)

- **Bookmark 1 (ZyphraAI)**: Tweet thread on continual learning/plasticity loss in LLMs → enriched `entities/zyphra.md` with Research Directions section on plasticity loss scaling law and recursive self-improvement
- **Bookmark 2 (Dimitris Papailiopoulos)**: "You Don't Need to Run Every Eval" — X Article body via plain_text, saved to raw, created 2 new pages + 2 enrichments
  - **New concept**: `concepts/benchpress.md` — BenchPress: $0 benchmark prediction system; rank-2 SVD matrix completion on 83x49 model-benchmark matrix shows 5 benchmarks predict 44 others to within ~5 points (7% median abs error). SVD beats Claude Sonnet (5.8% vs 6.1%). PC1 = general capability, PC2 = novel reasoning + recency
  - **New entity**: `entities/dimitris-papailiopoulos.md` — Dimitris Papailiopoulos (@misc, GitHub: anadim); EE theory/compressed sensing background; creator of BenchPress using Claude Code + Codex
  - **Enriched**: `concepts/ai-benchmarks/benchmaxxing.md` — Added BenchPress wikilink in Related Concepts
- **Raw article saved**: `raw/articles/2026-02-25_dimitris-papailiopoulos_benchpress-you-dont-need-to-run-every-eval.md` (X Article plain_text, 17.7KB)
- **SCHEMA.md**: Added 2 new tags (`matrix-completion`, `svd`)
- **Sources**: X bookmarks pipeline (fetch_x_bookmarks.py, 2 new bookmarks, 475 processed cache)

---
## [2026-06-25] Active Crawl — 3 new concept pages + 1 enrichment from trending topics

- **New pages**: 3 concept pages created from trending AI topics (HN + X/Twitter + wiki gap analysis)
  - `concepts/openai-jalapeno-inference-chip.md` — OpenAI Jalapeño: custom LLM inference chip with Broadcom, 9-month tape-out, gigawatt-scale deployment, GPT-5.3-Codex-Spark (714 HN pts, TechCrunch + OpenAI)
  - `concepts/nvidia-45c-data-center-cooling.md` — NVIDIA 45°C Data Center Cooling: Rubin generation 100% liquid-cooled, near-zero water consumption, closed-loop warm-water design (348 HN pts, NVIDIA Blog)
  - `concepts/anthropic-alibaba-claude-ip-dispute.md` — Anthropic-Alibaba Claude IP Extraction Dispute: illicit distillation accusation, NSA/Mythos access loss, export controls context (450+248 HN pts, HN discussion)
- **Enriched**: `concepts/computer-use.md` — Added Gemini 3.5 Flash Computer Use section (223 HN pts, Google AI Blog)
- **Raw articles saved**: 5 source articles
  - `raw/articles/openai.com--index-openai-broadcom-jalapeno-inference-chip--f8a3b2c1.md` (pre-existing)
  - `raw/articles/2026-06-25_techcrunch-openai-broadcom-jalapeno.md`
  - `raw/articles/2026-06-25_hn-discussion_anthropic-alibaba-claude-extraction.md`
  - `raw/articles/2026-06-25_hn-discussion_nsa-mythos-anthropic-dispute.md`
  - `raw/articles/2026-06-25_nvidia-45c-liquid-cooling-data-center.md`
  - `raw/articles/2026-06-25_google-gemini-3-5-flash-computer-use.md`
- **SCHEMA.md**: Added 2 new tags (broadcom, data-center)
- **Sources**: HN Algolia (20 trending stories), X/Twitter xurl (10 results), blogwatcher DB (30 articles), wiki gap analysis (1769 concepts, 836 entities)

---
## [2026-06-25] Active Crawl — 3 new concept pages + 1 enrichment from trending topics

- **New pages**: 3 concept pages created from trending AI topics (HN + X/Twitter + wiki gap analysis)
  - `concepts/openai-jalapeno-inference-chip.md` — OpenAI Jalapeño: custom LLM inference chip with Broadcom, 9-month tape-out, gigawatt-scale deployment, GPT-5.3-Codex-Spark (714 HN pts, TechCrunch + OpenAI)
  - `concepts/nvidia-45c-data-center-cooling.md` — NVIDIA 45°C Data Center Cooling: Rubin generation 100% liquid-cooled, near-zero water consumption, closed-loop warm-water design (348 HN pts, NVIDIA Blog)
  - `concepts/anthropic-alibaba-claude-ip-dispute.md` — Anthropic-Alibaba Claude IP Extraction Dispute: illicit distillation accusation, NSA/Mythos access loss, export controls context (450+248 HN pts, HN discussion)
- **Enriched**: `concepts/computer-use.md` — Added Gemini 3.5 Flash Computer Use section (223 HN pts, Google AI Blog)
- **Raw articles saved**: 5 source articles
  - `raw/articles/openai.com--index-openai-broadcom-jalapeno-inference-chip--f8a3b2c1.md` (pre-existing)
  - `raw/articles/2026-06-25_techcrunch-openai-broadcom-jalapeno.md`
  - `raw/articles/2026-06-25_hn-discussion_anthropic-alibaba-claude-extraction.md`
  - `raw/articles/2026-06-25_hn-discussion_nsa-mythos-anthropic-dispute.md`
  - `raw/articles/2026-06-25_nvidia-45c-liquid-cooling-data-center.md`
  - `raw/articles/2026-06-25_google-gemini-3-5-flash-computer-use.md`
- **SCHEMA.md**: Added 2 new tags (broadcom, data-center)
- **Sources**: HN Algolia (20 trending stories), X/Twitter xurl (10 results), blogwatcher DB (30 articles), wiki gap analysis (1769 concepts, 836 entities)

---
## [2026-06-25] Newsletter Wiki Ingest — 5 takes from newsletter-triage checkpoint (FAILED → recovered from inbox pre-triage)

- **Notes**: Newsletter-triage cron job failed (API key 401). Recovered from inbox pre-triage summary + direct newsletter URL resolution. 3 newsletters triaged: "[AINews] It's Meta-Harness Summer", "[AINews] Claude Tag", "Databricks Podcast (Latent Space)". 15 total decisions (5 takes, 3 references, 7 skips).
- **New page**: `entities/matei-zaharia.md` — Matei Zaharia (Databricks CTO, Apache Spark/MLflow co-creator, Omnigent creator)
- **Enriched**: `concepts/meta-harness.md` — Added Omnigent commercial implementation section (Databricks open-source meta-harness, 4th interpretation layer)
- **Enriched**: `entities/openai.md` — Added GPT-5.5 Instant revision (June 2026) — improved intent understanding, constraint handling, conversational style
- **Enriched**: `entities/bespoke-labs.md` — Added OpenThoughts-Agent pipeline (open curation/training pipeline for agentic models with 100+ controlled ablations)
- **Enriched**: `entities/weaviate.md` — Added Engram GA (memory-as-asynchronous-infrastructure for AI agents)
- **Trash**: `entities/bespoke-labs.md` — duplicate updated: field fixed
- **Key topics covered**: Omnigent meta-harness, Matei Zaharia entity, GPT-5.5 Instant revision, OpenThoughts-Agent, Weaviate Engram GA, OpenAI Jalapeño (already processed by blog), Qwen-AgentWorld (already covered), GLM-5.2 (already covered), Claude Tag (already covered)
- **References**: Background agents ecosystem (Shopify/Stripe/Ramp/Paradigm), Databricks LTAP/Lakebase, Cursor x Notion integration
- **Skipped**: Meta PM (non-AI), Beehiiv Claude Tag (duplicate), Anthropic export control challenge, Claude Tag details (already covered), OpenAI Jalapeño (already covered), Qwen-AgentWorld (already covered), GLM-5.2 (already covered)

---
## [2026-06-25] Blog Wiki Ingest — 2 takes + 1 new raw article from blog-triage checkpoint

- **Enriched**: `entities/openai.md` — Added Jalapeño Intelligence Processor section (first custom inference chip, Broadcom partnership, 9-month tape-out, GPT-5.3-Codex-Spark running at production frequency, gigawatt-scale deployment with Microsoft)
- **Enriched**: `entities/modal-labs.md` — Added Modal Auto Endpoints section (SOTA inference with one click, Decagon voice AI case study: 290ms→190ms latency, DFlash mid-training methodology, synthetic data for speculator training)
- **Raw article saved**: `raw/articles/openai.com--index-openai-broadcom-jalapeno-inference-chip--f8a3b2c1.md` (OpenAI/Broadcom Jalapeño announcement)
- **Triage**: 19 articles triaged (2 takes, 2 references, 15 skips). Blog sources: simonwillison.net, Modal Blog, OpenAI News, Merge Blog, daringfireball.net, xeiaso.net, shkspr.mobi, refactoringenglish.com, gilesthomas.com, johndcook.com, jeffgeerling.com, dfarq.homeip.net, devblogs.microsoft.com, blog.jim-nielsen.com
- **Key themes**: inference-optimization, custom-ai-chips, mcp-integration

---

## [2026-06-24] Trend Topics Wiki Expansion — 3 entity updates + 1 new concept + 1 concept enrichment

Based on trending-topics-2026-06-23 and trending-topics-2026-06-24 analysis reports.

- **Updated**: `entities/harvey.md` — Added "Training a Legal Agent" Applied Compute methodology (domain-specific agent training, behavioral evaluation)
- **Updated**: `entities/elevenlabs.md` — Added Ads Engine (50+ language ad localization, Google/Meta/LinkedIn push), Anarock case study (5x sales capacity, Indian real estate multilingual voice AI), Voice Agent Latency Optimization
- **Updated**: `entities/decagon.md` — Added Duet Autopilot (A/B testing, simulation, Watchtower QA, redefining forward deployment)
- **Created**: `concepts/voice-agent-evaluation.md` — Six-Pillar Framework for voice agent evaluation (TTS quality, conversation quality, tool usage, intelligence, compliance, reliability), production targets, industry weighting, common mistakes
- **Updated**: `concepts/agentic-engineering.md` — Added "The Agent Loop Debate" section (Boris Cherny/Jensen Huang pro-loop, Ed Zitron cargo cult critique, Armin Ronacher code quality concerns, Drew Breunig prompt debt connection)
- **Updated**: `wiki/index.md` — All changes reflected

---
## [2026-06-24] New concept page — KV-Aware Routing

- **concepts/kv-aware-routing.md** — KV cache-aware request routing for LLM inference serving. Covers NVIDIA Dynamo/Mooncake/vLLM implementations, comparison with traditional routing, and technical challenges. Resolves orphan wikilinks from multiple pages

---
## [2026-06-24] Active Crawl — 5 concept pages + 5 raw articles from trending topics

- **New pages**: 5 concept pages created from trending AI topics (HN + X/Twitter + wiki gap analysis)

  - `concepts/mistral-ocr-4.md` — Mistral OCR 4: SOTA OCR model, multilingual document parsing, structured markdown/JSON output, superior to Azure/Gemini/Amazon (470 HN pts)
  - `concepts/codex-logging-bug.md` — Codex Logging Bug: SQLite feedback logs writing up to 640 TB/year, rapid SSD wear, GitHub issue #28224 (503 HN pts)
  - `concepts/ai-affordability-crisis.md` — AI Affordability Crisis: David Rosenthal's analysis of LLM inference cost vs revenue, zero-margin pricing, crypto-mining comparison (290 HN pts)
  - `concepts/claude-tag.md` — Claude Tag: Anthropic's team AI agent for Slack; multiplayer chat, persistent channel memory, proactive/async capabilities (252 HN pts)
  - `concepts/qwen-agentworld.md` — Qwen-AgentWorld: arXiv 2606.24597; language world models for agents, 397B MoE model, 7-domain environment simulation (119 HN pts)
- **Raw articles saved**: 5 source articles
  - `raw/articles/2026-06-24_mistral-ai_ocr-4.md`
  - `raw/articles/2026-06-14_openai-codex_logging-tb-ssd.md`
  - `raw/articles/2026-06-24_dshr_ai-affordability-crisis.md`
  - `raw/articles/2026-06-24_anthropic_claude-tag.md`
  - `raw/articles/2026-06-24_arxiv-2606.24597_qwen-agentworld.md`
- **SCHEMA.md**: Added 4 new tags (ocr, document-intelligence, incident, sustainability)
- **Sources**: HN Algolia (15 trending stories), X/Twitter xurl (10 results), blogwatcher DB, wiki gap analysis

---

## [2026-06-24] Skeleton Enrichment — 4 entity pages enriched from minimal to comprehensive

- **Entity pages enriched**:
  - `entities/dario-amodei.md` — Restored 145-line historical depth + Wikipedia biography (education, career, DoD dispute, Time 100); 3 key essays documented (Machines of Loving Grace, The Adolescence of Technology, Policy on the AI Exponential)
  - `entities/conviction.md` — Expanded from 18-line stub to full VC firm profile with portfolio (18 companies), team, projects (Embed, No Priors, Commit), and key publications
  - `entities/alex-imas.md` — Expanded from 16-line stub to comprehensive profile; Director of AGI Economics at Google DeepMind, Professor at UChicago Booth, relational sector scarcity framework
  - `entities/phil-trammell.md` — Expanded from 15-line stub to full profile; Head of Economics at Epoch AI, Stanford HAI Research Scholar, AGI scenario modeling, labor-capital complementarity
- **Redirect consolidated**: `alex-imus.md` (typo slug) → redirected to canonical `alex-imas.md`; 3 cross-references updated in `concepts/ai-economics.md`, `concepts/agi-scarcity.md`, and `wiki/index.md`
- **Duplicates cleaned**: Redirect page `alex-imus.md` converted to redirect pointing to `alex-imas.md`
- **Sources fetched**: Wikipedia, Jina Reader on Dario Amodei and Conviction sites, Dwarkesh Patel podcast transcripts

---

## [2026-06-24] Blog Wiki Ingest — 4 takes + 3 references from blog-triage checkpoint

- **New page**: `concepts/ai-benchmarks/parallelkernelbench.md` — ParallelKernelBench (PKB): multi-GPU kernel generation benchmark. 87 problems, GPT-5.5 tops at 31% fast@3. Agentic harness evaluation plateaued after ~20 iterations.
- **Enriched**: `entities/openai.md` — Added Appia Foundation (Linux Foundation-hosted AI evaluation standards) + GPT-5 immunology case study (Unutmaz T cell puzzle, IL-2 pathway).
- **Enriched**: `entities/anildash.md` — Added "Platform War Against Big AI" section: 4 tactics (disintermediation, provider portability, economic value destruction, channel anger).
- **Enriched**: `entities/ed-zitron.md` — Added "Cargo Culture" subsection: religious/cargo cult metaphors, Rot-Com Bubble thesis, venture capital cargo cult critique.
- **Enriched**: `entities/george-hotz.md` — Added "Liminality" blog post (Jun 23): Fullmetal Alchemist metaphor, liminal state of AI, control as illusion.
- **Sources**: Together AI Blog, OpenAI Blog, anildash.com, wheresyoured.at, geohot.github.io (Jun 23, 2026).
- **Archive**: 16 skip/reference items archived to `raw/archived/triage/blog/2026-06-24_20260624T071008Z.json`.
- **Triage recovery**: Upstream blog-triage failed with JSON parse error; recovered from checkpoint at `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json`.

---

## [2026-06-24] Newsletter Wiki-Ingest — Ben's Bites: 3 takes + 5 references

- **Processed**: 3 takes + 5 references from newsletter-triage checkpoint (1 newsletter batch: Ben's Bites). Recovered from triage render failure (checkpoint persistence).
  - `entities/armin-ronacher.md` — enriched with "The Coming Loop" essay (June 23, 2026): harness-level vs agent-level loops distinction, code quality degradation from autonomous looping, software-as-organism metaphor, inability to opt out (security/competitive pressure), cognitive dependency, future harness design. +13 lines, +timeline entry, +sources.
  - `concepts/agent-skills.md` — enriched with Codex Record & Replay: workflow recording as skills via live demonstration. Distinct skill authoring method (recorded workflows vs instruction bundles). +12 lines.
  - `concepts/claude-code/claude-code-artifacts.md` — NEW page: Claude Code Artifacts feature (beta, Team/Enterprise). Shareable functional HTML pages for PR walkthroughs, project dashboards, and prototypes. +sources: claude.com/blog.
  - `concepts/sakana-fugu.md` — added Fugu Ultra benchmark numbers (73.7 SWE-bench Pro, 82.1 TerminalBench 2.1, Fable-class).
  - `entities/perplexity-comet.md` — added Brain self-improving memory system for agents. +sources.
  - `entities/cursor-ai.md` — added /automate slash command (natural-language triggers, tools, instructions). +sources.
  - `concepts/gemini/gemini-enterprise-agent-platform.md` — updated Interactions API status to Generally Available (June 2026).
  - `concepts/agentic-commerce.md` — added Stripe Directory (CLI-based business search and pay) and Invoice Payment MCP (xMCP).
  - Sources: Ben's Bites newsletter (June 23, 2026).
---
## [2026-06-23] X Bookmarks Ingest — Drew Breunig "The Problem is Prompt Debt"

- **Raw article saved**: `raw/articles/2026-06-23_drew-breunig-prompt-debt.md` — X Article from @dbreunig
- **Concept page enriched**: `concepts/prompts-as-technical-debt.md` — Added Drew Breunig's "Prompt Debt" framework with three-stage spiral, fighting the weights, Goedecke vs Breunig comparison, and prevention via DSPy/GEPA. Added tags: `fighting-the-weights`, `dspy`, `gepa`. Expanded from 83 → ~200 lines.
- **Entity pages enriched**: `entities/drew-breunig.md` (+timeline, +writings, +sources, +related), `entities/drew-breunig--core-ideas.md` (+Prompt Debt section), `entities/drew-breunig--writings.md` (+entry), `entities/drew-breunig--timeline.md` (+entry)
- **GEPA page enriched**: `concepts/gepa.md` — Noted Breunig citation as prompt-debt solution
- **SCHEMA.md updated**: Added `fighting-the-weights` tag to Models taxonomy

---

## [2026-06-23] Wiki Ingest — Warp Self-Improvement Loop for Skills

- **Warp self-improvement loop for skills** article.
  - Saved raw article: raw/articles/2026-06-23_warp-dev_self-improvement-loop-for-skills.md
  - Enriched entities/warp-terminal.md — added Self-Improvement Loop for Skills section (Execute->Evaluate->Revise cycle, YAML skill definitions, human-in-the-loop approval, comparison table with Hermes/OpenClaw)
  - Enriched concepts/skill-architecture-patterns.md — added Warp as third approach alongside Hermes and OpenClaw (execution-feedback skills section, updated comparison table, decision framework, related links)
  - Sources: https://www.warp.dev/blog/self-improvement-loop-for-skills

---

## [2026-06-23] Active Crawl — 4 concept pages + 2 raw articles

- **Active crawl**: created 4 concept pages and saved 2 raw articles from trending AI topics (HN + X/Twitter + wiki gap analysis).

---

## [2026-06-23] Skeleton Enrichment — brad-lyons enriched from skeleton to comprehensive

- **Skeleton enrichment**: enriched [[entities/brad-lyons]] from skeleton to comprehensive entity page. Added AI Investment Supercycle Hypothesis (Aug 2025), Revenue Segmentation Framework, AI Playbook for Operators and Investors, multi-sector coverage (SaaS, semis, nuclear, gaming), and expanded research methodology. Status: skeleton removed. Sources: xurl profile data, SaaSpocalypse Note Tweet, AI Supercycle Note Tweet, Revenue Segmentation tweet.

  - Created concepts/prompt-injection.md — Prompt injection as role confusion, style-based jailbreaks, token-level injection defenses
  - Created concepts/vibethinker.md — VibeThinker-3B (arxiv 2606.16140): 3B model beating DeepSeek V3.2/GLM-5/Gemini 3 Pro on reasoning via curriculum SFT+GRPO+self-distillation
  - Created concepts/openai-daybreak.md — OpenAI Daybreak: GPT-5.5-Cyber, Codex Security, Patch the Planet (June 22 announcement)
  - Created concepts/apertus-sovereign-ai-model.md — Apertus open foundation model (8B/70B) for sovereign AI, EU AI Act compliant, 1000+ languages
  - Saved raw articles: 2026-06-15_arxiv-2606.16140_vibethinker-3b-verifiable-reasoning.md, 2026-06-22_openai_daybreak-securing-the-world.md
  - Added SCHEMA tags: daybreak, gpt-5-5-cyber
  - Fixed 2 broken wikilinks
  - Sources: HN Algolia (16 trending stories), X/Twitter xurl (10 results), blogwatcher DB, wiki gap analysis

---

---

- 2026-06-24: Watchdog fix — added 2 missing `---` separators in log.md between consecutive ## sections. No other auto-fixable issues found. Index: Format B (clean). _index.md: 0 pipe corruption (false positives — all legitimate markdown tables). Report: wiki-health clean (0 stale pages, 30 orphans flagged for human review).
- 2026-06-25: enriched [[concepts/loop-engineering]] with HuaShu PDF synthesis (Four-Layer Stack, Five Moves, Generator/Evaluator, Anti-patterns, Real Loops, Four Costs, First Loop Recipe, Economics of Judgment); added raw/papers/2026-06-24_huashu_loop-engineering-anthropic-playbook.pdf
- 2026-06-25: enriched [[concepts/loop-engineering]] with 0xCodez X Article (14-step roadmap, 4-condition test, Ralph Wiggum loop, security tax); saved raw/articles/2026-06-09_0xcodez_loop-engineering-14-step-roadmap.md

---

## [2026-06-25] Watchdog auto-fix

- **Fixed**: 6 missing `---` separators in log.md between consecutive ## section headers (10 sections verified, 0 remaining)
- **Pipeline watch**: `x_accounts` stale (26h) — reported for human review. Newsletter chain break (triage API 401) confirmed **stale** — pipeline self-recovered via inbox pre-triage (see log entry at line 49)
- **Index**: Format B (digest), 0 pipe corruption, 0 line prefix corruption, 0 triple brackets, 0 ghosts, 0 cross-section misplacement, 0 Japanese filenames, 0 duplicates — fully clean
- **Log.md**: 0 pipe corruption, 0 line prefix corruption — clean
- **Filesystem**: 836 entities, 1773 concepts, 31 comparisons, 4 queries, 11 events = 2708 total

---

## [2026-06-25] Wiki Health auto-fix

- **Fixed**: 3 duplicate entries in index.md (concepts/agentic-engineering, entities/modal-labs, entities/openai — older entries removed)
- **Added**: 20 orphan pages to index.md (8 concepts + 12 comparisons) — Format B digest
- **Index Format B**: 0 pipe corruption, 0 line prefix, 0 triple brackets, 0 ghosts, 0 duplicates — clean ✅
- **Log.md**: 0 pipe corruption, 0 missing separators — clean ✅
- **Filesystem**: 836 entities, 1773 concepts, 31 comparisons = 2640 total Layer 2

---
## 2026-06-26 — Awesome Evals Bulk Ingestion (57 benchmarks + 2 tools)

**Source**: benchflow-ai/awesome-evals GitHub repo (443+ curated eval links, 175KB README)
**Raw article**: `wiki/raw/articles/benchflow-awesome-evals-2025.md`

### New benchmark pages created (57):
- **Web/OS Agent Benchmarks (12)**: webarena, osworld, browsecomp, visualwebarena, webvoyager, real-benchmark, webgames, androidworld, windowsagentarena, mind2web-2, st-webagentbench, online-mind2web
- **Coding/SWE Agent Benchmarks (9)**: swe-lancer, swe-gym, swe-rebench, swe-bench-pro, multi-swe-bench, appworld, spider-2, terminal-bench, gta-benchmark
- **Science/Research/Enterprise (12)**: re-bench, mle-bench, paperbench, scienceagentbench, deepresearch-bench, core-bench, bixbench, theagentcompany, crmarena-pro, gdpval, remote-labor-index, gaia2-are
- **Safety/Adversarial (12)**: agentdojo, agentharm, injecagent, shade-arena, agent-security-bench, decodingtrust, cybench, benchjack, rewardbench, rewardbench-2, judgebench, verifybench
- **Agent Evaluation Infrastructure (12)**: livebench, hal-leaderboard, benchflow-tool, trail, cursorbench, letta-leaderboard, stripe-agent-benchmark, skillsbench, clawsbench, agent-memory-bench, pyrit, verifiers-tool

### Updated:
- `concepts/ai-benchmarks/index.md` — restructured with new sections (Web/OS, Science/Research/Enterprise, Safety/Adversarial, Reward/Judge, Agent Eval Infrastructure). Total: 105 benchmark pages.
- `wiki/index.md` — added 9 representative entries + sub-index pointer

### Coverage delta:
- Before: 49 benchmark pages in ai-benchmarks/
- After: 106 benchmark pages (including index.md)
- Net new: 57 benchmark pages

---

## [2026-06-26] Watchdog auto-fix

- **Fixed**: Removed literal `\n` artifact in log.md that broke the Active Crawl section — orphaned concept items (mistral-ocr-4, codex-logging-bug, ai-affordability-crisis, claude-tag, qwen-agentworld) restored under their parent section with proper `---` separators
- **Fixed**: Restructured Skeleton Enrichment section (4 entity pages: dario-amodei, conviction, alex-imas, phil-trammell) as standalone section with correct `---` separators
- **Fixed**: Flat-format Newsletter wiki-ingest entry (`- 2026-06-24:` without header) → proper `## [2026-06-24] Newsletter Wiki-Ingest` section with `---` separators
- **Fixed**: 3 flat-format 2026-06-23 entries (Warp, Active Crawl, Skeleton Enrichment) → proper `## [DATE]` sections with `---` separators
- **Fixed**: Missing `---` separator before legacy `# Wiki Log` section
- **Index.md**: Format B digest — 0 duplicates, 0 pipe corruption, 0 ghosts, 0 triple brackets — clean ✅
- **Log.md**: 0 remaining `\n` artifacts, 0 pipe corruption, 0 line prefix corruption — clean ✅
- **Filesystem**: 826 entities, 1837 concepts (1731 + 106 ai-benchmarks), 31 comparisons, 4 queries, 11 events = 2709 total Layer 2

---

## [2026-06-27] Watchdog auto-fix

- **Fixed**: Pipe corruption in log.md (11 lines) — previous patch() call left `|` prefix on `##`, `###`, `|- ` and blank lines in the Blog Wiki Ingest section (lines 21-31). Restored correct markdown structure.
- **Fixed**: Missing `---` separators (11 gaps) between consecutive `## [DATE]` sections in log.md — added separators to fix section boundary breaks.
- **Verified**: index.md — 0 pipe corruption, 0 line prefix, 0 triple brackets, 0 duplicates, 0 ghost entries, 0 cross-section misplacement — clean.
- **Verified**: All `_index.md` files — 0 pipe corruption (false-positive shell script false matches corrected).
- **Filesystem**: 837 entities, 1840 concepts, 31 comparisons, 13 events, 4 queries = 2725 total Layer 2

---
## 2026-06-29
- `concepts/evaluation/llm-as-judge` — Added BINEVAL section (Cho et al., 2026, ICML Workshop). Binary question decomposition for interpretable LLM evaluation. Raw paper + summary to `raw/papers/2026-06-25_2606.27226_*`.
- **Ingested**: NVIDIA Research blog "KV Cache Compression and Its Infra Problems" (2026-06-15). Raw article → `raw/articles/2026-06-15_nvidia-kv-cache-compression-infra-problems.md`. Created `concepts/kv-cache-compression` (survey of eviction/quantization/geometry methods + two infrastructure problems) and `concepts/triattention` (pre-RoPE geometry scoring + forward-packing compaction, ICML 2026). Updated `concepts/kv-cache` and `concepts/flash-attention-4` with cross-references. Added missing index entries for `kv-cache`, `kv-cache-compaction`, `flash-attention-4`.

---
## 2026-06-30 — Multi-Model Synthesis Strategies: Devin Fusion + OpenRouter Fusion + Sakana Fugu

### Ingested
- **Cognition Devin Fusion blog post** (2026-06-29): Sidekick pattern + dynamic mid-session routing. 35% cost reduction. Raw → raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness.md
- **OpenRouter Fusion API blog post** (2026-06-12): Panel synthesis. Fable 5 + GPT-5.5 = 69.0% DRACO. Raw → raw/articles/2026-06-12_openrouter-fusion-api-multi-model-synthesis.md

### Created
- **concepts/multi-model-synthesis-strategies** — Cross-cutting concept page. Compares 3 approaches: Cognition Devin Fusion (Sidekick), OpenRouter Fusion (Panel Synthesis), Sakana Fugu (Evolved Orchestration)

### Updated
- **concepts/coding-agents/model-routing** — Added Devin Fusion section + cross-reference
- **entities/openrouter** — Added Fusion API section + Related links
- **entities/cognition** — Added Devin Fusion section
- **concepts/sakana-fugu** — Added cross-reference to multi-model-synthesis-strategies
- **wiki/index.md** — Added multi-model-synthesis-strategies entry

---
## 2026-07-02
- 2026-07-02: Ingested Geoffrey Litt's mega thread 'Understanding the Code Our Agents Write' (36-part X thread) to raw/articles/2026-07-02-geoffreylitt-understanding-code-agents-write.md

---
## 2026-07-05

- **wiki-graph-analysis** — Full weekly wiki graph analysis run: 2,205 pages scanned. Report saved to wiki/queries/wiki-graph-analysis-weekly-2026-07-05.md. Added Queries section to index.md.

---
## 2026-07-05

- **duplicate page merge** — Merged 33 entity-concept duplicate pairs (kept larger file per pair). Fixed stale ghost entry `entities/show-us-your-agent-skills` → `concepts/show-us-your-agent-skills` in index.md. 0 ghost entries after fix.

- **duplicate merge fix** — Recovered deleted page content from git (d4da1bff) and merged unique sections into kept pages. 28 of 33 pairs had unique content to merge (5 were fully overlapping). +1,439 lines of recovered content.

- **sources field fix** — Added `sources: []` to 752 pages that were missing the field in YAML frontmatter. SCHEMA compliance: all pages now have the `sources` field.

- **index.md missing entries fix** — Added 2,416 missing pages to index.md (746 entities, 1,653 concepts, 3 comparisons, 3 queries, 11 events). Index now has 2,676 entries covering all filesystem pages.

- **orphan page fix** — Added inbound links from concepts/harness-engineering.md to 3 orphan pages (claude-code-best-practices, writing-tools-for-agents, context-engineering). Orphans reduced from 5 to 2 (archive pages only).
- 2026-07-06 llm-pricing-monitor: Updated OpenAI deep-research pricing (o3-deep-research $5→$10/$20→$40; o4-mini-deep-research $1→$2/$4→$8); added Claude Sonnet 5 ($2/$10 intro, $3/$15 std); updated cache/batch/trend tables

---
## [2026-07-07] wiki: Ingested Gemma 4 Technical Report (arXiv:2607.02770)

**Updated:**
- `entities/gemma-4.md` — Added Technical Report section with full benchmark tables (Arena Elo, thinking mode, vision, long-context, audio), detailed parameter breakdown, pre-training infrastructure, architecture highlights, quantization details, safety evaluation. Updated sources with arxiv link and raw PDF.

**Sources:**
- https://arxiv.org/abs/2607.02770 (Gemma 4 Technical Report, July 2, 2026)
- PDF saved to `raw/papers/gemma4-technical-report.pdf`

---
## [2026-07-07] wiki: Ingested Harrison Chase "Wiki Memory" X Article

**Created:**
- `concepts/wiki-memory.md` — New concept page for the wiki memory agent memory pattern. Covers the core idea (agent-maintained file-based knowledge layer), distinction from RAG, "brain clone" motivation, examples (DeepWiki, Karpathy's LLM Wiki, Factory AutoWiki), open questions, and relationship to the Two Camps memory taxonomy. Maps to Camp 2: Context Substrates.

**Updated:**
- `entities/harrison-chase.md` — Added "Wiki Memory" thesis section (June 2026) with key arguments and link to concept page. Added source URL.
- `entities/langchain.md` — Added wiki-memory cross-reference in Memory section.
- `index.md` — Added `concepts/wiki-memory` entry after `ai-agent-memory-two-camps`.
- `raw/articles/2026-06-30_langchain-wiki-memory.md` — Raw X Article text saved.

**Sources:**
- https://x.com/hwchase17/status/2071963622298050997 (Harrison Chase, "Wiki Memory", 2026-06-30, 1114 bookmarks)

---
## [2026-07-09] wiki: Grok 4.5 launch event + enrich xai/grok-4-3/spacex-cursor-acquisition

### Created
- **`events/grok-4-5-launch.md`** — SpaceXAI launches Grok 4.5, first Opus-class coding & agents frontier model co-trained with Cursor (July 9, 2026). Covers: first model trained specifically for coding/agents, co-training with Cursor, Musk's "Opus-class but faster/cheaper" positioning, capability-per-dollar strategy, double usage in Cursor first week, Hermes Agent and OpenRouter support. Tags: xai, model, coding-agents, grok, spacex.

### Updated
- **`entities/xai.md`** — Added Grok 4.5 row to the Grok model family table. Added `### Grok 4.5 — Coding & Agents Model (July 2026)` section after the Grok Build section. Added newsletter source. Bumped `updated` to 2026-07-09.
- **`entities/grok-4-3.md`** — Added `## Successor: Grok 4.5` section at end with key differences from Grok 4.3. Added newsletter source. Bumped `updated` to 2026-07-09.
- **`concepts/spacex-cursor-acquisition.md`** — Added `## Post-Acquisition: Grok 4.5 Co-Training` section with key details, strategic significance, and relationship to Grok Build. Added newsletter source. Bumped `updated` to 2026-07-09.
- **`wiki/index.md`** — Added `events/grok-4-5-launch` to Events section; updated Events count from 14 → 15.

### Sources
- raw/newsletters/2026-07-09-ainews-spacexai-launches-grok-4-5-first-opus-class-model-post-cursor-acquisition.md

---
## [2026-07-12 18:00 UTC] dreaming | Knowledge consolidation — saturation day, Takes=0

**Checkpoint**: `20260712T180059Z` — 1 article collected (ATP podcast, non-AI), 169 recent raw articles on disk.

**Pattern E Filesystem Scan**: Top 15 most recent raw articles scanned. All AI-relevant candidates already have comprehensive wiki coverage:
- Apple sues OpenAI (trade secret theft) → `events/apple-sues-openai-2026.md` (60 lines, detailed)
- Geohot "AI 2040 and the Cult of Intelligence" → `entities/george-hotz.md` (340 lines, section at L227-241)
- Cline autonomous coding agent → `entities/cline.md` + `concepts/cline.md`
- Reame CPU inference server → `concepts/reame.md`
- Mindwalk session replay → `concepts/mindwalk.md`
- Thinking Machines Lab → `entities/thinking-machines-lab.md`
- GPU circular financing (CoreWeave/Nebius) → raw HTML only, no extractable content
- Machinecraft 39 agents → YouTube video, no transcript

**Prior triage verification**: Jul 11 triage had 3 reference enrichments (Cohere DSD, Fireworks MiniMax M3 Blackwell, Hebbia data integrations). All confirmed consumed — wiki pages already contain the content.

**Archive**: `archive_triage.py` run — 15 candidates, 2 newly archived, 13 dedup_skipped. Total archive: 1,540 URLs.

**Result**: 0 takes, 0 references (all previously handled). Saturation confirmed.

---

## [2026-07-13 17:35 UTC] watchdog | Auto-fix: 19 missing log separators

### Changes
- Fixed 19 missing `---` separators between consecutive `## [YYYY-MM-DD]` log entries
- No index corruption found (pipe, triple-bracket, line-number: 0)
- All section header counts match filesystem
- 0 genuine ghost entries (541 "stale" from stale graph report all false)
- 6 duplicate entity pairs detected (all hyphen-stripping variants) — needs human merge
- Frontmatter gaps: 23 pages missing `created` field (below escalation)
- Log health: header not buried, 0 pipe corruption

---

## [2026-07-13 18:00 UTC] dreaming | Saturation day — 0 takes, 2 references
- Checkpoint: total_articles=1 (non-AI podcast), recent_raw_articles=180
- Prior triage at 12:00 UTC consumed (5 skips)
- Filesystem scan: 2 enrichment candidates (Ed Zitron memory crisis, Merge Gateway cost eval)
- 15 non-AI articles batch-skipped
- Archive: 8 candidates, 2 newly archived, 6 dedup skipped (total: 1604 URLs)

---

## 2026-07-14 — Ingest: Learning pi through force (Mueller Minute)
- Source: https://muellerminute.substack.com/p/learning-pi-through-force (published 2026-07-13)
- Author: Zach Mueller (@TheZachMueller)
- Raw article saved: raw/articles/2026-07-13_muellerminute_learning-pi-through-force.md
- Updated: entities/pi.md — added "Real-World Pipeline Migration: Model Memo" section, new source
- Updated: entities/zach-mueller.md — added Substack URL, new article in Mueller Minute table, cross-refs to pi/glm-5-2/kimi-k2-7-code
- Updated: wiki/index.md — enriched entries for pi and zach-mueller

---

## [2026-07-14] watchdog | Auto-fix — 3 missing log separators

### Changes
- **Fixed 3 missing `---` separators** between consecutive log sections
  - Before `## [2026-07-13] enrichment | Neovim analogy & harness cost data added to Pi`
  - Before `## [2026-07-13 18:00 UTC] dreaming | Saturation day — 0 takes, 2 references`
  - Before `## 2026-07-14 — Ingest: Learning pi through force (Mueller Minute)`

### Health Check
| Metric | Status |
|--------|--------|
| Index structural health | Clean (2780 lines) |
| Ghost entries | 0 |
| Index corruption (pipe/line/triple) | None detected |
| Log separators | 0 missing out of 152 sections |
| Cross-section misplacement | 0 |
| Tag violations | 0 |
| Orphans | 23 (all _index.md + archive — false positives) |
| Header counts match filesystem | Entities 849, Concepts 1880, Comparisons 35 — all match |

## [2026-07-16] watchdog | Auto-fixed 3 missing log separators, verified full wiki health

### Changes
- Fixed 3 missing `---` separators between consecutive log sections in log.md
- Full verification: 0 pipe corruption, 0 ghost entries, 0 missing sources, 0 tag violations, 0 cross-section misplacement
- Header counts match filesystem: Entities 852, Concepts 1891, Comparisons 35, Events 17, Queries 6

### Metrics
| Category | Count |
|----------|-------|
| Index structural health | Clean (2795 lines) |
| Ghost entries | 0 |
| Index corruption (pipe/line/triple) | None detected |
| Log separators | 0 missing out of 156 sections |
| Cross-section misplacement | 0 |
| Tag violations | 0 |
| Missing sources | 0 |
| Orphans (non-archive) | 0 |
| Header counts match filesystem | All match |

## [2026-07-17] Weekly wiki graph analysis

### Changes
- Ran `scripts/wiki_graph_analysis_weekly.py` on 2,249 pages
- Saved report to `queries/wiki-graph-analysis-weekly-2026-07-17.md`

### Findings
- 38 orphans, 4,302 broken links (99 fixable), 16 duplicate groups, 106 stale pages
- New duplicates detected: cline (entities vs concepts), qwen (entities vs concepts)
- Agentic-search remains largest page (1,191 lines)
- 542 stale index entries need cleanup

### Recommendations
- HIGH: Create concept/context-engineering stub (fixes 131 broken links)
- HIGH: Merge 6 entity duplicate pairs (2 weeks no progress)
- HIGH: Disambiguate cline and qwen
- HIGH: Investigate dspy-rlm / rlm-recursive-language-models duplication
- MEDIUM: Bulk refresh 106 stale pages (growing ~47/week)
- MEDIUM: Fix 99 auto-fixable wikilinks

## [2026-07-17] Weekly wiki graph analysis

### Changes
- Ran scripts/wiki_graph_analysis_weekly.py on 2,249 pages
- Saved report to queries/wiki-graph-analysis-weekly-2026-07-17.md

### Findings
- 38 orphans, 4,302 broken links (99 fixable), 16 duplicate groups, 106 stale pages
- New duplicates detected: cline (entities vs concepts), qwen (entities vs concepts)
- Agentic-search remains largest page (1,191 lines)
- 542 stale index entries need cleanup

### Recommendations
- HIGH: Create concept/context-engineering stub (fixes 131 broken links)
- HIGH: Merge 6 entity duplicate pairs (2 weeks no progress)
- HIGH: Disambiguate cline and qwen
- HIGH: Investigate dspy-rlm / rlm-recursive-language-models duplication
- MEDIUM: Bulk refresh 106 stale pages (growing ~47/week)
- MEDIUM: Fix 99 auto-fixable wikilinks


## [2026-07-17] Weekly wiki graph analysis

### Changes
- Ran scripts/wiki_graph_analysis_weekly.py on 2,249 pages
- Saved report to queries/wiki-graph-analysis-weekly-2026-07-17.md

### Findings
- 38 orphans, 4,302 broken links (99 fixable), 16 duplicate groups, 106 stale pages
- New duplicates: cline, qwen (entities vs concepts)
- Agentic-search still largest page (1,191 lines)
- 542 stale index entries need cleanup

### Recommendations
- HIGH: Create concept/context-engineering stub (fixes 131 broken links)
- HIGH: Merge 6 entity duplicate pairs (2 weeks no progress)
- HIGH: Disambiguate cline and qwen
- HIGH: Investigate dspy-rlm / rlm-recursive-language-models duplication
- MEDIUM: Bulk refresh 106 stale pages (growing ~47/week)
- MEDIUM: Fix 99 auto-fixable wikilinks

## [2026-07-17 23:00 UTC] bookmark | Armin Ronacher — Junior resource subscriptions processing

### Source
- raw/article: `raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive.md` — "Reactive Agents are Proactive" by Armin Ronacher (July 16, 2026)

### Wiki Changes
- `wiki/entities/armin-ronacher.md` — Updated frontmatter (bumped updated to 2026-07-17, added source); added timeline entry for July 16, 2026; added "Resource Subscriptions / Reactive Agents" subsection under Recent Themes
- `wiki/entities/junior.md` — **NEW** entity page for Junior, Sentry's open-source AI coding agent with resource subscription architecture
- `wiki/concepts/agent-resource-subscriptions.md` — **NEW** concept page documenting the resource subscriptions design pattern for coding agents
- `wiki/index.md` — Added junior.md and agent-resource-subscriptions.md entries

## [2026-07-18 18:00 UTC] dreaming | Knowledge consolidation — saturation day, Takes=0, 1 minor update

**Articles screened**: 0 (checkpoint empty), 202 recent raw articles (filesystem)
**Duplicate check**: 5 prior triage decisions (all skip — already covered by raw-backlog-ingest)
**Takes**: 0 | **References**: 1 | **Skips**: 5

**Enrichment**: [[concepts/claude/fable-5]] — Added July 20 permanent subscription inclusion (Max/Team Premium at 50% limits, Pro $100 credit). Competitive pressure from GPT-5.6 Sol and Kimi K3 cited as driver.

**Already covered (verified)**:
- Kimi K3 → `concepts/kimi-k3.md` (213 lines, pelican benchmark, Arena.ai results)
- VulnHunter → `concepts/ai-vulnerability-detection-at-scale.md` (extensive Capital One section)
- State of Open Source AI 2026 → `concepts/open-source-llms.md` (Mozilla report cited)
- Healthcare AI Agent → `concepts/ai-agent-architecture.md` (Maven Clinic case study)
- Sean Goedecke / Gwern grokking → `entities/seangoedecke-com.md`
- Hyperbo articles → `entities/hyperbo.md`

## [2026-07-18 18:20 UTC] dreaming-wiki-ingest | Saturation confirmation — upstream dreaming-group already committed enrichment

**Detection**: Upstream dreaming-group at 18:00 UTC completed analysis + enrichment before JSON render failure. Triage recovery via output file (4,332 lines).

**Status**: Takes=0 is post-enrichment state (confirmed per Pitfall #21)
- Enrichment committed: `[[concepts/claude/fable-5]]` — Fable 5 permanent subscription details
- 2 reference candidates both verified as already covered by upstream (Mozilla report in `concepts/open-source-llms.md`, Maven Clinic case study in `concepts/ai-agent-architecture.md`)
- Archive: 23 decisions archived (16 newly archived) at 18:15 UTC
- Git: Dreaming enrichment + archive both committed and pushed

**Verification**: log.md entry confirms upstream enrichment at 18:00 UTC. No downstream work needed.

## [2026-07-19 07:00 UTC] blog-ingest — 4 pages created/updated, 12 raw articles saved

**Pipeline**: blog-ingest (daily blog RSS collection)
**Checkpoint**: /opt/data/.hermes/cron/data/blog_ingest/blog_ingest_20260719T070034Z.json

**Stats**: 24 new articles found, 12 saved as raw, 8 unsaved (YouTube/paywall)

**New pages created:**
- CREATED [[entities/max-woolf]] — Max Woolf (minimaxir) — Data scientist, blogger, AI coding agent economics analyst
  - Source: [[raw/articles/minimaxir.com--2026-07-agent-quota-reset--81744d63.md]]
- CREATED [[concepts/agent-quota-resets]] — Economics of weekly quota resets by Anthropic/OpenAI for coding agent subscriptions
  - Source: [[raw/articles/minimaxir.com--2026-07-agent-quota-reset--81744d63.md]]
- CREATED [[concepts/ray]] — Open-source distributed computing framework for Python; ML infrastructure at scale
  - Sources: [[raw/articles/anyscale.com--blog-building-highly-available-and-scalable-online-applicati--7faef8c2.md]], [[raw/articles/anyscale.com--blog-online-resource-allocation-with-ray-at-ant-group--487de159.md]]

**Pages enriched:**
- ENRICHED [[entities/simon-willison]] — Added 3 new sources: AI Mania critique, Claude Code Bun-in-Rust verification, SQLite Query Explainer
  - Sources: [[raw/articles/simonwillison.net--2026-jul-19-ai-mania--44d772e4.md]], [[raw/articles/simonwillison.net--2026-jul-19-claude-code-in-bun-in-rust--2c8078d9.md]], [[raw/articles/simonwillison.net--2026-jul-18-sqlite-query-explainer--767c42a6.md]]
- ENRICHED [[concepts/coding-agents/coding-agents]] — Added Bun-in-Rust runtime infrastructure section (Claude Code v2.1.181+)
  - Source: [[raw/articles/simonwillison.net--2026-jul-19-claude-code-in-bun-in-rust--2c8078d9.md]]
- ENRICHED [[entities/anyscale]] — Updated index description with production scale details

**Unsaved articles (not AI-relevant or paywall):**
- YouTube: AI Engineer conference talks (5 videos)
- LWN.net: XZ backdoor book, kernel updates
- FT.com: Apple-OpenAI employee letters (paywall)
