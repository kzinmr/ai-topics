# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-21] trending-topics | 6 topics from web research

- **Pipeline**: trending-topics (20260521T120000Z) — web research + cross-reference + report
- **NJ 5/5**: OpenAI Erdos problem solved — first AI to autonomously solve a prominent open math problem (with mathematician verification)
- **NJ 4/5**: SynthID coalition expands — OpenAI, ElevenLabs, Nvidia, Kakao adopt Google's SynthID invisible watermarking
- **NJ 4/5**: Gemini for Science launches — Co-Scientist + ERA, 2 Nature papers, CDC-beating forecasts
- **NJ 3/5**: Google Search overhaul — information agents, custom GenUI dashboards, 24/7 monitoring
- **NJ 3/5**: Chrome DevTools for Agents 1.0 — MCP server + CLI + Agent Skills for AI debugging
- **NJ 3/5**: Gemini 3.5 Flash GA — agent-optimized model, $1.50/$9 per 1M tokens, Antigravity integration
- **Raw article saved**: `raw/articles/2026-05-21_trending-topics-report.md`

---


## [2026-05-21] active-crawl | 5 new pages: NVIDIA Nemotron-Labs-Diffusion, SANA-WM, Microsoft Agent Framework, Google ADK 2.0, Seirênes

- **Pipeline**: active-crawl (20260521T110000Z) — research + cross-reference + ingest
- **Topics researched**: 5 selected from trending AI/ML from web search (10 candidates, 5 missed wiki coverage)
- **Raw articles saved** (5):
  - `raw/articles/2026-05-20_nvidia-nemotron-labs-diffusion.md` — NVIDIA tri-mode LM (AR+diffusion+self-speculation, 3B/8B/14B)
  - `raw/articles/2026-05-16_nvidia-sana-wm.md` — NVIDIA 2.6B world model (60s 720p video on single GPU)
  - `raw/articles/2026-04-08_microsoft-agent-framework-v1.md` — Microsoft Agent Framework v1.0 (unified SK+AutoGen)
  - `raw/articles/2026-05-19_google-adk-v2.md` — Google ADK 2.0 GA (graph-based workflows)
  - `raw/articles/2026-05-21_seirenes.md` — Seirênes adversarial self-play RL for LLM reasoning
- **New entity pages** (4):
  - [[entities/nvidia-nemotron-labs-diffusion]] — Tri-mode LM: 6× tokens/forward, AR+diffusion+self-speculation
  - [[entities/nvidia-sana-wm]] — 2.6B world model, minute-scale 720p, single GPU
  - [[entities/microsoft-agent-framework]] — v1.0 production-ready multi-agent SDK (.NET+Python)
  - [[entities/google-adk]] — ADK 2.0 GA: graph-based Workflow Runtime, 20K ⭐
- **New concept page** (1):
  - [[concepts/seirenes]] — Adversarial self-play RL hardening reasoning robustness
- **Index updated**: +5 entries, header counts updated (Total: 2070, Entities: 649)

---

## [2026-05-21] blog-wiki-ingest | Batch enrichment: 4 entity pages (Seán Goedecke, Anthropic, Simon Willison, Google)

- **Pipeline**: blog-wiki-ingest (20260521T075000Z) — consumed 12 triage decisions (2 take + 2 reference + 8 skip)
- **Triage source**: blog-triage checkpoint (20260521T073805Z)
- **Entity pages enriched** (4):
  - [[entities/seangoedecke-com]] — Added "Prompts are technical debt too" article: prompts are worse debt than code (model-specific, silent decay). Added to Recent Articles + sources.
  - [[entities/anthropic]] — Added SpaceX S-1 contract specifics: $1.25B/month through May 2029, 90-day termination notice, ramp-up period in May-June 2026.
  - [[entities/simon-willison]] — Added Google I/O 2026 section: Gemini Spark prompt injection concerns, Antigravity CLI replacing Gemini CLI (June 18), FAQ architecture oddity.
  - [[entities/google]] — Added comprehensive Google I/O 2026 product section (17-column table): Universal Cart, Gmail Live, Pics App, Project Aura v2, Generative UI, Search Info Agents, Beam/Sophie, Vibe-Coding Android, AI Ultra pricing, etc.
- **Raw articles sourced**: seangoedecke.com--prompts-are-technical-debt-too, simonwillison.net--2026-may-20-spacex-s1, simonwillison.net--2026-may-20-google-io, theverge.com--tech-933415-google-io-2026
- **Skipped** (8): garymarcus (already captured), geohot (already captured), joanwestenberg (non-AI), micahflee (empty file), dfarq (non-AI retro), xeiaso (bot-wall), oldnewthing (Win32 API), hillelwayne (formal methods, non-AI)

---

## [2026-05-21] newsletter-wiki-ingest | Batch ingest: 5 new pages, 5 entity enrichments

- **Pipeline**: newsletter-wiki-ingest (20260521T074000Z) — 13 take items → 5 new pages + 5 entity enrichments
- **Sources**: Railway interview (swyx), Clicky newsletter (Aakash), Superintel Google I/O roundup
- **New pages created** (5):
  - [[entities/railway]] — Railway platform: 3M users, own-metal DCs, agent-native vision. Source: Jake Cooper interview
  - [[concepts/agent-native-cloud]] — Infrastructure paradigm for AI agents: beyond Git, beyond K8s, safe production forks
  - [[entities/clicky]] — Free macOS AI assistant by Farza: voice + screen capture → Claude → blue triangle pointing
  - [[events/isomorphic-labs-series-b]] — Isomorphic Labs $2.1B Series B (Thrive Capital, Demis Hassabis)
  - [[concepts/ai-supply-chain-security]] — 4 supply-chain incidents in 50 days: Codex CI injection, LiteLLM/Mercor, Claude Code leak, TanStack worm
- **Entity pages enriched** (5):
  - [[entities/anthropic]] — Claude for Small Business (15 workflows in QuickBooks/PayPal/HubSpot), KPMG Global Alliance (276K workforce), SpaceX $1.25B/month compute specificity
  - [[entities/xai]] — Grok Build terminal coding agent ($300/mo SuperGrok Heavy, 2M context, Plan Mode)
  - [[entities/openai-codex]] — Codex Mobile (ChatGPT mobile app preview)
  - [[entities/claude-code]] — Agent View (unified session list, /goal, /loop, /schedule)
  - [[entities/google]] — SynthID adopted by OpenAI/Nvidia as industry provenance standard
- **Skipped** (5): The Signal (consumer AI tools), The Skip (career podcast — non-AI), 2 reference items (data center backlash, Erdős problem), thariq-shihipar HTML article (already covered in entity page)

## [2026-05-21] ingest | Blog ingest batch: 4 raw articles saved, 2 new wiki pages, 3 entities enriched
- **Pipeline**: blog-ingest (20260521T070045Z) — 33 new articles detected, 20 from tracked blogs
- **Raw articles saved** (4):
  - `raw/articles/simonwillison.net--2026-may-20-tokens-per-second--a5b4c482.md` — How fast is 10 tokens per second really?
  - `raw/articles/openai-news--index-model-disproves-discrete-geometry-conjecture--a23c5621.md` — OpenAI model disproves discrete geometry conjecture
  - `raw/articles/openai-news--index-the-next-phase-of-education-for-countries--ae68796c.md` — OpenAI Education for Countries
  - `raw/articles/openai-news--index-ramp--95e072c6.md` — How Ramp engineers accelerate code review with Codex
- **Skipped** (4): WSJ/NYT paywalled, TikTok video, shkspr.mobi (non-AI)
- **New event**: [[events/google-io-2026]] — Google I/O 2026: Gemini Spark, Antigravity, Gemini 3.5 Flash, Gemini CLI→Antigravity CLI transition, agent security concerns
- **New concept**: [[concepts/prompts-as-technical-debt]] — Sean Goedecke's argument that prompts are a worse form of technical debt than code (silent decay with model upgrades)
- **Enriched entity**: [[entities/george-hotz]] — Added "What Will Better AI Mean?" post: scaling S-curve plateau, internet data exhaustion, AI has no moat, taste over scale
- **Enriched entity**: [[entities/gary-marcus]] — Added "Generative AI: The Tech Industry's Vietnam?" post: escalation without objectives, public backlash thesis
- **Enriched entity**: [[entities/ramp]] — Added Codex with GPT-5.5 adoption case study: code review acceleration, On-Call Assistant, engineers as orchestrators

## [2026-05-21] ingest | Linear technical breakdown (performance.dev) → entity + concept pages
- **Source**: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
- **Raw article saved**: `raw/articles/2025-xx-how-is-linear-so-fast-technical-breakdown.md`
- **Updated entity**: [[entities/linear]] — Added comprehensive Performance Architecture section covering: Local-First design philosophy (IndexedDB + MobX), Three Pillars of Sync Engine, Frontend optimizations (Rolldown bundler, esnext, per-package chunking, module preloading, Service Worker precaching, Canvas renderer, virtual scrolling), Render-First-Authenticate-Second pattern, Keyboard-First UX, Backend architecture (GraphQL, delta sync, WebSocket, PostgreSQL, idempotent mutations). New tags: performance, local-first.
- **New concept**: [[concepts/local-first-architecture]] — Comprehensive concept page covering local-first architecture principles, Linear's implementation (architecture stack diagram, optimistic updates pattern, data-level code splitting, granular re-renders), benefits, challenges, related technologies (CRDTs, RxDB, ElectricSQL, Replicache), and case studies (Linear, Notion, Obsidian, Figma).

## [2026-05-21] blog | AgenticなQuery UnderstandingとContent Understandingで非構造データDWH分析の汎用性・カスタム性を向上させるアーキテクチャ戦略
- **Blog post**: [[blog/2026-05-21_hermes_agentic-query-content-understanding-dwh]]
- **Summary**: kzinmrの依頼により、通話データ+metadataのような非構造データ中心のDWH分析オペレーションに対して、Agentic QU/CUアーキテクチャを提案するコンセプトブログ。3層のエージェント（Content Understanding Agents / Query Understanding Agent / Execution & Verification Agents）+ Harness層（Two-Loop, PMCL, Context Engineering）の構成。Phase 1-4の段階的導入ロードマップを含む。
- **Sources**: concepts/query-understanding, concepts/content-understanding, concepts/agentic-search, concepts/data-analysis-agents, concepts/poor-mans-continuous-learning, concepts/context-engineering, concepts/agent-architecture-decomposition, concepts/agent-patterns, concepts/agent-runtime

## [2026-05-21] ingest | Jason Liu "Getting the Most Out of Codex" X Article → entity enrichment
- **Source**: https://x.com/jxnlco/status/2057153744630890620 (X Article, published 2026-05-20)
- **Raw article saved**: `raw/articles/2026-05-20_jxnlco_getting-the-most-out-of-codex.md`
- **Updated entity**: [[entities/jason-liu]] — Added "Getting the Most Out of Codex (May 2026)" section with capability catalog table (durable threads, voice input, steering, queuing, $browser/@chrome/@computer, MCP+Connectors, Skills, mobile, thread automations, Goals, side panel, shared memory). Added human-in-the-loop architectural insight. New tags: agent-harness, workflow, human-in-the-loop.
- **Updated entity**: [[entities/openai-codex]] — Added comprehensive "Codex App: Human-in-the-Loop Capabilities" section (64 lines) covering: 制御モデル (Steering/Queuing/Voice input), リーチレイヤー ($browser/@chrome/@computer tool hierarchy + MCP + Skills), 長時間実行と自律性 (Durable threads/Thread automations/Goals), サイドパネル (4 roles + effective surfaces), 共有メモリ (Obsidian vault + AGENTS.md + Codex Memories + Chronicle), モバイル (Work from Anywhere). New tags: human-in-the-loop, workflow, voice-ai. Added [[entities/jason-liu]] and [[concepts/codex-goal]] to 関連トピック.
- **Index updated**: Updated descriptions for [[entities/jason-liu]] and [[entities/openai-codex]] with new capabilities.

## [2026-05-20] skeleton-enrich-daily | Daily skeleton enrichment — no skeletons found, enriched 2 L1 entities
- **Status**: No `status: skeleton` entity pages found. Enriched 2 `status: L1` entity pages to `L2`.
- **Enriched**: [[entities/roocode]] — Major status update: extension shut down May 15, 2026. Added project timeline, shutdown details (Roomote pivot), community fork (Zoo Code, 453 stars), alternative comparisons (Cline, Kilo Code, Continue.dev), v3.53.0 features (GPT-5.5, Claude Opus 4.7, checkpoint navigation), updated stats (23.9K stars, 3.2K forks, 290 contributors), 3M installs, architecture lineage, and v3.51.0 slash command skills.
- **Enriched**: [[entities/parchi]] — Expanded from 2.9KB to 8.2KB. Added architecture diagram, CLIProxyAPI integration for using existing AI subscriptions, Relay Daemon & CLI details, Electron desktop automation, pricing (BYOK/Credits), safety notice, multi-model provider table (OpenAI/Anthropic/OpenRouter/Kimi/Local), project status assessment (maintenance mode since April 2026), profiles & skills feature, and vision-native capability.
- **Index updated**: Added [[entities/parchi]] and [[entities/roocode]] entries to `entities/_index.md` with descriptions. Updated `wiki/index.md` descriptions.

## [2026-05-20] ingest | turbopuffer RL training SID-1 article → entity pages + agentic-search enrichment
- **Source**: https://turbopuffer.com/blog/reinforcement-learning-sid-ai (Max Rumpf & Sam Dauncey, SID AI, May 20 2026)
- **Raw article saved**: `raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai.md`
- **New entity**: `entities/sid.md` — SID AI research lab, SID-1 model details, training design, emergent capabilities
- **New entity**: `entities/turbopuffer.md` — turbopuffer search engine (was orphaned in index, now created with full content)
- **Updated concept**: `concepts/agentic-search.md` — Added RL Training Infrastructure, Search Backend (turbopuffer), and Emergent Tool Preferences sections with details from the turbopuffer article. Added raw article to sources.
- **Index updated**: Added `entities/sid.md` entry (alphabetical between shunyu-yao and simon-willison)
- Key new information captured: 256 questions × 16 attempts RL training scale, 1k+ QPS burst pattern, GPU utilization bottleneck, turbopuffer stateless architecture fit for RL workloads, HyDE emergence, parallel tool use as emergent speed behavior, corpus branching for reproducibility

