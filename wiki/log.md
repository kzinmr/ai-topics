## [2026-04-30] Agent Sandbox Architecture — Browser Use production patterns

- Created [[concepts/agent-sandboxing-patterns]]: Browser Use's production agent sandboxing architecture (millions of concurrent web agents). Two patterns: isolate the tool vs. isolate the agent with control plane architecture and zero-secret sandboxes using Unikraft micro-VMs.
- Created [[entities/larsen-cundric]]: Browser Use's Founding Engineer, sole infrastructure engineer, authored the sandbox architecture article. Key achievement: migrated to AWS-native infra with 80% cost reduction and 3× latency improvement.
- Raw article: raw/articles/two-ways-to-sandbox-agents-2026-02-25.md

## [2026-04-29] Skeleton enrichment cycle — enriched 12 concept pages from skeleton/placeholder status to complete with research content and cross-links
|- Enriched [[concepts/agent-loop-orchestration]]: Added detailed content on reasoning-action loops, ReAct/plan-execute patterns, observability, and framework implementations
|- Enriched [[concepts/agent-orchestration-frameworks]]: Added comprehensive comparison of LangChain, AutoGen, CrewAI, Semantic Kernel, and Google ADK
|- Enriched [[concepts/ai-image-generation]]: Added evolution from GANs/VAEs to diffusion models (Stable Diffusion, DALL-E, Midjourney, Flux)
|- Enriched [[concepts/claude-code-best-practices]]: Added Anthropic's official best practices and community-accumulated patterns
|- Enriched [[concepts/claude-opus-4-7]]: Added model specs, benchmarks, architecture details, and context window information
|- Enriched [[concepts/local-llm/inference-hardware]]: Added consumer GPU guide with VRAM requirements and throughput comparisons
|- Enriched [[concepts/local-llm/ollama]]: Added full feature documentation, API reference, model management, and Ollama Python/Eino integration
|- Enriched [[concepts/monty-sandbox]]: Added Pydantic's Python sandbox by Samuel Colvin, code execution security model
|- Enriched [[concepts/nano-banana-2]]: Added Google's ultra-efficient image model (2B params), architecture and performance
|- Enriched [[concepts/openclaw-ecosystem]]: Added OpenClaw's open-source agent framework with ClawDBot and MoltBot
|- Enriched [[concepts/reverse-engineering]]: Added definition, tools (Ghidra, IDA Pro, Binary Ninja), and AI-RE convergence
|- Enriched [[concepts/memory-systems-bitter-lesson]]: New page on Rich Sutton's Bitter Lesson applied to agent memory systems
|- Updated index.md: +12 full entries, -4 stub entries (total: 671 pages, 642 full, 619 stubs)
|- Updated skeleton header count: 640 → 636

## [2026-04-29] dreaming | Consolidation cycle — updated gpjt.md with Part 32l IFT results and Landscape Hypothesis, added project-prometheus to index
- Updated [[entities/gpjt]]: Added Part 32l Instruction Fine-Tuning results, GPT-5.4 judge transition, and Landscape Hypothesis
- Added [[entities/project-prometheus]] to index.md (page created by Daily Active Knowledge Crawl but not yet indexed)
- Themes below threshold skipped (gumloop 0.48, ai-coding-best-practices 0.46, google-photo-scanning 0.42, bezos-project-prometheus 0.40)

### Created
- [[entities/alex-volkov]]: AI Evangelist at Weights & Biases, ThursdAI host
- [[entities/gergely-orosz]]: The Pragmatic Engineer newsletter author, Big Tech insights

### Updated
- [[entities/gpjt]]: Added Part 32l IFT results, GPT-5.4 judge transition, and Landscape Hypothesis (from dreaming cycle 2026-04-29T18:17)
- [[concepts/chatgpt-images-2.0]]: Updated with reasoning-before-generation feature
- [[concepts/google-photo-scanning-ai]]: Verified existing coverage of Personal Intelligence update
- [[entities/google-tpu]]: Already has TPU 8t/8i deep dive coverage
- [[concepts/tokenmaxxing]]: Cross-referenced with AINews Tasteful Tokenmaxxing coverage

### Articles Processed
- 17 newsletter articles collected (2026-04-22 to 2026-04-29)
- 2 new entity pages created
- 4 existing pages verified/updated

# Change Log

