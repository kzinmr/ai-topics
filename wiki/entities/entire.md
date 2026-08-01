---
title: Entire
type: entity
created: 2026-05-08
updated: 2026-08-01
status: L3
tags:
  - company
  - coding-agents
  - infrastructure
  - search
  - protocol
  - git
  - agent-observability
  - open-source
website: https://entire.io
github: https://github.com/entireio
sources:
  - https://entire.io
  - https://entire.io/blog
  - https://entire.io/blog/an-entirely-new-git-hosting-network
  - https://entire.io/blog/how-version-control-will-evolve-for-the-agent-boom
  - https://entire.io/about/company
  - raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents.md
aliases: [entire.io, Entire Inc, entireio]
---

# Entire — Agent Observability, Sessions & Distributed Git for the Agent Era

Entire is a developer platform company building infrastructure for AI agent observability, session capture, and distributed Git hosting. Founded by former GitHub CEO [[entities/thomas-dohmke]], it stores every agent session, prompt, and tool call alongside your commits, and operates a fast, distributed, Git-compatible mirror network so agent fleets can clone and push at scale. Valued at **$300M** by February 2026.

## Overview

Entire's thesis: as AI agents become the primary producers of code, **session logs are the most important artifact in software development** and should be stored alongside the code itself in the repository. The company productizes this in three layers:

1. **Checkpoints** — every commit gets paired with the full agent session (prompts, responses, tool calls, decisions) that produced it, stored directly in git history
2. **Entire CLI** — open-source (MIT), works with any agent (Claude Code, Codex, Gemini, Cursor, Goose) to capture and resume sessions
3. **Distributed Git Network** — regional mirrors of GitHub repos so agents clone fast without hitting origin rate limits

## Team & Funding

