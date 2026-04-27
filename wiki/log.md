## [2026-04-27] create | [[concepts/claude-code-tips]] — Claude Code in Docker with VSCode Dev Containers

### New Concept Pages
- [[concepts/claude-code-tips]] — Running Claude Code in Docker with VSCode Dev Containers for security isolation and cost efficiency. Covers motivation (security, performance, cost), step-by-step setup guide, fine-grained GitHub token configuration, and comparison with alternatives.
  - Source: timsh.org article "Switching to Claude Code + VSCode inside Docker"
  - GitHub reference implementation: tim-sha256/claude-in-docker
  - Related: agent-sandboxing, container-context, claude-code-leak
- [[index.md]] — Added entry under Concepts section (alphabetically after claude-code-source-patterns); total pages updated 575→576

---

## 2026-04-27 — X Bookmark Ingest (X native articles) — Part 2

### New Entity Pages
- **entities/ramp-labs.md** — AI research company focused on KV cache compaction for multi-agent systems; created Latent Briefing
- **entities/intuit-machine.md** — AI agent framework company; published 10 Design Principles of Agentic AI Skills
- **entities/anthropic.md** — Updated with Claude Managed Agents platform info
- **entities/jaya-gupta.md** — Foundation Capital partner, co-author of Context Graphs and Trillion-Dollar Loop
- **entities/foundation-capital.md** — Updated with Trillion-Dollar Loop and Claude Managed Agents articles

### Updated Entity Pages
- **entities/koylan-ai.md** — Added "Personal OS for AI Agents" (April 27, 2026) section — vision of phone as personal brain, first-class OS agents, memory systems, coordination layer
- **entities/anthropic.md** — Added Memory Stores section (April 27, 2026) — workspace-scoped memory, /mnt/memory/ mount, multi-agent sync, concurrency handling, API export

### New Concept Pages
- **concepts/agent-harness.md** — Definition of agent harness (context + toolset + guardrails); R.E.S.T framework, PPAF cycle
- **concepts/kv-cache-compaction.md** — KV cache optimization techniques (comprehensive, hybrid, dynamic, compaction)
- **concepts/latent-briefing.md** — Ramp Labs' method for sharing memory between agents via KV cache compaction
- **concepts/agentic-ai-skills.md** — Intuit Machine's 10 design principles for AI agent skills
- **concepts/personal-os-for-ai-agents.md** — Koylan AI's vision of phone as "personal brain" with AI agents, memory, web access, coordination
- **concepts/claude-managed-agents.md** — Claude Managed Agents platform with memory stores — workspace-scoped text documents, real-time multi-agent sync, concurrency handling, API export
- **concepts/filesystem-memory.md** — Filesystem-as-agent-memory pattern: using standard file I/O for persistent memory. Validated by Claude Plays Pokémon experiment showing models learn to organize memory files as intelligence scales.

### Raw Articles Saved
- raw/articles/2039441705586602134_The-Trillion-Dollar-Loop-B2B-Never-Had.md
- raw/articles/2039737982576636294_Googles-20-Year-Secret-Is-Now-Available.md
- raw/articles/2041927992986009773_Launching-Claude-Managed-Agents.md
- raw/articles/2042539396638085339_Harness-Engineering.md
- raw/articles/2042660310851449223_Latent-Briefing-Efficient-Memory-Sharing.md
- raw/articles/2043071219667480853_Ten-Design-Principles-of-Agentic-AI-Skills.md
- raw/articles/2043609541477044439_Google-Engineer-Automated-80-of-Work-with-Claude-Code.md
- raw/articles/2025286163641118915_The-File-System-Is-the-New-Database-Personal-OS-for-AI-Agents.md
- raw/articles/2047720067107033525_Memory-in-Claude-Managed-Agents.md

## 2026-04-27 — X Bookmark Ingest (X native articles) — Part 3

### New Entity Pages
- **entities/letta.md** — Letta AI / Letta Code (model-agnostic agent harness)
  - Source: X article from @letta_ai (214 bookmarks)

### Updated Concept Pages
- **concepts/harness-engineering.md** — Added "Open Source Agent Harnesses" comparison table
- **concepts/gemini.md** — Added "Gemini Embedding API as Multimodal Encoder" section

### New Concept Pages
- **concepts/thin-bi.md** — Thin BI evolution (comprehensive platform → thin interface)

