## [2026-05-03] Knowledge Shields — Systems Understanding Methodology from Entropic Thoughts

- **[[concepts/knowledge-shields]]** — Created concept page capturing Chris (Entropic Thoughts)'s unified methodology for understanding complex systems. Covers: the hypothesis-invalidation loop, mental model diagnosis through observation, self-verification skills (alternative approaches, feasibility checks, recursive verification), knowledge shields (strongly held wrong beliefs resist correction), productive vs. unproductive error classification, and motivation management. Includes connections to AI agent debugging, eval design, and prompt engineering. Sources: entropicthoughts.com/understanding-systems.
- **[[entities/entropicthoughts-com]]** — Added wikilink to knowledge-shields concept in Related section; added Understanding Systems to Timeline.
- Raw article already saved: raw/articles/entropicthoughts.com--understanding-systems--149e6399.md.
- Source: https://entropicthoughts.com/understanding-systems

## [2026-05-03] Raindrop — AI Agent Monitoring Platform

- **[[concepts/raindrop]]** — Created concept page for Raindrop, "Sentry for AI Agents" monitoring platform. Covers: Trajectories (agent-native trace viz), Signals (7 default + custom classifiers), Deep Search (natural language over traces), Experiments (A/B testing), Agent Self Diagnostics. Includes detailed comparison tables with Braintrust/LangSmith/Arize/Langfuse/Logfire and cross-category comparison with OpenAI Symphony (monitoring vs orchestration layers). Sources: raindrop.ai docs, blog posts (seed round, trajectories, agent self diagnostics), PRNewswire.
- **raw/articles/2026-05-03_raindrop-introduction.md** — Saved raw article with full detail.
- Source: https://www.raindrop.ai/docs/introduction

## [2026-05-03] ByteRover — Portable File-Based Memory Layer for Coding Agents

- **[[entities/byterover]]** — Created entity page for ByteRover (formerly Cipher). Portable, file-based memory layer for autonomous coding agents with market-best 92-96% retrieval accuracy on LoCoMo/LongMemEval. Built in TypeScript by campfirein (Vietnam). Architecture: replaces vector DBs with LLM-curated Hierarchical Context Tree of Markdown files with Adaptive Knowledge Lifecycle (AKL) and 5-tier progressive retrieval. Open source (Elastic 2.0), 4.2k+ GitHub stars. Native plugins for Hermes Agent, Claude Code, OpenClaw. arXiv:2604.01599.
- **[[entities/andy-nguyen]]** — Created entity page for Duy Anh "Andy" Nguyen (@kevinnguyendn), Founder & CEO of ByteRover. Based in Da Nang, Vietnam. Former ML Engineer at OpenLab JSC.
- **raw/articles/2026-05-03_ByteRover-overview.md** — Saved raw article from homepage + GitHub + arXiv paper.
- Source: https://www.byterover.dev/blog, https://github.com/campfirein/byterover-cli, https://arxiv.org/abs/2604.01599

## [2026-05-03] Minimal Coding Agent — Thorsten Ball's "Emperor Has No Clothes" Guide

- **[[concepts/minimal-coding-agent]]** — Created concept page for the minimal code-editing agent pattern: ~400 lines of Go, 3 tools (read_file/list_files/edit_file via string replacement), heartbeat loop. Thorsten Ball's thesis: the agent loop itself has no moat; differentiation comes from UI/UX, system prompts, error handling.
- **[[entities/thorsten-ball]]** — Created entity page for Thorsten Ball. Software engineer at Sourcegraph (Amp), author of Writing An Interpreter In Go / Writing A Compiler In Go, writes Register Spill newsletter.
- **[[concepts/agent-loop-orchestration]]** — Added [[concepts/minimal-coding-agent]] as a concrete Go implementation reference.
- **[[concepts/harness-engineering/system-architecture/building-effective-agents]]** — Added [[concepts/minimal-coding-agent]] as a concrete implementation of Anthropic's "simple composable patterns" principle.
- **raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md** — Saved raw article.
- Source: https://ampcode.com/notes/how-to-build-an-agent

