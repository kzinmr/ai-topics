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
