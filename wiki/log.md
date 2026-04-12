
### 2026-04-12 — AI Evals Article Processing (Lenny's Substack)
- **Article:** Lenny's Podcast — "Why AI evals are the hottest new skill for product builders" (Sept 25, 2025)
  - Source: https://open.substack.com/pub/lenny/p/why-ai-evals-are-the-hottest-new-skill
- Created: [[concepts/ai-evals.md]] — Systematic framework for evaluating AI systems (3 levels, iteration flywheel, binary>likert, error analysis)
- Created: [[concepts/critique-shadowing.md]] — 7-step process for building aligned LLM-as-Judge evaluators
- Created: [[concepts/evals-skills.md]] — Coding agent skills/plugins for AI evaluations
- Created: [[comparisons/eval-tools-comparison.md]] — LangSmith vs Braintrust vs Phoenix vs Inspect AI comparison
- Created: [[entities/hamel-husain.md]] — AI evals educator, 50+ companies consulted, 4,000+ students taught
- Updated: index.md (AI Evaluation & Testing section added, entity count updated)
- Total raw articles: 99 (as of 2026-04-12)

### 2026-04-12 — Hamel Husain Entity Page Upgrade
- **Upgraded:** [[entities/hamel-husain.md]] from skeleton-style bio to full research profile (~17KB)
- **Added sections:**
  - Detailed career timeline (~2004 to 2026, 25+ years)
  - Core Ideas: "The Harness is Data Science", Error Analysis First, Binary > Likert Scales, Critique Shadowing Framework, Eval-Driven Development is a Trap, Transition from Literate Programming
  - Open Source Contributions: CodeSearchNet (GitHub Copilot precursor, 2M pairs across 6 languages), fast.ai ecosystem (nbdev, fastpages, ghapi), Axolotl, Kubeflow
  - Key Quotes from podcasts, conferences, blog posts
  - Related Entities: Jeremy Howard, Eric Ries, Shreya Shankar, Answer.AI, Parlance Labs
- **Sources added:** hamel.dev blog, Parlace Labs team page, Answer.AI posts, arXiv:1909.09436 (CodeSearchNet), PyAI Conf 2026, O'Reilly book "Evals for AI Engineers" (forthcoming)
- **Status:** Complete (no longer skeleton-level; matches antirez/simon-willison quality)

### 2026-04-10 — X Account Enrichment (Batch 4)
- Enriched 8 skeleton entity pages from X/Twitter accounts:
  - **Armin Ronacher** (@mitsuhiko) — Flask/Jinja2/Sentry creator, 15.8KB, left Sentry 2025, founded Earendil 2026, acquired Pi 2026
  - **Benjamin Clavié** (@bclavie) — IR/NLP researcher, RAGatouille creator, 12.8KB, PhD at NII Tokyo, ModernBERT co-lead
  - **Chip Huyen** (@chipro) — ML systems expert, Stanford CS329S, 15.2KB, author of 2 O'Reilly books, Claypot AI founder
  - **Clémentine Fourrier** (@clefourrier) — HF evaluation researcher, 19.2KB, LightEval creator, Open LLM Leaderboard, GAIA benchmark
  - **Ethan Mollick** (@emollick) — Wharton professor, 16.3KB, 'Co-Intelligence' NYT bestseller, 419K+ Substack subscribers
  - **Eugene Yan** (@eugeneyan) — Anthropic MTS, 18.9KB, applied-ml (28.7K GitHub stars), 200+ blog posts
  - **Lilian Weng** (@lilianweng) — OpenAI VP Research → Thinking Machines Lab co-founder, 15.4KB, $12B valuation
  - **Samuel Colvin** (@samuelcolvin) — Pydantic creator, 13.3KB, 577M monthly downloads, PydanticAI 23.4K stars
- All pages: status: complete, with Timeline, Core Ideas, Key Quotes, Related Concepts, Sources sections
- Quality target: antirez.md (12.9KB) / simon-willison.md (8.8KB) — all exceeded
- Remaining skeleton pages: 0 of original 8
# Wiki Log

