## [2026-06-20] Active Crawl — 5 new pages (3 concepts + 1 entity + 1 concept)

**Pipeline:** active-crawl → parallel discovery (HN + X/Twitter + Wiki gaps) → cross-reference → page creation
**Sources:** HN Algolia (43 queries, 158 AI stories), xurl (11 queries), blogwatcher DB, wiki gap analysis

### Trend Discovery
- **Top HN stories:** SpaceX buys Cursor $60B (1142 pts), GLM-5.2 #1 open weights (894 pts), Norway AI school ban (688 pts), Fable 5 safety (608 pts), US holds off DeepSeek blacklist (533 pts), DeepSeek Vision (492 pts), Local Qwen vs Opus (481 pts)
- **X/Twitter trending:** @AndrewYNg on Anthropic export controls (275 bk), @simonw GLM 5.2 inference (217 bk), Claude Fable 5/Mythos 5 analysis, John Jumper talent migration
- **Blogwatcher unprocessed:** OpenAI Alignment Research "Beneficial RL" (HIGH), Anyscale Ray Serve distributed inference (HIGH), AI Engineer production playbook
- **Wiki gaps identified:** AI regulation/policy moderate (12 pages), AI hardware moderate (22 pages, NVIDIA-heavy), Multimodal moderate (12 pages)

### Pages Created

#### 🆕 Concepts
- **concepts/beneficial-rl.md** — Beneficial RL: Emergent Alignment via Trait-Based RL. OpenAI research (Jun 18, 2026) showing RL on beneficial traits (honesty, epistemic humility, metacognitive transparency, corrigibility, fairness, welfare concern) produces broad alignment generalization across 44/53 out-of-distribution evals. Health-domain training transfers to non-health alignment. Persistence under adversarial pressure with selective persistence (steerable for good, resistant to bad). Analogous to emergent misalignment in positive direction. Authors: Jagadeesh, Arora, Saab et al. Tags: alignment, reinforcement-learning, ai-safety, openai, model, post-training, rlhf, evaluation, evals, adversarial. Source: raw/articles/2026-06-18_openai-alignment_openai-beneficial-rl.md.
- **concepts/norway-ai-school-ban.md** — Norway AI School Ban: Elementary AI Restrictions. Norway imposed near-ban on AI in elementary schools (Jun 19, 2026, Reuters). 691 HN points, 482 comments. Dual policy: student restrictions + teacher monitoring via Sikt AI platform. Part of growing global education AI regulation trend alongside EU AI Act. HN reactions: 1990s internet ban analogies, how-it's-used debate, AI leaders' personal choices. Tags: regulation, policy, education, ai-governance, europe, ai-safety. Source: raw/articles/2026-06-19_hn-discussion_norway-ai-school-ban.md.
- **concepts/spacex-cursor-acquisition.md** — SpaceX Acquires Cursor: $60B Coding Agent Acquisition. SpaceX to buy Anysphere/Cursor for $60B (Jun 16, 2026, SEC filings). #1 HN story (1142 pts, 1694 comments). SpaceX raised $75B 4 days prior, using 80% for this deal. Largest AI coding agent acquisition. Implications: market validation, vendor concentration, harness alternatives surge. Tags: acquisition, coding-agents, cursor, spacex, anysphere, ai-economics, valuation, startup. Source: raw/articles/2026-06-16_hn-discussion_spacex-cursor-acquisition.md (Reuters 403-blocked).
- **concepts/local-qwen-vs-claude-opus.md** — Local Qwen vs Claude Opus: Different Tools for Different Jobs. Alex Ellis deep-dive (Jun 17, 2026) on running Qwen 3.6 27B locally on RTX 6000 Pro. Core thesis: local Qwen is NOT a worse Opus — different tool with different strengths. Covers: benchmark gap reality (SWE-Bench 77.2 vs 88.6 but benchmaxxing critique), cost (GPU ROI in 2-3 months, Uber $1500/mo cap), sovereignty (Fable 5 vendor risk), practical limitations (looping, quantization degradation, no long-horizon autonomous work), and appropriate use cases. 120 lines. Tags: local-llm, qwen, open-source, coding-agents, claude, benchmark, inference, cost-optimization, on-device, gpu. Source: raw/articles/2026-06-18_alexellis_local-qwen-vs-opus.md.

#### 🆕 Entities
- **entities/john-jumper.md** — John Jumper: Nobel laureate (Chemistry 2024) for AlphaFold protein structure prediction. Led AlphaFold team at Google DeepMind. Announced move to Anthropic (Jun 18, 2026). Part of AI talent war: Nobel-caliber researcher migration from DeepMind to Anthropic. Tags: person, ai-researcher, anthropic, deepmind, google-deepmind. Source: raw/articles/2026-06-18_hn-discussion_john-jumper-anthropic.md.

### Updates
- **wiki/SCHEMA.md** — Added tags: spacex, anysphere (People/Orgs), acquisition (Meta)
- **wiki/index.md** — Added 5 new entries, updated header counts: Total 2612, Concepts 1742, Entities 824, Indexed 2207
- **wiki/log.md** — This entry

### Cross-Reference Notes
- GLM-5.2 (894 HN pts) and DeepSeek Vision (492 HN pts) already had recent wiki pages — skipped
- Fable 5 export controls extensively covered in concepts/claude/fable-5.md and raw articles — skipped
- 3 Reuters articles 403-blocked; used HN Algolia discussions as fallback sources
- Local Qwen subagent also added its own log/index entries (defiant subagent pattern); parent reconciled counts from filesystem
- 15 wikilinks fixed post-creation (broken entity/concept paths)
- 1 remaining intentional future link: concepts/emergent-misalignment (page not yet created)

---
## [2026-06-20] Newsletter Ingest — Minor enrichment (triage output parse failure, Case C recovery)

- **entities/alex-banks.md** — Added timeline entry: "How to run multiple tasks at once in Cowork" (Jun 2026) — parallel task execution patterns (branching/batch) and context file design. Updated: 2026-05-01 → 2026-06-20. Source: raw/newsletters/2026-06-19-how-to-run-multiple-tasks-at-once-in-cowork.md

Triage recovery: newsletter-triage output parse failed, but triage_latest.json checkpoint was valid (checkpoint_run_id: 20260620T071413Z). 3 newsletters processed: Robotic/Interconnects (1 reference), The Signal/Cowork (1 reference enriched), ASML beehiiv (batch skip). No take decisions.

---
## [2026-06-20] Concept Page Created — Local Qwen vs Claude Opus

