# Wiki Log

_Log of all wiki changes. Newest entries at top._

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

**Created**: `comparisons/lambda-microvms-vs-agentcore.md` — AWS Lambda MicroVMs と Amazon Bedrock AgentCore の比較分析ページを作成。異なるスタックレイヤー（分離プリミティブ vs マネージドプラットフォーム）として整理し、アーキテクチャ位置付け、使用条件、競合状況を分析。

**Updated**:
- `concepts/aws-lambda-microvms.md` — 比較ページへのリンク追加
- `entities/amazon-bedrock-agentcore.md` — 比較ページへのリンク追加
- `index.md` — 比較ページを Comparisons セクションに追加

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
## [2026-06-25] OpenAI "How Agents Are Transforming Work" + Research Paper 取り込み

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

## 2026-06-29
- `concepts/evaluation/llm-as-judge` — Added BINEVAL section (Cho et al., 2026, ICML Workshop). Binary question decomposition for interpretable LLM evaluation. Raw paper + summary to `raw/papers/2026-06-25_2606.27226_*`.
- **Ingested**: NVIDIA Research blog "KV Cache Compression and Its Infra Problems" (2026-06-15). Raw article → `raw/articles/2026-06-15_nvidia-kv-cache-compression-infra-problems.md`. Created `concepts/kv-cache-compression` (survey of eviction/quantization/geometry methods + two infrastructure problems) and `concepts/triattention` (pre-RoPE geometry scoring + forward-packing compaction, ICML 2026). Updated `concepts/kv-cache` and `concepts/flash-attention-4` with cross-references. Added missing index entries for `kv-cache`, `kv-cache-compaction`, `flash-attention-4`.