### Raw Articles Saved
- raw/articles/2033670953956479223_lettas-next-phase.md
- raw/articles/2033543094373859488_turning-geminis-embedding-api-into-a-universal-mul.md
- raw/articles/2033336956961308721_薄くなるbiツール.md

## 2026-04-27 — Pi Coding Agent Articles Ingest

### Raw Articles Saved
- raw/articles/mariozechner.at--posts-2025-11-30-pi-coding-agent.md — Mario Zechner blog: "What I learned building an opinionated and minimal coding agent" — design philosophy, 4-package architecture, core principles
- raw/articles/docs.openclaw.ai--pi-integration-architecture.md — OpenClaw embedding pi SDK directly (not subprocess/RPC) — custom tool injection, session lifecycle, provider-agnostic model switching
- raw/articles/syntax.fm--976-pi-coding-agent.md — Syntax.fm #976 podcast: Armin Ronacher & Mario Zechner discuss pi, OpenClaw, bash minimalism, agent security risks
- raw/articles/github.com--disler-pi-vs-claude-code-comparison.md — Feature comparison: Claude Code vs Pi Agent (v0.52.10) — MIT license, multi-provider support, context handoff, in-process hooks vs MCP, JSONL session tree with branching

### Updated Entity Pages
- **entities/mario-zechner.md** — Already has pi-coding-agent mention; these articles provide deep technical source material for future enrichment
- **entities/peter-steinberger.md** — OpenClaw creator; pi integration is core to architecture

### Raw Articles NOT ingested (already covered)
- https://www.npmjs.com/package/@mariozechner/pi-coding-agent — npm registry page (not a technical article)

### Processed
- 125 total bookmarks processed
- 3 X native articles extracted via Bearer token API and wiki-edited
- 2 non-article bookmarks skipped (no article content)

## [2026-04-27] x-bookmarks-ingest | 4 new concept pages + 1 entity page + 1 concept update

- [deepdive] The Definitive Guide to Harness Engineering → Updated `concepts/harness-engineering.md`
  - **Key idea**: R.E.S.T framework (Reliability, Efficiency, Security, Transparency), Horse and Reins metaphor
  - PPAF cycle, Context Management, Function Calling design principles
  - Updated harness-engineering.md with R.E.S.T framework, PPAF cycle, and 3 new cross-references

- [deepdive] The Runtime Behind Production Deep Agents → `concepts/deep-agents-runtime.md` (NEW)
  - **Key idea**: Deep Agents runtime packages durable execution, memory, multi-tenancy, guardrails, HITL, observability, sandboxed code execution, scheduled cron
  - Built on LangGraph/LangSmith, supports multi-tenancy with Stripe-like pricing isolation
  - Guardrails: prompt injection prevention, PII redaction, jailbreak detection, rate limiting

- [monitor] Hermes Agent Polymarket Self-Learning Weather Trading Bot → `concepts/polymarket-trading-agents.md` (NEW)
  - **Key idea**: AI agent autonomously trading Polymarket prediction markets 24/7
  - Weather, crypto, sports markets — autonomous position sizing via Kelly Criterion
  - Self-learning with reinforcement learning, multi-agent coordination

- [deepdive] Turning the Entire Web Into a Filesystem → `concepts/web-as-filesystem.md` (NEW)
  - **Key idea**: Mount the entire web as a Unix filesystem — `tree`, `grep`, `cat`, `find` for documentation
  - Agent can search entire docs, build dependency graphs, cross-reference
  - Implementation: Nia (Nozomio Labs)

- [entity] What People Are Actually Using Hermes Agent For → `entities/hermes-agent.md` (ENRICHED)
  - **Key idea**: Community-driven use cases from Reddit, X, YouTube
  - Popular uses: DevOps automation (28%), code generation (23%), data analysis (18%)
  - Migration from OpenClaw, self-hosted advantages, privacy concerns

### Raw Articles Saved
- `raw/articles/2026-04-27_2047145274200768969_The-Definitive-Guide-to-Harness-Engineering.md`
- `raw/articles/2026-04-27_2046277232537256002_The-Runtime-Behind-Production-Deep-Agents.md`
- `raw/articles/2026-04-27_2045080054917476451_Hermes-Agent-Polymarket-Self-Learning-Weather-Trading-Bot.md`
- `raw/articles/2026-04-27_2045935785661349956_Hermes-Agent-What-People-Are-Actually-Using-It-For.md`
- `raw/articles/2026-04-27_2041215978957389908_Turning-the-Entire-Web-Into-a-Filesystem.md`

