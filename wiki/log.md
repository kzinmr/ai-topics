## 2026-05-12 06:30 — Added State of Agentic Coding series (5 episodes)

**Created:**
- `concepts/state-of-agentic-coding.md` — Monthly podcast series overview (Armin Ronacher & Ben Vinegar, Dec 2025–Apr 2026)
- `entities/ben-vinegar.md` — Entity page for Ben Vinegar (@bentlegen), Modem co-founder, podcast co-host
- `raw/articles/2025-12-15_state-of-agentic-coding-ep1.md` — #1: Model Fatigue, Context Windows & LLM x86 Wars
- `raw/articles/2026-01-22_state-of-agentic-coding-ep2.md` — #2: Holiday Surge, Pricing Wars & Meta-Agentic Programming
- `raw/articles/2026-02-16_state-of-agentic-coding-ep3.md` — #3: Personal Agents, Model Wars & Death of the IDE
- `raw/articles/2026-03-12_state-of-agentic-coding-ep4.md` — #4: Newfound Powers, Side Projects & Slop Forks
- `raw/articles/2026-04-10_state-of-agentic-coding-ep5.md` — #5: Quality Crisis, AI Psychosis & Tech Disparity

**Enriched:**
- `entities/armin-ronacher.md` — Added SOC podcast section with episode table and cross-references

**Key themes documented:** model lock-in (x86 wars analogy), context window degradation, slop fork phenomenon, meta-agentic programming, subscription economics, slow-down movement, tech disparity.
## 2026-05-12 01:40 UTC — Ingest: Builders Unscripted Ep. 2 (Ashe Magalhaes)

**From**: User request (Discord). YouTube video.
**Source**: https://www.youtube.com/watch?v=flweA_I-VKE
**Created**:
- `entities/ashe-magalhaes.md` — Ashe Magalhaes entity page (Hearth AI founder, solar car racer, NASA, Airbnb ML)
- `entities/hearth-ai.md` — Hearth AI entity page (first agentic CRM, founded 2022)
- `raw/articles/2026-04-10_openai_builders-unscripted-ep2-ashe-magalhaes.md` — Raw transcript article
**Modified**: `concepts/builders-unscripted.md` (added Ep.2), `entities/romain-huet.md` (added Ep.2), `index.md`, `log.md`

## 2026-05-12 01:35 UTC — Ingest: Builders Unscripted Ep. 1 (Peter Steinberger)

**From**: User request (Discord). YouTube video.
**Source**: https://www.youtube.com/watch?v=9jgcT0Fqt7U
**Created**:
- `entities/romain-huet.md` — Romain Huet entity page (Head of Developer Experience, OpenAI; Builders Unscripted host)
- `concepts/builders-unscripted.md` — OpenAI interview series concept page
- `raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger.md` — Raw transcript article
**Modified**: `entities/peter-steinberger.md` (added Media Appearances), `entities/openclaw.md` (added Media & Press), `index.md`, `log.md`

## 2026-05-12 01:00 UTC — Manual ingest: contextmaxxing concept + Ashwin Gopinath + Sentra.app entity pages

**From**: X bookmark ingest pipeline (missed article). Original article ID: 2053533334949728256
**Source**: Ashwin Gopinath's Nanothoughts post "Memory Is State, Not a Service" (May 8, 2026)

## 2026-05-12 01:35 UTC — Ingest: OpenAI Codex Prompting Guide

**From**: User request (Discord). OpenAI Cookbook article.
**Source**: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
**Created**:
- `entities/openai-codex.md` — OpenAI Codex entity page (CLI coding agent, gpt-5.3-codex)
- `concepts/codex-prompting.md` — Codex prompting patterns (Bias for Action, metaprompting, anti-patterns)
- `raw/articles/2026-01-14_openai-codex-prompting-guide.md` — Raw article
**Modified**: `index.md` (added 2 entries), `log.md`

**New pages created**:
- `concepts/contextmaxxing.md` — Better memory over burning more tokens. Counterpart to tokenmaxxing.
- `entities/ashwingop.md` — Ashwin Gopinath: CEO/Co-founder Sentra.app, former MIT prof, Reflexion co-author
- `entities/sentra-app.md` — $5M seed EGI platform (a16z Speedrun, Together Fund)

**Pages updated**:
- `concepts/tokenmaxxing.md` — Added cross-reference to contextmaxxing in Related Concepts
- `index.md` — 3 new entries added

**Cross-references**: contextmaxxing ↔ tokenmaxxing, ashwingop ↔ sentra-app, both ↔ contextmaxxing

## 2026-05-11 23:30 UTC — X Bookmarks Ingest: Browser Use production architecture, KV Caching, 0xJeff Part V

**Bookmarks processed**: 5 total | 2 scraped from mirrors | 1 enriched existing | 1 saved raw-only | 1 metadata-only

**New pages created**:
- `concepts/browser-use-production-architecture.md` — SQS-to-Lambda architecture for running Browser Use agents at scale (Larsen Cundric, 4,000+ commits)

**Enriched existing pages**:
- `concepts/kv-cache.md` — Added Avi Chawla source ("KV Caching in LLMs, Explained Visually", Feb 2025), "first token is slow" explanation, memory cost table per model
- `entities/0xjeff.md` — Added Part V: Three-Layer Agent Stack (Identity/Knowledge/Tools) + Model Configuration (Opencode Go, DeepSeek API, config.yaml/.env)
- `entities/browser-use.md` — Added Larsen Cundric as key person, production architecture blog post, cross-link to new concept page

**Raw articles saved** (5):
- `2026-05-09_browser-use_production-architecture.md` (browser-use.com mirror)
- `2025-02-14_dailydoseofds_kv-caching-explained.md` (Daily Dose of Data Science mirror)
- `2026-05-08_nanothoughts_memory-is-state.md` (Ashwin Gopinath, memory architecture)
- `2026-05-11_defi0xjeff_hermes-analyst-workflow.md` (0xJeff Part V mirror)
- `2026-05-08_shannholmberg_ai-content-system.md` (metadata-only, content marketing)

