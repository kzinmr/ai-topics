# Change Log

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

