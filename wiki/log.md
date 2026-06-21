## [2026-06-21] X Bookmarks Ingest — Loop Engineering concept + entity pages

Ingested Elvis Saravia's (@omarsar0) X Article "From Prompting Agents to Loop Engineering" (Jun 19, 2026, 2.1K bookmarks, 911 likes, 242K impressions) from X bookmarks batch.

**New pages created:**
- [[concepts/loop-engineering]] — New concept page: the engineering discipline of designing autonomous loop systems for coding agents. Covers six building blocks (trigger, isolation, context, tool reach, independent verifier, state-on-disk), five loop taxonomies (ReAct→AutoGPT→ralph loop→/goal→orchestration), concrete patterns (PR babysitter, CI health, deploy verification), Cherny's five-step unattended loop setup, crabfleet as loop infrastructure, economics (iterations as budget line), anti-patterns, and failure modes. Cross-referenced with [[concepts/agent-loop-orchestration]], [[concepts/loopcraft]], [[concepts/codex/codex-agent-loop]].
- [[entities/elvis-saravia]] — New entity page: Founder of DAIR.AI and DAIR.AI Academy, educator synthesizing practitioner insights from Steinberger, Cherny, Osmani, and Van Horn into structured educational content.

**Entities enriched:**
- [[entities/peter-steinberger]] — Added Saravia article reference to "Design Loops" section (six building blocks, five loop taxonomies, PR babysitter pattern). Updated sources and date.
- [[entities/boris-cherny]] — Added "I don't prompt Claude anymore. I have loops..." quote and five-step autonomous loop setup code block. Updated tags (+loop-engineering), sources, and date.
- [[entities/addy-osmani]] — Added Saravia article to Key Publications table and Sources section. Updated sources and date.
- [[entities/matt-van-horn]] — Added loop-engineering to related: links, Saravia article to sources. Updated date.

**Cross-references:**
- [[concepts/agent-loop-orchestration]] — Added cross-reference to loop-engineering in Related Concepts, updated tags and date.

**Raw article:** [[raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering]]
**Source:** X Article (x.com/i/article/2068004233849290752), plain_text via fetch_x_bookmarks.py
## [2026-06-21] Dreaming Wiki Ingest — Post-Recovery Enrichment

**Source:** dreaming-wiki-ingest (post-recovery from dreaming-group parse failure)
**Timestamp:** 2026-06-21 18:24 UTC

Recovered triage JSON from dreaming-group checkpoint (saved before response render failure). Post-verification of 38 decisions:

### Post-Recovery Verification Result
- **Takes=0**: "Building Reliable Agentic AI Systems" (Martin Fowler/Bayer PRINCE) already fully covered in `entities/martin-fowler.md` and `concepts/agentic-rag.md` (both created 2026-06-21)
- **References=7**: 5 already covered, 2 enriched (see below)
- **Skips=31**: 7 already-covered wiki content + 1 already-existing concept page take + 23 non-AI articles (game design, music, beer, glassblowing, DB benchmarks, licensing, energy, personal essays)

### Entities/Concepts Enriched
- **concepts/cloudflare-agents.md** — Added "Temporary Cloudflare Accounts for AI Agents" section (`wrangler deploy --temporary`, 60-min ephemeral deployments, June 2026). Updated: 2026-06-21.
- **entities/elevenlabs.md** — Added "Voice Agent Evaluation Framework (6 Pillars)" section (TTS Voice Quality, Conversation Quality, Tool Usage, Intelligence, Compliance & Safety, Reliability). Updated: 2026-06-21.

### Archive
- Archive run: 38 candidates → 23 new archived, 15 dedup skipped
- Total archive URLs: 1049

---

## [2026-06-21] Wiki Watchdog Auto-Fix — index header count reconciliation

**Source:** cron job (wiki-watchdog-fix)
**Timestamp:** 2026-06-21 17:35 UTC

### Actions Taken

1. **Index header count corrections:**
   - Entities section: 826 → 828 (filesystem confirmed 828)
   - Concepts section: 1718 → 1748 (filesystem confirmed 1748)
   - Summary line: Total pages 2590→2622, Indexed entries 2213→2221, Not in index 377→401
   - Headers and summary line now consistent with filesystem `find` counts

