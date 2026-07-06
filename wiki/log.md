# Wiki Log

_Log of all wiki changes. Newest entries at top._

## [2026-07-06 11:16 UTC]

**active-crawl**: Created 4 new concept pages from trending HN/X topics (July 3-6, 2026):

- [[concepts/ai-generated-code-policies]] — AI-Generated Code Policies: Godot engine ban on AI-authored code (558 HN pts), open source governance of AI contributions, policy design space
- [[concepts/reasoning-model-quality-degradation]] — Reasoning Model Quality Degradation: GPT-5.5 Codex reasoning-token clustering at 516/1034/1552 (366 HN pts), hidden constraints, reliability cliff
- [[concepts/enterprise-coding-agent-security]] — Enterprise Coding Agent Security: Claude Code session/cache leakage (313 HN pts) + Alibaba Claude Code workplace ban (335 HN pts), data exfiltration, sandboxing
- [[concepts/ai-inventorship-patent-law]] — AI Inventorship & Patent Law: Japan Supreme Court rules AI cannot be inventor (398 HN pts), DABUS cases, international comparison

Raw articles saved: 2026-06-30_pcgamer_godot-bans-ai-authored-code.md, 2026-06-27_github_gpt55-codex-reasoning-token-clustering.md, 2026-07-04_github_claude-code-session-cache-leakage.md, 2026-03-06_japannews_ai-cannot-be-patent-inventor.md

Sources: HN Algolia API, GitHub Issues API, PC Gamer, Japan News, HN discussions. Cross-referenced against wiki gaps — all 4 were genuine gaps with no prior concept pages.


## [2026-07-06] blog-wiki-ingest | Enriched SynthID C2PA section + Sean Goedecke entity page

### Changes
- **Enriched** [[concepts/synthid]] — Added "C2PAの限界と批判 — Sean Goedeckeの分析" section (6 critical lenses: all-image signing catch-22, SNS manifest stripping, 26-cert trust list, key management, safety theater, non-image applicability). Updated `updated` date and `sources` with new raw article.
- **Enriched** [[entities/seangoedecke-com]] — Added Timeline entry for "C2PA only works if everything is signed" with wikilink to new synthid C2PA section. Updated `updated` date and `sources`.

### Sources
- raw/articles/seangoedecke.com--c2pa-only-works-if-everything-is-signed--ae4eb8f4.md

### Stats
- Pages enriched: 2 (synthid, seangoedecke-com)
- Articles skipped (archived): 6

## [2026-07-06] newsletter-wiki-ingest | Enriched Microsoft + Figure AI + AI Jailbreaking pages

### Changes
- **Enriched** [[entities/microsoft]] — Added Microsoft Frontier Company section ($2.5B, 6,000 engineers embedded in enterprises, Rodrigo Kede Lima, early partners LSEG/Unilever/Accenture, any-model IP protection). Updated `updated` date and sources.
- **Enriched** [[entities/figure-ai]] — Added BMW Plant Spartanburg Deployment section (F.03 parts sequencing in logistics, Figure 02 30K+ BMW X3s track record, fingertip/3g sensors, palm cameras, wireless charging, Centre of Competence for Physical AI, Plant Leipzig pilot). Updated `updated` date and sources.
- **Enriched** [[concepts/ai-jailbreaking]] — Added Industry CVSS for Jailbreaks section (Anthropic+Amazon+Microsoft+Google framework, 4 criteria, HackerOne programme). Updated `updated` date and sources.

### Sources
- raw/newsletters/2026-07-05-anthropic-s-fable-freedom-microsoft-s-inside-job-and-figure-s-factory-foothold.md

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
## [2026-07-02] Ornith-1.0 公式リリースページ取り込み — wiki大幅更新

### Changes
- **raw/articles/deep-reinforce.com--ornith-1-0--official-release.md** — New: DeepReinforce公式リリースページ保存
- **concepts/ornith-self-scaffolding-llm.md** — Updated: Self-Improving Training Framework（2段階RLループ、Reward Hacking Defense 3層防御、Pipeline-RL）、詳細ベンチマーク数値（397B/35B/9B）、References拡充
- **comparisons/self-scaffolding-approaches.md** — Updated: Ornith欄をself-improving training frameworkの詳細に更新

### Sources
- https://deep-reinforce.com/ornith_1_0.html

---

## [2026-07-02] Self-Scaffolding Approaches — RLM / Dynamic Workflows / Ornith 比較ページ作成

### Changes
- **comparisons/self-scaffolding-approaches.md** — New: 3つのself-scaffoldingアプローチ（RLM, Dynamic Workflows, Ornith）の包括的比較ページ。実装層・訓練・並列性・決定フレームワークを含む
- **concepts/ornith-self-scaffolding-llm.md** — Updated: RLM/Dynamic Workflowsとの関連セクション追加、Related Pages拡充
- **concepts/dynamic-workflows.md** — Updated: Related ConceptsにRLM, Ornith, 比較ページへのリンク追加
- **concepts/rlm-recursive-language-models.md** — Updated: Related ConceptsにOrnith, 比較ページへのリンク追加
- **index.md** — Updated: comparisons/self-scaffolding-approaches追加