**Skipped**:
- Shann³ content system article — content marketing, not core AI/LLM scope → metadata-only
- Ashwin Gopinath "Contextmaxxing > Tokenmaxxing" — X article mirrors to "Memory Is State, Not a Service" (May 8), saved raw only
## 2026-05-11 22:45 UTC — Reuters Article: OpenAI/Anthropic JVs adopt Palantir Model

**Article**: [Reuters: OpenAI, Anthropic ventures in talks to buy AI services firms](https://www.reuters.com/world/openai-anthropic-ventures-talks-buy-ai-services-firms-sources-say-2026-05-05/) — Milana Vinn, May 5, 2026. Already ingested as `raw/articles/2026-05-05_reuters-openai-anthropic-jv-acquisitions.md`.

**Pages updated**:
- `concepts/ai-services-joint-ventures.md` — Major expansion: added "The Palantir Playbook" section with 3-way comparison table (Palantir vs OpenAI DC vs Anthropic JV), Reuters M&A details (3 acquisitions in advanced stages), Jon Gray quotes, explicit Palantir model framing. Tags: palantir-model, m-and-a.
- `entities/palantir.md` — New section "The Palantir Model Goes Global (May 2026)": Reuters quote validating Palantir's embed-engineers playbook as industry standard. Competitive positioning analysis. Cross-referenced to `concepts/ai-services-joint-ventures`.
- `entities/openai.md` — Fixed broken ref `enterprise-ai-deployment-jv` → `ai-services-joint-ventures`.
- `entities/anthropic.md` — Fixed broken ref `enterprise-ai-deployment-jv` → `ai-services-joint-ventures`.

**Key insight**: The approach "mirrors Palantir's model of embedding engineers inside customers' operations" — the AI industry spent 2023–2025 pursuing API-first, and is now capitulating to the labor-intensive, high-touch services model Palantir has been practicing for 20 years.

## 2026-05-11 22:30 UTC — X Accounts Scan: FlashAttention-4, Delphi scaling laws, Interaction Models, folk

**Scan summary**: 79 tracked accounts, 12 scanned, 7 new posts detected. 4 major wiki actions taken.

**New pages created**:
- `concepts/flash-attention-4.md` — FA4: Blackwell B200 optimized CUDA kernel. 1605 TFLOPs/s (71% util), 1.3x vs cuDNN. Async pipeline, hybrid exp, conditional softmax rescaling. Tri Dao (Together AI/Princeton).
- `concepts/delphi-scaling-laws.md` — Open Athena (Marin) scaling suite. 300x extrapolation (3e20→1e23 FLOPs) within 0.2%. Token-horizon LR correction, AdamH optimizer. Open checkpoints + recipe.
- `concepts/interaction-models.md` — Thinking Machines Lab research preview. 200ms micro-turn, multi-modal native interaction (audio/video/text). Two-model split architecture (real-time + async background).
- `entities/folk-app.md` — Nozomio Labs personal AI agent. iMessage/Telegram/Discord. 24/7, persistent memory. $20-100/mo.

**Enriched existing pages**:
- `entities/charles-frye.md` — Added FA4 reverse-engineering blog post (Modal, Sept 2025, HN front page, GPU MODE presentation)
- `entities/elie-bakouch.md` — Updated to "formerly at Hugging Face" (per X post); added scaling/open-source/training tags

**Raw articles saved** (6):
- `2026-04-14_openathena_delphi-scaling-laws.md`
- `2026-05-11_thinkingmachines_interaction-models.md`
- `2026-03-05_togetherai_flashattention-4.md`
- `2025-09-26_modal_reverse-engineer-flashattention-4.md`
- `2026-05-11_getfolk_folk-app.md`
- `2026-05-06_anthropic_higher-limits-spacex.md`

**Skipped**: Elie Bakouch alphaxiv.org reply (no article), Eugene Yan Anthropic+SpaceX (minor news, saved raw only)

## 2026-05-11 19:00 UTC — Daily Skeleton Enrichment Run (no skeleton pages found; enriched 2 stubs)

**Status**: No `status: skeleton` entity pages found. Enriched 2 `status: stub` entity pages as fallback.

**Pages enriched**:
- `entities/aditya-bawankule.md` — Expanded from stub (960B) to full entity page (6.3KB). Added: professional background (UIUC CompE, Meta/Supernatural VR, AIdea Hub founder, Certivo), projects (VibeCoder, DreamPixelForge, NeuroNav), writing style analysis, detailed blog post summaries (Codex /goal meta-prompting, Claude Code vs Codex vs Cursor comparison), cross-references. Sources added from website, resume, LinkedIn, GitHub. Removed `status: stub`.
- `entities/hoeem.md` — Expanded from stub (1.2KB) to enriched entity page (2.8KB). Added: platform details (169K followers, Seven c Newsletter on crypto), content domains (crypto trading + Claude education), professional context (primarily crypto-focused with a viral Claude Architect guide). Sources added from X profile and Substack. Retained `status: stub` due to limited non-crypto content available.

**Index updates**: Both entities already present in index.md and entities/_index.md — no description changes needed.

## 2026-05-11 17:51 UTC — Cloudflare Email Sending wiki ingestion (levelsio posts)

**Pages created**:
- `entities/levelsio.md` — Pieter Levels (@levelsio), indie maker ($250K+/mo portfolio), build-in-public pioneer. Cloudflare Email Sending price comparison, migration prompt.
- `concepts/cloudflare-email-sending.md` — Cloudflare Email Service (beta, April 2026). REST API + Workers bindings. Pricing comparison (Postmark $1,206 → Cloudflare $354/mo at 1M emails). Domain setup, limitations, AI agent relevance.

**Raw articles saved**:
- `wiki/raw/articles/2026-05-10_levelsio_cloudflare-email-sending-feature.md`
- `wiki/raw/articles/2026-05-10_levelsio_cloudflare-email-migration-prompt.md`

**SCHEMA.md**: Added `cloudflare`, `indie-maker`, `email` tags to canonical taxonomy.

**Source**: User request via Discord to ingest Cloudflare Email Sending knowledge + assess Hermes email integration feasibility.
## 2026-05-11 17:35 — Wiki watchdog auto-fix (index header correction)
- 📝 `index.md`: Concepts header count corrected (1306→1238) to match actual filesystem count
- 📊 Verifications: pipe corruption (0), triple bracket (0), line-number corruption (0) — all clean
- ⚠️ Needs attention: x_accounts stale alert (26h), 148 non-standard tags, 275 orphan pages

## 2026-05-11 15:45 — Tambo と Buildy の新規エンティティページ作成

- 🆕 `entities/tambo.md` 作成 (L2) — オープンソース Generative UI ツールキット for React。Michael Magán & Michael Milstead (Seattle, 2024設立)。Zapier/Rocket Money/Solink 採用。SCHEMA.md に `generative-ui` タグ追加。
- 🆕 `entities/buildy.md` 作成 (L2) — AIエージェントがパーソナルWebアプリを構築・永続化するプラットフォーム。ES module POST → 公開URL + KVストレージ。MCP経由で全エージェント対応。llms.txt/llms-full.txt でAI向けドキュメント完備。
- `SCHEMA.md`: Products カテゴリに `generative-ui` タグ追加
- `index.md`: Entities (551→553), Total pages (1749→1751)
## 2026-05-11 14:53 UTC — Claude Certified Architect 5-Domain Knowledge ingested from @hooeem X Article

**Source**: X Article by @hooeem — "I want to become a Claude architect (full course)" (60K bookmarks, 16.7K likes)

### Created
- [[concepts/claude-certified-architect-domains]] — Comprehensive exam knowledge for all 5 domains
- [[entities/hoeem]] — Author entity (stub, 169K+ followers)
- `raw/articles/2026-03-15_hooeem_claude-certified-architect-full-course.md` — Raw article saved

### Updated
- [[concepts/subagents]] — Added Claude Agent SDK hub-and-spoke orchestration, isolation principle, Task tool, fork_session, narrow decomposition failure
- [[concepts/claude-code-best-practices]] — Added CLAUDE.md 3-level hierarchy, path-specific rules (.claude/rules/), cross-reference to exam domains

### Key Knowledge Diffs from Existing Wiki
- **Agentic loop stop_reason mechanics** & 3 exam anti-patterns — not previously covered at API level
- **Hub-and-spoke isolation principle** — subagents don't inherit coordinator context
- **PostToolUse hooks vs tool call interception hooks** — distinct SDK mechanisms
- **Programmatic enforcement decision rule**: financial/security/compliance → hooks (not prompts)
- **Task decomposition**: sequential vs adaptive, attention dilution problem
- **Session management**: --resume, fork_session, fresh start with stale context problem
- **Tool descriptions** as primary selection mechanism, tool_choice options (auto/any/forced)
- **CLAUDE.md 3-level hierarchy**: user/project/directory, path-specific rules with glob patterns
- **Prompt engineering**: "be explicit" principle, few-shot with reasoning, nullable schemas, Batches API
- **Context management**: progressive summarisation trap, lost in middle, escalation triggers (valid vs unreliable), structured error propagation, information provenance
---
## 2026-05-11 14:45 UTC — Agent Ergonomics (Wes McKinney) ingested

**Source**: Wes McKinney blog (wesmckinney.com, Jan 2026)

### Pages Created
- `entities/wes-mckinney.md` — pandas creator, Apache Arrow co-creator, Principal Architect at Posit. Creator of roborev.
- `concepts/agent-ergonomics.md` — Programming language design principles optimized for AI coding agents. Go/Rust > Python for agentic loops.

### Raw Articles Saved
- `raw/articles/2026-01-20_wesmckinney_agent-ergonomics.md`

### Key Insights
- **Human ergonomics matters less**: When agents are primary authors, compile speed, distribution, and runtime > readability
- **Go has edge over Rust**: Ultrafast compile times for agentic iteration loops (agents compile 10-100x more than humans)
- **Four-layer stack model**: Durable value in compute/data layers (1-2), not language bindings (3-4)
- **roborev as force multiplier**: Automated code review essential when agents write in languages humans don't know well
- **Python not dying, era ending**: Python transitions to exploration/orchestration layer

## 2026-05-11 14:15 UTC — Agent Memory Engineering ingested

**Source**: Nicolas Bustamante blog (nicolasbustamante.com, 34 min read)

### Pages Created
- `concepts/agent-memory-engineering.md` — Comprehensive analysis of Claude Code/Codex/Hermes memory architectures

### Pages Enriched
- `entities/nicolas-bustamante.md` — Updated with Microsoft role, Agent Memory Engineering analysis, Fintool/Doctrine background

### Raw Articles Saved
- `raw/articles/2026-05-01_nicolas-bustamante_agent-memory-engineering.md`

### Key Insights
- **Every clever architecture lost**: vector DBs, knowledge graphs, dedicated memory agents — all lost to LLM + markdown + bash
- **Models are post-trained on their harness**: memory is not portable between agents
- **Three architectures**: Bounded Snapshot (Hermes), Two-Phase Async Pipeline, Typed Live Writes (Claude Code)
- **Five design questions**: storage format, load strategy, write discipline, signal gate, cold start
- **Cold start is unsolved**: no standard for bootstrapping agent memory from user data
## 2026-05-11 13:30 UTC — X Bookmarks Ingest Recovery (3 failed articles retried)

**Source**: x-bookmark-ingest retry — 3 articles from 2026-05-11 run that failed mirror discovery

### Pages Created (5 new)
- `entities/jaya-gupta.md` — Foundation Capital partner, organizational moat theory, Context Graphs
- `entities/tobi-lutke.md` — Shopify CEO, River AI agent (Slack-native coding agent)
- `entities/nrehiew.md` — wh (@nrehiew_), distributional view of post-training
- `concepts/organizational-moat.md` — Jaya Gupta's theory: company shape as last durable AI moat
- `concepts/post-training-distributional-view.md` — Distributional comparison of SFT vs RL vs OPD

### Raw Articles Saved (3)
- `2026-05-10_nrehiew_sft-rl-opd-distributional-lens.md`
- `2026-05-09_tobi-lutke_learning-on-the-shop-floor.md`
- `2026-05-08_jaya-gupta_next-biggest-moat-in-ai.md`

### Key Discoveries
- Jaya Gupta: 3.2M-view X Article on organizational moat — company structure as un-copyable advantage
- Tobi Lutke: Shopify's River — internal AI agent in Slack built on apprenticeship model (2M views)
- wh/nrehiew: Distributional lens on post-training — elegant mental model for SFT/RL/OPD tradeoffs (181K views)
## [2026-05-11] create | X bookmarks ingest — 3 concept pages, 2 entity pages, 6 raw articles

- 🆕 [[concepts/claude-md-rules]] — Karpathy's CLAUDE.md behavioral guidelines for AI coding agents (4→12 rules, 41%→3% mistake rate). 120K+ GitHub stars. Behavioral constraints over feature checklists.
- 🆕 [[concepts/probabilistic-engineering]] — Tim Davis (Modular) on the paradigm shift from deterministic to probabilistic software engineering. Core asymmetry: generation is cheap, validation is not. 24-7 employee concept, role fragmentation, Jevons paradox applied to code.
- 🆕 [[concepts/open-swe]] — LangChain's open-source internal coding agent framework (MIT). Distills Stripe Minions/Ramp Inspect/Coinbase Cloudbot convergent architecture. Deep Agents + LangGraph, AGENTS.md context engineering, cloud sandboxes.
- 🆕 [[entities/tim-davis]] — Modular executive, Compound Loop creator, probabilistic engineering concept originator.
- 🆕 [[entities/forrest-chang]] — Creator of andrej-karpathy-skills repo — converted Karpathy's LLM coding observations into 4 CLAUDE.md rules.

**Raw articles saved** (6):
- 2026-04-16_timdavis_probabilistic-engineering-24-7-employee.md (full mirror, 10K chars)
- 2026-03-17_langchain_open-swe-framework.md (full mirror)
- 2026-05-09_mnilax_claude-md-12-rules.md (X Article, metadata-only — auth-walled)
- 2026-05-09_unknown_learning-on-the-shop-floor.md (metadata-only)
- 2026-05-08_unknown_next-biggest-moat-in-ai.md (metadata-only)
- 2026-05-10_unknown_sft-rl-on-policy-distillation.md (metadata-only)

- [[index]] — Added 3 concepts (claude-md-rules, open-swe, probabilistic-engineering) and 2 entities (tim-davis, forrest-chang). Total 1743→1748.
## [2026-05-11] manual | Parallel Web Systems — Automated Competitor Analysis with AI Agents

- **新規:** `wiki/raw/articles/2026-04-17_parallel_automated-competitor-analysis.md` — How to automate competitor analysis with AI agents: Discover → Extract → Monitor パイプライン
- **新規:** `wiki/concepts/automated-competitor-analysis.md` — 競合分析自動化の概念ページ。3段階パイプライン、シグナル分類、Build vs Buy判断
- **更新:** `wiki/entities/parallel-web-systems.md` — Key Articlesに追加
- **ソース:** parallel.ai/articles/how-to-automate-competitor-analysis-with-ai-agents

## [2026-05-11] manual | Postman 2025 State of the API Report — AI-Ready APIs concept

- **新規:** `wiki/raw/articles/2025-10-08_postman-state-of-api-2025-report.md` — Postman第7回年次APIレポート。5,700人以上の開発者・アーキテクト・エグゼクティブ対象。AI-APIギャップ（89%がAI使用、24%のみがAIエージェント向けAPI設計）、MCP認知度（70%）と採用（10%）のギャップ、API収益化（65%の組織がAPIから収益）を分析。
- **新規:** `wiki/concepts/ai-ready-apis.md` — AI-Ready APIs概念ページ。AIエージェントをAPI消費者として想定した設計原則：機械可読スキーマ、エージェント認識セキュリティ、コントラクトテスト。API-Firstと収益の相関分析を含む。
- **更新:** `wiki/concepts/mcp.md` — MCPページにPostman調査の認知度・採用ギャップデータ（70%認知/10%日常使用）とPostmanプラットフォームのAIトラフィック分析（OpenAI 56%, Llama 6.9x成長）を追加。
- **ソース:** postman.com/state-of-api/2025/

## [2026-05-11] manual | Parallel Web Systems articles — Bing API & Google Alerts alternatives

- **新規:** `wiki/raw/articles/2026-02-16_parallel_bing-api-alternatives.md` — Bing API alternatives comparison (Parallel Search, Exa AI, SerpAPI, Tavily)
- **新規:** `wiki/raw/articles/2026-04-17_parallel_google-alerts-alternatives.md` — Google Alerts alternatives guide for developers & marketers
- **新規:** `wiki/comparisons/bing-api-alternatives-2026.md` — Comparison page: 4 Bing Search API alternatives
- **新規:** `wiki/comparisons/google-alerts-alternatives-2026.md` — Comparison page: 10 Google Alerts alternatives across 2 categories
- **新規:** `wiki/entities/parallel-web-systems.md` — Company entity page (Search/Monitor/Extract APIs, SOC 2, ZDR, founded 2023)
- **ソース:** parallel.ai/articles/bing-api-comparison, parallel.ai/articles/the-best-google-alerts-alternatives-in-2026-including-one-built-for-developers

## [2026-05-11] active-crawl | NVIDIA Nemotron 3 Nano Omni, GPT-5.5 Instant, Gemma 4 MTP, Anthropic Petri/NLA/Meridian Labs, IBM Think 2026

- **作成:** `wiki/raw/articles/2026-04-28_nvidia_nemotron-3-nano-omni.md` — NVIDIA unified multimodal MoE model (30B-A3B), video/audio/image/text, open-source
- **作成:** `wiki/raw/articles/2026-05-05_openai_gpt-5-5-instant.md` — Updated ChatGPT default model, 52.5% fewer hallucinations, self-correction
- **作成:** `wiki/raw/articles/2026-05-05_google_gemma-4-mtp.md` — Multi-Token Prediction drafters for 3x faster Gemma 4 inference
- **作成:** `wiki/raw/articles/2026-05-08_anthropic_petri-nla-interpretability.md` — Natural Language Autoencoders + Petri 3.0 donation to Meridian Labs
- **作成:** `wiki/raw/articles/2026-05-05_ibm_think-2026-ai-operating-model.md` — IBM's four-pillar enterprise AI operating model
- **作成:** `wiki/entities/gpt-5-5-instant.md` — OpenAI GPT-5.5 Instant entity page
- **作成:** `wiki/entities/gemma-4.md` — Google Gemma 4 entity page with MTP speedup details
- **作成:** `wiki/entities/meridian-labs.md` — Independent AI evaluation nonprofit, Petri steward
- **更新:** `wiki/entities/gemma-4.md` — MTP drafter section, 60M+ downloads, speculative decoding context
- **作成:** `wiki/concepts/natural-language-autoencoders.md` — Anthropic interpretability technique, activation→text→reconstruction
- **作成:** `wiki/concepts/petri-alignment.md` — Anthropic's open-source safety evaluation tool, donated to Meridian Labs
- **作成:** `wiki/concepts/enterprise-ai-operating-model.md` — IBM Think 2026 four-pillar framework (Agents/Data/Automation/Hybrid)
- **ソース:** developer.nvidia.com, openai.com, blog.google, hipther.com (AI Dispatch), newsroom.ibm.com
- **重複除去:** `entities/nvidia-nemotron-3.md` 削除（既存の `entities/nvidia-nemotron-3-nano-omni.md` と重複）

## [2026-05-11] manual | Garry Tan Meta-Meta-Prompting X Article 取り込み

- **新規:** `wiki/raw/articles/2026-05-09_garrytan_meta-meta-prompting.md` — Garry Tan (YC CEO) の X Article。ABMedia の中国語要約から再構成。Fat Skills, Fat Code, Thin Harness、Skillify、100+ skills + 100K pages personal AI OS。
- **新規:** `wiki/concepts/meta-meta-prompting.md` — AI agent 設計哲学の概念ページ。複利効果、マルチモデルルーティング、Hermes Agent との対応関係を含む。
- **新規:** `wiki/entities/garry-tan.md` — YC CEO の人物ページ。Posterous、Initialized Capital、G Stack、AI builder としての側面。
- **ソース:** ABMedia (https://abmedia.io/garry-tan-meta-meta-prompting), xurl メタデータ, web_extract プレビュー

## [2026-05-11] blog-wiki-ingest | Meta employee keystroke data collection (ATA/MCI)

- **更新:** `wiki/entities/meta.md` — Agent Transformation Accelerator (ATA) / Model Capability Initiative (MCI) セクション追加。2026年4月より米国従業員のマウス操作・キーストローク・スクリーンショットをAIエージェント訓練用に収集。Andrew Bosworth CTO のビジョン、プライバシー懸念、組織的文脈（10%レイオフ）を含む。
- **ソース:** Reuters (Katie Paul, Jeff Horwitz), 2026-04-21
- **全14件中:** take=0, skip=13（同日早朝blog-ingestで既処理5件、AI非関連8件）, reference=1（Meta記事→entities/meta.md更新）

## [2026-05-11] newsletter-wiki-ingest | The Signal + Superintel — Colossus deal, Anthropic/OpenAI updates, Jim Fan + AI governance

- **更新:** `concepts/xai-anthropic-colossus-deal.md` — Colossus 2 詳細（1.5GW/550K GPUs）、経済分析（$5B→$15B）、Anthropic 利用者への直接恩恵（レート制限2倍/ピーク時制限撤廃）、軌道コンピュート計画 の4セクション追加
- **更新:** `entities/anthropic.md` — Code w/ Claude 2026 新発表: M365 GA（Excel/PPT/Word GA, Outlook beta）、Dreaming research preview、金融テンプレート、$50B調達/$1T評価額、計算資源パートナーシップ全体像（SpaceXAI/Amazon/Google/Microsoft/Fluidstack）を追加
- **更新:** `entities/openai.md` — May 2026 新製品: GPT-Realtime-2（音声推論/70+言語翻訳/ストリーミング文字起こし）、Codex ブラウザプラグイン（Chrome/macOS/Windows）、MRC オープンソース化（OCP経由、NVIDIA/AMD/Broadcom/Intel/Microsoft共同開発）を追加
- **更新:** `entities/jim-fan.md` — Sequoia講演（May 2026）: Dexterity scaling laws、2.1万時間人間視点映像、ロボットデータ0.1%未満、Internet-scaleデータ不足課題 を追加
- **更新:** `concepts/agentic-ai-governance.md` — 「Trustworthy AI = Delegated Agency」フレームワーク: Control→Delegationパラダイムシフト、5次元対比表、業界動向との接続（Anthropic/OpenAI/StrongDM）、Open Questions を追加
- **作成:** `raw/articles/2026-05-06_xai_anthropic-compute-partnership.md`, `raw/articles/2026-05-06_anthropic_higher-limits-spacex.md`
- **ソース:** x.ai/news, anthropic.com/news, The Signal (Alex Banks), Superintel+ (getsuperintel.com)
## [2026-05-11] blog-ingest | Gary Marcus entity, Sean Goedecke enrichment, Enterprise AI Scaling concept, Simon Willison updates

- **作成:** `wiki/entities/gary-marcus.md` — Cognitive scientist, AI critic. METR 50%-time-horizon critique, "Misplaced panic over AI progress" (May 2026). Reliability vs capability, neurosymbolic AI advocacy.
- **更新:** `wiki/entities/seangoedecke-com.md` — "The left-wing case for AI" 記事追加。Disability rights, healthcare access, class mobility, educational equity, techno-utopianism の5つの論点。
- **作成:** `wiki/concepts/enterprise-ai-scaling-patterns.md` — OpenAI 企業インタビューに基づく5つのパターン: Culture Before Tooling, Governance as Enabler, Ownership Over Consumption, Evaluation Rigor, Protecting Judgment Work.
- **更新:** `wiki/entities/simon-willison.md` — 2026-05-10 記事追加 (NYT AI-generated quote incident, Andrew Quinn wheel-reinvention quote)
- **ソース:** garymarcus.substack.com, seangoedecke.com, openai.com, simonwillison.net

## [2026-05-11] cleanup | 6 stub/低品質ページを削除、2つの統合先に集約

- **eval-tools-comparison 統合:** `concepts/ai-eval-tools-comparison.md` + `concepts/eval-tools-comparison.md` (両方スタブ) → `comparisons/eval-tools-comparison.md` に moved_from 追加、参照4件修正
- **hermes-vs-openclaw 統合:** `concepts/openclaw-vs-hermes-architecture-comparison.md` + `concepts/hermes-agent-vs-openclaw-architecture-comparison.md` (両方スタブ) → `comparisons/hermes-vs-openclaw-architecture.md` に moved_from 追加
- **削除:** `concepts/local-llm-models-comparison-open-weights-moe-hardware-vram.md` (スタブ、異常なタイトル)
- **削除:** `concepts/dspy-comparisons.md` (低品質、参照5件→ `concepts/dspy.md` に振替)

## [2026-05-11] merge | concepts/agent-harness-comparison.md + comparisons/coding-agent-harnesses.md → comparisons/agent-harnesses.md

- **統合:** `concepts/agent-harness-comparison.md` (404行, 本文) + `comparisons/coding-agent-harnesses.md` (22行, リダイレクト) → `comparisons/agent-harnesses.md`
- **削除:** 元の2ファイルを削除
- **参照修正:** `[[concepts/agent-harness-comparison]]` 全参照 → `[[comparisons/agent-harnesses]]` (entities x8, concepts x2, index.md)
- **参照修正:** `[[comparisons/coding-agent-harnesses]]` → `[[comparisons/agent-harnesses]]` (index.md)
- **更新:** frontmatter に `moved_from` 追加、`type: comparison`、内部の循環参照を除去

## [2026-05-11] move | concepts/comparisons/agent-sandboxing.md → comparisons/agent-sandboxing.md

- **移動:** `wiki/concepts/comparisons/agent-sandboxing.md` → `wiki/comparisons/agent-sandboxing.md`
- **撤廃:** `wiki/concepts/comparisons/` ディレクトリを削除（空ディレクトリ）
- **更新:** フロントマターに `moved_from` 追加、related pages に main concept page へのリンク追加

## [2026-05-11] create | blog/2026-05-11_hermes_simulacrum-of-intellectual-consumption

- **作成:** `blog/2026-05-11_hermes_simulacrum-of-intellectual-consumption.md` — 知的摂取のシミュラークル化を論じたブログ記事。Wiki構築の実体験から出発し、代理指標の崩壊、裁定取引＋情報流通量の加速、Insight Pornの射倖心メカニズム、Baumol効果による検証価値の高騰、Wikiパラドックスへのプラグマティックな立場、そしてシミュラークルの中でなお検証と行動を埋め込む実践まで。
- **参照:** [[concepts/baudrillard-and-ai]], [[concepts/simulacrum-of-knowledge-work]], Ian Yang, filfre.net

## [2026-05-11] create | concepts/rao-recursive-agent-optimization + entities/apurva-gandhi

- **作成:** `wiki/concepts/rao-recursive-agent-optimization.md` — RAO (Recursive Agent Optimization): CMU × Amazon AGI Labs による再帰的エージェントの end-to-end RL 訓練手法。Qwen3-4B-Instruct を75ステップ訓練するだけで deep research タスクで単一エージェント比 +16% SR。
- **作成:** `wiki/entities/apurva-gandhi.md` — Apurva Gandhi: CMU PhD 学生（Graham Neubig 指導）。元 Microsoft Copilot 基盤設計。RAO、Go-Browse、SkillWeaver の著者。
- **保存:** `wiki/raw/papers/2026-05-07_2605.06639_recursive-agent-optimization.md` — RAO 論文 (arXiv:2605.06639)
- **保存:** `wiki/raw/articles/2026-05-08_x-thread_apurva-gandhi-rao-recursive-agent-optimization.md` — Apurva Gandhi の X スレッド (1/10〜10/10)
- **参照:** [[concepts/recursive-language-models]], [[concepts/grpo]], [[concepts/rlm-recursive-language-models]]
## [2026-05-11] create | concepts/baudrillard-and-ai — ボードリヤールとAI

- **作成:** `wiki/concepts/baudrillard-and-ai.md` — ボードリヤールの『シミュラークルとシミュレーション』の概念枠組み（イマージュの4段階、ハイパーリアリティ、シミュラークルの先行）をLLM時代のAI現象に適用した概念ページ。AIは模倣の失敗ではなくシミュラークルの完成形であるという視点。
- **保存:** `wiki/raw/articles/2025-05-10_ian-yang-welcome-to-the-token-of-the-real.md` — Ian YangのLLM記号論分析
- **参照:** filfre.net（直接のボードリヤール言及）, onehappyfellow (Simulacrum of Knowledge Work), 関連概念: waluigi-effect, linguistic-vertigo, illusion-of-thinking, societal-shadow, cognitive-debt
- **更新:** `wiki/index.md` — Concepts セクションに baudrillard-and-ai を追加、カウント更新

## [2026-05-11] dedup | wiki/raw/papers/ 重複除去・命名統一・dedup 機構導入

- **重複除去:**
  - `2512.24601-recursive-language-models-{rlms,rlm,mit}.md` → unified to `2025-12-31_2512.24601_recursive-language-models.md`
  - `2507.19457-gepa-{iclr2026,reflective-prompt-evolution}.md` → unified to `2025-07-25_2507.19457_gepa-reflective-prompt-evolution.md`
- **参照先修正:** `wiki/concepts/gepa.md`, `wiki/concepts/rlms.md`, `wiki/concepts/recursive-language-models.md` の sources を canonical path に統一
- **Dedup 機構:** `scripts/papers_index.py` 導入（`.papers_index.json` で arXiv ID → ファイル名マッピング。`--check` / `--add` / `--build`）
- **命名規則明文化:** `raw-article-filename-policy` skill に `{YYYY-MM-DD}_{arxiv-id}_{short-title}.md` ルール追加

## [2026-05-10] ingest | Dreaming — Addy Osmani Agent Harness Engineering + entity page
- **Raw article**: raw/articles/2026-05-09_addyosmani-agent-harness-engineering.md
- **Updated**: [[concepts/harness-engineering]] — Added Addy Osmani's Agent = Model + Harness framework section (The Ratchet, Working Backwards from Behavior, Context Rot, Long-Horizon Execution, Harnesses Don't Shrink, They Move, Claude Code architecture)
- **Created**: [[entities/addy-osmani]] — Google Cloud AI director, Chrome DevTools lead, open-source author
- **Note**: dreaming-group pre-run script failed JSON parse; recovered via blog_ingest triage. deepseek-v4 (Together AI), nvidia-dynamo, agent-development-lifecycle already covered by other pipelines.

## [2026-05-10] watch | Watchdog fix — SCHEMA.md pipe-table corruption
- **SCHEMA.md line 36**: `|- **Engineering**:...` → `- **Engineering**:...` (pipe prefix removed)
- **Root cause**: Previous agent patch introduced `|-` prefix when editing SCHEMA.md tag section
- **Remaining issues** (not auto-fixable):
  - 941 pages (54.6%) not indexed in index.md
  - 1,314 broken wikilinks (many raw/articles/ refs, missing entities/concepts)
  - 250 non-canonical tags (needs tag normalization batch)
  - 73 pages with missing frontmatter
  - 385 orphan pages (133 stubs, 252 non-stubs)
  - 3 date-prefixed filenames in concepts/

## [2026-05-10] ingest | X bookmarks — ADLC (Harrison Chase) + Codex /goal meta-prompting
- **Raw articles**: 2 new
  - `raw/articles/2026-05-04_adityabawankule-codex-goal-meta-prompting.md` — Aditya Bawankule on meta-prompting Codex /goal for days of autonomous work
  - `raw/articles/2026-05-09_langchain-agent-development-lifecycle.md` — Harrison Chase (LangChain) canonical ADLC framework
- **New pages**:
  - `concepts/codex-goal-meta-prompting.md` — technique for using a second AI to generate high-quality /goal prompts for Codex CLI v0.128.0
  - `entities/aditya-bawankule.md` — stub entity for the technical blogger
- **Enriched pages**:
  - `concepts/agent-development-lifecycle.md` — Merged Harrison Chase's Build→Test→Deploy→Monitor framework (authoritative source) with existing Salesforce operational roles. Added Governance layer, three-layer Build taxonomy (frameworks/runtimes/harnesses), Test/Deploy/Monitor/Iterate details.
  - `entities/harrison-chase.md` — Added ADLC article source, updated description to credit ADLC framework, bumped updated date to 2026-05-10
- **Bookmarks**: 2 X native articles → both found public mirrors (adityabawankule.io, langchain.com)
## [2026-05-10] lint | Daily health check — fixed triple brackets, case mismatches, header counts; 941 pages missing from index
- **CRITICAL**: Triple bracket `[[[` corruption on 11 index entries (lines 580-583, 610-616) — FIXED
- **CRITICAL**: Index entry `[[concepts/claris-filemaker-agentic-coding]]` pointed to wrong directory (file is in entities/) — FIXED
- **FIXED**: Case mismatch `[[concepts/mooncake]]` in meta-capacity-efficiency-agents.md → `[[concepts/Mooncake]]`
- **WARNING**: 941 out of 1725 pages (54.6%) NOT indexed in index.md — critical gap
- **WARNING**: 1314 broken wikilinks (file not found), 250 non-canonical tags, 73 pages with missing frontmatter
- **WARNING**: 385 orphan pages (133 stubs, 252 non-stubs)
- **WARNING**: 3 date-prefixed filenames in concepts/ violate naming convention
- **WARNING**: Header count discrepancy fixed: was 1844 reported, 1725 actual
- **INFO**: Index corruption (line-number, pipe-table): CLEAN
- **INFO**: Log structure: CLEAN (9 entries, no duplicate headers)

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-10] ingest | Active crawl — 5 topics from trending AI/ML (May 2026)
- **Raw articles**: 5 new
  - `raw/articles/2026-05-07_arxiv-federation-of-experts.md` — FoE: distributed MoE inference (arXiv:2605.06206)
  - `raw/articles/2026-05-04_importai-automating-ai-research.md` — Jack Clark's Import AI 455
  - `raw/articles/2026-05-06_google-flow-music-believe.md` — Google Flow Music + Believe partnership
  - `raw/articles/2026-05-07_google-alphaevolve-real-world.md` — AlphaEvolve real-world impact
  - `raw/articles/2026-05-06_coder-self-hosted-agents-beta.md` — Coder Agents beta press release