## [2026-05-02] OpenRouter State of AI 2025 — 100T Token LLM Usage Study

- **[[concepts/openrouter-state-of-ai-2025]]** — Created concept page for the landmark study by OpenRouter & a16z analyzing 100 trillion tokens of real-world LLM usage. Covers: reasoning inflection point (Dec 5, 2024, o1 release), open vs closed source dynamics (30% OSS equilibrium, Chinese OSS rise), agentic inference shift (50%+ reasoning tokens, 4x prompt length explosion), category taxonomy (Programming 50%+ tokens, Roleplay 52% of OSS), provider specializations, economics (price inelasticity, Jevons Paradox, market archetypes), and geography (Asia 31%, doubled).
- **[[concepts/glass-slipper-effect]]** — Created concept page for the Cinderella Glass Slipper retention framework. Foundational cohorts (~40% retention at Month 5), Boomerang Effect, cognitive inertia, and workload-model fit thesis.
- **[[entities/openrouter]]** — Created entity page for OpenRouter, the unified API gateway for 300+ LLMs. Published the State of AI 2025 study with a16z.
- **[[entities/malika-aubakirova]]** — Created entity page for Malika Aubakirova, a16z infrastructure researcher and co-author of the State of AI 2025 study.
- **raw/articles/2025-12-01_openrouter-state-of-ai-2025.md** — Saved raw article.
- Source: https://openrouter.ai/state-of-ai

## [2026-05-02] Sparse Signal Loop — stochi's Experimental Validation of MGH

- **[[concepts/sparse-signal-loop]]** — Created concept page for Sparse Signal Loop experiment. Controlled 2×2 matrix test of feedback density (sparse vs dense), memory location (chat vs files), and procedure persistence (reinjection vs skill files) across LongBench-Pro and Mini SWE Agent Plus. Key findings: feedback sparsity is task-dependent, the "Judge Gap" (0.9667 Judge YES vs 0.5667 actual solve), constraint beats free-form memory.
- **[[entities/stochi]]** — Created entity page for stochi (stochi0). Independent AI researcher focused on post-training, agents, RL, model architectures. Previously shipped AI at QX Labs and Unsiloed AI (YC F25).
- **[[concepts/mismanaged-geniuses-hypothesis]]** — Added "Empirical Validation: Sparse Signal Loop" section with 3 key findings (supports, refines, warns). Added [[concepts/sparse-signal-loop]] to Related Concepts and cross-connections.
- **raw/articles/2026-05-02_sparse-signal-loop.md** — Saved raw article.
- Source: https://stochi0.vercel.app/writings/sparse-signal-loop

## [2026-05-02] Antoine Buteau — Automation Series (10 Parts) Full Ingestion

- **[[entities/antoine-buteau]]** — Created entity page for Antoine Buteau (Head of BizOps at Shakepay, previously Replit). Documented career timeline, Automation Series overview table, other series (Agency, Power, Technical Literacy, Live Player), key ideas (Three Kinds of Work, Automation Boundary, HITL as Design Pattern, Bounded Agents), and key quotes.
- **[[concepts/automation-series]]** — Created concept page for the 10-part Automation Series. Parts table covering all entries from "Automation Is Not One Thing" through "The Automation Architecture Worksheet." Key insights synthesized: Three Kinds of Work, Confidence-Driven Action, Bounded Agents, Staged Autonomy, and more.
- **raw/articles/2026-05-02_antoine-buteau_automation-series-1.md** through **automation-series-10.md** — Saved all 10 raw articles.
- Sources: https://www.antoinebuteau.com (full series via sitemap)

## [2026-05-02] PyTorch GPU Memory Profiling — Memory Measurement Without Execution (FakeTensorMode)

