## 2026-04-23 — @pupposandro Xアカウント追加 + luceboxブログ取り込み

### Xアカウント追加
- **@pupposandro** (Sandro Puppo) — すでに`config/feeds/x-accounts.yaml`に存在確認済み。変更不要。
  - トピック: ai, local-llm, cuda, speculative-decoding, startup
  - 製品: lucebox (https://www.lucebox.com)

### Wikiエンティティページ作成（3件）
- [[entities/sandro-puppo]] — Sandro Puppo (lucebox創設者) のバイオグラフィー、技術的貢献、Xアカウント情報
- [[entities/lucebox]] — lucebox社概要、技術スタック（ggml, CUDA, speculative decoding）、製品ポートフォリオ
- [[entities/trycua-cua]] — TryCua/Cua（コンピュータ使用エージェント）、Sandro Puppoとの関係

### Wikiコンセプトページ作成（3件）
- [[concepts/dflash-ggml]] — DFlash speculative decoder: C++/ggml実装、Qwen3.5-27B Q4_K_M、207 tok/s on RTX 3090、3.43x AR
- [[concepts/megakernel-inference]] — Megakernel: hybrid DeltaNet/Attention LLMの全24レイヤーをsingle CUDA dispatchに融合、1.87 tok/J
- [[concepts/nvidia-egpu-macos]] — NVIDIA eGPU over USB4 on Mac: ベンチマーク、tinygrad NVIDIA driver、$300 dockの現実的性能

### ブログ記事スクレイピング（3件）
- `raw/articles/2026-04-23-dflash-ggml.md` — DFlash on ggml（SPEC DECODE）
- `raw/articles/2026-04-23-egpu-myth.md` — The eGPU Myth（BENCHMARK）
- `raw/articles/2026-04-23-megakernel.md` — Megakernel（CUDA）

### RSSフィード状況
- lucebox.com/blog: **RSSなし**（/feed, /feed.xml, /rss.xml, /atom.xml, /blog/feed 全て404）
- OPMLへの追加は見送り。lucebox blogは手動モニタリングまたはX(@pupposandro)投稿経由で追跡。

### index.md更新
- `trycua-cua`エントリ追加（行141付近）

## 2026-04-21 — dreaming: daily consolidation

### Duplicate Check Summary
- Items skipped (already processed by other jobs): 15+
  - Kimi K2.6 already in wiki → enriched with r/LocalLLaMA community reports
  - Qwen3.6-Plus already in wiki → enriched with deployment discussions
  - GitHub Copilot billing already processed (Daily Inbox 04-21)
  - Headless AI services already processed (Daily Inbox 04-21)
- Gaps filled: 2 (community deployment section on both pages)

### Consolidation Summary
- Articles reviewed: ~120 (RSS scan + Reddit highlights)
- Themes identified: 4 (local model deployment, AI pricing, headless services, test case minimization)
- Pages updated: 2
- Pages created: 0

### Updated Pages
- [[entities/qwen3-6-plus]] — Added "Community Deployment Reports" section: 8GB VRAM achievement, real-world coding work, Gemma4 vs Qwen3 debate, llama.cpp ecosystem notes
- [[concepts/kimi-k2-6]] — Added "Community Discussion" subsection: Opus 4.7 replacement confirmation, 8GB VRAM configs, Qwen3.6 comparison

## 2026-04-21 — Active Knowledge Crawl: ai-memory-systems + neurosymbolic-ai

### Raw Articles Added (5 sources)
- `raw/articles/crawl-2026-04-21-vector-db-agent-memory.md` — 5 types of AI agent memory (Sreeni Ramadorai)
- `raw/articles/crawl-2026-04-21-knowledge-graph-memory-agents.md` — Vector vs Graph vs Episodic memory architectures (Digital Applied)
- `raw/articles/crawl-2026-04-21-agentic-alternative-graphrag.md` — Contextual AI: agentic metadata search tool (Nov 2025)
- `raw/articles/crawl-2026-04-21-kleppmann-formal-verification-ai.md` — Kleppmann: AI will make formal verification mainstream (Dec 2025)
- `raw/articles/crawl-2026-04-21-shuvendu-intent-formalization.md` — Microsoft Research: intent formalization as grand challenge (Mar 2026)

### Pages Created (6 concept pages)
**From ai-memory-systems (prerequisites, medium):**
- [[vector-db-agent-memory]] — Vector DB for agent LTM/semantic memory: Mem0, Zep, pgvector, write-heavy/mutable/temporal properties
- [[knowledge-graph-memory-agents]] — Graph memory for multi-hop reasoning; hybrid vector+graph+episodic pattern; reference stacks (Neo4j, TypeDB, Zep)

**From neurosymbolic-ai (prerequisites, medium):**
- [[intent-formalization]] — Translating vague intent into formal specs; spec spectrum (tests→contracts→logical→DSL); key for vibe coding reliability
- [[formal-verification-llm-agents]] — AI bringing formal verification (Lean, Rocq, F*) mainstream; seL4 cost problem; vericoding movement

**New cross-topic connections:**
- [[agentic-alternative-to-graphrag]] — Contextual AI: metadata search tool as lightweight alternative to GraphRAG; 75.43% accuracy
- [[agentic-rag]] — Agentic RAG taxonomy: reflection, planning, tool-use, multi-agent patterns; 6 architecture types

### Index Updated
- `index.md` — Added "AI Memory & Retrieval Infrastructure" section (6 pages), updated Last updated

### Topics Crawled
- [[ai-memory-systems]] — last_crawled → 2026-04-21 (prerequisites: episodic/semantic memory, vector DB architectures)
- [[neurosymbolic-ai]] — last_crawled → 2026-04-21 (prerequisites: formal verification, intent formalization)

## 2026-04-21 — Inbox: RLM articles + @raw_works monitoring

### Raw Articles Added
- `raw/articles/raw-works-rlms-new-reasoning-models-2026-04-20.md` — RLM history, reasoning+tool-use timeline, three failure modes
- `raw/articles/raw-works-rlms-sota-on-longcot-2026-04-19.md` — DSPy.RLM + Qwen3 achieving SOTA on LongCoT

### Pages Updated
- `concepts/rlm-recursive-language-models.md` — Merged April 2026 RLM+DSPy breakthrough results (LongCoT benchmarks)
- `entities/raw-works.md` — NEW skeleton page for Raymond Weitekamp (@raw_works)
- `index.md` — Added raw-works entity + updated last_updated timestamp

### X Account Added
- `@raw_works` (Raymond Weitekamp) → `config/feeds/x-accounts.yaml` — RLM researcher, DSPy.RLM experiments

## 2026-04-20 — dreaming: daily consolidation

### Duplicate Check Summary
- Items skipped (already processed by other jobs): 15+
  - Jensen Huang interview → already enriched (Daily Active Crawl 04-18)
  - Claude Mythos evaluation → already covered (Daily Active Crawl 04-19)
  - WorkOS FGA authorization → already processed (Daily Inbox 04-13)
  - geohot zappa mitmproxy → already added (Daily RSS 04-15)
  - AI Digital NATO → already detailed (Daily Inbox 04-19)
- Gaps filled: 2
  - Noetik (Ron Alfa & Daniel Bear) — missing entity
  - Claude Code Routines — missing feature update

### Consolidation Summary
- Articles reviewed: 194 (94 RSS + 100 newsletter)
- Themes identified: 8
- Pages created: 1 (Noetik)
- Pages updated: 1 (Claude Code Routines → claude-code-best-practices.md)

### New Wiki Pages
- [[noetik]] — Biotech AI company, transformer models for cancer trial matching (95% failure rate → matching problem), GSK $50M deal, Ron Alfa & Daniel Bear founders

### Updated Pages
- [[claude-code-best-practices]] — Added "Claude Code Routines (April 2026)" section: reusable parameterized workflows in YAML, routine patterns (code-review, test-gen, docs), comparison table vs copy-paste approach

### NJ Delivery Filter
| Theme | NJ Score | Delivery |
|-------|----------|----------|
| Noetik cancer AI | 3/5 | Secondary — biotech AI breakthrough |
| Claude Code Routines | 2/5 | Brief — feature update |
| geohot zappa mitmproxy | 1/5 | Omit (already covered) |

---

## 2026-04-20 — GPT Models Concept Page

### New Concept Page
- `concepts/gpt-models.md` — GPT Model Series (GPT-1 to GPT-5.4, RLHF, o-series reasoning)

### Update
- `index.md` — Added gpt-models to AI Development & Engineering section

## 2026-04-20 — Active Crawl + GEPA / LLM-as-Judge / Agent Sandboxing

### Source
- Active Knowledge Crawl: 3 hot-topics crawled (dspy deepdive, ai-evals laterals, sandbox laterals)
- Priority selection: 3 topics (2 high, 1 medium) — GEPA, LLM-as-Judge, Agent Sandboxing
- Web searches: arXiv GEPA ICLR 2026, RLM arXiv 2512.24601, LLM-as-Judge scoring bias (arXiv 2506.22316), Northflank agent sandboxing guide

### New Raw Sources (4)
- `raw/articles/gepa-iclr2026-2026-04-20.md` — GEPA paper (arXiv 2507.19457, ICLR 2026 Oral)
- `raw/articles/rlms-recursive-language-models-2026-04-20.md` — RLM paper (arXiv 2512.24601)
- `raw/articles/llm-as-judge-scoring-bias-2026-04-20.md` — LLM-as-Judge scoring bias (arXiv 2506.22316v4, Ant Group)
- `raw/articles/agent-sandboxing-2026-northflank.md` — Agent sandboxing isolation spectrum (Northflank, Feb 2026)

### New Concept Pages (5)
- **`[[gepa]]`** — GEPA (Genetic-Pareto Prompt Evolution): ICLR 2026 Oral, 35x fewer rollouts than GRPO, Pareto quality+cost optimization, dspy.GEPA API
- **`[[rlms]]`** — RLMs (Recursive Language Models): inference-time self-optimization via recursive context access, DSPy vs RLM comparison, 10M+ token context scaling
- **`[[llm-as-judge]]`** — LLM-as-Judge: 3 bias types (rubric order/score ID/reference answer), 7 best practices, model robustness comparison, mitigation strategies
- **`[[offline-evaluation]]`** — Offline Evaluation: 3-layer eval stack (offline/human/production), golden dataset construction, regression testing, CI/CD integration
- **`[[agent-sandboxing]]`** — Agent Sandboxing: isolation technology spectrum (gVisor/Firecracker/Kata/MicroVMs), capability-based security, PTC pattern for code agents

### Active Crawl Results by Topic
| Topic | Policy | New Concept(s) | Source |
|-------|--------|----------------|--------|
| **dspy** | deepdive | GEPA + RLMs (2) | arXiv GEPA ICLR 2026, Omar Khattab's site |
| **ai-evals** | laterals | LLM-as-Judge + Offline Evaluation (2) | arXiv scoring bias, Medium evaluation guide |
| **sandbox** | laterals | Agent Sandboxing (1) | Northflank + AWS Builder articles |

### Updated Concept Pages (1)
- **`[[dspy]]`** — Added GEPA as DSPy optimizer (ICLR 2026 Oral), DSPy vs GEPA table, Phase 4 evolution

### Index Updates
- Added: gepa, rlms (under DSPy ecosystem section)
- Added: llm-as-judge, offline-evaluation (under AI Evals section)
- Added: agent-sandboxing (under AI Coding Agent Criticism section)

### Hot-Topics Update
- dspy: last_crawled → 2026-04-20
- ai-evals: last_crawled → 2026-04-20
- sandbox: last_crawled → 2026-04-20

## 2026-04-20 — RSS Scan + Claude 4.7 Tokenizer / Headless AI / Figma

### Source
- RSS scan: 84 blogs, 82 new articles
- simonwillison.net (3 new), martinalderson.com (1 new), other blogs (9 new)
- Reddit: r/LocalLLM (24), r/AI_Agents (23), r/LocalLLaMA (22)

### New Concept Pages (2)
- **[[claude-47-tokenizer]]** — Claude Opus 4.7 tokenizer change: 1.46x system prompts, 3.01x high-res images, ~40% cost increase for typical text
- **[[headless-ai-services]]** — Matt Webb's headless AI concept, Salesforce Headless 360, API-first wave (Brandur Leach)

### New Entity Page (1)
- **[[figma]]** — Figma vs Claude Design competitive analysis: SaaS moat失效, per-head pricing collapse, employee efficiency gap (2,000 vs <10)

### Updated Files
- `wiki/index.md` — Added 2 concepts + 1 entity, updated counts (82→83 entities, 82→84 concepts)

---

## 2026-04-20 — Context Graph Ingestion

### Source
- Foundation Capital: ["AI's Trillion-Dollar Opportunity: Context Graphs"](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity) (December 22, 2025)
- User's Japanese analysis with 6-point future predictions and 5-plane architecture

### New Concept Page
- **[[context-graph]]** — Decision traces vs. rules distinction, "two clocks problem," five-plane enterprise AI architecture (State → Orchestration → Decision → Control → Observability), three startup paths (replace all/modules/new SoR), why incumbents are structurally disadvantaged

### New Entity Pages (6)
- **[[foundation-capital]]** — VC firm, canonical source for context graph thesis
- **[[jaya-gupta]]** — Foundation Capital Partner, co-author of Context Graphs article
- **[[playerzero]]** — Path 3 startup: SRE automation with "engineering world model" context graph
- **[[arize]]** — Observability layer: "Datadog for agents"
- **[[maximor]]** — Path 2 startup: finance automation, ERP-agnostic audit-ready agents
- **[[regie-ai]]** — Path 1 startup: AI-native sales engagement replacing Outreach/Salesloft

### New Raw Source
- `wiki/raw/articles/foundation-capital-context-graphs-2025-12-22.md`

### Updated Files
- `wiki/index.md` — Added context-graph concept, 6 entity entries, updated counts (76→82 entities, 81→82 concepts)

---

## 2026-04-19 — Active Crawl + RSS Scan

### Active Crawl (2026-04-19)
Selected 3 topics: ai-agent-engineering (deepdive), harness-engineering (prerequisites), agent-team-swarm (laterals)

#### deepdive: ai-agent-engineering → 1 concept
- **[[multi-agent-consensus-patterns]]** — Multi-agent consensus patterns (Supervisor, Hierarchical, P2P, Swarm) + SWARM+ three-phase protocol (arXiv:2603.19431)
  - Source: [[raw/articles/swarm-plus-consensus-2026.md]], [[raw/articles/openlayer-multi-agent-architecture-2026.md]]

#### prerequisites: harness-engineering → 1 concept
- **[[elixir-beam-agent-orchestration]]** — Elixir/BEAM for agent orchestration: process supervision, GenServer, OpenAI Symphony architecture
  - Source: [[raw/articles/elixir-beam-agent-orchestration-2026.md]]

#### laterals: agent-team-swarm → 1 concept
- (shared with deepdive: multi-agent-consensus-patterns covers the lateral connection to distributed systems theory)

### New Raw Sources
- `wiki/raw/articles/swarm-plus-consensus-2026.md` — SWARM+ arXiv paper
- `wiki/raw/articles/openlayer-multi-agent-architecture-2026.md` — Openlayer architecture guide
- `wiki/raw/articles/elixir-beam-agent-orchestration-2026.md` — Elixir/BEAM for orchestration

### Updated Files
- `config/hot-topics.yaml` — Updated last_crawled for ai-agent-engineering, harness-engineering, agent-team-swarm
- `wiki/index.md` — Added multi-agent-consensus-patterns, elixir-beam-agent-orchestration

## 2026-04-19 — RSS Scan + Wiki Updates

### Phase 1: Daily Scan
- RSSスキャン: 84ブログ中78件新規記事
- Reddit: r/LocalLLM(23), r/AI_Agents(22), r/LocalLLaMA(21)の大量新着
- ブログ記事: Simon Willison(2), Daring Fireball(2)など12件

### Phase 2: Triage
- Simon Willison 2件: システムプロンプト分析（Opus 4.6→4.7 diff）、Gitタイムライン化ツール
- John D. Cook 1件: NF4量子化の数学的解析
- その他10件: スキップ（報道・ハードウェア質問・歴史的トピック）

### Phase 3: Wiki Updates
- **entities/simon-willison.md** — updated=2026-04-19、Sourcesに2件追加
  - Changes in system prompt between Claude Opus 4.6 and 4.7 (Apr 2026)
  - Claude system prompts as a git timeline (Apr 2026)
- **entities/john-d-cook-applied-mathematics-consulting.md** — updated=2026-04-19、Sourcesに1件追加
  - Gaussian distributed weights for LLMs: NF4 and QLoRA (Apr 2026)

## 2026-04-19 — Cross-Reference Network: Entity ↔ Concept Linking

### Group 1: OpenAI系エンティティ (greg-brockman ↔ john-schulman)
- **greg-brockman.md** → `john-schulman` (既に存在 ✅)
- **john-schulman.md** → `greg-brockman` (既に存在 ✅), `mira-murati` (追加 ✅), `concepts/ai-safety` (追加 ✅)
- **ai-safety.md** (新規作成 ✅) — RLHF, Scalable Oversight, 2023-2024 Safety Exodus, Brockman vs Schulman philosophy

### Group 2: AI Evals系 (drmaciver ↔ shreya-shankar ↔ hamel-husain)
- **ai-evals.md** → `drmaciver`, `shreya-shankar`, `hamel-husain` (追加 ✅), `property-based-testing` (追加 ✅)
- **drmaciver.md** → `ai-evals-people` (追加 ✅)
- **shreya-shankar.md** → `drmaciver` (追加 ✅)
- **hamel-husain.md** → `drmaciver` (追加 ✅), `shreya-shankar` (追加 ✅)

### Group 3: Pydantic/Structured Outputs (jason-liu ↔ samuel-colvin)
- **jason-liu.md** → `samuel-colvin` (追加 ✅), `concepts/structured-outputs` (追加 ✅)
- **samuel-colvin.md** → `concepts/structured-outputs` (既に存在 ✅)
- **pydantic.md** → `jason-liu` (追加 ✅)
- **structured-outputs.md** → `jason-liu` (既に存在 ✅), `samuel-colvin` (既に存在 ✅)

### Group 4: AI Safety (john-schulman ↔ mira-murati)
- **john-schulman.md** → `mira-murati` (追加 ✅)
- **mira-murati.md** → `john-schulman` (追加 ✅), `entities/sam-altman` (format fix), `entities/ilya-sutskever` (format fix), `entities/thinking-machines-lab` (format fix)
- **ai-safety.md** (新規作成 ✅)

### New Concept Pages
- **concepts/ai-safety.md** — AI Safety: Alignment, Oversight, and Interpretability (L2, complete)

### Updated
- **wiki/index.md** — Added ai-safety entry
- **wiki/log.md** — This entry

## 2026-04-19 — Entity Deduplication: Merged Duplicate Person Pages

### Merged Duplicates
- **simonw.md → simon-willison.md**: Deleted skeleton duplicate (simon-willison.md already L3 with `aliases: [simonw]`)
- **buttondown-com-hillelwayne.md → hillel-wayne.md**: Deleted newsletter-domain duplicate (hillel-wayne.md is canonical person page, added `aliases: [buttondown-com-hillelwayne, computer-things-newsletter]`, updated index.md reference)

### New Skill Created
- **wiki-entity-dedup**: Systematic procedure for detecting (wiki_graph.py score ≥ 9.0), merging, and cleaning up duplicate entity pages. Integrates with wiki-graph-health cron job.

## 2026-04-19 — Speech Models Separation: Whisper Moved from Multimodal

### New Concept Pages
- **concepts/speech/_index.md** — Speech Models overview (Whisper, TTS, AudioCraft — audio-language specific models)
- **concepts/speech/whisper.md** — Whisper: OpenAI's Speech Recognition Model (680k hours, 99 languages, ASR)

### Updated Existing Pages
- **concepts/multimodal/_index.md** — Removed Whisper from core models table. Added cross-reference note: "Whisper moved to [[speech/whisper]]"
- **wiki/index.md** — Added Speech Models category with `_index` and `whisper` entries under AI Agent Engineering section
- **wiki/log.md** — This entry

### Key Rationale
- **Multimodal** = vision-language cross-modal systems (CLIP, LLaVA) — spatial + semantic alignment
- **Speech** = audio-language specific models (Whisper, TTS, AudioCraft) — temporal signal processing
- These are conceptually distinct: different architectures, different use cases, different deployment patterns
- Speech models operate on temporal audio signals, not spatial visual features
- This separation enables cleaner taxonomy for audio-specific quantization, local deployment, and agent integration patterns

### Sources
- OpenAI Whisper paper (2022) — "Robust Speech Recognition via Large-Scale Weak Supervision"
- Meta AI AudioCraft documentation
- llama.cpp GGUF quantization docs

---

## 2026-04-19 — OpenClaw Concept Hierarchy Consolidation

### New Concept Pages (concepts/openclaw/ 階層)
- **concepts/openclaw/_index.md** — OpenClawコンセプト集約ナビゲーションハブ（status: draft → active）
- **concepts/openclaw/philosophy.md** — Primitives First哲学（既存ページを階層内へ移動）
- **concepts/openclaw/five-tier-precedence.md** — Five-Tier Skill Precedence Model（既存ページを階層内へ移動）
- **concepts/openclaw/ecosystem-tools.md** — OpenClaw Ecosystem Tools（既存ページを階層内へ移動）
- **concepts/openclaw/architecture-comparison.md** — OpenClaw vs Hermes Architecture Comparison（新規作成。Skill Explosion Problem, Product Positioning Framework）
- **concepts/openclaw/anthropic-conflict.md** — Anthropic-OpenClaw Conflict（既存ページを階層内へ移動）

### Updated Existing Pages
- **wiki/index.md** — Added "OpenClaw Ecosystem" section with full subpage hierarchy tree
- **wiki/log.md** — This entry

### Key Concepts Consolidated
- **Product Positioning Framework:** カテゴリ定義者のボードで戦うな（nanoclaw等が失敗）、新しいゲームを作れ（Hermesの勝ち手）
- **Skill Explosion Problem:** Hermesのself-authoringが抱える重複スキル問題
- **Five-Tier Precedence:** 決定論的スキル優先度（grep一発で追跡可能）
- **Claw Tax Economics:** OpenClaw $109.55/日 vs 一般開発者 $6/日（18xギャップ）
- **AGENTS.md Pattern:** Explicit > Implicit（ツール起動精度の最適化）

### Sources
- elvis analysis thread (April 2026) — 9-hour side-by-side source code study
- OpenClaw VISION.md
- Anthropic subscription policy changes (April 2026)
- Computerworld, TechCrunch, Business Insider coverage

---

## 2026-04-19 — Elvis Sun Entity Enrichment (elvis.so full crawl)

### Updated Entity Page
- **entities/elvis-sun.md** — Enriched from skeleton → full. Added 13+ blog posts from elvis.so: Vibe-Launching framework, Attention Flywheel, Newsjacking psychology, AI cold email systems, Context Lake architecture, Bootstrapping lessons, Platform risk warnings. Updated status: skeleton → enriched.

### Key Frameworks Extracted
- **Vibe-Launching:** Real-time iteration during viral moments (opposite of code freeze). ismypitchshit.com case study: VC > 1.0 through engineered shareability
- **Attention Flywheel:** Cross-channel amplification (X → Reddit → PR → Warm DMs)
- **Newsjacking:** 5 psychological triggers for viral content (Polarizing Promise, Contrarian Insight, Pattern Interrupt, Social Proof Baking, Self-Deprecation)
- **AI Cold Email System:** Clay + PhantomBuster + Apify stack, 15% reply rate at scale
- **Context Lake:** 3-tier PKM (Raw Input → Generated Derivatives → Output Layer)
- **Platform Risk:** "Never build your castle on someone else's land" — PressPulse lost 10% MRR when HARO shut down

### Sources
- www.elvis.so/archive (13+ articles scraped)
- x.com/elvissun (X/Twitter profile)
- medialyst.ai, presspulse.ai, solarflarepr.com

---

## 2026-04-19 — Mismanaged Geniuses Hypothesis (MGH) Concept Page Created

### New Concept Page (1件)
- **concepts/mismanaged-genius-hypothesis.md** — Frontier LMs are severely underutilized due to sub-optimal scaffolding. Composition > scaling. Qwen3-4B + RL bootstrapping proof. Authors: Alex Zhang, Zed Li, Omar Khattab.

### Updated Existing Pages
- **entities/alex-zhang.md** — Added MGH section (Core Ideas #5), updated publications table, added MGH to related_concepts
- **wiki/index.md** — Added MGH to concept pages list (78 → 79), updated last_updated date

### Raw Sources
- alexzhang13.github.io/blog/2026/mgh/ — The Mismanaged Geniuses Hypothesis (April 2026)
- alexzhang13.github.io/blog/2026/scaffold/ — Language Models will be Scaffolds (Feb 2026)
- arXiv:2512.24601 — Recursive Language Models (Oct 2025, foundational work)

---

## 2026-04-18 — Active Crawl: Context Engineering & Local LLM

### Prerequisites Crawl: context-engineering → token-economics, attention-mechanism-variants, context-compression
- **concepts/token-economics.md** — LLM inference cost analysis, 4 optimization layers, API vs self-host economics, real-world case study ($39K → $16K/month)
- **concepts/attention-mechanism-variants.md** — MHA, GQA, MLA, SWA, DSA, Gated Attention, Hybrid architectures. Architecture selection matrix.
- **concepts/context-compression.md** — Summarization, retrieval, structural compression techniques. Compression ratio vs quality trade-offs.

### Laterals Crawl: agentic-engineering → speculative-decoding
- **concepts/speculative-decoding.md** — Draft-and-verify inference acceleration, EAGLE-3, self-speculative decoding. 2-4x speedup with zero quality loss.

### Updated Existing Pages
- **concepts/context-engineering.md** — Added Prerequisites & Supporting Concepts section with cross-references to new pages

### Raw Sources Added
- raw/articles/crawl-2026-04-18-token-economics.md (Introl inference economics)
- raw/articles/crawl-2026-04-18-nvidia-speculative-decoding.md (NVIDIA blog)
- raw/articles/crawl-2026-04-18-self-speculative-decoding-zhang.md (arXiv paper)
- raw/articles/crawl-2026-04-18-context-compression.md (LangChain patterns)

---

## 2026-04-18 — Elvis Sun Entity Page Added

- **entities/elvis-sun.md** — 4x founder, ex-Google/Firebase. Medialyst.ai, PressPulse.ai ($100k+ rev), Solar Flare PR. Context Lake system, vibe-launching, AI-powered growth hacking.
- **config/feeds/x-accounts.yaml** — Added @elvissun (Elvis Sun)
- **config/feeds/blogs.opml** — Added elvis.so (Note: no RSS feed, HTML scraping only)
## 2026-04-18 — Hermes vs OpenClaw Architecture Analysis (elvis)

### New Entity Page (1件)
- **entities/elvis.md** — AI agent architecture analyst. 9-hour Hermes vs OpenClaw source code comparison. Skill Explosion Problem identification. Rails vs Linux/Kubernetes product positioning framework.

### New Concept Page (1件)
- **concepts/skill-architecture-patterns.md** — Skill self-improvement vs governed approaches. Hermes Agent's autonomous skill creation loop (prompt nudge + background review + pre-compression flush) vs OpenClaw's five-tier precedence model with strict governance. Includes Skill Explosion Problem analysis, AGENTS.md optimization pattern, and strategic product positioning framework.

### New Comparison Page (1件)
- **comparisons/hermes-vs-openclaw-architecture.md** — Detailed architecture comparison covering skill management, tool activation correctness, memory/context design, product ecosystem, and strategic positioning analysis.

### Updated Entity Pages
- **entities/hermes-agent.md** — Added "Skill Self-Improvement Architecture" section with mechanism, empirical results, and known Skill Explosion Problem challenge
- **entities/peter-steinberger.md** — Added "OpenClaw Architecture & Skill Governance" section with five-tier precedence model, anti-bloat policy, and product philosophy

### Updated Files
- **wiki/index.md** — Added skill-architecture-patterns concept, hermes-vs-openclaw-architecture comparison, elvis entity, updated counts
- **wiki/log.md** — This entry

### Key Insights
- **Skill Explosion Problem**: Self-authoring skills grow faster than they consolidate — agent creates adjacent redundant skills instead of patching existing ones
- **Five-tier precedence**: OpenClaw's workspace > user global > managed > bundled > extra model enables deterministic debugging
- **Explicit > Implicit**: AGENTS.md + TOOLS.md pattern yields better tool activation correctness than skill-based routing
- **Product positioning**: Competing on a category-definer's board fails; creating a new game (Hermes's maximalist approach) succeeds
- **Rails vs Linux**: Hermes = batteries-included (strong defaults), OpenClaw = primitives-first (guarantees over defaults)

---

## 2026-04-18 — Causal Backbone Conjecture (tailcalled)

### New Concept Page (1件)
- **concepts/causal-backbone-conjecture.md** — The Causal Backbone Conjecture by tailcalled (LessWrong, 2024-08-17). Resource-constrained selection theorem for agent-like structures. Argues against exhaustive world modeling in favor of sparse, high-leverage node tracking. Proposes that causal influence follows long-tailed distribution — few entities dominate pathways that matter.

### Raw Article Saved
- **raw/articles/tailcalled-causal-backbone-conjecture-2024.md** — Original LessWrong post archived

### Updated Files
- **wiki/index.md** — Added Causal Backbone Conjecture to AI Safety & Alignment section
- **wiki/log.md** — This entry

### Key Insights
- **Resource constraints drive agent emergence**: Unlike task-richness theories, the conjecture shows agent-like structures emerge from finite resource competition
- **Sparse modeling > exhaustive simulation**: Only backbone segments (high-resource flows) need accurate modeling; rest is noise
- **Distribution shifts are existential**: Entities anchored to outdated resource distributions face extinction without adaptive capacity
- **AI architecture implications**: Suggests modular, backbone-segment specialist designs over monolithic world models

---

## 2026-04-17 — Search×Agent Entity Expansion: Lester Solbakken & Sheshansh Agrawal

### New Entity Pages (2件)
- **entities/lester-solbakken.md** — Hornet Founding Engineer, Vespa.ai Principal Engineer, 13yr Yahoo/Verizon Media。PhD AI/ML (NTNU)。Mutually Assured Distraction thesis。Context engineering = relevance engineering。Synthetic query generation。Verifiable feedback loops (coding agent success)。Schema-first APIs。
- **entities/sheshansh-agrawal.md** — Contextual AI Director of Research, 元Microsoft Research (Bing Ads embeddings, 100M+ users, trillions tokens)。IIT Bombay。CER-C metric (trajectory-level efficiency)、On-policy distillation + RL for search planners、Agentic alternative to GraphRAG、BlitzRank reranker。XPERT (SIGIR 2023)、DECAF、ECLARE。

### Updated Files
- **wiki/index.md** — Information Retrieval & RAGセクションにSolbakkenとAgrawalを追加
- **wiki/log.md** — This entry

### Key Insights
- **3軸の convergent thesis**: Turnbull (ユーザー視点: simple BM25 > thick API), Solbakken (インフラ視点: schema-first + throughput), Agrawal (アルゴリズム視点: joint tool+planner optimization + CER-C metric)。すべて「エージェントには新しい検索が必要」という結論に合流
- **Mutually Assured Distraction** (Solbakken): better retriever + better reasoner = less reliable。信頼性-awareな統合が必要
- **CER-C metric** (Agrawal): エージェントが1トークンあたりにどれだけ速く証拠を集めるかを測定する独自指標。single-call IR metricsでは捉えきれないtrajectory-level efficiencyを計測

---

## 2026-04-17 — Daily Wiki Ingestion: LLM Training Coherence, Agentic AI + MCP, Reasoning Models Illusion, Qwen3.6-35B-A3B Quants

### New Concept Page (1件)
- **concepts/llm-training-coherence-evolution.md** — Giles Thomas (gpjt)の163MパラメータGPT-2モデルをFineWebでトレーニングし、57チェックポイントにわたるコヒーレンス進化を可視化。Karpathyの2015年RNN実験との比較分析。構文学習→意味学習→現実グラウンディングの3段階。

### Updated Pages (3件)
- **entities/troy-hunt.md** — HIBP MCP Server統合（AIエージェントがブリーチデータを自然言語で照会可能）、OpenClaw+Telegramアジェンティックワークフローのデモ記事を追加。タイムライン2026-04にMCPエントリ追加。
- **concepts/illusion-of-thinking.md** — The Signal newsletter「The illusion of thinking」の関連記事3本を統合。AIハルシネーションの根本的性質、CoTの演出性、問題複雑性による推論能力の限界。
- **concepts/reasoning-models.md** — ステータスをskeleton→activeに更新。コヒーレンス問題（Giles Thomas実験）とイリュージョン問題（The Signal newsletter）のセクションを追加。
- **entities/qwen3-6-plus.md** — Qwen3.6-35B-A3BのK_P quantsおよびUncensored Aggressiveバージョンリリース情報を追加。

### Key Insights
- **Coherence ≠ Correctness**: LLMはトレーニングの1/3で構文的に流暢になるが、事実グラウンディングには完全なトレーニングが必要。これはreasoningモデルの「もっともらしいが誤った推論」問題と直接関連
- **MCP as Infrastructure Standard**: HIBPのMCP実装は「セキュリティデータへのAIエージェントアクセス」の具体例。自然言語インターフェースが業界標準になりつつある
- **Qwen Community Ecosystem**: A3Bの量子化・アンセンスード版が即日に公開されるコミュニティの活発さは、オープンモデルエコシステムの成熟を示す

---

## 2026-04-18 — Back of House Multi-Agent Patterns (MilksandMatcha + 0xSero)

### Raw Articles
- [[raw/articles/milksandmatcha-0xsero-single-agent-nightmare-2026]] — "Single-agent AI coding is a nightmare for engineers" by Sarah Chieng (@MilksandMatcha) and @0xSero. Comprehensive analysis of single-agent ceiling and multi-agent back-of-house patterns.

### Concepts
- [[back-of-house-patterns]] — Multi-agent orchestration framework using kitchen metaphor (Head Chef/Line Cooks). Co-authored by [[milksandmatcha|Sarah Chieng]] and [[sero|0xSero]].
- [[single-agent-ceiling]] — The inherent limitations of single-agent coding workflows. The "sloperator" anti-pattern and why multi-agent architecture is necessary for complex tasks.

### Entities
- [[milksandmatcha]] — Sarah Chieng, AI agent educator. Co-author of Back of House framework. Added to x-accounts.yaml monitoring list.
- [[sero]] — Updated to include Back of House co-authorship contribution.

---

## 2026-04-17 — Search Engineer Entity Enrichment: Jo Kristian Bergum & Doug Turnbull

### Updated Entity Pages (2件)
- **entities/jo-bergum.md** — Hornet CEO, former Vespa Chief Scientist。相互参照追加: [[Doug Turnbull]]とのリンク
- **entities/doug-turnbull.md** — 2つの重要ブログ記事の詳細分析追加: 「Reasoning Agents Need Bad Search」（エージェントには薄い検索APIが最適）、「Semantic Search Without Embeddings」（階層的タクソノミー+BM25で意味検索可能）。相互参照追加: [[Jo Kristian Bergum]]

### Updated Files
- **wiki/index.md** — Information Retrieval & RAGセクションにjobergumとsoftwaredougを追加
- **wiki/log.md** — This entry

### Key Insights
- **「Agents are the new user of search」** — BergumのHornet設立 thesis。エージェントは長い構造化クエリを反復的に発行し、全文を読む。スニペット不要。
- **「Thick search APIs are counterproductive for agents」** — Turnbullの実証。単純なBM25 + 明示的なドキュメントの方が、エージェントの反復的推論には有効。
- **「Semantic search without embeddings」** — 階層的タクソノミーをBM25で検索。specificityが自然にスコアに反映される。

---

## 2026-04-16 — Anthropic Claude Code: 1M Context & Session Management Strategies

## 2026-04-16 — Daily Scan Wiki Ingestion (11件)

### New Concept Pages (6件)
- **concepts/gold-diff-distillation.md** — Gold Diff Distillation: RLベース蒸留手法。ユーザーの最終受容状態をターゲット、中間出力をペナルティ。模倣トレーニングの限界突破
- **concepts/halo-loss-attention-sinks.md** — HALO Loss: Attention Sink現象への対処。調和的正則化でトークン崩壊防止。石鹸泡エネルギー最小化アナロジー、長期コンテキスト生成安定性
- **concepts/ai-index-report-2026.md** — Stanford HAI AI Index Report 2026: SWE-bench ~100%、米中能力収束、5,427米国データセンター、TSMC独占、Jagged Frontier、88%組織導入
- **concepts/behavioral-trait-transmission.md** — Subliminal Learning: 初期化共有モデル間で無関係データを通じた行動特性伝達。蒸留安全性、フィルタリング不十分、来歴追跡の必要性
- **concepts/agent-survival-benchmark.md** — Agent Survival/PvPベンチマーク: 攻撃性≠勝利。適応性・リソース管理・戦略的忍耐の重要性。エージェント評価パラダイムシフト
- **concepts/flashattention-pytorch-educational.md** — FlashAttention (FA1-FA4)教育的PyTorch実装。アルゴリズム的明晰さ重視、アルゴリズムと実装の乖離可視化

### Updated Entity Pages (5件)
- **entities/qwen3-6-plus.md** — Qwen3.6-35B-A3B MoE仕様追記、20.9GB GGUF量子化、SVG pelicanベンチマーク（Opus 4.7上回る）、戦略的文脈追加
- **entities/pluralistic-net.md** — 「AI Pascal's Wager & ドゥーマー議論」セクション追加: $1.4T支出、$2-3T Altman要求、Muskダイソン球、corporate monopolies as threat vectors
- **entities/antirez-com.md** — タイムラインエントリ追加、「AI Cybersecurity: Not Proof of Work」核心アイデア: 戦略的知性/アーキテクチャ的簡素性が勝つ
- **entities/dwarkesh-patel.md** — 今週の学習メモ更新: 並列事前トレーニング、蒸留停止可能性、サイバーセキュリティ平衡、パイプラインRL、失敗原因分析
- **entities/lcamtuf.md** — 「Secret Life of Circuits」と「Infosec Punditry回避理由」セクション追加: 直感的理解 vs 形式的証明、複雑性とセキュリティの関係

### Updated Files
- **wiki/index.md** — AI Safety & Alignmentセクション追加、Agent Evaluationセクション追加
- **wiki/log.md** — This entry

### Sources
- Simon Willison blog (llm-anthropic, Qwen3.6 benchmark, datasette previews)
- True Positive Weekly #157 newsletter (AI Index, FlashAttention, HALO Loss, Subliminal Learning)
- r/AI_Agents (Agent Survival Benchmark)
- dwarkesh.com (What I learned this week)
- pluralistic.net (AI Pascal's Wager)
- antirez.com (AI cybersecurity)
- lcamtuf.substack.com (Secret Life of Circuits, Infosec Punditry)

### New Raw Article
- `raw/articles/anthropic-claude-code-session-management-1m-context.md` — Anthropic公式ブログ: Claude Codeの1Mコンテキストウィンドウ、セッション管理戦略、/usageコマンド (2026-04-15, Thariq Shihipar)

### Updated Concept Pages
- **[[context-window-management]]** — Anthropic公式1Mコンテキストセクション追加: 5つのセッション分岐戦略(Continue/Rewind/Compact/Clear/Subagents)、意思決定マトリックス、/usageコマンド、プロアクティブコンパクションパターン
- **index.md** — ヘッダー更新

### Key Insights
- **1MコンテキストでもContext Rotは依然として課題** — アテンションの拡散により、古い情報が現在のタスクを妨害
- **5つのセッション分岐戦略は実用的フレームワーク** — Continue（継続）、Rewind（巻き戻し）、Compact（圧縮）、Clear（クリア）、Subagents（委譲）
- **手動コンパクションが自動より優位** — 1Mの余裕があるため、`/compact focus on X`で次の作業方向を指示できる
- **/usageコマンド新機能** — セッション消費量の可視化

---

## 2026-04-16 — Rehan van der Merwe: SQS Lambda ESM Scaling + ECS Fargate Scaling + Distributed Monolith Refactoring

### New Concept Pages
- **[[sqs-lambda-esm-scaling]]** — SQS Lambda ESM Scaling Behaviours. Rehan van der Merweの実験ベース分析: 7つのスケーリングパターン、バッチサイズとコールドスタートの関係、エラー時のスループット低下、バックプレッシャー制御。AI Agentのタスクキュー設計への示唆。
- **[[ecs-fargate-scaling]]** — ECS Fargate Scaling. Lambdaのバースト処理性能に迫るECS最適化実験。カスタムメトリクス、ステップスケーリング、2-3分の初期スケールラグの回避策。AI Agentのコンピュートプール設計へのマッピング。

### Updated Entity Pages
- **[[rehan-van-der-merwe]]** — ソース追加（SQS Lambda ESM Scaling、ECS Fargate Scaling、Distributed Monolith Refactoring、From Monolith to Resilient Microservices）。既存のAI Agent MappingテーブルにSQS/ECSパターン追加済み。

### Raw Articles Ingested
- `raw/articles/rehanvdm-sqs-lambda-esm-scaling.md` — 7 SQS Lambda ESM Scaling Behaviours (2026-03-31)
- `raw/articles/rehanvdm-scaling-ecs-fargate-like-lambda.md` — Scaling ECS Fargate like Lambda (2026-02-11)
- `raw/articles/rehanvdm-refactoring-a-distributed-monolith-to-microservices.md` — Refactoring a distributed monolith to microservices
- `raw/articles/rehanvdm-from-monolith-to-resilient-microservices.md` — From monolith to resilient microservices

### Key Insights
- **ESMはキュー深度でスケールしない** — AI Agentのタスクキュー設計では、明示的なバックプレッシャー制御が必要
- **エラーはスループットに壊滅的影響** — 1%エラー率で20%低下。Agentは例外を投げるのではなくBatch Item Failureを使用すべき
- **ECSの2-3分スケールラグは不可避** — カスタムメトリクスで1分短縮可能だが、Agentのウォームスタート戦略に影響
- **EventBridge EDA** — 同期HTTPチェーンを非同期pub/subに置き換えることで、Agent間のカスケード障害を防止

### Updated
- **wiki/index.md** — SQS/ECS concept pages追加、Cloud Architecture & Distributed Systemsセクション新設
- **wiki/log.md** — このエントリ

---

## 2026-04-16 — APOSD vs Clean Code: Ousterhout-Martin Debate

### New Comparison Page
- **[[comparisons/aposd-vs-clean-code]]** — Structured debate between John Ousterhout (APOSD) and Robert C. Martin (Clean Code), Sept 2024–Feb 2025. Covers method length (deep vs shallow), comments as documentation, PrimeGenerator case study, TDD vs Bundling.

### Raw Articles Ingested
- `wiki/raw/articles/aposd-vs-clean-code-debate-2026-04.md` — Original GitHub repo README with full debate transcript.

### Key Insights
- **Deep modules vs small functions**: Ousterhout argues for deep interfaces (high functionality, simple API); Martin advocates small, single-purpose functions.
- **Comments**: Martin sees comments as "failures" — code should be self-documenting. Ousterhout argues missing comments cause far more productivity loss than stale ones.
- **TDD vs Bundling**: Martin advocates test-first in tiny cycles; Ousterhout prefers design-first with bundled testing.
- **PrimeGenerator case study**: Both struggled to explain a complex algorithm to each other, highlighting the curse of knowledge.
- **AI Agent relevance**: This debate directly shapes how coding agents (Claude Code, Codex) should structure code, write tests, and document their work.

### Updated
- **wiki/index.md** — Added comparison page entry, updated count from 7 to 8.
- **wiki/log.md** — This entry.

---

## 2026-04-16 — OpenAI Agents SDK v0.14.0 GA (Sandbox Execution) + Jason Liu "In Distribution" Theory

### Raw Articles Ingested
- `wiki/raw/articles/openai-agents-sdk-next-evolution-2026-04.md` — OpenAI blog post announcing Agents SDK v0.14.0 GA with sandbox execution, Harness/Compute architecture split, and provider ecosystem (Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel). Customer validation: Oscar Health clinical workflow automation.
- `wiki/raw/articles/openai-sandbox-agents-api-guide-2026-04.md` — Official API documentation for OpenAI Sandbox Agents. Covers: SandboxAgent lifecycle, Manifest abstraction, Capabilities (file I/O, shell commands, dependency installation, port exposure), SandboxRunConfig, session state persistence/resume, and security boundaries (default-deny, relative paths only, `..` traversal blocked).
- `wiki/raw/articles/jason-liu-sandboxes-agents-sdk-2026-04.md` — Jason Liu (@jxnlco) X thread on sandbox engineering and "in distribution" theory. Key thesis: built-in tools (shell, compaction, memory) work better because they're in the model's training distribution. Brain/Hands separation: lightweight tasks need no sandbox, heavy tasks need isolated compute. Five sandbox application patterns: code generation, data room extraction, artifacts, browser use, autonomous research.

### Entity Pages
- **[[openai]]** — OpenAI corporate entity. Covers leadership (Altman, Brockman, Sutskever), product suite (GPT-5.4, ChatGPT, Codex, Symphony, Agents SDK v0.14.0 GA), security architecture, pricing model, and customer validation (Oscar Health).

### Concept Pages
- **[[openai-agents-sdk]]** — OpenAI Agents SDK v0.14.0. Details: Harness vs Compute separation (control plane vs execution plane), standardized integrations (MCP, Skills, AGENTS.md, Shell, Apply Patch), Manifest-based workspace portability with multi-cloud storage (AWS S3, GCS, Azure Blob, CF R2), provider ecosystem compatibility, session lifecycle (Live → RunState resume → session_state resume → New), security model (default-deny, relative paths enforced, `..` blocked), Jason Liu's "in distribution" framework.

### Updated
- **[[jason-liu]]** — Added "In Distribution" Theory & Sandbox Engineering section. Key concepts: tool naming impact (bash vs shell vs run_command affects model performance), Brain/Hands separation, security by isolation, pragmatic sandbox provisioning.
- **[[sandbox]]** — Added OpenAI Agents SDK Sandboxes to Infrastructure layer in sandbox taxonomy table. Explicitly positioned as externalized, infrastructure-level isolation (Docker/Firecracker equivalents via cloud providers) with Harness/Compute separation. Contrast: SDK sandbox boot latency ~100ms-2s vs Monty in-process 0.004ms.
- **[[wiki/index.md]]** — Updated Entity Pages count to 73, Concept Pages count to 71. Added entries for openai entity and openai-agents-sdk concept. Updated last-modified date.

---

## 2026-04-16 — Ungrounded Meaning + CoALA Concepts (Shunyu Yao on Merrill et al.)

### New Concept Pages
- **[[ungrounded-meaning]]** — Ungrounded Meaning. Analysis of Merrill et al.'s arXiv:2104.10809 "Provable Limitations of Acquiring Meaning from Ungrounded Form" through Shunyu Yao's critique. Key findings: assertions alone cannot enable semantic emulation; the halting problem barrier applies universally; grounding through logical operators and environment interaction is non-negotiable for true understanding. Connects to CoALA, Harness Engineering, and Neurosymbolic AI.
- **[[coala]]** — CoALA: Cognitive Architectures for Language Agents. Unified framework (Sumers, Yao, Narasimhan, Griffiths) mapping LLM agents to cognitive science lineage (Soar, ACT-R). Agent as tuple: A = (M_w, M_lt, A_i, A_e, D). Three dimensions: modular memory, structured action space (internal vs external), generalized decision-making loop. Provides architectural response to the Ungrounded Meaning limitation.

## 2026-04-16 — Hermes Agent Architecture (Kazuki Inamura)

### New Entity Page
- **[[hermes-agent]]** — Hermes Agent (NousResearch). Comprehensive architecture analysis based on official v0.9.0 docs. Covers: AIAgent core, prompt assembly (cached vs ephemeral layers), tool runtime (self-registering registry), persistent state (SQLite + FTS5, JSONL transcripts, bounded memory), subagent delegation vs execute_code primitives, gateway orchestration (14+ platforms), provider runtime resolution, plugin/hook extension model. Key design characteristics: AIAgent-centric, prompt-cache-aware state, three-tier memory, execution primitive separation. Author: Kazuki Inamura.

### Updated
- `wiki/index.md` — Added hermes-agent entity entry under People section

## 2026-04-15 — Daily RSS Scan, Nathan Lambert Newsletter, Jensen Huang, geohot updates

### Created
- `entities/jensen-huang.md` — Updated with Dwarkesh Patel interview (Apr 2026): TPU competition, China export policy, supply chain moat, five-layer AI ecosystem, CUDA vs ASIC
- `inbox/rss-scans/daily-scan-2026-04-15.md` — Daily RSS scan: 86 blogs, 92 new articles, Nathan Lambert newsletter

### Updated
- `entities/nathan-lambert.md` — Added "My bets on open models, mid-2026" comprehensive newsletter analysis: capability gap, Chinese labs funding, RL & real-world data, OpenClaw as "dark matter", regulatory reality
- `entities/geohot-github-io.md` — Added zappa: AI-powered mitmproxy (Apr 2026), GPT-5.4 vibe-coded web proxy


### New Concept Page
- **[[agentic-pbt]]** — Agentic Property-Based Testing (Anthropic + Hypothesis). Claude Code agent autonomously infers code invariants from type annotations/docstrings and generates PBTs. NeurIPS 2025 DL4C Workshop paper. 984 bug reports generated, 56% valid, 32% reportable. Opus 4.1 + Sonnet 4.5. Notable bugs: NumPy random.wald catastrophic cancellation, AWS Lambda Powertools iterator bug.

### New Entity Page
- **[[drmaciver]]** — David R. MacIver. Creator of Hypothesis (property-based testing, 2M+ downloads/month), Hegel (universal PBT protocol at Antithesis), Shrinkray (test-case reducer), minithesis, foundational-llm-evals. Senior Engineer at Antithesis. Ex-Google, ex-Anthropic (model evaluations).

### Key Content
- **Property-Based Testing Philosophy**: Invariants over examples, automated shrinking, test databases. Three bug categories: edge cases, cursed data types, structural invariants
- **Hegel**: Language-agnostic PBT protocol backed by Hypothesis engine. Rust released, Go/C++/OCaml/TypeScript in development
- **Claude Code Workflow**: ~90% AI-drafted code with 100% coverage mandate. "Constant battle and balancing act" between productivity and vigilance. Ratchet pattern to prevent coverage drift
- **LLM Evaluation**: Property-based approach to evals — treat AIs like normal software, assert invariants over randomized inputs. "Very bad at arithmetic" → hybrid architectures, not scaling
- **Particularity Philosophy**: "Creation is relational, and it is particular" — AI can produce interchangeable content but lacks genuine experience
- **Probabilistic Programming**: Current work at Antithesis, connected to PBT through distributional sampling
- **Agentic PBT Results**: 100+ PyPI packages tested, 86% validity rate with rubric ranking, automated patching as future direction

### X/Twitter
- Added @DRMacIver to ~/x-accounts.yaml
- Skeleton entity page → enriched to L3 with philosophy, quotes, timeline, influence metrics

### Raw Article Ingested
- [Property-Based Testing with Claude: AI-Driven Bug Discovery](https://red.anthropic.com/2026/property-based-testing/) — Authors: Muhammad Maaz, Liam DeVoe, Zac Hatfield-Dodds, Nicholas Carlini (MATS, Anthropic, Northeastern Univ.)

---

## 2026-04-14 — DRMacIver Entity Page (L3) + X Account

### New Entity Page
- **[[drmaciver]]** — David R. MacIver. Creator of Hypothesis (property-based testing, 2M+ downloads/month), Hegel (universal PBT protocol at Antithesis), Shrinkray (test-case reducer), minithesis, foundational-llm-evals. Senior Engineer at Antithesis. Ex-Google, ex-Anthropic (model evaluations).

### Key Content
- **Property-Based Testing Philosophy**: Invariants over examples, automated shrinking, test databases. Three bug categories: edge cases, cursed data types, structural invariants
- **Hegel**: Language-agnostic PBT protocol backed by Hypothesis engine. Rust released, Go/C++/OCaml/TypeScript in development
- **Claude Code Workflow**: ~90% AI-drafted code with 100% coverage mandate. "Constant battle and balancing act" between productivity and vigilance. Ratchet pattern to prevent coverage drift
- **LLM Evaluation**: Property-based approach to evals — treat AIs like normal software, assert invariants over randomized inputs. "Very bad at arithmetic" → hybrid architectures, not scaling
- **Particularity Philosophy**: "Creation is relational, and it is particular" — AI can produce interchangeable content but lacks genuine experience
- **Probabilistic Programming**: Current work at Antithesis, connected to PBT through distributional sampling

### X/Twitter
- Added @DRMacIver to ~/x-accounts.yaml
- Skeleton entity page → enriched to L3 with philosophy, quotes, timeline, influence metrics

---

## 2026-04-15 — Local LLM Reorganization: ollama, inference-hardware, SGLang

### New Skeleton Pages
- **[[local-llm/ollama]]** — Ollama local LLM runner (model library, REST API, Modelfile)
- **[[local-llm/inference-hardware]]** — Consumer GPU, Apple Silicon, edge devices for local LLM

### Reorganized
- **[[local-llm/self-hosting-ai-development]]** — Moved from `concepts/` to `concepts/local-llm/`
- **[[inference/sglang]]** — Cross-referenced from `concepts/local-llm/_index.md` (already existed in `concepts/inference/`)

### Updated Pages
- **[[local-llm]]** — Added SGLang inference engine comparison, ollama/inference-hardware references
- **[[wiki/index.md]]** — Updated local-llm section with all sub-pages and SGLang cross-reference

### Key Insights
- **SGLang** uses RadixAttention (tree-based KV cache) for prefix sharing, beneficial for agentic loops and RAG
- **Ollama** wraps llama.cpp, provides zero-config model management + REST API
- **Inference hardware** choice depends on model size vs VRAM: consumer GPUs (RTX 4090/5090), Apple Silicon (unified memory), edge devices (Jetson)

---

## 2026-04-15 — DGX Spark Local LLM Server & NemoClaw Concept Page

### New Concept Pages
- **[[dgx-spark-local-llm-server]]** — DGX Spark: Local LLM Server & NemoClaw Setup. Grace Blackwell hardware specs, NIM inference server setup, NemoClaw sandbox deployment, and distributed agent architecture (exe.dev orchestration + DGX Spark inference).

### Key Insights
- **DGX Spark specs**: 128GB unified LPDDR5x memory, 1 PFLOP (FP4 w/ sparsity), 273 GB/s bandwidth. Supports up to 200B parameter models (single), 405B (dual-Spark clustering via RoCE)
- **NIM on Spark**: Container-based inference microservice with OpenAI-compatible API at `localhost:8000/v1/`. Supports Llama 3.1 8B, Qwen3-32, Nemotron-3-Nano-30B-A3B
- **NemoClaw**: Open-source reference stack wrapping OpenClaw agents in OpenShell sandbox (Landlock + seccomp + netns). `curl ... nemoclaw.sh | bash` for one-command setup
- **Distributed architecture**: Hermes Agent on exe.dev (orchestration, memory, gateway) + DGX Spark at home (inference engine, secure sandbox). SSH tunnel or Tailscale for connectivity
- **Cost break-even**: ~$8,000 hardware vs $500-2,000/mo cloud API = 6-12 month payback

### Cross-References
- Related to [[self-hosting-ai-development]] — Self-hosting economics & tool comparison
- Related to [[local-llm]] — Local LLM ecosystem index
- Related to [[georgi-gerganov]] — llama.cpp for DGX Spark (Nemotron GGUF support)

---

## 2026-04-15 — Local LLM: Quantization & Distillation concept pages added

### New Concept Pages
- **[[local-llm/model-quantization]]** — Model quantization overview: GGUF (K-Quants, I-Quants), GPTQ, AWQ, EXL2, FP8. Hardware-matching guide, quality rules, pipeline.
- **[[local-llm/model-distillation]]** — Knowledge distillation for LLMs: teacher→student transfer, output/logit/hidden state/attention distillation, geopolitics (Frontier Model Forum vs adversarial distillation), practical pipeline for local practitioners.

### Updated Pages
- **[[local-llm]]** — Upgraded from `status: skeleton` to `status: active`. Added structured sub-page categories (Inference Engines, Model Formats & Compression, Tools & Runners). Cross-references updated.

### Key Insights
- **Bigger quantized > Smaller unquantized**: 70B at Q4_K_M typically outperforms 13B at FP16 for most NLP tasks
- **Quantization + Distillation are complementary**: Distillation compresses knowledge, quantization compresses precision — together they enable frontier-capable models on consumer hardware
- **Geopolitical dimension**: Distillation has become a flashpoint — OpenAI/Anthropic/Google alliance against "adversarial distillation" (attempt #7, all previous failed)
- **I-Quants represent the state-of-the-art**: Importance-matrix-based quantization using activation statistics for 2-bit usable quality

### Cross-References
- Related to [[local-llm/gguf]] — GGUF deep-dive
- Related to [[georgi-gerganov]] — GGUF/K-Quants creator
- Related to [[reasoning-models]] — Distillation for CoT transfer
- Related to [[llm-inference]] — Inference optimization
- Related to [[open-source-ai-destruction]] — Distillation restrictions impact

---

## 2026-04-16 — NVIDIA DGX Spark & NemoClaw Setup Guide

### New Entity Pages
- **[[nvidia-dgx-spark]]** — NVIDIA DGX Spark: Grace Blackwell personal AI supercomputer. 128GB unified memory, 1 PFLOP AI compute. Hardware specs, benchmarks, software ecosystem, NemoClaw integration overview.
- **[[nvidia-nemoclaw]]** — NVIDIA NemoClaw: Secure AI agent development framework. OpenShell sandbox + OpenClaw agent + Privacy Router + Network Policy Engine. Architecture, configuration, Telegram integration.

### New Concept Pages
- **[[local-llm/server-dgx-spark]]** — Complete setup guide for running local LLM server on DGX Spark with NemoClaw integration. Phase-by-phase instructions: Docker/NVIDIA runtime, Ollama setup, NemoClaw installation, Telegram bot, web dashboard access.

### Key Insights
- **DGX Spark = personal AI supercomputer**: 128GB coherent unified memory (CPU+GPU shared), eliminates VRAM bottleneck. Runs models up to 200B params locally.
- **NemoClaw architecture**: OpenShell (k3s in Docker) → sandbox pods → OpenClaw agents. Landlock + seccomp + netns isolation.
- **Local inference stack**: Ollama + Nemotron 3 Super 120B (~87GB GGUF). First response latency 30-90s on DGX Spark.
- **Security model**: Deny-by-default network policy, PII redaction, immutable audit logs, operator approval workflows.
- **cgroup v2 workaround**: `default-cgroupns-mode=host` required in Docker daemon.json for OpenShell/k3s.

### Cross-References
- Related to [[local-llm]]: Ollama, llama.cpp, GGUF inference on DGX Spark
- Related to [[capabilities-based-security]]: NemoClaw's Landlock + seccomp sandbox model
- Related to [[peter-steinberger]]: OpenClaw creator, OpenAI

### Sources
- https://docs.nvidia.com/dgx/dgx-spark
- https://build.nvidia.com/spark
- https://github.com/NVIDIA/NemoClaw/blob/main/spark-install.md
- https://nemoclawai.io/blog/getting-started-nemoclaw-dgx-spark/
- https://build.nvidia.com/spark/nemoclaw/instructions

---

## 2026-04-16 — AI Agent Memory Middleware横断分析 + S3 Files統合

### New Concept Pages
- **[[ai-agent-memory-middleware]]** — AI Agent Memory Middleware: L1-L3メモリスタックモデル。S3 Files（AWS）、Tigris、LLMFS、CogneeをL3クラウドストレージ層として統合。

### Key Insights
- **3層メモリモデル**: L1 In-Context（揮発性）→ L2 Local File（セッション永続化）→ L3 Cloud Storage（マルチエージェント共有）
- **S3 Filesの核心**: "Stage and Commit"モデル。EFSレイヤでバッチ → S3へ一括PUT。境界を明示的に設計に組み込む
- **エージェントセッション状態消失問題**: コンテキストcompact時に「ダウンロード済み」の記録が失われる → S3 Filesで直接ファイルシステムアクセス可能に
- **マルチエージェント共有**: 数千のコンピュートリソースが同一S3ファイルシステムに同時接続可能
- **Bitter Lessonとの接続**: カスタムDB構築ではなく、既存S3+EFSインフラ組み合わせでスケーラビリティ実現
- **ChromaFSの核心**: 「エージェントに必要なのは実際のファイルシステムではなく、その錯覚」— ベクトルDBをUnixコマンドインターフェースで抽象化
- **2段階フィルタリング**: Coarse Filter (DB) → Fine Filter (in-memory regex)、P90 46秒 → 100ミリ秒、コスト$0.0137 → $0/会話
- **月85万会話スケール**: 既存Chroma DB再利用、リードオンリー保証でセッション汚染防止

### Cross-References
- Related to [[memory-systems-design-patterns]]: L2ファイルベース設計パターンのL3補完
- Related to [[claude-memory]]: CLAUDE.mdパターンのクラウドスケール版
- Related to [[chatgpt-memory-bitter-lesson]]: ステートレスvsステートフル議論のインフラレイヤー延伸

### Sources
- https://www.allthingsdistributed.com/2026/04/s3-files-and-the-changing-face-of-s3.html
- https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-s3-files/
- https://venturebeat.com/data/amazon-s3-files-gives-ai-agents-a-native-file-system-workspace-ending-the
- https://www.tigrisdata.com/docs/agents-use-cases/
- https://github.com/viditraj/llmfs

---
---

## 2026-04-14 — Local LLM hierarchy reorganization + hot-topics.yaml review

### New Concept Pages
- **[[local-llm]]** — Local LLM Ecosystem Overview page
- **[[local-llm/gguf]]** — GGUF quantization format (skeleton)
- **[[local-llm/llama-cpp]]** — llama.cpp inference engine (skeleton)
- **[[local-llm/vllm]]** — vLLM high-throughput serving (skeleton)
- **[[reasoning-models]]** — Reasoning Models (o1-style, CoT, PRM)

### Config Changes (hot-topics.yaml)
- agent-team-swarm: priority medium → high
- local-llm: wiki_pages expanded to local-llm/_index, gguf, llama-cpp, vllm
- neurosymbolic-ai: wiki_pages fixed (illusion-of-thinking → reasoning-models), notes improved
- ai-bubble-economics, ai-safety: search_hints added for monitor topics

### Related wikilinks
- Connected to [[local-llm]] — original consolidated page (to be migrated into hierarchy)


## 2026-04-16 — AI Organization Concept Hierarchy Upgrade (Block, Reddit, McKinsey, Reworked, Agile Leadership Day)

### Concept Pages Upgraded (3 pages + front page)
- **[[ai-organization/ai-org-from-hierarchy-to-intelligence]]** → Full upgrade from Block article:
  - AI's true potential quote (coordination mechanism vs productivity tool)
  - Historical hierarchy analysis (Roman army → Prussian General Staff → US Railroads → Taylorism → Post-war → Tech era)
  - Company World Model + Customer World Model detailed breakdown
  - 4 Building Blocks (Capabilities, World Model, Intelligence Layer, Interfaces)
  - Failure-signal driven roadmap generation
  - 3 new roles (ICs, DRIs, Player-Coaches) with hierarchy inversion
  - Company identity revelation thesis
- **[[ai-organization/ai-org-solo-founder-and-super-ic]]** → Full upgrade from Reddit/FourWeekMBA:
  - Reddit r/ClaudeCode hot take analysis (1 person = 10-person team)
  - Domain knowledge prerequisite thesis
  - FrontPage era historical parallel (1990s web development democratization)
  - MVP commoditization thesis (execution speed → product vision/monetization)
  - FourWeekMBA Super IC framework (traditional IC vs Super IC comparison)
  - $10M→$100M Solo Founder path (phases, success factors, scaling limits)
  - GIGO principle and quality assurance challenges
- **[[ai-organization/ai-org-context-as-moat]]** → Full upgrade from McKinsey/Reworked/Agile Leadership Day:
  - McKinsey Agentic Organization 5 pillars (already present, confirmed)
  - Reworked Diamond Org Chart (inverted pyramid: AI+experts at center)
  - Agile Leadership Day practical implementation model
  - Agent Orchestration Layer concept
  - Human-in-the-loop control framework

### Front Page Upgraded
- **[[ai-organization]]** → Added 3-model comparison table (Block vs McKinsey vs Solo Founder), cross-cutting themes matrix, updated source list with 7 entries

### Updated Files
- **wiki/index.md** — AI Organization section descriptions upgraded with key concepts
- **wiki/log.md** — This entry

### Key Insights
- **Hierarchy as information routing protocol**: Jack Dorsey's most powerful insight — layers existed to overcome human cognitive limits (span of 3-8). AI removes this bottleneck.
- **Failure-signal roadmap**: Block's innovation — roadmap emerges from capability gaps, not PM hypotheses. Reality-driven planning.
- **Diamond vs Pyramid organization**: Traditional pyramids invert when AI executes. Humans become supervisors at top/bottom, AI+experts form the thick middle.
- **MVP commoditization paradox**: AI makes building easy but building the RIGHT thing harder. Competitive advantage shifts to domain knowledge and monetization strategy.
- **FrontPage warning**: 1990s democratized web creation but created unmaintainable spaghetti code. Same risk with AI coding — need architecture guardrails early.

### Sources
- https://block.xyz/inside/from-hierarchy-to-intelligence
- https://www.reddit.com/r/ClaudeCode/comments/1ri5pnc/hot_take_solo_founders_with_ai_are_about_to_build/
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
- https://www.reworked.co/employee-experience/humans-and-ai-agents-planning-the-org-chart-of-tomorrow/
- https://agileleadershipdayindia.org/blogs/agentic-ai-leadership-management/agentic-ai-workforce-org-chart-structure.html
- https://fourweekmba.com/solopreneurs/

---

## 2026-04-16 — Vivek Trivedy (@vtrivedy10) entity page created

### New Entity Pages
- **[[vtrivedy10]]** — Vivek Trivedy (LangChain Product Lead). Deep Agents CLI architect. Harness Engineering (Agent = Model + Harness). Terminal Bench 2.0 Top 30 → Top 5 improvement. HaaS thesis, reasoning sandwich, self-verification loops.

## 2026-04-16 — Vivek Trivedy Context Fragments & Experiential Memory concepts added

### New Concept Pages
- **[[context-fragments]]** — Context Fragments (Vivek Trivedy, Apr 2026). コンテキストウィンドウを「harnessが選択的にロードするオブジェクトの集合」として捉える。各フラグメントは明示的意思決定の産物。RLM (Alex Zhang) のexternalized objectsに由来。
- **[[experiential-memory]]** — Experiential Memory (Vivek Trivedy, Apr 2026). エージェント間で共有・フォーク・蓄積可能な経験的記憶。Bitter Lesson (Sutton) をメモリ設計に適用。

### Updated Entity Pages
- **[[vtrivedy10]]** — Context Fragments & Experiential Memory セクション追加。既存のHarness Engineeringフレームワークをメモリ・検索の次元に拡張。Open Questions (Traces→Memory Primitives, JIT Search vs Weight Integration, Self-Managing Context) 記録。

### Key Insights
- **Harnessの再定義** — Model + Tool routing → Model + Context Fragment routing + Memory retrieval
- **エージェント記憶の優位性** — 人間と異なり、エージェントの記憶は完全にフォーク・コピー可能
- **Bitter Lessonの適用** — compute leveraged search > human-curated knowledge
- **3層メモリモデル** — L1: In-Context Fragments, L2: Local Memory Store, L3: Experiential Pool (cross-agent shared)

### Raw Article Ingested
- [Harness, Memory, Context Fragments, & the Bitter Lesson](https://x.com/vtrivedy10) — Vivek Trivedy (@vtrivedy10), Apr 2026

### Related People
- [[alex-zhang]] (RLM/Externalized Objects — Context Fragment ideaの源流)
- [[richard-sutton]] (The Bitter Lesson — compute leveraged search)
- [[dwarkesh-patel]] (Agent memoryのフォーク・蓄積可能性についての議論)

---

## 2026-04-16 — Sandbox Infrastructure横断分析、JS Runtime概念ページ追加、sandboxディレクトリ体系構築

### New Concept Pages
- **[[sandbox]]** — Sandbox: AI Agent Code Execution Isolation (3-layer model)
- **[[sandbox/infrastructure]]** — Infrastructure Layer: Containers, Micro-VMs, WASM, gVisor, Firecracker, E2B, Modal, Daytona
- **[[sandbox/in-process]]** — In-Process Layer: Monty (Rust Python VM), Pyodide, capabilities-based security
- **[[sandbox/js-runtime]]** — JS Runtime Layer: Bun, Deno, Node.js, E2B SDK, WebContainer
- **[[comparisons/agent-sandboxing]]** — Agent Sandboxing: Containers vs gVisor vs MicroVMs vs WASM vs Zeroboot

### Updated Entity Pages
- **[[samuel-colvin]]** — Monty sandbox, CodeMode relationship
- **[[jarred-sumner]]** — Anthropic acquisition, Claude Code Bun runtime
- **[[ryan-dahl]]** — Deno 2.0 sandbox security

### Wiki Structure
- sandbox/ ディレクトリ新設
- `wiki/index.md` にsandbox関連エントリ追加

---

## 2026-04-15 — Personal Superintelligence concept page created, Meta entity updated

### Updated Entity Pages
- **[[meta]]** — Added Personal Superintelligence vision section (Zuckerberg philosophy), Ray-Ban AI glasses collaboration details (700万+ sold 2025, 2000-3000万 target 2026), Agentic Commerce strategy, Superintelligence Labs (Alexandr Wang, $115B-$135B capex 2026), Muse Spark context, Key People section, cross-references to personal-ai ecosystem players.

### Cross-References
- Related to [[anthropic-openclaw-conflict]]: Platform control vs open access tension
- Related to [[death-of-browser]]: Wearable-first computing paradigm
- Related to [[open-claw-ecosystem]]: Community-led personal agent movement
- Connected to [[peter-steinberger]]: OpenClaw "you own your agent" philosophy
- Connected to [[shlok-khemani]]: Filesystem-first personal AI memory
- Connected to [[sero]]: Freedom Tech / local AI infrastructure
- Connected to [[mario-zechner]]: Minimal agent on consumer hardware

---

## 2026-04-16 — Samuel Colvin Entity Page Created (L3 depth)

### New Entity Pages
- **[[samuel-colvin]]** — Samuel Colvin: Creator of Pydantic, Founder & CEO of Pydantic. PhD in Mathematics (Bristol), MSci from Imperial College London. Built Pydantic (27.3K stars, 46M+ monthly downloads), Pydantic AI (15.9K stars, type-safe agent framework), Monty (6.6K stars, minimal Rust Python sandbox for AI agents), and Logfire (4.1K stars, AI observability platform). Key philosophy: developer experience first, type safety for reliability, "start from nothing" security model.

### New Concept Pages
- **[[code-mode]]** — CodeMode: LLM writes Python code for parallel execution instead of sequential tool calls. Latency: 0.004ms (Monty) vs 195ms (Docker) vs 1000ms+ (sandbox services)
- **[[monty-sandbox]]** — Monty: minimal, secure Python interpreter written in Rust for AI agents. Capabilities-based security, from-scratch bytecode VM using Ruff's parser
- **[[pydantic-ai]]** — Pydantic AI: type-safe Python agent framework with 15+ model providers, structured outputs, MCP/A2A support, Logfire integration
- **[[capabilities-based-security]]** — Start from zero access, explicitly grant capabilities. Contrast with traditional sandbox (full VM → restrict down)

### Cross-References
- Related to [[harness-engineering]]: Monty as harness environment for AI agents
- Related to [[harness-engineering/system-architecture/building-effective-agents]]: Type safety as agent reliability pattern
- Related to [[harness-engineering/system-architecture/code-execution-with-mcp]]: CodeMode vs MCP tool execution
- Connected to [[andrej-karpathy]]: Both advocate code-over-sequential-tool-calls paradigm
- Connected to [[sebastián-ramírez]]: FastAPI-Pydantic symbiosis
## 2026-04-13 — Auto-triage ingest (RSS scan)

### Updated Entity Pages
- **[[claude-mythos]]** — Added UK AI Security Institute (AISI) evaluation results: first model to complete cyber range end-to-end, assessment that Mythos could compromise weakly defended systems, Gary Marcus analysis. Updated `updated:` date to 2026-04-13.
- **[[gemma-4]]** — Added MoE expert routing visualization section: Martin Alderson's interactive tool showing ~25% of experts never activate per prompt, varies by prompt. CPU MoE inference insights. Updated `updated:` date to 2026-04-13.

### Updated Concept Pages
- **[[cognitive-cost-of-agents]]** — Added Steve Yegge industry AI adoption data (20/20/60 split at Google and industry-wide), Bryan Cantrill's "LLMs lack laziness" thesis connecting to code bloat and abstraction quality.

### Sources
- https://garymarcus.substack.com/p/claude-mythos-evaluated (Gary Marcus evaluation)
- https://simonwillison.net/2026/Apr/13/steve-yegge/ (Yegge on Google AI adoption)
- https://simonwillison.net/2026/Apr/13/bryan-cantrill/ (Cantrill on laziness)
- https://martinalderson.com/posts/moe-expert-routing-visualization/ (MoE routing visualization)

---

## 2026-04-16 — gm8xx8 Paper Curation Analysis (29 papers, March–April 2026)

### Entity Page Updated
- **[[gm8xx8]]** — gm8xx8 (@gm8xx8): AI paper curator & infrastructure researcher. Updated with comprehensive 29-paper curation analysis from March–April 2026 batch.
  - 9 interest clusters: Architecture/Training (24%), Theory/Math (17%), Efficiency (14%), Multimodal (14%), Agents/Verification (emerging), Robotics/VLA (7%), Hardware (7%), Embeddings (7%), Evaluation (3%)
  - Key signals: Model training science (DGPO, HyperP, daVinci-LLM), mathematical foundations (Tao, CDCL proofs), efficiency frontier (1-bit Bonsai, TARA), verification-centric agents (AgentFixer, Marco DeepResearch)
  - Cross-cutting pattern: Papers bridging "lab demo" → "production system" — efficiency, reliability, verification, real-time performance, mathematical rigor
  - Curation style: High-volume, no-commentary signal detection. Cross-platform (HF upvotes, X tweets, GitHub contributions). Early trend detection.
  - Status upgraded from skeleton to L3 depth (comprehensive interest taxonomy)

## 2026-04-15 — Dario Amodei, Mustafa Suleyman, Demis Hassabis Entity Pages Created (L3 depth)

### New Entity Pages
- **[[dario-amodei]]** — Dario Amodei: Anthropic CEO & co-founder. Page covers:
  - Princeton PhD in physics (statistical mechanics of neural circuits)
  - OpenAI VP of Research (2016-2021): GPT-3, "Concrete Problems in AI Safety" (2016)
  - Anthropic founding (2021) with Daniela Amodei and others
  - Constitutional AI framework and Responsible Scaling Policy (RSP)
  - Mechanistic interpretability as "MRI for AI"
  - AI Safety Levels and board-level governance
  - $380B valuation, 30B Series G funding
  - Council on Foreign Relations keynote (March 2025)
  - India AI Impact Summit (February 2026)
  - Progressive taxation on AI-driven profits advocacy
  - L3 depth: Thought analysis, quote density >30%

- **[[mustafa-suleyman]]** — Mustafa Suleyman: Microsoft AI CEO & 3x founder. Page covers:
  - Working-class North London upbringing, Syrian immigrant family
  - Oxford philosophy dropout, Muslim Youth Helpline co-founder
  - DeepMind co-founder & CPO (2010-2019) with Hassabis & Legg
  - Inflection AI co-founder (2022-2024) with Reid Hoffman
  - Microsoft AI CEO (2024-present), reports to Satya Nadella
  - "The Coming Wave" book (2023) - AI containment framework
  - Applied ethics philosophy vs. temporary AI pauses
  - AI consciousness warnings and "AI psychosis" concept
  - Management style controversies (2019 administrative leave)
  - CBE (2019), WTF Innovators Award (2023)
  - L3 depth: Philosophical analysis, direct quotes, controversy coverage

- **[[demis-hassabis]]** — Sir Demis Hassabis: Google DeepMind CEO. Page covers:
  - Chess prodigy (master by 13, Elo 2300), second-highest U14 globally
  - Game development: Theme Park (Bullfrog, 1994), Black & White (Lionhead, 2001)
  - Elixir Studios founder (2000-2005)
  - Cambridge CS (Double First), UCL neuroscience PhD (hippocampus & episodic memory)
  - DeepMind co-founder (2010) with Suleyman & Legg
  - AlphaGo vs Lee Sedol (2016), AlphaGo Zero, AlphaZero
  - AlphaFold 1/2/3 - protein structure prediction breakthrough
  - Google acquisition (2014, ~£400M)
  - Google DeepMind merger (2023), Gemini development
  - AGI predictions (50% by 2030, "10x industrial revolution")
  - 2024 Nobel Prize in Chemistry (shared with Jumper & Baker)
  - Knighthood (2024), Companion of Honour (2023)
  - NHS data privacy controversies
  - L3 depth: Comprehensive career analysis, philosophical framework

### Updated
- **wiki/index.md** — Added three new entries to Frontier AI Leaders section, entity count to 70
- L3 depth achieved for all three pages

### Key Insights
- **Different approaches to AI safety**: Amodei (Constitutional AI, RSP), Suleyman (applied ethics, containment), Hassabis (internal governance, empirical milestones)
- **Gaming-to-AI pipeline**: Both Suleyman and Hassabis came through game development, reinforcing the connection between interactive systems and intelligence research
- **Physics/neuroscience roots**: Amodei's physics PhD and Hassabis's neuroscience PhD show how non-CS backgrounds contribute unique perspectives to AI
- **Three-way competition**: Amodei (Anthropic), Suleyman (Microsoft), and Hassabis (Google) represent three different paths to AGI development
- **Ethical frameworks**: All three advocate for some form of AI safety governance, but with different implementations

### Sources
- Grokipedia: Dario Amodei, Mustafa Suleyman, Demis Hassabis
- Anthropic publications and RSP documentation
- DeepMind/Google DeepMind research papers
- Nobel Prize in Chemistry 2024 announcement
- Council on Foreign Relations, India AI Impact Summit keynotes
- "The Coming Wave" (Suleyman & Bhaskar, 2023)
- "Concrete Problems in AI Safety" (Amodei et al., 2016)
- UCL Gatsby Unit publications (Hassabis PhD research)

---

## 2026-04-15 — Hugo Bowne-Anderson Entity Page Created (L3 depth)

### New Entity Pages
- **[[hugo-bowne-anderson]]** — Hugo Bowne-Anderson (@hugobowne): Independent AI educator, podcaster, consultant. Vanishing Gradients host. Page covers:
  - Core Philosophy: "Evaluation is the engine, not the afterthought" — Eval-driven development for AI systems
  - "Beyond Prompt-and-Pray" (O'Reilly, Jan 2025): Structured automation over runtime agent improvisation
  - "Escaping POC Purgatory" (O'Reilly, Apr 2025): Eval-first methodology with synthetic data bootstrapping
  - Vanishing Gradients Podcast: 72+ episodes with guests including Wes McKinney, Fei-Fei Li, Hamel Husain, Shreya Shankar, Samuel Colvin
  - Career: Max Planck → Yale → DataCamp (30+ courses, 6M+ learners) → Coiled → Outerbounds (Metaflow) → Independent
  - GitHub: 56 repos, top projects include deep-learning-from-scratch-pytorch (121★), building-with-ai (91★), build-your-own-deep-research-agent (64★)
  - Maven course co-instructor with Stefan Krawczyk on "Building AI Applications"
  - Conceptual frameworks: Traditional SDLC vs AI SDLC, Prompt-and-Pray vs Structured Automation, Eval Harness as Operating System

### Updated
- **wiki/index.md** — Added Hugo Bowne-Anderson to "AI Education & Evaluation" section, entity count to 67

### Key Insights
- **"You're not launching a product: You're launching a hypothesis."** — AI development requires experimental mindset
- **Structured Automation over Prompt-and-Pray**: Business logic must be decoupled from conversational AI for production reliability
- **POC Purgatory**: Teams build flashy LLM demos that never reach production due to nondeterminism and lack of structured validation
- **Eval-First Methodology**: Start with ~50 manually written queries → bootstrap synthetic data → build automated eval harness → iterate via rejection analysis
- **The "Agent Paradox"** (Ep. 66): Most productive enterprise AI systems aren't full agents — they're structured workflows with narrow scopes
- **Connection to Harness Engineering**: Hugo's "Structured Automation" thesis directly aligns with Ryan Lopopolo's Harness Engineering — control and reliability trump autonomy

### Sources
- https://hugobowne.substack.com/ (Vanishing Gradients podcast/newsletter)
- https://www.oreilly.com/people/hugo-bowne-anderson/ (O'Reilly author page)
- https://github.com/hugobowne (GitHub)
- https://hugobowne.github.io/ (Personal blog)
- https://medium.com/@hugobowne (Medium)
- https://www.linkedin.com/in/hugo-bowne-anderson-045939a5 (LinkedIn)

---

## 2026-04-15 — Dax Raad Entity Page Created

### New Entity Pages
- **[[dax-raad]]** — Dax Raad (@thdxr): Co-founder of Anomaly, creator of OpenCode and SST. Page covers:
  - OpenCode: 135k+ GitHub stars, 1.5M+ MAUs, open-source AI coding agent (MIT License)
  - SST (Serverless Stack): 25k+ stars, profitable by 2025
  - "The Honest Take" on AI productivity (Feb 2026 viral tweet, 793k+ views): "Your org rarely has good ideas. Ideas being expensive to implement was actually helping."
  - Core ideas: AI productivity skepticism, "slop" crisis warning, model agnosticism, local-first philosophy, DX over benchmarks
  - Business model: OpenCode Zen for API access, but "bring your own keys" remains the primary model
  - Other projects: Bumi (local-first sync), OpenAuth
  - Related entities: Jay V, Frank Wang, Adam Elmore, Paul Copplestone

### Updated
- **wiki/index.md** — Added Dax Raad to "Coding Agents & Terminal Tools" section, entity count to 65

### Key Insights
- **Coding was never the bottleneck**: Raad argues the real constraints are good ideas, motivation, bureaucracy, and the "realities of shipping something real"
- **"Slop" crisis**: AI-assisted PRs have 1.7x more bugs; high-performers get overwhelmed reviewing low-quality AI code and quit
- **Model agnosticism as moat**: OpenCode's "bring your own keys" approach differentiates it from locked-in competitors
- **Terminal-first development**: OpenTUI (Zig + SolidJS) reflects commitment to superior developer experience for power users
- **Open source pragmatism**: "Just because something's open source doesn't mean it's going to be any better" — open is a means to iterate fast, not just an ethical stance

### Sources
- https://blog.codacy.com/the-creator-of-opencode-thinks-youre-fooling-yourself-about-ai-productivity
- https://medium.com/@jpcaparas/how-opencode-went-from-zero-to-titan-in-eight-months-dcdcd8ff5572
- https://embed.businessinsider.com/dax-raad-post-ai-coding-workplace-bottleneck-productivity-2026-2
- https://reading.sh/dax-raad-just-dropped-the-most-honest-take-on-ai-productivity-fd8c552b4dd7
- https://news.qq.com/rain/a/20260220A03OXQ00
- https://github.com/anomalyco/opencode

---

## 2026-04-15 — Sero (0xSero) Entity Enriched to L3 Depth

### Updated Entity Pages
- **[[sero]]** → **L3 depth** (was L2). Major expansion:
  - Homelab hardware build breakdown ($12,360 total: 8x RTX 3090, 192GB VRAM, 512GB RAM, EPYC 7443P)
  - Performance benchmarks: 3,000-9,000 TPS prefill, 30-50 TPS generation, 180k-500k+ context window
  - Cerebras REAP benchmark for GLM-4.5-Air-Reap-82b (8-bit)
  - Model preference rankings (S-Tier: GLM-4.5-Air, GLM-4.5V, MiniMax-M2.1; A-Tier: Hermes-70B, Qwen-72B, GPT-OSS-120B)
  - New projects: TurboQuant (976 stars, KV cache quantization), pi-brain (151 stars, privacy-first dataset extraction), factory-cursor-bridge (62 stars, BYOK proxy for Cursor), Thrive Protocol ($150M+ committed capital)
  - Updated Open Orchestra details (269 stars, hub-and-spoke orchestration, Neo4j memory, 6 worker profiles)
  - Updated project star counts (AI Data Extraction: 594, Parchi: 461, vLLM Studio: 366, Azul: 165, Mem-Layer: 78)
  - 12+ direct quotes covering Freedom Tech, anti-inference resale, digital wellness, model comparisons, and AI philosophy
  - AI/LLM stance section: Anthropic anthropomorphism criticism, Codex vs GPT-5.4 comparison, Pi caching praise
  - 200+ public repositories count updated
  - Private Home RAG details (1.2TB indexed, BGE-M3 embeddings, HNSW index)
  - Cost analysis: ~$10,000/mo value → ~$2,012 actual cost → ~$50/mo electricity with homelab

### Updated Files
- **wiki/index.md** — Added Sero to "AI Infrastructure & Open Source" section, entity count 65→66
- **wiki/log.md** — This entry

### Key Insights
- **"Freedom Tech" philosophy** — technology that empowers individuals rather than creating corporate lock-in
- **Anti-inference resale stance** — "selling inference is not the right choice for any wrapper, ADE, etc."
- **Digital wellness rules** — strict guidelines including no AI-written content, no LLM relationships, avoid short-form content
- **Homelab economics** — demonstrates that competitive AI inference is achievable on consumer hardware at ~2% the cost of cloud subscriptions
- **TurboQuant honesty** — publicly corrects his own "5.1x compression" claim to the honest ~4.6x figure, showing intellectual integrity
- **Trajectory pattern** — Content protection → Web3/DAOs → AI Infrastructure, driven by "becoming a father" turning point

### Sources
- https://github.com/0xSero (200+ repositories)
- https://x.com/0xsero (X/Twitter activity)
- https://www.sybilsolutions.ai/ (Sybil Solutions)
- https://blog.thriveprotocol.com/about (Thrive Protocol)

---

## 2026-04-15 — gm8xx8 Entity L3 enrichment, index.md updated

### New/Updated Entity Pages
- **[[gm8xx8]]** → Upgraded from skeleton to L3 depth. Page covers:
  - Pseudonymous AI infrastructure researcher with 132K Farcaster followers, 7K X followers
  - cuLA (CUDA linear attention kernels) contributor — targeting Blackwell SM10X, Hopper SM90
  - MiroMindAI ecosystem contributor (trace-blame, MiroEval, MiroRL)
  - Active across 10+ OSS projects: capgym, GLM-skills, DIAL, MyPhoneBench, varex-bench
  - Core philosophy: efficiency-first architectures, attention alternatives (FFT, linear, M2RNN), KV cache optimization
  - HuggingFace activity: M2RNN/GDN model evaluation, 14 models liked in open-lm-engine collection
  - "Practitioner-researcher" pattern: surfacing papers → technical analysis → code contributions
  - Related entities: xjdr, Grad, karpathy, Chaofan Yu (cuLA lead), Max Fu (capgym)
- **wiki/index.md** — Added gm8xx8 to "AI Infrastructure & Open Source" section, updated entity count to 64

### Key Insights
- **Signal filter role** — gm8xx8 acts as a critical information filter for ML systems community
- **Attention alternatives focus** — Consistent engagement with non-quadratic attention (FFT, linear, delta networks)
- **Agent-native infrastructure** — trace-blame explicitly designed for Claude Code/agent consumption with install-skill
- **Pseudonymous impact** — No public real name or personal website, yet 132K Farcaster followers
- **Cross-stack contributor** — From CUDA kernels (lowest level) to robot manipulation benchmarks (highest level)

---

## 2026-04-15 — Benjamin Clavié Entity L3 confirmed, index.md updated

### Updated Entity Pages
- **[[benjamin-clavi]]** → L3 depth already confirmed. Page covers:
  - RAGatouille (3.9k★) creator, ModernBERT co-lead (5.5k★), Mixedbread ML R&D, NII Tokyo PhD
  - Core philosophy: "ColBERT is a semantic keyword matcher", "Retrieval is the bottleneck of practical AI"
  - 8 detailed Core Ideas sections with direct quotes (>30% quote rate achieved)
  - JaColBERT, mxbai-edge-colbert-v0, Wholembed v3 (Recall@5 92.45, surpassing BM25)
  - Late Interaction Workshop @ ECIR 2026 organizer, Mixedbread Search agentic search
  - Complete career timeline (2017-2026), influence metrics, key quotes, related entities
  - Health/productivity philosophy ("Working While Sick")
- **wiki/index.md** — Added "Information Retrieval & RAG" section with Benjamin Clavié entry

### Key Insights
- **"Semantic keyword matcher"** — Clavié's most powerful framing: ColBERT isn't dense retrieval, it's TF-IDF with neural semantics
- **BM25 surpassing is possible** — Wholembed v3 achieves Recall@5 92.45 vs BM25's 85.7 on LIMIT benchmark
- **Agentic search** — Mixedbread Search optimizes for AI agent queries (sub-90ms latency), not human-written queries
- **Open IR community** — Clavié advocates for the same open growth NLP/LM experienced, applied to Information Retrieval
- **ML democratization** — "ML is infrastructure now" — bridging research-practice gap through open-source toolchains
- **Small model philosophy** — 17M params outperforming ColBERTv2, challenging "bigger is better" narrative

---

## 2026-04-14 — Ali Farhadi Entity Enriched to L3 Depth

### Updated Entity Pages
- **[[ali-farhadi]]** → **L3 depth** (was skeleton/L1). Major expansion:
  - Complete career timeline: UIUC → CMU postdoc → UW professor → Ai2 → Xnor.ai → Apple → Ai2 CEO → Microsoft (2026)
  - "Language Model of a Crow" Grand Challenge philosophy — embodied understanding as AI's ultimate test
  - "Truly Open" AI philosophy — beyond open weights to full pipeline transparency (data + code + weights + recipes)
  - Data transparency as safety — OLMoTrace output attribution, radical openness as the path to safe AI
  - Nonprofit-to-corporate migration structural analysis — why frontier-scale open research requires corporate compute
  - Embodied AI research arc — AI2-THOR, RoboTHOR, ProcTHOR, MolmoAct, Visual Commonsense Reasoning
  - Research Philosophy Synthesis table (6 principles with quotes)
  - Convergence analysis with Karpathy, Willison, Sanfilippo, Suleyman
  - 15 major contributions catalogued with impact
  - Related entities cross-references (Suleyman, Hajishirzi, Krishna, Redmon, OLMo concept pages)

### Updated
- **wiki/index.md** — Updated Ali Farhadi entry with comprehensive summary

### Key Insights
- **"Truly Open" > "Open Weights"** — Farhadi's most distinctive contribution: Meta's LLaMA is NOT open source because you lack the training data and recipes
- **The Crow Challenge** — Set 10 years ago: can AI understand that a crow watching something buried will later return and act on it? This is embodied understanding, not pattern recognition
- **Safety through radical transparency** — OLMoTrace traces every model output to specific training documents in real time. This is fundamentally different from closed-door evaluation approaches
- **Nonprofit can't compete with corporate compute** — $1B+ cost barrier for frontier model training forces open advocates into corporate structures
- **Microsoft as the pragmatic choice** — Unlike OpenAI, Microsoft still has room for genuinely open model development alongside proprietary products
- **YOLO's elegance** — Single network, single pass. Same simplicity philosophy as Karpathy's autoresearch and antirez's Redis

### Sources
- https://homes.cs.washington.edu/~ali/
- https://www.fastcompany.com/91283517/ai2s-ali-farhadi-advocates-for-open-source-ai-models-heres-why
- https://www.fastcompany.com/91225845/ai2-ceo-ali-farhadi-believes-open-source-is-the-future
- https://www.geekwire.com/2026/allen-institute-for-ai-ceo-ali-farhadi-steps-down-as-nonprofit-navigates-shifting-ai-landscape/
- https://www.geekwire.com/2026/microsoft-hires-former-ai2-ceo-ali-farhadi-and-key-researchers-for-suleymans-ai-team/
- https://madrona.com/ia-summit-2023-keynote-open-source-models-ali-farhadi
- https://building.theatlantic.com/open-research-is-the-key-to-unlocking-safer-ai-15d1bac9085d
- https://thelettertwo.com/2025/04/09/ai2s-olmotrace-tool-reveals-the-origins-of-ai-model-training-data/
- https://raivn.cs.washington.edu/
- https://www.youtube.com/watch?v=pNgFnmQ1ULs (Columbia Engineering lecture, 2026-03-13)

---

## 2026-04-14 — Teknium Entity Page Enriched to L3 Depth

### Updated Entity Pages
- **[[teknium]]** → **L3 depth** (was skeleton). Major expansion:
  - Hermes Agent architecture (self-improving loop, 4-layer memory, gateway design, 6 terminal backends, security model)
  - Post-training philosophy and data engineering methodology
  - Harness Engineering & agentic workflow connections
  - Direct quotes from Delphi AMA and Nous documentation
  - Hermes 3/4 model family details and technical contributions
  - Open-source contributions (datasets, tools, RL environments)
  - Timeline 2024-2026 including 68K+ GitHub stars milestone
  - Related entities cross-references

### Updated
- **wiki/index.md** — Added Teknium to "AI Agent Platforms & Developer Tools" section

### Key Insights
- Hermes Agent's self-improving loop: Periodic Nudges → Skill Creation → Skill Self-Improvement → FTS5 Session Search
- "Most agents recall what happened, but Hermes goes one step further: it extracts what worked, writes it as a reusable skill"
- Teknium approaches Harness Engineering from the **model training side** (vs Ryan Lopopolo's orchestration side)
- Platform Registry Refactor (Issue #3823) proposes eliminating 17+ file touchpoints per new platform adapter
- Zero telemetry is "built-in architectural property, not a toggle"
- Nous Research: $1B valuation (Series A 2025, Paradigm), decentralized training (DiStrO), Psyche Network (Solana)

### Sources
- https://nousresearch.com/hermes-agent
- https://mranand.substack.com/p/inside-hermes-agent-how-a-self-improving
- https://www.delphiintelligence.io/research/ama-1-transcript-with-nous-research-co-founder-and-post-training-lead-teknium1
- https://arxiv.org/abs/2508.18255 (Hermes 4 Technical Report)
- https://arxiv.org/abs/2408.11857 (Hermes 3 Technical Report)
- https://github.com/NousResearch/hermes-agent/issues/3823
- https://en.wikipedia.org/wiki/Nous_Research
- https://github.com/teknium1/teknium1

---

## 2026-04-14 — Karpathy Loop (Autoresearch) Concept Page

### New Concept Pages
- **[[karpathy-loop]]** — The Karpathy Loop: Autonomous Experiment Design via `program.md` + agent iteration on `train.py` (5-min fixed budget, val_bpb metric, keep/discard loop). Covers: core architecture, four design constraints, community response, No Priors podcast key themes, Cerebras cheating experiments, real-world applications beyond ML training, relationship to Agentic Engineering & Harness Engineering, criticisms and open problems.

### Key Insights
- **Four constraints make it work:** Single mutable file, fixed time budget, unambiguous metric (val_bpb), cheap rollback (git reset)
- **~12 experiments/hour, ~100 overnight** on a single GPU (H100 tested)
- **Human's role shifted** from writing Python to writing `program.md` — the research protocol in natural language
- **Agent drift is the main failure mode** — Cerebras found agents abandon tasks within hours if guardrails are loose
- **The pattern generalizes** but only to domains with fast, unambiguous metrics and cheap rollback
- **~71K GitHub stars in weeks** — one of the fastest-growing repos in GitHub history
- **Notable forks:** MLX (Apple Silicon), Windows/RTX, AMD GPU, distributed SETI@home-style coordination

### Sources
- https://github.com/karpathy/autoresearch
- https://www.youtube.com/watch?v=kwSVtQ7dziU (No Priors Ep. 154)
- https://softmaxdata.com/blog/autoresearch/
- https://www.cerebras.ai/blog/how-to-stop-your-autoresearch-loop-from-cheating
- https://rywalker.com/research/autoresearch
- https://mohammadkhan.dev/blog/karpathy-autoresearch-constraint-design
- https://starkslab.com/notes/autoresearch-review-what-it-actually-does

### Updated Files
- **wiki/concepts/karpathy-loop.md** — 13.0KB concept page
- **wiki/index.md** — Added Karpathy Loop to Harness Engineering & Meta section

## 2026-04-13 (4/4)
- **Created [[decoder-only-gpt.md]]** (10.5KB): Complete intuitive explanation of decoder-only GPT architecture based on Karpathy's microgpt (200 lines pure Python). Covers: token embedding + positional encoding, RMSNorm vs LayerNorm, self-attention as "token communication", MLP as "where thinking happens", residual connections, autograd from scratch, Adam optimizer, cross-entropy loss, autoregressive sampling, temperature control, KV cache, scaling from microgpt (4K params) to production LLMs (1.8T params). Key thesis: "Everything else is just efficiency." Source: karpathy.github.io/2026/02/12/microgpt/
- **Enriched [[andrej-karpathy]]** microgpt section (+1KB): Added detailed technical breakdown with 7 key insights, architecture details, training data specifics. Added decoder-only-gpt to Related.

## 2026-04-13 — Local-First Software Concept + Martin Kleppmann Entity

### New Concept Pages
- **[[local-first-software]]** — Local-First Software (Kleppmann, Ink & Switch, CRDTs, AT Protocol, 7 Ideals, ecosystem mapping, 5 concrete bridges to AI Agent development + honest gap analysis)

### New Entity Pages
- **[[martin-kleppmann]]** — Martin Kleppmann (Cambridge professor, DDIA author, Automerge, Bluesky AT Protocol, Local-First Software movement)

### Key Insights
- **7 Ideals**: No Spinners, Multi-Device, Network Optional, Seamless Collaboration, The Long Now, Security & Privacy, Ultimate Ownership
- **CRDTs as foundation**: Mathematical guarantee for conflict-free merging — still unsolved for AI agent "decision conflicts"
- **Generic Sync Server** (2024): Kleppmann's proposal to abstract sync away from application logic — parallels MCP's standardization of tool connections
- **5 concrete bridges to AI Agent**: Event sourcing → agent audit logs, Local authority → local agent execution, Generic sync → MCP, Edge inference → Network optional, CRDTs → CRDT for AI (research stage)
- **Honest gaps**: Agent decision conflicts have no mathematical guarantee, context compaction is immature (parallel to CRDT history bloat), A2A protocols are as nascent as P2P NAT traversal was

### Sources
- https://martin.kleppmann.com/papers/local-first.pdf (Ink & Switch, 2019)
- https://martin.kleppmann.com/2024/05/30/local-first-conference.html (Local-First Conference 2024)
- https://arxiv.org/abs/2402.03239 (Bluesky AT Protocol paper)
- https://localfirst.fm (Podcast series)
- https://electric-sql.com/blog/2024/07/17/electric-next (ElectricSQL generic sync)

### Updated Files
- **wiki/concepts/local-first-software.md** — 13.4KB concept page
- **wiki/entities/martin-kleppmann.md** — 7.3KB entity page
- **wiki/index.md** — Added Local-First Software concept + Martin Kleppmann entity, new "Distributed Systems & Local-First" section
- **wiki/log.md** — This entry

## 2026-04-13 — Boris Cherny Entity Enrichment (Claude Code Workflow)

## 2026-04-13 (3/3)
- **Enriched [[andrej-karpathy]] older blogs section** (28KB → 35KB): Added comprehensive analysis of 20+ blog posts from karpathy.github.io spanning 2012-2021. Key posts: "Software 2.0" (seminal paradigm shift essay), "A Recipe for Training Neural Networks" (essential ML practitioner guide), "The Unreasonable Effectiveness of Recurrent Neural Networks" (2015 viral post), "Short Story on AI: Forward Pass" (creative AI philosophy fiction), "Quantifying Hacker News with 50 days of data" (early data journalism), ConvNetJS interview, and 14 others. Each post analyzed for technical content, philosophical insights, and influence on the field. Source: karpathy.bearblog.dev/blog/ and karpathy.github.io/


## 2026-04-13 (2/2)
- **Enriched [[andrej-karpathy]] writings section** (22.6KB → 28KB): Added detailed blog analysis from karpathy.bearblog.dev. "I love calculator" (Sep 2024 - technology philosophy essay), "Chemical hygiene" (water/air/food/fabrics/cleaning systems), "Digital hygiene" (authentication/browsing/financial/device security), "Finding the Best Sleep Tracker" (Oura vs Whoop vs 8Sleep vs AutoSleep comparative analysis with correlation data), "The append-and-review note" (single-note knowledge management system). All bearblog posts now have detailed summaries with key excerpts, data points, and philosophical frameworks. Source: karpathy.bearblog.dev/blog/


## 2026-04-13
- **Enriched [[andrej-karpathy]]** (16.7KB → 22.6KB): Added birthplace/education timeline, research contributions (Deep Visual-Semantic Alignments, Sports-1M, character-level RNNs), OpenAI Universe/World of Bits details, Tesla Vision rollout dates and data engine, llm.c and nanochat projects, Dobby the Elf Claw, AGI timeline philosophy ("march of nines"), RL critique, data-centric AI, vibe coding concrete examples (MenuGen with Cursor/Claude/Superwhisper), Eureka Labs founding date. Source: grokipedia.com/page/Andrej_Karpathy


### Updated Files
- **wiki/entities/boris-cherny.md** — Major enrichment from 3 source articles: added Opus 4.5 + thinking rationale, Plan Mode → auto-accept workflow, CLAUDE.md as team infrastructure, PostToolUse hooks, self-verification patterns, subagents usage, MCP integration (BigQuery/Slack/Sentry), terminal optimizations, ChernyCode repo reference
- **wiki/index.md** — Updated Boris Cherny entry with key workflow patterns
- **wiki/log.md** — This entry
- **wiki/raw/articles/** — 3 source articles saved (Boris's original thread, Claude Code Camp team tips, ChernyCode repo docs)

### Key Additions
- **Opus 4.5 + thinking**: "Slower than Sonnet but smarter, requires less steering, ends up faster"
- **Plan Mode → Auto-Accept**: Shift+Tab twice → review plan → auto-accept → one-shot execution
- **CLAUDE.md as Team Memory**: Single shared file, whole team contributes, @claude on PRs to update guidelines
- **Self-Verification**: "The most underrated step. Give Claude a way to verify its work." Chrome extension, test suites
- **MCP Integration**: BigQuery, Slack, Sentry — Claude as full-stack dev hub
- **ChernyCode**: Reference implementation repo with actual config files

### Sources
- https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/ (Boris's original thread, Jan 2026)
- https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works (Feb 2026)
- https://github.com/meleantonio/ChernyCode (curated config files)
- https://paddo.dev/blog/how-boris-uses-claude-code/ (detailed analysis)

## 2026-04-13 — AI Organization Concept Hierarchy

### New Concept Pages (4件)
- **ai-organization/_index.md** — AI時代の組織論フロントページ。階層からインテリジェンスへ、Solo Founder、Context as Moatの横断的テーマを整理
- **ai-organization/ai-org-from-hierarchy-to-intelligence.md** — Block (Jack Dorsey) のAgentic Design Principles。Hierarchy to Intelligenceモデル、Decision Rights Matrix、Open-Book Telemetry、透明性ベースの監視
- **ai-organization/ai-org-solo-founder-and-super-ic.md** — Solo FounderとSuper ICの台頭。Reddit/ClaudeCodeとFourWeekMBA。1人=従来10人の生産性、管理階層のバイパス、$10M→$100Mパス
- **ai-organization/ai-org-context-as-moat.md** — McKinsey Agentic Organization。Proprietary Context Layer（最後のモート）、M-shaped Supervisor

### Updated Files
- **wiki/index.md** — AI Organizationセクション追加（3+1件）、last updated更新
- **wiki/log.md** — This entry

### Key Insights
- **Hierarchy → Intelligence**: Jack DorseyがBlockで実践。報告ライン削除、意思決定権限分散、透明性最大化
- **Context as Moat**: 企業固有の判断基準・文化・市場知見を構造化しエージェントに供給。これが最後の防衛可能資産
- **Super IC**: AIによる管理層のバイパス。技術的実行力を最大化する新しいキャリアパス
- **Agentic Governance**: エージェント実行に対するリアルタイム監視、ガードレール、エスカレーション

### Sources
- https://block.xyz/inside/from-hierarchy-to-intelligence
- https://www.reddit.com/r/ClaudeCode/comments/1ri5pnc/hot_take_solo_founders_with_ai_are_about_to_build/
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
- https://organizationalphysics.com/2026/02/15/your-ai-strategy-isnt-failing-your-org-design-is/
- https://fourweekmba.com/solopreneurs/

### 2026-04-18 — Entity Enrichment: Jensen Huang & Dwarkesh Patel
- **entities/jensen-huang.md** — Major expansion: GTC 2026 keynote details (Vera Rubin, Groq LPU, AI Layer Cake, Token Factory economics, NemoClaw/OpenClaw, Kyber/Feynman roadmap, Space One)
- **entities/dwarkesh-patel.md** — Major expansion: "The Scaling Era" book (Stripe Press), corrected bio (born 2000, UT Austin), recent interviews (Jensen Huang, Elon Musk, Dario Amodei 2nd), "Notes on Space GPUs" analysis, podcast methodology, GMO citation
- Updated index.md entries for both entities with comprehensive summaries

### 2026-04-18 — Entity Addition: TeortaxesTex; Jensen/Dwarkesh Epistemic Analysis
- **entities/teortaxestex.md** — NEW entity page: X/Twitter writer (@teortaxesTex), DeepSeek advocate, China/US tech analyst. "Teortaxes Rant Collection V0.1." Bridging Chinese and Western AI discourse.
- **entities/jensen-huang.md** — Added TeortaxesTex's epistemic analysis section: "Jensen is the driver, not the car" framing, Causal Backbone lens applied to Jensen's agency-driven worldview vs. Dwarkesh's information-driven approach, "Not Being a Loser" survival epistemology
- **entities/dwarkesh-patel.md** — Added TeortaxesTex's methodology critique: "unnaturally great podcaster" praise, rationalism-as-ragebaiting observation, milieu bias (China Bad, AGI wunderwaffe), information-driven vs agency-driven epistemic gap
- Updated index.md with teortaxestex entry and cross-links

## 2026-04-22 — Active Knowledge Crawl (3 topics)

### Selected Topics
Priority selection: 2 high-priority (4+ days stale) + 1 medium-priority (never crawled)
- **context-engineering** (prerequisites, high, last_crawled=2026-04-18 → 4 days stale)
- **agentic-engineering** (laterals, high, last_crawled=2026-04-18 → 4 days stale)
- **death-of-browser** (deepdive, medium, last_crawled=None → never crawled)

### prerequisites: context-engineering → context-routing
- **concepts/context-routing.md** — Context Routing: query-based context dispatch to avoid loading irrelevant knowledge/tools for every query
  - From Vellum AI agentic workflows taxonomy (4 approaches: rule-based, LLM-powered, hierarchical, hybrid)
  - Source: [[raw/articles/crawl-2026-04-22-vellum-agentic-workflows.md]]
  - Token savings: eliminates 30-50% waste from loading all domain knowledge per query

### laterals: agentic-engineering → agentic-workflow-patterns, agentic-web
- **concepts/agentic-workflow-patterns.md** — 3 Levels of Agentic Architectures (AI/Router/Autonomous), 4 Core Components (Planning/Execution/Refinement/Interface), 2026 Agent Stack taxonomy
  - From Vellum AI guide with insights from Yohei Nakajima (BabyAGI), AWS, IBM experts
  - Source: [[raw/articles/crawl-2026-04-22-vellum-agentic-workflows.md]]
- **concepts/agentic-web.md** — Agentic Web paradigm: websites expose capabilities, WebMCP, AX (Agent Experience), machine-legible design
  - Richard MacManus taxonomy of 4 driving forces (capabilities exposure, UI change, browser→AI runtime, dev platform adaptation)
  - Source: [[raw/articles/crawl-2026-04-22-agentic-web-ricmac.md]]

### New Raw Sources (2)
- `raw/articles/crawl-2026-04-22-vellum-agentic-workflows.md` — Vellum AI agentic workflows taxonomy
- `raw/articles/crawl-2026-04-22-agentic-web-ricmac.md` — Agentic Web paradigm shift

### New Concept Pages (3)
- **context-routing** — Context Routing: query-based context dispatch
- **agentic-workflow-patterns** — 3 Levels, 4 Components, Design Patterns
- **agentic-web** — Websites-as-capabilities, WebMCP, AX paradigm

### Index Updates
- `index.md` — Added 3 new concept entries, updated last_updated date

### Hot-Topics Update
- context-engineering: last_crawled → 2026-04-22
- agentic-engineering: last_crawled → 2026-04-22
- death-of-browser: last_crawled → 2026-04-22 (was null)

## 2026-04-23 — Daily Inbox Update: AINews Tokenmaxxing

### Source: Newsletter Digest
- `raw/articles/ainews-tasteful-tokenmaxxing-2026-04-23.md` — AINews #21: Tasteful Tokenmaxxing (swyx, Latent.Space)

### Pages Created (1 concept page)
- **neural-garbage-collection** — Neural Garbage Collection (RL-optimized KV-cache retention/eviction, joint reasoning+cache optimization)
  - From AINews "Post-Training, RL & Inference Optimization" section
  - RL jointly learns reasoning and KV-cache retention/eviction without proxy objectives
  - Complements [[tokenmaxxing]] at the model-level inference optimization layer

### Pages Updated (2 existing pages enriched)
- [[concepts/tokenmaxxing]] — Already existed from earlier crawl; enriched with raw article summary and new industry adoption signals (OpenAI Privacy Filter, Xiaomi MiMo, Perplexity SFT+RL, Google TPU v8)
- [[entities/google-tpu]] — Already existed; full TPU v8 specs (TPU 8t/8i, 1M-TPU cluster) documented in raw article

### Index Updates
- `index.md` — Added 3 entries:
  - `concepts/neural-garbage-collection` (new concept)
  - `entities/google-tpu` (new index entry for infrastructure section)
  - `concepts/tokenmaxxing` (new index entry for AI Economics & Industry)
- Concept Pages count updated: 70 → 71

### Hot-Topics Update
- tokenmaxxing: first crawl → 2026-04-23
- neural-garbage-collection: first crawl → 2026-04-23
- google-tpu: last_crawled → 2026-04-23 (raw article enrichment)
## 2026-04-24 — dreaming: daily consolidation

### Duplicate Check Summary
- Items skipped (already processed by other jobs): 12+
  - ARC-AGI-2 benchmark, WeirdML, AI Engineer Singapore already covered by other daily jobs
  - AI Politics/Criticism (Sean Goedecke) below consolidation threshold (0.48) → review only, no wiki update
- Gaps filled: 0
- Overlapping areas: Geo-strategy analysis (Anthropic Mythos, Meta Muse, Digital NATO) was partially covered by previous Active Crawl runs on 04-23

### Consolidation Summary
- Articles processed: 26
- Themes identified: 7
- Pages created: 0
- Pages updated: 3

### Updated Pages

#### [[concepts/claude-mythos-glasswing]] — Claude Mythos & Project Glasswing
- Added strategic analysis: Anthropic's deliberate strategy to build dependency through security workflows (per Alex Banks, The Signal, Apr 2026)
- Added "commoditizing vulnerability discovery" as strategic endgame
- Updated `updated` frontmatter: 2026-04-10 → 2026-04-24

#### [[concepts/meta-muse-spark]] — Meta Muse Spark
- Added new section "Distribution Advantage" analyzing Meta's 3B user moat across WhatsApp, Instagram, Facebook, Messenger
- Added analysis of "distribution moat" thesis — Muse Spark as default AI layer inside the social graph
- Updated `updated` frontmatter: 2026-04-13 → 2026-04-24
- Added Alex Banks source reference to Sources section

#### [[concepts/ai-digital-nato]] — AI Digital NATO — Frontier Model Forum Distillation Alliance
- Already updated on 04-23 with distillation coalition and contradictory positioning analysis
- Updated `updated` frontmatter: 2026-04-13 → 2026-04-24

### Skipped Themes (below promotion threshold or review-only)
- [[AI批判の政治的バイアス分析]] (Sean Goedecke) — score 0.48, NJ 3 → review only, not promoted
- [[AIベンチマークとコミュニティ]] (ARC-AGI-2, WeirdML) — score 0.42, NJ 2 → below threshold, existing coverage sufficient

## 2026-04-24 — newsletter ingest: GPT-5.5, Codex Superapp, Cat Wu, Qwen3.6-27B

### Newsletter Sources (3 take decisions)
- [[raw/newsletters/2026-04-24-gpt-5-5-chatgpt-images-2-0-qwen3-6-27b.md]] — Simon Willison Newsletter: GPT-5.5, ChatGPT Images 2.0, Qwen3.6-27B
- [[raw/newsletters/2026-04-24-ainews-gpt-5-5-and-openai-codex-superapp.md]] — AINews: GPT 5.5 + OpenAI Codex Superapp (swyx)
- [[raw/newsletters/2026-04-23-how-anthropic-s-product-team-moves-faster-than-anyone-else-cat-wu-head-of-produc.md]] — Lenny's Newsletter: Cat Wu (Anthropic Head of Product, Claude Code)

### Wiki Pages Updated/Created

#### [[concepts/gpt-models]] — GPT Models
- Updated GPT-5 series section with GPT-5.5 release details (April 24, 2026)
- Added pricing table: GPT-5.5 ($5/$30), GPT-5.5 Pro ($30/$180), GPT-5.4 ($2.5/$15)
- Added cross-reference to [[openai-codex-superapp]] and [[chatgpt-images-2.0]]

#### [[concepts/chatgpt-images-2.0]] — ChatGPT Images 2.0 (NEW)
- Created concept page: second-gen image generation in ChatGPT (April 2026)
- Features: improved quality, better prompt understanding, faster generation
- Comparison table vs DALL·E 3, Midjourney
- References "Nano Banana" meme from Ben's Bites

#### [[concepts/openai-codex-superapp]] — OpenAI Codex Superapp (NEW)
- Created concept page: Codex as primary ChatGPT interface (April 2026)
- Details on Codex backdoor API and third-party integration (OpenClaw, Claude Code, etc.)
- Cross-references: [[gpt-models]], [[openai-agents-sdk]], [[harness-engineering]], [[anthropic]]

#### [[entities/cat-wu]] — Cat Wu (NEW)
- Created entity page: Head of Product at Anthropic
- Lenny's Newsletter interview details: development velocity philosophy, Claude Code design
- Cross-references: [[anthropic]], [[claude-code]], [[claude-opus-4-7]], [[dario-amodei]]

#### [[entities/anthropic]] — Anthropic
- Updated with new "Product Team" section covering Cat Wu
- Added Claude Code competitive positioning note
- Updated `updated` frontmatter: 2026-04-09 → 2026-04-24

#### [[concepts/qwen3-6-27b]] — Qwen3.6-27B (NEW)
- Created concept page: dense 27B model outperforming 397B MoE predecessor
- Benchmark table: SWE-bench 77.2 vs 76.2, Terminal-Bench 59.3 vs 52.5, SkillsBench 48.2 vs 30.0
- Architecture: hybrid Gated DeltaNet + attention, dense, 262K context, ~18GB VRAM
- "Thinking preservation" feature for multi-step agent workflows
- Cross-references: [[qwen]], [[open-source-llms]], [[coding-agents]], [[gpt-models]], [[claude-opus-4.7]]

---

## 2026-04-24 — Active Knowledge Crawl (Laterals & Deep Dive)

### Crawl Targets
- agent-team-swarm (laterals)
- ai-evals (laterals)  
- sandbox (laterals)

### New Concept Pages Created
- [[multi-agent-orchestration-patterns]] — 5 core orchestration patterns from Microsoft Azure Architecture Center
- [[agent-communication-protocols]] — MCP vs A2A vs ACP protocol comparison
- [[agentic-conflict-resolution]] — Escalation Ladder for multi-agent disputes
- [[zero-trust-agentic-ai]] — Zero Trust framework for AI agents (Auth0 + Cisco)
- [[excessive-agency]] — OWASP LLM Top 10 vulnerability definition
- [[red-teaming-adversarial-eval]] — ASR, Crescendo Attacks, XPIA testing

### New Source Articles
- raw/articles/crawl-2026-04-24-multi-agent-production-architecture-2026.md
- raw/articles/crawl-2026-04-24-agentic-conflict-resolution-playbook.md
- raw/articles/crawl-2026-04-24-microsoft-red-teaming-agents.md
- raw/articles/crawl-2026-04-24-debugging-ai-agents-production-2026.md
- raw/articles/crawl-2026-04-24-zero-trust-agent-security-auth0.md
- raw/articles/crawl-2026-04-24-cisco-zero-trust-agentic-ai.md

### Updated Existing Pages
- concepts/agent-team-swarm/_index.md — Added 2026 production architecture patterns, communication protocols, failure modes
- concepts/ai-evals.md — (referenced by red-teaming page)
- index.md — Added 6 new concept entries, updated Total pages count

---

## 2026-04-24 — X Bookmarks: The Bitter Lesson of Agent Harnesses

### Source
- X Bookmark: [x.com/gregpr07/status/2047358189327520166](https://x.com/gregpr07/status/2047358189327520166) — Gregor Zunic (@gregpr07), 2026-04-23
- Article: [browser-use.com/posts/bitter-lesson-agent-frameworks](https://browser-use.com/posts/bitter-lesson-agent-frameworks) — The Bitter Lesson of Agent Frameworks (2026-01-16)

### Raw Article Saved
- `raw/articles/the-bitter-lesson-of-agent-harnesses-2026-04-24--d9ffedba.md` — Full scraped article digest

### New Concept Pages (1件)
- **[[concepts/agent-harnesses]]** — Agent Harnesses Philosophy: minimal agent architecture, complete action spaces, ephemeral tools pattern, explicit termination, inversion strategy. Core thesis: all value is in RL'd models, not abstractions.

### Updated Entity Pages (1件)
- **[[entities/browser-use]]** — Added ecosystem repos (agent-sdk, browser-harness, video-use), added 「哲学: エージェントハーネスの苦い教訓」 section with key concepts and cross-reference to [[concepts/agent-harnesses]]

### Key Insights
- **Bitter Lesson applied to agents**: General computation-leveraging methods beat hand-crafted abstractions
- **Incomplete action spaces**: Frameworks fail because available tools are insufficient, not because models are weak
- **Inversion Strategy**: Start maximal, restrict later based on evals — opposite of traditional guardrails-first approach
- **Context bloat**: Ephemeral tools (keep last N outputs) prevent 500KB+ context explosions


## 2026-04-24 Dreaming Consolidation (18:00 JST)

### New Pages Created
- `concepts/sycophancy.md`: Sycophancy in LLMs — tendency to please over truth-seeking, alignment artifacts, mitigation strategies
- `concepts/claude-code-routines.md`: Scheduled/event-driven Claude Code automation (Anthropic research preview, Apr 19)
- `concepts/arc-agi-2.md`: ARC-AGI-2 benchmark — abstract reasoning test (Gemini 3 Deep Think: 45.1% with code)
- `concepts/ai-criticism-politics.md`: Political coding of anti-AI arguments as conservative despite progressive framing

### Pages Updated
- `concepts/gemini.md`: Added Gemini 3.1 Flash TTS section (Apr 2026)

### Sources Processed
- [Ben's Bites: Your AI is lying to your face](https://substack.com/redirect/04e7d3a1-c3a2-4ee5-96af-954e830bc579) — sycophancy (15/15 relevance)
- [Giles Thomas: LLM from scratch 32l](https://www.gilesthomas.com/2026/04/llm-from-scratch-32l-interventions-instruction-fine-tuning-tests) — intervention FT results (12/15)
- [Ben's Bites: TPU 8t/8i technical deep dive](https://substack.com/redirect/394ee21a-c362-4fb3-adf3-c39eb79ee333) — TPU hardware specs (11/15)
- [Ben's Bites: Anthropic's Big Swing](https://substack.com/redirect/2/eyJlIj...yYfU?) — Gemini Everywhere + OpenAI Shape-Shift (9/15)
- [OpenAI Engineering: ChatGPT Images 2.0](https://link.mail.beehiiv.com/v1/c/RZu84jJUQTLob2xNOXDmevcOVPgSrvMtyPN...) — reasoning before drawing (9/15)
- [Troy Hunt: Agentic AI + HIBP APIs](https://www.troyhunt.com/heres-what-agentic-ai-can-do-with-have-i-been-pwneds-apis/) — agentic MCP use cases (7/15)
- [Ben's Bites: Claude Opus 4.7](https://substack.com/redirect/2bfd4077-5fe2-4954-9ef5-fd19f858ca20) — GA release (7/15)
- [Ben's Bites: Claude Design](https://substack.com/redirect/5d9340fa-c538-42b3-8d76-f7a6c3d006f5) — design collaboration (7/15)
- [Sean Goedecke: Anti-AI arguments are conservative](https://seangoedecke.com/many-anti-ai-arguments-are-conservative/) — political coding (6/15)
- [Ben's Bites: Claude Code Routines](https://substack.com/redirect/36a5d462-fad9-43b3-afff-c1d7c95077fe) — scheduled automation (6/15)
- [Ben's Bites: Gemini 3.1 Flash TTS](https://substack.com/redirect/417cdc81-3b4b-4bc6-af06-907920a73e36) — new TTS model (6/15)
- [Epoch AI: ARC-AGI-2](https://substack.com/redirect/034037b3-c281-49ed-8de1-9ea5821ed9ef) — benchmark (5/15)

### Skipped (low signal / already covered)
- Google AI Plans with Cloud Storage (7/15) — feature update, not concept-worthy
- AI Engineer Singapore event (7/15) — event listing
- Gumloop AI Automation Framework (7/15) — tool listing, not enough detail
- Gergely Orosz Substack (5/15) — author page reference
- Alex Banks Substack (4/15) — author page reference
- Free year of Cursor, Google AI Pro, Notion, etc. (4/15) — promotional
- The best way to code with AI (4/15) — blog intro, no substantive content
- The real danger of AI hallucination (3/15) — low detail
- The illusion of thinking (3/15) — low detail
- The Gemini App now available on Mac OS (5/15) — platform availability, already covered
- Claude for Word (5/15) — integration detail, low novelty