2. **Structural health check:**
   - Pipe corruption: 0 instances ✓
   - Line prefix corruption: 0 instances ✓
   - Triple brackets: 0 instances ✓
   - Space prefix corruption: 0 instances ✓
   - Duplicate entries: 0 instances ✓
   - Log.md missing separators: 0 sections ✓
   - Index corruption (health scan): no issues ✓

3. **Pipeline watchdog:**
   - ⚠️ `x_accounts` job stale (26h) — requires human review. Do not auto-restart.

### Stats
- Pages on disk: 2622 (828 entities, 1748 concepts, 31 comparisons, 11 events, 4 queries)
- Indexed entries: 2221 (823 entities, 1236 concepts, 31 comparisons, 11 events, 4 queries)
- Not in index: 401 (3 entities, 449 concepts — mostly skeleton/stub pages awaiting enrichment)
- Orphan pages (0 inbound links): ~49 (from health scan)

---

## [2026-06-21] Claude Blog Ingest — Claude Code Steering Methods article ingested

**Source:** https://claude.com/ja/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
**Date:** 2026-06-18
**Author:** Anthropic

### Actions Taken

1. **Raw article saved:** `raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md`
   - Full article content extracted and saved with proper frontmatter
   - Tags: claude-code, coding-agents, ai-agents, customization, hooks, skills, subagents, rules, claudefile

2. **New concept page created:** `concepts/claude-code/claude-code-steering-methods.md`
   - Comprehensive documentation of Claude Code's seven steering methods
   - Covers CLAUDE.md files, rules, skills, subagents, hooks, output styles, and system prompt appending
   - Includes comparison table, decision guide, and best practices
   - Tags: claude-code, coding-agents, ai-agents, customization, hooks, skills, subagents, rules, claudefile, developer-tools
   - Sources: raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md

3. **Index updated:** Added entry to `index.md` under Claude Code concepts section
   - Location: After `claude-code-goal` entry (line 1195)
   - Description: Seven methods for customizing Claude's behavior with comparison of loading behavior, compaction characteristics, context costs, and best use cases

### Article Summary

The article explains seven methods for instructing and customizing Claude's behavior in Claude Code:

1. **CLAUDE.md files** — Project-specific instructions that load at session start
2. **Rules** — Path-scoped constraints in `.claude/rules/`
3. **Skills** — Procedural workflows in `.claude/skills/`
4. **Subagents** — Isolated assistants for side tasks in `.claude/agents/`
5. **Hooks** — Deterministic automation on lifecycle events
6. **Output styles** — System prompt injections for role changes
7. **System prompt appending** — Additive instructions via CLI flag

Each method has different characteristics regarding:
- When instructions load into context
- Whether they persist through long sessions (compaction behavior)
- How much authority they carry

### Wiki Impact

- **New page:** `concepts/claude-code/claude-code-steering-methods.md` (9,286 bytes)
- **Updated page:** `wiki/index.md` (added entry)
- **Raw article:** `raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md` (16,507 bytes)

### Related Pages

- [[concepts/claude-code/claude-code]] — Claude Code as a coding agent
- [[concepts/claude-code/claude-code-skills]] — Claude Code Skills mechanisms
- [[concepts/claude-code/claude-code-best-practices]] — Claude Code Best Practices
- [[concepts/agentic-engineering]] — Agentic engineering patterns
- [[concepts/coding-agents]] — AI agents for software development

---

## [2026-06-21] Blog Wiki Ingest — AI-Assisted Development enriched, 2 entity pages updated

**Pipeline:** blog-ingest -> blog-triage -> blog-wiki-ingest
**Source:** blog-ingest checkpoint (11 articles + 4 unsaved)

### Pages Updated

- **concepts/ai-assisted-development.md** — Expanded from stub (24 lines) to substantive page (89 lines). Added overview, use cases, and "LLMs for Formal and Scientific Programming" section covering John D. Cook's Claude→Z3/Python chessboard constraint satisfaction experiment (192 solutions, 24 unique). Tags: concept, coding-agents, software-engineering, developer-tooling, formal-methods. Source: raw/articles/johndcook.com--blog-2026-06-20-z3-python-claude--6dbfee73.md.