- **concepts/local-qwen-vs-claude-opus.md** — New concept page synthesized from Alex Ellis's blog post "Local Qwen isn't a worse Opus, it's a different tool" (published 2026-06-17, ingested 2026-06-20). 215 lines. Covers: core thesis (different tool, not worse Opus), cost analysis (GPU ROI in 2-3 months, Uber $1500/mo cap, subsidized coding plans), sovereignty and vendor risk (Fable 5 withdrawal, air-gapped analysis), benchmark realism (SWE-Bench gap, benchmaxxing critique), practical limitations (looping, quantization degradation, unattended work risk), appropriate use cases (guided tasks, customer support, codebase reading), setup details (RTX 6000 Pro, llama.cpp, MTP speculative decoding), and concrete recommendations. Tags: local-llm, qwen, open-source, coding-agents, claude, benchmark, inference, cost-optimization, on-device, gpu, model-quantization, vendor-lock-in, privacy, agent-loop. Wikilinks: [[entities/alex-ellis]], [[concepts/qwen]], [[entities/qwen]], [[concepts/claude/index]], [[concepts/local-llm]], [[concepts/ai-benchmarks/benchmaxxing]]. Source: raw/articles/2026-06-18_alexellis_local-qwen-vs-opus.md.
- **index.md** — Added concepts/local-qwen-vs-claude-opus entry under Concepts section (alphabetical order, between local-llm/local-ai and long-running-search-agents).

---
## [2026-06-20] Blog Ingest — 4 AI-relevant articles enriched

**Pipeline:** blog-ingest → blog-triage → blog-wiki-ingest
**Run ID:** 20260620T070024Z
**Checkpoint:** ~/.hermes/cron/data/blog_ingest/latest.json

### Scan Summary
- Total new articles: 26
- Blog articles: 20
- Saved as raw: 14
- Unsaved (YouTube/Reddit/paywall): 6

### Triage Results
- **Takes (4):** Modal speculative decoding, Dwarkesh sample efficiency Part 2, Ed Zitron Silicon Valley Bubble Part 2, Cory Doctorow Big Con
- **References (0)**
- **Skips (10):** Non-AI articles (Bobby Prince, Arp 29, Jay Miner, Goldilocks principle, Kung-fu, Full Page Paralysis, Carlsberg, etc.)

### Enrichments Made

#### 🆕 Concepts Updated
- **concepts/speculative-decoding.md** — Added "Modal's Speculative Decoding Thesis (June 2026)" section: DFlash architecture, Qwen 3.5 1000 tok/s, Bitter Lesson framing, open-source engine parity, custom speculator training as "ML on easy mode". Updated: 2026-05-05 → 2026-06-20.
- **concepts/sample-efficiency.md** — Added "Part 2: The Data Black Hole Revisited (June 2026)" section: open models lag 4 months (Epoch), expert data industry scaling, genome argument rebutted, Chinchilla limits (~10x), white collar automation bet, deaf/blind intelligence argument. Updated: 2026-06-09 → 2026-06-20.

#### ✏️ Entities Updated
- **entities/modal-labs.md** — Added "Speculative Decoding Initiative (June 2026)" section: DFlash speculator release for Qwen 3.5, "Speculation Is All You Need" thesis, Z Lab partnership, Hugging Face releases. 51 → 78 lines. Updated: 2026-05-22 → 2026-06-20.
- **entities/dwarkesh-patel.md** — Added Part 2 to Notable Posts timeline and sources. Updated: 2026-06-09 → 2026-06-20.
- **entities/ed-zitron.md** — Added "The Silicon Valley Bubble Series (June 2026)" section: OpenAI $21B loss/$34B spend/$13B revenue, SoftBank dependency, accounting obfuscation, Cal Newport comparison, 4-part bubble thesis. 484 → 507 lines. Updated: 2026-06-16 → 2026-06-20.
- **entities/cory-doctorow.md** — Added "The Big Con — AI as Pyramid Scheme (June 2026)" section: pyramid scheme framing via Bridget Read, Uber CEO failure admission, Amway/Heritage Foundation connection. 152 → 172 lines. Updated: 2026-06-19 → 2026-06-20.

### Skipped Articles (Non-AI)
- Bobby Prince has died (oldvcr.blogspot.com) — Game music composer
- Arp 29: The fireworks galaxy (maurycyz.com) — Astronomy
- There Are No Instances in atproto (overreacted.io) — Dan Abramov on AT Protocol architecture
- The Goldilocks Principle in Fantasy Strategy (filfre.net) — Gaming
- Jay Miner, Atari and Amiga (dfarq.homeip.net) — Retro computing
- Full Page Paralysis (blog.jim-nielsen.com) — Web design essay
- I know Kung-fu (idiallo.com) — Essay on information vs knowledge
- Converting Coal Plants to Natural Gas (construction-physics.com) — Energy
- DaringFireball links (6 unsaved: YouTube, Reddit, WSJ paywall, NBC News)

---
## 2026-06-20 — X Article ingestion: Design Arena — GLM-5.2 vs Fable 5

**Source**: https://x.com/designarena/status/2068030598028087788
**Type**: X Article (tweet.fields=article, OAuth2)
**Author**: Design Arena (@Designarena) / Anmay Gupta (@Intelligence_ai)

- **Created**: `concepts/ai-benchmarks/design-arena.md` — New entity page for Design Arena, an LLM web design evaluation platform using head-to-head human preference voting. Covers Web Design, Game Dev, Data Visualization, 3D Design, UI Component leaderboards. Methodology includes template similarity clustering, dependency usage tracking, and error case analysis.
- **Updated**: `entities/glm-5-zai.md` — Added Design Arena Deep Dive section (June 19, 2026): behavioral analysis of GLM-5.2's #1 ranking. Three key patterns: high-quality expert templates, reliable dependency usage (TailwindCSS 91%, chart.js/three.js +6pp win rate), more intricate outputs (+25% code, 2x generation time). Trade-offs: speed vs quality Pareto frontier, #2 on Game Dev/Data Viz/3D behind Fable 5. Added raw article source.
- **Raw article**: `raw/articles/2026-06-19_designarena_glm-52-beat-fable-5-website-design.md`
- **Updated**: `index.md` — Added Design Arena entry in concepts/ai-benchmarks section.

---

## 2026-06-19 — X/Twitter article ingestion: Deli Chen AutoResearch

**Source**: https://x.com/victor207755822/status/2067259098584985954
**Type**: Note Tweet (long-form)
**Author**: Deli Chen (@victor207755822) — Deep Learning Researcher at DeepSeek

**Actions**:
- Created raw article: `raw/articles/2026-06-17_victor207755822_auto-research-skill-open-source-self-play.md`
- Created concept page: `concepts/auto-research.md` — AutoResearch framework, self-play, GRPO, continual learning
- Created entity page: `entities/deli-chen.md` — Deli Chen biography, research contributions
- Updated `index.md`: Added entities/deli-chen and concepts/auto-research entries

**Content summary**: AutoResearch SKILL open-sourced (June 17, 2026). 4th survey paper on self-play. AutoResearch Agent autonomously planned GPU experiments and submitted RL runs on DeepSeek 285B model. 100% automated RL pipeline. GRPO tool usage. Beginning of continual learning research journey.

