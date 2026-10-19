---
title: "Active Crawl Research Note — 2026-10-19"
type: research-note
date: 2026-10-19
sources:
  - url: https://machinelearning.apple.com/research/mlx-distributed-inference
    title: "Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio"
    org: Apple Machine Learning Research
    date: 2026-10-16
  - url: https://starskirmish.com/bench/v0-2/
    title: "StarSkirmish Bench v0.2"
    author: Kai McPheeters
    date: 2026-10-15
  - url: https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web
    title: "Websites are closing their doors to AI agents"
    author: Emma Roth
    org: The Verge
    date: 2026-10-18
  - url: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model
    title: "Anthropic's proposed AI safety bill only kicks in if 50 deaths or $1B in damages"
    org: Tom's Hardware
    date: 2026-10-18
    note: "HN 164p; paywall blocked; article context from HN discussion"
tags: [active-crawl, research]
---

# Active Crawl Research Note — 2026-10-19

## Topic 1: Apple MLX 2.0 — Muse Spark Open on Mac Studio + RDMA Distributed Inference

**Source**: Apple ML Research blog, Oct 16 2026 (HN 365p)
**Gap**: FULL. `concepts/mlx.md` exists (59 lines) but does NOT cover Muse Spark Open, RDMA, or distributed inference. `entities/muse-spark.md` covers the model but not the MLX deployment story.

**Key facts**:
- MLX (new version released Oct 16) runs Muse Spark Open (816B MoE, NVFP4 precision) at 36+ tok/s on a cluster of 4x Mac Studio M5 Ultra
- Single Mac Studio M5 Ultra: up to 512GB unified memory; 1.2 TB/s memory bandwidth (vs 819 GB/s M3 Ultra); GPU Neural Accelerators give 4.6x TTFT speedup over M3 Ultra for matrix-heavy ops
- RDMA over Thunderbolt driver enables tensor/pipeline parallel across multiple Macs — a first for consumer desktop clusters
- Benchmarks: Qwen 3.8 27B and Mistral Medium 3.5 128B fit on single Mac Studio; Muse Spark Open requires 2-4 nodes
- Models evaluated: Muse Spark Open (816B MoE, NVFP4), Mistral Medium 3.5 (128B dense, FP8), Qwen 3.8 (27B dense, BF16)
- Three parallelization schemes: pipeline-2 (2 Mac Studio), tensor-2, tensor-4
- Key claim: agentic coding workloads need large contexts → Mac Studio M5 Ultra is "desktop of choice for very large contexts"

## Topic 2: StarSkirmish Bench v0.2 — LLM Agents in StarCraft: Brood War

**Source**: starskirmish.com, Oct 15 2026 (HN 249p). Show HN format by Kai McPheeters.
**Gap**: FULL. No StarCraft/real-time-game benchmark coverage in wiki (0 hits on starcraft/sc2/smac/game-benchmark in concepts/).

**Key facts**:
- Benchmark: each LLM gets 1 hour to write a Protoss bot in C++ (BWAPI 4.4.0, OpenBW), then evaluates against human-written bots + other LLM bots
- Tests long-horizon reasoning + agentic coding: LLMs must incorporate learnings from practice games to improve their bot
- v0.2 leaderboard (win rate 0-100 against human bot roster, 5 runs avg):
  1. GPT-6 Astra (top score, step ahead)
  2. GPT-6.1 Sol (best cost/value — 1/10th GPT-6 Astra cost)
  3. Gemini 4 Argon (tied ~37-39, high variance ±18)
  4. Claude Opus 5.5 (tied ~37-39)
  5. Claude Fable 5.1 (tied ~37-39, outlier: scores 37 practicing only vs weak bots)
  6. (others incl Muse Wonder Full 7th, GPT-6 Luna, Claude Haiku 5.5)
- No sign of saturation: best model wins only 7% against top human bots (Stardust, PurpleWave, BananaBrain)
- Key insight: strongest predictor of score = how much model practiced against 7 strongest roster bots during the hour
- Maps: Heartbreak Ridge, Benzene, Destination (3 PvT maps, 60-min cap, BASIL ladder rules)
- Gemini 4 Argon runs at "high" reasoning effort; all others at "max"
- Models run in 1st-party CLI harnesses (Codex, Claude Code, etc.)

## Topic 3: Websites Blocking AI Agents — Access Crisis

**Source**: The Verge, Emma Roth, Oct 18 2026 (HN 144p)
**Gap**: FULL. `concepts/death-of-browser.md` covers the agentic browsing thesis but NOT the blocking/access-restriction counter-movement.

**Key facts**:
- Yelp: only allows AI agents via paid data licensing program
- Delta Air Lines: prevents AI agents from booking tickets
- JPMorgan Chase + Charles Schwab: blocking AI agents from accessing accounts (security concerns)
- Amazon: fighting Meta Muse, xAI Grok, OpenAI Dots (renewed after Perplexity Comet suit; appeals court overturned initial ban in Aug 2026; Amazon filed amended complaint)
- Quiet blocks: Cars.com, Amtrak stopped working for agents without announcement
- Meta strategy: partner with Walmart, Gap, Sephora, Best Buy instead of fighting Amazon
- Shopify: opened storefront network to AI agents
- Cloudflare: 1-click AI crawler block (2025) → now blocking dual-purpose crawlers (search + training)
- Anti-bot systems (not agent-specific) catching agents as false positives
- Chris Canal (EquiStamp CEO): "fewer useful things the agents can do" if companies actively block
- Meta statement: "Turning away a personal agent means turning away the customer behind it"
- xAI/Elon Musk response to Amazon block: "maybe I should start a competitor to Amazon"
- Structural issue: ad-revenue web can't tolerate agents (no eyeballs → no ad impressions)

## Topic 4 (deferred): Anthropic AI Safety Bill — Commerce Dept Gate

**Source**: Tom's Hardware (paywall blocked), HN 164p, Oct 18 2026
**Gap**: PARTIAL. `concepts/ai-regulation-2026.md` covers state/federal landscape broadly; `concepts/ai-safety/` may need enrichment.

**Key facts** (from HN discussion, article paywalled):
- Anthropic proposed federal AI safety bill; effective trigger threshold: 50 deaths OR $1B in damages
- Would make Commerce Department the sole agency capable of stopping/shutting down an AI model
- Critics note: $1B bar trivially cleared by single crypto hack; Anthropic had refused Mythos access to crypto defenders
- Comment: next step would be requiring Certified Safe AI models to carry $1B insurance → only big labs can serve government/enterprise
- Related: Lawfare article on pooled mutualized AI insurance fund proposal
- Note: article body paywalled (Tom's Hardware); using HN discussion context; marked `status: hn-context`

**Decision**: Deferred. Paywall prevented full extraction; existing `concepts/ai-regulation-2026.md` is a reasonable home for this enrichment. The full HN comments are preserved in the raw note.

## Topics Considered but Deferred

- **Context Engineering book (Alex Mikhalev, published Oct 19)**: Low engagement (0 bookmarks, 1 reply). Single source, unverified quality. Track for future crawl.
- **Sphinx (HN 246p)**: Interesting dev tool (git hook that quizzes you on AI-written code), but very new, thin product page, likely vaporware/pre-launch. Defer.
- **Tmux + Claude Code (crystl.dev)**: 39p, dev tips post. Too tactical/operational for a concept page. Could enrich an existing coding-agents page in a future session.
