---
title: "Wiki Activity Log"
tags: [uncategorized]
created: 2026-04-24
updated: 2026-04-24
---

# Wiki Activity Log

## [2026-04-26] agent-swarms | New concept page created
- [laterals] agent-team-swarm → [[agent-swarms]]
  - **Key distinction**: agent-team-swarmは分散システム管理視点（階層的オーケストレーション）、agent-swarmsは自律的創発振る舞い視点（生物学的スワームからインスパイア）
  - Biology-inspired swarm intelligence: Boid algorithms, ant colony optimization, stigmergy
  - Emergent behavior measurement: MAEBE framework, temporal synergy, goal-directed complementarity
  - LLM swarm experiments: OpenAI Swarm (educational), Emergent Coordination paper (GPT-4.1 + Llama)
  - Implementation patterns: Stigmergic communication, market-based allocation, gradient following
  - New page: concepts/agent-swarms.md (status: skeleton)
  - Updated: wiki/index.md (Concept Pages 93→94)
  - Added hot-topics.yaml entry: agent-swarms (priority: medium, crawl_policy: laterals)

## [2026-04-25] active-crawl | 2 new concepts ingested (harness-engineering deepdive + agentic-engineering prerequisites)
- [prerequisites] harness-engineering → [[agent-harness-primitives]]
  - Source: LangChain blog (Vivek Trivedy), Medium article (Steven Cen)
  - 6 core primitives: filesystem, code execution, tools, orchestration, feedback, recovery
  - Added raw/articles/2026-04-25-langchain-anatomy-agent-harness.md, 2026-04-25-harness-engineering-era-3.md
- [deepdive] ai-agent-engineering → [[agentic-design-patterns]]
  - Source: arXiv:2601.19752 (Dao et al., Jan 2026)
  - 12 design patterns mapped to 5 subsystems (RWM, PG, AE, IAC, LA)
  - Added raw/articles/2026-04-25-agentic-design-patterns-arxiv.md

## [2026-04-25] dreaming | consolidation — 2 new pages, 8 updates

### New Entity Pages
- [[claude-design]] — Claude Design (Anthropic Labs product, visual design tool powered by Opus 4.7, design-to-code handoff to Claude Code)
- [[anthropic-labs]] — Anthropic Labs (experimental product division, first product: Claude Design)

### Updated Entity Pages
- [[anthropic]] — Added Claude Opus 4.7 highlights and "Big Swing" April 2026 strategy analysis
- [[claude-code]] — Added Claude Design handoff pipeline integration (design-to-code workflow)
- [[google]] — Added Gemini macOS App, Gemini 3.1 Flash TTS, Google AI Plans with Cloud Storage
- [[gpjt]] — Added LLM from Scratch Part 32l (Interventions: instruction fine-tuning results)

### Updated Concept Pages
- [[chatgpt-images-2.0]] — Added reasoning capabilities section (first image model with reasoning, layout planning, multi-image coherence, advanced text rendering)
- [[claude-code-routines]] — Added Opus 4.7 integration (xhigh effort, self-verification, task budgets) and Claude Design handoff
- [[gemini]] — Added Gemini macOS App, Gemini 3.1 Flash TTS, Google AI Plans with Cloud Storage
- [[arc-agi-2]] — Added Epoch AI Benchmarking Hub and WeirdML v2 updates
- [[ai-criticism-politics]] — Added Sean Goedecke conservative alignment analysis

### Navigation
- index.md: entity count 88 → 90, updated last-updated line

## [2026-04-26] active-crawl | 3 new concepts, 1 updated page (agent-governance, multi-agent-orchestration-architecture, differential-symbolic-modules, formal-logic-foundation, death-of-browser update)
- [laterals] agentic-engineering → [[agent-governance]]
  - Source: CIO (Viral Gandhi, Mar 26 2026) + Zenity (Cinthia Portugal, Mar 12 2026)
  - Platform-independent governance: identity/access, runtime guardrails, policy enforcement at runtime
  - Added raw/articles/crawl-2026-04-26-agent-governance.md
- [laterals] agentic-engineering → [[multi-agent-orchestration-architecture]]
  - Source: CIO (Viral Gandhi, Mar 26 2026) — multi-agent orchestration as Phase 2 of AI development
  - Specialized agent roles (Architect, Coder, Test, Security, DevOps, Documentation)
  - Parallelized cognition, Stripe metric: 1,000+ PRs/week from AI agents
  - Added raw/articles/crawl-2026-04-26-agent-governance.md (shared source)
- [deepdive] death-of-browser → updated [[death-of-browser]] page
  - Source: TechLatest.Net (Apr 2026) — Complete AI Browser Selection Guide 2026
  - Added 2026 tool sections: Browser Use BU-2.0, Perplexity Comet, ChatGPT Atlas
  - Added timeline entries for Jan–Apr 2026 tools
  - Fixed frontmatter to SCHEMA.md compliance
- [prerequisites] neurosymbolic-ai → [[differential-symbolic-modules]]
  - Source: arXiv:2508.13678 (Brinzeu et al., Sep 2025) — NeSy Taxonomy paper
  - Differentiable symbolic operations (t-norms, s-norms, fuzzy implication)
  - Logic Tensor Networks, differentiable unification
  - Added raw/articles/crawl-2026-04-26-neurosymbolic-taxonomy.md
- [prerequisites] neurosymbolic-ai → [[formal-logic-foundation]]
  - Source: arXiv:2508.13678 — formal logic systems underlying NeSy reasoning
  - Three reasoning modes: deductive, inductive, abductive
  - Propositional, first-order, fuzzy logic systems
  - Added raw/articles/crawl-2026-04-26-neurosymbolic-taxonomy.md (shared source)
- Updated [[neurosymbolic-ai]] — added NeSy taxonomy section, Dual Process Theory mapping, links to new prerequisite pages
- Updated [[death-of-browser]] — 2026 tools section, fixed frontmatter
- index.md: updated last-updated line, added 4 new entries, updated death-of-browser summary

## [2026-04-26] create | Agent Swarms concept page + hot-topics entry
- Created concept page: `concepts/agent-swarms.md` — Decentralized multi-agent systems with emergent collective behavior
- Added to hot-topics.yaml: `agent-swarms` topic (medium priority, laterals crawl policy)
- Updated index.md: Added [[agent-swarms]] under Agent Team/Swarm section
- Sources: 4 articles (Riedl arXiv:2510.05174, OpenAI Swarm framework, Metal Toad, Medium)
- Key distinction from [[agent-team-swarm]]: focuses on emergent behavior and decentralized control vs. hierarchical orchestration