---
## [2026-06-19] blog-wiki-ingest — 2 entity enrichments from blog triage

**Source**: blog-ingest (run_id: 20260619T070014Z)
**Triage outcome**: 0 takes, 3 references, 13 skips (Case C2 — triage produced valid decisions, cron output parse failed)

**Enrichments (references)**:
- [[entities/cory-doctorow.md]] — Added "AI Digital Sovereignty — The 'Problem + AI = Problem − AI' Framework (June 2026)" section. Doctorow applies his blockchain critique framework to AI sovereignty, arguing AI sovereignty fears distract from real US platform dependency risks. Raw article: pluralistic.net--2026-06-18-their-trillions-our-billions. Updated: 2026-05-27 → 2026-06-19.
- [[entities/entropicthoughts-com.md]] — Added timeline entry for "GLM 5.2 playing text adventures" (Jun 18, 2026). GLM 5.2 evaluated against Gemini 3 Flash on text adventure benchmarks with mixed-effects regression. Raw article: entropicthoughts.com--glm-5-2-playing-text-adventures. Updated: 2026-06-13 → 2026-06-19.
- [[entities/cursor-ai.md]] — Already fully updated (market share data on line 190, acquisition status correct). No enrichment needed.

**Archive**: Triage decisions saved to blog_ingest archive.

---
## 2026-06-19 — Newsletter wiki ingest (recovered from triage failure, 3 enrichments)

- **Pipeline recovery**: newsletter-triage upstream failed to parse JSON output. Checkpoint file at `triage_latest.json` contained valid triage decisions. 9 items: 3 takes, 3 references, 3 skips.
- **Enriched**: `entities/cursor-ai.md` — Updated SpaceX-Cursor Connection section to reflect formal acquisition agreement ($60B all-stock, signed June 16, closing Q3 2026). Added Deal Terms, Industry Context, Prior Right-to-Acquire subsections. Source: CNBC + Ben's Bites newsletter.
- **Enriched**: `entities/dean-ball.md` — Added OpenAI Career (July 2026) section. Dean Ball joining OpenAI as Head of Strategic Futures, effective July 6. Reports to Jason Kwon (Chief Strategy Officer). New Strategic Futures team focused on frontier AI policy.
- **Enriched**: `entities/semianalysis.md` — Expanded Datacenter Industry Model with proprietary three-model architecture (Datacenter Industry Model + Energy Model + Industrials Model, 550+ suppliers, 6,000+ facilities). Debunked Bloomberg/Sightline "half canceled" claim: denominator error, speculative pre-construction misinterpretation, Tier 1 continued on schedule.
- **References**: AINews GLM-5.2 (AA-Briefcase, Open Fable forecast, poolside Laguna M.1), Simon Willison Datasette Apps, Anjney Midha AMP interview.
- **Skipped**: 3 items (Elena Verna SaaS, Midjourney beehiiv 403 expired, True Positive Weekly pure link digest).
- **Archive**: Running archive_triage.py (newsletter pipeline).

---

## 2026-06-18 — Dreaming wiki ingest (recovered from triage failure, 4 enrichments)

- **Pipeline recovery**: dreaming-group upstream failed to parse JSON output. Checkpoint file at `triage_latest.json` contained valid decisions. 65 articles evaluated: 1 take, 3 references, 61 skips.
- **Enriched**: `entities/cohere.md` — Added LLM Serving Fairness section. Cohere's 4-layer scheduling architecture (Rate Limiter → Performance Tier → Deficit Round Robin → Priority Selector) for multi-tenant LLM serving. Request-based vs token-based budgeting, noisy-neighbor mitigation. +21 lines.
- **Enriched**: `entities/harvey.md` — Added Microsoft 365 Copilot Integration (June 2026) section. Harvey available as agent inside Copilot and Copilot Cowork. @Harvey in Copilot for legal answers, Vault retrieval, deep analysis escalation. Copilot Cowork multi-step workflows (opposition drafting, NDA document creation). +20 lines.
- **Enriched**: `entities/elevenlabs.md` — Added Multimodal Input Processing (June 2026) section. File-backed vs inline input paths, WhatsApp/Web/Mobile channels, Rohlik case study (90% auto-resolution). +21 lines.
- **Enriched**: `entities/langchain.md` — Added Trace Judge — Perceived Error Detection (June 2026) section. LangChain Labs × Fireworks AI collaboration on Qwen-3.5-35B fine-tuning. 96.1% accuracy, 10-100x cost reduction vs frontier models. Cross-domain transfer confirmed. +38 lines.
- **Cross-pipeline dedup**: Blog-triage already processed GLM-5.2, Kimi K2.7, LifeSciBench, AI Chemist (4 takes). Log.md showed 6+ pages ingested (Midjourney Medical, Agent Separation, ENPIRE, Deployment Sim, Vicki Boykis, George Hotz). Existing wiki pages covered 20+ articles.
- **Archive**: All skip/reference items previously archived (dedup).

---
## 2026-06-18 — SOC Episode 7 Wiki Ingestion (YouTube transcript)

---
## 2026-06-18 — Agent Separation of Duties concept page created

- **Source**: X/Twitter thread by @aakashgupta (2026-06-18), full article at news.aakashg.com
- **Raw Article**: `raw/articles/2026-06-18_agent-safety-separation-of-duties.md`
- **New Page**: `concepts/security-and-governance/agent-separation-of-duties.md` — Agent Separation of Duties concept page. Structural accountability pattern where worker model ≠ evaluator model. Independent convergence by OpenAI (/goal in Codex, Apr 2026) and Anthropic (Claude Code 2.1.139, May 2026). Worker executes; separate model judges completion from transcript. Based on centuries-old accounting separation-of-duties principle. Real-world results: bug backlog cleared in 31 unsupervised turns.
- **Index**: `index.md` — Added agent-separation-of-duties entry under Concepts > security-and-governance (2580 total, 1721 concepts)