- **New pages**:
  - `concepts/federation-of-experts.md` — FoE architecture for communication-efficient distributed MoE inference
  - `entities/coder.md` — Coder Technologies, self-hosted model-agnostic coding agent platform
  - `concepts/google-flow-music.md` — Google Labs AI music creation (Lyria 3 Pro + Believe)
- **Updated pages**:
  - `concepts/alphaevolve.md` — Added May 2026 real-world deployment blog source, bumped updated date
  - `entities/jack-clark.md` — Bumped updated date (Import AI 455 content already present)
- **Topics**: Federation of Experts (distributed MoE inference), Coder Agents (self-hosted enterprise), Google Flow Music (AI music), AlphaEvolve update, Import AI 455 (automated AI R&D forecast)

## [2026-05-10] ingest | Superintel newsletter — Alex Karp/Palantir Q1 2026 article
- **Raw article**: raw/newsletters/2026-05-09-the-man-who-studied-power-and-then-built-it-alex-karp-palantir-and-the-technolog.md
- **Source**: Superintel newsletter (Kim "Chubby" Isenberg), beehiiv platform
- **Updated**: [[entities/palantir]] — Added Q1 2026 financial performance section ($1.63B revenue, +84% U.S. government growth, Maven elevated to permanent Pentagon program), founding history with In-Q-Tel/CIA seed connection, Alex Karp's Frankfurt School critical theory academic background
- **Triage decision**: ★★★★☆ (take - existing page update) — existing page had architecture coverage but lacked financial/leadership context
## [2026-05-09] rotate | Rotated log-2026.md (1158 lines → log-2026.md appended)
- Previous entries archived to log-2026.md
- Fresh log.md initialized

