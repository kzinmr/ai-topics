---
title: "X Accounts Scan — 2026-09-09"
date: 2026-09-09
source: "x-accounts-scan cron job"
type: x-scan-report
---

# X Accounts Scan — 2026-09-09

Scan run at 2026-09-09T22:30:32Z. 11 accounts scanned out of 84 tracked (rotating budget of 12). 4 substantive new posts; 0 errors.

## Posts & Links

### Simon Willison — OpenAI Navier–Stokes Millennium Prize Problem
- Tweet: https://x.com/simonw/status/2097474703380365698
- Article: https://simonwillison.net/2026/Sep/8/on-navier-stokes/
- Raw: raw/articles/simonwillison-net--2026-Sep-8-on-navier-stokes--80062e04.md
- Wiki: entities/openai-astra.md (new "Navier–Stokes Verification & the Scooping Controversy" section), entities/simon-willison.md, concepts/mathematical-proof-verification.md

OpenAI used an unreleased reasoning model (GPT-5.3/Codex line) plus an expert-built Lean 4 formalization to prove the existence and smoothness of 3D Navier–Stokes — a Millennium Prize Problem, with a companion 2D non-uniqueness result. Simon's technical skepticism: "AI proved Navier-Stokes" is a category error (what's proven is a precise formalization, the formalization is the work, the proof has been machine-checked). Two independent verifications (Kevin Buzzard's mathlib-based, Sean Willekes's standalone Lean project). Separately, Simon treats the OpenAI/Claude Code source-leak story ("scoop, or independent development?", Lenny Rachitsky, Hacker News thread) as a live data-processing-rights test of the "to improve model performance" clause in ToS.

### Simon Willison — CaMeL quote-tweet on layered prompt-injection defense
- Tweet: https://x.com/simonw/status/2097475247595536880
- Article: https://simonwillison.net/2025/Apr/11/camel/
- Wiki: concepts/prompt-injection.md (new "Layered Product Defense: Muse" section, cross-linked to CaMeL)

Quote-tweeting the Muse launch thread ("deterministic code checks the result" sounds like a CaMeL variant). CaMeL (DeepMind, Dec 2024): controls data flow so untrusted content can influence values but never instructions; dual LLM (control-flow from trusted query only, capacity from tools); Croissant proof-carrying provenance tags. Not deployable today (no LLM-capable prover, no control-flow interpreter, single-agent only, ~10x cost).

### Florian Brand — scaffold elicitation is correct methodology
- Tweet: https://x.com/xeophon/status/2097802629581582806
- Article: https://epoch.ai/gradient-updates/why-benchmarking-is-hard
- Raw: raw/articles/epoch-ai--gradient-updates-why-benchmarking-is-hard--40577117.md
- Wiki: entities/florian-brand.md (new "Benchmark Criticism and Elicitation" section), concepts/evaluation/agent-evaluation-methodology.md (new "Scaffold Elicitation" subsection), concepts/harness-engineering.md (cross-link)

Reply to an Epoch AI Gradient Updates discussion: "models are trained and used in their harnesses and if you want to report raw capabilities, pushing them as hard as possible is the thing you should do." Epoch's piece: scaffolds and API providers are the two most impactful benchmark components; scaffolding is now so powerful it is a method to elicit better performance; no scaffold standardisation, so leaderboard scores reflect scaffold + model + provider simultaneously.

### Ryan Lopopolo — Agent Platforms for Inventing Agents
- Tweet: https://x.com/_lopopolo/status/2097359306060702009
- Article: https://hyperbo.la/w/agent-platform/
- Raw: raw/articles/hyperbo-la--w-agent-platform--a447d51a.md
- Wiki: entities/ryan-lopopolo--writings.md (new entry), concepts/agent-platform.md (cross-link), concepts/harness-engineering.md (cross-link)

An agent is a parameterized program over a set of capabilities: "We recognize the capabilities, but we do not know their best concrete implementations." Therefore an agent platform's job is to let builders discover what works without waiting on someone else's config knobs and roadmap. Three rules: one shared substrate, no roadmap, permission to delete. Cites the harness-engineering lineage — Codex's shell/apply-patch/JSON-RPC/compaction choices were "accidents of context and time."