- **CEO**: [[entities/thomas-dohmke]] — former GitHub CEO (2021–2025), co-founder of HockeyApp (acquired by Microsoft 2014)
- **Engineering**: Evis Drenova (Principal SWE, see [[entities/evis-drenova]]), Georg Friedrich, Kai Ramuenke, Stefan Haubold, Paul van der Walt, Alex Ong, Victor Gutierrez Calderon, Peyton Montei, Pat Leamon, Robin Wohlers-Reichel, Alisha Kawaguchi, Patrick Dinger, Sven Pfleiderer, Daniel Vydra, Andrea Nodari, Matthias Wenz
- **Strategy & GTM**: Cole Driver; **Design Engineering**: Daniel Adams; **Operations**: Jordyn Myers
- **Investors**: $60M seed round at $300M valuation (per [[entities/evis-drenova]]: Felicis, Madrona, M12, plus angels incl. Datadog's CEO, YC's CEO, Jerry Yang). Company page also lists Basis Set Ventures, Cherry Ventures, Global Founders Capital, Picus Capital — possibly a separate/earlier round.
- **Founded**: early 2026 (announced after Dohmke's August 2025 departure from GitHub); $300M valuation by February 2026
- Remote-first, globally distributed team; "zero-bugs policy with SLAs"

## Core Products

| Product | Description |
|---------|-------------|
| **Entire CLI** | Open-source CLI for agent interaction ([github.com/entireio/cli](https://github.com/entireio/cli)) — MIT licensed, works with any agent |
| **Checkpoints** | Sessions, prompts, and tool calls stored in git history; every commit paired with the agent session that produced it |
| **Distributed Git Network** | Regional mirror cells (US, EU, Australia, India) that absorb agent clone/push traffic; GitHub stays the origin |
| **Git Sync** | SSH-based regional mirror that stays in sync; `entire repo mirror create` one-command setup |
| **Skills** | Package knowledge, conventions, and workflows into reusable skills so any agent picks up where you left off |
| **Marvin** | Entire's own agent, used in their changelog/dispatch workflow ("Mostly harmless, mostly revolutionary") |
| **pgr** | Open-source Rust MCP agentic search tool — definitions-first, path-aware ranking ([github.com/entireio/pgr](https://github.com/entireio/pgr)) |

## Key Capabilities

### Checkpoints: "Context that's attached, not archived"

Entire creates a checkpoint for every commit: the code change paired with the full agent session that produced it.

- **"Why did we write it this way?"** — look at any change and the reasoning is right there
- **"Where does all this context actually go?"** — nowhere new: checkpoints live in your git history. No hosted service, no external database
- **"Why does the agent keep making the same mistakes?"** — because it starts every session from zero; checkpoints give agents the full history of how the codebase was built — not just the code, but the decisions behind it
- **Private by design**: sensitive data never leaves your machine; Entire detects and redacts secrets before anything is stored
- **`entire session resume`** — move work between agents with full session state carried forward
- **Ref-based checkpoint storage** (Jul 2026): checkpoints get their own Git refs for faster, lighter pushes and reads as history grows
- **Import pre-existing sessions** (Jul 2026): bring untracked coding-agent sessions into history
- **`entire blame`** (Jun 2026): trace file lines back to checkpoints and sessions
- **Token-level code navigation** (Jul 2026): repository viewer traces symbols across files and previews Markdown
- **Goose support** (Jun 2026): capture Goose session history alongside repository history

### Distributed Git Network

Launched July 8, 2026 with the essay "An Entirely New Git Hosting Network" by Thomas Dohmke:

> "By design, Git was always meant to be decentralized... This was sustainable until agents came along, sending thousands of concurrent requests in seconds, triggering traffic caps, and exposing failure points. We believe that Git hosting must return to its original promise: a truly distributed network, not a system where the world's software lives in a single location."

- Mirror your public or private GitHub repos on Entire; repo stays on GitHub, agents fetch from a regional Entire cell
- **Entire-native branches** (`entire/unmirrored/`) stay local to the region for maximum write throughput
- **ForgeMark** — open-source (MIT) benchmark for concurrent git-push throughput and latency under agent-fleet load patterns (released with the network)
- **Architecture**: global control plane for identity/placement + regional data planes for content-addressed Git storage; compare-and-set ref updates; object writes fan out across storage nodes; writes replicated across availability zones
- **Performance** (ForgeMark measurements): 570K clones/h, 1.7M operations/h mixed workload, 2.1M pushes/h (128 agents pushing 2KB files)
- **Roadmap**: decentralize and open-source the Git network, allow self-hosting, expand regions

### Agentic Search Research (May 2026)

Entire published a landmark study on agentic code search, analyzing 1,983 real coding-agent checkpoints (~202K tool calls) from their open-source `entireio/cli` repo:

- **48.8% of all agent tool calls are search-related**
- **Faster search (fff: 14.7ms → 1.7ms) only modestly improves end-to-end (38.57s → 36.99s)**
- **Better ranking (pgr) improves first-query Hit@1 from 26% → 34% (implementation tasks: 14.3% → 42.9%)**
- **Tool execution is only ~0.4% of total agent wall clock** — the bottleneck is model inference + planning, not search speed

This research is one of the first public, data-driven analyses of how coding agents spend their time and what actually improves their effectiveness.

## "The Soul of Software" Thesis

Dohmke's framing (July 2026): Git captures what was written; agent sessions reveal **why**. Session logs are the semantic memory layer:

- Agents stop repeating mistakes → higher accuracy, increased productivity, decreased token spend
- Humans understand and verify what was built and why → provenance layer → faster reviews
- Groups of humans and fleets of agents collaborate in parallel without overwriting, colliding, or losing understanding

## Company Culture

Entire operates as a globally distributed, remote-first team:

- Small squads (2-4 people) around time-boxed epics; engineers or designers lead
- No OKRs or A/B tests; align on a north star and use judgment
- Short specs, high tempo, feature flags to internal users first
- **Zero-bugs policy with SLAs**; weekly bug dashboard; "If we fuck it up, it's on us"
- "Constraints create clarity" — say no to keep the bar high
- On-call rotations that follow the sun

## People

- **Thomas Dohmke** — CEO; see [[entities/thomas-dohmke]]
- **Evis Drenova** — Principal Software Engineer; see [[entities/evis-drenova]]

## See Also

- [[concepts/pgr]] — The agentic search tool built by Entire
- [[entities/thomas-dohmke]] — CEO and founder (ex-GitHub CEO)
- [[entities/evis-drenova]] — Principal engineer, author of the agentic search study
- `fff` — Fast indexed MCP search server by Dmitry Kovalenko
- `ripgrep` — Baseline grep tool
- GitHub — Origin platform for mirrored repositories (no entity page yet)

## Sources

- [entire.io](https://entire.io) — Homepage, scraped 2026-08-01
- [An Entirely New Git Hosting Network](https://entire.io/blog/an-entirely-new-git-hosting-network) — Jul 8, 2026, Thomas Dohmke
- [How Version Control Will Evolve for the Agent Boom](https://entire.io/blog/how-version-control-will-evolve-for-the-agent-boom) — Jul 6, 2026, Thomas Dohmke
- [Company page](https://entire.io/about/company) — Team, values, investors
- [Blog index](https://entire.io/blog) — Dispatch changelog series
- raw/articles/2026-05-06_entire-improving-agentic-search-in-coding-agents.md