### Wiki Pages Created/Updated
- NEW: `concepts/deep-agents-runtime.md` — Deep Agents runtime (LangChain/Anthropic production agent framework)
- NEW: `concepts/polymarket-trading-agents.md` — Polymarket prediction market trading agents
- NEW: `concepts/web-as-filesystem.md` — Web-as-filesystem concept (Nia/Nozomio Labs)
- UPDATED: `concepts/harness-engineering.md` — Added R.E.S.T framework, PPAF cycle, context management
- NEW: `entities/hermes-agent.md` — Enriched Hermes Agent entity page with community use cases

### Index Updates
- `concepts/_index.md` — Added Web-Filesystem.Md, Deep-Agents-Md, Polymarket-Trading-Agents sections
- `entities/_index.md` — Updated hermes-agent entry

---

## [2026-04-27] x-accounts-scan | 6 new concept pages created from X posts

- [deepdive] Shopify Reflexive AI → [[reflexive-ai]]
  - **Key idea**: Reflexive AI framework — agents that reflect on their own behavior to improve
  - Continuous improvement loop: act → reflect → adapt
  - New page: concepts/reflexive-ai.md

- [monitor] Solo Founder Stack 2026 → [[solo-founder-stack]]
  - **Key idea**: One-person unicorn toolkit — AI-powered stack enabling solo founders to build billion-dollar companies
  - Dario Amodei: 70-80% chance of one-person billion-dollar company by 2026
  - New page: concepts/solo-founder-stack.md

- [deepdive] Agreement is a Bug (NYK Builderz) → [[agreement-bug]]
  - **Key idea**: Forcing 11 Claude Code agents to disagree before agreeing uncovers blind spots
  - 40+ architecture decisions tested with structured disagreement
  - New page: concepts/agreement-bug.md

- [monitor] Mac Studio for Local AI → [[mac-studio-local-ai]]
  - **Key idea**: Mac Studio (M3/M4 Ultra, 512GB unified memory) as local LLM inference platform
  - 600B-1T parameter models feasible with 4-bit quantization
  - MLX 10-25% faster than llama.cpp on Apple Silicon
  - New page: concepts/mac-studio-local-ai.md

---

## [2026-04-27] create | [[concepts/ai-industry-news]] — AI industry roundup from The Signal (Apr 26)

### New Concept Pages
- [[concepts/ai-industry-news]] — Summary of The Signal newsletter by Alex Banks (Apr 26, 2026). Covers OpenAI's four-product launch week (ChatGPT Images 2, GPT-5.5, Workspace Agents, ChatGPT for Clinicians), Anthropic's expansion (Cowork live artifacts, Managed Agent memory via text files, 15 new consumer connectors), and SpaceX-Cursor strategic partnership ($60B acquisition option).
  - Source: `raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md`
  - Cross-references: [[entities/openai]], [[entities/anthropic]], [[concepts/chatgpt-images-2.0]], [[concepts/gpt-5.5]], [[concepts/openai-workspace-agents]], [[concepts/cursor-ide]]

### Index Updates
- Added entry under Concepts (alphabetically after ai-index-report-2026); total pages 577→578

---

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-27] create | [[concepts/cryptography-patterns]] — Bitwarden encryption architecture

### New Concept Pages
- [[concepts/cryptography-patterns]] — Bitwarden/Vaultwarden encryption and decryption architecture. Documents: two-layer encryption design (passphrase→master key→secrets), master key generation (64 random bytes → enc_key + mac_key), key derivation via PBKDF2-HMAC-SHA256 (600K iterations) with HKDF-Expand stretching (or Argon2id alternative), AES-256-CBC with PKCS7 padding, HMAC-SHA256 integrity verification, cipherstring format (version.iv|ciphertext|mac), and the full decryption process.
  - Source: Miguel Grinberg article "How Bitwarden Encrypts and Decrypts Secrets"
  - Related: [[concepts/self-hosting-ai-development]], [[entities/miguel-grinberg]]
- [[index.md]] — Added entry under Concepts section (alphabetically after critique-shadowing, before cybersecurity-proof-of-work); total pages updated 578→579

---

## [2026-04-27] update | [[concepts/harness-engineering/agentic-workflows/vibe-coding]] + [[entities/xeiaso-net]] — enrich with Apr 27 articles