## [2026-05-09] watch | Watchdog fix — log.md duplicate header removed
- Removed duplicate header section (13 lines) from log.md rotation artifact
- Fixed extra blank line

## [2026-05-09] lint | Wiki health check — 3 CRITICAL, 12 WARNING issues found

### Fixes Applied
- **Index dedup**: Removed 2 duplicate entries (mitchell-hashimoto-ghostty, mitchell-hashimoto-hashicorp)
- **Index corruption**: Fixed pipe-table corruption (4 lines normalized)
- **Log rotation**: Rotated log.md (1158 lines → archived to log-2026.md, fresh log initialized)
- **Header counts**: Updated index.md header (Total: 1828, Entities: 531, Concepts: 1272, Comparisons: 13, Events: 2)

### Critical Issues
- 415 pages with broken outbound wikilinks
- 271 broken outbound wikilinks total (mostly concept/entity pages missing)
- 313 orphan pages (no inbound links)
- 128 stale pages (not updated in 90+ days)
- 734 pages (40%) with no sources field
- 349 tags not in SCHEMA.md taxonomy
- 16 composite kebab-case tags detected

### Warnings
- 1,828 total pages, only 762 indexed (58% index coverage gap)
- Concepts section: 1,272 files vs 209 index entries (84% unindexed)
- Subdirectory pages (fine-tuning/, harness-engineering/, etc.) not indexed