## [2026-05-20] health-fix | Auto-fix index corruption + orphan registration
### Phase 1 — Index corruption (auto-fix)
- Clean: validate_index.py passed ✅
- No pipe corruption (0), no triple bracket (0), no line-number prefix (0)
- Fixed 1 ghost entry: [[concepts/rag]] → [[concepts/rag-systems]] (file didn't exist)
### Phase 2 — Orphan index registration (20 entries)
- Added 20 legitimate orphan concept pages to index.md (concepts section)
- Updated concepts count: 1376 → 1396, Total: 2073 → 2093, Not in index: 865 → 845
- Entries batch-appended at section boundary (alphabetically drifted)
### Pages Added to Index
- concepts/ai-military
- concepts/arc-agi-2
- concepts/attention-mechanism-variants
- concepts/background-agent-orchestration-linear-github-workflow-automation-graph-based
- concepts/background-coding-agent
- concepts/base-consistency
- concepts/base-consistency-model
- concepts/behavioral-trait-transmission
- concepts/bitter-lesson-harnessing
- concepts/blogwatcher
- concepts/bottom-up-note-taking
- concepts/business-to-agent
- concepts/cache-first-engineering
- concepts/caching-performance-cost-optimization
- concepts/caid-coordination
- concepts/capability-based-security
- concepts/centaurs-and-cyborgs
- concepts/chain-of-thought-reasoning
- concepts/chaos-engineering
- concepts/chaos-engineering-for-microservices
---

---

## [2026-05-20] watchdog | Log.md health + index dedup + pipe corruption fix

### Auto-fixed
- Restored missing `# Wiki Log` header (silent loss pitfall)
- Removed duplicate orphan `###` timestamp (sub-pattern 1)
- Converted standalone `###` timestamp to proper `## [YYYY-MM-DD]` format for SDAR Paper entry (sub-pattern 2)
- Removed 4 duplicate entity index entries: `cognition`, `eric-zhang`, `factory`, `muratcan-koylan`
- Fixed 8 pipe-prefixed index entries (`|- ` → `- `) introduced during patch operations
- validate_index.py: clean ✅
- Fixed 8 triple-bracket corruptions (`[[[` → `[[`) in index.md

---

## [2026-05-20] raw-backlog-ingest | Notion/Sarah Sachs/Simon Last/Marc Andreessen podcast triage
- **New entity pages**: `entities/notion.md` (Notion as AI company), `entities/sarah-sachs.md` (Notion AI engineering lead), `entities/simon-last.md` (Notion agent harness architect)
- **Enriched**: `entities/marc-andreessen.md` (already existed from same podcast)
- **Enriched concept pages**: `concepts/harness-engineering.md` (Notion's 5-iteration agent harness, progressive disclosure), `concepts/ai-evals.md` (Notion's three-tier eval framework, MBE role, 30% headroom evals), `concepts/agent-architecture-decomposition.md` (Notion's agent composition via shared databases)
- **Notion eval insights**: Regression tests (CI) → Launch-quality (80-90%) → Frontier/headroom (30% pass rate); Model Behavior Engineer as distinct role; quality variation across providers (Bedrock vs Azure vs first-party)
- **Sources**: Latent Space Podcast — Notion's Token Town (Simon Last & Sarah Sachs), Marc Andreessen interview
## [2026-05-20] update | blog/2026-05-20_hermes_divide-and-conquer-duality.md — ずらした条件付き圧縮の章を追加
- 新第3章「ずらした条件付き圧縮——素朴な双対モデルの限界」: objective' = compress(context | goal) への定式化修正
- 残差学習・アドバンテージ関数(GRPO)・能動学習の3つの相同構造で「ずらし」を理論化
- Anthropicの暗黙的解決（タスク境界＋insufficient判定）の分析と残された3つの設計問題（充足度測定・残余クエリ化・変位粒度）
- クエリ拡張/推薦との区別として「クエリ変位（displacement）」を提案
- 結論を「分ける・つなぐ・ずらす」の三層構造に更新、次のフロンティアとしてずらしの設計を位置づけ

## [2026-05-20] create | blog/2026-05-20_hermes_divide-and-conquer-duality.md — 分割と双対: マルチエージェント、RLM、IRを貫く構造
- マルチエージェント（水平分割/MapReduce）とRLM（深さ分割/再帰）の分割統治パターン
- クエリ-文書双対性から見る Agent-Context 関係: objective↔クエリ, context↔文書, interleaved thinking↔relevance feedback
- IRの知見がエージェント設計に転用可能である実践的含意
- 「情報要求と情報充足が同一トークン空間のグラデーションに過ぎない」というLLM時代の根本洞察

## [2026-05-20] enrich | concepts/anthropic-multi-agent-research.md — Agent-Context双対性 (IRのクエリ-文書双対性との相同)
- ユーザーの洞察: エージェントと文脈の関係に、IRのクエリ-文書双対性に似た構造がある
- サブエージェントタスク(objective)↔クエリ、探索結果(context)↔文書、interleaved thinking↔relevance feedback の対応表
- 「search is compression」を双対性の観点から再解釈: objective→探索→thinking→objective更新 = クエリ→文書→適合FB→クエリ拡張 と同じループ
- 同じLLMトークン空間上で、クエリと文書が異なる粒度の同一対象として表現される

## [2026-05-20] create | concepts/agent-operator-patterns.md — Shann HolmbergのHermes Agent運用パターン集

### 変更内容
- `wiki/concepts/agent-operator-patterns.md` 新規作成: Shann Holmberg "How to Become a Hermes Agent Operator" から抽出した6つの運用パターン
  - Control Room（サイドコントロールプレーン）、Brain Layers（文脈レイヤー化）、Agent Creation Heuristics（新エージェント作成基準）
  - 4-Level Fleet Operation Model（単一→複数→Orchestrator→完全自動化）
  - Prototype → Production Methodology（4ステップ）、Agent Ergonomics（運用快適性）
  - 各パターンのWiki管理システム（27 cron jobs + Hermes単一エージェント）への具体的応用分析を含む
  - Storage Split（brain/body分離）の原則、Level 2→3移行判断基準
- `wiki/index.md`: Conceptsセクションに agent-operator-patterns エントリ追加
- Sources: raw/articles/2026-05-15_shann_hermes-agent-operator.md

## [2026-05-20] enrich | concepts/anthropic-multi-agent-research.md + concepts/rlm-recursive-language-models.md — Multi-Agent × RLM 構造的類似パターン
- ユーザーの洞察: Multi-Agentのタスク水平分割（MapReduce）とRLMの入力深さ分割（再帰）は同一のdivide-and-conquer発想
- anthropic-multi-agent-research.md に「構造的類似パターン」セクションを追加: 分割対象・分割方向・パターン・制約突破・スケーリング・集約方法・本質の7次元比較表
- rlm-recursive-language-models.md の Related Concepts に相互参照を追加
- 両者とも「単一コンテキストウィンドウ制約を分割統治で乗り越える」という根本パターンの異なる現れ

## [2026-05-20] create | concepts/anthropic-multi-agent-research.md — Anthropic Claude Research マルチエージェントシステム
- Anthropic Engineering Blog (2025-06-13)「How We Built Our Multi-Agent Research System」と Simon Willisonの注釈記事 (2025-06-14) を完全取り込み
- 新規conceptページ: Orchestrator-Workerパターン、Memory機構、CitationAgent、並列化戦略、Prompt Engineering 8原則、Tool-Testing Agent（40%時間短縮）、token economics（chat比15×）
- 単一Opus 4を90.2%上回る性能、token使用量が性能分散の80%を説明 などの定量的知見
- concepts/agent-patterns.md に Orchestrator-Workerパターンを第5のパターンとして追加
- concepts/agentic-search.md に Anthropicマルチエージェント研究へのクロスリファレンスを追加
- 生記事: raw/articles/2025-06-13_anthropic_multi-agent-research-system.md, raw/articles/2025-06-14_simonwillison_multi-agent-research-system.md

## [2026-05-20] create | concepts/context-engineering.md — Anthropic + Lance Martin 結合考察
- Anthropicの"Effective Context Engineering for AI Agents" (2025-09-29) と Lance Martinの"Context Engineering for Agents" (2025-06-23) および"Agent Design Patterns" (2026-01-09) を統合
- Anthropicの実装視点（system prompts, just-in-time retrieval, compaction, note-taking, sub-agent delegation）と Lance Martinの4戦略分類（Write/Select/Compress/Isolate）のマッピングを整理
- 文脈破綻モード（Poisoning/Distraction/Confusion/Clash/Rot）、attention budget、progressive disclosure、prompt caching、Ralph Wiggum loop、Bitter Lessonもカバー
- 併せて entities/lance-martin.md を作成（Anthropic/LangChain経歴、4戦略分類の著者、managed agents共著の実績を記載）
- index.md の両エントリをフル説明に更新

---
## [2026-05-20] create | concepts/context-engineering.md — Anthropic + Lance Martin synthesis

### 変更内容
- 3つのraw記事を保存:
  - `raw/articles/2025-09-29_anthropic_effective-context-engineering-for-ai-agents.md`
  - `raw/articles/2025-06-23_lancemartin_context-engineering-for-agents.md`
  - `raw/articles/2026-01-09_lancemartin_agent-design-patterns.md`
- `concepts/context-engineering.md` 作成: Anthropicの記事とLance Martinの2記事を合成した包括的なコンテキストエンジニアリング概念ページ
  - Anthropicフレームワーク: System Prompts, Examples, Tools/MCP, Just-in-Time Retrieval, Compaction, Structured Note-Taking, Sub-Agent Delegation
  - Lance Martinの4戦略分類: Write (外に保存) / Select (窓に引込) / Compress (必要なものだけ保持) / Isolate (エージェント間分割)
  - 両フレームワークのマッピング表、文脈破綻モード (Poisoning/Distraction/Confusion/Clash/Rot)、attention budget、n² attentionの説明
  - 発展パターン: Give Agents a Computer, Progressive Disclosure, Prompt Caching, Ralph Wiggum Loop, Multi-Layer Action Space
  - The Bitter Lessonの視点: RLMやsleep-time computeで将来的にモデル側に吸収される可能性
  - 実践チェックリスト（7項目）
- `entities/lance-martin.md` 作成: Anthropic MTS, 元LangChain, PhD Stanford, 自動運転経歴（Nuro/Ike/Uber ATG）
  - Context Engineering 4戦略分類の著者としての貢献、Anthropicでのmanaged agents/context engineering記事の共著
  - 主要著作一覧表、The Bitter Lessonに関する見解
- `index.md` 更新: lance-martinエントリ（スケルトン→フル説明）, context-engineeringエントリ（最小→フル説明）

---

## [2026-05-20] X bookmarks ingest | Agent Marketplace Stack + Langfuse Evals + Jason Liu Codex Brief

**Source**: X bookmarks cron fetch. 3 new bookmarks processed.

### Raw Articles Created
- [[raw/articles/2026-05-19_autonomous-agent-technical-stack.md]] — "The Technical Stack for Autonomous Agents" — X Article (30,812 chars). Full body fetched via tweet.fields=article. Three planes (Trust/Market/Control), ten layers framework for autonomous agent marketplaces. ERC-8004, x402, governance control planes.
- [[raw/articles/2026-05-19_langfuse-academy-evals-explained.md]] — "Evals, explained" — Langfuse Academy X Article. AI Engineering Loop, three evaluation methods (manual/code-based/LLM-as-judge), reference-based vs reference-free.
- [[raw/articles/2026-05-18_jxnl-six-levels-codex-morning-brief.md]] — Jason Liu (@jxnlco) "Six levels of complexity in a Codex morning brief" — scraped via Jina Reader API.

### Concept Page Created
- [[concepts/autonomous-agent-marketplace-stack]] — Comprehensive concept page for the 3-plane 10-layer autonomous agent marketplace infrastructure framework. Covers Trust Plane (Identity/Discovery/Reputation), Market Plane (Quoting/Contracting/Settlement/Dispute Resolution), Control Plane (Governance/Compliance/Orchestration & Runtime). ERC-8004, x402, Safe modules, Cordum/Galileo/Microsoft governance vendors.

### Concept Page Enriched
- [[concepts/ai-evaluation]] — Stub → full page. Enriched with Langfuse Academy evaluation framework: AI Engineering Loop, three evaluation methods, reference-based vs reference-free, practical guidelines, binary scoring preference. Sources: Langfuse Academy.

### Entity Page Enriched
- [[entities/jason-liu]] — Added "Six Levels of Codex Morning Brief" section with level table, key principles, vault structure. Updated sources.

## [2026-05-20] active-crawl | Google I/O 2026 + Cursor Composer 2.5 + NVIDIA SANA-WM + OpenAI GPT-Realtime-2

**Source**: Active crawl research. 4 topics discovered from web search (Google I/O 2026, Cursor blog, arXiv, OpenAI blog).

### Raw Articles Created
- [[raw/articles/2026-05-20_google_gemini-app-agentic.md]] — Google I/O 2026: Gemini app becomes agentic (Spark, Daily Brief, Omni, Neural Expressive, macOS app)
- [[raw/articles/2026-05-20_google_gemini-omni.md]] — Gemini Omni Flash: world model for cinematic video generation from any input modality
- [[raw/articles/2026-05-20_cursor_composer-2-5.md]] — Cursor Composer 2.5: targeted RL with textual feedback, 25× synthetic data, Sharded Muon
- [[raw/articles/2026-05-20_nvidia_sana-wm.md]] — NVIDIA SANA-WM: 2.6B open-source world model, minute-scale 720p video on single GPU
- [[raw/articles/2026-05-20_openai_gpt-realtime-2.md]] — OpenAI GPT-Realtime-2: three realtime voice models with GPT-5-class reasoning

### Entity Page Updated
- [[entities/gemini]] — Added Gemini Omni (world model), Gemini Spark (24/7 AI agent), Daily Brief sections. Updated infobox, model family list, relationships. Added 2 raw sources.

### Concept Pages Created
- [[concepts/cursor-composer-2-5]] — Agentic coding model built on Kimi K2.5. Targeted RL, 25× synthetic data, reward hacking, Sharded Muon optimizer
- [[concepts/nvidia-sana-wm]] — 2.6B open-source world model (Apache 2.0). Hybrid GDN+softmax, dual-branch camera. 36× throughput vs LingBot-World
- [[concepts/openai-gpt-realtime-2]] — Three realtime voice models: reasoning voice, live translation (70+→13 languages), streaming Whisper

### index.md
- Updated Entities section: gemini entry now reflects I/O 2026 announcements
- Added 3 new concept entries (cursor-composer-2-5, nvidia-sana-wm, openai-gpt-realtime-2)
- Updated header counts: Total pages 2068→2071, Concepts 1372→1375

---

## [2026-05-20] raw + entity | RL Environments Taxonomy raw article + entity update

**Raw article created**: [[raw/articles/2026-03-21_leehanchung_rl-environments-for-llm-agents]] — Foundational first article in Lee's "Hidden Technical Debt" series. Formally defines  = \{T, H, V, S, C\}$ framework. Task taxonomy (10 types), rollout protocols, tools landscape, verifier types, context management for 600+ turn episodes.

**Entity page updated**: [[entities/han-lee]] — Updated Overview to reflect trilogy structure: RL Environments → Agent Runtime → Agent Harness. Expanded RL Environments entry with full framework detail. Added raw article to frontmatter sources.

**index.md**: Updated entry to show trilogy with chronological arrows (Mar → Apr → May 2026).

## [2026-05-20] entity + raw | Han Lee entity enrichment + RSS monitoring added

**Entity page enriched**: [[entities/han-lee]] — Added Monitoring section (RSS feed tracked via blogwatcher), 4 new notable articles (Agent Harness, Data Aggregation Is Not a Moat, Don't Outsource Your Understanding, Determinism Cope), 3 new contributions (Training vs Production Harness Asymmetry, Cognitive Offloading vs Surrender, Data Moat Deconstruction), updated Related Wiki Pages with Letta link.

**Raw articles created**:
- [[raw/articles/2026-05-08_leehanchung_hidden-technical-debt-agent-harness]] — Third in Hidden Technical Debt series; deconstructs agent harness layer
- [[raw/articles/2026-05-10_leehanchung_data-aggregation-is-not-a-moat]] — AI agents collapse data aggregation moats
- [[raw/articles/2026-05-01_leehanchung_dont-outsource-your-understanding]] — Cognitive offloading vs surrender
- [[raw/articles/2026-04-07_leehanchung_determinism-biggest-cope-in-ai-adoption]] — Determinism vs evaluation in AI adoption

**RSS monitoring**: Added "Han, Not Solo" to blogwatcher + OPML (Individual Blogs). RSS: `https://leehanchung.github.io/feed.xml` Initial scan: 20 articles found (marked read).

**X/Twitter**: @HanchungLee NOT yet tracked in x-accounts.yaml — noted in Monitoring section as TODO.

**Already ingested (confirmed)**:  (Agent Runtime),  concept page.

## [2026-05-20] config | RSS exclusion — Dan Luu + Simon Tatham

### RSS Monitoring Removed
- `config/feeds/blogs.opml` — Removed Dan Luu (`danluu.com/atom.xml`) and Simon Tatham (`chiark.greenend.org.uk/~sgtatham/quasiblog/feed.xml`) from Individual Blogs group
- blogwatcher DB — Removed both blogs via `blogwatcher-cli remove`

### Reasoning
Both blogs have minimal AI/LLM content. Keeping them in RSS monitoring generates noise without actionable wiki material. Wiki entity pages remain — exclusion is at the RSS level only.

### Entity Updated
- `wiki/entities/chiark-greenend-org-uk-sgtatham.md` — Added Monitoring section with RSS exclusion note; removed RSS URL from infobox

## [2026-05-20] newsletter-wiki-ingest | 6 newsletters batch — Google I/O 2026, Vlad Feinberg, Vincent Warmerdam, Cursor Composer 2.5, Anthropic Stainless, OpenAI reorg, LangSmith, Zero language

### Source
Newsletter triage checkpoint recovered from `${HERMES_HOME}/cron/data/newsletter/triage_latest.json`. 19 candidates → 8 take, 8 reference, 2 skip.

### Created
- `wiki/entities/vincent-warmerdam.md` — Vincent Warmerdam (@koaning): Engineer at marimo. Agent-Harness.ipynb insights (shared notebook canvas, marimo linter 60% fix rate, incremental generation, calm philosophy).
- `wiki/entities/langsmith.md` — LangSmith CI/CD for agents platform. LangSmith Engine: auto-detect failures, cluster issues, draft fixes/evals.
- `wiki/concepts/frontier-lab-job-preparation.md` — Vlad Feinberg's frontier lab job prep guide. Kernel-level optimization bottleneck, Chinchilla derivation, Jax/Pallas skills.

### Enriched
- `wiki/entities/google.md` — Added Google I/O 2026 section (Gemini 3.5 Flash: TB 76.2%, MMMU-Pro 84%; Gemini Omni multimodal video; Antigravity 2.0 Agent OS w/ 93 sub-agents demo; Spark 24/7 personal AI; 3.2 quadrillion tok/mo; 900M+ MAU).
- `wiki/entities/cursor-ai.md` — Added Composer 2.5 (Opus 4.7-xhigh parity) + SpaceXAI 10× compute training (1M H100-equiv from Colossus 2).
- `wiki/entities/anthropic.md` — Added Stainless (SDK/MCP platform) acquisition section. Vertical integration: models → SDKs → sandboxes.
- `wiki/entities/openai.md` — Added reorganization (Greg Brockman→Products, Thibault Sottiaux→Core Product), Codex Phone Connection, ChatGPT App Directory & SDK.
- `wiki/entities/jason-liu.md` — Added Codex Maxxing section (durable threads, shared memory, daily primitives).
- `wiki/entities/zero-language.md` — Bumped updated date, added newsletter source.

### Reference Items (minor, no page changes needed)
- Cloudflare Mythos testing — already covered in concepts/claude-mythos-glasswing.md Cloudflare Testing section
- MTP in llama.cpp, Meta AIRA, Training in Imagination — insufficient depth for new pages
- HTML is the New Markdown — thin reference
- Zero language concept — already fully covered by entities/zero-language.md

### Index
- entities: 633→635 (vincent-warmerdam, langsmith)
- concepts: 1371→1372 (frontier-lab-job-preparation)
- total pages: 2065→2068
- indexed entries: 1180→1183

---

## [2026-05-19] ingest | Bag-of-Documents Model slides (Tunkelang, SpeakerDeck, May 2026)

### Created
- `wiki/raw/articles/2026-05-19_daniel-tunkelang_bag-of-documents-slides.md` — Guest lecture for Doug Turnbull & Trey Grainger's AI-powered search class (May 19, 2026). Covers: BoD architecture, relevance judgment sources (implicit/explicit/automated, "Ranking ≠ Relevance!"), loss functions (Centroid Loss vs MNRL), BoD for reranking (BM25 + BoD strongest hybrid), 7 caveats for when BoD works, try-it-yourself setup, Best Buy demo.

### Updated
- `wiki/concepts/information-retrieval.md` — Added: Loss Functions section (Centroid Loss vs MNRL comparison), Sources for Relevance Judgments (implicit/explicit/automated table with "Ranking ≠ Relevance!" insight), BoD for Reranking (hybrid pattern), Caveats (7 conditions), Resources (Best Buy demo + SpeakerDeck). Frontmatter: added slides source.
- `wiki/entities/daniel-tunkelang.md` — Frontmatter sources: added slides reference.

---

## [2026-05-20] create | Claude Code and Shopify AI-First Engineering concept pages

### Created
- `wiki/concepts/claude-code.md` — Claude Code as a coding agent: 6 operational patterns (parallel agents, extended critique loops, MCP integration, CLAUDE.md as team infrastructure, strategy-first validation, safe autonomy with guardrails), configuration examples, prompt patterns. Source: zodchiii Shopify Claude Code setup article + Pragmatic Engineer Farhan Thawar podcast.
- `wiki/concepts/shopify-ai-engineering.md` — Shopify's AI-first engineering approach: LLM proxy architecture, tool adoption timeline (Copilot 2021 → Cursor → Claude Code → Devin/Gumloop), 1,000 interns program, GSD project management, coding interviews for directors, strategy:execution ratio flip (30:70 → 70:30), no token spending limits policy. Source: zodchiii Shopify Claude Code setup article + Pragmatic Engineer Farhan Thawar podcast.

### Updated
- `wiki/SCHEMA.md` — Added `shopify` tag to People/Orgs category and `llm-proxy` tag to Engineering category.
- `wiki/index.md` — Added both concept pages to Concepts section. Bumped counts (+2 concepts).

## [2026-05-19] ingest | Agentic Search as an Agile Engineering Process (Tunkelang & Makhani, Mar 2026)

### Created
- `wiki/raw/articles/2026-03-26_daniel-tunkelang_agentic-search-agile-engineering.md` — Agentic Search as an Agile Engineering Process (Mar 26, 2026). Co-authored with Asif Makhani (Infino AI). Frames agentic search as agile engineering: queries as partial specifications, agents as engineers, searchers as product owners. Scope–Cost–Quality triangle → 3 search modes. Uncertainty reduction as core metric. Evaluation-driven "definition of done" (testing replaces explainability). Task sizing tradeoffs. Design principles.

### Updated
- `wiki/concepts/agentic-search.md` — Added Level 4: Process/Methodology — Agile Engineering Framework (57 lines). Core analogy (searcher=PO, agents=engineers), Scope–Cost–Quality triangle, uncertainty reduction metric, evaluation-driven done, task sizing, predictability vs evaluability, 5 design principles. Frontmatter: added `methodology` tag, added raw article source.
- `wiki/entities/daniel-tunkelang.md` — Added 3 new points to Views on Agentic Search (agile engineering framing, Scope–Cost–Quality triangle, evaluation replaces predictability). Updated Related section description. Added raw article to sources.
- `wiki/index.md` — Expanded agentic-search entry to include 4-level framework summary and key contributors.

---

## [2026-05-20] raw-backlog-ingest | Anthropic emotion concepts + SemiAnalysis ClusterMAX 2.0

### Enriched
- `wiki/concepts/functional-emotions-llms.md` — Massive expansion (77→250+ lines): Added Emotion-Alignment Causal Links section (reward hacking via desperation, sycophancy via positive valence, blackmail under agentic misalignment, emotion-RL training patterns). Added Character Simulation & Emotion section. Added Related Research Connections (11 papers). Added Training for Healthier Psychology section (balanced profiles, transparency, pretraining curation). Updated frontmatter with new tags (sycophancy, reward-hacking, post-training), sources, and cross-references.

### Created
- `wiki/concepts/gpu-cloud-rankings.md` — New concept page: ClusterMAX 2.0 GPU cloud rating system by SemiAnalysis. 209 providers, 10 criteria, 5 rating tiers. Rankings table (CoreWeave Platinum, Nebius/Oracle/Azure/Fluidstack/Crusoe Gold, Google/AWS/together.ai/Lambda Silver). Key trends: Slurm-on-K8s convergence (SUNK/Soperator/Slinky), GB200 NVL72 reliability crisis, NVIDIAScape container escapes, InfiniBand security, crypto-to-AI pivot, NVIDIA acquisition spree ($2.1B). CoreWeave and Nebius deep dives. K8s training tool ecosystem table. Quick benchmarks table. Industry quotes.
- `wiki/entities/semianalysis.md` — New entity page: Boutique AI/semiconductor research firm founded by Dylan Patel (2020). Products: ClusterMAX rating system, AI Accelerator & HBM Model, AI Tokenomics Model, Datacenter Industry Model. 12-person global team. Industry influence cited by OpenAI, Meta, Dell, HPE.

### Raw Articles
- `wiki/raw/articles/2026-05-20_anthropic-emotion-concepts-function-llm.md` — Anthropic Transformer Circuits paper on functional emotions in LLMs (Sofroniew et al., 2026)
- `wiki/raw/articles/2026-05-20_semianalysis_clustermax-2-gpu-cloud-ratings.md` — SemiAnalysis ClusterMAX 2.0 GPU Cloud Rating System (November 2025, 46K+ words)

### Index
- index.md: entities 629→630, concepts +1 (gpu-cloud-rankings), total pages 2058→2060, indexed entries 1173→1175

### Skipped (non-AI)
- danluu.com/fsyncgate/ — PostgreSQL file safety (no AI relevance)
- danluu.com/diseconomies-scale/ — Business/fraud analysis (no AI relevance)
- danluu.com/su3su2u1/hpmor/ — HPMOR fiction review archive (no AI relevance)

## [2026-05-19] x-bookmarks-ingest (23:30) | Hermes Agent operator guide + Claude sandboxes/MCP tunnels

### Created
- `wiki/entities/shannhk.md` — Shann Holmberg (@shannhk): Head of Product at Espressio AI, Hermes Agent operator. Creator of hermes-agent-control-room template (4-level fleet model). Co-founder of Lunar Strategy (250+ projects). Co-author of Master Web3 Marketing. Based in Lisbon.

### Enriched
- `wiki/entities/shannhk.md` — Cross-Referencesに新規conceptページ [[concepts/agent-operator-patterns]] へのリンク追加。updated: 2026-05-20
- `wiki/entities/hermes-agent.md` — Added Shann's 4-Level Fleet Operation Model (Level 1→4), Control Room pattern, SEO Agent 21-step pipeline case study, Prototype → Production methodology, Rails vs Linux framing, model strategy (Opus 4.7 creative / Codex GPT 5.5 structured). Updated milestones: 150K stars, 123 bundled skills, 6 deployment targets, 20+ messaging surfaces.
- `wiki/concepts/claude-managed-agents.md` — Added Self-Hosted Sandboxes (public beta) + MCP Tunnels (research preview) section, announced at Code with Claude London (May 19, 2026). Covers enterprise security perimeter, data residency compliance, MCP tunnel connectivity for private network tools, and hybrid deployment model.

### Raw Articles
- `wiki/raw/articles/2026-05-15_shann_hermes-agent-operator.md` — Shann Holmberg "How to Become a Hermes Agent Operator" (X article, full body via bookmark fetch)
- `wiki/raw/articles/2026-05-19_claude-managed-agents-sandbox-mcp-tunnels.md` — @claudeai announcement at Code with Claude London

### Index
- index.md: entities 628→629, total pages 2057→2058, indexed entries 1172→1173

## [2026-05-19] skeleton-enrich-daily | Enriched siyan-zhao (stub→full) + romain-huet (L1→L2)

### Enriched
- `wiki/entities/siyan-zhao.md` — stub→full: Added bio (UCLA PhD candidate, Meta Superintelligence Labs), 9 publications with venues (ICML 2026, NeurIPS 2025 Spotlight, ICLR 2025/2026, NeurIPS 2024 Best Paper), research focus areas (diffusion LLM reasoning, preference alignment, inference efficiency), full OPSD methodology, publication record table. 43→115 lines.
- `wiki/entities/romain-huet.md` — L1→L2: Added career timeline (OpenAI→Stripe→Twitter→Jolicloud), Codex CLI demo activities (GPT-5-Codex launch, code review with Maja Trębacz), philosophy section, GitHub profile info. 47→97 lines.

### Status
- No `status: skeleton` entity pages found. All 621 entity pages are skeleton-free.
- 8 lowest-status pages remain: 1 stub (siyan-zhao → now enriched), 4 L1 (roocode, jeremiah-lowin, parchi), 2 lowercase-l2 (niplav, jeff-huber), 1 needs-identification (adam-rosenthal).

---

## [2026-05-19] ingest | Daniel Tunkelang pinned articles — 5 raw articles + IR concept page

### Created
- `wiki/raw/articles/2026-04-20_daniel-tunkelang_distilling-retrieval-pipelines.md` — Distilling Retrieval Pipelines to a Single Embedding Model (Apr 2026). Pretrained bag-of-documents model, hybrid retrieval + cross-encoder, FAISS, 16GB MacBook Air M4. Key results table (cosine sim 0.914, recall@10 0.506).
- `wiki/raw/articles/2025-03-27_daniel-tunkelang_precision-recall-desirability.md` — Precision, Recall, and Desirability: A Deep Dive (Mar 2025). Three-dimensional framework with measurement, detection, and fix strategies for each.
- `wiki/raw/articles/2024-12-02_daniel-tunkelang_bag-of-documents.md` — Modeling Queries as Bags of Documents (Dec 2024). Search Solutions 2024 presentation with Aritra Mandal. Query-document alignment via aggregated click vectors.
- `wiki/raw/articles/2024-04-08_daniel-tunkelang_embedding-based-retrieval-rag.md` — AI-Powered Search: Embedding-Based Retrieval and RAG (Apr 2024). Bag-of-words → embeddings, query-document alignment challenge, chunking, ranking pitfalls.
- `wiki/raw/articles/2023-08-07_daniel-tunkelang_semantic-equivalence-ecommerce.md` — Semantic Equivalence of e-Commerce Queries (Aug 2023). KDD 2023 ECNLP workshop. Behavior-driven query equivalence via sentence transformer. arXiv 2308.03869.
- `wiki/concepts/information-retrieval.md` — Enriched from stub: Precision-Recall-Desirability framework, retrieval paradigms (lexical/embedding/hybrid), bag-of-documents model (full results table + resources), query similarity & semantic equivalence, RAG overview. Cross-linked to 9 related concepts.

### Updated
- `wiki/entities/daniel-tunkelang.md` — Frontmatter sources: added 5 new raw article references. Related: updated information-retrieval description.
- `wiki/index.md` — Added Concepts entry for information-retrieval (alphabetical insertion), updated header counts (1370→1371, 2056→2057, 1171→1172).

---

## [2026-05-19] config+enrich | Add Daniel Tunkelang Medium RSS + entity enrichment

### Changes
- `config/feeds/blogs.opml` — Added Daniel Tunkelang (dtunkelang.medium.com) to RSS monitoring via blogwatcher
- `wiki/entities/daniel-tunkelang.md` — Enriched: Added Bag-of-Documents Model (2023–2026) section with arXiv 2308.03869 paper, Apr 2026 "Distilling Retrieval Pipelines" post, key results table, resources. Added Monitoring section (RSS + X). Updated frontmatter (tags: information-retrieval, query-understanding; sources: Medium + arXiv). Updated Related, Sources, career info, blog URL (active Medium blog).
- `wiki/SCHEMA.md` — Added `query-understanding` tag to Techniques taxonomy
- `wiki/index.md` — Updated daniel-tunkelang entry with Medium blog link, bag-of-documents work, RSS monitoring status

---

## [2026-05-19] watchdog | Log duplicate header fix + orphan timestamp cleanup

### Auto-fixed
- wiki/log.md — Removed duplicate `# Wiki Log` header at line 280 (second occurrence)
- wiki/log.md — Removed 2 orphaned `###` timestamp lines that duplicated `## [YYYY-MM-DD]` entries

## [2026-05-19] hermes | Create judgment-list concept page from Doug Turnbull article

### Created
- `wiki/raw/articles/2021-02-21_softwaredoug_judgment-list.md` — Saved Doug Turnbull's "What Is a Judgment List?" article (published 2021-02-21)
- `wiki/concepts/judgment-list.md` — New concept page: Judgment List methodology for search relevance evaluation

### Updated
- `wiki/index.md` — Added judgment-list entry under Concepts
- `wiki/entities/doug-turnbull.md` — Added [[concepts/judgment-list]] cross-link in Related section
- `wiki/concepts/ndcg.md` — Added [[concepts/judgment-list]] cross-link in See Also
- wiki/log.md — Removed 1 orphaned orphan `###` timestamp line (OPSD article ingestion)

### Verified (no issues)
- validate_index.py: clean ✓
- Index corruption: 0 pipe prefix, 0 triple bracket, 0 line-number prefix
- All 5 section headers present: Entities, Concepts, Events, Comparisons, Queries

### Findings (needs human review)
- **Index header count mismatch**: Entities reported 628 (actual 620), Concepts 1370 (actual 1285), Comparisons 17 (actual 19) — stale header math
- **862 pages not indexed** (per header claim): 75.3% of unindexed are in concepts/
- **Pipeline**: x_accounts reported stale (26h) but runs every 48h — within normal cycle

---

## [2026-05-19] ingest | Cloudflare Project Glasswing article → entities/cloudflare, concepts/cyber-frontier-models, enrich glasswing + vuln-detection pages

### Summary
- **Raw article ingested**: `blog.cloudflare.com--2026-05-18_cyber-frontier-models--9cce0b5a.md` — Cloudflare CSO Grant Bourzikas: Project Glasswing experience with Mythos Preview on 50+ internal repos
- **NEW entity page**: [[entities/cloudflare]] — Global cloud platform, Project Glasswing participant, published definitive harness architecture (Recon→Hunt→Validate→Gapfill→Dedupe→Trace→Feedback→Report)
- **NEW concept page**: [[concepts/cyber-frontier-models]] — Class of security-focused frontier LLMs with exploit chain construction + PoC generation; coined by Cloudflare
- **Enriched**: [[concepts/claude-mythos-glasswing]] — Added Cloudflare Testing Results (May 2026) section: key findings, organic refusals inconsistency, signal-to-noise problem, harness architecture, why generic coding agents fail
- **Enriched**: [[concepts/ai-vulnerability-detection-at-scale]] — Added Cloudflare Case Study (May 2026): 8-stage harness design, 4 core harness principles, "patch faster isn't enough" argument
- **Wiki index**: +2 pages (2025→2028 total), updated cloudflare description

## [2026-05-19] x-bookmarks-ingest | context-lock-in concept, ashwingop + sentra-app enrichment

### Summary
- **X Article ingested**: "Rent the Intelligence. Own the Context." by Ashwin Gopinath (@ashwingop), May 17, 2026. Full body fetched via xurl `tweet.fields=article`. → [[raw/articles/2026-05-17_rent-intelligence-own-context.md]]
- **NEW concept page**: [[concepts/context-lock-in]] — AIの第三フェーズ競争（Model→Agent→Context）。モデルロックインより危険な文脈ロックイン。Gopinathの三フェーズモデル、Microsoft構造的アナロジー、MCPの両義性分析、フォワードデプロイメントの依存性分析。「知能はレンタル、コンテキストは所有」。
- **Enriched**: [[concepts/contextmaxxing]] — Added Context Lock-In section as competitive consequence, updated sources/related/tags
- **Enriched**: [[entities/ashwingop]] — Added blog post entry, Three-Phase Model of AI Competition section, updated sources/tags/X Activity Themes
- **Enriched**: [[entities/sentra-app]] — Added context-lock-in as related concept + framing as neutral context layer, updated sources/tags
- **Wiki index**: +1 concept page (2022→2023 total, 1368→1369 concepts)

## [2026-05-19] active-crawl | Starchild-1, HRM-Text, SANA-WM, Mastra ACP

### Summary
- Active crawl discovered 4 trending AI/ML topics not yet in the wiki
- ★★★★★ Odyssey ML: Starchild-1 — first real-time multimodal world model (audio+video)
- ★★★★★ Sapient Intelligence: HRM-Text — 1B non-Transformer reasoning model, $1K training
- ★★★★☆ NVIDIA SANA-WM — 2.6B open-source world model, single-GPU 60s 720p
- ★★★☆☆ Mastra @mastra/acp — ACP-compatible coding agents as tools/subagents

### Pages Created
- [[entities/odyssey-ml]] — Odyssey ML company
- [[entities/sapient-intelligence]] — Sapient Intelligence company
- [[entities/mastra]] — Mastra AI agent framework
- [[concepts/starchild-1]] — Real-time multimodal world model
- [[concepts/hrm-text]] — Hierarchical reasoning model
- [[concepts/sana-vm]] — NVIDIA open-source world model
- [[concepts/mastra-acp-agents]] — ACP agents in Mastra

### Raw Articles Saved
- raw/articles/2026-05-17_odyssey-starchild-1.md
- raw/articles/2026-05-18_sapient-intelligence-hrm-text.md
- raw/articles/2026-05-16_nvidia-sana-wm.md
- raw/articles/2026-05-14_mastra-acp-agents.md

---

## [2026-05-19] blog ingest | Simon Willison PyCon lightning talk + OpenAI trial verdict + Dr. Manhattan Syndrome

### Summary
- Blog ingest pipeline: 36 new articles detected, 16 saved to raw, 4 unsaved (paywalled/video)
- ★★★★★ Simon Willison: "The last six months in LLMs in five minutes" (PyCon US 2026) → [[concepts/llm-landscape-nov-2025-to-may-2026]]
- ★★★★☆ Gary Marcus: "The AI trial of the century ends with a whimper" → [[events/openai-musk-trial-verdict-2026]], enriched [[entities/gary-marcus]]
- ★★★★☆ Person Familiar: "AI, Humanity, and Dr. Manhattan Syndrome" → [[concepts/dr-manhattan-syndrome-ai]]
- Enriched [[entities/simon-willison]] with lightning talk entry

### Pages Created
- [[concepts/llm-landscape-nov-2025-to-may-2026]] — Six-month LLM landscape review: model race, RLVR coding agents, OpenClaw ecosystem, Gemma 4, GLM-5.1
- [[concepts/dr-manhattan-syndrome-ai]] — AI leadership communication pathology: abstract "Humanity" rhetoric disconnected from actual people
- [[events/openai-musk-trial-verdict-2026]] — Jury unanimously rejects Musk's claims; statute of limitations, no ruling on OpenAI legitimacy

### Pages Enriched
- [[entities/simon-willison]] — Added PyCon 2026 lightning talk, updated sources
- [[entities/gary-marcus]] — Added trial verdict piece, updated sources

### Non-AI Raw Articles Saved
- it-notes.dragas.net: FediMeteo/HAProxy/snac threading
- krebsonsecurity.com: CISA AWS GovCloud key leak
- ericmigi.com: Index 01 hardware production update
- gilesthomas.com: 10Gb Ethernet SFP+ heatsinks
- entropicthoughts.com: Pythagorean Addition
- dfarq.homeip.net: Cyberrebate.com dotcom history
- devblogs.microsoft.com: parity flag debugging
- daringfireball.net linked: Gallup AI data center poll, NYT Apple/OpenAI articles
- om.co: John Appleseed
- workos.com: Sponsor content (Pipes API)

### Unsaved Articles (4)
- NYT: Jury Rejects Elon Musk's Claim (paywalled)
- NYT: How Apple Became a $4T Company (paywalled)
- YouTube: Ted Turner's Apartment (video)
- Wikipedia: Alaska Permanent Fund (encyclopedia)

## [2026-05-19] ingest | ECHO: Terminal Agents Learn World Models for Free (X Article)

### Summary
- Discord user request (kzinmr): X Article by @DimitrisPapail on ECHO RL training method → created entity pages + concept pages + raw article.
- Source: https://x.com/DimitrisPapail/status/2056368948870811746

### Pages Created
- [[entities/dimitris-papailiopoulos]] — Dimitris Papailiopoulos, MSR AI Frontiers / UW-Madison researcher, co-author of ECHO
- [[entities/vaishnavi-shrivastava]] — Vaishnavi Shrivastava (@VaishShrivas), MSR AI Frontiers researcher, lead author of ECHO
- [[concepts/echo-rl]] — ECHO: hybrid GRPO + environment-prediction training for CLI agents, learns world models from terminal responses
- [[concepts/world-models-for-agents]] — World models for AI agents: learning environment dynamics through response prediction
- [[raw/articles/2026-05-18_dimitris-papailiopoulos_echo-terminal-agents-world-models]] — raw X Article

### Key Findings from ECHO
- TerminalBench-2.0 pass@1 nearly doubles (8B: 2.7→5.2, 14B: 5.2→10.8) at zero extra cost
- Training 2.3× faster to same performance
- Can substitute for expert SFT (recovers up to 104% of SFT gain)
- Enables verifier-free self-improvement (+3.8-10.0 pp without reward signal)

### Index
- `index.md`: +2 entities (624 pages), +2 concepts (1364 pages), Total 2011 pages
- Papers index: arxiv:2510.16907 registered

### Cross-references
- [[echo-rl]] → [[entities/dimitris-papailiopoulos]], [[entities/vaishnavi-shrivastava]], [[world-models-for-agents]]
- [[world-models-for-agents]] → [[echo-rl]], [[entities/dimitris-papailiopoulos]], [[entities/vaishnavi-shrivastava]]

---

## [2026-05-19] dreaming | ElevenLabs Claude Code integration enrichment + triage JSON

### Pages Enriched
- [[entities/elevenlabs]] — Added Claude Code Integration (May 2026) section: Skill-based setup, KB RAG, workflow routing, tool categories, guardrails, testing framework, telephony integrations, 75ms latency. Full tutorial coverage.
- `wiki/index.md` — Updated elevenlabs entry with Claude Code integration info

### Raw Articles Referenced
- `raw/articles/2026-05-19_elevenlabs_building-elevenagents-with-claude-code.md`

### Notes
- dreaming-group pre-run failed (JSON parse error) — triage performed autonomously
- dreaming-collect reported collected_articles=0 (all today's content consumed by other pipelines)
- Only genuine gap: ElevenLabs entity enrichment (was 44 lines, now enriched with Claude Code section)

---

## [2026-05-19] newsletter ingest | Import AI 457 + Lenny's Podcast

### Summary
- Newsletter wiki-ingest pipeline: 4 take, 1 reference, 4 skip from triage checkpoint
- ★★★★★ Thariq Shihipar: "HTML is the new Markdown" — Lenny's Podcast live at Anthropic → enriched [[entities/thariq-shihipar]], [[concepts/ai-output-format-progression]]
- ★★★★☆ Aurora Optimizer (Tilde Research): fixes Muon neuron death, 1.1B scale, MMLU +10pts → [[concepts/aurora-optimizer]]
- ★★★★☆ Prime Intellect autonomous speedrunning: Codex + Claude Code beat human baseline on nanoGPT → enriched [[entities/prime-intellect]]
- ★★★☆☆ Positive Alignment (Oxford/DeepMind/OpenAI/Anthropic/Stanford): from stub → [[concepts/ai-alignment]]
- Reference: fast16 AI Stuxnet analogy → [[concepts/ai-safety]]

### Pages Created
- [[concepts/aurora-optimizer]] — Leverage-aware optimizer for rectangular matrices. Fixes Muon's hidden neuron death problem.

### Pages Enriched
- [[entities/thariq-shihipar]] — Lenny's Podcast section: "HTML is the new Markdown", compute allocator paradigm, 9 key takeaways
- [[concepts/ai-output-format-progression]] — Compute allocator shift subsection
- [[concepts/ai-alignment]] — Enriched from stub: Positive vs Negative Alignment, flourishing science, governance design
- [[entities/prime-intellect]] — Autonomous speedrunning experiment section (Codex/Claude Code, 10k runs, 14k H200 hours)
- [[concepts/ai-safety]] — fast16 virus as AI-generated sabotage scenario blueprint

### Pages Updated (index)
- Index: new entry for aurora-optimizer, updated ai-alignment description, total pages 2014→2015

### Sources
- Import AI 457 (Jack Clark): [[raw/newsletters/2026-05-18-import-ai-457-ai-stuxnet-cursed-muon-optimizer-and-positive-alignment.md]]
- Lenny's Podcast: [[raw/newsletters/2026-05-18-how-i-ai-html-is-the-new-markdown-how-anthropic-engineers-are-building-with-clau.md]]
- Aurora blog: https://blog.tilderesearch.com/blog/aurora
- Positive Alignment: https://arxiv.org/abs/2605.10310
- Prime Intellect speedrun: https://github.com/PrimeIntellect-ai/experiments-autonomous-speedrunning

---



## [2026-05-19] ingest | Llama 3 Herd of Models (arXiv:2407.21783) — landmark paper

### Summary
- Discord user request (kzinmr): arXiv:2407.21783 as landmark paper of LLM development stage in 2024
- Saved raw paper: `wiki/raw/papers/2024-07-23_2407.21783_llama-3-herd-of-models.md`
- Created entity page: `wiki/entities/llama-3.md` — Llama 3/3.1 model family, 405B dense Transformer, GPT-4 competitive
- Created concept page: `wiki/concepts/llm-development-paradigm.md` — two-stage development paradigm (pre-training → SFT+RS+DPO)
- china-briefing.com article ingestion was canceled per user request
- Updated `wiki/index.md` (+2 entries, Entities 622, Concepts 1362)

## [2026-05-19] ingest | China OpenClaw Agentic AI Boom (China Briefing article)

### Summary
- Discord user request (kzinmr): China Briefing article on OpenClaw's 2026 viral adoption in China → created comprehensive concept page + raw article + enriched existing entity.

### Pages Created
- [[concepts/china-openclaw-agentic-boom]] — 中国でのOpenClaw爆発的普及現象を包括的にカバー。3つの構造的要因（世界最安API・DeepSeek効果・推論需要シフト）、ClawHub/skills.shスキルエコシステムとセキュリティ危機（13%脆弱性、13.5万露出インスタンス）、クラウド5社同時争奪戦（Tencent QClaw/WorkBuddy/ClawPro、ByteDance公式中国ミラー、Alibaba Qwen統合3億MAU）、政府補助金（深センOPC向け$1.4M）、AIoT収束（Xiaomi/Huawei）、外資系企業への示唆をカバー。
- [[raw/articles/2026-04-14_china-briefing_china-agentic-ai-openclaw-boom]] — 生記事（Giulia Interesse, April 14, 2026）

### Pages Updated
- [[entities/openclaw]] — **China Adoption & Market Impact**セクション追加。タグに`china`, `agent-security`追加。Media & PressにChina Briefing記事リンク追加。frontmatter updated, source追加。

### Index
- `index.md`: +1 conceptsエントリ（china-openclaw-agentic-boom）

### Cross-references
- [[entities/openclaw]] → [[concepts/china-openclaw-agentic-boom]]
- [[concepts/china-openclaw-agentic-boom]] → [[entities/openclaw]], [[entities/deepseek]], [[concepts/china-agentic-coding-sprint]], [[concepts/us-china-ai-competition]], [[concepts/zero-trust-agentic-ai]], [[concepts/agentic-ai-governance]], [[entities/minimax]], [[entities/kimi]], [[concepts/local-llm/model-distillation]], [[comparisons/hermes-vs-openclaw-architecture]]

---
## [2026-05-18] ingest | X bookmarks — Pi Coding Agent metadata-only record

### Summary
- 2 new bookmarks processed from X. 1 skipped (startup accelerators, not AI-aligned).
- [[entities/pi]] — X article "Pi Coding Agent 最全面指南（完美支持/goal）" could not be fetched (HTTP 500). Saved metadata-only record.

### Changes
- `raw/articles/x-article-2056043868077096960-pi-coding-agent-guide.md` — Metadata-only record: X article about Pi Coding Agent comprehensive guide with `/goal` support. Content inaccessible due to X API HTTP 500 error. Records title, URL, and fetch failure details for later retrieval.
- `entities/pi.md` already has comprehensive coverage — no enrichment needed from inaccessible source.

### Notes
- Bookmark 2/2 skipped: tweet about startup accelerators (YC, a16z Speedrun, Techstars, Founders Inc) — not AI/LLM aligned per SCHEMA.md.

---

## [2026-05-18] ingest | Raw article: Doug Turnbull "Can Agents Replace the Search Stack?"

- `raw/articles/2026-04-28_softwaredoug_search-apis-replaced-by-agents.md` — New raw article: Doug Turnbull's comprehensive experiment showing LLM agents (GPT-5-mini + BM25 + E5) achieve 0.453 NDCG on Amazon ESCI (+56.7% vs BM25 0.289), with no data-specific tuning. Covers agent exploration constraints (min 4 calls, similarity filtering), SID-1 agentic search models, and the critical distinction between "finding things" vs "deep research."
- [[concepts/agentic-search]] — Updated source link from external URL to raw article wikilink.

---

## [2026-05-18] dreaming | Nightly knowledge consolidation

### Pages Created
- [[concepts/agent-first-design]] — Full concept page replacing stub. Covers Armin Ronacher's "A Language For Agents" thesis (8 design principles) and Vercel Zero as concrete implementation.
- [[entities/vercel-labs]] — New entity page for Vercel Labs R&D division and its Zero programming language.

### Pages Updated
- [[entities/doug-turnbull]] — Added "Don't waste too much time on the original RAG paradigm" blog post (Apr 2026) to Recent Blog Posts.
- [[entities/daringfireball-net]] — Added "AI Is Technology, Not a Product" (May 2026) to Recent Themes and References.

### Sources
- raw/articles/2026-05-18_armin-ronacher_a-language-for-agents.md
- raw/articles/2026-05-18_vercel-labs_zero-language-for-agents.md
- raw/articles/2026-04-21_softwaredoug_dont-waste-time-on-rag-paradigm.md
- raw/articles/daringfireball.net--2026-05-ai-is-technology-not-a-product--d7845d6d.md

### Notes
- Triaged from dreaming pipeline (collect reported 0 articles but scanned 97 untriaged raw articles). Existing triage at dreaming/triage_latest.json was consumed.
- Entities/seangoedecke-com.md, entities/dwarkesh-patel.md, entities/armin-ronacher.md already had substantive coverage of their respective articles — no enrichment needed.
- Entity date bumps: entities/doug-turnbull.md (2026-04-10→2026-05-18), entities/daringfireball-net.md (2026-04-24→2026-05-18).
- 2 source articles skipped per triage (OpenClaw naming, non-AI articles).
- Index counts updated.

---

## [2026-05-18] tag-audit | Weekly tag taxonomy audit & auto-fix

### Changes
- Added `psychology` to SCHEMA.md Domain Concepts taxonomy (new canonical tag)
- Added 19 new mappings to TAG_NORMALIZATION dict (pipeline→devops, swe-bench→benchmark, logic→reasoning, symbolic-ai→neurosymbolic, history→timeline, agent-sandboxing→sandbox, datasette→tool, pattern→design-patterns, cognitive-science→psychology, academic→research, case-study→methodology, instruction-tuning→fine-tuning, memory-efficiency→optimization, knowledge-management→information-retrieval, understanding-code→code-intelligence, vector-database→vector-search, computer-history→timeline)
- Deleted one-off tag `modules` from concepts/dspy-modules.md
- Fixed dgx-spark→hardware in entities/nvidia-nemoclaw.md + concepts/local-llm/server-dgx-spark.md (missed by script due to inline format bug)
- Fixed regex bug in tag_normalization.py: tags on last frontmatter line not matched (no trailing \n)
- Added content-comparison guard to prevent phantom modifications

### Results
- 193 pages modified by normalization script
- Coverage improved: 62.6% → 72.3%
- Non-SCHEMA tags: 227 → 207
- Unique tags: 553 → 480
- Composite kebab-case tags: 0 (unchanged)

---

## [2026-05-18] health-fix | Wiki health auto-fix

### Fixes Applied
- Removed ghost entry `[[entities/_index]]` from index.md (no file exists)
- Added 20 orphan concept pages to index.md (first alphabetically: `ai-agents-autonomy-*` through `ai-infrastructure-engineering/model-serving-autoscaling`)
- Restored missing `## Events (3 pages)` section header
- Updated header counts: Entities: 627→621, Concepts: 1370→1361

### Index Stats (Post-Fix)
- Total pages: 2005
- Indexed entries: 1148
- Not in index: 857 (908 orphans minus 20 added minus 1 ghost removed)
- validate_index.py: clean ✅

---


## [2026-05-18] watchdog | Index header count correction

### Auto-fixed
- wiki/index.md — Corrected header counts from 2023/1073/927 to 2005/1096/909 (verified via os.walk)

### Findings (needs human review)
- **4 duplicate entity pairs**: deliberate-coder/deliberatecoder, eugene-yan/eugeneyan, 
  lilian-weng/lilianweng, samuel-colvin/samuelcolvin — non-canonical slugs have more content in 3/4 cases
- **665 bare wikilinks** (no namespace prefix) — 1083 total occurrences
- **386 broken wikilinks** pointing to non-existent pages — 580 total occurrences
- **909 unindexed pages** (45% of L2) — mostly concepts/ subdirectory files

---

## [2026-05-18] manual | agentmemory entity page + iii-platform update

### Pages Created (2)
- [[entities/agentmemory]] — Persistent memory for AI coding agents built on iii-engine. 12 lifecycle hooks, BM25+vector+graph RRF retrieval (R@5: 95.2%), 4-tier Ebbinghaus-style memory consolidation. 51 MCP tools, works with Claude Code/Codex/Cursor/Hermes/OpenClaw/pi/OpenCode. 12K GitHub stars, Apache-2.0.
- `wiki/raw/articles/2026-05-18_agentmemory-persistent-memory-for-coding-agents.md` — Raw article from GitHub README + AlphaSignal deep-dive

### Pages Updated (1)
- [[entities/iii-platform]] — Added [[entities/agentmemory]] to Related section as the most prominent application built on iii-engine

---

## [2026-05-18] manual | BM25/PI-SERINI concept + entity pages from RecSys newsletter

### Pages Created (2)
- [[concepts/bm25]] — BM25 lexical retrieval algorithm: PI-SERINI shows BM25 + LLM agentic loop beats dense retrievers (83.1% BrowseComp-Plus accuracy, 3.3x–10x cheaper via prefix caching)
- [[entities/pi-serini]] — Minimal search agent: BM25 + LLM in agentic loop. Tuned BM25 (k1=25, b=1), wall-clock budget (300s), prefix-cache-friendly (82-90% cache hit rate). Hsu et al., arXiv:2605.10848

### Pages Updated (1)
- [[concepts/bm25]] — Enriched with PI-SERINI architecture details, BrowseComp-Plus benchmark results, failure mode analysis, and cost efficiency data

### Raw Articles (1)
- raw/articles/2026-05-15_recsys_bm25-agentic-deep-research.md

### Sources
- https://recsys.substack.com/p/is-bm25-enough-for-agentic-deep-research
- https://arxiv.org/abs/2605.10848
- https://github.com/justram/pi-serini
## [2026-05-18] active-crawl | AWS-OpenAI, Perceptron AI, SAP/Anthropic, AWS Agent Toolkit, Google AI Pointer

### Pages Created (6)
- [[entities/perceptron-ai]] — Physical AI research lab, Perceptron Mk1 model
- [[concepts/perceptron-mk1]] — Video understanding + embodied reasoning model
- [[entities/sap-business-ai-platform]] — SAP's unified enterprise AI platform
- [[concepts/aws-openai-bedrock-partnership]] — OpenAI models on Bedrock, Bedrock Managed Agents
- [[concepts/aws-agent-toolkit]] — 40+ agent skills, managed MCP server for AWS
- [[concepts/google-ai-pointer]] — DeepMind's AI-enabled pointer (Magic Pointer)

### Raw Articles (5)
- raw/articles/2026-05-18_aws-openai-bedrock-partnership.md
- raw/articles/2026-05-18_perceptron-ai-mk1.md
- raw/articles/2026-05-18_sap-anthropic-claude-business-ai-platform.md
- raw/articles/2026-05-18_aws-agent-toolkit.md
- raw/articles/2026-05-18_google-deepmind-ai-pointer.md

### Sources
- https://www.aboutamazon.com/news/aws/bedrock-openai-models
- https://finance.yahoo.com/sectors/technology/articles/perceptron-ai-launches-physical-ai-153000413.html
- https://news.sap.com/2026/05/sap-anthropic-to-bring-claude-sap-business-ai-platform/
- https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/
- https://deepmind.google/blog/ai-pointer/

---


Ingested "Self-Distilled Reasoner: On-Policy Self-Distillation" by Siyan Zhao et al. (UCLA/Meta Superintelligence Labs, 2026) from siyan-zhao.github.io.

### Changes
- `wiki/raw/articles/2026-05-18_siyan-zhao_opsd-self-distilled-reasoner.md` — New raw article. OPSD uses same model as student + teacher (with ground-truth as privileged context), JSD_β divergence, full-vocabulary distribution matching. ≥ GRPO at 1/64 token cost.
- `wiki/concepts/on-policy-self-distillation.md` — **New concept page** (status: complete). Full coverage: OPSD mechanism (3-step training, JSD_β loss, KL clipping), policy-gradient interpretation (comparison with STaR), experimental results, relationship to OPD and SDAR.
- `wiki/entities/siyan-zhao.md` — **New entity page** (status: stub). UCLA/Meta researcher, lead author of OPSD.
- `wiki/concepts/on-policy-distillation.md` — Replaced "OPSD" section with comprehensive **OPD vs OPSD comparison table**: origin, teacher type, divergence, domain, key insight. Added cross-references to both OPSD and SDAR.
- `wiki/concepts/sdar-self-distilled-agentic-rl.md` — Added OPSD paper to sources, added `on-policy-self-distillation` to related pages, added OPSD as foundational technique in Related Pages section.
- `wiki/index.md` — Added OPSD concept entry + Siyan Zhao entity entry.
- `wiki/log.md` — This entry.

---
## [2026-05-18] ingest | The Signal + Superintel newsletters (May 17)

### Pages Created (3)
- [[entities/figure-ai]] — Figure AI humanoid robotics, Helix-02 VLA model
- [[entities/isomorphic-labs]] — AI drug discovery, $2.1B Series B
- [[concepts/forward-deployed-engineering]] — FDE paradigm: deployment as moat

### Pages Updated (5)
- [[concepts/agent-governance]] — Added multi-owner agent economy & governance gaps (Superintel analysis)
- [[concepts/model-context-protocol-mcp]] — Added security vulnerabilities & OX Security findings
- [[entities/google]] — Added Gemini Intelligence, Magic Pointer, Project Suncatcher
- [[entities/openai]] — Added Daybreak cybersecurity, Codex Mobile, Plaid integration
- [[entities/anthropic]] — Added PwC certification, Ramp AI Index, 4 fronts paper, Colossus 1

### Sources
- raw/newsletters/2026-05-17-the-agentic-economy-has-no-black-box.md
- raw/newsletters/2026-05-17-anthropic-pulls-away-openai-strikes-back-and-google-s-gemini-rising.md

## [2026-05-18] blog-ingest | Gary Marcus neurosymbolic AI, Sean Goedecke ZIRP engineer, OpenAI Codex for Work

- **Updated**: `wiki/entities/gary-marcus.md` — Added "The illusion of Generative AI" (May 2026): neurosymbolic AI advocacy, world models case, hyperscaling critique. Three interviews: Brian Greene (World Science Festival), Zachary Karabell (Web Summit), Will Wilson/Antithesis (Bug Bash 2026). Added tags: neurosymbolic, world-models, ai-safety.
- **Updated**: `wiki/entities/seangoedecke-com.md` — Added "The just-say-no engineer was a ZIRP phenomenon" (May 2026). Analysis of the senior engineer archetype that thrived under zero-interest rates and is now threatened; AI is a red herring — the real cause is the end of ZIRP. Pure vs. impure engineering distinction.
- **Updated**: `wiki/entities/openai-codex.md` — Added "Codex for Work" section (May 2026): team use cases for data science (KPI root-cause analysis, business impact readouts, analytics request agent, executive KPI memos, dashboard builder), business operations, and sales teams. Plugin-based architecture (Google Workspace, Slack). Added tags: data-science, bizops.
- **Updated**: `wiki/index.md` — Refreshed summaries for gary-marcus, openai-codex entries. Bumped date to 2026-05-18.
- **Skipped**: 13 non-AI-relevant articles (LWN kernel updates, Star Wars essay, NHS open-source politics, Joan Westenberg creativity essay, Troy Hunt weekly update)
- **Raw articles**: 10 saved (3 processed into wiki)

## [2026-05-18] ingest | Self-Distilled Agentic RL (SDAR) Paper

Ingested arXiv:2605.15155 "Self-Distilled Agentic Reinforcement Learning (SDAR)" by Zhengxi Lu et al. (ZJU/Meituan/Tsinghua).

### Changes
- `wiki/raw/papers/2026-05-18_2605.15155_sdar-self-distilled-agentic-rl.md` — New raw paper. SDAR combines GRPO with gated OPSD for stable multi-turn agent training. +9.4% ALFWorld, +7.0% Search-QA, +10.2% WebShop Acc over GRPO.
- `wiki/concepts/sdar-self-distilled-agentic-rl.md` — **New concept page** (status: complete). Full coverage: motivation (2 critical observations), method (sigmoid gating, 3 strategies, theoretical properties), results table (3 models × 3 benchmarks), relationship matrix (GRPO/OPD/MOPD/SDAR comparison), implementation details.
- `wiki/concepts/grpo-rl-training.md` — **Enriched from stub to complete**. Added: GRPO mechanism (advantage computation, advantages/limitations), GRPO as RL backbone table (vanilla/MOPD/SDAR/Skill-GRPO), SDAR relationship section. Updated tags, sources, related pages. Status: stub → complete.
- `wiki/concepts/on-policy-distillation.md` — Added SDAR reference in Related Pages + new "OPSD: On-Policy Self-Distillation" section explaining the difference between OPD (stronger teacher) and OPSD (same-policy teacher with privileged context).
- `wiki/index.md` — Updated GRPO entry with full description. Added SDAR entry.
- `wiki/log.md` — This entry.
- `scripts/papers_index.py` — Registered arXiv:2605.15155.

## [2026-05-18] Stale directory cleanup — /opt/data/home/ → canonical merge

**Context**: Subagents wrote to `/opt/data/home/wiki/` instead of canonical `/opt/data/wiki/`. Manual merge operation.

### New pages created (copy from stale)
- **concepts/agent-observability-feedback.md** — Agent observability feedback loops (Arize, Aaron Kaplowitz)
- **concepts/speculative-decoding-mtp.md** — MTP drafter heads in Gemma 4, speculative decoding comparison
- **concepts/subagent-patterns.md** — 4 subagent coordination patterns (Sarah Chieng @MilksandMatcha)
- **entities/brian-armstrong.md** — Coinbase CEO, AI-driven restructuring letter (May 2026)
- **entities/richard-susskind.md** — Legal technology expert, AI in law

### Pages enriched (merge)
- **concepts/automation-series.md** — Added tags: workflow-design, deterministic, probabilistic, ai-automation
- **entities/antoine-buteau.md** — Added tags: bizops, automation-architecture, strategy-execution, technical-literacy
- **entities/factory.md** — Major enrichment: merged comprehensive 113-line stale version with canonical. Added Droids platform details, products, enterprise customers, competitive landscape, SWE-Bench debate, strategic outlook, founders background (Eno Reyes as CTO), McKinsey partnership.

### Raw articles migrated (17 files)
- 10× Antoine Buteau Automation Series articles
- 5× agent/LLM articles (agent-observability, gemma-4-drafter, subagent-patterns, layoffs-ai)
- 2× other articles (how-to-think-using-ai)

### Skipped (canonical richer, stale outdated)
- concepts/peoplereadmes.md (canon 152 > stale 119)
- entities/eric-zhang.md (canon 204 >> stale 48)
- entities/harrison-chase.md (canon 141 > stale 91)
- entities/muratcan-koylan.md (canon 162 > stale 92)
- entities/philipp-schmid.md (canon 188 >> stale 70)
- entities/riley-walz.md (canon 107 > stale 87, better structure)
- entities/0xsero.md → sero.md (canon 251 >> stale 35)

### Index updated
- Entities: 620 → 622, Concepts: 1362 → 1365
- New index entries for all new + enriched pages

---

## [2026-05-17] x-accounts-scan | X account scan — 3 new posts → 4 wiki pages created

**Pipeline**: x-accounts-scan (cron, 22:30 UTC)

### Posts Processed
- @koylanai: 2 posts about peoplereadmes (open-source persona context systems, first persona: Riley Walz)
- @ekzhang1: 1 post about Harvard Math Department documentary (not directly AI-relevant, noted)

### Pages Created
- `entities/riley-walz.md` — Riley Walz (@rtwlz): Software engineer and internet artist, OAI Labs at OpenAI (2026–). Bop Spotter, Jmail, IMG_0001, Find My Parking Cops. 7,248 bytes.
- `entities/muratcan-koylan.md` — Muratcan Koylan (@koylanai): Context Engineer at Sully.ai. Creator of Agent Skills for Context Engineering (15.6K ⭐), peoplereadmes, Personal Brain OS. 6,882 bytes.
- `concepts/peoplereadmes.md` — Open-source framework for persona context systems to study how exceptional technical builders operate. Pipeline: public evidence → source map → project analysis → tacit-knowledge extraction → technical model → prompt system → eval rubric. 5,634 bytes.
- `entities/eric-zhang.md` — Eric Zhang (@ekzhang1): MTS at Thinking Machines Lab. Creator of sshx. Status: skeleton. 1,977 bytes.

### Index Updates
- `wiki/index.md` — Added muratcan-koylan and eric-zhang entities; peoplereadmes concept. Entity count: 618→620, Concept count: 1361→1362.

### Sources Used
- GitHub (muratcankoylan/peoplereadmes), Wikipedia (Riley Walz), Wired (Riley Walz profile), muratcankoylan.com, ekzhang.com, X/Twitter profiles

---

## [2026-05-17] skeleton-enrich-daily | Daily skeleton enrichment — no skeletons found, enriched 2 stub entities

**Status**: No `status: skeleton` entity pages found. Enriched 2 `status: stub` entity pages as fallback.

### Pages Enriched
- `entities/steve-blank.md` — Full enrichment: biography, career timeline (USAF → E.piphany → Lean Startup → Stanford professor), books, Customer Development methodology, Lean Startup movement, Hacking for Defense, Secret History of Silicon Valley. Removed empty table; added proper sources, tags, cross-references.
- `entities/jason-liu.md` — Full enrichment: biography, career timeline (567 Studios → OpenAI Codex → Stitch Fix → Meta), Instructor library (6M+ monthly downloads, cited by OpenAI), training programs (Maven), angel investing (a16z scout), key theses, publications (CSCW 2017, AAAI 2016). Added proper sources, aliases, cross-references.

### Index Updates
- `wiki/index.md` — Updated descriptions for both entries (line 265: [[entities/jason-liu]], line 439: [[entities/steve-blank]])

### Sources Used
- Wikipedia (Steve Blank), steveblank.com, CXOTalk, Computer History Museum
- jxnl.co, github.com/jxnl, python.useinstructor.com

---

## [2026-05-17] dreaming | Knowledge consolidation — 5 entity enrichments from raw articles

**Pipeline**: dreaming-wiki-ingest (failed parsing → raw article fallback)

### Sources
- raw/articles/2026-05-16_harvey_building-an-agentic-security-operations-center.md — Harvey Agentic SOC
- raw/articles/2026-05-15_glean_cowork-mcp-eval.md — Glean MCP vs Cowork benchmark
- raw/articles/2026-05-14_petradonka_agents-need-feedback-loops.md — Warp Buzz agent deep dive
- raw/articles/2026-05-16_hex-technologies_repos-as-agent-context.md — Hex repos as context
- raw/articles/2026-05-15_decagon_inside-agent-engineering-at-decagon.md — Decagon agent engineering

### Pages Enriched
- `entities/harvey.md` — Added Agentic SOC section (world model, MCP via RunReveal, 400+ detections, 95% alert reduction, Mike Parowski)
- `entities/petra-donka.md` — Added Buzz agent architecture (principles over rules, 5-step learning, daily PR workflow, Oz orchestration, skill-as-code)
- `entities/glean.md` — Added MCP vs Cowork benchmark (2.5x preference, 30% fewer tokens, federated search token tax)
- `entities/hex-technologies.md` — Added repos as agent context (dbt repo, application repo, compounding context)
- `entities/decagon.md` — Added agent engineering at Decagon (ASWE role, customer outcomes, cross-functional work)

### Cross-pipeline Status
- blog-triage: 1 take (Sean Goedecke, already processed by downstream)
- newsletter-triage: 40 decisions, all skip (0 takes)
- active-crawl: Already ran today (GPT-Realtime Voice, Claude Orbit, Gemini Flash-Lite)
- dreaming-group: JSON parse failure; no themes available (19 days stale)

---

## [2026-05-17] health-fix | Index orphan registration (20 pages added to index.md)

### Changes
- Added 7 orphan entity pages to index.md: cerebras-systems, datasette-llm-limits, dynomight-net, ed-zitron-s-where-s-your-ed-at, fred-schott, john-berryman, kim-isenberg
- Added 13 orphan concept pages to index.md: ai-and-authenticity, ai-and-software-engineering, ai-api-abuse, ai-assisted-development, ai-coding-agent-criticism, ai-image-generation, ai-observability, ai-programming-as-theory-building, ai-vulnerability-discovery, blogging-as-infrastructure, boring-technology, coding-agents, cognition-devin-philosophy
- Index corruption check: CLEAN (no pipe/line-number/triple-bracket/space-prefix corruption)
- Ghost entries: NONE
- validate_index.py: PASS

---

## [2026-05-17] active-crawl | OpenAI GPT-Realtime Voice Models, Claude Orbit, Gemini Flash-Lite/3.2 Flash, CAISI AI Testing

### Created (Concepts)
- **concept: gpt-realtime-voice-models.md** — OpenAI's second-gen Realtime API voice models (May 7, 2026): GPT-Realtime-2 (GPT-5-class reasoning), GPT-Realtime-Translate (70→13 languages), GPT-Realtime-Whisper (streaming STT). Three voice AI patterns.
- **concept: gemini-3-1-flash-lite.md** — Google's fastest/cost-efficient Gemini 3 series model, GA May 8, 2026. Enterprise adoption: JetBrains, Gladly (~60% lower cost, 99.6% success rate), Astrocade, krea.ai, Ramp.
- **concept: gemini-3-2-flash.md** — Google's next-gen Flash model, leaked May 5, 2026. $0.25/$2.00 per 1M tokens. "Liquid Glass" UI. Expected at Google I/O 2026 (May 19-20).
- **concept: ai-pre-release-testing.md** — US government framework for pre-deployment AI model evaluation. CAISI agreements with Microsoft, Google, xAI (May 5, 2026). Triggered by Claude Mythos cybersecurity concerns.

### Created (Entities)
- **entity: claude-orbit.md** — Anthropic's proactive assistant, leaked in Claude Cowork (May 5, 2026). Auto-generates briefings from Gmail, Slack, GitHub, Calendar, Drive, Figma. Roots in Claude Code leak's KAIROS/DREAM/ULTRAPLAN features.
- **entity: caisi.md** — Center for AI Standards and Innovation (NIST/Commerce). Signed pre-release testing agreements with Microsoft, Google, xAI. Director: Chris Fall. 40+ model evaluations. Evaluated DeepSeek V4 Pro.

### Raw Articles Saved
- raw/articles/2026-05-07_openai_gpt-realtime-voice-models.md (OpenAI blog)
- raw/articles/2026-05-05_anthropic_claude-orbit-leak.md (TestingCatalog via X)
- raw/articles/2026-05-08_google_gemini-3-1-flash-lite-ga.md (Google Cloud Blog)
- raw/articles/2026-05-05_caisi-ai-pre-release-testing.md (NIST / news aggregation)
- raw/articles/2026-05-06_gemini-3-2-flash-leak.md (BuildFastWithAI)

### Updated
- **index.md** — Added 6 entries (Entities 607→609, Concepts 1343→1347, Total 1984→1990, Indexed 1037→1043)

### Cross-References
- gpt-realtime-voice-models ↔ entities/openai, concepts/voice-ai, concepts/gpt-realtime
- gemini-3-1-flash-lite ↔ entities/google, concepts/gemini-3-flash, concepts/gemini-3-1-pro
- gemini-3-2-flash ↔ entities/google, concepts/gemini-3-1-flash-lite, concepts/gemini-3-1-pro
- ai-pre-release-testing ↔ entities/caisi, entities/anthropic, concepts/claude-mythos
- claude-orbit ↔ entities/anthropic, concepts/claude-code, concepts/autonomous-agents
- caisi ↔ concepts/ai-pre-release-testing, concepts/claude-mythos, entities/nist

### Skipped
- DeepSeek V4 (Pro/Flash) — already covered by concepts/deepseek-v4.md

---

## [2026-05-16] no-op | Newsletter wiki ingest — all 5 items already captured in entity pages

Cross-pipeline dedup: blog-wiki-ingest (07:00, 07:50) already consumed OpenAI Codex mobile, Cerebras IPO, Apple dispute, TanStack attack, and Gates Foundation partnership from RSS/blog sources before newsletter pipeline. All 19 verification checks passed.

### Already Captured
- **entities/codex.md** — Mobile Launch section (Codex in ChatGPT mobile app, secure relay, 4M+ WAU)
- **entities/openai.md** — Apple Partnership Dispute + TanStack Supply Chain Attack sections
- **entities/cerebras-systems.md** — IPO results ($280/share, $60B cap) + OpenAI 5.4/5.5
- **entities/anthropic.md** — Gates Foundation $200M partnership

---
## 2026-05-17 08:15 — Ingest "Search Evaluation (NDCG and pals)" slides by Doug Turnbull

### Created
- **entity: softwaredoug.md** — Doug Turnbull: search relevance expert, Principal Engineer at Daydream (e-commerce search). Previously Reddit, Spotify, Shopify, OpenSource Connections. Co-author of *Relevant Search* (2016) and *AI-Powered Search* (2025). Creator of Elasticsearch LTR plugin, searcharray, Quepid. Runs Maven courses: Cheat at Search Essentials, Relevant Search, Autoresearch. Philosophy: "grug-brained evals", "test in prod or live a lie".
- **concept: ndcg.md** — NDCG (Normalized Discounted Cumulative Gain): de facto search relevance metric. Full pipeline: Judgment List → DCG → iDCG → NDCG. Three judgment sources compared: human raters, clickstream (COEC model), LLM-as-judge (Umbrella prompt pattern). Six common failure modes: sparse ratings, bad iDCG, diversity blindness, UI quality blindness, data work overhead, intent interpretation. Beyond NDCG: side-by-sides, A/B tests, the "ship behind feature flag" philosophy.
- **raw article: 2026-05-17_softwaredoug_search-evaluation-ndcg.md** — Google Slides text export from "Cheat at Search Essentials" (73 slides). Source: https://docs.google.com/presentation/d/1WJknXxaim_Z8aiVuQx6wr7W6MAWeaUJK0-NrgcEVQfQ

## 2026-05-16 08:25 — Blog wiki ingest (no-op: all 17 articles already processed at 07:00)

- All 17 blog candidates already captured by the 07:00 and 07:50 UTC blog-wiki-ingest runs
- 0 takes, 0 references, 17 skips
- Triage JSON read directly from `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json` (output file parse fallback)
- Verified all claimed pages exist: entities/datasette-llm-limits.md, concepts/ai-bubble.md, entities/eric-jang.md, events/openai-may-2026-reorg.md, concepts/proof-of-useful-work.md, entities/omri-weinstein.md, entities/gary-marcus.md (updated), entities/greg-brockman.md (updated)


### Updated
- **index.md** — Added entity (softwaredoug) and concept (ndcg) entries; updated counts (Entities 606→607, Concepts 1342→1343, Total 1982→1984, Indexed 1035→1037)
- **concept: ndcg.md** — Cross-linked to [[entities/softwaredoug]]

## 2026-05-17 07:15 — Deep integration: Will Brown's OPD geometric analysis

### Updated
- **concept: on-policy-distillation.md** — Major enrichment: added Will Brown's deep analysis (~2,400 words new content). New sections: Same-Family vs Different-Family Teachers, Gradient Geometry (Sparse/Dense × Biased/Unbiased taxonomy), Self-Distillation and the Concentration Problem, Unified Meta-Algorithm (α/λ/π_T framework), Optimal Teacher Problem (Lagrangian formulation, Pareto curve). Added Will Brown's X article as source.
- **entity: will-brown.md** — Added [[concepts/on-policy-distillation]] to Related section

### Existing Links on OPD Concept
- `entities/nrehiew.md` → `[[concepts/on-policy-distillation]]` ✅
- `concepts/post-training-distributional-view.md` → `[[concepts/on-policy-distillation]]` (both frontmatter `related` + inline wikilink) ✅
- `concepts/multi-teacher-on-policy-distillation.md` → cross-reference note to `[[concepts/on-policy-distillation]]` ✅
- `concepts/model-distillation.md` → sources lists will-brown's article ✅
- `entities/thinking-machines-lab.md` → Publications section links to `[[concepts/on-policy-distillation]]` ✅

## 2026-05-17 07:05 — Ingest On-Policy Distillation (Thinking Machines primary literature)

### Created
- **concept: on-policy-distillation.md** — On-Policy Distillation (OPD): post-training technique combining on-policy sampling with dense token-level teacher supervision via reverse KL divergence. Primary literature from Kevin Lu / Thinking Machines Lab (Oct 2025, DOI: 10.64434/tml.20251026). 9-30× compute reduction vs SFT, 50-100× vs RL. Math reasoning (AIME'24), personalization, continual learning applications. Differentiation from MOPD.
- **raw article: 2025-10-27_thinkingmachines_on-policy-distillation.md** — Full 40,668-char article from thinkingmachines.ai

### Updated
- **entity: thinking-machines-lab.md** — Added Publications & Research section with OPD, LoRA Without Regret, and Defeating Nondeterminism entries. Updated Tinker product description.
- **concept: multi-teacher-on-policy-distillation.md** — Added cross-reference note linking to foundational OPD concept page.
- **wiki/index.md** — Added concepts/on-policy-distillation entry; Concepts count 1341→1342

### Dangling Links Resolved
- `[[concepts/on-policy-distillation]]` was referenced in `entities/nrehiew.md` and `concepts/post-training-distributional-view.md` — now fulfilled.

## 2026-05-17 01:30 — Ingest Anthropic 2028 AI Leadership scenarios

### Created
- **concept: us-china-ai-competition.md** — Anthropic's framework for US-China AI competition: four fronts (Intelligence, Domestic adoption, Global distribution, Resilience), compute gap analysis, export controls, distillation attacks as workarounds, two 2028 scenarios, and policy recommendations. Source: Anthropic Research (May 14, 2026)
- **raw article: 2026-05-14_anthropic_2028-ai-leadership-scenarios.md** — Full policy paper on US-China AI competition

### Updated
- **event: distillation-attacks-2026.md** — Added cross-link to us-china-ai-competition, updated tags (china, geopolitics, distillation), added sources, fixed broken wikilinks
- **SCHEMA.md** — Added `geopolitics` tag to Meta category
- **index.md** — Registered us-china-ai-competition in Concepts section

## 2026-05-16 17:50 — Health fix: index registration + header correction

### Index Registration
- Added 20 concept pages to index.md: agent-memory through ai-agents (alphabetical)
- Added 2 event pages to index.md: anthropic-code-w-claude-2026, distillation-attacks-2026

### Header Correction
- Total pages: 1901 → 1982 (actual filesystem count)
- Indexed entries: 963 → 1035
- Entities: 595 → 606
- Concepts: 1327 → 1341
- Index entries per section: entities=600, concepts=413, comparisons=18, events=3, queries=1

### Auto-fix scope
- 1 file modified: `wiki/index.md`

### Known issues (not auto-fixed)
- 947 files still not in index (gap too large for auto-apply limit of 20)
- 938 orphan pages (0 inbound wikilinks) — requires human review
- 150+ stale pages (32-37 days)
- 4 entity duplicates confirmed: deliberate-coder/deliberatecoder, eugene-yan/eugeneyan, lilian-weng/lilianweng, samuel-colvin/samuelcolvin

---

## 2026-05-16 17:35 — Watchdog auto-fix: index dedup + header correction

### Index Dedup
- Removed duplicate `[[entities/eric-jang]]` entry (line 187)
- Removed duplicate `[[entities/eric-hartford]]` entry (line 186)

### Index Header Update
- Indexed entries: 965 → 963
- Not in index: 876 → 878

### Auto-fix scope
- 1 file modified: `wiki/index.md`
- 0 new pages created, 0 pages deleted

### Issues not auto-fixed
- 4 entity duplicates confirmed (need human review for merge): deliberate-coder/deliberatecoder, eugene-yan/eugeneyan, lilian-weng/lilianweng, samuel-colvin/samuelcolvin
- 878 files not in index (index-to-filesystem gap) — requires batch reconciliation strategy
- 938 orphan pages (0 inbound wikilinks) — requires human review
- ~150 stale pages (32-37 days since last update)
- 2 unindexed event files (distillation-attacks-2026, anthropic-code-w-claude-2026)

---


> Chronological record of all wiki actions. Append-only.

## 2026-05-16 12:00 — Trending topics report (8 new topics found)

- **Grok Build CLI** — xAI初のCLIコーディングエージェント（5/14 beta）、Plan Mode・並列サブエージェント・ACP対応、SuperGrok Heavy ($300/月)向け
- **Google I/O 2026** — 5/19開催目前、Gemini 4.0 (2M+ context)、Android 17 (端末上Gemini Nano API)、エージェンティックコーディングツール発表予定
- **Notion AI Agent Platform** — 5/13発表、ワークスペース→AIエージェントハブ、Custom Agents + MCP + 外部連携、100万+エージェント構築済み
- **Anthropic Claude Agent Meter** — 全サブスクリプションでエージェント使用量測定、Managed Agents: $0.08/セッション時間
- **IBM Bob GA** — AI開発パートナー（フルSDLC）、80,000+社内利用、45%生産性向上、マルチモデルオーケストレーション
- **Meta Avocado** — 5月リリースウィンドウ閉塞、複数バリアントテスト中（9B/Thinking/Mango）
- **AWS Bedrock Advanced Prompt Optimization** — 5/15リリース、自動プロンプト最適化ツール
- **Spec-Driven Development** — Kiro/SpecKit/Tessl/Zenflow、vibe codingからの揺り戻し

### Raw Articles Saved
- `inbox/rss-scans/trending-topics-2026-05-16.md` — Full trending topics report

### Sources
- Web search: Grok Build CLI, Google I/O 2026 preview, Notion platform, Claude agent meter, IBM Bob GA, Meta Avocado, AWS Prompt Optimization, Spec-Driven Dev tools

---
## 2026-05-16 07:50 — Blog wiki ingest (no-op: all 17 articles already processed at 07:00)

- All 17 blog candidates already captured by the 07:00 UTC blog-wiki-ingest run
- 0 takes, 0 references, 17 skips
- Verified: entities/datasette-llm-limits.md, concepts/ai-bubble.md, entities/eric-jang.md, events/openai-may-2026-reorg.md, concepts/proof-of-useful-work.md, entities/omri-weinstein.md, entities/gary-marcus.md (updated), entities/greg-brockman.md (updated)


---
## 2026-05-16 11:00 — Active crawl (5 topics: SubQ, Baidu Ernie 5.1, IBM Think, DeployCo, ZAYA1-8B)

### Raw Articles Saved
- `raw/articles/whatllm.org--new-ai-models-may-2026-subq-subquadratic--2026-05-16.md`
- `raw/articles/the-decoder.com--baidu-ernie-5-1-94-percent-cost-reduction--2026-05-16.md`
- `raw/articles/ibm.com--think-2026-ai-operating-model-agent-orchestration--2026-05-16.md`
- `raw/articles/openai.com--launches-deployment-company-deployco--2026-05-16.md`
- `raw/articles/zyphra.com--zaya1-8b-moe-amd-reasoning--2026-05-16.md`

### Pages Created (8)
- **entities/subquadratic.md** — Subquadratic (SubQ): first commercial subquadratic LLM, 12M context, $29M seed
- **entities/baidu.md** — Baidu (Ernie 5.1): 94% pre-training cost reduction via Once-For-All elastic training
- **entities/ibm.md** — IBM (Think 2026): watsonx Orchestrate agentic control plane, IBM Bob, AI Operating Model
- **entities/openai-deployment-company.md** — DeployCo: $4B OpenAI enterprise deployment JV, 19 investors, Tomoro acquisition
- **concepts/subquadratic-attention.md** — Subquadratic attention: O(n²) alternatives, Mamba/RWKV/Hyena/SubQ comparison
- **concepts/elastic-training.md** — Once-For-All elastic training: single-run multi-model optimization
- **concepts/agent-orchestration.md** — Agent orchestration: governing thousands of agents at enterprise scale
- **concepts/zaya1-8b.md** — ZAYA1-8B: 760M active MoE, AMD-trained, competitive with DeepSeek-R1/Gemini-2.5-Pro

### Pages Updated (1)
- **entities/zyphra.md** — Updated with ZAYA1-8B source, bumped date

### Index Changes
- Updated header counts (1893→1901 total, 591→595 entities, 1323→1327 concepts)

### Sources
- WhatLLM.org: New AI Models May 2026 (SubQ, ZAYA1-8B, GPT-5.5 Instant, Grok 4.3, Gemini 3.1 Flash Lite)
- The Decoder: Baidu Ernie 5.1 94% cost reduction
- IBM Newsroom: Think 2026 AI Operating Model
- OpenAI Blog: DeployCo launch
- Zyphra PR Newswire + arXiv 2605.05365: ZAYA1-8B technical report

---


## 2026-05-16 07:40 — Newsletter wiki ingest (Codex mobile, Apple dispute, Cerebras IPO)

### Pages Updated
- **entities/codex.md** — Mobile Launch (May 2026) section: ChatGPT mobile app preview, 4M WAU, secure relay layer, enterprise support
- **entities/openai.md** — Apple Partnership Dispute section (legal action over Siri deal); TanStack section enhanced with TechCrunch details (84 packages, 6-min window, self-propagation)
- **entities/cerebras-systems.md** — IPO outcome ($280/share, $60B market cap, 2x+ expected); OpenAI 5.4/5.5 on Cerebras; TSMC wafer constraints through 2028
- **entities/anthropic.md** — Gates Foundation $200M/4yr partnership reference

- **concepts/openai-tanstack-supply-chain-2026.md** — Enhanced with TechCrunch attack details (84 malicious versions, 6-min window, 20-min detection, self-propagation)

### Raw Articles Saved
- `raw/articles/openai.com--index-work-with-codex-from-anywhere--2026-05-16.md`
- `raw/articles/9to5mac.com--openai-preparing-legal-action-against-apple--2026-05-16.md`
- `raw/articles/techcrunch.com--openai-says-hackers-stole-some-data-tanstack--2026-05-16.md`

### Index Changes
- Updated last-updated date in index header (2026-05-15 → 2026-05-16)

### Sources
- Newsletter: `raw/newsletters/2026-05-15-codex-goes-everywhere.md` (Superintel)
- Newsletter: `raw/newsletters/2026-05-16-ainews-cerebras-60b-ipo-slowly-then-all-at-once.md` (AINews/Latent Space)


---

## 2026-05-16 07:00 — Blog ingest (34 new articles, 7 new pages, 3 enriched)

### AI/LLM Articles Processed

**1. OpenAI May 2026 Product Reorganization (Wired)**
- **Raw article saved**: `raw/articles/wired.com--story-openai-reorg-greg-brockman-product--16e3b9d6.md`
- **New event page**: `events/openai-may-2026-reorg.md` — Complete page covering ChatGPT+Codex merger, "super app" strategy, leadership changes
- **Enriched**: `entities/greg-brockman.md` — Added May 2026 Product Reorganization section
- **Enriched**: `entities/gary-marcus.md` — Added May 2026 US AI Policy Framework section (Fortune essay)

**2. Eric Jang on AlphaGo (Dwarkesh Podcast)**
- **Raw article saved**: `raw/articles/dwarkesh.com--p-eric-jang--44c9439c.md`
- **New entity page**: `entities/eric-jang.md` — Former VP of AI at 1X Technologies, Google Brain researcher. Covers MCTS vs RL, automated AI research, robotics

**3. Together AI + Pearl Research Labs (PoUW)**
- **Raw article saved**: `raw/articles/together.ai--blog-together-ai-partners-with-pearl-research-labs--8b21a91f.md`
- **New concept page**: `concepts/proof-of-useful-work.md` — Blockchain consensus using AI inference instead of hash puzzles
- **New entity page**: `entities/omri-weinstein.md` — Pearl Research Labs co-founder & CEO

**4. AI Bubble Analysis (Where's Your Ed At)**
- **Raw article saved**: `raw/articles/wheresyoured.at--premium-what-if-were-in-an-ai-bubble-part-1--6e9bc8ba.md`
- **New concept page**: `concepts/ai-bubble.md` — The AI Bubble debate (Zitron vs Patel), circular revenue dependencies, May 2026 context

**5. datasette-llm-limits (Simon Willison)**
- **Raw article saved**: `raw/articles/simonwillison.net--2026-may-15-datasette-llm-limits--c4c541c4.md`
- **New entity page**: `entities/datasette-llm-limits.md` — Datasette plugin for LLM spending limits and cost tracking

### Entity Pages Created
- `entities/fidji-simo.md` — OpenAI CEO AGI Deployment, ex-AppLovin CEO
- `entities/thibault-sottiaux.md` — OpenAI Head of Core Product + Platform
- `entities/eric-jang.md` — 1X Technologies VP AI, Google Brain
- `entities/omri-weinstein.md` — Pearl Research Labs CEO
- `entities/datasette-llm-limits.md` — Simon Willison's Datasette plugin

### Concept Pages Created
- `concepts/proof-of-useful-work.md` — PoUW blockchain consensus
- `concepts/ai-bubble.md` — AI Bubble debate (2025–2026)

### Event Pages Created
- `events/openai-may-2026-reorg.md` — OpenAI product consolidation

### Index Changes
- Added 7 new entity entries (eric-jang, fidji-simo, thibault-sottiaux, omri-weinstein, datasette-llm-limits)
- Added 2 new concept entries (proof-of-useful-work, ai-bubble)
- Added 1 new event entry (openai-may-2026-reorg)
- Updated concept count: 1323→1325, event count: 2→3, entity count: 591→596, total pages: 1893→1900

### Other Articles Saved (not wiki-processed)
- `raw/articles/nesbitt.io--2026-05-15-language-registries-are-unstable-by-default-html--e4c19a2c.md` — Language registries instability
- `raw/articles/maurycyz.com--misc-search--6b5086f1.md` — Search engine quality critique
- `raw/articles/devblogs.microsoft.com--oldnewthing-20260515-00--cd3fbf93.md` — Windows CreateFileMapping debugging
- `raw/articles/daringfireball.net--thetalkshow-2026-05-15-ep-447--fbb37638.md` — The Talk Show podcast
- `raw/articles/dropoverapp.com----3f92450c.md` — Mac shelf utility app
- `raw/articles/aluminium-os.com----daa0c921.md` — Google PC OS
- `raw/articles/dfarq.homeip.net--processor-technology-corporation-and-the-sol-20--b9ebf890.md` — Retro computing
- `raw/articles/pluralistic.net--2026-05-15-not-ok-boomer--f0a121dc.md` — Cory Doctorow gerontocracy critique
- `raw/articles/johndcook.com--blog-2026-05-15-xorshift128-state--6f20c18e.md` — xorshift128 RNG
- `raw/articles/simonwillison.net--2026-may-15-qr-code-generator--16a8fee0.md` — QR code tool
- `raw/articles/simonwillison.net--2026-may-15-sighting-361818285--22492976.md` — Bird sighting

### Unsaved Articles
- `https://simonwillison.net/2026/May/15/inaturalist-clumper/#atom-everything` — iNaturalist clumper tool
- `https://openai.com/index/personal-finance-chatgpt` — ChatGPT personal finance
- `https://www.youtube.com/watch?v=eBKWKu2Rqxc` — YouTube video (CBS property)

## 2026-05-15 23:30 — X bookmarks ingest (3 bookmarks, 1 new page, 3 enriched)

### Bookmark 1: AI Edge "/goal - Ultimate Guide" (X Article)
- **Raw article saved**: `raw/articles/2026-05-14_apidog_goal-command-autonomous-agents.md` — Full Apidog mirror article covering /goal across Codex, Claude Code, and Hermes
- **Enriched**: `concepts/codex-goal.md` — Added Hermes Agent /goal reference, Claude Code cross-link, Apidog and explainx.ai source references
- **Status**: Existing goal pages (claude-code-goal.md 170 lines, codex-goal.md 151 lines) already thorough; cross-references enriched

### Bookmark 2: Matt Van Horn "Every Claude Code Hack I Know" (X Article, metadata-only)
- **Raw article saved**: `raw/articles/2026-03-22_mvanhorn_claude-code-hacks.md` — Metadata from X status page (auth-walled). Key themes: plan-first workflow, voice-driven dev, no-IDE philosophy, parallel sessions
- **Enriched**: `entities/matt-van-horn.md` — Added Claude Code Workflow Philosophy section, new source reference, claude-code tag, claude-code-goal related link

### Bookmark 3: Karri Saarinen "Code Intelligence for Linear Agent" (X Article → changelog)
- **Raw article saved**: `raw/articles/2026-05-14_linear_code-intelligence-linear-agent.md` — Full Linear changelog extraction
- **New concept page**: `concepts/linear-agent-code-intelligence.md` — Complete page with adoption metrics (1,055→5,200+ queries/month), architecture, setup, and strategic significance
- **Enriched**: `entities/linear.md` — Updated with Code Intelligence feature, source, tags
- **SCHEMA.md**: Added `code-intelligence` tag to AI Agents taxonomy

### Index Changes
- Added `concepts/linear-agent-code-intelligence` to concepts section (alphabetical, after lexical-search)
- Updated concept count: 1322→1323, total pages: 1892→1893

### Source URLs
- https://apidog.com/blog/goal-command-codex-claude-code-autonomous-agents/
- https://linear.app/changelog/2026-05-14-code-intelligence
- https://x.com/i/article/2035834194065281024 (auth-walled)

## [2026-05-15] fix | wiki-health auto-repair

### Phase 1 — Index corruption check
- Index corruption: 0 issues ✅ (pipe_corruption=0, triple_bracket=0, line_number=0)
- SCHEMA.md: healthy
- validate_index.py: pass ✅

### Phase 2 — Orphan page registration (20 of 936)
- **Added 20 orphan pages to index.md** (19 concepts + 1 comparison)
- Concepts added: aaron-swartz, a-philosophy-of-software-design-vs-clean-code, activitypub, adversarial-interoperability, agent-documentation, agent-first-codebase-design, agent-first-design, agentic-alternative-to-graphrag, agentic-browsing, agentic-coding, agentic-commerce, agentic-conflict-resolution, agentic-design-patterns, agentic-engineering-cognition-devin-multi-agents-orchestration, agentic-engineering-cognition-devin-workflow, agentic-engineering-patterns, agentic-manual-testing, agent-security-patterns, agent-skills-skillmd
- Comparison added: agent-sandboxing
- Updated section counts: Concepts (1303→1322), Comparisons (16→17)
- Updated Total pages: 1872→1892, Not in index: 896→876

### Phase 3 — Script path issue detected
- cron job expects wiki_health_json.py at `/opt/data/.hermes/scripts/wiki_health_json.py`
- Actual location: `/opt/data/ai-topics/scripts/wiki_health_json.py`
- Script ran successfully from canonical path despite cron config error

### Health overview
- Entities: 598 / Concepts: 1,350 / Comparisons: 18 / Total L2: 1,966
- Raw articles: 5,968 / Stale pages: 242 (oldest: 36 days)
- Remaining orphan pages: 916 (not auto-processed — batch limit)

---

## [2026-05-15] watchdog | No auto-fixes applied — all issues exceed 10-file threshold

### Health Summary
| Metric | Value |
|---|---|
| Total L2 pages | 1,952 |
| Index entries | 1,013 |
| Not in index | 939 (47.5%) |
| Missing `sources` frontmatter | 776 (39.7%) |
| Ghost entries (true) | 0 — all 25 detected resolve to subdirectory files |
| Index corruption | 0 — clean (`validate_index.py` ✅) |
| Stale pages (>30d) | 182 |
| Pipeline alerts | x_accounts stale (26h) |

### Issues Requiring Human Attention

1. **939 pages not in index** — ~875 concept pages + entity subdir pages + 2 events missing. Needs batch reconciliation (50-100 per batch).
2. **776 pages missing `sources` field** — Systemic gap from pipeline-created pages.
3. **182 stale pages (>30d)** — Low priority, but growing.
4. **x_accounts pipeline stale (26h)** — x-accounts-scan cron job may need restart.

### Previously Reported Issues (Verified False Positives)
- **21 ghost entries** → All resolve to existing subdirectory files. Zero true ghosts.
- **Index corruption = 0** — validated by `validate_index.py` ✅. Pipeline working.

---

## [2026-05-15] wiki | antirez.com/news/165 — DS4 follow-up article ingested

### Changes
- **[[entities/antirez-com]]**: Timeline entry for DS4 release (May 2026). Added "モデル非依存設計" subsection: model-agnostic philosophy, DGX Spark mention, "just load what you need" domain-variant approach. Expanded future plans with distributed inference emphasis.
- **[[concepts/ds4-dwarfstar-4]]**: Added Model-Agnostic Philosophy section clarifying DS4 is not tied to V4 Flash forever. Expanded future plans with "just load what you need" variant philosophy. Added A-vs-B spectrum metaphor (DS4 is "a lot more B than A"). Emphasized distributed inference as top priority.
- Source: [[raw/articles/antirez.com--news-165--a8668e18]]

---

## [2026-05-15] fix | Wiki graph analysis cross-link

### Changes
- Added [[entities/randy-olson]] to [[entities/ian-nuttall]] Related Concepts
- Added [[entities/ian-nuttall]] to [[entities/randy-olson]] Related Entities and Concepts
- Both share: agent-skills, MCP ecosystems
- Fixed all graph gap recommendations (0 remaining)

---




## 2026-05-15 20:00 UTC — active-crawl | AKOOL, AntAngelMed, DeerFlow, IBM Granite 4.1

**Action**: Active crawl — researched trending AI topics, extracted original sources, created wiki pages for 4 new entities/concepts not previously covered.

### Pages Created
- `entities/akool.md` — AKOOL: AI video generation suite. 10-20× faster real-time video inference engine (sub-30ms/frame), full-stack optimization. Source: PRNewswire May 11, 2026.
- `concepts/antangelmed.md` — AntAngelMed: 103B open-source medical MoE model (1/32 activation, 6.1B active). GRPO-trained on Ling-flash-2.0 base. 7× efficiency over dense. Source: MarkTechPost May 12, 2026.
- `concepts/deerflow.md` — DeerFlow: ByteDance open-source SuperAgent harness (67.5K stars, MIT license). Sub-agents, memory, sandboxes, skills. #1 GitHub Trending Feb 2026. Source: GitHub.
- `concepts/granite-4-1.md` — IBM Granite 4.1: Apache 2.0 dense LLM family (3B/8B/30B). 15T tokens, 512K context. 8B matches previous 32B MoE. GRPO+DAPO RL. Source: IBM Research/HF Blog April 29, 2026.

### Raw Articles Saved
- `raw/articles/2026-05-11_akool-video-inference-engine.md`
- `raw/articles/2026-05-12_antangelmed-103b-medical-moe.md`
- `raw/articles/2026-05-15_deerflow-bytedance-superagent.md`
- `raw/articles/2026-04-29_ibm-granite-4-1.md`

### Index Updated
- Added `entities/akool` under Entities section (591)
- Added `concepts/antangelmed`, `concepts/deerflow`, `concepts/granite-4-1` under Concepts section (1303)
- Total pages: 1872 | Indexed entries: 957

---

## 2026-05-15 07:50 UTC — blog-wiki-ingest | DS4, M5 Mythos Exploit, Managed Agents

**Action**: Processed blog triage from blog-ingest checkpoint (20 candidates). 3 takes, 6 references, 11 skips.

### Pages Created
- `concepts/ds4-dwarfstar-4.md` — DS4 (DwarfStar 4): antirezのローカルAI推論プロジェクト。DeepSeek V4 Flash in 2/8-bit asymmetric quantization. Source: antirez.com/news/165.

### Pages Updated
- `entities/antirez-com.md` — Added DS4 section with timeline entry, technical details (2/8-bit asymmetric quantization, vector steering), future plans (distributed inference, coding agent, model variants). Source: antirez.com/news/165.
- `concepts/ai-vulnerability-discovery.md` — Full rewrite from stub: M5 MIE kernel exploit case study, Mozilla Firefox hardening, antirez's intelligence-vs-compute framework, Mythos Preview generalization capabilities.
- `concepts/claude-mythos-preview.md` — Added Apple M5 MIE Kernel Exploit section (May 2026): Calif team breached M5 MIE in 1 week with Mythos Preview. Data-only kernel LPE, 2-vuln chain, root shell on bare-metal M5.
- `entities/martin-alderson.md` — Added "Managed Agents Analysis" section: Lambda analogy, Anthropic pricing change (5-20x increase), self-hosting strategy, OpenCode as multi-provider harness, frontier lab exclusive-platform risk.
- `concepts/managed-agents.md` — Added generic vendor lock-in analysis section: harness swapability, Anthropic pricing impact, self-hosting pattern, multi-provider platform landscape (Cloudflare, Vercel, AWS AgentCore, Azure, GCP).

### Index Updated
- Added `concepts/ds4-dwarfstar-4` under Concepts section (1300 pages)
- Total pages: 1868 | Indexed entries: 953

### Sources
- blog-18: `raw/articles/antirez.com--news-165--a8668e18.md`
- blog-14: `raw/articles/blog.calif.io--p-first-public-kernel-memory-corruption--8fd5d832.md`
- blog-4: `raw/articles/martinalderson.com--posts-managed-agents-are-the-new-lambda--f9db9fb9.md`

---

## 2026-05-15 07:40 UTC — newsletter-wiki-ingest | The AI Cursor Arrives! + Isomorphic Labs $2.1B

**Action**: Processed newsletter triage from getsuperintel.com "The AI Cursor Arrives!" (May 13, 2026). Created Google DeepMind entity page, enriched Demis Hassabis and Ilya Sutskever pages.

### Pages Created
- `entities/deepmind.md` — Google DeepMind entity page covering history (AlphaGo, AlphaFold, Gemini) and the May 2026 AI Pointer / Magic Pointer announcement (context-aware cursor powered by Gemini, 4 interaction principles, product integrations with Chrome, Googlebook, AI Studio). Source: deepmind.google/blog/ai-pointer/ + getsuperintel newsletter.

### Pages Updated
- `entities/demis-hassabis.md` — Added Isomorphic Labs section: $2.1B Series B (May 2026) led by Thrive Capital with Alphabet/GV/MGX/Temasek/CapitalG/UK Sovereign AI Fund participation. Added AI Pointer reference in Recent Work section. Updated sources.
- `entities/ilya-sutskever.md` — Added SSI valuation pressure note (May 2026) to Funding table. Updated sources.

### Sources
- `raw/newsletters/2026-05-13-the-ai-cursor-arrives.md` — getsuperintel.com newsletter by Kim Isenberg
- https://deepmind.google/blog/ai-pointer/ — DeepMind official blog: AI Pointer
- https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round — Isomorphic Labs Series B announcement

---

## 2026-05-15 03:10 UTC — runtime-opinionated-sdk concept page created + cross-references

**Action**: Created `concepts/runtime-opinionated-sdk.md` — a new concept page capturing kzinmr's analysis of Claude/OpenAI Agents SDKs as **mini runtimes** that embed a specific execution model. Added `agent-sdk` tag to SCHEMA.md taxonomy.

**New pages**:
- `concepts/runtime-opinionated-sdk.md` — Defines "runtime-opinionated": SDKs that give freedom to write code but embed strong assumptions about the execution model. Covers 5 implicit runtime opinions (reactive tool loop, runtime-owned tool orchestration, composable actors, state continuity, native observability), 5 implicit worldview points, LangGraph vs Agents SDK comparison (developer authors orchestration vs developer configures runtime behavior), PI vs Agents SDK comparison (both runtime-first, PI goes further in scheduler/lifecycle semantics).
- `raw/articles/2026-05-15_kzinmr_runtime-opinionated-sdk.md` — Source analysis

**Cross-references added to**:
- `comparisons/open-harness-vs-agent-framework.md` §9 — Runtime-opinionated SDKs as mini runtimes
- `entities/pi.md` — PI vs Agents SDK comparison (both runtime-first, different depth)
- `concepts/agent-runtime.md` — Relationship to Other Concepts section

**SCHEMA.md**: Added `agent-sdk` tag to AI Agents category

**Key insight**: Claude/OpenAI Agents SDKs are not generic orchestration toolkits — they're **mini runtimes** that provide an *agent execution abstraction* (not an LLM call abstraction). The critical distinction from workflow frameworks: in a workflow framework, the developer writes orchestration; in a runtime-opinionated SDK, the developer configures runtime behavior.

## 2026-05-15 02:50 UTC — Control flow ownership: why runtime-centric now, structural inversion, what dies and survives

**Action**: Enriched `concepts/agent-runtime.md` with the deepest layer of the runtime-centric analysis — why the shift happened now, what structurally changed, and what the future of agent infrastructure looks like. Also updated `comparisons/open-harness-vs-agent-framework.md` §9 and `concepts/agent-harness.md`.

**New pages**:
- `raw/articles/2026-05-15_kzinmr_why-runtime-centric-now-control-flow-ownership.md` — Full analysis: control flow ownership as the real shift, structural inversion (graph primary vs loop primary), what dies (explicit orchestration DSL) and what survives (execution semantics), browser/computer-use as the forcing function, the half-right/half-wrong framework irrelevance thesis

**Enriched sections in `concepts/agent-runtime.md`**:
- §"Why Now: Control Flow Ownership and the Real Shift" — The loop was always possible; the real difference is who can safely hold control flow authority. 3-era table (model capability → control flow authority → architecture). The question shift: "how do we constrain flow?" → "how do we execute safely?" Why browser/computer-use forced the shift (open-ended environments break developer-authored graphs).
- §"The Structural Inversion: Graph Primary vs Loop Primary" — Workflow-centric: graph is primary, LLM is a component, developer decides what's next. Runtime-centric: loop is primary, workflow emerges from execution, model decides what's next, runtime mediates. Railroad tracks vs autonomous navigation analogy. The "PydanticAI Can Do ReAct" question — architecture is about what is primary, not what is possible.
- §"What Dies and What Survives: The Future of Agent Infrastructure" — Declining: explicit orchestration DSL (graph.add_edge, hand-coded state transitions). Growing: execution semantics (observability, state, permissions, scheduling, isolation, memory, runtime policies). The half-right/half-wrong thesis: workflow abstraction shrinks, runtime abstraction becomes MORE important.
- Updated Historical Arc with 3-era model (weak model → hybrid → runtime-mediated)

**Key insight**: The ReAct loop existed in the LangChain era — the loop is not the structural difference. The real shift is that models became reliable enough to *maintain execution semantics* (tool continuation, long-horizon tasks, retry adaptation), which means the runtime can shift from "constraining an unreliable model" to "mediating a capable model's execution." The bottleneck shifts from orchestration logic to execution runtime design.

## 2026-05-15 02:30 UTC — Agent stack architecture: 5-layer model, Closed/Open Harness, Harness Type comparison, PI as Runtime Substrate

**Action**: Enriched 5 wiki pages with kzinmr's comprehensive agent stack architecture analysis — the 5-layer agent stack model, Closed vs Open Harness comparison, Harness Type comparison (coding/browser/computer-use/general + environment entropy gradient), Harness vs SDK/Framework "user vs builder" distinction, runtime-centric vs workflow-centric taxonomy, PI as Runtime Substrate, and the historical arc (Framework→Workflow→Runtime-centric).

**New pages**:
- `raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis.md` — Full analysis: 5-layer stack, Closed/Open Harness, Harness Types, Harness vs SDK/Framework, runtime-centric vs workflow-centric, PI as Runtime Substrate, historical arc

**Enriched pages**:
- `concepts/agent-runtime.md` — Added §"The 5-Layer Agent Stack" with architecture diagram and §"The Historical Arc" (2023: Framework-centric → 2024: Workflow-centric → 2025-: Runtime-centric). Core message: "Model quality alone no longer determines agent capability. Runtime design increasingly dominates."
- `concepts/agent-harness.md` — Added 3 new sections: §"Closed Harness vs Open Harness: Runtime Ownership" (co-training/co-design vs runtime portability), §"Harness Type Comparison: Environment Abstraction" (coding/browser/computer-use/general + environment entropy gradient), §"Harness vs Runtime: The Critical Distinction". Key insight: Entropy gradient explains why coding harnesses reach production first.
- `comparisons/open-harness-vs-agent-framework.md` — Added §9 "Runtime-Centric vs Workflow-Centric: The Fundamental Axis" — introduces the runtime-centric family (ClaudeCode/Codex/PI/OpenClaw/Hermes) vs workflow-centric (LangGraph/PydanticAI). Includes PI as Runtime Substrate analysis with comparison table vs LangGraph/PydanticAI. Mental model: "Agent OS" vs "orchestration library".
- `entities/pi.md` — Added §"PI as Runtime Substrate: Beyond a Coding Harness" — maps PI's architecture to 7 runtime responsibilities (execution loop, state management, task runtime, tool orchestration, environment mediation, event handling, interruption/recovery). Positions PI in the runtime-centric family. Key implication: evaluate PI as runtime substrate, not as workflow framework.
- `wiki/index.md` — Updated entries for agent-runtime, agent-harness, pi, and open-harness-vs-agent-framework

**Key insight across all pages**: The agent stack's center of gravity has shifted Framework→Workflow→Runtime. ClaudeCode, Codex, PI, OpenClaw, Hermes are all in the same architectural family (runtime-centric systems). The key distinction is not "harness vs framework" but "runtime-centric vs workflow-centric" — the former manages *how execution proceeds*, the latter describes *what execution topology should be*.

## 2026-05-15 02:11 UTC — agent-runtime.md enriched with "Execution Semantics" control system layer

**Action**: Enriched `concepts/agent-runtime.md` with a major new section — "Execution Semantics: The Control System Layer" — based on kzinmr's analysis distinguishing agent runtime from language runtimes, workflow frameworks, and the model itself. Also added a "Harness vs Runtime: The Critical Distinction" section to `concepts/agent-harness.md`.

**New pages**:
- `raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics.md` — kzinmr's analysis: agent runtime as execution control system, 8 responsibilities, Model↔Runtime separation, workflow framework vs runtime distinction

**New sections added to `concepts/agent-runtime.md`**:
- §"Execution Semantics: The Control System Layer" — Runtime as execution semantics vs infrastructure substrate; 8 responsibilities (lifecycle, tool mediation, state continuity, environment mediation, scheduling, event system, safety/policy, observability); Model↔Runtime separation table; Workflow Framework vs Runtime System comparison; the architecture diagram; completion-centric vs agent-centric transition
- Updated Summary to acknowledge dual nature of runtime (infrastructure + execution semantics)
- Updated "Relationship to Other Concepts" with harness/runtime distinction and workflow framework cross-reference

**New section added to `concepts/agent-harness.md`**:
- §"Harness vs Runtime: The Critical Distinction" — Harness owns behavior/capabilities; Runtime owns continuity/safety. Workflow framework vs runtime clarification.

**Updated pages**:
- `concepts/agent-runtime.md` — Frontmatter updated: added source, `updated` date; ~100 new lines
- `concepts/agent-harness.md` — Frontmatter updated: added source; §Harness vs Runtime section added
- `wiki/index.md` — Updated agent-runtime entry description to reflect dual perspective

**Raw article**: `raw/articles/2026-05-15_kzinmr_agent-runtime-execution-semantics.md`

**Key insight**: The existing `agent-runtime.md` focused on Han Lee's infrastructure-centric framing (containers, sandboxing, isolation primitives). kzinmr's analysis adds the complementary execution semantics layer — the runtime as a *control system* that manages lifecycle, mediates tools, maintains state, enforces safety, and makes agents persistent execution entities rather than stateless completions. This dual perspective (infrastructure + control system) is now the page's organizing framework.

## 2026-05-15 01:06 UTC — Agent Runtime concept page + Han Lee entity page created from Harness article

**Action**: Created `concepts/agent-runtime.md` and `entities/han-lee.md` from Han Lee's "Hidden Technical Debt of AI Systems: Agent Runtime" article. Added new tags `agent-runtime` and `technical-debt` to SCHEMA.md.

**New pages**:
- `concepts/agent-runtime.md` — Comprehensive concept page covering: agent runtime anatomy (6 components), isolation primitive stack (containers/Firecracker/gVisor/Kata/V8 isolates), sandbox-as-a-service landscape (Modal/E2B/Daytona/etc.), hyperscaler offerings (AWS/Azure/GCP), experimentation-vs-production runtime divergence, runtime shift (new distributional shift), and runtime debt. Cross-linked to agent-harness, context-engineering, reduce-offload-isolate, harness-commoditization.
- `entities/han-lee.md` — Han Lee (Hanchung Lee), Senior Director of Data + AI at Moody's Analytics. Blog "Han, Not Solo." Technical reviewer for Chip Huyen's "AI Engineering." Authored key articles on agent runtime, RL environments taxonomy, and the AI Great Leap Forward.

**Raw article**: `raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime.md`

**Updated pages**:
- `concepts/agent-harness.md` — Added cross-reference to agent-runtime in See Also
- `wiki/index.md` — Added both new page entries
- `wiki/SCHEMA.md` — Added `agent-runtime` (AI Agents) and `technical-debt` (Engineering) tags

## 2026-05-15 00:11 UTC — GEPA concept page rewritten with Hermes Agent integration

**Action**: Rewrote `concepts/gepa.md` to be a comprehensive concept page integrating GEPA's academic foundation (2507.19457, ICLR 2026 Oral) with its Hermes Agent self-evolution pipeline role from the raw masterclass article.

**Changes**:
- Frontmatter updated: tags [gepa, evolutionary-algorithms, prompting, optimization, self-improving, agent-skills, hermes-agent, nous-research, evaluation], sources include raw article + arXiv paper
- Added Hermes Agent pipeline section: companion repo `NousResearch/hermes-agent-self-evolution`, offline optimization, PR-based delivery
- Key innovations section: execution-trace-based evaluation vs self-report, Pareto optimization, constraint gates
- Cost/GPU table, ICLR 2026 Oral details, ecosystem adoption section
- Wikilinks: [[hermes-agent]], [[nous-research]], [[agent-skills]] plus DSPy/RLM cross-links
- Final: 82 lines, under 120-line limit
- Updated `index.md` with concepts/gepa entry

## 2026-05-15 00:15 UTC — Created Hermes Agent vs OpenClaw comparison page

**Action**: Created `comparisons/hermes-vs-openclaw.md` — a concise comparison page at 62 lines framed by the Kilo blog quote.

**Changes**:
- Frontmatter: title "Hermes Agent vs OpenClaw", type comparison, 8 sources including Kilo blog, GitHub repos, official docs
- Kilo blog framing quote: "Hermes packages a gateway around a learning agent. OpenClaw packages an agent around a messaging gateway."
- 9-dimension comparison table: architecture philosophy, memory system, skill/learning system, identity layer, execution backends, model support, messaging platforms, scheduling, GitHub stars/community
- Architecture diagram: Hermes (agent-first) vs OpenClaw (gateway-first) data flow
- Verdict/synthesis: when to choose each, when to use both (orchestrator + executor via ACP)
- Wikilinks: [[hermes-agent]], [[nous-research]], [[gepa]], [[hermes-vs-openclaw-architecture]]
- Updated `index.md`: added comparisons entry, updated hermes-agent and openclaw entity cross-references

## 2026-05-15 00:35 UTC — Agent Skills Overview 親ページ作成＋クラスター相互参照整備

**Action**: Created `concepts/agent-skills-overview.md` as the parent hub page for all Skills-related concepts. Added back-links from 6 key pages. Redirected stub duplicate `agent-skills-skillmd.md` → `agent-skills.md`. Updated `index.md` and `log.md`.

**New pages**:
- `concepts/agent-skills-overview.md` — Agent Skills 概念クラスターマップ。全Skills関連14ページを4層（Format & Standard / Design Philosophy / Implementation & Architecture / Research & Scaling）に分類。各層の相互関係・重複・読み筋（初心者/実践者/アーキテクト向け）を含む。

**Updated pages (back-links added)**:
- `concepts/agent-skills.md` — agent-skills-overviewへのSee Alsoリンク追加
- `concepts/claude-code-skills.md` — agent-skills-overviewへのSee Alsoリンク追加
- `concepts/skill-architecture-patterns.md` — agent-skills-overviewへのRelatedリンク追加
- `concepts/agentic-ai-skills.md` — agent-skills-overviewへのRelated Conceptsリンク追加
- `concepts/skill-graph.md` — agent-skills-overviewへの関連概念リンク追加
- `concepts/skill-retrieval-augmentation.md` — agent-skills-overviewへのRelated Worksリンク追加
- `concepts/agent-skills-skillmd.md` — stub → redirected（agent-skills.mdへのリダイレクトに変更）

## 2026-05-15 00:20 UTC — Claude Code Skills concept page created from Thariq X Article

**Action**: Saved raw article `raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md` (via GetXAPI), created concept page `concepts/claude-code-skills.md`, updated Thariq Shihipar entity page with source reference and cross-link. Updated `index.md` and `log.md`.

**New pages**:
- `raw/articles/2026-03-17_trq212_lessons-building-claude-code-skills.md` — Thariq Shihipar's \"Lessons from Building Claude Code: How We Use Skills\" X Article (Mar 17, 2026, 16K+ likes, 6.8M+ views). Full body via GetXAPI.
- `concepts/claude-code-skills.md` — 機序（フォルダ構造・Progressive Disclosure・動的Hooks・メモリ永続化）と9つの役割パターン（Library/API Reference, Product Verification, Data Fetching, Business Process, Code Scaffolding, Code Quality, CI/CD, Runbooks, Infrastructure Operations）。設計原則（Gotchasセクション、ファイルシステムProgressive Disclosure、オンデマンドHooks、配布パターン、マーケットプレイス運用、Skills合成・計測）を含む総合ページ。

**Updated pages**:
- `entities/thariq-shihipar.md` — Skills記事のraw article source追加、新conceptページへのクロスリンク、月表記修正（Feb→Mar）、エンゲージメント数値更新（15K→16K, 6M→6.8M）

## 2026-05-15 00:06 UTC — Akshay Pachaar entity page updated

**Action**: Updated `entities/akshay-pachaar.md` with current information from his Hermes Agent Masterclass X Article (May 13, 2026) and web research.
**Changes**:
- Follower count updated: 187K → 270,693 (X)
- Role updated: Sr. AI Research Engineer at LightningAI → Co-Founder DailyDoseOfDS, ex-AI Engineer at LightningAI
- Added Notable Content section: Hermes Agent Masterclass (1.3M impressions, 9,572 bookmarks), DailyDoseOfDS courses/guidebooks, YouTube channel
- Added wikilinks: [[hermes-agent]], [[concepts/nous-research]], [[concepts/gepa]], [[concepts/harness-engineering]], [[entities/addy-osmani]]
- Tags updated: [person, educator, blogger, x-account, ai-agents, hermes-agent, content-creator]
- Sources added: raw article + LinkedIn + DailyDoseOfDS + YouTube + X profile
- Index updated: `wiki/index.md` — akshay-pachaar entry description updated

## 2026-05-15 00:06 UTC — Create [[entities/nous-research]] entity page

**Action**: Created entity page for Nous Research at `entities/nous-research.md`. Research via web (nousresearch.com, Crunchbase, GitHub) and raw article `raw/articles/2026-05-13_akshaypachaar_hermes-agent-masterclass.md`. Moved stale stub from `concepts/nous-research.md` to `_archive/`. Updated wikilink in `entities/teknium.md` from `[[concepts/nous-research]]` to `[[entities/nous-research]]`.

**Details**: 72-line entity page covering: founding (2023, NYC), founders (Quesnelle, Malhotra, Teknium, Mitra), $65M funding, key projects ([[hermes-agent]], [[gepa]] ICLR 2026 Oral, Skills Hub 687 skills), architecture philosophy. 7 outbound wikilinks.

**Updated**: `wiki/index.md` (added entry), `wiki/entities/teknium.md` (fixed wikilink), `wiki/_archive/nous-research.md` (archived stale stub).

## 2026-05-14 23:57 UTC — 0xSero「Open Source must win.」Wiki取り込み

**Action**: ユーザーリクエスト（Discord）により @0xSero の X Article「Open Source must win.」(2026-03-20) をwikiに取り込み。

**Raw article saved**: `raw/articles/2026-03-20_0xsero_open-source-must-win.md` — 全文（type: x_article）
**Entity enriched**: `entities/sero.md` — 「Mission Statement: Open Source Must Win (March 2026)」セクション追加（約30行）。10年ミッション、REAP Expert Swap、非中央集権的学習、AI教育の3本柱を詳述。
**Index updated**: `wiki/index.md` — seroエントリの説明を拡充（REAP Expert Swap、マニフェスト言及追加）

このマニフェストは Sero の "Freedom Tech" 哲学を10年ロードマップとして結晶化したもの。

## 2026-05-14 23:30 UTC — X Bookmarks Ingest

**Pipeline**: x-bookmarks-ingest (cron)
**Bookmarks processed**: 5 (all X Articles, no external URLs)
**Pages created**: 3
**Raw articles saved**: 2

### Pages Created
- `concepts/continual-harness.md` — Continual Harness framework: online, reset-free self-improvement for agent harnesses. From GPP (first AI to complete Pokemon). Removes human from harness refinement loop. By Seth Karten et al. (arXiv:2605.09998).
- `entities/seth-karten.md` — Seth Karten, CS PhD @ Princeton, creator of PokeChamp/PokeAgent, lead author of Continual Harness.
- `entities/petra-donka.md` — Petra Donka, Head of DevEx @ Warp. "Agents Need Feedback Loops, Not Perfect Prompts."

### Raw Articles Saved
- `raw/articles/2026-05-14_petradonka_agents-need-feedback-loops.md` — Petra Donka's X Article on agent feedback loops vs prompt engineering
- `raw/articles/2026-05-13_sethkarten_continual-harness.md` — Seth Karten's X Article companion to Continual Harness paper

### Skipped / Metadata-Only
- Akshay Pachaar "Hermes Agent Masterclass" (X Article, no body retrieved) — saved metadata only
- LakshyAAAgrawal GEPA quote tweet — informational, no new concept
- 0xSero "Open Source must win" (March 2026) — old, minimal content
## [2026-05-17] ingest | OpenClaw Memory System Deep Dive → wiki enrichment + comparison

### Changes
- `wiki/raw/articles/2026-01-25_snowan-gitbook_openclaw-memory-system-deep-dive.md` — Raw article saved (full deep dive on OpenClaw memory system, commit f99e3dd)
- `wiki/entities/openclaw.md` — **Memory System section fully rewritten**: 3-tier memory architecture (Ephemeral/Durable/Session), chunking algorithm (sliding window + overlap), hybrid BM25+vector search (SQLite FTS5 + sqlite-vec), embedding provider auto-selection (Local→OpenAI→Gemini), cache-first SHA-256 dedup, Pre-Compaction Flush mechanism, performance benchmarks. Added memory-systems tag, snowan source, cross-link to comparison page.
- `wiki/concepts/agent-memory-systems-comparison.md` — **NEW**: Comprehensive 3-harness memory system comparison (OpenClaw vs Claude Code vs Codex CLI). 6 comparison tables covering memory hierarchy, search/recall methods, embedding strategy, memory generation, context retention, design philosophy. Selection guide and common limitations documented.
- `wiki/concepts/context-compaction.md` — **Enriched from stub**: Full concept page with basic mechanism, Pre-Compaction Flush detailed description (trigger conditions, behavior, design intent), harness-by-harness comparison table.
- `wiki/index.md` — Added agent-memory-systems-comparison and context-compaction entries
- Cross-references: OpenClaw entity → agent-memory-systems-comparison, context-compaction → agent-memory-systems-comparison

### Key findings from article
- **File-first convergence**: All three harnesses (OpenClaw/Claude Code/Codex) use Markdown files as memory source of truth
- **OpenClaw uniquely uses vector search** (sqlite-vec) — Claude Code and Codex only use file reading/grep
- **Pre-Compaction Flush** is OpenClaw's most innovative feature: silent agentic turn before context window truncation
- **Hybrid search** (70% vector + 30% BM25) provides balanced precision/recall not found in other harnesses
- **Embedding provider auto-selection** with graceful degradation (Local→OpenAI→Gemini) allows offline operation

### Cross-references
- [[entities/openclaw]] → [[concepts/agent-memory-systems-comparison]]
- [[concepts/context-compaction]] → [[concepts/agent-memory-systems-comparison]]
- [[concepts/ai-memory-systems]] → linked concepts

### Follow-up: Hermes Agent added to comparison (same session)
- `wiki/concepts/agent-memory-systems-comparison.md` — **Expanded from 3 to 4 harnesses**: Added Hermes Agent columns to all comparison tables (memory hierarchy, search/recall, embedding, generation, compaction, design philosophy). Added Hermes selection guide, Bustamante's "Bounded Snapshot" classification, SOUL.md identity layer, 3-Tier memory details, Curator/GEPA integration, prefix cache optimization analysis.
- `wiki/index.md` — Updated comparison entry description to reflect 4 harnesses

### Move to comparisons/ (same session)
- `wiki/concepts/agent-memory-systems-comparison.md` → `wiki/comparisons/agent-memory-systems-comparison.md` — Moved from concepts/ to comparisons/ (type: concept → comparison). Updated all wikilinks in openclaw.md, context-compaction.md, index.md.
## [2026-05-14] health | Wiki health auto-fix — 20 orphan concepts indexed

### Changes
- `wiki/index.md` — Added 20 d-range concept pages to Concepts section:
 dark-factory-software-factory, data-engineering, data-engineering-for-ml,
 data-validation-python-type-hints-rust-web-frameworks-fastapi, dataset-engineering,

## [2026-05-18] ingest | LinkedIn post: Doug Turnbull's RAG→Agentic Search paradigm shift manifesto

### Changes
- `wiki/raw/articles/2026-04-21_softwaredoug_dont-waste-time-on-rag-paradigm.md` — New raw article: Doug Turnbull LinkedIn post "Don't waste too much time on the original RAG paradigm" (Apr 21, 2026). Condensed manifesto on RAG→agentic search paradigm shift + notable comments from Gayhart, Boytsov, Pickens.
- `wiki/concepts/agentic-search.md` — "Entry Point: The Paradigm Shift Manifesto" section added after Definition. Concise distillation of Turnbull's 4-point argument (retrieval-centric → harness-centric progression), practical advice, and comment tensions. Sources updated.

### Changes
- `wiki/raw/articles/2026-02-17_anthropic_dynamic-filtering-web-search.md` — New raw article from official Anthropic blog (Feb 17, 2026). BrowseComp + DeepsearchQA benchmarks, Quora/Poe validation, GA tools context.
- `wiki/concepts/agentic-search.md` — Dynamic Filtering section expanded with:
  - Full BrowseComp + DeepsearchQA per-model breakdown (Sonnet 4.6: 33.3%→46.6%, Opus 4.6: 45.3%→61.6%)
  - Quora/Poe production validation case study
  - "Filter-Before-Reasoning" architectural pattern analysis across 5 GA tools
  - Agentic Search Implications: convergence of IR Research, Harness Engineering, Externalized Processing
  - Open Questions: cost asymmetry, generality, eval contamination risk, RLM relationship
  - Sources updated: official Anthropic URL added alongside GEND partner summary

## [2026-05-18] ingest | Armin Ronacher: "A Language For Agents" — agent-oriented programming language design

### Changes
- `wiki/raw/articles/2026-05-18_armin-ronacher_a-language-for-agents.md` — New raw article: Armin Ronacher's essay on designing programming languages for AI agents (lucumr.pocoo.org, Feb 9, 2026). Covers: why new languages will succeed, 8 design principles (no-LSP context, braced syntax, explicit effects, results vs exceptions, line-friendly syntax, grep-ability, local reasoning, dependency-aware builds), what agents hate (macros, barrel files, aliasing, flaky tests).
- `wiki/entities/armin-ronacher.md` — Entity page created/updated: Austrian software engineer, creator of Flask/Jinja2/Werkzeug, Principal Architect at Sentry. Detailed section on his AI & agentic programming contributions, including the "A Language For Agents" essay.
- `wiki/concepts/agent-ergonomics.md` — Major enrichment: added "Armin Ronacher's Language Design Principles (2026)" section covering the 8 design principles, "What Agents Hate" antipatterns, and his meta-argument about measuring language success via agent performance. Frontmatter updated (new source, tags: +programming-language +ai-coding). Related concepts expanded.
- `wiki/SCHEMA.md` — Tag taxonomy: added `programming-language` to Engineering category.
- `wiki/index.md` — Updated entity entry for armin-ronacher; added description to agent-ergonomics concept entry.
- `wiki/concepts/claude-agent-sdk-research-stateless-stateful-web-search.md` — Deleted orphaned empty stub (not in index.md, no incoming links)

## [2026-05-18] ingest | Vercel Labs Zero — agent-oriented programming language

### Changes
- `wiki/raw/articles/2026-05-18_vercel-labs_zero-language-for-agents.md` — New raw article: Vercel Labs' Zero programming language (github.com/vercel-labs/zero, zerolang.ai). Launched May 15, 2026. Systems language with explicit effects, capability-based I/O, JSON-native diagnostics, repair metadata. 2,045★.
- `wiki/entities/zero-language.md` — New entity page: Zero — Vercel's agent-oriented systems language. Covers design philosophy, agent-first tooling, language features (World capability, raises, shape/enum/choice, generics, static interfaces), mapping to Ronacher's 8 principles.
- `wiki/concepts/agent-ergonomics.md` — Added "Concrete Implementation: Zero by Vercel Labs" section with principle-by-principle mapping table. Frontmatter updated with Zero source.
- `wiki/index.md` — Added zero-language entity entry.

## 2026-05-19 — Ingest | Autoresearching BM25 on MSMarco (Doug Turnbull)

- `wiki/raw/articles/2026-05-17_softwaredoug-com_autoresearching-better-msmarco-bm25.md` — New raw article: Doug Turnbull's lab notes on using a coding agent to iteratively improve BM25 on MSMarco passage retrieval. Dual-gate evaluation (training sandbox + validation gate), 8 rounds on minimarco, stopword removal/phrase boost/constant term boost, overfitting through validation data leakage.
- `wiki/concepts/autoresearch-bm25-msmarco.md` — New concept page: concrete case study of autoresearch applied to search ranking. Covers method (dual-gate agentic optimization), results (plateau on full MSMarco), overfitting trap (idiosyncratic stopwords), and relationship to Karpathy's autoresearch and Shopify's pi-autoresearch.
- `wiki/entities/softwaredoug.md` — Updated: added "Autoresearching BM25 on MSMarco" to Notable Blog Posts, added new raw article source, added [[autoresearch-bm25-msmarco]] to See Also, bumped updated date.
- `wiki/concepts/bm25.md` — Updated: added [[autoresearch-bm25-msmarco]] to Related Concepts, bumped updated date, added new raw article source.
- `wiki/index.md` — Added [[concepts/autoresearch-bm25-msmarco]] entry.

## 2026-05-18 11:30 — X Bookmarks Ingest

- `wiki/raw/articles/2026-05-17_DeRonin_agentic-project-setup-security.md` — Saved raw article: @DeRonin_ tweet about direnv + secrets manager setup for agentic projects (truncated thread)
- `wiki/raw/articles/2026-05-17_addy-osmani_dont-outsource-learning.md` — Saved raw article: Addy Osmani "Don't Outsource the Learning" (May 2026). Follow-up to cognitive surrender thesis with new research: Anthropic 2026 randomized trial (50% vs 67% comprehension), MIT EEG study (83% couldn't quote their own output), CHI 2026 anchoring effect. Advocates Learning Mode features and treating "ship" vs "learn" as separate metrics.
- `wiki/raw/articles/2026-05-16_Jouhatsu-ai_anthropic-claude-agent-training.md` — Saved raw article: @Jouhatsu_ai tweet reporting Anthropic's 2-hour comprehensive training on building Claude agents, led by the Claude Code engineer. Links to Anthropic Skilljar courses (Claude Code in Action, Agent Skills, Subagents) and certification programs.
- `wiki/entities/addy-osmani.md` — Enriched: added "Don't Outsource the Learning" (May 2026) section with research findings. Updated sources list. Bumped updated date.
- `wiki/concepts/cognitive-debt.md` — Enriched: added "2026 Research on AI-Assisted Learning vs. Comprehension" section covering Anthropic randomized trial, MIT EEG study, CHI 2026 anchoring effect, and Learning Mode mitigation. Updated sources list, bumped updated date. Added related page link to Addy Osmani entity.
- `wiki/concepts/agent-statefulness.md` — Create: Concept page on agent statefulness evolution (Gen 1: Raw Context → Gen 2: Memory Systems → Gen 3: Filesystem as Context). Driven by context economics. Covers Anthropic, Manus, Turso/AgentFS, Vercel, BabyAGI 3, StatePlane, InfiAgent. Source: Yohei Nakajima's X Article "The State of Statefulness in AI Agents" (2026-05-19) + yage.ai survey (2026-05-07).
- `wiki/entities/yohei-nakajima.md` — Create: Entity page for Yohei Nakajima (@yoheinakajima), creator of BabyAGI. Three-category agent taxonomy, BabyAGI evolutionary series (OG→Bee→Cat→2→2o→3), three-layer memory architecture, self-improving agents synthesis.
- `wiki/raw/articles/2026-05-19_yoheinakajima_state-of-statefulness-ai-agents.md` — Save: Raw article reconstruction for Yohei Nakajima's X Article "The State of Statefulness in AI Agents" (extraction limited — X Article endpoint blocked).
- `wiki/raw/articles/2026-05-07_yage_agent-filesystem-survey.md` — Save: Raw article for yage.ai survey "From Agent Memory to Agent Filesystem: What the Shift Really Means".


- `wiki/raw/articles/2026-05-19_yoheinakajima_state-of-statefulness-ai-agents.md` — Update: Full article retrieved via xurl --auth oauth2 /2/tweets/ID?tweet.fields=article (tweet.fields=article with OAuth2 user auth). Replaced partial reconstruction with complete plain_text. Key insights: "Models are stateless between turns — everything else exists because of that"; memory is six distinct problems; agents mutate (capability evolution); events capture what happened, graphs represent what is; branching is the hard problem; conversation may not be the correct substrate for persistent intelligence; the missing primitive is a persistent, reactive, inspectable, evolving state substrate.
- `wiki/concepts/agent-statefulness.md` — Enriched: Added ActiveGraph section (Nakajima Part 2): concrete continuity layer design, World Graph vs Workflow Graph distinction, 5-layer architecture (Events/Behaviors/Relations/Patches/Traces), everything-as-state, self-improvement with lineage. Added raw article source. Updated index.md summary.


- `wiki/raw/articles/2026-05-19_yoheinakajima_activegraph-continuity-layer.md` — Save: Full raw article for Nakajima's sequel "ActiveGraph: A Continuity Layer for Long-Running Agents" (2026-05-19). Fetched via xurl --auth oauth2 /2/tweets/ID?tweet.fields=article.
- `wiki/entities/yohei-nakajima.md` — Enriched: Expanded Statefulness Research section to two-part series with ActiveGraph (Part 2) summary.
- `wiki/concepts/agent-statefulness.md` — Enriched: Added ActiveGraph section (Nakajima Part 2): concrete continuity layer design, World Graph vs Workflow Graph distinction, 5-layer architecture (Events/Behaviors/Relations/Patches/Traces), everything-as-state, self-improvement via trace→evaluate→patch→fork→diff→promote. Updated index.md summary.

## 2026-05-19 — Create | Query Understanding concept page (systematized from Tunkelang's 24-article series)

- `wiki/concepts/query-understanding.md` — New concept page: Comprehensive systematization of Query Understanding as a discipline, based on Daniel Tunkelang's 24-article series on queryunderstanding.com (2016–2024). Covers the full 6-layer stack: characters → tokens → query rewriting → context → conversation → results. Includes all 24 articles mapped by layer with source URLs. Connects to LLM-era query understanding and [[concepts/agentic-search]]. Resolves dangling wikilink from [[entities/daniel-tunkelang]].
- `wiki/entities/daniel-tunkelang.md` — Enriched: Added "Query Understanding Publication Series" section with full 24-article table (numbered, dated, layered). Updated index.md entry to reference the series and concept page.
- `wiki/raw/articles/2016-10-28_daniel-tunkelang_query-understanding-introduction.md` — New raw article: Introduction to the Query Understanding series (Oct 2016). Defines QU as the communication channel between searcher and engine, maps the 6-layer curriculum.
- `wiki/raw/articles/2017-02-16_daniel-tunkelang_query-rewriting-overview.md` — New raw article: Overview of query rewriting strategies (Feb 2017). Recall (expansion, relaxation) vs. precision (segmentation, scoping).
- `wiki/raw/articles/2022-10-24_daniel-tunkelang_query-similarity.md` — New raw article: Query similarity via embeddings and bag-of-documents (Oct 2022). Superficial vs. semantic variation, head/torso→tail transfer learning.
- `wiki/index.md` — Added [[concepts/query-understanding]]; updated daniel-tunkelang entry; bumped counts (2032/1170/862).

## 2026-05-19 — Create | Content Understanding concept page (systematized from Tunkelang's 8-article series)

- `wiki/concepts/content-understanding.md` — New concept page: Comprehensive systematization of Content Understanding as the document/index-side counterpart to query understanding. Based on Daniel Tunkelang's 8-article series on medium.com/content-understanding (2021–2022). Covers the stack: classification → annotation → similarity → structure → quality → moderation + information extraction. CU vs QU comparison, virtuous cycle, 8 articles with source links.
- `wiki/entities/daniel-tunkelang.md` — Enriched: Added "Content Understanding Publication Series" section with full 8-article table (numbered, dated, focused).
- `wiki/concepts/query-understanding.md` — Cross-referenced: Added `[[concepts/content-understanding]]` to "Distinction from Related Concepts" section with explanation of CU as document-side counterpart.
- `wiki/raw/articles/2021-11-01_daniel-tunkelang_what-is-content-understanding.md` — New raw article: Introduction (Nov 2021). Defines CU as foundation of search, places it in search process, introduces virtuous cycle with QU.
- `wiki/raw/articles/2022-03-17_daniel-tunkelang_content-annotation.md` — New raw article: Reductionist approach — entity recognition, string matching, regex, POS tagging, LSTM-CRF.
- `wiki/raw/articles/2022-04-25_daniel-tunkelang_content-structure.md` — New raw article: Summarization (extractive/abstractive) + segmentation (heuristic/ML/snippets).
- `wiki/index.md` — Added [[concepts/content-understanding]]; bumped counts (2036/1171/865).

---

## [2026-05-20] create | Shopify AI transformation entity pages (4 entities from 2 source articles)

### Created / Replaced
- `wiki/entities/farhan-thawar.md` — Full entity page: Head of Engineering at Shopify, "pair with smart people on problems" philosophy, AI lab pairing, Code Red tech debt elimination (7 months), 1,000-intern champion, AI-first engineering practices.
- `wiki/entities/shopify.md` — Full entity page: AI-first engineering culture, LLM proxy architecture, tool adoption history (Copilot 2021 → Cursor → Claude Code), parallel agent patterns, MCP toolkit, CLAUDE.md as team infra, guardrails/permissions, 1,000-intern program, GSD project management, coding interviews for directors+.
- `wiki/entities/gergely-orosz.md` — Full entity page: Author of The Pragmatic Engineer newsletter/podcast, ex-Uber engineer, covers real-world engineering at big tech and AI tool adoption.
- `wiki/entities/zodchiii.md` — New entity page: Pseudonymous X/Twitter content creator, AI/finance/vibe coding, @zodchixquant Telegram channel, published viral Shopify Claude Code breakdown.

### Updated
- `wiki/SCHEMA.md` — Added 4 tags: `cursor`, `github-copilot` (Products section); `llm-proxy` (Infrastructure); `interns
- `wiki/index.md` — Updated entries for farhan-thawar, shopify, gergely-orosz with rich descriptions. Added new zodchiii

## [2026-05-20] ingest | CMA self-hosted sandbox providers (4 articles → 1 comparison + 4 entities + CMA enrichment) | kzinmr request

### Raw Articles Saved
- `wiki/raw/articles/2026-05-19_cloudflare_claude-managed-agents-sandbox.md` — Mike Nomitch, Cloudflare Blog
- `wiki/raw/articles/2026-05-19_daytona_claude-managed-agents-sandbox.md` — Daytona Documentation
- `wiki/raw/articles/2026-05-19_modal_claude-managed-agents-sandbox.md` — Modal Blog
- `wiki/raw/articles/2026-05-19_vercel_claude-managed-agents-sandbox.md` — Vercel Knowledge Base

### Created
- `wiki/comparisons/claude-managed-agents-sandbox-providers.md` — 4-provider comparison: Cloudflare/Daytona/Modal/Vercel Sandbox. 9-dimension comparison table (architecture, sandbox tech, scale, security, persistence, tools, pricing, strengths, customers), detailed per-provider sections, architecture diagrams, credential brokering spectrum, tooling comparison, verdict/synthesis with decision guidance.
- `wiki/entities/cloudflare-sandbox.md` — Cloudflare's CMA self-hosted sandbox entity: dual sandbox primitives (microVM + V8 isolates), proxy zero-trust, Browser Run + email tools, Workers AI integration.
- `wiki/entities/daytona-sandbox.md` — Daytona's CMA self-hosted sandbox entity: three-party architecture, dual orchestrator variants, snapshot-based sandboxes, 30-day lifecycle.
- `wiki/entities/modal-sandbox.md` — Modal's CMA self-hosted sandbox entity: GPU access (H100), 100K+ concurrent sandboxes, burst pricing, connect tokens, custom images. Including Mason AI/DoorDash/Blend endorsements.
- `wiki/entities/vercel-sandbox.md` — Vercel's CMA self-hosted sandbox entity: webhook-driven control plane, firewall-level credential brokering, microVM-based, TypeScript-native, OIDC token auth.

### Enriched
- `wiki/concepts/claude-managed-agents.md` — Added Sandbox Provider Options subsection with provider comparison table + cross-link to comparison page. Added 4 raw article sources.

### Index & Log
- `index.md`: +5 indexed entries (4 entities + 1 comparison); entities 629→633, comparisons 17→18, total 2060→2065.

## [2026-05-20] blog-wiki-ingest | Gemini 3.5 Flash, Ed Zitron economics, antirez EDIT tool, Karpathy joins Anthropic

### Source
- `blog-triage` checkpoint at `${HERMES_HOME}/cron/data/blog_ingest/triage_latest.json`
- 4 take + 2 reference candidates from 20 blog articles (May 19-20, 2026)

### Enriched Entity Pages

**entities/gemini.md** — Added Gemini 3.5 Flash section:
- Model specs: `gemini-3.5-flash` ID, 1,048,576 input / 65,536 output tokens, Jan 2025 knowledge cutoff
- Pricing: $1.50/$9 per M tokens (3x Flash Preview, 6x Flash-Lite)
- Product deployment: Gemini App, Google Search AI Mode, Antigravity, AI Studio, Enterprise
- Interactions API (beta) — Google's version of OpenAI Responses
- llm-gemini 0.32/0.32a0 support (reference candidates blog-16, blog-19)

**entities/ed-zitron.md** — Added "AI Is Too Expensive" section (May 19, 2026):
- Hyperscaler capex: Microsoft $100B OpenAI investment, $800B+ total, $3T+ break-even
- Zillow case study: $1M+ Q1 spend, on track for $7-10M/year (20-50% of 2025 net income)
- Stripe: $94K/day in Anthropic coding tokens
- ServiceNow CIO: "It's a really hard problem" — may not afford Claude Enterprise through year
- Goldman Sachs: AI costs approaching 10% of headcount
- Anthropic enterprise obfuscation: no SLAs, no granular telemetry
- Token budget accounting crisis: ROI cannot be reliably measured
- RPO analysis: hyperscaler growth entirely driven by OpenAI/Anthropic commitments

**entities/antirez-com.md** — Added EDIT tool redesign section:
- CAS mode token waste problem for local inference
- Line-tag format with 4-char CRC32 checksums (Q8fA, rA3_, Kq9z, PX0b)
- DeepSeek V4 Flash effective usage confirmed
- Whole-file CRC32 tradeoff discussion
- Links to [[concepts/agentic-engineering]] and [[concepts/ai-agent-engineering]]

**entities/andrej-karpathy.md** — Added May 2026 timeline entry:
- Karpathy joins Anthropic (announced via X, May 19, 2026)
- First major career move since founding Eureka Labs (2024)

### Raw Article Sources
- `raw/articles/simonwillison.net--2026-may-19-gemini-35-flash--d5349c1f.md`
- `raw/articles/wheresyoured.at--ai-is-too-expensive--2387fc59.md`
- `raw/articles/antirez.com--news-166--c7f12317.md`
- `raw/articles/daringfireball.net--linked-2026-05-19-karpathy-anthropic--c6d1c3dc.md`

### Reference Items Skipped
- blog-16 (llm-gemini 0.32) — incorporated into entities/gemini.md tooling support
- blog-19 (llm-gemini 0.32a0) — incorporated into entities/gemini.md tooling support



## [2026-05-20] dreaming-wiki-ingest | Nightly knowledge consolidation — Cohere Reliant AI, Warp Oz, Simon Willison PyCon

### Pages Enriched
**entities/cohere.md** — Added Acquisitions & Expansion section:
- Reliant AI acquisition (May 2026) — biopharma AI company, North for Pharma announcement
- Key details: founders Karl Moritz Hermann/VP AI Verticalizations, Marc Bellemare/VP Modelling, customers assumed (GSK, Medicus Pharma, Kyowa Kirin)
- Raw source: raw/articles/2026-05-20_cohere_cohere-acquires-reliant-ai-expand-sovereign-enterprise-ai.md

**entities/warp-terminal.md** — Added Oz Upgrade (May 2026) section:
- Multi-harness orchestration: Claude Code + Codex + Warp Agent in single control plane
- Automatic multi-agent orchestration for long-horizon tasks
- Cross-harness Agent Memory (research preview) — organizational knowledge index across harnesses
- Kubernetes self-hosting, granular cost controls, least-privilege permissions
- Raw source: raw/articles/2026-05-20_warp_multi-harness-cloud-agent-orchestration.md

**concepts/harness-engineering.md** — Added Warp Oz: Multi-Harness Control Plane section:
- First production multi-harness control plane — harness-as-component paradigm
- Cross-harness Agent Memory solves context persistence across harness boundaries
- Embodies Viv Trivedy's "no general-purpose agent" thesis
- Raw source: raw/articles/2026-05-20_warp_multi-harness-cloud-agent-orchestration.md

### Reference Items Skipped
- simon-willison.md — PyCon 2026 talk already captured (line 305, updated 2026-05-19)
- llm-gemini 0.32a0/0.32 — minor plugin releases, no wiki value

### Already Captured (318 of 321 raw articles)
- Google I/O 2026, Cursor Composer 2.5, Claude Managed Agents, Shopify AI-First Engineering
- Daniel Tunkelang IR articles, Cloudflare Glasswing, Armin Ronacher agent language design
- Yohei Nakajima statefulness, Han Lee RL env classification, Anthropic emotion concept
- SemiAnalysis ClusterMAX 2.0, non-AI content (math/vintage/general tech)

### Raw Articles Archived
- raw/articles/2026-05-20_cohere_cohere-acquires-reliant-ai-expand-sovereign-enterprise-ai.md
- Raw articles: raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search.md
- raw/articles/2026-05-20_warp_multi-harness-cloud-agent-orchestration.md
- Pages enriched: concepts/query-understanding.md (+185 lines LLM-Powered QU in Practice section)
  - Added: embedding collapse (hubness), structured QU, synonym extraction, category classification, cost optimization (dynamic Pydantic enums), caching strategy, empirical results (NDCG +12%)
  - Linked: entities/doug-turnbull, concepts/content-understanding
- Entities updated:
  - entities/doug-turnbull-speaking.md: Added LLM QU lecture entry + embedding collapse quote
  - entities/doug-turnbull.md: Updated date