### Updated: Vibe Coding
- Expanded "実践事例" section with two comprehensive subsections:
  - **Xe Iaso: Sponsor PanelをVibe Codingで構築** — enriched with GraphQL swamp background, Skills details (4 templ skills), parallel ops/code-generation workflow, full tech stack table, limitations (org sponsorships broken, code quality), and the "ugly but shipped" philosophy
  - **Tim Sh: セルフホスティングでVibe Codingアプリを運用** — new section: Coolify + Hetzner VPS setup, cloud PaaS pricing critique, levels of abstraction framework, 15-minute local-to-production pipeline for vibecoded apps
- Sources:
  - `raw/articles/xeiaso.net--blog-2026-vibe-coding-sponsor-panel--10523b6c.md`
  - `raw/articles/timsh.org--why-you-should-self-host--bff25172.md`

### Updated: Xe Iaso (xeiaso-net)
- Added **"Claude Code /buddy: The Perfect April Fools Prank (2026)"** section — Xe's 10/10 review of Claude Code's `/buddy` tamagochi feature, the Xentwine robot companion, and analysis of why opt-in harmless pranks succeed where disruptive April Fools jokes fail
- Added both new articles to Sources section
- Source: `raw/articles/xeiaso.net--notes-2026-claude-code-wins-april-fools--f3f49e16.md`

---


- Updated GPT-5.5 entry with Codex unification info: since GPT-5.4, no separate coding model — unified into single system
- Updated Codex entry to reflect that no GPT-5.5-Codex will be released
- Added raw source: Simon Willison quoting Romain Huet (OpenAI DevRel lead)
- Source: `raw/articles/simonwillison.net--2026-apr-25-romain-huet--fea00393.md`

## [2026-04-26] ingest | Mac Studio for Local AI — 6 Months Later (spicyneuron / Elvis Sun)
- Raw article: `raw/articles/spicyneuron-mac-studio-local-ai-6months.md`
- Source: https://spicyneuron.substack.com/p/a-mac-studio-for-local-ai-6-months
- Key findings:
  - Mac Studio M3 512GB viable for running 600B–1T parameter models daily
  - MLX framework 10–25% faster than llama.cpp on Apple Silicon
  - MoE architectures essential for leveraging unified memory
  - Claude Code runs locally at usable speeds (~90s for 16k tokens)
  - GPU memory override reclaims ~120GB beyond macOS default 75% cap
  - 4-bit dynamic quantization is the sweet spot for Apple Silicon
- New entity page: `entities/elvis-sun.md` — Elvis Sun (spicyneuron), AI researcher and newsletter author
- New concept page: `concepts/mac-studio-local-ai.md` — Mac Studio hardware setup, performance benchmarks, MoE model selection, prompt caching fixes
- New concept page: `concepts/mlx-llm.md` — Apple MLX framework, mlx-lm vs mlx-vlm, comparison with llama.cpp
- Total pages created: 3 (1 entity + 2 concepts)

## [2026-04-26] create | [[concepts/mcp]] — Model Context Protocol concept page

### New Concept Pages
- [[concepts/mcp]] — Model Context Protocol: open standard for connecting AI agents to tools and data sources
  - Created by Anthropic; adopted by OpenAI, Google, Red Hat
  - 150M+ SDK downloads; outpacing React's first 3 years in 16 months
  - Core primitives: resources, tools, prompts over stdio/HTTP transport
  - 2026 roadmap: triggers, streaming, skills, enterprise integration
  - Security concerns: RCE vulnerabilities in MCP servers identified by OX Security
  - Sources: troyhunt.com HIBP MCP article, LangChain anatomy of agent harness, Gemini Deep Research
  - Added to index.md (concept count 6→7, total 16→17)
- Updated SCHEMA.md: added `protocol` tag to taxonomy

## [2026-04-25] create | Wiki initialized
- Domain: AI/ML research and engineering
- Structure created: SCHEMA.md, index.md, log.md
- Directory structure: entities/, concepts/, comparisons/, queries/, raw/

## [2026-04-25] ingest | ChatGPT Images 2.0 is genuinely fantastic (The Signal newsletter)
- Raw article saved: `raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md`
- Created entity pages: `entities/openai.md`, `entities/google.md`, `entities/gemini.md`
- Created concept pages: `concepts/gpt-image-2.md`, `concepts/ai-image-generation.md`, `concepts/nano-banana-2.md`
- Created comparison page: `comparisons/gpt-image-2-vs-nano-banana-2.md`
- Total pages created: 7