### Sources
- Simon Willison: https://simonwillison.net/2026/Jun/29/ornith/
- RLM: arXiv:2512.24601, Alex Zhang clarification (May 2026)
- Dynamic Workflows: Anthropic blog (June 2026)

---

## [2026-07-02] Pioneer AI & GLiNER Model Family — 新規エンティティ＆コンセプトページ作成

### Changes
- **entities/fastino-labs.md** — New: Fastino Labs企業ページ — SLM応用研究ラボ; Pioneerプラットフォーム, GLiNERモデルファミリー
- **entities/pioneer-ai.md** — New: Pioneer AIプロダクトページ — SLMファインチューニング＆推論エージェント; Agent Mode, Research Mode, Adaptive Inference; AdaptFT-Bench
- **concepts/gliner-model-family.md** — New: GLiNERモデルファミリーコンセプト — GLiNER→GLiNER2→GLiGuard→GLiNER2-PII; 双方向エンコーダアーキテクチャ; 42 PIIタイプ; OpenAI Privacy Filter比較
- **raw/articles/pioneer-ai-blog-*.md** — New: 6本のPioneer AIブログ記事をraw保存
- **SCHEMA.md** — Tags追加: `encoder-model`, `small-language-model`, `named-entity-recognition`, `pii-detection`

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

|---
## [2026-07-01 07:45] — Blog wiki-ingest — 2 takes, 4 references from 19 blog candidates (recovered from triage checkpoint after JSON parse error)

**Source:** blog-triage checkpoint (saved before response render failure)

### New pages created (2):
- `entities/giles-thomas.md` — Giles Thomas; "Writing an LLM from scratch" series (part 34a), JAX/NNX/Optax training loop, outside-in methodology
- `entities/grant-sanderson.md` — Grant Sanderson (3Blue1Brown); skeleton entity, AI as leading indicator in mathematics, Dwarkesh Patel podcast

### Existing pages enriched (3):
- `entities/ed-zitron.md` — Added "June 2026: BIS Systemic Risk Warning" section: BIS annual report $1T+ hyperscaler capex warning, Oracle $129.5B debt/$38B lease/$260B future lease, Exponential View report critique, "The Four Losers" framing
- `entities/simon-willison.md` — Added June 30 entries: Claude Sonnet 5 tokenizer analysis (1.42× English, sampling params deprecated, 30% effective price increase, Adaptive Thinking default ON) and shot-scraper video feature (agent self-recorded demos via storyboard.yml/Playwright)
- `concepts/claude/fable-5.md` — Added Export Controls Lift (June 30, 2026) section: Commerce Department lifted restrictions on Fable 5/Mythos 5 after ~18-day suspension
|---
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
- **concepts/multi-model-synthesis-strategies** — 横断概念ページ。3アプローチ比較: Cognition Devin Fusion (Sidekick)、OpenRouter Fusion (Panel Synthesis)、Sakana Fugu (Evolved Orchestration)

### Updated
- **concepts/coding-agents/model-routing** — Added Devin Fusion section + cross-reference
- **entities/openrouter** — Added Fusion API section + Related links
- **entities/cognition** — Added Devin Fusion section
- **concepts/sakana-fugu** — Added cross-reference to multi-model-synthesis-strategies
- **wiki/index.md** — Added multi-model-synthesis-strategies entry

## 2026-07-02
- 2026-07-02: Ingested Geoffrey Litt's mega thread 'Understanding the Code Our Agents Write' (36-part X thread) to raw/articles/2026-07-02-geoffreylitt-understanding-code-agents-write.md

## 2026-07-05

- **wiki-graph-analysis** — Full weekly wiki graph analysis run: 2,205 pages scanned. Report saved to wiki/queries/wiki-graph-analysis-weekly-2026-07-05.md. Added Queries section to index.md.

## 2026-07-05

- **duplicate page merge** — Merged 33 entity-concept duplicate pairs (kept larger file per pair). Fixed stale ghost entry `entities/show-us-your-agent-skills` → `concepts/show-us-your-agent-skills` in index.md. 0 ghost entries after fix.

- **duplicate merge fix** — Recovered deleted page content from git (d4da1bff) and merged unique sections into kept pages. 28 of 33 pairs had unique content to merge (5 were fully overlapping). +1,439 lines of recovered content.

- **sources field fix** — Added `sources: []` to 752 pages that were missing the field in YAML frontmatter. SCHEMA compliance: all pages now have the `sources` field.

- **index.md missing entries fix** — Added 2,416 missing pages to index.md (746 entities, 1,653 concepts, 3 comparisons, 3 queries, 11 events). Index now has 2,676 entries covering all filesystem pages.

- **orphan page fix** — Added inbound links from concepts/harness-engineering.md to 3 orphan pages (claude-code-best-practices, writing-tools-for-agents, context-engineering). Orphans reduced from 5 to 2 (archive pages only).
- 2026-07-06 llm-pricing-monitor: Updated OpenAI deep-research pricing (o3-deep-research $5→$10/$20→$40; o4-mini-deep-research $1→$2/$4→$8); added Claude Sonnet 5 ($2/$10 intro, $3/$15 std); updated cache/batch/trend tables