- **Source**: [State of Agentic Coding #7](https://youtu.be/QqtW2q9ftu0) — Armin Ronacher and Ben Vinegar (Jun 12, 2026, 94:31)
- **Transcript**: `transcripts/2026-06-12_state-of-agentic-coding-ep7.md` + `.en.txt` + `.en.vtt` (2,481 segments, ~109K chars)
- **Raw article**: `raw/articles/2026-06-12_state-of-agentic-coding-ep7.md` — 8 chapters, key insights, notable quotes
- **Updated**: `concepts/coding-agents/state-of-agentic-coding.md` — Added episode 7 to table, insights, hosts trajectories, 3 new recurring themes (Language Elimination, Dead Internet, Local Models), 5 new predictions
- **Updated**: `entities/armin-ronacher.md` — Added SOC podcast section to Recent Themes
- **Updated**: `entities/ben-vinegar.md` — Added ep7 to episode list and key positions
- **Updated**: `wiki/index.md` — Concept page updated to 7 episodes, transcript entry added
- **Key ep7 themes**: Neither host practices autonomous looping; token spend as unprecedented dollar-correlated metric; Claude credits separating programmatic access; Bun Zig-to-Rust as most significant slop fork; Ruby/Zig as Louisiana French (human-first languages dying); DwarfStar 4 local model breakthrough; memory leak debugging failure (3 engineers, 24hrs, agents wrong); dead internet theory confirmed (90% agent-generated issues); fast fashion of software; concentration of power in 2 countries

---
## 2026-06-18 — Blog wiki ingest (recovered from triage failure, 1 reference enriched)

- **Pipeline recovery**: blog-triage upstream failed to parse JSON output. Checkpoint file at `triage_latest.json` contained valid decisions from prior run with 4 takes (already processed), 4 references, 12 skips.
- **Enriched**: `entities/george-hotz.md` — Added "Summoning the Demon" (Jun 17, 2026) reference entry: poetic essay on AI as "social crime" and "reflection of demonic desires." Updated frontmatter (updated: 2026-06-18, added raw article source).
- **Archive**: `archive_triage.py blog --keep-reference` — 16 items archived (4 references + 12 skips). Total archive URLs: 888.

---

## 2026-06-18 — Newsletter wiki ingest (4 newsletters, 2 takes, 1 reference)

- **Pipeline recovery**: Newsletter-triage cron output failed to parse but triage_latest.json was from yesterday's batch. Independently triaged 4 new newsletters from today's ingest (run_id=20260618T072217Z).
- **New Page**: `entities/midjourney.md` — Midjourney entity page. Covers company overview, Midjourney Medical scanner (full-body ultrasonic CT: 358K elements, 70cm ring, 17GB/s, 2 PFLOPS, 0.5mm resolution), Midjourney Spa (Union Square SF, 25K sq ft, 2027 target), business model, and self-funded status.
- **New Page**: `entities/radical-ai.md` — Radical AI entity page. Joseph Krause's AI-driven materials discovery company. Self-Driving Lab: 1200 alloys in 6 months (10x DARPA MACH speedup), 300 materials tested with 10 novel SOTA properties. Open-source: TorchSim, MATRIX/MATRIX-PT.
- **Updated**: `entities/nathan-lambert.md` — Added Mid-2026 career update: departure from Ai2, Interconnects AI LLC formation (Jan 2026), advising agreements with Arcee AI and Mercor, newsletter growth to 70K subscribers / ~900 paid.
- **Skipped**: GLM-5.2 beehiiv newsletter — Cloudflare challenge blocked all links; content already covered by entities/glm-5-zai.md.
- **Archive**: Newsletter triage saved to triage_latest.json (4 decisions: 2 takes, 1 reference, 1 skip).

---
## 2026-06-18 — Blog ingest triage (20 articles, 4 takes)

- **Triage**: 20 blog articles from 2026-06-17 blog-ingest checkpoint. 4 takes, 4 references, 12 skips.
- **New Page**: `concepts/ai-benchmarks/lifescibench.md` — OpenAI LifeSciBench benchmark (750 tasks, 173 Ph.D. contributors, 7 workflows, 7 biological domains). GPT-Rosalind 36.1% vs GPT-5.5 25.7% pass rate.
- **Updated**: `entities/glm-5-zai.md` — Added Simon Willison's independent review (Artificial Analysis #1, Code Arena #2, pricing, token hunger).
- **Updated**: `concepts/kimi-k2-7-code.md` — Added Together AI cost comparison (94% cheaper than Fable 5, design MCP server pattern).
- **Updated**: `entities/openai.md` — Added Near-Autonomous AI Chemist section (GPT-5.4 + Molecule.one Maria, Chan-Lam coupling, TEMPO additive, 10K reactions).
- **Rescraped**: `raw/articles/openai.com--index-ai-chemist-improves-reaction--f8a3c2d1.md` — Original scrape failed (403), rescued with user-agent header.
- **Checkpoint**: `~/.hermes/cron/data/blog_ingest/triage_latest.json` saved for downstream blog-wiki-ingest.

---

---
## 2026-06-18 — Deployment Simulation concept ingestion (OpenAI + Sierra)

- **Raw Articles Created**: `raw/articles/2026-06-11_openai_deployment-simulation.md`, `raw/articles/2025-08-19_sierra_simulations-the-secret-behind-every-great-agent.md`
- **Concept Created**: `concepts/deployment-simulation.md` — Three-actor pattern (user simulator + agent + judge) for testing AI agents via simulated conversations. Covers OpenAI research framework (200+ scenarios, safety degradation) and Sierra product platform (auto-generated tests, CI/CD integration, 35K tests/day).
- **Comparison Created**: `comparisons/openai-vs-sierra-agent-simulation.md` — Research framework vs product platform. Shared architecture, complementary perspectives. Maturity model: Level 0 (no testing) → Level 4 (continuous simulation in CI/CD).
- **Entity Updated**: `entities/sierra.md` — Added Agent Simulation Platform section with deployment simulation capabilities and cross-references.
- **Concept Updated**: `concepts/scenario-based-simulation.md` — Added cross-link to deployment-simulation concept.
- **Index Updated**: `index.md` — Added deployment-simulation concept (189 concepts section), openai-vs-sierra-agent-simulation comparison (31 comparisons).

---
## 2026-06-17 — X accounts scan: newsjack discovery (22:30 UTC)

- **Entity Updated:** `entities/elvis-sun.md` — Added Newsjack to "Currently Building" section and Timeline. Added [[concepts/newsjack]] cross-reference and source link. Updated 2026-06-17.
- **Page Created:** `concepts/newsjack.md` — Newsjack (Agent PR Skills). Open-source Go + Markdown skills framework by Elvis Sun that turns Claude Code / Codex / Hermes / OpenClaw into a full PR team. 428 ★, MIT license. Covers three-lane architecture (Detect/Act/Strategize), platform compatibility matrix, key design decisions, and relationship to Elvis Sun's PR ecosystem.
- **Source:** X post by @elvissun (2026-06-17): https://x.com/elvissun/status/2067037758296580296, linking to https://newsjack.sh and https://github.com/elvisun/newsjack
- **Index updated:** `concepts/newsjack` inserted alphabetically in index.md concepts section.
- **Cross-references:** [[elvis-sun]], [[concepts/harness-engineering]], [[entities/hermes-agent]], [[concepts/newsjacking-framework]], [[concepts/vibe-coding]].

---
## 2026-06-17 — dreaming-wiki-ingest (18:20 UTC)
- `entities/dario-amodei.md` — Enriched with "Policy on the AI Exponential" (Treebeard analogy, 5 policy areas, FAA-style regulation, MATCH/OVERWATCH). 29→145 lines.
- `entities/martin-alderson.md` — Added KV Cache Compression History (100× compression since 2017, MHA→MQA→GQA→MLA evolution, linear-attention hybrids). 232→261 lines.
- `concepts/evaluation/agent-evaluation-methodology.md` — Added Lee Han-chung evaluation infrastructure framework (RL 5-tuple, rollouts/traces, state infrastructure, checkpoint/replay, evaluation debt). 210→336 lines.
- `entities/fireworks-ai.md` — Added Inference Providers vs API Routers subsection (direct providers vs proxies, performance analysis, DPA/sovereignty, verification methods). 213→289 lines.
- `entities/calvin-french-owen.md` — Created entity skeleton from "Reflections on OpenAI." 25 lines.
---
## 2026-06-17 — AG2/AutoGen concept page creation

- **Page Created:** `concepts/ag2-autogen.md` — Comprehensive concept page covering AG2/AutoGen (Microsoft's open-source multi-agent framework). Covers history (v0.2 → v0.4 → AG2 rebrand → maintenance mode), architecture (AgentChat/Core/Extensions/Studio layers), key features (multi-agent conversations, code execution, HITL, tool use, distributed execution), comparison with LangGraph/CrewAI/OpenAI Agents SDK/Microsoft Agent Framework, and adoption & ecosystem context.
- **Sources:** 3 raw articles (LangChain framework philosophy, Microsoft Agent Framework v1.0, Agent Governance Toolkit) + AutoGen official docs and GitHub README.
- **Cross-references:** [[entities/microsoft-agent-framework]], [[entities/microsoft]], [[concepts/langgraph]], [[concepts/crewai]], [[concepts/openai/agents-sdk]], [[concepts/multi-agents/multi-agent]], [[concepts/multi-agents/agent-orchestration-frameworks]], [[concepts/microsoft-agent-governance-toolkit]], [[concepts/mcp]].
- **Index updated:** Entry inserted alphabetically at concepts section.

---
## 2026-06-17 — sovereign-ai concept page creation

- **Page Created:** `concepts/sovereign-ai.md` — Comprehensive concept page covering national LLM initiatives (GPT-NL, GPT-SW3, Rio/Nex-N2 controversy), drivers (data sovereignty, strategic autonomy, economic competitiveness, national security), infrastructure (sovereign cloud, on-premise, datacenter sovereignty debate), Cohere's sovereign AI push (Reliant AI acquisition, Indra Group MOU), challenges (model quality vs independence, cost, talent shortage, model merge controversies), and relationship to EU AI Act and AI regulation.
- **Sources:** 4 raw articles (Cohere blog ×3, Martin Alderson datacenter sovereignty analysis).
- **Cross-references:** [[entities/cohere]], [[entities/mistral-ai]], [[concepts/eu-ai-act]], [[concepts/ai-regulation-2026]], [[concepts/korean-ai]], [[concepts/enterprise-ai-operating-model]].
- **Index updated:** concepts/sovereign-ai added to index.md under Concepts section (alphabetical order).

---
## 2026-06-17 — blog-wiki-ingest (07:50 UTC)

- **Pages Updated (3 reference items):**
  - `entities/georgi-gerganov.md` — Added Local Coding Workflow section (Qwen3.6-27B daily usage, pi agent lightweight harness). Updated 2026-06-17.
  - `entities/steve-blank.md` — Added Spring 2026 Stanford Lean LaunchPad AI data (8 teams, 978 interviews, "team hallucination" observation). Updated 2026-06-17.
  - `entities/gilesthomas.md` — Added Flax Debugging: Making a Hash of Things subsection under JAX Exploration (parameter hashing debugging technique, @jax.jit vs @nnx.jit pitfall). Updated 2026-06-17.
- **Articles archived:** All 20 blog articles from ingest checkpoint processed (3 reference, 17 skip — already archived in pipeline).
- **Triage checkpoint:** blog-triage JSON recovered from pipeline checkpoint despite cron output parse failure.

---
## [2026-06-17] Newsletter wiki ingest

- **Action**: Enriched entity and concept pages with SemiAnalysis RL Systems article data
- **Source**: raw/articles/2026-06-16_semianalysis_rl-systems-throughput.md — SemiAnalysis "RL Systems: Mind the Gap" (Jun 2026)
- **Pages created**: None (entity already existed)
- **Pages updated**:
  - `entities/semianalysis.md` — updated tags to canonical [organization, research, infrastructure, blog, ai-economics]; added Key People section (Dylan Patel, Myron Xie, Daniel Nishball, Prime Intellect/Modal collaborators); added Key Research Areas (GPU Economics, AI Infrastructure, RL Training Systems); added RL Systems publication to Key Publications (+ other publications remain); added RL Systems article to sources
  - `concepts/post-training/grpo-infrastructure.md` — added SemiAnalysis Throughput Matching Framework section (Three-Actor Model, Queue Model, PipelineRL Asynchrony, Group Size Impacts, Sandbox Challenges, Throughput Optimizations, Policy Staleness Tolerance); added RL Systems article to sources
  - `concepts/post-training/asynchronous-rl.md` — added SemiAnalysis PipelineRL & Throughput Matching section (PipelineRL In-Flight Weight Syncing comparison table, Throughput Matching as Async Framework, Policy Staleness in PipelineRL, Group Size and Throughput); added RL Systems article to sources
  - `index.md` — updated SemiAnalysis entity entry description with RL Systems, key people, research areas
- **Key details**: SemiAnalysis RL Systems article introduces generator/trainer throughput matching, PipelineRL asynchrony with in-flight weight pushing, queue model for production rate balancing, sandbox challenges (startup latency via Modal, concurrency scaling, robustness), group size guidelines (N=8/16/64), and throughput optimizations (early pruning, adaptive sampling). Collaborators include Prime Intellect (Matej Sirovatka, Ameen Patel, Sami Jaghouar) and Modal (Peyton Walters, Nan Jiang, Erik Dunteman).

---
## [2026-06-17] Newsletter wiki ingest

- **Action**: Enriched GLM-5 entity page with GLM-5.2 data; created IndexShare concept page
- **Source**: raw/articles/2026-06-17_ainews_glm-52-indexshare.md
- **Pages updated**:
  - `entities/glm-5-zai.md` — Added GLM-5.2 specs (744B MoE, 40B active, MIT, 1M ctx), benchmark data (#1 Design Arena, #3 FrontierSWE, first >80% Terminal-Bench), IndexShare mention, ecosystem support
  - `index.md` — Updated GLM-5 entry with key stats; added IndexShare concept entry
- **Pages created**:
  - `concepts/index-share.md` — IndexShare technique extending DeepSeek Sparse Attention, reuses one indexer across four sparse layers
- **Key details**: GLM-5.2 released June 17, 2026 by Z.ai. 744B MoE, MIT license, 1M context, two reasoning modes (high/max), IndexShare for sparse attention efficiency, MTP speculative decoding improvements

---
## [2026-06-17] Zvi Mowshowitz — Entity Page Creation

- **Action**: Created entity page for Zvi Mowshowitz / Don't Worry About the Vase blog
- **Source**: https://thezvi.wordpress.com/, https://thezvi.wordpress.com/about/, RSS feed
- **Pages created**: `entities/zvi-mowshowitz.md` — comprehensive entity covering blog, perspectives on AI safety/model welfare/policy, writing style
- **Pages updated**:
  - `index.md` — added entity entry (alphabetically between zach-tratar and zakirullin)
  - `config/feeds/blogs.opml` — added RSS feed for blog monitoring (85 blogs total)
- **Key details**: Substack primary + WordPress mirror, ~5 posts/week, weekly AI numbered series, deep model welfare coverage

---
## [2026-06-17] OpenAI Insider Reflections — Concept Page Creation

- **Action**: Created concept page for OpenAI insider reflections article
- **Source**: https://calv.info/openai-reflections
- **Pages created**: `concepts/openai/reflections-on-openai.md` — comprehensive concept covering OpenAI's internal culture, Python monorepo, Azure infrastructure, and 7-week Codex development sprint
- **Pages updated**:
  - `index.md` — added concept entry (alphabetically between realtime-voice-models and responses-api)
  - `raw/articles/openai-reflections.md` — raw article saved
- **Key details**: Calvin French-Owen's firsthand account (Segment founder → OpenAI engineer, 2024-2025). Covers Slack-centric communication, bottom-up research culture, meritocracy, rapid direction changes, secrecy, safety focus, Meta→OpenAI pipeline, and Codex launch details (630K PRs in 53 days).

---
## [2026-06-17] ChatGPT Memory Dreaming — Concept Page Creation

- **Action**: Created concept page for ChatGPT memory dreaming system
- **Source**: https://openai.com/index/chatgpt-memory-dreaming/
- **Pages created**: `concepts/openai/chatgpt-memory-dreaming.md` — comprehensive concept covering OpenAI's scalable memory synthesis system evolution from saved memories to Dreaming V3
- **Pages updated**:
  - `index.md` — added concept entry (alphabetically between aws-bedrock-partnership and frontier-governance-framework)
- **Key details**: Automatic memory synthesis from conversation history, addresses staleness/correctness/scalability, evolution from explicit saved memories (2024) to background dreaming (2025) to standalone system (2026). Evaluations show improved context carry-forward, preference following, and temporal awareness.

---
## [2026-06-17] OpenAI WebRTC Audio Session — Concept Page Creation

- **Action**: Created concept page for OpenAI WebRTC audio session playground
- **Source**: https://simonwillison.net/2026/Jun/12/openai-webrtc/
- **Pages created**: `concepts/openai/webrtc-audio-session.md` — browser-based playground for realtime audio conversations using GPT-Realtime-2 model with document context input
- **Pages updated**:
  - `index.md` — added concept entry (alphabetically between tanstack-supply-chain-2026 and openclaw)
- **Key details**: Simon Willison's tool demonstrating OpenAI's WebRTC API for realtime audio interactions. Supports GPT-Realtime-2 model with GPT-5-class reasoning and document context for conversational exploration of text content.

---
## [2026-06-17] OpenAI vs Anthropic Enterprise Adoption — Concept Page Creation

- **Action**: Created concept page for enterprise adoption patterns comparison
- **Source**: https://x.com/JayaGup10/status/2065266818810527770
- **Pages created**: `concepts/openai/enterprise-adoption-patterns.md` — Fortune 500 deployment patterns showing ChatGPT as org-wide default vs Claude for power users
- **Pages updated**:
  - `index.md` — added concept entry (alphabetically between chatgpt-memory-dreaming and frontier-governance-framework)
- **Key details**: Enterprise adoption pattern where ChatGPT serves as organization-wide default while Claude is ring-fenced for power users due to variable-cost fear and capability mismatch perception.

---
## [2026-06-17] AI for Alzheimer's Initiative — Concept Page Creation

- **Action**: Created concept page for OpenAI Foundation's Alzheimer's research initiative
- **Source**: https://openaifoundation.org/news/ai-for-alzheimers
- **Pages created**: `concepts/openai/ai-for-alzheimers.md` — $100M+ initiative for Alzheimer's research using AI across six institutions
- **Pages updated**:
  - `index.md` — added concept entry (alphabetically between agents-sdk and aws-bedrock-partnership)
- **Key details**: Five-layer research stack: causal mapping, drug design, biomarker discovery, clinical collaboration, off-patent treatment testing. Collaborators include Arc Institute, University of Washington, UCSF, Harvard Medical School.

---
## [2026-06-17] Economic Futures in the Age of AI — Concept Page Creation

- **Action**: Created concept page for OpenAI Foundation's economic futures initiative
- **Source**: https://openaifoundation.org/news/economic-futures-in-the-age-of-ai
- **Pages created**: `concepts/openai/economic-futures-age-of-ai.md` — $250M initiative for economic futures in the age of AI
- **Pages updated**:
  - `index.md` — added concept entry (alphabetically between enterprise-adoption-patterns and frontier-governance-framework)
- **Key details**: Three pillars: understanding the shift, supporting the transition, and building for long-term economic security. Focus on worker agency, government capacity, and new economic models including sovereign wealth funds and taxation shifts.

---
## [2026-06-17] Newsletter wiki ingest

- **Action**: Created entity page for Finbarr Timbers and enriched Nathan Lambert page with post-training recipe interview
- **Source**: `raw/articles/2026-06-16_interconnects_post-training-recipe-review.md`
- **Pages created**: `entities/finbarr-timbers.md` — comprehensive entity covering background (ex-DeepMind, Midjourney, Ai2), post-training contributions (Tülu 3, OLMo 3), MOPD expertise, and RL recipe evolution timeline
- **Pages updated**:
  - `entities/nathan-lambert.md` — added sources frontmatter (+raw article), new subsection "Interconnects Podcast #18 — Finbarr Timbers Interview" covering recipe evolution timeline, MOPD pattern details, and models discussed
  - `index.md` — added Finbarr Timbers entity entry (between filfre-net and fireworks-ai)
- **Key details**: MOPD is the dominant 2026 post-training pattern: train N domain-specialist teachers, train one general student by sampling its own trajectories, minimize reverse-KL to the relevant teacher per rollout. Lineage: MiMo Flash v2 → DeepSeek V4 & Nemotron 3 Ultra (10+ teachers).

---
## [2026-06-17] Active Crawl — 4 New Pages

**Sources**: HN Algolia, X/Twitter (xurl), blogwatcher DB, wiki gap analysis

### Pages Created

- **[[concepts/multi-objective-policy-distillation]]** — Multi-Objective Policy Distillation (MOPD): the dominant 2026 post-training pattern. Train N domain-specialist teachers (each SFT→RL), distill into one general student via reverse-KL on on-policy rollouts. Covers IcePop (logit masking), Full-Vocabulary Distillation, Write-Ahead Log fault tolerance. Adopted by MiMo-V2-Flash, GLM-5, Nemotron-Cascade 2, DeepSeek-V4.
  - Sources: `raw/articles/2026-05-04_multi-teacher-on-policy-distillation.md`, `raw/articles/2026-06-08_chinmaykarkar_opd-survey-2026.md`, `raw/articles/2026-06-16_interconnects_post-training-recipe-review.md`
  - Cross-references: [[concepts/multi-teacher-on-policy-distillation]], [[concepts/model-distillation]], [[concepts/grpo]], [[entities/nathan-lambert]], [[entities/finbarr-timbers]]

- **[[concepts/sovereign-ai]]** — Sovereign AI: national LLM initiatives, data sovereignty, and the global push for domestic AI infrastructure. Covers GPT-NL (Netherlands/TNO, 222 HN pts), GPT-SW3 (Sweden), Rio/Nex-N2 controversy (Brazil, 402 HN pts), Cohere's sovereign enterprise AI strategy, datacenter sovereignty debate, EU AI Act relationship.
  - Sources: `raw/articles/2026-05-20_cohere_cohere-acquires-reliant-ai-expand-sovereign-enterprise-ai.md`, Martin Alderson datacenter sovereignty analysis
  - Cross-references: [[entities/cohere]], [[entities/mistral-ai]], [[concepts/eu-ai-act]], [[concepts/ai-regulation-2026]]

- **[[concepts/ag2-autogen]]** — AG2 / AutoGen: Microsoft's open-source event-driven multi-agent framework. Actor model architecture with AgentChat (high-level) and Core (low-level) layers. History: v0.2 (2023) → v0.4 (2024) → AG2 rebrand (2025) → maintenance mode (April 2026), succeeded by Microsoft Agent Framework.
  - Sources: raw articles from LangChain agent framework analysis, Microsoft Agent Framework v1.0 announcement, Agent Governance Toolkit
  - Cross-references: [[concepts/langgraph]], [[concepts/crewai]], [[concepts/openai/agents-sdk]], [[entities/microsoft]], [[concepts/multi-agents/multi-agent]]

- **[[entities/groq]]** — Groq: LPU (Language Processing Unit) inference provider. Custom ASIC architecture for ultra-low-latency LLM inference. Founded by ex-Google TPU engineers. Key competitor to GPU-based inference (vLLM, Together AI, Fireworks). Recent expansion beyond inference into cloud platform.
  - Sources: groq.com, web research
  - Cross-references: [[entities/together-ai]], [[entities/fireworks-ai]], [[entities/cerebras]], [[concepts/inference-engines]], [[concepts/vllm]]

### HN Trends (June 13-17)
- Fable 5 US government access suspension (3,148 pts) — AI safety/policy
- SpaceX to buy Cursor for $60B (1,040 pts) — largest AI tooling acquisition
- Local models replacing Claude/GPT for coding (1,261 pts) — open models trend
- GPT-NL sovereign LLM for Netherlands (222 pts) — sovereign AI wave
- Qwen-Robot Suite foundation models for physical AI (183 pts)

### Wiki Gap Analysis
- HIGH priority gaps addressed: MOPD (concept), Sovereign AI (concept), AG2/AutoGen (concept), Groq (entity)
- Remaining HIGH gaps: NVIDIA ENPIRE (no accessible source), RLAIF (concept needed)

---

## 2026-06-17 — wiki-watchdog-fix (17:35 UTC)

- **Auto-fixed (2):**
  - `index.md` summary line: Total pages 2530→2574, Indexed entries 2530→2183, added Not in index: 391
  - `log.md`: Added 13 missing `---` separators between consecutive section headers
- **Verified clean:**
  - Pipe corruption: 0 | Line prefix corruption: 0 | Triple brackets: 0 | Space prefix: 0
  - Duplicate entries: 0 | Ghost entries: 0 | Japanese filenames: 0
  - Log separators: 0 missing | validate_index.py: clean
- **Deferred (human review):**
  - `x_accounts` job stale (26h) — last run ~16h UTC Jun 16, needs investigation
  - 504 missing concept entries in index.md — large batch (>50), needs dedicated pass
---
## 2026-06-17 — Machine Studying article ingestion

### Created
- `concepts/machine-studying.md` — Machine Studying concept page (Li, Battle, Khattab, MIT CSAIL, Jun 2026). Three paradigms for agents developing expertise from corpora: self-supervised objectives, synthetic data/environments, amortized context management. StudyBench benchmark.
- `entities/jacob-xiaochen-li.md` — Jacob Xiaochen Li entity page (MIT CSAIL, Machine Studying co-author)
- `raw/articles/2026-06-17_jacobxli_machine-studying.md` — Raw article from jacobxli.com

### Updated
- `entities/omar-khattab.md` — Added Machine Studying (2026) section and See Also link
- `index.md` — Added 3 new entries, updated page counts (2576 total, 813 entities, 1719 concepts)

### Source
- https://jacobxli.com/blog/2026/machine-studying/

- 2026-06-18 update concepts/post-training/rl-algorithms-for-llm-training.md — add GSPO section (arXiv 2507.18071, Qwen Team)

---
## 2026-06-18 — Ingest Vicki Boykis "Running local models is good now"

**Source**: https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/

**New pages:**
- `entities/vicki-boykis.md` — Data scientist, local LLM practitioner, blogger
- `entities/lm-studio.md` — Desktop app for local LLM inference with OpenAI-compatible API

**Updated pages:**
- `entities/gemma-4.md` — Added Vicki Boykis source reference and See Also link
- `entities/gpt-oss.md` — Added Vicki Boykis See Also link
- `concepts/local-llm/_index.md` — Added LM Studio to inference engine table, Vicki Boykis to Key Figures
- `index.md` — Added Vicki Boykis and LM Studio entries

**Deleted:**
- `concepts/local-llm-inference.md` — Redundant with existing `concepts/local-llm/_index.md`

---
## 2026-06-18 — ENPIRE concept page created

**Created:**
- `concepts/enpire.md` — ENPIRE (Agentic Robot Policy Self-Improvement) concept page. NVIDIA GEAR Lab system bridging coding agents (Codex, Claude Code, Kimi Code) with physical robotics through auto-evaluation and auto-reset environment loop. 99% success rate on dexterous manipulation tasks.

**Updated:**
- `index.md` — Added ENPIRE entry under Concepts section, updated page counts

---
## 2026-06-18T11:17:44Z — Active Crawl: 3 new concept pages

**Source**: HN Algolia, xurl (X/Twitter), blogwatcher DB, wiki gap analysis
**Topics discovered**: 15 HN stories, 10 X/Twitter results, 30 wiki gap assessments
**Pages created**:
- `concepts/glm-5-2.md` — GLM-5.2: 744B MoE open-weights LLM (40B active, MIT license, 1M context) by Z.AI/Zhipu AI. #1 open-weights on Artificial Analysis Intelligence Index v4.1 (score 51). Sources: Simon Willison, Artificial Analysis, Fireworks AI, AINews.
- `concepts/enpire.md` — ENPIRE: NVIDIA GEAR Lab's system where coding agents (Codex, Claude Code, Kimi Code) autonomously develop robot manipulation policies via environment loop (auto-eval + auto-reset). 99% success on dexterous tasks. Sources: NVIDIA GEAR Lab, X/@DarthUtopian.
- `concepts/security-and-governance/agent-separation-of-duties.md` — Agent Separation of Duties: safety architecture pattern independently adopted by OpenAI (/goal in Codex, Apr 2026) and Anthropic (Claude Code 2.1.139, May 2026). Worker-evaluator structural separation. Sources: Aakash Gupta X thread, news.aakashg.com.
**Raw articles saved**: 6 (3 new + 3 pre-existing referenced)
**Index/log**: index.md updated with corrected counts (1720 concepts, 820 entities, 2585 total)

---

## 2026-06-18 — Wiki watchdog auto-fix

- **Auto-fixed**: Removed 8 duplicate entries from index.md (managed-agents, claude-design, deep-learning, gpt-5-system-card, gpt-deep-research-system-card, grpo-rl-training, isaac-flath, transcripts cheat-at-search)
- **Auto-fixed**: Updated index header counts to match actual files (822 entities, 1732 concepts, 2599 total)
- **Pipeline health**: No pipeline_watchdog alerts. No wiki_health report found. Graph analysis (2026-06-12) identified 329 thin pages and 10 high-similarity pairs — needs human review.
- **Note**: ~516 concept pages and ~9 entity pages exist on filesystem but lack index.md entries — index regeneration recommended.

---

## 2026-06-18 — Wiki watchdog auto-fix (2nd run)

- **Auto-fixed**: Removed 1 ghost entry from index.md (`concepts/anthropic/model-context-protocol` — no backing file)
- **Auto-fixed**: Added 7 missing `---` separators in log.md between consecutive section headers
- **Auto-fixed**: Updated index.md header counts (Indexed entries: 2599→2189, Not in index: 0→410)
- **Verified clean**: Pipe corruption: 0 | Line prefix corruption: 0 | Triple brackets: 0 | Space prefix: 0
  Duplicate entries: 0 | Ghost entries: 0 | Log separators: 0 missing | validate_index.py: clean
- **Deferred (human review)**: ~410 missing concept/entity entries in index.md — large batch (>50), needs dedicated pass

---
## [2026-06-19] Active Crawl — 4 New Concept Pages

- Created `concepts/deepseek-vision.md` — DeepSeek Vision multimodal capabilities launch (June 2026)
- Created `concepts/mcp-enterprise-oauth.md` — MCP enterprise OAuth managed authentication
- Created `concepts/ai-governance-political-pressure.md` — Anthropic-Trump political pressure case study
- Created `concepts/ai-industry-financial-sustainability.md` — OpenAI financials and Herbalife Moment economics critique
- Sources: HN Algolia trending stories, X/Twitter search, blogwatcher DB scan
- Coverage gaps addressed: multimodal (priority 1), MCP protocols (priority 3), AI regulation/policy (priority 2), industry economics
- Total wiki pages: 2599 → 2603
---

## [2026-06-19] Weekly Wiki Graph Analysis

- Ran comprehensive graph analysis (scanning 2,105 pages)
- Found:
  - 36 content-rich orphan pages with no inbound links
  - 4,597 broken wikilinks (933 fixable, 3,664 truly missing targets)
  - 32 potential duplicate groups (4 entity↔entity, 28 entity↔concept)
  - 472 pages not in index.md, 394 stale index entries
  - 185 oversized pages (>200 lines), 7 tag violations
  - 674 pages (32%) missing sources field
- Saved report to: `wiki/queries/wiki-graph-analysis-weekly-2026-06-19.md`
- Updated index.md (added to Queries section)
---

## 2026-06-19 — wiki-watchdog-fix (17:35 UTC)

- **Auto-fixed (2):**
  - `wiki/index.md` — Restructured section boundaries: ~1160 concept entries that had spilled into Events section (under `## Events (11 pages)`) were moved back under `## Concepts (1736 pages)`. Concepts section went from 11→1170 entries. Events section corrected to 11 entries (matching 11 files on disk).
  - `wiki/log.md` — Removed duplicate `---` separator and cleaned up pipe character artifacts from previous patch attempts.
- **Updated:**
  - `wiki/index.md` header — Total pages 2603→2661, Indexed entries 2194→2196, Concepts 1736→1716
- **Verified clean:**
  - Pipe corruption: 0 | Line prefix corruption: 0 | Triple brackets: 0 | Space prefix: 0
  - Duplicate entries: 0 | Ghost entries: 0 | Log separators: 0 missing
  - Tag violations (non-canonical): 0 on Layer 2 pages
- **Deferred (human review):**
  - `x_accounts` job stale (26h) — recurring alert, was also noted Jun 17 and Jun 18
  - ~465 concept entries missing from index.md (need human-driven index regeneration)
  - 36 content-rich orphan pages with zero inbound links (needs human review)
  - 933 fixable cross-namespace wikilinks (across many files — exceeds 10-file threshold)
  - 4 entity↔entity duplicate pairs: deliberate-coder/deliberatecoder, eugene-yan/eugeneyan, lilian-weng/lilianweng, samuel-colvin/samuelcolvin


---

## [2026-06-20] Watchdog Auto-Fix - 8 log separator fixes

**Pipeline:** wiki-watchdog-fix cron (17:35 UTC)

### Auto-Fixed
- ✅ **Log separators**: Added 8 missing `---` separators between consecutive `##` section headers in wiki/log.md

### Verified Clean (no action needed)
- ✅ Pipe corruption: 0 | Line prefix corruption: 0 | Triple brackets: 0 | Space prefix: 0
- ✅ Duplicate entries: 0 | Ghost entries: 0
- ✅ Header consistency: Total=2612 Indexed=2207 NotIn=405 (OK)
- ✅ Section boundaries: Clean (Concepts 1742, Events 11, no mixing)
- ✅ validate_index.py: Passes
- ✅ _index.md files: No corruption detected

### Needs Attention (human review)
- ⚠️ ~507 concept entries missing from index (filesystem: 1742 files, indexed: 1230 entries) - deferred batch-add
- ⚠️ 30 orphan pages (no inbound links) - 8 are _index.md files (expected), 22 content pages need review
- ⚠️ Stale graph analysis (26h) - weekly run produced 21 issues across 7 categories