## [2026-04-25] active-crawl | 3 concepts from 3 hot-topic crawls
- **dspy** (deepdive, high) → [[gapa]] — ICLR 2026 Oral paper on reflective prompt evolution outperforming RL
- **dspy** (deepdive, high) → [[concepts/recursive-language-models]] — RLM: inference paradigm for unbounded context via recursive LM calls
- **context-engineering** (prerequisites, high) → [[concepts/memory-architecture]] — Three-layer memory model (episodic, semantic, state) for production agents
- Raw articles saved: 3 in raw/articles/
- Total new pages: 3 (concepts)

## [2026-04-26] ingest | China AI Machine newsletter + Claude Code newsletter
- Raw articles saved:
  - `raw/articles/2026-04-25-china-ai-robotics-industry-competitive-landscape.md` (Newsweek, TheRoboWire, AI2Work)
  - `raw/articles/2026-04-26-claude-code-anthropic-agentic-coding-system.md` (Anthropic docs, AI Wiki)
  - `raw/newsletters/2026-04-25-my-four-days-inside-china-s-ai-machine-tales-and-analysis.md`
  - `raw/newsletters/2026-04-26-dive-into-claude-code.md`
- Created entity pages (11):
  - `entities/china-ai-industry.md` — China's comprehensive AI/robotics ecosystem
  - `entities/unitree-robotics.md` — World's #1 humanoid robot seller; pricing disruption
  - `entities/deepseek.md` — Open-source LLM cost disruption
  - `entities/xpeng.md` — EV manufacturer with robotics and flying vehicle divisions
  - `entities/dji.md` — Global drone market dominance
  - `entities/ubtech-robotics.md` — Service robots and humanoid platforms
  - `entities/agi-bot.md` — Second-largest Chinese humanoid robot seller
  - `entities/fourier-intelligence.md` — Rehabilitation and humanoid robotics
  - `entities/claude-code.md` — Anthropic's agentic coding system
  - `entities/anthropic.md` — American AI company; Claude models and Claude Code
- Created concept pages (1):
  - `concepts/open-source-ai.md` — Open-source AI strategy and adoption feedback loops
- Created comparison pages (2):
  - `comparisons/ai-agent-platforms.md` — Claude Code vs OpenAI Codex architectures
  - `comparisons/ai-competition.md` — U.S. vs China strategic divergence
- Total pages created: 15 (11 entities + 1 concept + 2 comparisons + 1 existing concept update)

## [2026-04-26] create | [[turboquant]] + [[dflash]] — AI inference optimization concepts

### Raw Articles
- `raw/articles/turboquant-google-research-blog.md` — Google Research blog post on TurboQuant
- `raw/articles/turboquant-arxiv-2504-19874.md` — arXiv paper by Zandieh, Daliri, Hadian, Mirrokni
- `raw/articles/turboquant-lmcache-blog.md` — LMCache/Tensormesh blog by Kuntai Du
- `raw/articles/dflash-z-lab-arxiv-2602-06036.md` — arXiv paper by Jian Chen, Yesheng Liang, Zhijian Liu

### New Concept Pages
- [[turboquant]] — Google's vector quantization for LLM KV cache compression
  - Two-stage quantization: PolarQuant (random rotation + scalar quantization) + 1-bit QJL residual correction
  - KV cache: 3.5 bits/channel quality-neutral, 2.5 bits/channel marginal degradation
  - 6x memory reduction, 4x context capacity per GPU
  - Within ~2.7x constant of information-theoretic lower bounds
  - Sources: Google Research Blog, arXiv:2504.19874, LMCache Blog
- [[dflash]] — Block diffusion for speculative decoding (z-lab)
  - Replaces sequential autoregressive drafting with parallel block diffusion
  - Single forward-pass drafting, context-aware conditioning from target LLM
  - >6x lossless speedup, 2.5x higher than SOTA EAGLE-3
  - Supports Qwen3.5-122B-A10B, Qwen3.6-35B-A3B, Kimi-K2.5, gpt-oss-120b, LLaMA-3.1
  - GitHub: 2.3k stars, MIT license, vLLM/SGLang/Transformers/MLX integration
- [[concepts/agent-swarms]] — Added to index (multi-agent coordination patterns)
- [[ai-competition]] — Added to Comparisons section in index

