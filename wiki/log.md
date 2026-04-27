## [2026-04-27] x-bookmarks-ingest | 5 new concept pages created

- [monitor] Telegram Bot API 9.6 → [[telegram-managed-bots]]
  - **Key idea**: No-code bot creation system where manager bots provision and control subordinate bots
  - Bot API 9.6 adds can_manage_bots, ManagedBotCreated, getManagedBotToken primitives
  - New page: concepts/telegram-managed-bots.md

- [deepdive] Karpathy AutoResearch → [[autoreason]]
  - **Key idea**: Self-refinement framework extending karpathy-loop into subjective reasoning via blind Borda count voting
  - Fixes three structural failures: prompt bias, scope creep, lack of restraint
  - New page: concepts/autoreason.md

- [monitor] Khe Hy framework → [[company-ai-pilled]]
  - **Key idea**: Organizational AI maturity model distinguishing surface AI usage from deep cultural transformation
  - Levels: AI User → AI Adopter → AI-Pilled → AI-Native
  - New page: concepts/company-ai-pilled.md

- [deepdive] Claude Code Memory → [[claude-perfect-memory]]
  - **Key idea**: Filesystem-based persistent memory architecture with lifecycle layer (session commands, rotation crons, drift detection)
  - Extends CLAUDE.md primitives with persistent memory management
  - New page: concepts/claude-perfect-memory.md

- [monitor] Content automation → [[content-engine]]
  - **Key idea**: AI-powered content creation, curation, and distribution pipeline applying agentic engineering
  - Components: Research → Drafting → Editing → Distribution → Analytics
  - New page: concepts/content-engine.md

---

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

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