## [2026-04-30] X bookmarks ingest | Batch from 2026-04-28/29

### New Entity Pages Created:
- **entities/palantir.md** — AI-powered decision infrastructure. Palantir Ontology as enterprise agent workflow framework.
- **entities/mistral-ai.md** — French AI company. Workflows (enterprise orchestration) and Voxtral TTS releases.
- **entities/talkie.md** — Open-weight 13B historical LLM trained exclusively on pre-1930 data.
- **entities/david-duvenaud.md** — AI researcher, co-announced Talkie with Alec Radford and @status_effects.
- **entities/periodic-ai.md** — AI research company with physical lab for RL scaling (1T+ parameters).
- **entities/mimo.md** — Xiaomi's open-source LLM. MiMo-V2.5-Pro: 1.02T MoE (42B active), 1M context.
- **entities/supermemory.md** — Company building SMFS, agent-optimized filesystem replacing RAG pipelines.

### New Concept Pages Created:
- **concepts/smfs.md** — Supermemory Filesystem: mountable FS for AI agents, replaces UNIX ops with agent-aware alternatives.
- **concepts/mesa-filesystem.md** — Enterprise AI agent filesystem for artifacts beyond chat history.

### Pages Updated:
- **entities/hermes-agent.md** — Added "15 Features Deep Dive" section from viral X article (2791 bookmarks, 350K impressions)
- **entities/nvidia.md** — Updated Nemotron 3 Nano Omni details (30B params, 256K context, multimodal)
- **concepts/harness-engineering.md** — Added iii platform "The Harness Is the Backend" thesis (Worker/Trigger/Function primitives)

### Raw Articles Saved:
- 14 files in wiki/raw/articles/ (4 X-native articles + 7 tweet metadata + 3 external articles)

### Index Updated:
- Total pages: 671 → 678 (+7 new)
- Full entries: 642 → 649


> Chronological record of wiki changes, updates, and additions.
> See [[log-2026]] for entries before the rotation.

## [2026-04-29] blog-triage ingest | Batch from 20260427T081429Z checkpoint