### Index Updates
- Total pages: 17 → 19 (added turboquant, dflash; fixed agent-swarms and ai-competition entries)
- SCHEMA.md: added `quantization`, `speculative-decoding`, `diffusion` tags to Techniques taxonomy
## [2026-04-26] dreaming | Knowledge consolidation — 21 articles, 8 themes

### Checkpoint
- Run ID: 20260426T180018Z
- Articles processed: 21
- Themes evaluated: 8

### Duplicate Check Summary
- Already processed (previous runs): 7/8 themes
- New page created: 1
- Gaps filled: 0

### Processed Themes (all previously handled)
1. **ChatGPT Images 2.0 reasoning** — ✅ Already in `concepts/chatgpt-images-2.0.md`
2. **Claude Code Routines + Opus 4.7** — ✅ Already in `concepts/claude-code-routines.md`
3. **Anthropic Big Swing strategy** — ✅ Already in `entities/anthropic.md`
4. **Gemini ecosystem expansion** — ✅ Already in `concepts/gemini.md`
5. **Claude Design (Anthropic Labs)** — ✅ **NEW page created** → `concepts/claude-design.md`
6. **GPJT LLM from Scratch 32l** — ✅ Already in `entities/gpjt.md`
7. **ARC-AGI-2 benchmark trends** — ✅ Already in `concepts/arc-agi-2.md`
8. **Anti-AI conservative political arguments** — ✅ Already in `concepts/ai-criticism-politics.md`

### New Pages
- `concepts/claude-design.md` — Anthropic Labs product for collaborative visual design via conversational AI

### Updated Pages
- `index.md` — Added claude-design entry, total pages 22→23

### Notes
- Pre-run script failed to parse JSON checkpoint (`ok: false`), but grouped themes were loaded from `grouped_themes_latest.json`
- Most themes were already processed in earlier runs (active-crawl, daily ingest)
- Claude Design was the only theme requiring new page creation
- 7/8 themes had complete coverage from previous runs — no gaps identified

## 2026-04-27 — X Bookmarks Ingest (6 articles)

### X Native Article API 成功

`GET /2/tweets/:id?tweet.fields=article,entities` で `plain_text` フィールドが取得可能を確認。Bearer tokenのアクセスレベルは `read-write-directmessages`（Elevated相当）。

### Raw Articles (6件)
1. `2041206959848735107` @ankrgyl — AI observability is a database problem: how Brainstore works (13,358 chars)
2. `2040467997022884194` @hwchase17 — Continual learning for AI agents (5,376 chars)
3. `2041185537172607014` @dani_avila7 — Skills can use subagents, Subagents can use skills (3,309 chars)
4. `2041146899319971922` @akshay_pachaar — The Anatomy of an Agent Harness (18,056 chars)
5. `2041897427431563613` @ericzakariasson — Optimizing your dev environment for coding agents (3,547 chars)
6. `2041479655035679163` @carnot_cyclist — Defining Continual Learning (12,005 chars)

### Wiki Updates
- **NEW:** `concepts/continual-learning.md` — 新規作成（3層学習 + 古典ML定義）
- **UPDATED:** `concepts/harness-engineering.md` — 3層学習フレームワーク + Agent Harness Anatomyセクション追加
- **UPDATED:** `concepts/subagents.md` — Skills/Subagents相互関係セクション追加
- **UPDATED:** `concepts/coding-agents.md` — stub→complete（Eric Zakariasson記事をベースに更新）
- **UPDATED:** `concepts/ai-observability.md` — Brainstoreセクション追加
|- **UPDATED:** `index.md` — continual-learningエントリ追加

---

## 2026-04-27 — Newsletter Ingest (The Signal: OpenAI Is Cooking)

### New Concept Pages
- **concepts/gpt-5.5.md** — First fully retrained base model since GPT-4.5; 82.7% Terminal-Bench 2.0
- **concepts/openai-workspace-agents.md** — Codex-powered shared agents for Business/Enterprise plans
- **concepts/world-id-4-agentkit.md** — World ID 4.0 iris-scanning + AgentKit cryptographic human attestation

### Updated Entity Pages
- **entities/openai.md** — GPT-5.5, Workspace Agents, ChatGPT Images 2.0 Thinking mode/Image Arena #1, ChatGPT for Clinicians
- **entities/anthropic.md** — Mythos breach, Live Artifacts, Consumer connectors (200+), Managed Agents file-based memory

