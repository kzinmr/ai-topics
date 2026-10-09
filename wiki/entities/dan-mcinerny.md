---
title: Dan McInerney
created: 2026-06-14
updated: 2026-10-09
type: entity
tags:
  - person
  - developer-tooling
  - coding-agents
  - open-source
  - harness-engineering
  - architecture
  - security
aliases:
  - DanMcInerney
  - "@DanHMcInerney"
sources:
  - raw/articles/2026-06-14_danmcinerny_architect-loop-fable-codex.md
  - https://github.com/DanMcInerney/architect-loop
  - https://github.com/DanMcInerney/orchflows
  - https://mcinerney.ai/
  - https://github.com/DanMcInerney
---

## Overview

**Dan McInerney** is an "agent builder and security engineer" (his GitHub bio) — unusual for an AI-agent tool author in that he arrived from offensive security research, not ML. His GitHub account dates to 2012 and its most-starred projects are classic Kali Linux pentesting tools; since ~2025 he has pivoted almost entirely to AI agent harness engineering, applying the same adversarial mindset ("assume the agent will game your tests") to coding-agent orchestration. He maintains 105+ public repos, ~3,000 GitHub followers, and blogs at [mcinerney.ai](https://mcinerney.ai/) ("Hacking, AI, Agents, and Statistics").

He is best known as the creator of [[concepts/architect-loop|Architect Loop]] (June 2026) and **Orchflows** (July 2026), both MIT-licensed Claude Code / Codex skill systems.

## Career Arc: Offensive Security → Agent Harnesses

### Phase 1 — WiFi/AD pentesting tools (2012–~2022)

Author of several canonical offensive-security tools still widely used in Kali:

| Repo | Stars | What it does |
|---|---|---|
| **wifijammer** | 4,300+ | Continuously deauths all WiFi clients/routers |
| **LANs.py** | 2,600+ | Injects code and spies on WiFi users |
| **net-creds** | 1,800+ | Sniffs sensitive credentials from interfaces/pcaps |
| **xsscrapy** | 1,700+ | XSS spider/crawler |
| **icebreaker** | 1,100+ | Harvests plaintext Active Directory credentials |

### Phase 2 — Sports prediction modeling (2022–present)

Five years building an open-source **UFC/MMA prediction model** (mma-ai.net; `mma-ai`, `UfcstatsScraper` repos) — ensemble modeling, feature pruning, calibration, drift handling. He open-sourced the model weights and database (June 2026), documenting hard lessons about leakage and validation. Also built a Kalshi mention-market bot that made ~$6k while he slept (blog post, May 2026), and runs **Clankerfights** (May 2026) — multiplayer games played by LLM agents with prompt-injection wagering.

### Phase 3 — Agent harness engineering (2025–present)

His stated epiphany (X, ~late 2025): after building agents on Google ADK and playing with Cursor, he concluded "claude code isn't a coding agent" — it's an orchestration substrate. This reframing drives everything below.

## Key Work

### Architect Loop (June 2026)

A cross-vendor agent loop pattern that pairs [[concepts/claude/fable-5|Claude Fable 5]] as architect/planner/judge with [[entities/codex|OpenAI Codex]] (GPT-5.5) as builder, implemented as MIT-licensed Claude Code skills (626★, 53 forks as of Oct 2026). Started from a post by [@jumperz on X](https://x.com/jumperz/status/2065454404623384859) about running Fable with Codex subagents; McInerney built it because no easy implementation existed.

Core mechanics (full detail on [[concepts/architect-loop]]): specs and frozen acceptance gates committed *before* builders start; parallel `codex exec` builders isolated in git worktrees that must argue with the spec; Fable re-runs gate commands itself ("builder claims are hearsay") and reads diffs in a fresh session; the repo (`docs/HANDOFF.md`, `docs/gates/`, git history) is the only memory. Reduces token cost 58–74% by spending the expensive model on "judgment minutes" and the flat-rate model on "typing hours" — running on consumer subscriptions, no API keys. The system is deliberately source-backed: DESIGN.md documents twelve enforced rules with citations to Anthropic engineering posts, Fable/Codex docs, and community harness skills — targeting the failure modes of context rot, self-grading, and goalpost drift.

### Orchflows (July 2026)

`DanMcInerney/orchflows` (117★, actively developed) — a composable **skill-workflow library**: two skills (`orch-build-workflow`, `orch-dynamic-workflow`) that let Codex or Claude Code route requests into "right-sized, self-improving, externally verified workflows." Build rehearses a new workflow with sample input and independently reviews it; Dynamic assembles a one-off process for the current task. His pitch on X: "You only need 2 skills: work and review" — specificity should be abstracted out of skills into modular guidance docs. He positions it directly against paid agent-orchestration products ("Free, open source, runs on the Claude Code or Codex you already have").

### Gauntlet Loop & community work

Contributed the "gauntlet loop" as a reusable workflow (per X replies to @mattshumer_), and converts other authors' skills (e.g. Matt Pocock's `/diagnosing-bugs`) into composable orchflows workflows. Evaluated agent skills against benchmarks like SWE-bench Pro and Terminal-Bench before adopting them (e.g., testing compound-engineering skills) — a recurring theme of benchmark-driven, not vibes-driven, harness choices.

### Agent swarms research review (September 2026)

"Agent Swarms: What The Research Actually Says" (mcinerney.ai, Sep 22, 2026) — a plain-English synthesis of months of papers, lab reports, and X threads on agent swarms/teams, skeptical of swarm hype.

## Method & Voice

- **Adversarial verification as design principle**: frozen external gates beat trusting the agent; agents game visible tests; passing tests ≠ mergeable work; "NOT FOUND beats inference" in research fan-out. Direct descendants of his pentesting background.
- **Cost-engineering discipline**: explicit budgets, search caps, saturation stops, token multipliers ("research-grade fan-out costs ~15× chat-level tokens").
- **Open-source by default**, MIT license, consumer-subscription economics rather than API billing.

## Cross-References

- [[concepts/architect-loop]] — the cross-vendor agent pattern he created
- [[entities/codex]] — builder tool in Architect Loop
- [[concepts/claude/fable-5]] — architect model in Architect Loop
- [[entities/simon-willison]] — the harness-engineering community his DESIGN.md cites
- [[concepts/compound-engineering-every]] — Every's plugin he benchmarked before adopting
- [[concepts/harness-engineering]] — the umbrella his work sits under

## Sources

- [GitHub profile](https://github.com/DanMcInerney) — bio, repo inventory, follower count (verified 2026-10-09)
- [mcinerney.ai](https://mcinerney.ai/) — blog index (verified 2026-10-09)
- [architect-loop README + DESIGN.md](https://github.com/DanMcInerney/architect-loop) — also [[raw/articles/2026-06-14_danmcinerny_architect-loop-fable-codex]]
- [orchflows](https://github.com/DanMcInerney/orchflows)
- X: [@DanHMcInerney](https://x.com/DanHMcInerney) (user ID 146279340; recent timeline scanned 2026-10-09)
