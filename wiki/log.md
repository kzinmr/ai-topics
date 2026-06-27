|---
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

# Wiki Log
- 2026-06-23: Created entities/martinfowler.md — Martin Fowler entity page enriched with PRINCE case study (Bayer AG + Thoughtworks, Agentic RAG + Text-to-SQL), context engineering and harness engineering sections. Added redirect from martin-fowler.md. (June 23)
- 2026-06-23: Dreaming wiki-ingest — enriched `concepts/claude-code/claude-code-skills.md` with Anthropic official steering methods (CLAUDE.md, rules, skills, subagents, hooks, output styles, system prompt, comparison table). +100 lines. (June 23)
  - Sources: Anthropic Engineering Blog (Steering Claude Code)
- 2026-06-23: Blog wiki-ingest — enriched 6 pages (4 takes from blog-triage, recovered from checkpoint).
  - Enriched `entities/simon-willison.md` — Prompt Injection as Role Confusion research (destyling: 61%→10%) and Porting Moebius 0.2B to browser via Claude Code
  - Enriched `entities/martin-alderson.md` — added Machine Learning Research section with expert-aware quantization for MoE models (Qwen3.6 35B-A3B, Q4-hot/Q2-cold recovers ~90% gap)
  - Enriched `entities/modal-labs.md` — added Sandbox Startup Latency Analysis (5-stage lifecycle, Readiness Probes GA, Warm Pools)
  - Enriched `concepts/agentic-engineering.md` — added Moebius browser porting case study (muse-on-X, subagent delegation, vibe coding)
  - Enriched `concepts/model-quantization.md` — added Expert-Aware Quantization (MoE-specific) subsection
  - Enriched `concepts/modal-sandboxes.md` — added 5-stage sandbox startup lifecycle and Readiness Probes
  - Sources: simonwillison.net (Prompt Injection as Role Confusion, Porting Moebius), martinalderson.com (Expert-aware quantisation), Modal Blog (Sandbox startup latency)
- 2026-06-23: Newsletter wiki-ingest — processed 3 articles from 6 newsletters.
  - Enriched `entities/glm-5-zai.md` — added Nate Lambert analysis of GLM-5.2 as "step change for open agents" (strategic release context, economic impact, first-hand experience, ecosystem adoption)
  - Enriched `concepts/google-spacex-ai-compute-deal.md` — added Reflection AI $6.3B deal (SpaceX's third GPU rental customer), SpaceX as $28B/yr neocloud, Baseten $13B Series F
  - Enriched `concepts/claude/mythos.md` — added Gray Swan red-teaming analysis (Zico Kolter/Matt Fredrikson interview, Shade/Cygnal/Arena tools, "lethal trifecta", agent security nightmare)
  - Sources: Interconnects (Nate Lambert), AINews (swyx/Latent Space), Latent Space (Gray Swan)
# Wiki Log
- 2026-06-23: Processed batch of 5 articles.
  - Added `reframing-superintelligence-fhi-2019.md` (K. Eric Drexler)
  - Added `2026-06-03_microsoft-mai-thinking-1-tech-report.md` (Microsoft AI Team)
  - Added `dwarkesh.com--p-alex-imus-phil-trammell--f12d8644.md` (Alex Imas, Phil Trammell)
  - Added `2026-06-10_darioamodei_policy-on-the-ai-exponential.md` (Dario Amodei)
  - Added `2026-06-18_agent-safety-separation-of-duties.md` (Aakash Gupta)
  - Created concepts: `superintelligence`, `cais`, `mai-thinking-1-report`, `agent-safety`.
- 2026-06-23: Watchdog fix — removed 1 ghost entry from concepts/_index.md (concepts/capabilities-based-security — target file did not exist).

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