### Updated Concept Pages
- **concepts/gpt-models.md** — GPT-5.5 added to model lineage table
- **concepts/coding-agents.md** — SpaceX×Cursor $60B acquisition option, OpenAI Workspace Agents section
- **concepts/ai-memory-systems.md** — Anthropic Managed Agents file-based memory approach
- **concepts/chatgpt-images-2.0.md** — Thinking mode with web search, Image Arena #1 (+242 over NB2), 2K resolution

### Updated Navigation
- **index.md** — 3 new concept entries (gpt-5.5, openai-workspace-agents, world-id-4-agentkit); total pages 575

### Raw Source
- `raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md` — newsletter saved as source

### Follow-up Batch (Triage Processing)

#### Updated Entity Pages
- **entities/cursor-3.md** — SpaceX partnership details: $60B acquisition option / $10B collaborative work alternative, Composer 2 on Moonshot's Kimi, Kevin Kwok analysis
- **entities/claude-code.md** — Pricing test incident (Apr 2026): quietly removed from $20 Pro plan, fake door probe, inference cost economics, Rohan Varma mockery
- **entities/anthropic.md** — Added newsletter as additional source reference

#### Updated Navigation
- **index.md** — cursor-3 entry updated with SpaceX partnership summary


## [2026-04-27] ingest | Blog batch (Apr 27, 2026) — 6 articles processed

### New Concept Pages
- [[concepts/self-hosting-ai-development]] — Self-hosting patterns for AI-generated applications: Coolify + Hetzner stack, cost comparison vs Vercel/Railway, downsides and mitigations
  - Source: timsh.org "Why you should self-host your (vibecoded) app"

### Updated Concept Pages
- [[concepts/harness-engineering/agentic-workflows/vibe-coding]] — Added Xe Iaso's practical sponsor panel creation experience: skills-as-context pattern, mock-data-first iteration, "ugly but shipped" ethos
  - Source: xeiaso.net "Vibe Coding Trip Report"
- [[concepts/harness-engineering/agentic-engineering]] — Added Xe Iaso's abstraction costs perspective: "fine is the enemy of good", emotional weight of form letter, voice as non-negotiable
  - Source: xeiaso.net "I don't know if I like working at higher levels of abstraction"
- [[concepts/gpt-5.5]] — Added Codex Unification detail: since GPT-5.4, Codex and main model unified into single system; no separate coding line model
  - Source: Romain Huet via simonwillison.net

### Updated Entity Pages
- [[entities/openai]] — Added GPT-5.5 Codex unification: no GPT-5.5-Codex model; single unified system
- [[entities/xeiaso-net]] — Added recent blog activity (Apr 2026): vibe coding trip report, abstraction costs essay, Claude Code April Fools note

### Updated Navigation
- [[index.md]] — Added concepts/self-hosting-ai-development under Concepts section

## [2026-04-27] blog-ingest | Batch 2 — Theseus AI funding, Harness Engineering principles

### New Concepts
- [[concepts/ai-industry-news]] — AI industry roundup from The Signal by Alex Banks (Apr 26). Covers OpenAI's 4-product week, Anthropic sweep (Cowork artifacts, Managed Agent file-based memory, 200+ connectors), SpaceX-Cursor partnership.
  - Source: raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
- [[concepts/cryptography-patterns]] — Miguel Grinberg's deep-dive into Bitwarden/Vaultwarden encryption architecture: two-layer design, PBKDF2/Argon2id derivation, AES-256-CBC + HMAC-SHA256, cipherstring format. Python code examples.
  - Source: raw/articles/blog.miguelgrinberg.com--post-how-bitwarden-encrypts-and-decrypts-secrets--146d9a70.md
- [[concepts/claude-code-tips]] — Running Claude Code inside Docker with VSCode Dev Containers. Security isolation, cost efficiency vs Cursor Pro, fine-grained GitHub token setup.
  - Source: raw/articles/timsh.org--claude-inside-docker--6842418e.md

### Updated
- [[concepts/agentic-engineering]] → [[concepts/harness-engineering/agentic-engineering]] — Made redirect to canonical location

### Raw Articles Saved
- raw/articles/timsh.org--switching-to-claude-code-vscode-inside-docker--*.md
- raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
- raw/articles/blog.miguelgrinberg.com--post-how-bitwarden-encrypts-and-decrypts-secrets--146d9a70.md
