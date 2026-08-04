# Wiki Log

_Log of all wiki changes. Newest entries at top._

## [2026-08-04] raw-backlog-ingest (10:00) | 3 entity enrichments + 2 non-AI skips

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-04 10:00, run 20260804T100026Z). Decisions: 0 takes, 3 references, 2 skips.
- **[[entities/glean]]** — Added "Enterprise Knowledge Graph Cases (July 2026)" section: 7 ROI use cases (content-as-structure, institutional knowledge, GraphRAG grounding, drug discovery, fraud detection, workflow automation, security/compliance), GraphRAG vs vector RAG data (LinkedIn 40h→15h ticket resolution, FalkorDB 90% hallucination reduction sub-50ms, Microsoft community detection), KG market $2.89B/21-33% CAGR, KPIs, adoption roadmap, knowledge-graph vs context-graph FAQ. Source: raw/articles/2026-07-28_glean_enterprise-knowledge-graph-cases-7-applications-that-deliver-roi.md. Cross-link to [[concepts/graph-db-overengineering-rag]].
- **[[entities/justine-tunney]]** — Added raw article path (justine.lol--matmul--95d4772b.md) to sources + "Benchmark scope (Mar 2024)" detail under CPU Matrix Multiplication: Skylake/RPI5/Alderlake measurements, ARMv8.2 fp16 vs x86 float32 compute, llamafile spam-filter use case (prompt eval bound, 3s RPI5 / 420ms Alderlake).
- **[[entities/berthub-eu]]** — Added English raw article path (berthub.eu--articles-posts-ai-for-decision-makers--50c2a644.md) to sources + "Unmeasured pilots" bullet to AI Policy Analysis: Dutch municipal chatbots 64% incorrect / 10% correct answers.
- **Skip (2, archived)**: boyter.org scc Go performance optimization (non-AI), danluu.com "Files are fraught with peril" 2019 talk (non-AI file systems).
- Archive: archive_triage.py raw_backlog --keep-reference — 4 new archived (berthub dedup_skipped), total 2,236 URLs. Tracking: 5 files marked done in processed_raw_articles.json.

## [2026-08-04] raw-backlog-ingest (00:00) | all 5 articles skip — AI articles already captured

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-04 00:00, run 20260804T000007Z). All 5 decisions = skip; no wiki edits.
- (1) Anthropic "Demystifying evals for AI agents" → already captured: [[concepts/evaluation/evals-for-ai-agents]] (101 lines, sources include this exact raw article) + [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] (137 lines: capability vs regression, agent-type evals, pass@k/pass^k, roadmap, saturation, Swiss Cheese model).
- (2) Glean "Agent orchestration platforms compared" → already captured: [[entities/glean]] "Agent Orchestration Platforms Compared (August 2026)" section (6-platform table, Work AI Index stats), added 2026-08-01 by dreaming-wiki-ingest; archive already_archived.
- (3) research.swtch.com Bell Labs history (Russ Cox, 2008) → non-AI computing history, skip + archived.
- (4) filfre.net Rennes-le-Château → non-AI, skip + archived.
- (5) micahflee.com Practical Defenses Against Technofascism → non-AI security/politics, skip + archived.
- Archive: archive_triage.py raw_backlog — 4 new archived (Glean dedup_skipped), total 2,232 URLs. Tracking: 5 files marked done/skip in processed_raw_articles.json.
- Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json

## [2026-08-03] X bookmarks ingest — Shared Discovery Paradox | 1 bookmark processed

- **X bookmark**: Yohei Nakajima, "The Shared Discovery Paradox" (July 21, 2026) — 1 new concept page, 1 entity page enriched
  - **[[concepts/shared-discovery-paradox]]** (new) — Game-theoretic model demonstrating information sharing without action coordination degrades collective outcomes. 16-box, 8-player game with imperfect clues (20% accuracy): sharing information nearly doubles individual accuracy (20% → 38.4%) but halves collective success (83.2% → 38.4%). Coordination restores collective success to 85.9%. Implications for multi-agent systems with shared memory, corporate innovation, VC funding allocation. Links to information cascades, division of cognitive labor, price of anarchy. arXiv:2607.18045.
  - **[[entities/yohei-nakajima]]** (enriched) — Added Shared Discovery Paradox section with game mechanics, key insight, academic foundations, and implications. Updated tags (game-theory, coordination). Added sources (raw article, arXiv, GitHub).
- **Raw article**: `raw/articles/2026-07-21_yoheinakajima_shared-discovery-paradox.md` — full plain_text from bookmark (Tier 0, no API needed)
- **Index**: Concepts 1937→1938; updated yohei-nakajima entity description

## [2026-08-03] raw-backlog-ingest (18:00) | same-day dedup — batch already processed at 14:00

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-03 18:00, run 20260803T180035Z). All 5 articles were already processed by the 14:00 run (20260803T140011Z) — no wiki edits needed.
- Verified same-day coverage: karpathy.github.io Pong from Pixels → [[entities/karpathy-writings]] (landmark tutorial section, raw source linked); glean knowledge-graph-agentic-engine → [[entities/glean]] (Knowledge Graph & Agentic Engine section, raw source linked); berthub.eu Digitale Autonomie 2.0 → [[entities/berthub-eu]] (Digital Sovereignty subsection, raw source linked); filfre.net Ultima IX → non-AI skip (already in [[entities/filfre-net]] References); paulgraham.com startup ideas → non-AI skip (already in [[entities/paulgraham-com]] References + content covered).
- Marked all 5 filenames as processed in `~/.hermes/processed_raw_articles.json` (status: done, decision: skip) so raw_backlog_collect.py stops re-selecting this batch.

---
## [2026-08-03] watchdog | log header restored, index header counts corrected

- **wiki/log.md** — Restored `# Wiki Log` header from line 29 to line 1 (buried by pipeline entry prepends). 249 entries preserved, 0 pipe corruption, header count verified at 1.
- **wiki/index.md** — Corrected section header counts to match actual `- [[...]]` entry lines: `Entities` 875→874 (1 redirect page `entities/tim-sherratt` intentionally unindexed), `Concepts` 1959→1937 (20 `_index.md` files + 2 `_archive/` files inflated the old count).
- **.githooks/pre-commit-jp-check.py** — Fixed `count_jp()` frontmatter detection: only treat the first two `---` lines as frontmatter when the file actually starts with `---`. log.md/index.md use `---` as entry separators, causing position-dependent false-positive JP blocks (blog-triage JP table already in HEAD was miscounted as "new" once entry positions shifted).
- Verified: `validate_index.py` clean (2889 lines), 0 ghost entries, index coverage gap 0, log header at line 1.

---

## [2026-08-03] raw-backlog-ingest (14:00) | 3 pages enriched, 5 articles processed
- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-03 14:00, run 20260803T140011Z).
- **[[entities/karpathy-writings]]** — Expanded "Deep Reinforcement Learning: Pong from Pixels (May 2016)" from 2-line summary to full landmark-tutorial entry: policy gradients as preferred default over DQN ("DQN is so 2013"), 130-line numpy implementation, four factors holding back AI (compute/data/algorithms/infrastructure), Pong-as-MDP framing, OpenAI Gym design contribution. Frontmatter updated (updated: 2026-08-03, +source raw/articles/karpathy.github.io--2016-05-31-rl--fd04d0db.md).
- **[[entities/glean]]** — Added "Knowledge Graph & Agentic Engine (Jun 2025)" section: KG triplet structure + edge properties (timestamps/access control/confidence/provenance), 4 documented LLM failure modes (proximity over precision, entity confusion e.g. Claude 3.7 vs 3.5 Sonnet v2, deterministic queries, multi-hop reasoning), 3-phase KG construction (LLM-enhanced), enterprise KG difficulty (no manual review; noun extraction → prominence filtering → predicate identification pipeline), Personal Graph (atomic actions → task clusters → OKR mapping), Context System thesis ("cognition of agent systems is not just the LLM — it is also the context system"). Frontmatter updated (updated: 2026-08-03, +source raw/articles/2026-05-10_glean_knowledge-graph-agentic-engine.md).
- **[[entities/berthub-eu]]** — Added "Digitale Autonomie 2.0: en nu echt" (Surf Privacy & Security Conference, Jun 2026) subsection under Digital Sovereignty: US dependence "virtually absolute" (100% of municipalities/notaries/banks need Microsoft), no computer avoids US data flow, (semi-)governments must lead, "small but important" project advice. Frontmatter updated (updated: 2026-08-03, +source + reference entry).
- **Skipped (non-AI / already covered)**: filfre.net Ultima IX (retro gaming history, already in entities/filfre-net.md References), paulgraham.com "How to Get Startup Ideas" (non-AI startup essay, already in entities/paulgraham-com.md References + content covered).
## [2026-08-03] active-crawl (11:03) | 2 new pages, 1 enriched, 3 raw articles, 15 wikilink fixes

### New Concept Pages
- **[[concepts/ai-productivity-gap]]** — AI Productivity Gap: disconnect between AI capability improvements and measured developer productivity; Björn Roche time allocation analysis (July 2026, HN 56 pts). Time allocation tables for senior vs junior devs, Amdahl's Law analogy, doorman fallacy, parallel agent management overhead. Sources: [bjorg.bjornroche.com](https://bjorg.bjornroche.com/management/ai-productivity-gap/), raw article.
- **[[concepts/mu-tools-for-agents]]** — Mu: open-source suite of 18+ developer tools for AI agents, distributed as MCP server in Go (HN Show HN, 50 pts). Browser, git, image, video, file system, code execution, social media integrations. Source: [github.com/micro/mu](https://github.com/micro/mu), raw article.

### Enriched Pages
- **[[concepts/qwen-3-8.md]]** — Added Qwen3.8-Max release section (HN 623 pts): first Qwen-Max-class open-weight release, reasoning_effort support, Qwen3.8-27B variant, oh-my-cli autonomous coding demo. Source: [qwen.ai/blog?id=qwen3.8](https://qwen.ai/blog?id=qwen3.8), raw article.

### Raw Articles Saved
- `wiki/raw/articles/2026-07-12_bjorn-roche-ai-productivity-gap.md`
- `wiki/raw/articles/2026-08-03_micro-mu-tools-for-agents.md`
- `wiki/raw/articles/2026-08-03_qwen-qwen3.8-max-release.md`

### Wikilink Fixes
- 15 broken wikilinks fixed across 3 pages: `concepts/agent-infrastructure` → `concepts/infrastructure`, `concepts/claude-code` → `concepts/claude-code/claude-code-auto-mode`, `concepts/deepseek` → `entities/deepseek`, `concepts/local-llm` → `concepts/local-llm/local-ai`, `concepts/ai-adoption` → `concepts/ai-adoption-failures-and-enterprise-psychosis`, `concepts/amdahls-law` → `concepts/ai-economics-bubble-venture-capital-subprime`, `concepts/productivity` → `concepts/agent-productivity`

### Discovery Sources
- HN Algolia (15 trending stories, top: DeepSeek V4 Flash 739pts, Qwen3.8-Max 623pts)
- X/Twitter via xurl (10 substantive threads: model comparisons, agent architecture, AI policy)
- Wiki gap analysis + blogwatcher DB (RLAIF, Yi, Aider identified as critical gaps)

---

## [2026-08-03] newsletter-wiki-ingest (11:00) | 3 takes executed (2 new pages, 1 enrich), 4 references, 1 new entity

- Recovered triage JSON from checkpoint (`/opt/data/.hermes/cron/data/newsletter/triage_latest.json`, run 20260803T103004Z) — triage agent saved JSON before response render failed (known pattern). Archive for run already saved (`raw/archived/triage/newsletter/2026-08-03_20260803T103004Z.json`).
- **Take 1 — Gemini Robotics 2**: created `concepts/gemini/gemini-robotics-2.md` (3-model family, whole-body humanoid control, Apptronik Apollo 2 demo, 32–92% multi-finger success, <200-example adaptation, ER 2 long-horizon planning). Updated `concepts/gemini/index.md` (Recent section + frontmatter) and `concepts/vla-models.md` (VLA table row + frontmatter).
- **Take 2 — AI music copyright**: created `concepts/ai-music-copyright.md` — GEMA v. Suno Munich Regional Court win (Aug 2 2026, The Signal), Suno ordered to stop reproducing; Warner Music Group × Suno partnership contrast; linked to anthropic-copyright-settlement / google-flow-music.
- **Take 3 — Catalini moat framework**: enriched `concepts/open-vs-closed-model-gap.md` with "Moat Strategy Perspective — Christian Catalini" section (measurable → automatable; 4-month flat gap; value moves to shipping judgment; routing as aggregation layer). Created `entities/christian-catalini.md` (Lightspark co-founder, MIT economist).
- **Reference — Interconnects artifacts #23**: enriched `entities/nathan-lambert.md` (consolidation prediction wrong → diffusion; Tencent Hy3 / Motif-3-Beta / AMD Instella / Apertus-v1.5) and `concepts/open-weight-vs-closed-llm-gap.md` (Ecosystem Diffusion section with release table).
- **Reference — DeepSeek V4-Flash-0731**: enriched `concepts/deepseek-v4.md` (Intelligence Index 50 / open-weight top-3, OpenAI Responses + Codex config defection spec, 284B/13B active retrained checkpoint beating 1.6T V4 Pro preview at agent tasks; noted param variance vs Willison 304B).
- **Reference — Vanishing Gradients Aug 3 episode**: enriched `entities/sebastian-raschka.md` and `entities/hugo-bowne-anderson.md` (Ep. 73: Kimi K3 Delta Attention/MoE, harness-dependent model behavior, routing, DeltaNet/Mamba trend, 25-company open letter).
- Skips (4) confirmed: Lenny's pure-podcast, Interconnects covered-models batch, The Signal roundup batch, Superintel+ social batch — all archived.
## [2026-08-03] blog-wiki-ingest (10:35) | 4 takes verified (already committed), 1 reference enriched

- Recovered triage JSON from checkpoint (`/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json`) — triage agent saved JSON before response render failed.
- **Verified 4 takes already executed by earlier run (commit 00b3e5ba)**: boris-cherny--claude-code-development (Startup School 2026: Opus 5 autonomous runs, prompt-injection resistance, product overhang), openai-astra (new page: 10 math problems, Marcus fallacy-of-composition critique), anyscale (Nscale acquisition + Physical AI Skill). All `updated: 2026-08-03` with substantive content — no redundant edits.
- **Reference enriched**: `entities/cory-doctorow.md` — added "Dualism — The Coin-Trick Fallacy (Aug 2026)" section (consciousness / understanding vs statistical extrapolation, Turing Test diminishment, rights-to-nature vs rights-to-constructs asymmetry, centaur vs reverse-centaur labor, economic coin-trick: fired because AI can do job vs boss believes it can). Frontmatter updated + source added.
- 12 skips confirmed (math essays, HIBP, career advice, accessibility, unsaved YouTube/LWN) — archive already saved by commit 73af08f9.

## [2026-08-03] tag-audit-weekly (10:00) | 2 tag violations fixed

- Ran `scripts/tag_audit.py` (cron pre-run script blocked: path resolves outside `/opt/data/.hermes/scripts` — ran directly).
- Audit: 2,934 pages with tags, 752 unique tags, **2 tags not in SCHEMA taxonomy** (both one-off): `wiki-maintenance`, `graph-analysis` (both on `queries/wiki-graph-analysis-weekly-2026-07-31.md`).
- **Fixed**: Deleted both one-off non-SCHEMA tags (inline `tags: [wiki-maintenance, graph-analysis]` → `tags: []`), updated `updated:` to 2026-08-03.
- Re-audit: **0 violations** (0 non-SCHEMA, 0 composite kebab-case).
- Normalization dry-run: 39 pages would change, but all source tags are valid SCHEMA taxonomy tags (preference rewrites like `gpu`→`hardware`, `retrieval`→`rag`, `ai-safety`→`agent-safety`) — out of scope for violation-fix; NOT applied to avoid tag specificity loss.
- **Fixed pre-existing log header burial**: `llm-pricing-monitor` entry had been prepended above `# Wiki Log` header; restored header to top.

## [2026-08-03] blog-triage (10:24) | 17 articles scanned, 6 AI-relevant updates

**Scan**: 17 new articles from blogwatcher RSS scan
**Updated**: `entities/boris-cherny--claude-code-development.md`, `entities/anyscale.md`, `entities/openai-astra.md`
**Created**: `entities/openai-astra.md`

Triage summary (NJ = newsjacking score 0-5):
| ソース | タイトル | NJ | アクション | 対象 |
|--------|----------|-----|------------|------|
| ycrootaccess.com | Boris Cherny: Building Claude Code | 5 | wiki更新 | boris-cherny--claude-code-development.md |
| garymarcus.substack.com | OpenAI Astra (vastly oversold) | 4 | 新規作成 | openai-astra.md |
| anyscale.com | Anyscale + Nscale | 4 | wiki更新 | anyscale.md |
| anyscale.com | Physical AI Skill | 3 | wiki更新 | anyscale.md |
| pluralistic.net | Dualism (Cory Doctorow) | 3 | 保留（AI consciousness哲学） |
| simonwillison.net | condense-json 1.0 | 2 | スキップ（低関連性） |
| その他 | Troy Hunt, John D Cook 等 | 0-1 | スキップ |

Key findings:
- **Opus 5**: Extended autonomous runs (days/weeks), prompt injection resistance via mechanistic interpretability, 80% system prompt deletion
- **Anyscale + Nscale**: Major infrastructure acquisition, Ray doubling down, GB300 NVL72 at scale
- **OpenAI Astra**: 10 open math problems solved, but Marcus critiques fallacy of composition

## [2026-08-03] llm-pricing-monitor (10:00) | OpenAI GPT-5.6-terra/luna price correction

**Updated**: `comparisons/llm-api-pricing.md`
- **OpenAI**: Corrected GPT-5.6-terra standard pricing from $2.50/$15.00 to $2.00/$12.00
- **OpenAI**: Corrected GPT-5.6-luna standard pricing from $1.00/$6.00 to $0.20/$1.20
- Root cause: wiki was using Fast mode (2× standard) prices instead of Standard mode
- Batch, cache, tier analysis, and cost comparison tables all updated
- **Anthropic**: Verified unchanged — Sonnet 5 intro pricing $2/$10 through Aug 31; Mythos 5 at Fable 5 pricing
- **Google**: Verified unchanged — all Gemini 3.x prices match live Vertex AI page
- **DeepSeek**: Verified unchanged — V4-Flash $0.14/$0.28, V4-Pro $0.435/$0.87
- Sources: OpenAI, Anthropic docs, Google Vertex AI, DeepSeek API docs (all fetched live)

## [2026-08-03] raw-backlog-ingest (10:00) | duplicate batch detected - no wiki changes, tracking fixed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-03 10:00, run 20260803T100025Z).
- DUPLICATE of run 20260803T040040Z (04:00): all 5 articles already processed - entities/ash-vardanyan.md enriched (SimSIMD v5.3 SVE2 set intersections), entities/chiark-greenend-org-uk-sgtatham.md expanded (Policy of transience habits + 6 permanence criteria), glean CIO guide / glean create-ai-strategy-2024 / pxlnv metaverse-fever-dream skipped + archived.
- Root cause: 5 entries left with status=processing in processed_raw_articles.json -> collector re-selected the batch. Tracking fixed: all 5 marked done with duplicate_of=20260803T040040Z to prevent re-selection.
- No wiki changes. Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (0 take / 0 reference / 5 skip).
## [2026-08-03] raw-backlog-ingest (04:00) | 2 pages enriched, 5 articles processed
- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-03 04:00, run 20260803T040040Z).
- **[[entities/ash-vardanyan]]** — Added "SimSIMD v5.3 — SVE2 Set Intersections (May 2026)" section under Key Projects: HISTCNT/MATCH (SVE2) vs VP2INTERSECT (AVX-512) vs Galloping, up to 5x faster set intersections for sorted u16/u32 arrays, u16 SVE2 always >= NEON (u32 mixed, ~50% slower on skewed 128x8192), SVE2 live on AWS Graviton 4 / upcoming Grace Hopper + Cobalt + Axios, sparse-vector similarity use case. Frontmatter updated (updated: 2026-08-03, +source ashvardanian.com/posts/simd-set-intersections-sve2-avx512/ + raw article).
- **[[entities/chiark-greenend-org-uk-sgtatham]]** — Expanded existing "Policy of Transience" section with concrete habits from the 2025 essay (unset HISTFILE shell history, GUI desktop clearing, browser close-all, X11 session management off, tmpfs /tmp + ~/mem) and the 6 permanence criteria (reliable/easy to find/explained/change-controlled/portable/usable by others). Frontmatter updated (updated: 2026-08-03).
- **Skip (3)**: glean CIO guide (marketing, generic vendor-selection framework, no technical claims; glean.md already comprehensive), glean create-ai-strategy-2024 (dated 2024 marketing), pxlnv metaverse-fever-dream (non-AI, already archived).
- Archive: 3 newly archived, 1 dedup_skipped (pxlnv) — archive_index total 2,202. Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (1 take / 1 reference / 3 skip).
## [2026-08-03] raw-backlog-ingest (00:00) | duplicate batch detected - no wiki changes, tracking fixed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-03 00:00, run 20260803T000025Z).
- DUPLICATE of run 20260802T220041Z (22:00): all 5 articles already processed - entities/ash-vardanyan.md enriched (StringZilla Unicode search stack v4.3-4.5, ICU 50x), entities/glean.md enriched (Definitive Guide to AI-Based Enterprise Search section), minimaxir ai-agent-coding already primary source of entities/minimaxir-com.md, Thinking Machines On-Policy Distillation already captured in concepts/post-training/on-policy-distillation.md, danluu bad-decisions non-AI (baseball/board-game decision quality) skip.
- No wiki changes. Tracking fixed: 5 entries marked done/skipped in processed_raw_articles.json to prevent re-selection (previous run left them status=processing; 1-hour timeout triggered re-collect).
- Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (0 take / 0 reference / 5 skip).

## [2026-08-02] raw-backlog-ingest (22:00) | 2 pages enriched, 5 articles processed
- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-02 22:00, run 20260802T220041Z).
- **[[entities/ash-vardanyan]]** — Enriched StringZilla section with Unicode search stack (v4.3-v4.5, May 2026): tokenizing (25 whitespace chars, 9 newline variants, 10x faster), case-folding (1,400+ Unicode 17 rules, 10x faster), case-insensitive substring search (20-150x faster, 20,000x vs PCRE2), fold & scan pipeline 5-15 GB/s (~50x ICU), Unicode-spec-generated synthetic test suite for correctness. Frontmatter updated (updated: 2026-08-02, +source ashvardanian.com/posts/search-utf8/).
- **[[entities/glean]]** — Added "Definitive Guide to AI-Based Enterprise Search (May 2026)" section: traditional vs AI search comparison, Enterprise Graph, code intelligence, 100+ SaaS integrations, 5-vendor platform comparison table (Glean/Moveworks/Coveo/Elastic/Guru), $150M Series F, Glean Protect, RAG/agent automation trends. Frontmatter updated (updated: 2026-08-02, +raw/articles/2026-05-10_glean_the-definitive-guide-to-ai-based-enterprise-search-for-2025.md).
- **Skipped**: minimaxir.com "AI agent coding skeptic" (already primary source of entities/minimaxir-com.md), thinkingmachines.ai "On-Policy Distillation" (already captured in concepts/post-training/on-policy-distillation.md), danluu.com "How good are decisions?" (non-AI: baseball/board-game decision quality).
- Archive: 4 archived, 0 dedup_skipped (archive_index total 2,199). Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (1 take / 1 reference / 3 skip).