- **[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]** — Added Section 4: "モデルを実行せずにメモリ使用量を測定する — FakeTensorMode + MemoryTrackingMode". Covers Alban Desmaison's ~30-line MemoryTrackingMode implementation, simultaneous use with FakeTensorMode for CUDA-on-CPU memory estimation, Module-wise tracking (PR #124688), allocated vs reserved memory distinction with fragmentation, NCCL buffer blind spot, and PyTorch caching allocator refactoring roadmap.
- Source: https://dev-discuss.pytorch.org/t/how-to-measure-memory-usage-from-your-model-without-running-it/

## [2026-05-02] PyTorch GPU Memory Profiling — Memory Snapshot & Profiler Tools Ingestion

- **[[concepts/ai-infrastructure-engineering/pytorch-gpu-memory-profiling]]** — Created concept page for PyTorch v2.1+ GPU memory debugging tools. Covers Memory Snapshot (allocation trace visualization with stack traces), Memory Profiler (categorized usage: gradients/optimizer/activations), OOM staircase pattern fix (`optimizer.zero_grad(set_to_none=True)`), `record_function` labeling, and tool comparison table.
- **[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]** — Added `pytorch-gpu-memory-profiling` to `related` and `Related Pages` sections.
- **[[concepts/ai-infrastructure-engineering/_index]]** — Added "Memory Debugging" row to scope table with link to new page.
- Source: https://pytorch.org/blog/understanding-gpu-memory-1/

## [2026-05-02] Braintrust Evals 101 Course — Practical Eval Methodology Ingestion

- **[[concepts/ai-evals]]** — Added "Braintrust Evals 101: Practical Eval Methodology" section covering: non-determinism as core thesis, 3-component eval model (dataset/task/scorer), LLM-as-Judge with choice scores, trial counts for variance reduction, multi-level trace scoring (per-turn vs per-trace), online scoring, the Improvement Loop with temperature=0/max_concurrency=1 settings, and the GPT-4o sycophancy rollback case study.
- **[[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]]** — Enriched with Braintrust eval features, Evals 101 course module table, and comparison matrix with LangSmith/Arize Phoenix/Inspect AI.
- **raw/articles/2026-05-02_braintrust-evals-101-why-are-evals-important.md** — Saved raw article with full module-by-module breakdown (14 modules across Learn/Build/Refine sections).
- Source: https://www.braintrust.dev/foundations/why-are-evals-important | GitHub: braintrustdata/eval-101-course

## [2026-05-02] lambda-RLM (Typed Recursive Reasoning) — Huawei Paper Ingestion