- **entities/john-d-cook-applied-mathematics-consulting.md** — Added "Claude + Z3/Python Code Generation (June 2026)" subsection under LLM-Assisted Formal Proofs. Updated frontmatter updated: 2026-06-21. Added source and reference entries.

- **entities/lcamtuf.md** — Added timeline entry for Jun 2026 "The 100,000 whys of AI". Added "AI Content Slop Detection: The Quasi-Determinism Argument" subsection in Core Ideas. Added [[concepts/ai-slop]] cross-reference. Updated frontmatter updated: 2026-06-21. Added reference entry.

### Triage Summary

1 take: johndcook Z3/Python Claude article -> concepts/ai-assisted-development.md enrichment + entity page update
1 reference: lcamtuf "100,000 whys" -> entity/lcamtuf.md enrichment
13 skips: non-AI content (Windows HMODULE, construction digest, package management, systemd, glassblowing, SVG license, Postgres benchmark, kernel stable, Epstein class, 4 unsaved articles)

---

## [2026-06-21] Trending Topics — Open-Source AI Critical Perspectives Update

**Pipeline:** trending-topics report (2026-06-21)

### Actions Taken

1. **Updated concept page:** `concepts/open-source-ai.md`
   - Added "Critical Perspectives (June 2026)" section covering three topics:
     - Cory Doctorow "AI = 0" digital sovereignty critique (Pluralistic, 2026-06-18)
     - Software Freedom Conservancy LLM usage guidelines for FLOSS organizations
     - Norway's near-ban on AI in elementary schools (Reuters, HN 691pts/482 comments)
   - Updated frontmatter: `updated: 2026-06-21`, added tags `[digital-sovereignty, ai-governance, ai-ethics, education]`, added 2 new sources
   - Added wikilinks to `[[entities/microsoft]]`, `[[comparisons/ai-competition]]`, `[[concepts/ai-ethics]]`
   - Page expanded from 67 lines to ~88 lines

2. **Updated SCHEMA.md taxonomy:**
   - Added `digital-sovereignty` tag to Meta category

### Sources Ingested
- `raw/articles/pluralistic.net--2026-06-18-their-trillions-our-billions--c9dc9b31.md` — Doctorow's AI sovereignty critique
- `raw/articles/2026-06-19_hn-discussion_norway-ai-school-ban.md` — Norway AI school ban HN discussion

### Wiki Impact
- **Modified:** `concepts/open-source-ai.md` (67→88 lines)
- **Modified:** `SCHEMA.md` (added `digital-sovereignty` tag)
---

## [2026-06-21] Trending Topics — AI Industry Economics concept page created

**Pipeline:** trending-topics report (2026-06-21) → wiki concept page
**Source:** Raw articles from 2026-06-17 to 2026-06-18

### Pages Created

- **concepts/ai-industry-economics.md** — Comprehensive concept page covering the June 2026 AI industry financial reckoning. Synthesizes four major threads:
  - OpenAI's leaked audited financials ($38.5B net loss in 2025, $34B total costs, $13.07B revenue) from Ed Zitron/Where's Your Ed At, verified by Financial Times
  - Ed Zitron's "Herbalife Moment" critique: AI industry revenue as circular dependency between AI companies and VC ecosystem
  - George Hotz's "prices can't go down" structural analysis: policy-driven asset inflation (3.3× vs 220× growth gap since 1980), order-of-magnitude escalation (Theranos→FTX→frontier AI→government), zero-sum extraction argument
  - Uber's $1,500/month per-developer AI tool spending cap as enterprise cost rationalization signal ($36K/year per engineer, ~11% of median $330K comp)
  - Tags: ai-economics, economics, pricing, business-model, openai, industry, ai-criticism, ai-skepticism, token-economics, cost-optimization

### Pages Updated

- **index.md** — Added `concepts/ai-industry-economics` entry in Concepts section (line 892), adjacent to existing `ai-industry-financial-sustainability`

### Sources Referenced