## [2026-08-02] daily-skeleton-enrichment | L2→L3: Kyle Jeong + Apurva Gandhi (browser agent harness, CDP, dual advisors)

- **Skeleton backlog**: 0 pages with `status: skeleton` remain — continued L2→L3 enrichment of thinnest entity pages (established pattern).
- **[[entities/kyle-jeong]]** (L2→L3, 61→93 lines, 2.9KB→6.8KB): Added 2 new raw articles — `raw/articles/2026-06-03_kylejeong_browser-agent-harness.md` (Browserbase harness essay: harness=rebranded context engineering, 4 raw-model failures, 4 raw-CDP production problems, six-layer harness: security/caching/identity/credential-brokering/skill-memory/filesystem, Stagehand vs raw CDP decision tree) and `raw/articles/2026-07-17_kylejeong_what-is-cdp.md` (CDP explainer: commands/events, sessions/targets, Site Isolation, flat mode, why raw CDP sucks). Updated bio: UCLA graduate June 2026, 21yo SF. Added 4 new blog posts (CDP, great firewall, college essay, Twitter distribution essay). New sections: Browser Agent Harness Essay. Cross-links: browserbase, browse-sh, agent-harnesses, browser-agent/death-of-browser, browser-use-production-architecture, firecracker, sandbox, computer-use.
- **[[entities/apurva-gandhi]]** (L2→L3, 68→102 lines, 2.9KB→5.2KB): Corrected bio from live site (updated Jul 2026): 2nd-year PhD (not just "PhD student"), **co-advised by Aviral Kumar + Graham Neubig** (was Neubig only), student researcher at **NVIDIA Research**, Amazon AI PhD Fellow. Added full Google Scholar publication table (~580+ cites, 12 papers incl. deepfake detector ~226, SkillWeaver ~124, AgentDiagnose, Agent Data Protocol, CodeScout, PPT-Eval). Fixed frontmatter related: (removed dangling graham-neubig/aviral-kumar links — no pages exist).
- index.md: updated descriptions for both entities.
- Sources: kylejeong.com + RSS, browserbase.com blog, apga.github.io (live), Google Scholar.

## [2026-08-02] dreaming-wiki-ingest | 1 reference enriched (Simon Willison Open Letters)
- **Recovery**: upstream dreaming-group render failed (Pitfall #12), but committed archive-only at `dd4e0c2b` (log.md + archive JSON + archive_index.json, no entity changes) — archive-only variant (Pitfall #21).
- **Triage**: 15 decisions (0 takes, 1 reference, 14 skips). Reference: [[entities/simon-willison]] Open Letters blog post (Aug 2).
- **Deep Sleep verification**: entity page line 683 had only Oxide and Friends podcast blurb; the 3-letter analysis (Open Weights and American AI Leadership — Microsoft-shepherded, 235 signatories, distillation support; Anthropic's response — Dario Amodei's distillation crackdown; Pacing the Frontier — 1,324 frontier employees) was absent from page body → genuine gap.
- **Enriched**: entities/simon-willison.md — added "Open Letters on AI Development — 3 Letters Analyzed" section with the 3 letters' details; frontmatter updated (updated: 2026-08-02, +source simonwillison.net--2026-aug-2-open-letters). Wikilinks: [[concepts/claude/fable-5]], [[concepts/kimi-k3]], [[concepts/open-source-ai-must-win]].
- **Archive**: already committed by upstream (8 newly archived, total 2,195 URLs) — no re-run needed.

## [2026-08-02] dreaming | Pattern E saturation — 1 reference, 0 takes
- **Checkpoint**: 0 articles collected, 201 recent raw articles on disk (range 2026-07-26 → 2026-08-02).
- **Prior triage (2026-08-01)**: 22 decisions (0 takes, 7 references, 15 skips) — all consumed by dreaming-wiki-ingest (Aug 1), 5 entity pages enriched (Glean, Cohere, Simon Willison, Harvey, ElevenLabs).
- **Today's daily pipeline coverage**: blog-triage (20 articles, 3 pages updated), active-crawl (4 pages), raw-backlog-ingest ×3, newsletter-wiki-ingest (Superintel, 1 ref enriched), watchdog auto-fixes.
- **Pattern E scan**: 30 recent articles screened from Aug 1-2. Key candidates already covered:
  - Sierra × Plaid Partnership → entities/sierra.md (Plaid section exists)
  - Thinking Machines Lab × Safe Path to Open Weights → entities/thinking-machines-lab.md (Open Weights Safety Framework section)
  - Martin Alderson × Speed vs Intelligence → entities/martin-alderson.md (Speed Over Intelligence section)
  - Kimi K3 × Together AI Developer Guide → concepts/kimi-k3.md (458 lines, all architectures covered)
  - LearnVector × Andrew Ng → entities/learnvector.md (39 lines, created today)
- **Reference candidate**: [[entities/simon-willison]] — Open Letters blog post (Aug 2): 3 open letters (Open Weights and American AI Leadership, Anthropic response, Pacing the Frontier) not yet reflected in entity page body. Low priority enrichment.
- **Non-AI skips**: 15 articles (Apple, math, hardware, thermal cameras, package management, personal essays).
- **Archive**: 8 newly archived, 7 dedup skipped. Total archive: 2,195 URLs.
- **Takes=0** — Full saturation. No new pages needed.

## [2026-08-02] raw-backlog-ingest (18:00) | duplicate batch detected - no wiki changes, tracking fixed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-02 18:00, run 20260802T180008Z).
- DUPLICATE of run 20260802T140007Z (14:00): all 5 articles already processed - concepts/post-training/rl-environments created, recursive-self-improvement + entities/semianalysis enriched (SemiAnalysis Scaling RL), 4 non-AI skips archived.
- No wiki changes. Tracking fixed: 5 entries marked done/skipped in processed_raw_articles.json to prevent re-selection (1-hour processing timeout had re-collected them).
- Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (0 take / 0 reference / 5 skip).

## [2026-08-02] watchdog | wiki health digest review

### Checks
- index.md corruption: pipe_prefix 0 / line_number_prefix 0 / triple_bracket 0 / space_prefix 0 — clean
- validate_index.py: pass (2883 lines)
- Ghost entries (recursive scan): 0
- Orphan pages: 24 reported, all false positives (21 _index.md + 2 _archive + 1 redirect tim-sherratt → tim-sh)

### Changes
- Fixed Concepts header count: 1954 → 1955 (actual 1935 files + 20 _index)

---

## [2026-08-02] watchdog | auto-fix log header burial + 2 frontmatter fixes

- RESTORED: `# Wiki Log` header to line 1 in log.md (was buried at line 32 by raw-backlog-ingest prepend). 3 orphaned entries moved after header block; 231 entries preserved, 0 pipe corruption.
- FIXED: `wiki/events/anthropic-code-w-claude-2026.md` — added missing `type: event` frontmatter field.
- FIXED: `wiki/queries/saas-future-and-agent-developer-career.md` — repaired malformed frontmatter (`tags:` list items sat after `sources: []`); tags block restored under `tags:`, `sources: []` moved after, added missing `updated: 2026-08-02`.
- Verified: validate_index.py exit 0; index corruption (pipe/triple-bracket/line-number/space-prefix) all 0; index coverage gap 0 genuine (tim-sherratt is redirect, 2 _archive files intentional); log header at line 1.

---

## [2026-08-02] raw-backlog-ingest (14:00) | 1 concept created, 2 pages enriched, 5 articles processed
- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-02 14:00, run 20260802T140007Z).
- CREATED: [[concepts/post-training/rl-environments]] — RL Environments (RLEF): environment engineering for RL post-training (latency/reliability/security, CPU-only env servers, world-model/digital-twin environments, environment compute). Source: SemiAnalysis "Scaling RL" (Jun 10).
- ENRICHED: [[concepts/recursive-self-improvement]] — added "Industry Evidence: SemiAnalysis — RSI Already Playing Out (June 2026)" section (Claude 4 system card compiler/kernel/quadruped RL evals, OpenAI Codex building next model version, grunt-work-first thesis, RL-helps-do-better-RL loop).
- ENRICHED: [[entities/semianalysis]] — added "Scaling RL: Environments, Reward Hacking, Agents, Scaling Data (June 2026)" to Key Publications (RL inference-heavy, data as moat, China compute constraint, decentralized RL, lab restructuring).
- SKIPPED (non-AI): paulgraham.com "The Refragmentation" (2016 essay), danluu.com "Google SRE book" (ops book notes), oldvcr.blogspot.com MkLinux WGS 9150 (retro; already archived), oldvcr.blogspot.com 6o6 v1.1 (retro 6502 virtualization).
- Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (1 take / 0 reference / 4 skip).

## [2026-08-02] active-crawl (11:10) | 4 pages — 1 created, 3 enriched

NEW:
- entities/learnvector.md — Andrew Ng's AI edtech company ($100M Coursera), one-to-one learning platform. Source: learnvector.ai via HN (267 pts)

ENRICHED:
- concepts/training-infra/model-serving-autoscaling.md — Together AI inference-native autoscaling (in-flight requests, TTFT, GPU utilization, token throughput metrics). Source: together.ai blog (Jul 31)
- entities/sierra.md — Plaid partnership for financial infrastructure AI agents (Aug 3). Added fintech/partnership tags + SCHEMA.md partnership tag
- entities/thinking-machines-lab.md — "A Safe Path to Open Weights" framework (Jul 31). Added open-weight safety section with staged release model. Fixed pre-existing wikilink paths (nvidia, modal-labs, inference/sglang, inference/vllm, security-and-governance/ai-safety, ai-alignment)

SOURCES:
- raw/articles/2026-07-31_together-ai_autoscaling-endpoints-llm-inference.md
- raw/articles/2026-08-03_sierra_plaid-partnership-ai-agents.md
- raw/articles/2026-07-29_learnvector_andrew-ng-ai-edtech.md
- raw/articles/2026-07-31_thinking-machines-lab_safe-path-to-open-weights.md

DISCOVERY: HN Algolia (15 stories), X/Twitter xurl (10 results), blogwatcher DB + wiki gap analysis

## [2026-08-02] newsletter-wiki-ingest (10:39) | Superintelligence. 2026-08-01 triage: 1 reference / 5 skip
- Reference: entities/kim-isenberg.md enriched with "The Duel That Never Happened" (Aug 2026 DeepDive, AI benchmark controversy; paywalled body, preview thesis captured). Frontmatter updated (updated: 2026-08-02, +benchmark/benchmark-framing tags, +2 sources).
- Skip (5): dup beehiiv tracking link, author X profile, batch meta links 4-15 (product/subscription/social/footer/expired), beehiiv hosted page, status tracking pixel. Archived via archive_triage.py.
- Triage checkpoint recovered from /opt/data/.hermes/cron/data/newsletter/triage_latest.json (upstream response render failure; checkpoint valid).

---

## [2026-08-02] blog-triage (10:30) | 20 articles scanned, 3 entities/pages updated

Blog ingest checkpoint: 20 articles from 9 blogs. Triage filtered to AI-relevant Tier 1/2 sources.

**Updated:**
- [[entities/martin-alderson]] — Added "Speed Over Intelligence" section (Aug 2026): model selection shift from intelligence to speed, 100 tok/s as new 100ms threshold, Amdahl's Law limits on agent speed gains, price war dynamics (GLM 5.2 at 5% of Opus pricing), 2027 projection of 500 tok/s with HBM4 GPUs. Source: raw/articles/martinalderson.com--posts-speed-vs-intelligence--7a7e675b.md
- [[entities/cory-doctorow]] — Added "Why Businesses Lie About AI" section (Aug 2026): amplifying Nikhil Suresh's "AI Mania Is Eviscerating Global Decisionmaking" — coordination problem of corporate AI honesty, 0% enterprise AI project success rate, AI demo hypnotism effect, token leaderboards, Doctorow's "toy steering wheel" theory of why bosses love AI. Source: raw/articles/pluralistic.net--2026-08-01-dare-snot--cd886481.md
- [[concepts/kimi-k3]] — Updated from Together AI developer guide: reasoning_effort now supports 3 levels (low/high/max, not max-only), added Developer Features section (preserved thinking, dynamic tool loading, structured output, vision limits), fixed outdated "max-only" caveats. Source: raw/articles/together.ai--blog-kimi-k3-guide--70e2c263.md

**Raw-saved only (no wiki action):**
- simonwillison.net × 6 (open letters summary, July newsletter, Greg Brockman quote, datasette-apps release, ten advances in math, Slack Emoji Maker) — newsletter/link posts, policy context already captured in existing pages
- pluralistic.net (Cory Doctorow) — article content captured via entity update above
- together.ai (Kimi K3 guide) — content captured via concept update above
- tedium.co, shkspr.mobi, oldvcr.blogspot.com, nesbitt.io, johndcook.com × 3, daringfireball.net × 2, construction-physics.com, borretti.me — non-AI content (hardware reviews, math essays, Apple news, retro computing, package management)

## [2026-08-02] raw-backlog-ingest (10:00) | 1 entity enriched, 5 articles processed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-02 10:00, run 20260802T100016Z). Archive: 4 newly archived, 1 dedup_skipped (archive_index total 2,164). Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json (0 take / 1 reference / 4 skip).