- **Source:** [The Signal: OpenAI Is Cooking, The Anthropic Sweep, and SpaceX Courts Cursor](https://open.substack.com/pub/thesignal/p/openai-is-cooking-the-anthropic-sweep) — Updated [[openai-workspace-agents]] (GPT-5.5/Codex unification, World ID integration), updated [[openai]] entity (World ID, Codex merge)
- **Source:** [Xe Iaso: I don't know if I like working at higher levels of abstraction](https://xeiaso.net/blog/2026/ai-abstraction/) — Already covered in [[cognitive-debt]] (enriched with Xe Iaso source)
- **Source:** [Xe Iaso: Vibe Coding Trip Report](https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/) — Already covered in [[vibe-coding]]
- **Source:** [timsh.org: Switching to Claude Code + VSCode inside Docker](https://timsh.org/claude-inside-docker/) — Created [[ai-coding-workflows]] (Docker dev container patterns, security, credential management, Claude Code vs Cursor cost comparison)
- **Source:** [Simon Willison: Romain Huet quote](https://simonwillison.net/2026/Apr/25/romain-huet/) — Updated [[openai]] entity
- **Source:** [timsh.org: Why you should self-host your vibecoded app](https://timsh.org/why-you-should-self-host/) — Already covered in [[vibe-coding]]
- **Index:** Updated total pages (658 → 659)

## [2026-04-29] Symphony blog article ingestion

- **Source:** [OpenAI Engineering Blog: Open-Source Codex Orchestration — Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/)
- **Updated:** concepts/openai-symphony.md (added 500% PR increase data, Codex App Server mode, economic shift analysis, lessons learned, updated status/frontmatter)
- **Saved:** wiki/raw/articles/openai-codex-orchestration-symphony.md (structured raw article)
- **Index:** Updated concepts/openai-symphony entry with Linear control plane and 500% PR increase summary
- **Created skill:** openai-blog-article-ingestion (standardized workflow for OpenAI blog ingestion)

## [2026-04-28] skeleton enrichment | 21 concept pages: skeleton→full (L3)
- **Batch:** Enriched 21 concept pages with substantive content via web research
- **Fixed broken frontmatter:** fine-tuning, multimodal, openclaw, sandbox, speech
- **Enriched 17-line skeletons:** mlx, langgraph, rags, cursor-ide, context-management, defense-in-depth, durable-execution, human-in-the-loop, self-learning-agents, tool-orchestration, dual-process-theory, clinical-ai, cloud-data-warehouses, data-engineering
- **Consolidated:** agent-memory.md → [[ai-agent-memory]] (redirect). Created comprehensive ai-agent-memory.md with two-camps framework
- **Sources:** Apple MLX docs, LangChain docs, Cursor docs, Anthropic engineering blog, Temporal docs, Kahneman dual process, FDA AI medical devices, Snowflake/BigQuery docs, Letta/Anthropic memory docs
- **Index:** Updated counts (stubs: 644→623, full entries: 604→625)

## [2026-04-28] blog-triage recovery | Batch from 2026-04-28_07-34-28 checkpoint

Previous triage agent had JSON parse error — recovered and processed directly.

**Take decisions:**
- Updated: concepts/harness-engineering/agentic-workflows/red-green-tdd.md (Martin Alderson's agentic TDD re-evaluation)
- Updated: concepts/cognitive-debt.md (Xe Iaso's AI abstraction cost essay — full enrichment)
- Created: concepts/agentic-sysadmin.md (Claude Code as sysadmin assistant pattern)
- Updated: concepts/agent-sandboxing.md (Docker isolation pattern from timsh.org)
- Updated: concepts/agentic-security.md (Nesbitt.io package security for AI agents)
- Updated: index.md (+1 new page entry, updated 3 existing entries)

**Reference decisions:**
- blog-34 (Telegram scam investigation) — interesting security methodology, skip
- blog-39 (Xe vibe coding sponsor panel) — already captured in vibe-coding.md
- blog-44 (Xe Claude Code April Fools) — already captured in xeiaso-net.md
- Various personal posts, non-AI tech content — skipped

**Skip decisions:**
- Joan Westenberg essays (general tech commentary, no specific AI relevance)
- Hugo Tunius privacy posts (pre-2026, historical only)
- Filfre.net gaming history (off-topic)
- John D. Cook math posts (peripheral AI interest only)
- Paul Graham essay archive dumps (already ingested via other means)
- Rakhim.exotext.com general software essays (no direct AI agent relevance)
- Miguel Grinberg SQLAlchemy series (off-topic)
- Giles Thomas LLM from scratch (interesting but peripheral)

- Sources: timsh.org (Docker isolation), martinalderson.com (agentic TDD, sysadmin pattern), xeiaso.net (abstraction costs), nesbitt.io (package security)

## [2026-04-28] newsletter ingest | Batch 2026-04-27/28

- Updated: concepts/gpt-5.5.md (agentic patterns: "I trust you" prompt, zero follow-up runs, Codex personality issues)
- Created: concepts/physical-ai.md (Physical AI vs Screen AI thesis, Applied Intuition platform, onboard vs offboard)
- Updated: entities/anthropic.md (Claude Design tool review, iteration speed vs Figma, GPT-Image-2 + Codex threat)
- Updated: entities/google.md (TPU v8 "Ironwood" chip independence, 8i vs 8t split, edge inference strategy)
- Updated: concepts/openai-symphony.md (OSS pipeline: Issue → Agent → PR → Human Review)
- Updated: concepts/agent-team-swarm.md (Sakana Conductor 7B, Kimi K2.6 300 parallel agents, 5-level autonomy model, orchestration patterns, agent economics)
- Created: concepts/agent-economics.md (1000x token multiplier, cost structure by autonomy level, value drivers)
- Updated: index.md (+2 new pages, counts updated)
- Sources: "How I AI" newsletter (GPT 5.5, Claude Design), AINews (ImageGen/AGI), Applied Intuition (Physical AI), Google (AI chip independence)

## [2026-04-28] Active Crawl [prerequisites + laterals] | context-engineering → kv-cache / harness-engineering → process-supervision / sandbox → capability-based-security

**Scope:** Daily active knowledge crawl based on hot-topics.yaml. Selected topics with last_crawled ≥ 3 days: context-engineering (prerequisites), harness-engineering (prerequisites), sandbox (laterals).

### Created: concepts/kv-cache.md
- **Parent topic:** context-engineering (prerequisites policy)
- **What:** KV Cache is the foundational optimization technique in transformer inference that stores intermediate attention computations, avoiding redundant recomputation. Understanding KV cache mechanics — size scaling (batch × layers × heads × d_k × sequence_length × precision), memory bandwidth bottleneck, and cache-aware scheduling — is a prerequisite for context engineering, prompt caching, and inference optimization.
- **Sources:** Sebastian Raschka (coding the KV cache from scratch), vLLM blog (KV cache crunching)

### Created: concepts/process-supervision.md
- **Parent topic:** harness-engineering (prerequisites policy)
- **What:** Process supervision is the infrastructure discipline of managing long-running AI agent processes — automatic restart on failure, health monitoring, supervised process trees, and cgroup-based resource control. A prerequisite for building reliable agent harnesses that must supervise subprocesses (tool execution, sandboxed code).
- **Sources:** Brightlume AI (long-running agents), OmniDaemon (PyPI), s6/skarnet documentation

### Enriched: concepts/capability-based-security.md (skeleton → full)
- **Parent topic:** sandbox (laterals policy)
- **What:** Capability-based security is an alternative security paradigm to ACLs/RBAC where authority is transmitted via unforgeable capabilities rather than identity-based checks. Applied to agent sandboxing, it enables fine-grained permissions without ambient authority. Merged from old skeleton (capabilities-based-security.md) into complete page.
- **Sources:** Wikipedia (capability-based security), Cowork Security Architecture (Medium)

### Files affected:
- Created: concepts/kv-cache.md
- Created: concepts/process-supervision.md
- Enriched: concepts/capability-based-security.md
- Deleted: concepts/capabilities-based-security.md (merged)
- Updated: index.md (+3 factual entries, -1 stub)
- Updated: hot-topics.yaml (last_crawled for context-engineering, harness-engineering, sandbox)
- Added: raw/articles/crawl-2026-04-28-kv-cache.md
- Added: raw/articles/crawl-2026-04-28-process-supervision.md
- Added: raw/articles/crawl-2026-04-28-capability-based-security.md

## [2026-04-29] newsletter ingest | Batch 2026-04-28/29

Processed triage checkpoint from newsletters dated 2026-04-28 and 2026-04-29.

### New Pages Created:
- **entities/gpt-5.5.md** — GPT-5.5 model entity (benchmarks, token efficiency, agentic patterns)
- **entities/poolside.md** — Poolside company entity with Laguna XS.2 and M.1 models (MoE architecture, open-weight release)
- **concepts/ai-agent-engineering.md** — Platform architecture for agent execution (Anthropic Managed Agents vs OpenAI Symphony)

### Pages Updated:
- **entities/openai.md** — Microsoft deal "breakup" details, new sources
- **entities/microsoft.md** — New entity page created (previously didn't exist)
- **entities/cursor-3.md** — SpaceX/xAI $60B option deal, funding round pause
- **entities/nvidia.md** — Nemotron 3 Nano Omni release details
- **concepts/gpt-5.5.md** — Benchmarks (Epoch Capabilities Index: 159, FrontierMath Tier 4), VibeBench, ParseBench
- **concepts/claude-managed-agents.md** — Public beta launch (April 2026), platform-level orchestration
- **concepts/harness-engineering.md** — Mistral Workflows public preview, Agentic Literacy section
- **concepts/serving-llms-vllm.md** — vLLM v0.20.0 TurboQuant 2-bit KV cache, DeepGEMM MoE kernels
- **index.md** — Added new entries, updated total page counts
- **log.md** — Appended this entry

### Sources Processed:
- [OpenAI Breaks Free From Microsoft](https://link.mail.beehiiv.com/v1/c/...) (2026-04-28)
- [Ben's Bites - Builders](https://substack.com/home/post/p-195538456) (2026-04-28)
- [AINews - Not Much Happened Today](raw/newsletters/2026-04-29-ainews-not-much-happened-today.md) (2026-04-29)

### Skipped:
- Couch-to-5K for AI (behavioral/habit content, not technical AI)
- Substack UI noise (like buttons, comment links, share links)

## [2026-04-29] Active Crawl [deepdive + deepdive + prerequisites] | ai-agent-engineering → Engineering Discipline Patterns / dspy → Khattab's Law / ai-memory-systems → Memory Scaling

**Scope:** Daily active knowledge crawl based on hot-topics.yaml. Selected topics with last_crawled ≥ 3 days:
- ai-agent-engineering (deepdive, high) — last_crawled 2026-04-25
- dspy (deepdive, high) — last_crawled 2026-04-25
- ai-memory-systems (prerequisites, medium) — last_crawled 2026-04-25

### Enriched: concepts/ai-agent-engineering.md (deepdive)
- **Parent topic:** ai-agent-engineering (deepdive)
- **Added:** "Engineering Discipline Patterns for AI Agents" section — Paul Duvall's 5 patterns (Specification-Driven, Codified Rules, Atomic Decomposition, Observable Development, Ralph Loops), XP revival in AI workflows (Red/Green/Refactor, trunk-based dev, plan mode), Shift-Left/Shift-Right feedback loops, evolution of engineering role toward "one pizza teams"
- **Source:** InfoQ / Paul Duvall (March 2026) — raw/articles/crawl-2026-04-29-paul-duvall-agentic-patterns.md

### Enriched: concepts/dspy.md (deepdive)
- **Parent topic:** dspy (deepdive)
- **Added:** "Khattab's Law: The Production Adoption Gap (2026)" section — the observation that any complex AI system rebuilds DSPy's abstractions ad hoc; canonical seven-stage evolution; production users (JetBlue, Databricks, Replit); download gap (4.7M vs 222M); adoption barriers (labeled data requirement, exploratory friction, lighter alternatives like LiteLLM, academic roots)
- **Source:** Agent Wars / Skylar Payne (March 24, 2026) — raw/articles/crawl-2026-04-29-dspy-adoption-gap-khattabs-law.md

### Created: concepts/memory-scaling.md (prerequisites)
- **Parent topic:** ai-memory-systems (prerequisites policy)
- **What:** Memory Scaling is a third scaling axis (alongside parametric and inference-time scaling) where agent performance improves via accumulated external memory. Introduced by Databricks AI Research (April 2026). The MemAlign framework distills episodic interactions into semantic rules, enabling smaller models with rich memory stores to outperform larger models.
- **Why it's a prerequisite:** Understanding why memory systems matter requires understanding the scaling dynamics they unlock — memory scaling explains the ROI of building persistent memory for AI agents.
- **Source:** Databricks Engineering Blog (April 10, 2026) — raw/articles/crawl-2026-04-29-databricks-memory-scaling.md

### Files affected:
- Created: concepts/memory-scaling.md
- Updated: concepts/ai-agent-engineering.md (added Engineering Discipline Patterns section)
- Updated: concepts/dspy.md (added Khattab's Law section, frontmatter sources)
- Created: raw/articles/crawl-2026-04-29-databricks-memory-scaling.md
- Created: raw/articles/crawl-2026-04-29-paul-duvall-agentic-patterns.md
- Created: raw/articles/crawl-2026-04-29-dspy-adoption-gap-khattabs-law.md
- Updated: index.md (+1 entry, total 660)
- Updated: config/hot-topics.yaml (last_crawled for ai-agent-engineering, dspy, ai-memory-systems)

## [2026-04-30] lint | Wiki health check — 72 broken wikilinks, 75 orphan pages, 103 missing from index, 16 incomplete frontmatter, 124 stale articles

- **Broken wikilinks:** 72 unique broken links detected (top offenders: agent-engineering, boris-cherny subpages, concepts/dspy-architecture/*, drew-breunig subpages, harness-engineering subpages)
- **Orphan pages:** 75 pages with zero inbound links (includes _index.md files, agent-memory.md, clinical-ai.md, etc.)
- **Missing from index:** 103 pages exist on disk but are not listed in index.md
- **Frontmatter issues:** 1 file missing frontmatter entirely (log-2026.md), 16 files missing `type` field
- **Stale raw articles:** 124 articles >30 days old by filename date; 1,950 total raw articles (32 berthub.eu political articles likely need cleanup)
- **Duplicates:** 8 entity groups with same root name (boris-cherny, claude-code, clefourrier, drew-breunig, dspy, eugene-yan, jason-liu, ryan-lopopolo); 54 concept groups with same root name (mostly `_index.md` in subdirs + duplicate concept pages)
- **Fixed:** Added `coding-agent` and `memory-system` to canonical tag taxonomy in SCHEMA.md (were being used but not declared)
- **Tag sprawl:** 1,524 tag uses not matching canonical taxonomy — need bulk cleanup or taxonomy expansion