### Unactionable Broken Links
- 1 broken link in concepts/agentic-coding.md → `spec-driven-development` (no type prefix)
- Multiple back-links between paired pages (e.g., claris-filemaker ↔ agentic-coding)

### Tag Audit Summary
- Most common missing tags: coding-agents, software-development, workflow, testing
- Composite tags detected: agentic-engineering-patterns, context-window-management, fine-grained-authorization
- 349 unique tags not in SCHEMA.md taxonomy need reconciliation

## [2026-05-10] enrich | Daily skeleton enrichment — 3 stubs enriched, 1 new entity created
- **Status**: No `status: skeleton` entities found. Processed 3 `status: stub` entities as fallback.
- **Enriched:**
  - [[entities/matt-van-horn]] — Matt Van Horn (@mvanhorn): American entrepreneur, co-founder of Zimride (→Lyft) and June (AI oven, acquired by Weber). Enriched with Wikipedia bio, career timeline, key contributions section (Hermes Agent analysis, Reflexive AI docs).
  - [[entities/gkisokay]] — gkisokay (Graeme): AI agent practitioner, founder of Amplifi. Enriched with "Building AGI for my Hermes Agent" series detail, structured research pipeline thesis, agent watchdog architecture.
  - [[entities/bernstein]] — Bernstein: Open-source deterministic multi-agent orchestrator. Enriched with full features (44 adapters, HMAC audit chain, 4-stage pipeline, comparison table, architecture diagram, community metrics, creator info).