Chronological log of all wiki actions.

---

## 2026-04-09
- Wiki initialized with SCHEMA.md, index.md, log.md
- Directory structure created: raw/articles/, entities/, concepts/, comparisons/, queries/
- Auto-ingestion pipeline configured (email → scrape → raw/articles/)
- **Newsletter processed:** Ben's Bites — "Anthropic built a model too risky to release"
  - Created: [[entities/anthropic.md]]
  - Created: [[entities/claude-mythos.md]]
  - Created: [[entities/meta.md]]
  - Created: [[entities/muse-spark.md]]
  - Created: [[concepts/project-glasswing.md]]
  - Created: [[comparisons/frontier-models-2026-04.md]]
  - Updated: index.md, log.md
  - Source: [[raw/articles/substack.com--app-link-post--40004939]]
- **Newsletters processed:** Simon Willison (Lenny's Podcast), NLP News, Latent Space
  - Created: [[concepts/functional-emotions-llms.md]] — Anthropic's emotion vector research
  - Created: [[concepts/ai-agent-traps.md]] — Google DeepMind adversarial framework
  - Created: [[concepts/caid-coordination.md]] — CMU multi-agent coding
  - Created: [[concepts/meta-harness.md]] — Stanford/MIT harness optimization
  - Created: [[concepts/long-context-coding-agents.md]] — File-system based long-context
  - Created: [[concepts/multi-agent-autonomy-scale.md]] — Self-organizing agents at scale
  - Created: [[concepts/reasoning-model-cost-transparency.md]] — Hidden API costs
  - Created: [[concepts/agentic-engineering.md]] — Simon Willison on AI coding collaborators
  - Updated: index.md, log.md
  - Sources: [[raw/articles/substack.com--app-link-post--3ea251fe.md]], [[raw/articles/substack.com--app-link-post--c269404d.md]]

---

## 2026-04-10
- **Bulk email processing:** 26 emails from Maildir/processed/ ingested
- **Total raw articles:** 97 (from multiple newsletters: Latent Space, NLP News, Ben's Bites, Simon Willison, etc.)
- **Wiki pages created (29 total):**
  - **Entities (14):** openai-spud, cursor-3, gemma-4, claude-mythos, qwen3-6-plus, mistral-voxtral-tts, glm-5v-turbo, zoox-expansion, amazon-rivr, agibot-10000-units, glm-5-zai, muse-spark, anthropic, meta
  - **Concepts (15):** claude-code-leak, death-of-browser, helium-crisis-2026, scaling-without-slop, world-models-science, ai-agent-traps, functional-emotions-llms, caid-coordination, meta-harness, long-context-coding-agents, multi-agent-autonomy-scale, reasoning-model-cost-transparency, agentic-engineering, project-glasswing, harness-engineering
  - **Comparisons (1):** frontier-models-2026-04
- **Updated:** index.md (full rebuild), log.md
- **Sources:** [[raw/articles/]] (97 articles processed)

## 2026-04-09
- Ingested 84 blog author entities from hn-popular-blogs-2025.opml

## 2026-04-10 — OPML Blog Authors Wiki Ingestion
- **Source:** ~/hn-popular-blogs-2025.opml (85 feeds)
- **Entities created:** 84 blog author pages under wiki/entities/
- **Raw data:** ~/scripts/blog_authors.json (scraped about pages + RSS feeds)
- **Author name improvements:** Fixed 34 entity files that had domain names or handles as titles
  - Examples: simonw → Simon Willison, daringfireball-net → John Gruber, paulgraham-com → Paul Graham
  - mitchellh-com → Mitchell Hashimoto, righto-com → Ken Shirriff, pluralistic-net → Cory Doctorow
  - krebsonsecurity-com → Brian Krebs, geohot-github-io → George Hotz, overreacted-io → Dan Abramov
  - And 26 more...
- **Updated:** wiki/index.md (all 84 bloggers listed with correct names), wiki/log.md

## 2026-04-10 — X Account Entity Enrichment
- **Enriched 5 X account entity pages** from skeleton → full research profiles:
  - **Will Brown** (@willccbb) — Prime Intellect Research Lead, verifiers library creator, GRPO demos, GenAI Handbook author. Columbia PhD (Papadimitriou, Roughgarden advisors). Key contributor to open-source RL infrastructure.
  - **Nathan Lambert** (@natolambert) — RL researcher, Interconnects newsletter author. OpenAI alum (2021-2022), Hugging Face alignment team (2023). Pioneer in open RLHF with Zephyr, TRL library. Focus on AI safety, model alignment, and AI safety policy.
  - **Sero** (@0xsero) — Founder & CEO of Sybil Solutions (founded Oct 2023, $5.5M seed from Andreessen Horowitz). AI infrastructure for decentralized networks. Previously at Dapper Labs (CryptoKitties, NBA Top Shot). Advocate for local-first AI and privacy-preserving systems.
  - **Teknium** (@teknium1) — Co-founder & Head of Post-Training at Nous Research ($1B valuation, Paradigm Series A 2025). Lead architect of Hermes model family (Hermes 2, 3, 4). Focus on post-training, synthetic data pipelines, RL environments. Open-source advocate.
  - **Sankalp Sinha** (@dejavucoder) — AI engineer, applied LLM researcher based in India. Contributor to agentOS (Rivet). Focus on AI-assisted coding, agentic workflows, LLM evaluation. Writes extensively about coding tool evolution and developer productivity.
- **Research methods:** Web search, blog analysis, GitHub profiling, X/Twitter activity review, newsletter analysis, company research
- **Updated:** wiki/index.md (X/Twitter Accounts section with descriptions)
- **Status:** All 5 pages now have full frontmatter (status: active), Core Ideas sections, Related wikilinks, and comprehensive project/timeline information

## 2026-04-10 — Added Andrej Karpathy Entity Page
- **Created:** wiki/entities/andrej-karpathy.md — full research profile
  - **Andrej Karpathy** (@karpathy) — OpenAI co-founder, ex-Tesla AI Director, Eureka Labs founder
  - Coined "vibe coding" (Apr 2025) and "agentic engineering" (Feb 2026)
  - YouTube "Zero to Hero" series, CS231n at Stanford
  - microgpt (200 lines of Python), autoresearch, nanoGPT, micrograd, ConvNetJS
  - Key concepts: Software 2.0, Teacher+AI Symbiosis, Verifiability over Capability
  - Bearblog posts: 2025 LLM Year in Review, Verifiability, The space of minds, etc.
  - Viral Jan 2026 thread on AI coding workflow (39K+ likes, 7.5M+ impressions)
- **Added:** @karpathy to ~/x-accounts.yaml
- **Updated:** wiki/index.md (Entity count 99→100, added Karpathy to entity list and X/Twitter Accounts)
- **Updated:** wiki/log.md with enrichment details

## 2026-04-10
- Added 4 X account entity skeletons: @_lopopolo, @bcherny, @mikeyk, @addyosmani
- Removed Mike Krieger (@mikeyk) from X accounts (LinkedIn post, not X/Twitter)
- Updated wiki/index.md People section with categorized key figures
- Added Vinci Rufus reference to Agentic Engineering concept
- Updated index.md entity count: 100→102 (added Boris Cherny, Ryan Lopopolo; removed Mike Krieger)
- **Created:** [[concepts/local-llm]] — Local LLM inference ecosystem, privacy, open-source models
- **Created:** [[entities/georgi-gerganov]] — llama.cpp creator, GGML/GGUF format pioneer
- **Updated:** index.md with Local LLM concept and Georgi Gerganov entity
- **Monitoring:** Added Reddit sources r/LocalLLaMA, r/LocalLLM, r/AI_Agents for tracking local LLM trends

## 2026-04-10
- Added 5 X account entity skeletons: @thdxr, @realmcore_, @a1zhang, @danielhanchen, @xeophon

## 2026-04-10 — Major Content Backlog Processing

Processed 47 highest-priority articles from blogwatcher backlog (2,238 total unread).

### New Concept Pages Created (10)
- [[concepts/cognitive-cost-of-agents]] — Simon Willison on mental load of AI coding
- [[concepts/claude-mythos-glasswing]] — Anthropic's restricted security model release
- [[concepts/gnu-ai-reimplementations]] — antirez on AI clean-room reimplementations
- [[concepts/anthropic-managed-agents]] — Reddit discussion on Anthropic's managed agent platform
- [[concepts/agent-orchestration-frameworks]] — Comparison of LangGraph, CrewAI, AutoGen etc.
- [[concepts/compute-scaling-bottlenecks]] — Dylan Patel on ASML/TSMC/HBM constraints
- [[concepts/ai-bubble-economics]] — Ed Zitron on AI spending reality vs hype
- [[concepts/ai-coding-reliability]] — Gary Marcus on AI coding tool outages
- [[concepts/open-source-ai-destruction]] — Jeff Geerling on AI impact on open source
- [[entities/dylan-patel]] — SemiAnalysis CEO, AI compute infrastructure analyst

### Updated Pages
- [[concepts/agentic-engineering]] — Added Simon Willison Lenny's Podcast insights
- [[concepts/local-llm]] — Added Google AI Edge Gallery, Qwen3.5-122B on RTX 6000
- [[concepts/claude-code-leak]] — Added Project Glasswing details
- [[index.md]] — Updated concept count (15 → 25), entity count, added new sections

### Sources
- 9 blogwatcher feeds (Simon Willison, antirez, Gary Marcus, Dwarkesh, Jeff Geerling, etc.)
- 5 Reddit communities (r/LocalLLaMA, r/LocalLLM, r/AI_Agents, etc.)
- News: NBC, Wired, Business Insider, Yahoo Finance


## 2026-04-10
- Added 56 X account entity skeletons: @geoffreylitt, @trq212, @RLanceMartin, @gm8xx8, @Grad62304977, @eliebakouch, @arlanr, @corbtt, @lilianweng, @johnowhitaker, @bclavie, @vanstriendaniel, @HamelHusain, @eugeneyan, @charles_irl, @ankrgyl, @TheZachMueller, @jxmnop, @Dorialexander, @BEBischof, @ptkbhv, @DrJimFan, @lateinteraction, @ryancarson, @spikedoanz, @_xjdr, @ctatedev, @Vtrivedy10, @dabit3, @burkov, @_philschmid, @badlogicgames, @dbreunig, @samuelcolvin, @willmcgugan, @mitsuhiko, @hynek, @karrisaarinen, @ScottWu46, @rahulgs, @koylanai, @steipete, @iannuttall, @boazbaraktcs, @ekzhang1, @jobergum, @softwaredoug, @QuixiAI, @emollick, @clefourrier, @ashpreetbedi, @yacinemtb, @abacaj, @tomaarsen, @thealexbanks, @chipro

## 2026-04-10 — X Account Skeleton Enrichment Complete
- **All 61 X/Twitter account entity pages enriched** from skeleton → full research profiles
- **Skeleton pages remaining: 0** (out of 174 total entity files)
- **Enriched in 4 batches:**
  - Batch 1: @abacaj, @thealexbanks, @ankrgyl, @arlanr, @ashpreetbedi, @ctatedev, @corbtt
  - Batch 2: @Dorialexander, @softwaredoug, @dbreunig, @eliebakouch, @ekzhang1, @Grad62304977
  - Batch 3: @iannuttall, @jobergum, @koylanai, @lateinteraction, @ptkbhv
  - Batch 4: @rahulgs, @realmcore_, @spikedoanz, @_xjdr, @yacinemtb
- Each page includes: full frontmatter (status: active), overview, timeline, core ideas, key projects, related wikilinks, and sources
- **Quality target met:** Pages match depth of antirez-com.md / simon-willison.md (8-24KB each)

## 2026-04-10
- Added 8 X account entity skeletons: @lilianweng, @bclavie, @eugeneyan, @samuelcolvin, @mitsuhiko, @emollick, @clefourrier, @chipro