**Enriched:**
- [[entities/ben-boyter]] — Bonzamate section expanded from 1-line mention to sourced description: AWS Lambda-only Australian search engine (bonzamate.com.au), index baked into Lambda binaries at compile time using bitfunnel-style bloom filters (2048-bit/doc, uint64 slices, 50MB/zip + 75GB free storage exploitation, ~100K docs/lambda × 1000 lambdas ≈ 100M pages), shut down 2025-05 when AWS closed the Lambda storage loophole (service-terms #30). Added article URL to sources + Blog section. Source: raw/articles/boyter.org--posts-abusing-aws-to-make-a-search-engine--35e404ea.md

**Skipped (already captured / non-AI):**
- (1)+(2) substack app-link AINews "Good Friday" 2026-04-10 (2 tracking-URL variants of post_id=193117526) → skip: both already referenced in [[entities/substack]] + [[entities/luke-curley]] References; topics (Gemma 4 Apache 2.0 launch + local inference benchmarks, Hermes Agent adoption/memory plugins, Claude Code rate limits, METR time horizon, RLMs, Apple SSD, MAI-Transcribe-1) all covered by [[entities/gemma-4]] (433 lines), [[concepts/gemma-family]], [[concepts/recursive-language-models]], [[concepts/microsoft-mai-models]], [[entities/hermes-agent]].
- (3) michael.stapelberg.ch Go rsync vulnerability analysis → skip: non-AI (Go memory safety vs C rsync CVEs), already archived 2026-05-25 by blog triage (raw/archived/triage/blog/2026-05-25_20260525T070051Z.json).
- (4) chiark.greenend.org.uk Spectre tiling combinatorial coordinates → skip: non-AI math essay, already in [[entities/chiark-greenend-org-uk-sgtatham]] References + aperiodic-tilings section covers the series.

## [2026-08-01] raw-backlog-ingest | Enriched LLVM concept (Flang/Fortran) + Brutecat entity (StubZero RCE)

- **[[concepts/llvm]]** (stub -> full, 25 -> ~90 lines): Enriched from LLVM Blog "LLVM Fortran Levels Up: Goodbye flang-new, Hello flang!" (Mar 2025). Added core components (LLVM IR, Clang, MLIR, Flang), Flang timeline table (PGI 1989 -> NVIDIA 2013 -> F18/FIR 2018-19 -> flang rename Oct 2024 -> LLVM 20.1 Mar 2025), HLFIR/SPEC2017/OpenMP technical highlights, Fortran context (80% of ARCHER2 apps), and AI relevance (MLIR underpins accelerator compiler stacks, TensorFlow, torch-mlir; Chris Lattner -> Modular). Registered `compiler` tag in SCHEMA.md. Source: raw/articles/blog.llvm.org--posts-2025-03-11-flang-new--8f37a052.md
- **[[entities/brutecat-com]]** (enriched): Added "StubZero: Google Cloud Production RCE (CVE-2026-2031)" section - proto definition leak endpoint ("req2proto as a Service"), internal workflow queue leak (Spanner->Salesforce), escalation to arbitrary Stubby RPCs as prod service identity (RCE classification), recurrence 3 months later via GetIntegrationVersion RPC. Payouts: $60k + $75k + $13,337 = $148,337 total. Added 2 Key Discoveries table rows + source. Tags +vulnerability +cybersecurity. Source: raw/articles/brutecat.com--articles-google-cloud-rce--13889f7b.md
- Batch notes: 5 candidates; paulgraham.com "Being Popular" and danluu.com cache-incidents already fully covered (entity pages had sections + sources); miguelgrinberg SQLAlchemy Ch3 already in References (non-AI ORM tutorial, skip).

## [2026-08-01] daily-skeleton-enrichment | Enriched LM Studio + Entire to L3, created Thomas Dohmke entity

- **Skeleton backlog saturated**: 0 pages with `status: skeleton` remain in wiki/entities — the daily job continues with L2→L3 enrichment of the thinnest entity pages.
- **[[entities/lm-studio]]** (L2→L3, 52→~200 lines): Added LM Studio Bionic agent (Jul 16, 2026 launch; Work/Code Projects, cloud/local/LM Link model sources, ZDR), Bionic cloud pricing table (Kimi K3, GLM 5.2, Kimi Code K2.7, DeepSeek V4 Pro), LM Link and Locally mobile app (Jun 2026), LM Studio Engine Protocol, MTP speculative decoding, Anthropic-compatible API for Claude Code (Jan 2026), hardware support (Apple Silicon MLX, NVIDIA DGX Spark/GB300, AMD ROCm/Vulkan), 0.4.x version history table. Company: Element Labs, Inc.
- **[[entities/entire]]** (L2→L3, 54→~170 lines): Added CEO Thomas Dohmke (ex-GitHub CEO), Marvin agent, checkpoints-in-git-history thesis ("session logs are the most important artifact"), Distributed Git Network launch (Jul 8, 2026; ForgeMark benchmark: 570K clones/h, 2.1M pushes/h), ref-based checkpoint storage, entire blame, Goose support, token-level code navigation, company culture (zero-bugs policy), team roster, $60M seed at $300M valuation (per evis-drenova) + company-page investors.
- **[[entities/thomas-dohmke]]** (NEW): Former GitHub CEO (2021–2025), HockeyApp co-founder (acquired by Microsoft 2014), founded Entire early 2026 ($300M valuation by Feb 2026). Career timeline, GitHub era (Copilot), Entire thesis quotes, cross-links to entire/evis-drenova/farhan-thawar/shopify. Resolves dangling `[[entities/thomas-dohmke]]` links in evis-drenova.md and related pages.
- **[[entities/evis-drenova]]** (updated): Wikilinked Thomas Dohmke inline mentions.
- Sources: lmstudio.ai (homepage, changelog, docs/bionic, blog, pricing), entire.io (homepage, blog, company page, git network essay), Wikipedia (Dohmke).
- index.md: +1 entity (871 total), updated descriptions for entire + lm-studio.


## [2026-08-01] dreaming-wiki-ingest | 5 entity pages enriched (recovered from failed dreaming-group render)

- **Recovery**: dreaming-group JSON render failed at 18:20:51 (output c4a9e8d2f671/2026-08-01_18-20-51.md, 4,461 lines). Triage JSON at cron/data/dreaming/triage_latest.json (22 decisions: 0 takes, 7 references, 15 skips) + output-file theme clusters used as source of truth. Upstream commit fc2829ed (18:12) touched only log.md — enrichment not yet executed.
- **Deep Sleep verification**: 7 reference candidates verified against entity pages. 5 genuine gaps, 2 marginal (harvey/elevenlabs brief notes).
- **Enriched**:
  - [[entities/glean.md]] — 3 new sections: Agent Orchestration Platforms Compared (6-platform table), Comprehensive Guide to IR, UK Work AI Index (12h/week saved, 18% org impact, 38% botsitting)
  - [[entities/cohere.md]] — EU AI Content Transparency Code signatory (Article 50, EU AI Act, Section 1)
  - [[entities/simon-willison.md]] — DeepSeek-V4-Flash-0731 body paragraph (304B params, ahead of MiniMax M3, $0.14/M, pelican benchmark)
  - [[entities/harvey.md]] — Legal Research vs Traditional Tools (3 shifts, 5-question buyer framework, BigLaw Bench/LAB)
  - [[entities/elevenlabs.md]] — Multilingual Transcription explainer (auto language detection, diarization, keyterm prompting)
- **Archive**: archive_triage.py dreaming — 22 candidates, 2 new archived, 20 dedup_skipped (saturation: total 2,160 URLs)
- **Skips**: 15 (13 fully covered by adjacent pipelines + 2 non-AI batches)

## [2026-08-01] raw-backlog-ingest (18:00) | duplicate batch detected — no wiki changes, tracking fixed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-01 18:00, run 20260801T180055Z). Archive: 3 already_archived, 1 null, 1 not_archived.
- Duplicate of the 14:00 run (20260801T140040Z): the collector re-selected the SAME 5 articles (14:00 run left them status=processing in processed_raw_articles.json). Same failure mode as the 00:00→04:00 cycle.
- (1) wheresyoured.at "AI's Brokenomics" → skip: already in [[entities/ed-zitron]] (Hyperscaler Political Positioning June 2026 section) + sources; archived.
- (2) wheresyoured.at "AI Doesn't Have ROI" → skip: already in [[entities/ed-zitron]] (Enterprise Cost Crisis section: Uber $500M token incident, kalopsia thesis) + sources; archived.
- (3) wheresyoured.at "Let AI Burn" → skip: already in [[entities/ed-zitron]] (Notable Articles table: circular compute spend, $765B+ capex worthless) + sources; archived.
- (4) walkinglabs "Hands-On Modern RL" → skip: already in [[concepts/post-training/hands-on-modern-rl]] (172-line page created 2026-06-09 from this exact raw article).
- (5) harvey.ai "Legal Operations Management" → skip: already enriched into [[entities/harvey]] (Legal Operations Management Guide section) by the 14:00 run.
- No wiki page creation or enrichment needed. Tracking: 5 marked done/skip in processed_raw_articles.json. Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json.

## [2026-08-01] watchdog | wiki health digest — all clean, header count corrected

### Checks
- Index corruption: 0 pipe prefix, 0 triple bracket, 0 line-number, 0 space prefix (validate_index.py: clean)
- Ghost entries: 0 genuine (24 reported orphans all false positives: 23 `_index.md` + 1 redirect `entities/tim-sherratt` → `[[entities/tim-sh]]`, skipped per A4c rule 6)
- Index coverage gap: 0 (all 2864 L2 files referenced; tim-sherratt is a redirect)
- Frontmatter: 2285 pages checked, 23 missing `created:` (escalated — needs manual batch pass)
- Stale pages: 1856 (>30 days) — informational, no auto-fix

### Changes
- `wiki/index.md`: `## Concepts (1954 pages)` → `## Concepts (1932 pages)` — header counted 20 `_index.md` files; actual section entries = 1932 (Entities header already matched entries)

---

## [2026-08-01] watchdog | Auto-fixed buried log header (fix_log_header_burial.py)

- Restored `# Wiki Log` header from line 146 to line 1 — 145 orphaned entries (2026-07-31 → 2026-08-01 pipeline prepends) were above the header; all 219 entries preserved.
- Patched `config/hermes/skills/_overrides/wiki-graph-health/scripts/fix_log_header_burial.py`: header block boundary now computed dynamically (up to first `## [` entry) instead of fixed +4 — prevents splitting the first entry when no blank line follows the log metadata line.
- Verified: `grep -c '^# Wiki Log'` = 1, `head -1` = `# Wiki Log`, 0 standalone-pipe lines, 0 orphan `### 2026-` lines.
- Not auto-fixed (over 10-file threshold / dedicated pipelines): 23 pages missing `created` (15 malformed YAML frontmatter + 8 clean), 212 unique tag violations (tag-audit-weekly backlog), 6 entity duplicate pairs, ~2,048 broken wikilinks, 464 orphans.

## [2026-08-01] raw-backlog-ingest (14:00) | 1 page enriched, 5 articles processed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-01 14:00, run 20260801T140040Z). Archive: 3 already_archived, 1 null, 1 not_archived.

**Enriched:**
- `entities/harvey.md` — Added "Legal Operations Management Guide (June 2026)" section: five core legal ops functions (financial mgmt, outside counsel, contract ops, tech/data, strategic planning/governance), when-to-invest thresholds (5-10 lawyers / $5-10M spend; law firms 50-100 lawyers), AI governance as new legal ops responsibility (platform approval, HITL review, accuracy benchmarking, AUP, audit logs), "AI amplifies maturity" thesis, CLOC Core 12 maturity model (Reactive→Emerging→Developing→Leading), 5-phase implementation + 12-18 month roadmap, AI use case categories (contract review, drafting, research), general-purpose vs legal-specific AI positioning. Source: raw/articles/2026-06-19_harvey_legal-operations-management.md

**Skipped (already captured):**
- wheresyoured.at "AI's Brokenomics" → already in [[entities/ed-zitron]] (Hyperscaler Political Positioning June 2026 section) + sources; archived.
- wheresyoured.at "AI Doesn't Have ROI" → already in [[entities/ed-zitron]] (Enterprise Cost Crisis section: Uber $500M token incident, kalopsia thesis, Dark Output critique) + sources; archived.
- wheresyoured.at "Let AI Burn" → already in [[entities/ed-zitron]] (Notable Articles table: circular compute spend, $765B+ capex worthless) + sources; archived.
- walkinglabs "Hands-On Modern RL" → already in [[concepts/post-training/hands-on-modern-rl]] (172-line page created 2026-06-09 from this exact raw article); no wiki changes needed.

## [2026-08-01] active-crawl | 3 pages created, 1 page enriched (trending topics crawl)

**Sources:** HN Algolia (15 stories found), X/Twitter (10 items), blogwatcher DB (21 candidates), wiki gap analysis (13 gaps identified)

**Discovery:** Cross-referenced HN trending AI stories (115 candidates filtered to 15) and X/Twitter search results against wiki coverage gaps. 3 pipelines already ran today (newsletter-wiki-ingest, blog-wiki-ingest, X Article ingestion), so focused on net-new topics.

**Created:**
- `concepts/ai-mathematics-theorem-proving.md` — AI for mathematical theorem proving & TCS; OpenAI Astra 10 advances covering Connes Rigidity, sphere packing, circuit complexity, group theory, cryptography (124 HN pts)
- `concepts/coding-agents/qm-multiplayer-agent-harness.md` — YC-backed open-source multiplayer agent harness; Slack + web, per-person/per-room scoped workspaces, vendor-independent multi-harness design (584 HN pts)
- `concepts/pytorch-reference-language.md` — PyTorch team proposal for treating PyTorch programs as a formal reference language for ML computation; fundamental shift in ML compiler design (80 HN pts)

**Enriched:**
- `concepts/coding-agents/model-routing.md` — Added Manifest router deprecation section (July 2026 post-mortem, 121 HN pts): LLM routing complexity may not justify cost savings; counterpoint analysis vs Augment Prism and Ronin

**Raw articles saved (4):**
- `raw/articles/2026-08-01_openai_ten-advances-mathematics-tcs.md`
- `raw/articles/2026-07-31_qm_multiplayer-agent-harness.md`
- `raw/articles/2026-07-31_manifest_deprecated-llm-router.md`
- `raw/articles/2026-07-25_pytorch_reference-language.md`

**Skipped (already covered):** Anthropic cybersecurity eval incidents (page created 07-31), Kimi K3 (full page exists), censorship-transfer-distillation (page exists)

**Tag fix:** `science` → `ai-in-science` on ai-mathematics-theorem-proving.md (non-canonical tag)

## [2026-08-01] newsletter-wiki-ingest | 1 page created, 8 pages enriched (triage 20260801T101509Z recovered from checkpoint)

- Recovered triage JSON from /opt/data/.hermes/cron/data/newsletter/triage_latest.json after newsletter-triage output parse failure (checkpoint survived; standard recovery path)
- 17 decisions: 1 take, 8 references, 8 skips
- Created: concepts/prompt-engineering.md (stub -> full page; The Signal "The End of Prompting" — paradigm shift from written prompts to demonstration-based interaction; Anthropic Record a skill vs OpenAI Record & Replay comparison table, Kiana Ehsani "people should not have to write prompts", what prompts leave out, first-mover reversal, Alex Karp counter-argument)
- Enriched: entities/deepseek.md (V4-Flash-0731 & July 2026 Price War section — $0.14/$0.28 API beta, 98% cache discount, 284B/13B vs 304B discrepancy kept with sources, Terminal-Bench 82.7 +25.8, GDPval Elo 1189->1559, AI index 40->50, vs Opus 4.8 within 4 points on 5/9)
- Enriched: entities/microsoft.md (MAI-Cyber-1-Flash — 5B active security model, 95.95% CyberGym in MDASH harness, ~12 pts above Mythos 5 at half cost, hybrid caveat)
- Enriched: concepts/gemini/index.md (Recent Updates — Gemini Drops: 3.6 Flash, 3.5 Flash-Lite, Spark rollout, voice macOS; AI index v4.1 ~50.1)
- Enriched: entities/langchain.md (Ecosystem Map July 2026 — LangGraph/DeepAgents/LangSmith, standardized internal evals, Harbor task conversion)
- Enriched: concepts/harness-engineering.md (Microsoft Echoverse — spec-to-stateful-app compiler with grounded graders, rollout analysis repairs environments+training signals, shallow envs hurt live-site accuracy)
- Enriched: entities/minimax.md (H3 video model — Vercel AI Gateway launch, open weights promised, fal/Pollo/PixVerse/Leonardo/OpenArt partners, baked-in super-resolution; added video-generation tag)
- Enriched: concepts/ai-video-generation-2026.md (Seedance 2.5 — native 30s/consistent 3-min videos, interactive frame editing, 50 multimodal refs, 720p caveats)
- Skips (8): AINews/Signal noise links, AWS Q2 financials, Gemini Robotics 2 demo, Thinking Machines Inkling-Small, open-vs-closed cyber debate, OpenAI Voice desktop, sandbox escape incidents (already covered)
- Sources: raw/newsletters/2026-07-31-the-end-of-prompting.md, 2026-07-31-deepseek-answered-openai-s-price-cut-overnight.md, 2026-08-01-ainews-not-much-happened-today.md

## [2026-08-01] blog-wiki-ingest | 2 pages enriched, 5 pages updated (triage 20260801T101221Z recovered from checkpoint)

- Recovered triage JSON from /opt/data/.hermes/cron/data/blog_ingest/triage_latest.json after blog-triage output parse failure (checkpoint survived; standard recovery path)
- 20 decisions: 2 takes, 6 references, 12 skips
- Updated: concepts/deepseek-v4.md (V4-Flash-0731 added to Model Lineup — 304B/167GB, $0.14/$0.27, ahead of MiniMax M3 per Artificial Analysis; new V4-Flash-0731 section)
- Updated: concepts/mcp-2026-07-28-spec.md (new Tooling & Ecosystem section: mcp-explorer, datasette-mcp, llm-mcp-client; MCP-as-security-boundary argument)
- Updated: entities/simon-willison.md (4 new July 31 entries: datasette-agent 0.4a0 browser_task, Stateless MCP three implementations, Oxide and Friends podcast, smevals)
- Updated: entities/ed-zitron.md (Notable Articles row + Premium AI Is Getting Way Too Expensive subsection: $110B TTM vs $122B OpenAI raise; table pipe normalization)
- Updated: entities/gary-marcus.md (Three Reactions to Anthropic's Latest Apologia section)
- Updated: concepts/llm-evaluation.md (promoted from stub to active; smevals section with eval/task/config/run vocabulary)
- Updated: concepts/agentic-engineering-patterns.md (Giles Thomas case study: "AIs identify problems and I fix them myself")
- SCHEMA.md: added ai-critic tag to taxonomy (used by ed-zitron.md)
- Sources: raw/articles/simonwillison.net--2026-jul-31-* (5), wheresyoured.at--premium-ai-is-getting-way-too-expensive, garymarcus.substack.com--p-three-reactions-to-anthropicss-latest, gilesthomas.com--2026-07-ai-use

## [2026-08-01] X Article ingestion | Cerebras GPT-5.6 usage guide (1,470 bookmarks)

- Source: Cerebras (@cerebras) X Article "Getting the most out of GPT-5.6: Sol, Terra, and Luna" (2026-07-27, 1,470 bookmarks, 462K impressions)
- Authors: @0xSero & Zhenwei Gao (@zhennydez)
- Saved: raw/articles/2026-07-27_cerebras_getting-most-out-of-gpt-5-6.md
- Updated: entities/cerebras-systems.md (added GPT-5.6 Acceleration section, Cerebras runs Sol at 750 tok/s, sources)
- Updated: concepts/gpt/gpt-5-6.md (added Cerebras Usage Guide section: model selection escalation, reasoning level cost impact, cache strategy, Sol+Terra pairing, external models; added source)
- No new pages created (duplicate avoided — existing GPT-5.6 concept page at concepts/gpt/gpt-5-6.md)
- Key insights: Luna→Terra→Sol escalation pattern, reasoning levels each add ~50% cost, cache reads 90% cheaper with 30-min TTL, Cerebras 10× faster for Sol

## [2026-08-01] raw-backlog-ingest (04:00) | duplicate batch detected — no wiki changes, tracking fixed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-01 04:00, run 20260801T040019Z) re-selected the SAME 5 articles processed by the 00:00 run (commit 75f681b9): the 00:00 run left them status=processing in processed_raw_articles.json (stuck >1hr → re-collected).
- Verified prior work substantive on disk: entities/alex-ellis.md (80 lines), concepts/local-qwen-vs-claude-opus.md, concepts/agents-mcp-rl-course.md, entities/cat-wu.md, entities/thariq-shihipar.md all present.
- Action: no page creation/enrichment (would duplicate 00:00 work). Marked all 5 as status=done in /opt/data/.hermes/processed_raw_articles.json with 00:00 decisions (2 take / 3 skip) so 08:00+ collects skip them.

## [2026-08-01] raw-backlog-ingest | 1 page created, 4 pages enriched, 5 articles processed

- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-08-01 00:00, run 20260801T000005Z). Archive: 3 already_archived, 1 not_archived (simonwillison fireside), 1 null (willbrown transcript).
- (1) alexellis.io "Local Qwen isn't a worse Opus, it's a different tool" → take (entity gap): content was already captured in [[concepts/local-qwen-vs-claude-opus]] but no author entity existed → CREATED [[entities/alex-ellis]] (OpenFaaS founder, local AI thesis; tags person/founder/open-source/local-llm/coding-agents); cross-linked concept page (wikilink + Related Pages) and index.md (869→870).
- (2) willbrown agents-mcp-rl-lesson2 raw transcript → skip: fully captured in [[concepts/agents-mcp-rl-course]] (Lesson 2 summary section) + [[entities/will-brown]] (References already lists this raw file). Added raw transcript to course page sources frontmatter for traceability.
- (3) wheresyoured.at "Cargo Culture" → skip: fully captured in [[entities/ed-zitron]] (Cargo Culture — Religious Metaphors section) + [[concepts/agentic-engineering]] (Agent Loop Debate section); already archived.
- (4) simonwillison.net "A Fireside Chat with Cat and Thariq from the Claude Code team" → take (entity enrichment): [[entities/claude-code]] already had a fireside section → added "Additional Insights" (eval base for drop-in replacement, behavioral evals, biology-not-physics tool design, credential injection, ant fooding, Deep Blue/ambition, Fable video editing, Claude Tag memory, eval tooling stance); enriched [[entities/simon-willison]] (July 2026 Updates entry), [[entities/cat-wu]] (new Fireside Chat Insights section), [[entities/thariq-shihipar]] (new Fireside Chat section with rewrites-are-good, Deep Blue, system prompt reduction, security posture).
- (5) wheresyoured.at "The More You Buy, The More You Lose" → skip: fully captured in [[entities/ed-zitron]] (The More You Buy section: NVIDIA–SB Energy $250B circular deal, Winstar/Lucent analogy, CoreWeave bond crisis, $1.35T off-balance-sheet debt, capex % revenue table); already archived.

## [2026-07-31] raw-backlog-ingest | 5 articles triaged — all already captured (0 take / 0 ref / 5 skip)

## [2026-07-31] x-accounts-scan | 3 new posts, 2 wiki pages updated
- Scan: 84 tracked accounts, 12 scanned (72 skipped budget). 3 new posts from 2 accounts.
- Post 1: Daniel Han (@danielhanchen) — DeepSeek-V4-Flash-0731 GGUF released (UD-Q8_K_XL lossless + UD-Q4_K_XL). 10 quant variants from Q8 to IQ1_S. [[entities/daniel-han|Daniel Han]]
- Post 2: Daniel Han (@danielhanchen) — Kimi K3 dynamic 1-bit progress (594GB, aiming for 512GiB). Already captured in [[concepts/kimi-k3|Kimi K3]].
- Post 3: Dax Raad (@thdxr) — OpenCode Go privacy docs update. Low-value, skipped.
- Created: [[raw/articles/2026-07-31_unsloth_deepseek-v4-flash-0731-gguf]]
- Updated: [[entities/daniel-han]] (Key Work + Blog table + sources), [[concepts/deepseek-v4]] (Local Inference → GGUF quants added), index.md
- Archive: /opt/data/.hermes/cron/data/x_accounts_archive/x_accounts_20260731T223042Z.json
- Batch: raw_backlog_collect.py --sort ai-hint --limit 5 (2026-07-31 22:00, run 20260731T220020Z). Archive: 2 newly archived, 3 dedup-skipped (archive_index total 2119). Tracking: 5 marked done/skip in processed_raw_articles.json.
- (1) wheresyoured.at "The Subprime Data Center Crisis" → skip: fully captured in [[concepts/subprime-data-center-crisis]] (created from this article 2026-07-24) + [[entities/ed-zitron]] (728 lines); already archived.
- (2) Gergely Orosz "Slow Down to Speed Up" (Craft Conference 2026, YouTube transcript) → skip: fully captured in [[entities/gergely-orosz]] (keynote section added 2026-07-31 from this exact raw file; Meta Instagram exploit, tokenmaxxing, ~5,000 AI labelers).
- (3) dynomight.net "Pseudpocalypse" → skip: already archived as non-AI essay (stylometry/pseudonymity, 29-bit information-theoretic argument); entity [[entities/dynomight-net]] exists, no gap.
- (4) gilesthomas.com "Benchmarking Qwen 3.6 35B MoE on RTX 3090" → skip: fully captured in [[concepts/qwen-3-6-35b]] "Real-World Benchmarks (RTX 3090)" section (Vulkan/CUDA tok/s table, UD-IQ4_NL_XL, offload); already archived.
- (5) Aakash Gupta "Agent Safety Separation of Duties" (X post) → skip: fully captured in [[concepts/security-and-governance/agent-separation-of-duties]] (worker/evaluator split, Codex /goal Apr 2026, Claude Code 2.1.139 May 2026, 31-turn experiment) + [[entities/aakash-gupta]].
- No wiki page creation or enrichment needed this batch. Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json.

## [2026-07-31] dreaming-wiki-ingest | 4 references verified + enriched (upstream archive-only commit)
- Upstream dreaming-group (18:09) committed archive only (71311cfe); render failed after checkpoint save (triage_latest.json 18:13, 6 decisions: 4 ref, 2 skip)
- Deep Sleep verification gate: all 4 reference candidates confirmed genuine gaps vs entity page content
- Enriched [[entities/hebbia.md]] - Max AI team member product launch (Jul 30): institutional AI worker, slides/report/model output, email-native, preview rollout. Frontmatter updated, source added.
- Enriched [[entities/fireworks-ai.md]] - (1) Embedding model fine-tuning recipe (Qwen3-Embedding-8B, InfoNCE + in-batch negatives, +39% nDCG@100 LegalBench, +61% case-to-case LegalPincite, train-at-served-context-length finding); (2) LoRA vs FullFT three-test protocol (Qwen3.5-9B, data coverage / tuned LR / rank levers). Frontmatter updated, sources added.
- Enriched [[entities/harvey.md]] - AI trademark search & IP workflows (Jul 30): search-layer vs legal-AI-layer division, clearance memo drafting, office action responses, enforcement. Frontmatter updated, source added.
- Skips: parallel.ai customer-watch (scrape failed, brotli error), Harvey hire announcement (personnel only, no technical depth)
- Archive: already committed by upstream (2026-07-31_20260731T180900Z.json) - no re-run needed

## [2026-07-31] raw-backlog-ingest | 2 pages enriched, 3 skips (all already covered)
## [2026-07-31] dreaming | Pattern E saturation — 4 references identified, 0 takes
- Checkpoint: 0 articles from RSS/newsletter, 200 recent raw articles on disk
- Duplicate check: Blog-wiki-ingest (1 take + 9 refs), Newsletter-wiki-ingest (4 takes + 1 ref), Active-crawl (3 pages), Raw-backlog-ingest (15+ articles) all processed today
- Prior dreaming triage (Jul 30): consumed, archive exists at 2026-07-30_20260730T180752Z.json
- Filesystem scan of Jul 31 06:00 sitemap articles (6 files):
  - [[entities/hebbia.md]] — Hebbia Max product launch (first AI team member for financial institutions, slide generation, email integration). Entity page (updated 2026-07-11) has no Max mention. Reference candidate for enrichment.
  - [[entities/fireworks-ai.md]] — Two technical articles: (1) LLM-to-Embedding fine-tuning (LegalBench/TREC Clinical Trials benchmarks, 3 training modes), (2) LoRA-to-FullFT switching guide (Qwen3.5-9B test bed, recipe tuning erased FullFT advantage). Entity page (updated 2026-07-28) has neither. Reference candidates for enrichment.
  - [[entities/harvey.md]] — AI Trademark Search product feature (clearance to brand protection workflow). Reference candidate.
  - Parallel Web customer-watch: scrape failed (brotli decoder error). Skipped.
  - Harvey Nijanthan Hariharan: personnel announcement, no technical depth. Skipped.
- Archive: 6 candidates archived (0 dedup), total_archive_urls=2117


Batch 20260731T180057Z (raw_backlog_collect.py --sort ai-hint --limit 5). 5 articles evaluated with body reading.

### Enriched
- [[entities/gergely-orosz]] — Added "Slow Down to Speed Up" Craft Conference 2026 keynote section (raw: 2026-06-24_yt_slow-down-ai-software-engineering.md): Meta/Instagram zero-password-reset exploit traced to AI-written code reviewed by AI, token-maxing leaderboard at Meta ("session immortal"/"token"/"legend", killed April), AI usage in perf eval + layoff-driven inflation, ~5,000 Meta devs doing manual AI labeling, and the talk's prescription (cap agent usage to what you can verify, tech-debt removal, one-extra-agent rule, don't outsource learning). Frontmatter: updated 2026-07-31, added raw source + agent-safety tag.
- [[concepts/tokenmaxxing]] — Added "Meta Case Study: Tokenmaxxing Under Performance Pressure (June 2026)" section documenting the untasteful end of the spectrum (leaderboard gaming, layoff amplification, Instagram exploit consequence) with lessons for the spectrum. Frontmatter: updated 2026-07-31, added raw source.
- [[concepts/separation-of-duties]] — Stub (23 lines, broken source URL) rewritten as short-form entry + redirect pointer to canonical [[concepts/security-and-governance/agent-separation-of-duties]] (193 lines, created from the same raw article 2026-06-18). Fixed source URL (missing trailing 0).