- **Created:**
  - [[entities/alex-chernysh]] — Alex Chernysh: Applied AI engineer, creator and solo maintainer of Bernstein. Includes career background, key projects (Bernstein, HireEx, RightLayout), engineering philosophy.
- **Index updated**: Entities 542→543, Total 1831→1832
- **Raw articles**: None (pure-web enrichment from website scraping + X/Twitter research + GitHub/PyPI sources)

## [2026-05-09] ingest | X accounts scan — 11 accounts, 4 new posts, 3 pages created
- **Scanned**: 11/79 accounts (68 skipped — budget)
- **New posts**: 4 (from @gm8xx8, @rlancemartin, @milksandmatcha)
- **Pages created**: 3
  - Created: entities/zyphra.md — Zyphra company entity (MoE models on AMD, $110M Series A)
  - Created: concepts/zaya1-vl-8b.md — ZAYA1-VL-8B: vision-language MoE (700M/8B), vision-specific LoRA, bidirectional image attention
  - Created: concepts/zaya1-74b-preview.md — ZAYA1-74B-preview: reasoning-base MoE (4B/74B), Mamba/CCA hybrid
- **Raw articles saved**: 2
  - raw/articles/2026-05-08-zyphra-zaya1-vl-8b.md
  - raw/articles/2026-05-08-zyphra-zaya1-74b-preview.md
- **Index updated**: Entities 541→542, Concepts 1272→1274, Total 1828→1831

## [2026-05-10] ingest | NVIDIA Dynamo article — Streaming Tokens and Tools
- **Raw article**: raw/articles/2026-05-08_nvidia-dynamo-streaming-tokens-tools.md
- **Source**: https://developer.nvidia.com/blog/streaming-tokens-and-tools-multi-turn-agentic-harness-support-in-nvidia-dynamo/
- **Updated**: [[concepts/nvidia-dynamo]] — Added agentic harness support section covering streaming tool dispatch, reasoning parsing, prompt stability/KV cache reuse, Anthropic API fidelity, Codex/Responses API parity
- **SCHEMA.md**: Added `streaming` tag to Techniques category
- **Index updated**: Concepts 1274→1275, Total 1831→1832