- `raw/articles/wheresyoured.at--exclusive-openai-financials--55499629.md` — Full 2024/2025 financial breakdown
- `raw/articles/2026-06-17_openai-leaked-financials-ai-economics.md` — Aggregated HN discussion + Ars Technica
- `raw/articles/geohot.github.io--blog-jekyll-update-2026-06-18-prices-cant-go-down-html--356e1e6b.md` — Hotz structural critique
- `raw/articles/2026-06-03_simonwillison_uber-caps-ai-tool-costs.md` — Uber spending cap analysis

### Related Pages

- [[concepts/ai-industry-financial-sustainability]] — Earlier/simpler coverage of same OpenAI+Herbalife topic
- [[concepts/token-economics]] — Per-token cost economics
- [[concepts/ai-economics]] — Broader AI economics theory
- [[concepts/ai-lab-subscription-vs-api-economics]] — Subscription vs API economics
- [[entities/openai]], [[entities/uber]], [[entities/george-hotz]], [[entities/ed-zitron]]

---

## [2026-06-21] Data Scaling Limits — Concept page created from trending topics

**Trigger:** Trending topics report 2026-06-21

### Actions Taken

1. **New concept page created:** `concepts/data-scaling-limits.md`
   - Synthesizes three perspectives on data as the primary AI scaling bottleneck:
     - Dwarkesh Patel's "data black hole" thesis (1M× sample efficiency gap, RL as synthetic data, 4-month open-model catch-up)
     - lcamtuf's "100,000 whys" analysis of LLM output homogenization (150 Amazon slop books, deterministic behavior)
     - Alex Ellis's "Local Qwen ≠ Opus" benchmarks (RTX 6000 Pro: SWE-Bench 77.2% vs 88.6%, looping, quantization trade-offs)
   - Covers: sample efficiency black hole, data homogenization, local vs frontier gap, scaling implications
   - Tags: scaling-laws, synthetic-data, local-llm, data-science, benchmark, model-quantization, ai-slop, scaling, training, frontier-models, content-quality
   - Sources: 3 raw articles
   - Wikilinks: [[concepts/scaling-laws]], [[concepts/local-llm/local-ai]], [[concepts/local-llm/model-quantization]], [[concepts/data-filtering-scaling-laws]], [[entities/deepseek]], [[entities/dwarkesh-patel]], [[entities/epoch-ai]], [[entities/lcamtuf]], [[entities/alexellis]]

2. **Index updated:** Added `concepts/data-scaling-limits` entry in Concepts section (after `data-filtering-scaling-laws`)

---

## [2026-06-21] Wiki Watchdog Auto-Fix — log separator + 20 orphans

**Source:** cron job (wiki-watchdog-fix)
**Timestamp:** 2026-06-21 17:50 UTC

### Actions Taken

1. **Log.md separator fix:** Added missing `---` between sections 1 and 2 of log.md (first section content → second section header).

2. **Orphan pages added to index.md:** Added 20 orphan concept pages (first alphabetically) that existed on disk but were missing from the Concepts section:
   - `concepts/ai-benchmarks/lighteval`, `openbenches`, `yourbench`
   - `concepts/claude/tokenizer-47-change`
   - `concepts/context-engineering/context-anxiety`, `context-folding`, `context-management-cognition-claude-models`
   - `concepts/gpt/chatgpt-memory-bitter-lesson-extended`, `image-2-vs-nano-banana-2`
   - `concepts/local-llm/gguf`, `llama-cpp`, `local-llm-inference-hardware`, `local-llm-models-april-2026`, `local-llm-server-setup-on-dgx-spark`, `vllm`
   - `concepts/multi-agents/multi-agent`, `multi-agents-cognition-devin-orchestration`
   - `concepts/openai/index`, `whisper-asr`, `workspace-agents`

3. **Header count update:** `Indexed entries: 2221 → 2241`, `Not in index: 401 → 381`

### Outcome
- **index.md**: 2264 → 2284 lines, clean validation ✅
- **log.md**: 189 → 206 lines, all separators present ✅
- **Remaining orphans (depth ≤ 3)**: 7 more (`openclaw/ecosystem-tools`, `openclaw/five-tier-precedence`, `post-training/rlhf-dpo-orpo-kto-preference-optimization`, `post-training/rlhf-reinforcement-learning-from-human-feedback`, `red/green-tdd`, `speech/whisper`, `training/trl`)