- **[[concepts/typed-rlm]]** — Created concept page for lambda-RLM (typed functional runtime, Huawei Noah's Ark Lab). Formal guarantees (termination, cost bounds, optimal partition k*=2), Y-combinator fixed-point over SPLIT/MAP/REDUCE combinators. 29/36 wins, +21.9pp accuracy, 4.1x faster. arXiv:2603.20105 (arXiv-only, ingested per user request).
- **[[concepts/lambda-rlm]]** — Updated with disambiguation warning distinguishing from Huawei's lambda-RLM. Added [[concepts/typed-rlm]] to related.
- **[[concepts/rlm-recursive-language-models]]** — Added lambda-RLM variant section with comparison table. Updated Related Concepts.
- **raw/papers/2026-03-20_2603.20105_y-combinator-for-llms.md** — Saved raw paper summary with blocked reason: no_peer_review.
- Source: `raw/papers/2026-03-20_2603.20105_y-combinator-for-llms.md` | https://arxiv.org/abs/2603.20105

## [2026-05-02] Recursive by Design — Lambda-RLM, Theodoros Galanos & The Harness Blog Ingestion

- **[[concepts/lambda-rlm]]** — Created concept page for Lambda-RLM, a deterministic pipeline variant of RLM for the AEC domain. Plan (0 LLM calls) → Extract+Review → Generate. 14x token reduction, +8.4% quality improvement over open REPL.
- **[[entities/theodoros-galanos]]** — Created entity page for Theodoros Galanos, AI researcher and harness engineering practitioner. Chief Science Officer at infrared.city. Creator of Lambda-RLM and AEC-Bench.
- **[[entities/the-harness-blog]]** — Created entity page for The Harness blog (theharness.blog). 25 posts across 6 topics on harness engineering, agent evaluation, and AI in AEC.
- **[[concepts/rlm-recursive-language-models]]** — Updated with Lambda-RLM production case study section and benchmark metrics.
- **[[concepts/recursive-language-models]]** — Updated with Lambda-RLM variant reference.
- Source: `raw/articles/2026-05-02_the-harness-blog_recursive-by-design.md` | https://theharness.blog/blog/recursive-by-design/

## [2026-05-02] Paul Hoekstra — Agentic Engineering 4-Layer Framework (Full Series Ingestion)

- **[[entities/paul-hoekstra]]** — Created entity page for data engineer and Paul's Pipeline author. Documented 4-layer Agentic Engineering framework, key articles, and contributions.
- **[[concepts/harness-engineering/agentic-engineering-configuration-layer]]** — Created concept page for Layer 1. CLAUDE.md, Skills system, `<HARD-GATE>` enforcement, SkillsBench findings, anti-rationalization tables, division of labor strategy.
- **[[concepts/harness-engineering/agentic-engineering-capability-layer]]** — Created concept page for Layer 2. MCP with deferred loading, live docs (Context7, DeepWiki, Exa), visual output tools (Figma, frontend-slides, Remotion, draw.io), 3-layer memory strategy (MEMORY.md, episodic-memory, QMD).
- **[[concepts/harness-engineering/agentic-engineering-orchestration-layer]]** — Created concept page for Layer 3. Subagents vs Agent Teams, Ralph Loop, Git worktrees, context compression, "context over roles" design principle.
- **[[concepts/harness-engineering/agentic-engineering-guardrails-layer]]** — Created concept page for Layer 4. Poisoned instructions, homoglyph attacks, sandboxing (bubblewrap/Apple), permissions system, AST-grep, pre-commit/CI gates.
- **[[concepts/harness-engineering/agentic-engineering]]** — Updated: Added "Paul Hoekstra's 4-Layer Framework" section with integration notes vs Willison's framing. Updated sources and further reading.
- Source raw articles: 6 articles saved (4 series parts + statusline article + visual output article)

## [2026-05-02] Pi Podcast (Syntax #976) — Entity Enrichment & Concept Update

- **[[entities/pi-coding-agent]]** — Enriched with podcast insights: Pi's core definition ("a while loop with 4 tools"), "Bash is all you need" philosophy, steering queue, self-modifying skills with hot reloading, MCP critique vs Pi approach, prompt injection concerns, "Code is truth" memory philosophy, MAM (Master of Mischief) Slack bot.
- **[[entities/mario-zechner]]** — Enriched: Syntax.fm podcast appearance added to Recent Posts, Pi podcast revelations added to pi section (OpenClaw connection, steering queue, self-modifying skills).
- **[[entities/armin-ronacher]]** — Enriched: Syntax.fm #976 appearance added to timeline (Feb 4, 2026).
- **[[concepts/agentic-security]]** — Updated: Added "Camel Paper" section documenting the two-LLM approach to prompt injection defense and its practical limitations, with quote from the Pi podcast.
- Source: `raw/articles/2026-02-04_pi-syntax-fm-podcast.md` | https://syntax.fm/show/976/pi-the-ai-harness-that-powers-openclaw-w-armin-ronacher-and-mario-zechner/transcript

## [2026-05-02] Simulacrum of Knowledge Work — Concept & Entity Ingestion

- **[[concepts/simulacrum-of-knowledge-work]]** — Created concept page. Critical analysis by @onehappyfellow of how LLMs broke the proxy measures that knowledge work relies on for quality assessment. Covers proxy measures, incentive alignment crisis, Goodhart's Law recursive problem, and the "tokens-spent leaderboard" meta-commentary.
- **[[entities/onehappyfellow]]** — Created entity page for the author of "Simulacrum of Knowledge Work." Head of The Institute for Type Safe Memetic Research. OCaml programmer, technology writer, and rapper.
- Source: `raw/articles/2026-04-25_onehappyfellow-simulacrum-of-knowledge-work.md` | https://blog.happyfellow.dev/simulacrum-of-knowledge-work/

## [2026-05-02] Fireworks AI Podcast (SE Daily Episode 1919) — Entity & Concept Ingestion

- **[[entities/fireworks-ai]]** — Created entity page for Fireworks AI. AI inference and model customization platform for open-weight models. 13T+ tokens/day. Multi-hardware (NVIDIA + AMD), FireAttention kernels, custom speculator training, RFT capabilities.
- **[[entities/benny-chen]]** — Created entity page for Benny Chen, Co-Founder of Fireworks AI. Former Meta ML infrastructure. Key theses: RFT, "Traces Are All You Need," Eval Protocol, multi-hardware supply chain strategy.
- **[[concepts/reinforcement-fine-tuning]]** — Created concept page for RFT. Pragmatic RL fine-tuning using production traces + LLM-as-Judge. RFT vs SFT comparison table, Vercel case study (40x faster code fixing).
- **[[concepts/fine-tuning]]** — Updated: Added RFT as a method in Key Ideas + Terminology. Added related wikilinks to RFT page and Fireworks AI.
- **[[concepts/speculative-decoding]]** — Updated: Added "Custom Speculator Training (Fireworks AI Approach)" section. Documented distribution-matched speculators achieving 90%+ acceptance rates.
- Source: `raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md` (SED transcript)

## [2026-05-02] Skeleton Enrichment — Foundation Capital Portfolio Companies (4 entities enriched)

- **[[entities/maximor]]** — Enriched from skeleton to L3 page. Added funding ($9M seed, Foundation Capital), founder bios (Ramnandan Krishnamurthy & Ajay Amudan, ex-Microsoft), Audit-Ready Agent architecture, product table, ERP-agnostic design principles. Sources: Blog, SaaSNews, TechCrunch, Axios.
- **[[entities/regie-ai]]** — Enriched from skeleton to L3 page. Added funding history ($50M total, $30M Series B Feb 2025), founder bios (Srinath Sridhar, Matt Millen), RegieOne platform features, investor list (Khosla Ventures, Scale Venture Partners, Foundation Capital). Sources: Crunchbase, PRNewswire, Regie blog.
- **[[entities/arize]]** — Enriched from skeleton to L3 page. Added funding ($131M total, $70M Series C), founder bios (Jason Lopatecki, Aparna Dhinakaran), Phoenix OSS details (2M+ monthly downloads, 9.5K GitHub stars, OpenTelemetry-based), AI Copilot, enterprise customers (Uber, Chime, eBay, Spotify, US Air Force). Sources: Arize blog, PRNewswire, GitHub, Crunchbase.
- **[[entities/playerzero]]** — Enriched from skeleton to L3 page. Added funding ($20M total, $15M Series A led by Foundation Capital), founder bio (Animesh Koratana, Stanford DAWN lab), context graph technology deep-dive (two clocks problem, engineering world models, code simulation), competitive positioning vs Cursor/Datadog/APM, customer Zuora, investor list (Matei Zaharia, Drew Houston, Dylan Field, Guillermo Rauch). Sources: TechCrunch, PlayerZero resources, AInvest.
- **[[entities/larsen-cundric]]** — Cleaned up stale `**Status:** skeleton` body text (frontmatter already showed `status: active`).

## [2026-05-02] Wiki Health Lint — Daily Automated Check

- **Critical Issues Found:**
  - 110 broken wikilinks to non-existent concept/entity pages
  - 331 unknown tags (tag sprawl — not in SCHEMA.md taxonomy)
  - 27 orphan entity pages, 172 orphan concept pages
  - 43 pages with incomplete frontmatter
  - Index count mismatch: header says 760 total but 1498 actual pages exist

- **Warnings:**
  - 91 oversized pages (>200 lines), including index.md at 1521 lines
  - 638 stub pages containing TODO markers
  - 7 entities split across 4-6 sub-pages each (claude-code, clefourrier, etc.)
  - 1 corrupted raw article with HTML parsing artifacts

- **Minor:**
  - 4 pages missing from index.md
  - 2 subdirectories missing _index.md
  - 1 page without frontmatter (log-2026.md)

## [2026-05-02] Active Crawl — xAI Grok 4.3, Microsoft Copilot Wave 3, MIT FTTE, SpaceX-xAI Merger

- **Researched 5 trending AI/ML topics** not yet covered in wiki:
  1. **xAI Grok 4.3** — Always-on reasoning, 1M context, aggressive pricing, Custom Voices
  2. **Microsoft Copilot Wave 3** — Copilot Cowork with Anthropic Claude, Agent 365, E7 Frontier Suite
  3. **MIT FTTE** — Federated Tiny Training Engine, 81% faster FL on edge devices
  4. **SpaceX acquires xAI** — $1.25T combined valuation
  5. **Grok Computer** — xAI's autonomous desktop agent

- **Saved 4 raw articles:**
  - `raw/articles/2026-05-01_xai-grok-4-3-launch.md`
  - `raw/articles/2026-03-09_microsoft-copilot-wave-3-frontier-transformation.md`
  - `raw/articles/2026-04-29_mit-ftte-federated-learning-edge-devices.md`
  - `raw/articles/2026-02-02_spacex-acquires-xai-merger.md`

- **Created 5 wiki pages:**
  - [[entities/xai]] — Company entity covering Grok ecosystem, SpaceX acquisition, pricing strategy
  - [[entities/grok-4-3]] — Latest model: always-on reasoning, 1M context, benchmarks, Custom Voices
  - [[concepts/grok-computer]] — Desktop agent: pixel-reading, universal app control, Grok 4.3 integration
  - [[concepts/microsoft-copilot-wave-3]] — Wave 3 transformation: Copilot Cowork, Agent 365, E7 suite
  - [[concepts/federated-tiny-training-engine]] — MIT FTTE: semi-async FL with 81% speedup on edge devices

- **Updated [[index]]** — Added 2 entities + 3 concepts. Total: 755→760. Entities: 365→367. Concepts: 402→405.

## [2026-05-02] Shopify — "The Most Future-Proof Job: Entrepreneurship" Data Analysis

- Saved raw article: `raw/articles/2026-04-15_shopify-future-proof-job-entrepreneurship.md` — Shopifyデータサイエンスチームによる起業家精神の分析。AIによる雇用減少（2026年3月の解雇の25%）と起業家増加（Shopify初回販売が2018年比7倍）の「Risk Flip」を示すデータ。リピート創業者の2倍以上の売上、eコマースの市場拡大（14%→20%+）、AI「Exoskeletons」の役割。
- Updated [[entities/shopify]] — 「Entrepreneurship & Ecommerce Trends」セクションを追加。「Risk Flip」テーゼ、リピート創業者 compounding、AI Exoskeletonsのデータを収録。
- Updated [[solo-founder-stack]] — 「Empirical Support: Shopify Data」セクションを追加。Shopifyの実証データで solo founder テーゼを補強（Risk Flip、Compounding Entrepreneur、AI Accelerator）。

## [2026-05-02] Every Guide — Agent-native Product Management + Compound Engineering

- Saved raw article: `raw/articles/2026-05-02_guide-to-agent-native-product-management.md` — Every社のガイド。Marcus Moretti（Spiral GM）が提唱するエージェントネイティブPM。ce:strategy（戦略策定）とce:product-pulse（自動ヘルスレポート）の2スキルを中核に、MCP経由でPostHog/Stripe/Datadogを統合。80/20計画重視シフト。

- Created [[entities/every-inc]] — AI-native media & software company (CEO Dan Shipper). 5 products with single-person teams. Compound Engineering plugin (7K+ stars).

- Created [[entities/marcus-moretti]] — GM of Spiral, author of Agent-native PM guide.

- Created [[entities/kieran-klaassen]] — GM of Cora, author of Compound Engineering: The Definitive Guide.

- Created [[concepts/agent-native-product-management]] — PMフレームワーク: 会話が仕事、80/20計画シフト、ce:strategy/ce:product-pulseスキル、エージェント管理バックログ。

- Created [[concepts/compound-engineering-every]] — Every社版Compound Engineering（各作業が将来を容易化）。Simon Willison版（コードレベルの反復改善ループ）とは異なる。

- Updated [[concepts/compound-engineering-loop]] — Stub→redirect（compound-engineering-every および Simon Willison版への誘導ページに変更）。

- Updated [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Simon Willison版にEvery社版への相互参照を追加。

- Updated [[index]] — Added 3 entities + 2 concepts. Total: 750→755. Reclassified 1 stub.

## [2026-05-02] YouTube Video — "Why 2026 is The Year of Agentic Search" (Doug Turnbull & Jo Kristian Bergum)

- Saved raw article: `raw/articles/2026-05-01_doug-turnbull-2026-is-the-year-of-agentic-search.md` — 65-min fireside chat covering four pillars: LLM Query Understanding at scale, Autoresearch (agents writing ranking code), Agentic Search Harnesses (feedback loops for dumb retrievers), and LLM-as-a-Judge for principled search evaluation.
- Updated [[entities/doug-turnbull-speaking]] — Added talk to conference talks list (removed duplicate Berlin Buzzwords entry).
- Updated [[concepts/agentic-search]] — Added source with summary of four pillars.

## [2026-05-01] X Bookmarks Ingest — OpenAI WebSockets, LangChain Harness Engineering, Meta Autodata

- Saved raw articles:
  - `raw/articles/2026-04-22_openai-websockets-agentic-workflows.md` — OpenAI's transition to WebSocket transport for the Responses API, achieving ~40% faster agentic cycle latency (up to 1,000+ TPS). Techniques: `previous_response_id`, incremental safety processing, token caching.
  - `raw/articles/2026-02-17_langchain-improving-deep-agents-harness-engineering.md` — Vivek Trivedy (LangChain) case study: +13.7pts on Terminal Bench 2.0 from harness-only changes (Build-Verify Loop, Context Engineering, Loop Detection, Reasoning Sandwich).
  - `raw/articles/2026-04-08_langchain-better-harness-hill-climbing-evals.md` — Vivek Trivedy follow-up: evals as training data for autonomous harness hill-climbing with holdout sets.
  - `raw/articles/2026-04-30_meta-autodata-agentic-data-scientist.md` — Meta AI's Autodata: agentic data scientists using Weak-vs-Strong solver paradigm. 34% discrimination gap vs 1.9% baseline. Meta-optimization: 12.8%→42.4% pass rate.

- Updated [[concepts/harness-engineering]] — Added "LangChain Harness Engineering Case Studies" section with two sub-sections: Improving Deep Agents (+13.7pts, 4 techniques) and Better Harness (eval-driven hill-climbing recipe). Updated sources, tags, aliases, and related links.

- Created [[concepts/autodata-agentic-data-creation]] — New concept page for Meta AI's Autodata framework. Covers the 4-subagent Weak-vs-Strong paradigm, experimental results (34% gap), meta-optimization, and significance for inference-time compute scaling.

- Updated [[index]] — Added autodata-agentic-data-creation entry. Updated harness-engineering description to reference LangChain case studies and Vivek Trivedy. Total pages: 749→750.

- 5 X Articles behind auth wall (no external mirrors found): "How to Beat GRPO Without Touching Model Weights", "On SFT, RL, and on-policy distillation", "大语言模型训练与服务背后的数学原理", "If AI is so great, why isn't it working?", "The 5 principles for AI that ships to production". Saved as metadata-only in bookmark records.

## [2026-05-01] GLiClass | New concept page (encoder-only zero-shot classification)

- Created [[concepts/gliclass]] — Comprehensive concept page for Knowledgator's GLiClass model family. Covers:
  - **Architecture**: single-forward-pass classification, GLiNER-inspired design, 3 architecture types (uni/bi/bi-fused/encoder-decoder)
  - **Three sub-families**: GLiClass-V3 (general, 6 variants, DeBERTa/ModernBERT/Ettin backbones), GLiClass-Instruct (instruction-following, 3 variants), GLiClass-Multilang (20 languages, 3 variants, CrossAttn Scorer)
  - **V3 features**: hierarchical labels, few-shot, label descriptions, task prompts, long document chunking
  - **Training**: LoRA fine-tuning, multi-label PPO, logic-focused datasets
  - **RAC** (Retrieval-Augmented Classification): inference-time example retrieval, up to +141% F1 boost
  - **Benchmarks**: V3 large-v3.0 avg F1 0.7001, Instruct large-v1.0 avg F1 0.7199, Multilang Ultra avg F1 0.7212 (EN)
  - **Use cases**: RAG reranking, sentiment/topic, intent, NLI, hallucination detection, LLM safety
- Created [[entities/knowledgator]] — Organization entity page. Lists GLiNER/GLiClass/GLiREL product family, HF collections.
- Sources: arXiv:2508.07662, HuggingFace collections (3), GitHub repo, Medium blog, 3 X posts by @gm8xx8
- Updated: index.md, log.md

## [2026-05-01] AI Infrastructure Engineering — 親ページとスケルトン群の作成

- Created [[concepts/ai-infrastructure-engineering/_index]] — 親ページ。GPU/VRAM基礎、分散学習、モデルサーブ、オブザーバビリティ、コスト最適化の統合マップ。学習ロードマップ、既存ページ一覧表、Key Entitiesを含む。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUメモリ階層（HBM→SRAM）、VRAM計算式、Roofline Model、バッチング経済学、量子化効果、GPU選定ガイド、マルチGPUトポロジ。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/distributed-training]] — DDP→FSDP→DeepSpeed ZeRO(1/2/3)、3D並列化（TP/PP/EP/Expert Parallel）、戦略選択ガイド（モデルサイズ×GPU数）、CPUオフロード比較。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — デプロイ構成、スケーリングシグナル（queue/GPU/KV cache）、4つのスケーリングパターン、ロードバランシング戦略（Round Robin→LRU→Semantic）、コスト最適化パターン。⬜ L1
- Created [[concepts/ai-infrastructure-engineering/llm-observability]] — 推論メトリクス（TTFT/TPOT/ITL）、GPUリソース指標、品質シグナル、Observability Stack（Prometheus/OTel/Arize）、コスト帰属、劣化検知パターン、vLLM OTel統合。⬜ L1
- Created [[concepts/tensorrt-llm]] — NVIDIA推論最適化エンジン。FP8/FP4 Transformer Engine、vLLMとの比較表、ベンチマーク概算値、導入判断基準、Triton統合パターン。⬜ L1
- Enriched [[concepts/model-quantization]] — stub→L1。精密形式一覧（FP32→BitNet）、GPTQ/AWQ/GGUF/SmoothQuant/FP8比較、ハードウェアサポート表、トレードオフ実測値、KV Cache量子化。
- Enriched [[concepts/pytorch-fsdp-distributed-training]] — stub→L1。Sharding戦略詳細（NO_SHARD/SHARD_GRAD_OP/FULL_SHARD）、メモリ節約計算例、CPU Offload、DeepSpeed比較表、設定パラメータサンプルコード。
- Updated [[concepts/inference/_index]] — TensorRT-LLMをエンジン比較表に追加
- Updated [[index]] — Concepts 393→399, added 7 new entries + updated 2 TODO entries
- Sources: (new pages are skeleton/L1, will need article ingestion for enrichment)