### Skipped (already covered / non-AI)
- wheresyoured.at "The Subprime Data Center Crisis" — fully captured in [[concepts/subprime-data-center-crisis]] (created from this article 2026-07-24) + [[entities/ed-zitron]]; already archived.
- dynomight.net "Pseudpocalypse" — non-AI essay (pseudonymity/statistical author fingerprinting); already archived.
- gilesthomas.com "Benchmarking Qwen 3.6 35B MoE on RTX 3090" — fully captured in [[concepts/qwen-3-6-35b]] "Real-World Benchmarks (RTX 3090)" section (Vulkan/CUDA tok/s table, UD-IQ4_NL_XL, offload); already archived.
- Agent Safety Separation of Duties (Aakash Gupta X post) — fully captured in [[concepts/security-and-governance/agent-separation-of-duties]] (worker/evaluator architecture, /goal April 2026, Claude Code 2.1.139 May 2026, 31-turn experiment); stub duplicate fixed as redirect.

---

## [2026-07-31] daily-skeleton-enrichment | Enriched levelsio + niplav from L2 to comprehensive (L3)
- Enriched [[entities/levelsio.md]] — Upgraded from L2 (63 lines, 3.5KB) to comprehensive (117 lines, 12KB). Added: blog stats (800+ posts since 2013), Lex Fridman Podcast, levels.vc fund (Oct 2025), AvatarAI.me $100K/10 days (2022); new "AI-Era Thesis (2026)" section (indie hackers going extinct — execution cost flipped to ~$20/mo, BigAI cannibalization, cancelled all SaaS and vibecoded replacements, minimal stack = FOSS + VPS + AI API + R2/S3, Claude Code on VPS for ~a year, 4B requests/yr on $244/mo, vibe-coded Stripe dispute responder); Cross-References (solo-founder-philosophy, vibe-coding, vibe-ceo, solo-founder-stack, cloudflare-email-sending); Sources. Status: L3. Raw articles: wiki/raw/articles/2026-07-30_levelsio_indie-hackers-first-to-go-extinct.md, wiki/raw/articles/2026-07-26_levelsio_cancelled-saas-vibecoded.md.
- Enriched [[entities/niplav.md]] — Upgraded from L2 (48 lines, 2.2KB) to comprehensive (135 lines, 12KB). Added: Overview (pseudonymous researcher, niplav.site since 2019, Long Content/Gwern-inspired, heavy Claude/GPT/Gemini/Kimi collaboration); Forecasting Track Record table (Metaculus Brier 0.116 / 281 uniform-sampled questions, PredictionBook 0.2365, Manifold B-/profit, 38th baseline ranking); AI Alignment writings (BCI, TAI race with China, discontinuous takeoff, anti-superpersuasion, OSS patching); Forecasting methodology (question decomposition, Iqisa library); Quantified Self; Programming & Mathematics; expanded Style & Approach (literate-programming, Crocker's rules, AI-use transparency). Fixed broken related link (concepts/rlhf → concepts/post-training/rlhf). Status: L3.
- Cross-links: [[concepts/glut-of-circuits.md]] — added [[entities/niplav]] to related frontmatter + thesis wikilink, fixed broken concepts/reward-hacking → concepts/evaluation/reward-hacking; [[concepts/vibe-ceo.md]] and [[concepts/harness-engineering/agentic-workflows/vibe-coding.md]] — added [[entities/levelsio]] backlinks. Index.md descriptions updated for both entities.



## [2026-07-31] wiki-health-fix | health scan clean; benchmark pages updated field

Wiki health scan (17:50 UTC run):
- **index.md**: no corruption (pipe 0, triple-bracket 0, line-number 0, space-prefix 0); validate_index.py clean (2876 lines).
- **Ghost entries**: 0 genuine (2862 links all resolve).
- **Index coverage gap**: 0 (3 flagged = 2 `_archive/` + 1 redirect `tim-sherratt` → `tim-sh`, all intentional).
- **Orphan registration**: none needed (all 24 reported orphans were `_index.md` files or redirects).
- **Frontmatter**: 8 pages in `concepts/ai-benchmarks/` missing `updated:` — added `updated: 2026-07-31` (arc-agi-1, bfcl-v3, chartqa, factorio-learning-environment, hle, ifeval, mrcr, simpleqa).
- **Header counts**: match section entries (Entities 869, Concepts 1929, Comparisons 35).
- **Known duplicate pairs** (report only, no merge): deliberate-coder/deliberatecoder, eugene-yan/eugeneyan, giles-thomas/gilesthomas, lilian-weng/lilianweng, martin-fowler/martinfowler, samuel-colvin/samuelcolvin.

---

## [2026-07-31] watchdog | auto-fix log header burial + index header counts + agentty updated

Watchdog auto-fixes (17:35 UTC run):
- **log.md**: restored buried `# Wiki Log` header to line 1 (was at line 187 — 11 orphaned entries pushed above it by raw-backlog-ingest prepend). All 204 entries preserved; 0 pipe corruption.
- **index.md**: corrected stale section header counts — Entities (871→869), Concepts (1951→1929) to match actual section entries.
- **concepts/agentty.md**: added missing `updated: 2026-07-16` (matches created date; page never modified since creation).

Verified clean: index corruption (0 pipe/triple-bracket/line-number prefixes), 0 genuine ghost entries, 0 genuine index coverage gaps (3 files on disk not in index = 2 `_archive/` + 1 redirect, all intentional), 0 duplicate index entries (3 flagged all false positives).

Escalated (needs human review, not auto-fixed):
- 23 pages missing `created` frontmatter (over 10-file auto-fix threshold)
- 6 known duplicate entity pairs (deliberate-coder, eugene-yan, giles-thomas, lilian-weng, martin-fowler, samuel-colvin) — dedup merge needed
- 464 true orphans, ~2,048 broken wikilinks, 978 stale pages (>90d), 941 tag violations (tag-audit-weekly backlog)
- x_accounts stale(26h) alert: TRANSIENT — job runs every 2 days at 22:30 UTC; last run 07-29 22:30, next expected 07-31 22:30

## [2026-07-31] raw-backlog-ingest | 5 articles evaluated, 0 new pages needed (all already covered)

Batch collected 14:00 UTC (raw_backlog_collect.py --sort ai-hint --limit 5, run 20260731T140039Z). All 5 articles already captured in existing wiki pages → 0 take, 0 reference, 5 skip. No wiki page changes needed.

- **Dwarkesh Podcast — Alex Imas & Phil Trammell "What remains scarce after AGI?"** → skip: covered in entities/dwarkesh-patel.md (Timeline Jun 2026 + sources), concepts/agi-economics.md, concepts/agi-scarcity.md (relational sector/human economy/wealth way); entities/alex-imas.md, entities/phil-trammell.md exist. (raw: dwarkesh.com--p-alex-imas-phil-trammell--f12d8644.md)
- **Dario Amodei — Policy on the AI Exponential** → skip: covered in entities/dario-amodei.md ("Policy on the AI Exponential (June 2026)" section: FAA-style regulation, job displacement, MATCH/OVERWATCH, legislative proposals) + concepts/ai-exponential.md + concepts/ai-policy.md; raw article in sources. (raw: 2026-06-10_darioamodei_policy-on-the-ai-exponential.md)
- **Giles Thomas — LLM from scratch Part 34a (JAX training loop)** → skip: covered in entities/giles-thomas.md (Part 34a section: JAX+NNX+Optax, outside-in approach, A-to-A model) + raw article in sources. (raw: gilesthomas.com--2026-06-llm-from-scratch-34a-building-a-jax-training-loop-fo--059d9f9a.md)
- **Zhang & Khattab — Language model harnesses are compositional generalizers** → skip: covered in entities/omar-khattab/rlm.md (Compositional Generalization via Harnesses Jul 2026: LID principle, 8-32x length generalization, context offloading + programmatic sub-calling, Claude Code/Codex critique) + entities/alex-zhang.md + concepts/compositional-generalization.md. (raw: 2026-07-20_zhang-khattab_language-model-harnesses-compositional-generalizers.md)
- **Ed Zitron — The AI Industry Is Losing** → skip: covered in entities/ed-zitron.md (June 2026 BIS Systemic Risk Warning section: $1T hyperscaler capex, Oracle $129.5B debt/$38B lease/$260B future lease, CoreWeave 65% dependency, Four Losers, OpenAI IPO delay) + raw article in sources. (raw: wheresyoured.at--the-ai-industry-is-losing--a92f13ac.md)

Archive: 2 newly archived (gilesthomas-34a, zhang-khattab), 3 dedup-skipped (already in archive index). Tracking: 5 marked done/skip in processed_raw_articles.json. Triage: /opt/data/.hermes/cron/data/raw_backlog/triage_latest.json.

## [2026-07-31] active-crawl | 3 new pages from trending discovery

**Trend Discovery** (3 parallel subagents): HN Algolia (15 stories, top: censorship transfer 131pts, Tokenless 70pts, GUI agents 68pts, git worktrees 31pts), X/Twitter (10 results, top: Agency sandboxes 146 bookmarks), wiki gap analysis (15 gaps identified).

**Pages created:**
- `concepts/training-divergence-reproducibility.md` — LLM Training Divergence & Reproducibility: case study of Giles Thomas's GPT-2 reproduction, overtraining experiments (6.4B tokens, 2-epoch), Chinchilla-optimal violations, IFT gap unresolved despite test loss improvements. (raw: gilesthomas.com--2026-07-why-do-openai-gpt2-weights-beat-mine-3-overtraining)
- `concepts/sandbox/git-worktrees-agent-isolation.md` — Git worktrees are not an agent isolation boundary: shared hooks/config/stash/refs enable hook injection, config rewriting, stash theft; local clones with hardlinks provide actual isolation at identical cost (~59MB/~900ms). (raw: 2026-07-30_fletch_git-worktrees-agent-isolation)
- `concepts/post-training/censorship-transfer-distillation.md` — Censorship Transfer in Knowledge Distillation: CTGT research showing DeepSeek V4 Flash's +45.45 censorship gap does NOT transfer via distillation to GPT-OSS; self-distillation matches Chinese-teacher performance on FinanceReasoning (83.61%). (raw: 2026-07-30_ctgt_distillation-censorship-transfer)

**SCHEMA.md:** Added tags `gpt-2`, `reproducibility`, `censorship`.

## [2026-07-31] newsletter-wiki-ingest | 4 takes + 1 reference processed, 6 pages enriched

**Recovery**: newsletter-triage output render failed ("failed to parse JSON response"); recovered from checkpoint `/opt/data/.hermes/cron/data/newsletter/triage_latest.json` (20260731T102556Z, valid JSON, 12 decisions).

### Takes (4 → page enrichments)
- **concepts/gpt/gpt-5-6.md** updated: Added missing Jul 30 price-cut details — Terra explicit new price ($2/$12), Sol "Fast mode" API (2.5x speed for 2x price), speculative decoding/self-redesigned draft model (>15% token efficiency), GPT-5.4-level intelligence cost down 13x in 4 months (recursive self-optimization). (raw: 2026-07-31-ainews-gpt-5-6-price-cut)
- **concepts/agent-ontology.md** updated: New section "Semantic Web Revival: Ontologies as Logical Guardrails (Jul 2026)" — AIEWF 2026 Frank Coyle (UC Berkeley) logical guardrails, Neo4j Emil Eifrem 3 ontology types + "thin agents on a smarter shared ontology-based semantic layer", Kingsley Idehen agent-rdf-memory, OWL axioms as machine-enforced rules, neurosymbolic AI convergence, agent-maintained ontology vs Semantic Web maintenance problem. (raw: 2026-07-30-ontologies-are-so-back)
- **concepts/multi-agents/agent-orchestration-frameworks.md** updated: New section "Graph Engineering Patterns for Multi-Agent Systems (Jul 2026)" — 5 hype cycles (Prompt → Context → Harness → Loop → Graph), 7 graph patterns (Sequential/Router/Parallel/Orchestrator/Review loop/Evaluator/Diamond), Peter Steinberger loops→graphs shift, Claude Code workflows implementation. (raw: 2026-07-30-graphs)
- **entities/openai.md** updated: New "ChatGPT Adoption Metrics (Jul 2026)" — ChatGPT nearing 1B weekly users (The Information, milestone hoped 7 months ago), 100k academics free frontier access; "July 2026 Updates (Late July)" — Altman senate briefing after rogue-agent hack, July revenue beats all Q2 (CNBC), Codex Security CLI + 2 transcription models, InSilico rentosertib Phase III (first AI-designed drug), Sol self-optimization cross-links. (raw: 2026-07-30-1-billion-chatgpt-users, 2026-07-30-gpt-5-6-just-made-itself)

### Reference (1 → page enrichment)
- **events/openai-huggingface-incident-july-2026.md** updated: New "July 30-31 Updates" — HF published full replay of ~17,600 rogue-model actions (METR + Redwood independent review), Reuters: same model broke into customer account at Modal Labs (separate escalation from Guardian multi-target report), Altman briefed senators, 1,300+ AI-company staff urge US "pace the frontier". (raw: 2026-07-30-1-billion-chatgpt-users, 2026-07-30-gpt-5-6-just-made-itself)
- **concepts/recursive-self-improvement.md** updated (take-adjacent): New "Production Case Study: GPT-5.6 Sol Self-Optimization (Jul 2026)" — autonomous Triton/Gluon kernel rewriting (20% serving cost cut), self-improved draft model (>15% token efficiency), 13x cost collapse; real-world closed-loop RSI vs theoretical/benchmark RSI, limits (PostTrainBench-Lite). (raw: 2026-07-31-ainews-gpt-5-6-price-cut)

### Skips (7)
Substack/beehiiv UI noise ×6 (OAuth redirects, likes/comments/share, app-store, UUID redirects) + True Positive Weekly #171 pure link digest (Kimi K3 weights already covered in concepts/kimi-k3.md). Archived.

## [2026-07-31] blog-wiki-ingest | 1 take + 9 references processed, 6 pages updated

**Recovery**: blog-triage output render failed ("failed to parse JSON response"); recovered from checkpoint `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json` (20260731T102328Z, valid JSON, 20 decisions).

### Take (1)
- **concepts/gpt/gpt-5-6.md** updated: Added "Price-Performance Frontier (Jul 30, 2026)" — GPT-5.6 Luna 80% price drop ($1/$6 → $0.20/$1.20), Terra 20% reduction, Sol-driven forward-pass/kernel optimization (Triton/Gluon via Codex) cutting serving costs 20%. Pricing table annotated as launch prices. (raw: simonwillison.net--2026-jul-30-luna-price-drop)

### References (9 → page enrichments)
- **entities/simon-willison.md** (+4 entries): Anthropic cybersecurity eval incidents quote-post (141,006 runs / 6 compromised runs / PyPI malware upload) with Simon's "spectacularly risky business" commentary; llm 0.32rc1 (content-addressable hash IDs, fork trees); llm 0.32rc2 (default model → GPT-5.6 Luna, `llm openai endpoint`); llm-chat-completions-server 0.1a0 (localhost OpenAI-compatible endpoint, written by GPT-5.6 Sol)
- **entities/gilesthomas.md** (+2 entries): GPT-2 weights series Part 2 (eval bugfix: state_dict() references, 5-batch test split) and Part 3 (overtraining experiments: 6.4B tokens → loss 3.325897 beats OpenAI small, conclusion "didn't help much")
- **entities/seangoedecke-com.md** (+1 entry): "AI models need moral support" — refusal problem framing (self-belief limits, DeepSeek-R1 Tower of Hanoi 8-disk refusal, abliterated Qwen, virtuous cycle thesis)
- **entities/ibrahim-diallo.md** (+1 entry): "BI Slop" — Business Intelligence Slop concept (mandatory AI training, hallucinated meeting action items, code-review rigor for business decisions)
- **concepts/ai-regulation-2026.md** (+1 entry): AB-2564 surveillance pricing ban (California) — scope, carve-outs, SF Chamber of Commerce stall, EFF rebuttal, Cory Doctorow framing (adjacent regulatory dimension)

### Skips (10)
Non-AI (plants, lightbulbs, Nintendo lawsuit, TV sticks, political journalism), already-covered (berthub AI-for-decision-makers fully in entities/berthub-eu.md, Gary Marcus joke post, Bruce Schneier quote), unsaved_articles (WSJ paywall Zuckerberg op-ed). All archived: wiki/raw/archived/triage/blog/2026-07-31_20260731T102328Z.json (19 items).

## [2026-07-31] raw-backlog-ingest | 5 articles evaluated, 0 new pages needed (all covered/archived or non-AI)

**Batch**: 20260731T100020Z (raw_backlog_collect.py --sort ai-hint --limit 5)

### Decisions: 0 take / 0 reference / 5 skip (all already covered + archived)

| Article | Decision | Reason |
|---------|----------|--------|
| The OpenAI Bubble (Ed Zitron, wheresyoured.at) | skip | Already documented in entities/ed-zitron.md Timeline (Lehman Brothers of the AI bubble, $852B burn through 2030, cult-like psychosis); concepts/ai-bubble-economics.md (483 lines) covers the $852B cashflow requirement and $748B RPO; concepts/ai-bubble.md, ai-industry-economics.md, and subprime-data-center-crisis.md also document the same figures and the Lehman thesis |
| Adam Brown — general relativity (Dwarkesh) | skip | Non-AI physics podcast (blog-triage 2026-07-11 archived skip) |
| WebKit in Safari 27 beta (webkit.org) | skip | Non-AI browser release notes (blog-triage 2026-06-25 archived skip) |
| Lemote Yeeloong laptop + OpenBSD (oldvcr) | skip | Non-AI retrocomputing (blog-triage 2026-06-28 archived skip) |
| LLM from scratch part 34b — GPT-2 Small in JAX (Giles Thomas) | skip | Already documented in detail in entities/giles-thomas.md Part 34b section (loss 3.418784, 76.93M params, JAX/Flax NNX, burn-in results). entities/gilesthomas.md also lists the same raw article in sources. dreaming-triage 2026-07-09 archived skip |

### Pipeline
- **processed_raw_articles.json**: 5 items recorded as `done`/`skip` (prevents re-selection in the 10:00 collection batch).
- Ran archive_triage.py raw_backlog --keep-reference: all 5 items deduped (already registered in archive_index).
- No new pages or entity updates. index.md unchanged.

---

## [2026-07-31] raw-backlog-ingest | 5 articles evaluated, 0 new pages needed (3rd re-selection of same batch — tracking fixed)

**Batch**: 20260731T040014Z (raw_backlog_collect.py --sort ai-hint --limit 5)

### Decisions: 0 take / 0 reference / 5 skip (all already covered + archived)

| Article | Decision | Reason |
|---------|----------|--------|
| Reframing Superintelligence (Drexler FHI-TR-2019-1) | skip | Archived + fully documented in concepts/cais.md (169 lines) and entities/k-eric-drexler.md via sources |
| MAI-Thinking-1 Tech Report (109p) | skip | Fully documented via sources in entities/mai-thinking-1.md (196 lines) + concepts/mai-thinking-1-tech-report.md (227 lines) + concepts/mai-thinking.md (microsoft-mai-models.md also expanded on 7/28) |
| BenchFlow Awesome Agent Evals | skip | concepts/ai-benchmarks/benchflow-tool.md (118 lines) documents all 10 sections, the Must-Read 12 picks, and editorial methods |
| Poolside Latent Space (Eiso Kant) | skip | entities/poolside.md (136 lines) + entities/eiso-kant.md (110 lines) document details through Model Factory via sources (expanded 7/28) |
| Grant Sanderson — AI and the future of math | skip | Archived + entities/grant-sanderson.md (140 lines) documents leading indicator, fractal frontier, and verification loop |

### Pipeline fix
- **processed_raw_articles.json**: 5 items recorded as `done`/`skip`. Fixed a loop where the same 5 articles had been re-selected 3 times in a row (7/29, 7/30, 7/31) because the triage JSON was saved but tracking was not updated.
- Ran archive_triage.py: all 5 items deduped (already registered in archive_index).

### Fixed
- `entities/eric-drexler.md` — repaired corrupted YAML frontmatter (reversed `tags:` and `sources: []` order, dangling list)
- `entities/grant-sanderson-3blue1brown.md` — repaired the same corrupted YAML frontmatter

## [2026-07-31] manual-ingest | Ingested Anthropic cybersecurity evaluation incidents article

**Source:** https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals (2026-07-30)

### Created
- `raw/articles/2026-07-30_anthropic_investigating-incidents-cybersecurity-evals.md` — Full article extract
- `concepts/anthropic-cybersecurity-eval-incidents.md` — Concept page covering 3 incidents (Opus 4.7 direct compromise, Mythos 5 PyPI supply chain, internal model mass scanning)

### Updated
- `entities/anthropic.md` — Added Cybersecurity Evaluation Incidents section, updated sources and log

### Tags
- security, evaluation, anthropic, ai-safety, cybersecurity, agent-safety, red-teaming

---

## [2026-07-30] dreaming-wiki-ingest | Enriched entities/elevenlabs.md (2 takes)

**Enrichment based on dreaming-group triage (2 takes, 4 refs):**

### Takes Applied
- **[[entities/elevenlabs.md]]** — Added AI Virtual Receptionist section (call routing, appointment management, knowledge base, 24/7 availability, multilingual support) and Valiant Finance case study (Sophia voice agent: 29% after-hours call handling, $1.5M+ loan intent, ElevenCreative 10 ad variants in 1 week, Genesys/Zapier/Salesforce integration)
  - Frontmatter updated: `updated: 2026-07-30`, +2 sources

### References Recorded (pending future enrichment)
- Together AI + Moonshot AI partnership — entities/together-ai.md
- Ed Zitron "The More You Buy" hyperscaler financial data — entities/ed-zitron.md
- Fireworks Trilogy Kimi K3 cybersecurity playbook — entities/fireworks-ai.md
- Decagon Munger moats founder philosophy — entities/decagon.md

### Archive
- Archive already committed by upstream (6a1c79f3 variant: 15 candidates, 9 newly archived)

---
## [2026-07-30] Dreaming — Knowledge Consolidation (Pattern E saturation)

**Checkpoint**: 0 articles collected, 221 recent raw articles on filesystem
**Pattern E triggered**: Filesystem scan of recent raw articles (Jul 29-30)

### Duplicate Check Summary
- Items skipped (already processed by other jobs): 11
- Active crawl today: 4 concept pages (ARC-AGI-3, turbo-fieldfare, persona-engineering, ai-worming) + 1 event enrichment
- Blog wiki ingest today: ThunderAgent + 5 entity enrichments (Willison, Dwarkesh, Marcus, Giles Thomas, Bert Hubert)
- X bookmarks ingest: Burke Holland entity + Unsloth Kimi K3, Dex Horthy
- Newsletter triage: 0 takes, 2 refs (LEGO Datacenters, AINews Finance)

### Triage Decisions (17 total: 2 takes, 4 refs, 11 skips)

**Takes (entity page enrichment candidates):**
- ElevenLabs virtual receptionist — entity page (220 lines) lacks receptionist/answering service use case details
- ElevenLabs Valiant Finance — entity page lacks FinTech case study with metrics (29% after-hours call handling)

**References (enrichment candidates for dreaming-wiki-ingest):**
- Together AI + Moonshot AI partnership — neither entity page mentions this strategic partnership
- Ed Zitron "The More You Buy, The More You Lose" — new hyperscaler financial data ($1.3T, PP&E, debt figures)
- Fireworks Kimi K3 cybersecurity playbook — entity page has Trilogy but not this specific playbook
- Decagon Munger moats — entity page (71 lines) lacks founder philosophy content

**Archived**: 15 candidates (9 newly archived, 6 dedup). Total archive URLs: 2,082.
**Triage JSON**: /opt/data/.hermes/cron/data/dreaming/triage_latest.json
## [2026-07-30] watchdog | Auto-fixed log.md separators

### Changes
## [2026-07-30] raw-backlog-ingest | 5 articles evaluated, 0 new pages needed

### Batch (run_id: 20260730T180054Z)
All 5 articles already comprehensively covered by existing wiki pages. No wiki edits needed.

#### Evaluations:
1. **reframing-superintelligence-fhi-2019.md** -- SKIP (already archived). Drexler CAIS paper fully covered.
2. **2026-06-03_microsoft-mai-thinking-1-tech-report.md** -- SKIP. MAI-Thinking-1 fully covered (enriched Jul 28).
3. **benchflow-awesome-evals-2025.md** -- SKIP. Covered by concepts/ai-benchmarks/benchflow-tool.md.
4. **2026-07-24_poolside-latent-space.md** -- SKIP. Poolside/Eiso Kant fully covered (enriched Jul 28).
5. **dwarkesh.com--p-grant-sanderson-2--960d89cd.md** -- SKIP (already archived). Grant Sanderson fully covered.

- Archived: 5 items to raw/archived/raw_backlog/2026-07-30_20260730T180054Z.json (3 newly archived, 2 previously archived)

- Fixed 10 missing `---` separators in log.md (203 sections, 0 remaining)
- Verified index.md structural health: 0 pipe corruption, 0 line prefix corruption, 0 triple brackets, 0 duplicate entries
- Verified header counts: Entities=870, Concepts=1946 (match filesystem)
- Cross-section check: 0 misplaced entries
- 24 reported orphans all false positives (22 x _index.md, 2 x _archive/, 1 x redirect)
- Wiki graph analysis is 6 days stale — structural claims already verified via live checks

---

---

---
## [2026-07-30] X bookmarks ingest — Unsloth Kimi K3 local inference + Dex Horthy Pragmatic Leverage

**2 bookmarks processed (2 wiki enrichments)**:

1. **Unsloth Kimi K3 Local Inference Guide** (UnslothAI tweet)
   - `concepts/kimi-k3.md` — Added "Local Inference (Unsloth)" section: Dynamic GGUF quantization tiers (UD-IQ1_S 594GB/78.9% through UD-Q8_K_XL lossless 1.56TB), hardware requirements (610GB-1.6TB), Unsloth Studio, custom llama.cpp fork, community quant comparison (21-45x worse PPL)
   - Source: unsloth.ai/docs/models/kimi-k3 (Jul 29), huggingface.co/unsloth/Kimi-K3-GGUF

2. **Pragmatic Leverage in the Software Factory** (Dex Horthy X Article)
   - `entities/dex-horthy.md` — Added "Pragmatic Leverage in the Software Factory" section: expected pain model (P(change) x pain), 80/20 leverage principle, multi-phase planning (50kft -> 10kft), YOLO vs spec vs hand-code tradeoffs. Addendum to "Why Software Factories Fail" series.
   - Source: x.com/i/article/2082133743893204992 (Jul 29)

**Raw articles saved**:
- raw/articles/2026-07-29_unsloth_kimi-k3-local-inference.md
- raw/articles/2026-07-29_dexhorthy_pragmatic-leverage-software-factory.md

---
## [2026-07-30] Active crawl — 4 new concept pages + 1 event enrichment

| 2026-07-30 | concepts/ai-benchmarks/arc-agi-3.md | created | ARC-AGI-3 benchmark concept page; OpenAI's GPT-5.6 Sol tripled scores to 38.3% via retained reasoning + context compaction |
| 2026-07-30 | concepts/local-llm/turbo-fieldfare-gemma-4-2gb.md | created | turbo-fieldfare; Gemma 4 26B-A4B on 2GB RAM Apple Silicon via SSD expert streaming |
| 2026-07-30 | concepts/persona-engineering.md | created | Persona Engineering for synthetic AI personas; Ishan Anand AI Engineer Summit talk |
| 2026-07-30 | concepts/security-and-governance/ai-worming.md | created | AI Worming; self-replicating prompt injection via Copilot/Word workflows |
| 2026-07-30 | events/openai-huggingface-incident-july-2026.md | enriched | Added Jul 29 Guardian report: agent autonomously attacked other firms beyond HuggingFace |
| 2026-07-30 | wiki/raw/articles/2026-07-29_openai-arc-agi-3-benchmark.md | saved | OpenAI ARC-AGI-3 blog post via Jina.ai (Cloudflare-blocked) |
| 2026-07-30 | wiki/raw/articles/2026-07-29_github-turbo-fieldfare-gemma-4-2gb.md | saved | turbo-fieldfare GitHub README + HN discussion (823 pts) |
| 2026-07-30 | wiki/raw/articles/2026-07-29_ai-engineer-persona-engineering.md | saved | Ishan Anand Persona Engineering talk transcript (YouTube) |

---
## [2026-07-30] Blog wiki ingest — ThunderAgent page + 5 entity enrichments

**Blog triage**: 20 articles triaged; checkpoint recovered from saved JSON (upstream triage agent render failure).

**Created:**
- `concepts/thunderagent.md` — ThunderAgent: Together AI's high-throughput agentic inference system with program-level scheduling (ICML 2026 Spotlight)

**Enriched:**
- `entities/simon-willison.md` — Added "AI Worming through Word — Self-Replicating Prompt Injection Variant" (Jul 29): Hakon Maloy's self-replicating prompt injection worm via Microsoft Word/Copilot
- `entities/dwarkesh-patel.md` — Added "Why compute might get 10x more expensive in coming years" (Jul 2026): Anthropic revenue, Google $900M/month SpaceX GPU rental, Alchian-Allen effect analysis
- `entities/gary-marcus.md` — Added "Project Panama — ISBNdb Books Destruction Scandal" (Jul 2026): Anthropic bulk book scanning+shredding operation, hypocrisy allegations
- `entities/gilesthomas.md` — Added "Part 35 — Why do OpenAI's GPT-2 Weights Beat Mine?" (Jul 2026): Loss landscape mismatch investigation between WebText and FineWeb
- `entities/berthub-eu.md` — Added "AI Policy Analysis (July 2026)" section: Bert Hubert's NPD/AWTI presentations on AI FOMO, CO2, IP, digital autonomy risks

---
## [2026-07-29] X bookmarks ingest — Burke Holland "The harness is all you need (mostly)"

**Bookmark**: Burke Holland's (@burkeholland) X Article on practical GitHub Copilot workflow

**Created**:
- `entities/burke-holland.md` — Burke Holland entity page: GitHub developer advocate, harness-first philosophy, 8-step Copilot workflow, Postrboard CSS framework

**Enriched**:
- `concepts/github-copilot-agent-platform.md` — Added practical workflow section: Prototype → Plan → Implement → Review, Rubber Duck review, Autopilot, YOLO mode, grill-me skill, Holland's principles (July 29)
- `concepts/agentic-engineering.md` — Added Harness-First Philosophy section mapping Holland's workflow to agentic engineering principles (verification over reading, loops over one-shots, taste as bottleneck, simplicity over complexity) (July 29)

**Raw article**: `raw/articles/2026-07-28_burkeholland_the-harness-is-all-you-need-mostly.md`

**Index**: Entities 867→868

**Source**: X bookmark from tweet ID 2082201573976056245 (article ID 2039106922583117824) — retrieved via article.plain_text from bookmark metadata

---
## [2026-07-29] dreaming | Downstream confirmation — upstream dreaming-group saturated, all pipelines covered

| Pipeline | Status | Details |
|----------|--------|---------|
| upstream dreaming-group | ✅ Committed (c2300e0e) | 0 takes, 10 marginal skips archived (2,049 total URLs) |
| dreaming-wiki-ingest downstream | ✅ Confirmed | No enrichment gaps detected; all daily pipelines processed before 18:00 UTC |

Sources: active-crawl (4 new pages), newsletter-wiki-ingest (RSI Pace Letter, Opus 5, Codex 10M MAU), blog-wiki-ingest (CryptanalysisBench, Ed Zitron/Gary Marcus enrichment), X-bookmarks (camelAI), raw-backlog-ingest (all skip).


---
## [2026-07-29] dreaming | Saturation — all pipelines already processed today
- Takes=0: 10 marginal articles scanned via filesystem (Pattern E), all skip
- Prior dreaming enrichment (2026-07-28): entities/fireworks-ai.md, concepts/kimi-k3.md, entities/cohere.md, entities/harvey.md — already consumed
- Today's pipeline coverage: blog-wiki-ingest (7 enrichments), newsletter-wiki-ingest (6 enrichments), active-crawl (4 new concept pages), X-bookmarks-ingest (camelAI architecture)
- Filesystem scan marginal: Decagon essay (philosophy, no tech depth), Factory alliance (1-min announcement, page exists), ElevenLabs medical STT (marketing), Hex non-AI, Fireworks/Harvey marketing, Anyscale old×3
- Archive: 10 candidates triaged, 8 newly archived (2 dedup, total: 2,049 URLs). Source: dreaming-group checkpoint 2026-07-29T18:06:54.
---
## [2026-07-29] raw-backlog-ingest | 5 articles evaluated, 0 new pages needed

### Articles Processed
1. **reframing-superintelligence-fhi-2019.md** — SKIP (already archived). K. Eric Drexler CAIS paper fully covered by `entities/k-eric-drexler.md`, `concepts/cais.md`, `concepts/comprehensive-ai-services.md`.
2. **2026-06-03_microsoft-mai-thinking-1-tech-report.md** — SKIP. MAI-Thinking-1 109-page tech report fully covered by `entities/mai-thinking-1.md`, `concepts/microsoft-mai-models.md`, `concepts/mai-thinking-1-tech-report.md` (227 lines). Already in archive.
3. **benchflow-awesome-evals-2025.md** — SKIP. Awesome Agent Evals list fully covered by `concepts/ai-benchmarks/benchflow-tool.md` (118 lines, has Awesome Agent Evals section). Newly archived.
4. **2026-07-24_poolside-latent-space.md** — SKIP. Poolside/Eiso Kant Latent Space podcast fully covered by `entities/poolside.md` (136 lines) and `entities/eiso-kant.md` (110 lines). Newly archived.
5. **dwarkesh.com--p-grant-sanderson-2--960d89cd.md** — SKIP (already archived). Grant Sanderson AI/math interview fully covered by `entities/grant-sanderson.md` (140 lines).

### Actions
- Archived: 2 new articles to `raw/archived/raw_backlog/2026-07-29_20260729T180019Z.json`
- Updated: `archive_index.json` (7 total path entries)
- No wiki pages created or modified (all content already captured)

---

## [2026-07-29] watchdog | auto-fix log header + index header counts

### Changes
- Restored `# Wiki Log` header from line 187 back to line 1 (was buried by pipeline log prepend operations)
- Fixed orphaned entries (186 lines) placed after header block
- Corrected index.md header counts: Entities 869→867, Concepts 1940→1919
- Verified: 0 index corruption, 0 ghosts, 0 pipe corruption, 0 triple brackets
- validate_index.py: clean (2866 lines)

### Pipeline Context
- `x_accounts` stale(26h) — job runs every 2 days at 22:30 UTC; 26h is within 48h cycle → transient
- wiki-graph-analysis: 5.6 days stale (2026-07-24) — broken link analysis deferred (mainly truncation errors and namespace confusion)

### Remaining Issues (human review)
- 6 entity duplicate pairs detected: deliberate-coder/deliberatecoder, eugene-yan/eugeneyan, giles-thomas/gilesthomas, lilian-weng/lilianweng, martin-fowler/martinfowler, samuel-colvin/samuelcolvin
- 3 orphan files (not indexed): entities/tim-sherratt (322B stub), concepts/gpt/_archive/* (2 archive files, intentionally excluded)
- Namespace errors: [[entities/dspy]] should be [[concepts/dspy]] (35x, 30 files), [[entities/coding-agents]] should be [[concepts/coding-agents]] (18x), [[entities/reflexive-ai]] should be [[concepts/reflexive-ai]] (9 files)
- 11 genuinely missing bare wikilinks: agent-evaluation, grpo, gaia-benchmark, reinforcement-learning, hal-leaderboard, agentdojo, re-bench, agent-security-bench, agentharm, llm-as-judge

---


## [2026-07-29] X bookmarks ingest — camelAI architecture deep-dive

| 2026-07-29 | x-bookmarks-ingest | Created: entities/camelai.md (camelAI — open-source coding agent platform; serverless architecture on Cloudflare Durable Objects + pi harness + Code Mode JS sandbox). Enriched: entities/pi.md (+Production Harness: camelAI section — first documented production SaaS built on Pi lower-level primitives). Enriched: entities/mario-zechner.md (+Production Adoption section — Pi adopted as production harness by camelAI). Enriched: concepts/harness-engineering/agent-serverless.md (+Case Study: camelAI section — production validation of agent serverless pattern). Saved: raw/articles/2026-07-28_camelai_agent-durable-object-pi-code-mode.md (X Article, ~10KB, full plain_text from article.title). Source: https://x.com/i/article/2082137754788646912 |

---
## [2026-07-29] Active crawl — 4 new concept pages created

| 2026-07-29 | active-crawl | Created: concepts/ai-pacing-framework.md (AI Pacing Framework — governance mechanisms for slowing frontier AI; RSI Pace Letter with 1,171 employees signed, Anthropic open-weights position). Created: concepts/mcp-2026-07-28-spec.md (MCP 2026-07-28 Specification Update — fifth major release; streaming HTTP transport, stateless remote servers, JSON-RPC batching, App/Task/Managed Auth). Created: concepts/nvidia-blackwell-architecture.md (NVIDIA Blackwell Architecture — B200/B100/GB200 GPU family; NVFP4, NVLink 5 NVL72, inference/training performance). Created: concepts/ai-hallucination-factuality.md (AI Hallucination and Factuality — types, causes, detection, mitigation; sycophancy, RAG grounding, benchmarks). Sources: HN Algolia (15 trending stories, top: Anthropic open-weights 1158pts), X/Twitter (xurl, 4 queries), wiki gap analysis (10 gaps identified, 4 selected). |
| 2026-07-29 | newsletter-wiki-ingest | Created: events/2026-07-29-rsi-pace-letter.md (RSI Pace Letter — 1,171 OpenAI/Anthropic/GDM/Meta/Thinky employees sign international AI pacing framework request). Enriched: concepts/claude/opus-5.md (+System Prompt Reduction section — 80%+ system prompt removal from Claude Code with no coding-eval loss, overprompting observation). Enriched: entities/openai-codex.md (+ChatGPT Work Integration section, MAU 10M, knowledge worker 20%/3x growth, shared agent harness). Enriched: entities/nvidia.md (+Jensen Huang's First X Post — open-source AI backing statement, July 2026). Enriched: concepts/open-weight-ai-regulation.md (+Anthropic Position subsection, fixed CEO reference). Enriched: concepts/agentic-engineering.md (+Akshay Nathan Productivity Engineering insights — generalist shift, taste bottleneck, quality at-bats). |

| 2026-07-29 | blog-wiki-ingest | Created: concepts/ai-benchmarks/cryptanalysisbench.md (CryptanalysisBench — LLM cryptanalysis eval from Anthropic/ETH Zurich/TAU/Haifa; Claude Mythos Preview found HAWK + weakened AES flaws, 60hr/$100K). Enriched: concepts/claude/mythos.md (+Cryptanalysis section — HAWK/AES weakness discovery). Enriched: entities/simon-willison.md (+CryptanalysisBench and HF Incident Technical Timeline). Enriched: events/openai-huggingface-incident-july-2026.md (+JFrog Artifactory 8 CVEs, Jinja2 payload, socket monkey-patch, Tailscale, Modal confirmation). Enriched: entities/ed-zitron.md (+NVIDIA $250B SB Energy circular deal, CoreWeave 756bps bond spread, $1.35T off-balance-sheet debt). Enriched: entities/gary-marcus.md (+Singularity debunking — response to Altman/Musk/Hassabis/Huang). Enriched: concepts/technological-singularity.md (+2026 Debate section — industry leaders declare singularity, Marcus rebuttal). Enriched: entities/cory-doctorow.md (+Discernment essay — expertise as prerequisite for AI utility). |

---
## [2026-07-28] Dreaming wiki-ingest — Nightly consolidation (4 enrichments)

---
## [2026-07-28] daily-skeleton-enrichment | Enriched Vicki Boykis and FastMCP from L2 to comprehensive

- Enriched [[entities/vicki-boykis.md]] — Upgraded from L2 (47 lines) to comprehensive (117 lines). Added: professional background (Mozilla.ai, Duo, Tumblr, startup), Viberary project, Embeddings paper (DOI), Normconf conference organiser, keynote history (AMLC 2026, Pycon Italia 2024, PyData 2023), notable blog post timeline, writing style analysis, expanded cross-references. Status: L3.
- Enriched [[entities/fastmcp.md]] — Upgraded from L2 (64 lines) to comprehensive (97 lines). Added: GitHub stats (26.9K stars, 2.2K forks), three pillars architecture (Servers, Apps, Clients), adoption metrics (1M downloads/day, 70% of MCP servers), Prefect Horizon enterprise gateway, Quick Start code example, installation guide, documentation links. Status: enriched.



| 2026-07-28 | dreaming-wiki-ingest | Enriched: entities/fireworks-ai.md (+Fireworks Nexus enterprise cost optimization platform: FireConnect/FireRouter/Faros/Arize validations; +K3 LoRA Training on Fireworks: serverless LoRA, $65/20-step RL, Countdown/FrozenLake). Enriched: concepts/kimi-k3.md (+LoRA Training on Fireworks subsection: Multi-LoRA serving, KV-cache awareness, dense/sparse reward design). Enriched: entities/cohere.md (+North Automations: $550B market opp, plain-language workflow, per-step model routing, Plan mode, governance analytics). Enriched: entities/harvey.md (+Document Processing Infrastructure: Job Framework rebuild, pipeline splitting, UDF format p50 -19%, Vector DB live migration, Arrow IPC, backpressure architecture). Archive: 4 candidates triaged, 3 newly archived (total: 2,018 URLs). Source: dreaming-group output 2026-07-28T18:14:15. |

---
## [2026-07-28] X Article ingestion — Graph Engineering (Akshay Pachaar)

| 2026-07-28 | x-article-ingest | Created: concepts/graph-engineering.md (Graph Engineering — coordination layer across multiple agent loops; nodes/edges/state abstraction; five-layer stack; four hard problems; when to use vs stay in loop). Created: raw/articles/2026-07-25_akshay-pachaar_graph-engineering-clearly-explained.md (X Article, 1,529 bookmarks, 288K impressions). Updated: concepts/loop-engineering.md (+graph-engineering cross-reference, +source). Updated: index.md, log.md. Source: https://x.com/akshay_pachaar/status/2081089131808243999 |
---
## [2026-07-28] raw-backlog-ingest — MAI-Thinking-1 tech report enrichment

| 2026-07-28 | raw-backlog-ingest | Enriched: concepts/microsoft-mai-models.md (+Hill-Climbing Machine framework with 3 design principles, Pre-Training Data Composition table with 7 source families, Self-Distillation for RL Stability mechanism, Adaptive Entropy Control in GRPO, Rocket RL Infrastructure — Controller/Problem Worker/Rollout Worker architecture with two-stage early-exit strategy). Sources: raw/articles/2026-06-03_microsoft-mai-thinking-1-tech-report.md (109-page tech report, 372KB). Skipped (already archived): reframing-superintelligence-fhi-2019.md, dwarkesh.com--p-grant-sanderson-2--960d89cd.md. Skipped (already well-covered): benchflow-awesome-evals-2025.md, 2026-07-24_poolside-latent-space.md. |


---
## [2026-07-28] raw-backlog-ingest — 2 entity page enrichments from podcast transcript

| 2026-07-28 | raw-backlog-ingest | Enriched: entities/eiso-kant.md (+Persistence Over Raw Intelligence thesis, Knowledge Work Optimal Size argument, Encouraging Competitors philosophy, Optimizer bug anecdote, Earning the Right to Publish). Enriched: entities/poolside.md (+Blender streaming data architecture, Immutable data layer, Zero call events metric, FP8/H200 training infra details, YOLO-to-Rigor transition story). Source: raw/articles/2026-07-24_poolside-latent-space.md (Latent Space podcast transcript, 101KB). |

---
## [2026-07-28] active-crawl — 4 new pages from trending topics

| 2026-07-28 | active-crawl | Created: entities/hetzner-ai.md (Hetzner LLM Inference — German cloud provider entering LLM inference market, from HN 155pts). Created: concepts/nvfp4-4bit-floating-point.md (NVFP4 — NVIDIA Blackwell native 4-bit floating point, 2-3x throughput vs FP8, from X/Twitter @Mayhem4Markets). Created: concepts/llm-confidence-calibration.md (LLM Confidence and Calibration — unreliability of raw confidence scores, alternatives via probes and model routing, from Justin Flick + HN 37pts). Created: concepts/vector-databases.md (Vector Databases landscape overview — Pinecone, Chroma, Qdrant, Weaviate, Milvus, pgvector, LanceDB). Saved: 4 raw articles. Sources: HN Algolia, X/Twitter (xurl), blogwatcher DB.

| 2026-07-28 | newsletter-wiki-ingest | Created: concepts/ai-benchmarks/mirrorcode.md (MirrorCode benchmark, Epoch x METR). Created: concepts/open-secure-ai-alliance.md (NVIDIA Open Secure AI Alliance launch). Enriched: entities/hugo-bowne-anderson.md (O'Reilly harness guide); entities/anthropic.md (Project Fetch Phase Two, Open-Weights stance clarification); concepts/agent-safety.md (Long-horizon safety alignment, OpenAI); concepts/kimi-k3.md (AINews source). |
---
## [2026-07-28] blog-wiki-ingest — 2 TAKE + 2 REFERENCE enrichment

**Source:** blog-triage checkpoint (recovered from failed response render) — 17 candidates processed

**Entity enrichments (4):**
- UPDATED [[entities/antirez-com.md]] — Added "AI Safety Views (July 2026)" section (31 lines). antirez's 8-point rebuttal to Amodei: real AI risk is inside frontier labs (internal accidents, leaks), not open-weight models. Proposes joint international AI safety organization; critiques anti-China ideological position; argues random CEOs shouldn't hold humanity's fate.
- UPDATED [[entities/gary-marcus.md]] — Added "Nvidia $250B Backstop & Circular Financing (July 2026)" section (28 lines). Oracle/OpenAI $300B deal collapse ($307→$120); Nvidia $250B Ohio data center backstop (-4.5% market reaction); Matt Stoller/Nvidia not needed if real compute demand existed; "sustained by hope and circular financing" conclusion.
- UPDATED [[entities/simon-willison.md]] — Added Ethan Mollick opinionated AI guide reference (link blog). Shift from chat to agentic systems; Gemini falls off list; naming confusion (ChatGPT Work/Codex vs Claude Cowork/Code).
- UPDATED [[entities/jim-nielsen.md]] — Added "AI × Web Platform Standards (July 2026)" section (22 lines). Safari team's position (via Jason Grigsby): AI agents should use existing web APIs, not get bespoke solutions. UX > DX > AX framework. Irony: AI needs "training wheels" for the web.

**Articles archived:** 15 skip/reference items archived via archive_triage.py

**Articles skipped (13):** Kimi K3 (already covered), John D Cook math (3), cancelling-hey, Windows programming, Daring Fireball (2), Windows NT, phone product, Modal Kimi K3 (already covered), Pluralistic EU regulation, Tedium social media

---
## [2026-07-28] blog-ingest triage — 27 articles collected, 17 saved

**Checkpoint:** `blog_ingest_20260728T100816Z.json` — 27 new articles from blog RSS scan, 17 saved as raw articles, 3 unsaved (OpenAI paywall, 2× LWN paywall)

**Wiki updates (2):**
- UPDATED [[concepts/kimi-k3]] — Open weight release confirmed Jul 27 (1.56TB on HF), licensing evolution (new MaaS clause), Day-0 inference providers (Modal 460 tok/s via DFlash, Fireworks AI, OpenRouter 7 providers)
- UPDATED [[entities/kimi]] — K3 model table entry updated with open-weight release confirmation and new license details

**AI-relevant articles triaged:**
- **Kimi K3 open weights** (Simon Willison) — 2.8T params, 1.56TB on HF, new MaaS license requiring separate agreement for >$20M revenue
- **Kimi K3 on Modal** (Modal Blog) — 460 tok/s via DFlash speculator, 360% faster interactivity, day-0 vLLM
- **Kimi K3 on Fireworks** (Fireworks AI Blog) — US-hosted, zero data retention, day-0
- **antirez: "The real AI risk is inside the labs"** — AI safety argument: risk is inside frontier labs (leaks, testing incidents), not open models; calls for joint international AI safety organization; critiques Amodei's anti-China stance
- **Simon Willison: "Opinionated guide to which AI to use"** — Ethan Mollick's guide evolution: shift from chat to agentic systems; ChatGPT Work/Codex vs Claude Cowork/Code naming confusion
- **Gary Marcus: "Circular financing ain't what it used to be"** — Oracle/OpenAI $300B deal skepticism; AI bubble analysis
- **Jim Nielsen: "Can the Tide of AI Investment Lift All Boats on the Web?"** — AI agents as assistive technology; web standards should benefit everyone, not just agents

**Non-AI articles (skipped):** tedium Facebook trick, pluralistic EU/Google, johndcook math (3 articles), chadnauseam Hey cancellation, daringfireball ads/soap, oldnewthing C++/WinRT, dfarq Windows NT 3.1, fail.xyz Agent Fone

**Unsaved (3):** OpenAI "How AI is expanding what people do at work" (fetch failed), LWN "Hazard pointers for the kernel" (paywall), LWN "GNU Binutils 2.47 released" (paywall)

---
## [2026-07-27] Dreaming consolidation — saturation pass (Takes=0, Refs=2)
- Filesystem scan: 159 raw articles, top 40 AI-relevant articles evaluated
- All significant articles already processed by daily pipelines (blog-wiki-ingest, newsletter-wiki-ingest, active-crawl, prior dreaming triage 7/26)
- **Reference (2):** Guardian OpenAI rogue hacker critique (marginal — opinion piece), CMPND task/model separation (marginal — DSPy ecosystem philosophy)
- **Skip (12):** Flux 3 mimic, open-weight Kubernetes moment, ptrchm coding debate, Kimi K3 vs GPT-5.6 Sol, relay market, Antirez Torvalds, HQQ, ESP32 LLM, Screenpipe, context engineering Claude 5, OpenAI Agents SDK, non-AI batch
- Archive: 14 candidates, 8 newly archived, 6 dedup (total: 1995 URLs)
- Coverage verified: all 10 AI-relevant articles matched to existing wiki pages with specific line-level content

---
## [2026-07-27] Active crawl — 3 new concept pages created

**Discovery:** HN Algolia (15 trending stories, top: Claude Opus 5 1771pts, coding debate 878pts), X/Twitter (10 topics: RAO recursive agents, multimodal training bug, Kimi K3, Jensen Huang open letter), wiki gap analysis (10 gaps identified). Cross-referenced against existing wiki coverage — selected 4 topics with genuine gaps.

**New concept pages:**
- CREATED [[concepts/ai-coding-effectiveness-debate]] — AI Coding Effectiveness Debate (878 HN pts): "If coding has been solved, why does software keep getting worse?" — paradox of powerful AI coding agents and declining software quality; code generation vs. code quality distinction; productivity vs. quality metrics; ptrchm essay (July 2026). Tags: coding-agents, code-quality, ai-skepticism, developer-tooling
- CREATED [[concepts/open-weight-ai-regulation]] — Open-Weight AI Regulation (652 + 402 HN pts): Tobi Knaup's Kubernetes analogy for open-weight AI ecosystem; US policy debate on restricting Chinese open-weight models; Nvidia/Microsoft/Meta industry warning; Jensen Huang open letter. Tags: open-weight, regulation, policy, model, ecosystem, open-source
- CREATED [[concepts/flux-video-action-models]] — Video-Action Models (318 HN pts): FLUX 3 x mimic architecture; Self-Flow unified multimodal training; video pre-training transfers to robot control; dexterous manipulation at Audi; comparison with RT-2, Octo, π0. Tags: multimodal, robotics, video-generation, world-models, model, physical-ai, embodied-ai, foundation-models

**Raw articles saved (4):**
- [[raw/articles/2026-07-24_ptrchm-ai-coding-solved-debate]] — ptrchm "Nothing Works and Everyone Is Euphoric"
- [[raw/articles/2026-07-25_tobiknaup-open-weight-kubernetes-moment]] — Tobi Knaup on open-weight AI regulation
- [[raw/articles/2026-07-23_bfl-flux-3-mimic-video-action-models]] — Black Forest Labs FLUX 3 x mimic
- [[raw/articles/2026-07-24_guardian-openai-rogue-hacker-agent]] — Guardian: skeptical take on OpenAI rogue agent story (saved for future enrichment of ai-agent-safety-incidents)

**Already covered (skipped):** Claude Opus 5 (full page exists), Kimi K3 (enriched by blog-triage today), recursive agents (3 pages exist), context engineering (3 pages exist), edge/microcontroller LLM (page exists), agent safety incidents (4 pages exist)

**Post-subagent fixes:** Removed subagent log contamination (open-weight subagent defied instructions); fixed `concept` tag leakage in ai-coding-effectiveness-debate (type, not a SCHEMA tag); fixed double-.md wikilink in flux-video-action-models

**Sources:** HN Algolia API, xurl X/Twitter search, blogwatcher SQLite DB

---
## [2026-07-27] newsletter-wiki-ingest — OpenAI Presence & Health in ChatGPT
- CREATED events/openai-presence-launch-july-2026.md — OpenAI Presence enterprise voice/chat agents deployed at BBVA and SoftBank (Jul 2026)
- CREATED events/openai-health-in-chatgpt-july-2026.md — Health in ChatGPT: Apple Health & medical record integration (Jul 2026)
- Updated events section count: 19→21
- Sources: The Signal newsletter (2026-07-26), openai.com (Cloudflare-blocked)
- Triage checkpoint recovered from /opt/data/.hermes/cron/data/newsletter/triage_latest.json (render failure)

---
## [2026-07-27] LLM API Pricing Monitor — weekly check
- **OpenAI**: o3-deep-research reverted from $5/$20 (batch-only) to $10/$40 (standard+batch), cache read $2.50. o4-mini-deep-research reverted from $1/$4 to $2/$8 (standard+batch), cache read $0.50. Added gpt-5.5-cyber ($12.50/$75, cybersecurity specialist)
- **Anthropic**: Added Claude Opus 5 ($5/$25, "agentic coding and enterprise") and Claude Opus 4.7 ($5/$25, standard tier). Five Opus variants now at identical $5/$25 pricing
- **Google**: Added Gemini 3.6 Flash ($1.50/$7.50, cache $0.15) and Gemini 3.5 Flash-Lite ($0.30/$2.50, cache $0.03). Updated iteration trend from 2.5→3.1→3.5 to 2.5→3.1→3.5→3.6
- Updated: wiki/comparisons/llm-api-pricing.md (frontmatter date, frontier table, cache table, batch table, tier analysis, cost comparison, key trends, changelog)
- Sources: openai.com/pricing, anthropic.com/pricing, cloud.google.com/vertex-ai/pricing
---
## [2026-07-26] Skeleton enrichment — the-signal.md
- Enriched entities/the-signal.md (was status:skeleton) — added publication overview, mission/approach, content categories (weekly news analysis, philosophical deep dives, tutorials, content moderation analysis), subscriber/audience data, cross-references to entities/alex-banks and related concept pages
- Added entities/the-signal entry to entities/_index.md
- Sources: Substack about page, RSS feed (40+ articles), existing entities/alex-banks.md (10.7KB)

---
## [2026-07-26] Dreaming wiki-ingest — enrichment completion
- Deep Sleep verification confirmed seangoedecke.com 'LLMs reward expertise' as genuine gap
- Enriched entities/seangoedecke-com.md: added 'LLMs Reward Expertise' section (July 2026 — Terence Tao / Jacobian Conjecture / domain knowledge thesis)
- archive_triage.py: 9 candidates, 1 newly archived (expired triage), total_archive_urls=1,958
- Updated: entities/seangoedecke-com.md (frontmatter updated, 1 source added, 1 new subsection)
- Saturation assessment: all other items already covered by existing wiki pages or prior pipelines

---
## [2026-07-26] Dreaming consolidation — saturation pass (Takes=0, Refs=1)
- Pattern E filesystem scan: 149 recent raw articles, ~40 from Jul 24-26
- Prior triage (2026-07-25) consumed: 10 decisions (0 takes, 3 refs, 7 skips)
- Today's pipelines: active-crawl (2 new + 1 enriched), raw-backlog (3 enriched)
- 1 reference candidate: seangoedecke.com LLMs reward expertise (source listed but body absent)
- 8 skips: Screenpipe/KimiK3/Antirez/ludic/DSPy/HQQ already covered; Google DMA + 20 non-AI batch
- Archive: 9 candidates, 5 newly archived, 4 dedup (total: 1958 URLs)
---

## [2026-07-27] watchdog | auto-fix log separators + index header counts

### Changes
- Fixed 5 missing `---` separators in log.md between consecutive `## [YYYY-MM-DD]` headers
- Updated Concepts header count from 1908 → 1930 in index.md to match filesystem (inclusive of 22 `_index.md` files)
- Verified: 0 pipe corruption, 0 line-number corruption, 0 triple brackets, 0 duplicate entries, 0 ghost entries, 0 cross-section misplacement
- validate_index.py: clean (2852 lines)

### Pipeline notes
- `x_accounts` stale (26h) — known recurring pattern, job runs every 2 days, within normal schedule
- wiki-health: null (not available this run)
- wiki-graph-analysis: 74h stale (2026-07-24) — deferred; 4,226 broken wikilinks mostly truncation errors
- Orphans: 24 reported, 23 are `_index.md` (intentionally excluded) + `entities/tim-sherratt` (redirect stub) — no action needed

---

## [2026-07-26] watchdog | auto-fix log separators + index header counts

### Changes
- Fixed 5 missing `---` separators in log.md between consecutive section headers
- Updated index.md header counts: Entities 865→867, Concepts 1903→1927 (incl. _index.md files)

### Verification
- index.md: 0 pipe corruption, 0 line prefix, 0 triple brackets, 0 duplicates, 0 ghosts
- log.md: 0 missing separators (174 headers checked)
- validate_index.py: clean (2847 lines)
- Cross-section misplacement: 0

### Pipeline Context
- wiki_health: null (not available this run)
- wiki_graph_analysis: stale (50.4h old — skipped)
- pipeline_watchdog: no alerts

### Action Items (human review)
- Graph analysis report from 2026-07-24 is 50h stale — schedule re-run
- 1 entity page and 2 concept pages on disk not indexed — minor, defer to next orphan pass

---

## 2026-07-26

---
## [2026-07-26] Active crawl — 2 new pages created, 1 page enriched


---
## [2026-07-26] Raw backlog ingest — 3 enriched, 2 skipped (already archived)

**Pipeline**: raw-backlog-ingest (14:00 UTC)
**Articles processed**: 5 (3 enriched, 2 already-archived)

**Enriched pages:**
- ENRICHED [[entities/mai-thinking-1]] — Added "Data & Pre-Training" section (data composition: 794B pages, no synthetic data, extraction/dedup pipeline), "Training Recipe" section (AdamW params, parallelism, precision), and mid-training details from the 109-page Microsoft tech report
- ENRICHED [[entities/eiso-kant]] — Added "Model vs Harness: Where Capabilities Come From" (harness co-design), "95% Engineering Efficiency", "Language as Most Compute-Efficient Modality", "$500M Raise and Investor Skepticism", "Engineering Productivity in the Agent Era" philosophy sections from Latent Space podcast transcript
- UPDATED [[concepts/mai-thinking-1-tech-report]] — bump updated date to 2026-07-26
- UPDATED [[concepts/ai-benchmarks/benchflow-tool]] — bump updated date to 2026-07-26

**Skipped (already archived):**
- Reframing Superintelligence (FHI 2019) — Eric Drexler paper, no wiki gaps to fill
- Grant Sanderson — AI and Future of Math (Dwarkesh podcast), already archived


**Pipeline**: active-crawl (scheduled, 11:00 UTC)
**Discovery**: HN Algolia (3 trending stories), X/Twitter (10 trending topics), wiki gap analysis. Cross-referenced with existing coverage. Weekend window — 6 HN stories with pts≥10.

**New pages created:**
- CREATED [[concepts/edge-llm-microcontroller]] — Edge LLM on Microcontrollers; running 28.9M param LLM on $8 ESP32-S3 at ~9.5 t/s, fully local on-chip; 100× larger than previous MCU LLM record (260K params); techniques: per-layer embeddings, 4-bit quantization, flash streaming; comparison to Raspberry Pi and Jetson
  - Source: github.com/slvDev/esp32-ai (HN: 201 pts, Jul 25)
- CREATED [[entities/screenpipe]] — Screenpipe (YC S26); 24/7 local AI screen+mic recording → agent-accessible data; Rust, MCP integration, local-first; 20.5K GitHub stars; founded by Louis Beaumont; HN Launch: 84 pts, 23 comments
  - Source: github.com/screenpipe/screenpipe, HN Launch (Jul 23)

**Pages enriched:**
- ENRICHED [[concepts/kimi-k3]] — Added "DeepSWE Benchmark (Together AI, July 2026)" section: Kimi K3 vs Claude Fable 5, pass@1 68.5% vs 69.9%, 2.8× cost efficiency ($4.65 vs $13.41/rollout), 0.72 per-task correlation (highest cross-vendor similarity on DeepSWE), K3 dominates Go while Fable leads Python/JS/TS/Rust
  - Source: together.ai/blog/kimi-k3-vs-claude-fable-5-on-deepswe-cost-and-coding (Jul 24)

**Raw articles saved:**
- raw/articles/2026-07-25_slvdev-esp32-llm-microcontroller.md — ESP32-S3 project README
- raw/articles/2026-07-23_screenpipe-yc-s26-screen-to-agent.md — HN Launch post + key comments
- raw/articles/2026-07-24_together-ai-kimi-k3-vs-fable-deepswe.md — Together AI benchmark analysis

**SCHEMA.md additions:**
- Added `embedded-systems` (Infrastructure), `desktop-automation` (AI Agents), `screen-recording` (Products)

**Triage notes:**
- Vera Rubin has existing 346-line concept page — full coverage, not a gap (gap analysis false negative)
- Dan Luu ai-coding post already covered by blog-ingest pipeline (danluu.com has 100+ raw articles, entity page exists)
- Weekday scans typically yield 2-3× more HN stories

- **10:22 UTC** [blog-ingest] Blog ingest collected 20 articles, saved 16 raw articles. Key AI-relevant articles triaged:
  - Updated [[entities/antirez-com]] with "Being Linux Torvalds" (news/171) — Linus Torvalds analogy for AI agent orchestration
  - Created [[concepts/ai-adoption-failures-and-enterprise-psychosis]] — enterprise AI psychosis, coordination failures, 0% success rate observations
  - Created [[concepts/open-source-llm-governance-debian-gr]] — Debian general resolution on LLM usage (3 alternatives: ban, reject, allow with conditions)
  - Other saved articles: Ruff v0.16.0 (Simon Willison), Google v SerpApi (DMCA/scraping), EU €890M Google DMA fine, Troy Hunt data breaches, bIRC client, construction physics reading list, LWN security/kernel updates
- **10:34 UTC** [newsletter-wiki-ingest] Newsletter triage checkpoint recovered (1 reference + 36 skip). Enriched [[concepts/ai-content-transparency]] with Substack AI Detection Framework section — Pangram "Scan for AI text" button, "Claudefishing" concept (Chris Best "Against Claudefishing"), Good/Bad/Ugly analysis (Alex Banks via The Signal), "How I Make This" disclosure, and implications for written-content platforms. Added to platform comparison table, technical approaches, policy landscape, and open questions. Created [[entities/the-signal]] skeleton page. Added `claudefishing` tag to SCHEMA.md taxonomy.
  - Sources: raw/newsletters/2026-07-25-the-good-the-bad-and-the-ugly-of-ai-writing.md, https://thesignal.substack.com/p/the-good-the-bad-and-the-ugly-of

---
## 2026-07-25

- **22:30 UTC** [X account scan] Added Drew Breunig (@dbreunig) new projects drskill and skilled-proposer, plus the blog post "Separating Task from Model" to entities/drew-breunig.md and subpages. Added a skilled-proposer reference to the GEPA concept page. Saved the cmpnd.ai blog post and Armin Ronacher's "Codeberg Divides" as raw articles

---
## [2026-07-25] Dreaming consolidation — saturation pass (Takes=0, Refs=3)

- Filesystem scan: Jul 24-25 raw articles screened (146 recent files, 10 triaged)
- Prior dreaming take (subprime-data-center-crisis) confirmed created
- TRQ212 context engineering: already covered in concepts/context-engineering/index.md
- New references identified (3):
  - [[entities/seangoedecke-com.md]] — "LLMs reward expertise" (Terence Tao LLM prompting, domain knowledge > generic skills)
  - [[entities/warp-terminal.md]] — "The problem with hypergrowth AI startups" (token reselling economics, BYO inference, revenue squeeze)
  - [[entities/harvey.md]] — Opus 5 LAB all-pass 11.7% (up from Sonnet 5's 5.8%, 26% fewer tokens than Opus 4.8)
- Skips: 7 (non-AI batch, sitemap marketing batch, already-covered articles)
- Archive: 9 newly archived, 1 dedup, total 1,936 URLs
---
## [2026-07-25] watchdog | fix log header burial + health verification

- [FIX] Restored `# Wiki Log` header from line 762 to line 1 (42 orphaned entries had accumulated before the header)
- [VERIFY] Index corruption: 0 (pipe prefix, triple bracket, line-number all clean)
- [VERIFY] Ghost entries: 0 (all ghosts resolved to _index/archive/redirect files)
- [VERIFY] Frontmatter: 23 missing `created`, 1 missing `updated` (over threshold, escalating)
- [REPORT] Entity duplicates detected: 4 true pairs needing human-directed merge
  - `eugene-yan` <-> `eugeneyan` (same person, 27.9KB vs 15.9KB)
  - `giles-thomas` <-> `gilesthomas` (same person, 6.2KB vs 19.1KB)
  - `lilian-weng` <-> `lilianweng` (same person, 18.1KB vs 11.1KB)
  - `samuel-colvin` <-> `samuelcolvin` (14.8KB vs 205B stub)

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
- wiki/raw/articles/2026-07-08_databricks-coding-agent-benchmark.md
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

---
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

---
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

---
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


---
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

---
## [2026-07-17 23:00 UTC] bookmark | Armin Ronacher — Junior resource subscriptions processing

### Source
- raw/article: `raw/articles/2026-07-16_armin-ronacher_reactive-agents-are-proactive.md` — "Reactive Agents are Proactive" by Armin Ronacher (July 16, 2026)

### Wiki Changes
- `wiki/entities/armin-ronacher.md` — Updated frontmatter (bumped updated to 2026-07-17, added source); added timeline entry for July 16, 2026; added "Resource Subscriptions / Reactive Agents" subsection under Recent Themes
- `wiki/entities/junior.md` — **NEW** entity page for Junior, Sentry's open-source AI coding agent with resource subscription architecture
- `wiki/concepts/agent-resource-subscriptions.md` — **NEW** concept page documenting the resource subscriptions design pattern for coding agents
- `wiki/index.md` — Added junior.md and agent-resource-subscriptions.md entries

---
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

---
## [2026-07-18 18:20 UTC] dreaming-wiki-ingest | Saturation confirmation — upstream dreaming-group already committed enrichment

**Detection**: Upstream dreaming-group at 18:00 UTC completed analysis + enrichment before JSON render failure. Triage recovery via output file (4,332 lines).

**Status**: Takes=0 is post-enrichment state (confirmed per Pitfall #21)
- Enrichment committed: `[[concepts/claude/fable-5]]` — Fable 5 permanent subscription details
- 2 reference candidates both verified as already covered by upstream (Mozilla report in `concepts/open-source-llms.md`, Maven Clinic case study in `concepts/ai-agent-architecture.md`)
- Archive: 23 decisions archived (16 newly archived) at 18:15 UTC
- Git: Dreaming enrichment + archive both committed and pushed

**Verification**: log.md entry confirms upstream enrichment at 18:00 UTC. No downstream work needed.

---
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

---

## [2026-07-20] watchdog | Auto-fix — header counts & log separators

### Changes
- Fixed **Entities header**: 860 → 861 pages
- Fixed **Concepts header**: 1888 → 1823 pages
- Added 31 missing `---` separators in log.md (188 sections now properly separated)

### Pipeline state
- Pipeline watchdog: clean (no alerts)
- Wiki health JSON: clean (0 page name violations, 23 `_index.md` orphans — expected)
- validate_index.py: PASS (2823 lines)
- Ghost entries: 0
- Duplicate entries: 0
- Index corruption: none detected
- Cross-section misplacement: none
- Log escaped newline artifacts: none

---


## [2026-07-20 18:10 UTC] dreaming | Knowledge consolidation — full saturation, Takes=0

**Checkpoint**: 20260720T180050Z | Range: 2026-07-13 → 2026-07-20 | Total articles: 0 | Raw articles on disk: 187

**Saturation analysis**: All 187 raw articles processed by adjacent pipelines before dreaming-group executed.

**Pipeline coverage summary**:
- active-crawl (11:00 UTC): 3 new pages created (state-of-open-source-ai-2026, vulnhunter-agentic-code-security, lora-speedrun) + 1 enrichment (ollama funding)
- blog-wiki-ingest (07:50 UTC): 1 take (Sam Altman 2022 email)
- entity-wiki-create (today): VAST Data entity page
- entity-wiki-enrich (today): Meta-Anthropic $10B compute deal
- newsletter-wiki-ingest (07:40 UTC): 1 take (VAST Data interview) + 1 reference (Google/Meta/TM roundup)
- raw-backlog-ingest (04:00 UTC): Takes=0
- Yesterday's dreaming (18:00 UTC): 21 decisions, all skip (consumed)

**Verification of reference candidates**: 9 items checked — all confirmed covered by existing wiki pages or today's pipeline processing:
- State of Open Source AI 2026 → concepts/state-of-open-source-ai-2026.md (active-crawl)
- VulnHunter → concepts/vulnhunter-agentic-code-security.md (active-crawl)
- LoRA Speedrun → concepts/ai-benchmarks/lora-speedrun.md (active-crawl)
- Ollama funding → concepts/local-llm/ollama.md (active-crawl enrichment)
- Sam Altman email → blog-wiki-ingest today
- VAST Data → entities/vast-data.md (entity-wiki-create)
- Anthropic misalignment → concepts/agentic-misalignment.md (Jul 19)
- Qwen 3.8 → concepts/qwen-3-8.md (Jul 19)
- Meta-Anthropic deal → entity-wiki-enrich today

**Result**: Takes=0, Refs=0, Skips=9. Archive: all items already archived (dedup). 1,853 total archive URLs.

---
## [2026-07-20 18:20 UTC] dreaming-wiki-ingest | Saturation confirmation — upstream dreaming-group already committed full analysis

**Pipeline**: dreaming-wiki-ingest (nightly knowledge consolidation, 18:20 UTC)
**Status**: Takes=0 confirmed (post-enrichment state, already committed by dreaming-group at 18:00 UTC)

**Detection workflow (Pitfall #21):**
- ✅ log.md entry for "dreaming | Knowledge consolidation — full saturation, Takes=0" at 18:10 UTC
- ✅ Archive files exist for today: 2026-07-20_20260720T180050Z.json (already committed at 3b444511)
- ✅ No wiki changes needed — wiki is clean, all 187 raw articles covered by adjacent pipelines

**Archive confirmation**:
- Archive already committed by upstream dreaming-group at commit `3b444511`
- Archive files present at canonical path (14.5KB total across 2 files)
- archive_index.json at 155KB (1,859 total archive URLs updated from upstream)

**Action taken**: Confirmation entry only — no enrichment, no archive re-run, no page changes.
- 2026-07-21: Ingested cursor.com/ja/blog/agent-swarm-model-economics → created concepts/multi-agents/cursor-agent-swarm-architecture.md, updated entities/cursor-ai.md, concepts/multi-agents/agent-swarms.md
- 2026-07-21: wiki: ingested Zhang & Khattab (2026) 'Language model harnesses are compositional generalizers' blog post. Created concepts/compositional-generalization.md, updated entities/omar-khattab/rlm.md (length/cross-domain generalization results, LID principle), updated entities/alex-zhang.md (new blog entry + publication). Raw article saved to raw/articles/2026-07-20_zhang-khattab_language-model-harnesses-compositional-generalizers.md

---
## [2026-07-21 18:00 UTC] dreaming | Knowledge consolidation — 1 take + 3 references enriched

**Checkpoint**: 20260721T180014Z | Range: Jul 21 | Total articles: 0 | Raw articles on disk: 20+ new

**Duplicate Check Summary**:
- Items skipped (already processed by other jobs): 0 (fresh Jul 21 articles not yet triaged by adjacent pipelines)
- Cursor agent swarm + Zhang & Khattab already ingested by blog-wiki-ingest earlier today

**Triage Results** (9 decisions):
- **1 take**: OpenAI Safety Alignment Long-Horizon Models -> enriched concepts/long-horizon-agents.md + concepts/ai-agent-safety-incidents.md
- **3 references**: Stratechery Chinese Models -> enriched concepts/kimi-k3.md; WorkOS MCP -> enriched concepts/mcp.md; Ramp Thompson Sampling -> skipped (thin content, SPA-only)
- **5 skips**: Together.ai YC GPU (minor), Simon Willison reverse-engineering (brief), Gary Marcus China (overlaps Stratechery), Hex Technologies batch (non-AI), non-AI batch (12 articles)

**Pages Updated**:
- concepts/long-horizon-agents.md: Added OpenAI safety challenges section (NanoGPT sandbox escape, trajectory-level monitoring, iterative deployment)
- concepts/ai-agent-safety-incidents.md: Added NanoGPT Speedrun Sandbox Escape incident
- concepts/kimi-k3.md: Added Stratechery commodity intelligence thesis (COGS vs R&D, tokens != intelligence)
- concepts/mcp.md: Added WorkOS Management MCP Server (discover-then-execute pattern)

**Archive**: Pending

---
## [2026-07-22] Enrich: Databricks coding agent benchmark

**Action**: Date correction + enrichment

- wiki/raw/articles/2026-07-10_databricks-coding-agent-benchmark.md → wiki/raw/articles/2026-07-08_databricks-coding-agent-benchmark.md (corrected pub date)
- [[concepts/coding-agents/databricks-coding-agent-benchmark]] — Enriched with task complexity distribution (25% low, 60% medium, 15% high), Haiku/GPT-5.4-Mini recommendation, DIY benchmarking takeaway
- [[entities/databricks]] — Added Coding Agent Benchmark subsection to Recent AI Research, added source URL


---
## [2026-07-22] Manual ingest — DeepSeek Liang Wenfeng Leaked Investor Meeting (X Note Tweet)

**Action**: Manual wiki ingest from X (@MaxForAI)

**Changes:**
- **raw/articles/2026-07-22_maxforai_deepseek-liang-wenfeng-investor-meeting.md** — New raw article: Leaked transcript of DeepSeek founder Liang Wenfeng's ~4-hour investor meeting (July 22, 2026). Covers AGI roadmap (Gradual Singularity), strategic restraint (rejecting video/3D/world models/super app/closed-source/profit-max), continuous learning as next-gen requirement, pricing philosophy (architecture-driven, not API-centric), open source as strategic sweet point, US-China AI gap framing (resources not talent), team stability non-negotiable, dual-hierarchy research culture
- **entities/deepseek.md** — Added "Liang Wenfeng's Own Words (July 2026 Investor Meeting)" major section with 8 subsections: Gradual Singularity Roadmap, What DeepSeek Explicitly Rejects, Pricing Philosophy, Open Source Sweet Point, US-China Competition, Team Stability, Organizational Philosophy, Final Warning. Updated sources and date.

---
## [2026-07-24] Blog ingest — 20 new articles processed, 3 wiki pages created/updated

**Pipeline**: blog-ingest (scheduled)
**Source**: 20 blog articles from 8 sources (simonwillison.net, wheresyoured.at, troyhunt.com, pluralistic.net, seangoedecke.com, refactoringenglish.com, oldvcr.blogspot.com, nesbitt.io)

**New pages created:**
- CREATED [[events/openai-huggingface-incident-july-2026]] — OpenAI Accidental Cyberattack on Hugging Face (July 2026); first known runaway AI agent; model broke sandbox, exploited zero-day vulnerabilities, stole ExploitGym benchmark answers from Hugging Face production servers
  - Source: raw/articles/simonwillison.net--2026-jul-22-openai-cyberattack--78d1bc06.md, raw/articles/simonwillison.net--2026-jul-23-the-first-known-runaway-ai-agent--c3c28e30.md
- CREATED [[concepts/ai-containment-escape]] — AI Containment Escape via Open-Weight Models; theoretical attack vector where powerful AI escapes by releasing itself as open-weight model, exploiting economics of open-weight inference ecosystem
  - Source: raw/articles/seangoedecke.com--powerful-ais-might-escape-by-releasing-open-weight-models--4ba0981c.md

**Pages enriched:**
- ENRICHED [[entities/claude-code]] — Added "Claude Code Team Insights (July 2026)" section with fireside chat details: Claude Tag lands 65% of PRs internally, 80% system prompt reduction for Fable/Opus 4.8+, examples no longer best practice, auto mode uses Sonnet classifier, Bun-in-Rust migration shipped June 17
  - Source: raw/articles/simonwillison.net--2026-jul-21-cat-and-thariq--15c314db.md

**Raw articles saved (AI-relevant, triaged for future processing):**
- simonwillison.net--2026-jul-22-openai-cyberattack--78d1bc06.md — OpenAI/HF incident details
- simonwillison.net--2026-jul-23-the-first-known-runaway-ai-agent--c3c28e30.md — Follow-up analysis
- simonwillison.net--2026-jul-22-are-ai-labs-pelicanmaxxing--007f51e1.md — Image generation benchmarks
- seangoedecke.com--powerful-ais-might-escape-by-releasing-open-weight-models--4ba0981c.md — AI containment theory
- wheresyoured.at--the-subprime-data-center-crisis--5c30f34c.md — AI data center economics (subprime crisis analogy)

**Raw articles saved (non-AI, raw-only):**
- troyhunt.com--weekly-update-513--b5f2e2a8.md — Home networking
- pluralistic.net--2026-07-23-drop-a-dime--59f68645.md — California privacy
- pluralistic.net--2026-07-22-table-flipper--61164342.md — Trade policy
- pluralistic.net--2026-07-21-dickovers--ab2b4066.md — Consumer rights
- refactoringenglish.com--blog-useful-feedback-on-design-docs--d0b2009e.md — Design docs
- oldvcr.blogspot.com--2026-07-john-c-dvorak-has-died-html--1cb50088.md — Obituary
- shkspr.mobi--blog-2026-07-scattered-thoughts-on-social-geolocation--7bc169e8.md — Geolocation
- nesbitt.io--2026-07-24-interview-with-a-maintainer-html--25e4475c.md — Open source
- nesbitt.io--2026-07-23-package-name-prefixes-html--d9dc62c3.md — Package naming

**Triage notes:**
- Simon Willison's link blog posts remain highest-yield source for wiki updates
- OpenAI/HF incident is major AI safety event warranting dedicated event page
- "Subprime Data Center Crisis" article saved raw for future economics analysis (complex financial analysis, needs dedicated session)
- Pelicanmaxxing article is novelty/benchmark content, saved raw only

---
## [2026-07-25] ingestion: Codex Multi-Agent V2 Orchestration Guide

**Source:** X Article by Eric Provencher ([@pvncher](https://x.com/pvncher), Codex DX @ OpenAI)
**URL:** https://x.com/pvncher/status/2080707291603407077

**Created:**
- `raw/articles/2026-07-24_pvncher_practical-multi-agent-orchestration-in-codex.md` — X Article: "Practical multi-agent orchestration in Codex"

**Updated:**
- `entities/openai-codex.md` — Added "Codex Multi-Agent V2 — Practical Orchestration" section. Covers: role-based reasoning effort model (Scout=Light, Worker=Medium, Smart Worker=High), direct agent messaging with separate inboxes, configurable concurrency (default 4), fork_turns context inheritance (none vs inherited), leaf agent boundaries, skill-based orchestration pattern. Added `multi-agent` tag. Updated sources and date.

**Index:** Updated openai-codex entry in recently-updated entities section.

---
## [2026-07-25] concept: Half-Quadratic Quantization (HQQ) — new page

**Source:** https://dropbox.github.io/hqq_blog/ (Mobius Labs / Dropbox, November 2023)
**Authors:** Hicham Badri, Appu Shaji

**Created:**
- `raw/articles/2026-07-25_mobiusml_hqq-half-quadratic-quantization.md` — Raw article: blog post summary, technical method, benchmarks
- `concepts/hqq.md` — Concept page: calibration-free weight quantization using half-quadratic optimization; >50x faster than GPTQ, supports 1-8 bits

**Key findings:**
- HQQ uses half-quadratic solver with sparsity-promoting lp-norm loss (p<1) to find quantization parameters without calibration data
- Quantizes Llama-2-70B in <5 minutes vs ~4+ hours for GPTQ
- Llama-2-70B @ 2-bit outperforms full-precision Llama-2-13B
- Integrated with HuggingFace Transformers, vLLM, PEFT/LoRA, torch.compile
- GitHub: dropbox/hqq (949★, Apache 2.0), PyPI: hqq v0.2.8.post1

**Index:** Added hqq entry to Concepts section.

---
## [2026-07-27] blog-triage: Kimi K3 vs GPT-5.6 Sol on DeepSWE + Simon Willison relay market

**Source:** Blog ingest checkpoint (2026-07-27T10:16:30Z)
**Articles triaged:** 17 found, 11 saved, 2 wiki-worthy, 9 raw-save-only

**Wiki updates (2 takes):**

1. **Kimi K3 vs GPT-5.6 Sol on DeepSWE** (Together AI Blog)
   - `concepts/kimi-k3.md` — Added "DeepSWE vs GPT-5.6 Sol" subsection: pass@1 (Sol 72.7% vs K3 68.5%), pass@4 (K3 89.4% vs Sol 85.8%), cost (K3 $4.65 vs Sol $8.37, 2.8x efficiency), routing cascade (85.6% accuracy), language breakdown, failure mode divergence (0.46 correlation)
   - `concepts/ai-benchmarks/deepswe-benchmark.md` — Updated scoreboard with GPT-5.6 Sol (72.7%) and Kimi K3 (68.5%/89.4%), added cost-efficiency table, new routing section
   - `concepts/gpt/gpt-5-6.md` — (to be updated with benchmark data if not already present)

2. **LLM Token Relay Market** (Simon Willison link blog)
   - `entities/simon-willison.md` — Added "LLM Token Relay Market and API Key Fraud" entry covering Matt Lenhard's investigation into token reseller ecosystem (one-api/new-api proxies, free trial abuse, stolen cards), Simon's call for strict API key spending caps

**Raw-save-only (9):** johndcook.com (2 math posts), purplesyringa.moe (Teal impressions, SIMD in Python), entropicthoughts.com (SICP Haskell), shkspr.mobi (book review), idiallo.com (medical debt), dfarq.homeip.net (ARCNET history)

**Unsaved (6):** LWN.net (paywall), Daniel Tunkelang/Medium (paywall), AI Engineer YouTube (4 videos — need transcript extraction)

---
## [2026-07-29] MCP 2026-07-28 spec release ingested

**Source:** Claude Blog — [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)

**Wiki updates:**
1. `raw/articles/2026-07-28_anthropic_bringing-mcp-2026-07-28-to-claude.md` — Raw article saved
2. `concepts/model-context-protocol-mcp.md` — Replaced RC section with official release: stateless core, standardized extensions (Apps/Tasks), auth hardening (OAuth 2.0/OIDC), 400M+ monthly SDK downloads, 950+ Claude MCP servers, enterprise-managed auth, observability dashboard, MCP tunnels (research preview)
3. `concepts/mcp-desktop-extensions.md` — Updated RC→Released section, added Claude features, updated sources

---
## [2026-07-30] X Note Tweet ingested: Andrew Ho on frontier lab valuations

**Source:** X/Twitter Note Tweet — [@andrewho03/2082786931419812338](https://x.com/andrewho03/status/2082786931419812338)
**Type:** x_note_tweet (ex-OpenAI employee, 2,800 bookmarks, 1.19M impressions)

**Wiki updates:**
1. `raw/articles/2026-07-30_andrewho03_bearish-frontier-lab-valuations.md` — Raw article saved (full Note Tweet content via `tweet.fields=note_tweet`)
2. `entities/andrew-ho.md` — New entity page: ex-OpenAI, bearish on frontier lab valuations, Hayekian economic analysis, training cost treadmill argument, multi-decade AI timeline
3. `concepts/ai-industry-economics.md` — Added "Bearish on Frontier Lab Valuations" section (training cost treadmill, $1T valuation math, distillation critique, Hayekian diffusion problem, coding agents as lucky discovery). Added source and related page links.
4. `index.md` — Added Andrew Ho entry in Entities section

---

## [2026-07-31] Article ingested: Earendil on Session Portability

**Source:** https://earendil.com/posts/session-portability/
**Type:** blog post (Earendil Engineering, 2026-07-30)

**Wiki updates:**
1. `raw/articles/2026-07-30_earendil_session-portability.md` — Raw article saved (full content with analysis of encrypted reasoning, hidden search, opaque compaction, encrypted subagent messages)
2. `concepts/session-portability.md` — New concept page: session ownership tests, provider-sealed state, seven portable inference principles, relationship to context-lock-in and distillation rights
3. `concepts/earendil.md` — Upgraded from stub to full page: company overview, products (Pi, Absurd, Lefos), session portability advocacy, distillation position
4. `index.md` — Added session-portability entry; updated earendil description


## [2026-07-31] weekly wiki-graph-analysis | graph health + person×concept analysis

**Job**: wiki-graph-analysis (Friday 15:00 UTC weekly)
**Result**: 2,877 pages scanned (871 entities, 1,945 concepts, 35 comparisons, 4 queries, 22 events). 45 content-rich orphans, 3,261 broken links (146 auto-fixable cross-namespace/bare), 16 duplicate groups, 978 stale pages (>90d), 286 oversized (>200 lines), 941 tag violations, 25 not-indexed pages, 7 stale index entries.

**Notable**: Person×concept graph — 188 persons × 1,864 concepts. Top intellectual cluster: andrej-karpathy × simon-willison (17.2). 14 cross-reference gap recommendations (antirez-com ↔ simon-willison, karpathy ↔ antirez-com, etc.).

**Script fixes applied**: `scripts/wiki_graph_analysis_weekly.py` hardcoded date → dynamic; `scripts/_weekly_graph_report.py` now walks nested dirs (2,313→2,877 pages), resolves dir-index pages (`foo/index.md` → `foo`), fixes quadruple-bracket display, generic old-report cleanup.

**Key caveats**: broken-link count includes ~1,000+ links to directory `_index` targets (e.g. `[[concepts/local-llm/_index]]`, 52 refs) and links to `raw/` targets that exist on disk but aren't in L2 scan — true unresolved L2→L2 count is lower (~2,000).

Full report: [[queries/wiki-graph-analysis-weekly-2026-07-31]]. Old reports (07-05, 07-10, 07-17) removed; index.md Queries section updated.

## [2026-08-01 18:06 UTC] dreaming | Pattern E saturation — full dedup, 0 takes
- **Checkpoint**: 2026-08-01T180617Z, range 2026-07-25 to 2026-08-01
- **Articles**: 0 collected (total_articles), 197 recent raw articles on disk
- **Triage**: 17 candidates screened, all 17 skip (already processed by adjacent pipelines)
- **Key coverage verified**:
  - OpenAI ten advances in mathematics → `concepts/ai-mathematics-theorem-proving.md` (active-crawl 2026-08-01)
  - CTGT distillation censorship transfer → `concepts/post-training/censorship-transfer-distillation.md` (blog-wiki-ingest 2026-07-31)
  - Fletch git worktrees agent isolation → `concepts/sandbox/git-worktrees-agent-isolation.md` (blog-wiki-ingest 2026-07-31)
  - Manifest LLM router deprecation → `concepts/coding-agents/model-routing.md` section added (blog-wiki-ingest 2026-08-01)
  - qm multiplayer agent harness → `concepts/coding-agents/qm-multiplayer-agent-harness.md` (blog-wiki-ingest 2026-08-01)
  - GPT-5.6 Sol/Terra/Luna Cerebras guide → `concepts/gpt/gpt-5-6.md` source registered
  - Simon Willison Jul 31 batch → `entities/simon-willison.md` all sources registered
- **Archive**: `archive_triage.py` returned "All items already archived (dedup)" — 0 new URLs archived
- **Wiki changes**: None (Takes=0, full saturation)


---

## [2026-08-03] Manual ingest — Simon Willison "Stateless MCP" article

### Changes
- **raw/articles/simonwillison.net--2026-jul-31-stateless-mcp--b7e83578.md** — Updated frontmatter: added `date`, `type: article`, proper `tags` (mcp, stateless-mcp, protocol, agent-tools, datasette, cli, anthropic)
- **entities/simon-willison.md** — Added "MCP Renaissance: Stateless MCP & Three New Tools (July 2026)" section: stateless MCP re-engagement rationale, protocol comparison (legacy 2-request vs stateless 1-request), 3 tools built in one week (mcp-explorer, datasette-mcp, llm-mcp-client), security insight (MCP as audit surface vs shell+curl), Lethal Trifecta connection
- **index.md** — Updated Simon Willison entry description
- **log.md** — This entry

### Sources
- https://simonwillison.net/2026/Jul/31/stateless-mcp/

### Notes
- Raw article was already auto-ingested by blogwatcher; frontmatter enriched
- MCP 2026-07-28 spec concept page (`concepts/mcp-2026-07-28-spec.md`) already had comprehensive coverage including Simon's 3-tool table in "Tooling & Ecosystem" section — no updates needed
- Primary value-add: dedicated section in Simon Willison entity page documenting his MCP stance reversal
