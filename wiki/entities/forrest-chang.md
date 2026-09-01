---
title: "Forrest Chang"
created: 2026-05-11
updated: 2026-09-01
url: https://x.com/forrestchang
type: entity
description: Co-founder of Multica and author of the viral andrej-karpathy-skills CLAUDE.md file (209K+ stars)
aliases: [forrestchang, jiayuan_jy]
tags:
  - person
  - ai-agents
  - developer-tooling
  - coding-agents
  - agent-harness
  - open-source
  - founder
related:
  - "[[concepts/claude-code/claude-md-rules]]"
  - "[[entities/andrej-karpathy]]"
  - "[[concepts/harness-engineering]]"
sources:
  - https://x.com/kaborov/podcasts/
  - https://github.com/multica-ai/andrej-karpathy-skills
  - https://multica.ai/
  - https://x.com/forrestchang
  - https://x.com/jiayuan_jy
  - raw/articles/2026-05-09_mnilax_claude-md-12-rules.md
---

# Forrest Chang

**Forrest Chang** (X: [@forrestchang](https://x.com/forrestchang)) is the author of the [`andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) repository — a single CLAUDE.md file of coding-agent behavioral guidelines derived from Andrej Karpathy's observations about how LLMs fail at code — and co-founder of **Multica**, an open-source project-management platform for mixed human + AI-agent teams. His CLAUDE.md file became one of the most-referenced artifacts in Claude Code practice, spawning a large ecosystem of forks, translations, and derivative "rules" articles.

## Background

Chang is best known for two artifacts that bookend the "agentic coding discipline" wave of early 2026:

- **andrej-karpathy-skills** (2026-01-27): after reading Karpathy's January 2026 thread on LLM coding failure modes, Chang converted the observations into 4 behavioral rules in a single CLAUDE.md file. It became one of the fastest-growing single-file repos of 2026 (209K+ stars).
- **Multica** (co-founder, with [[entities/jiayuan-zhang|Jiayuan Zhang]]): an open-source platform for managing human + agent teams, extending the same philosophy ("agents as accountable teammates, not passive tools") to the team-orchestration layer.

## The andrej-karpathy-skills Repository

Created 2026-01-27 under the `multica-ai` GitHub org, the repo distills Karpathy's viral commentary on LLM coding pitfalls into four behavioral principles for coding agents:

1. **Think before coding** — surface assumptions and tradeoffs rather than silently choosing
2. **Simplicity first** — avoid over-engineering; the LLM's default is to gold-plate
3. **Surgical changes** — touch only what the task requires; don't opportunistically refactor
4. **Goal-driven execution** — define verifiable success criteria and loop until met

The file encodes these as hard constraints with embedded self-check prompts ("Did I add anything the prompt didn't ask for?"), which is what made it effective as a CLAUDE.md drop-in rather than just advice.

**Scale of adoption** (GitHub API, 2026-09-01): **209,359 stars / 21,302 forks** — placing it among the most-starred prompt-engineering artifacts ever published. Notable derivative ecosystem:

| Fork / Variant | Stars | Notes |
|---|---|---|
| `multica-ai/andrej-karpathy-skills` (canonical) | 209K | Original CLAUDE.md |
| `vtroisWhite/andrej-karpathy-skills` | 413 | Chinese translation |
| `mbeijen/andrej-karpathy-skills-cursor-vscode` | 272 | Cursor/VS Code port |
| `duolahypercho/andrej-karpathy-skills` | 220 | Codex-first conversion |
| `LearnPrompt/andrej-karpathy-skills` | 91 | Agent Skills packaging |

The file's practical impact circulated widely via third-party articles — e.g. @Mnilax's viral X article claiming Karpathy's rules cut Claude mistake rates from 41% to 11%, extended with eight more rules — see [[raw/articles/2026-05-09_mnilax_claude-md-12-rules]] and [[concepts/claude-code/claude-md-rules]].

## Multica

**Multica** ([multica.ai](https://multica.ai/), [GitHub](https://github.com/multica-ai/multica)) is an open-source platform that treats coding agents as project teammates rather than tools. The tagline — *"Your next 10 hires won't be human"* — frames its core thesis: agents get profiles, report status, create issues, comment, and change status in a shared board alongside humans.

Key capabilities:
- **Assign to an agent like a colleague** — issue assignment, progress reporting, and delivery from agents
- **Shared context** — discussions, records, and deliverables live in one workspace visible to the whole team
- **Scheduled autonomous runs** — multiple agents collaborate on schedules without human triggering
- **Skill compounding** — capture working patterns as reusable skills every agent can inherit
- **Multi-runtime** — works with Claude Code, Codex, Gemini CLI, OpenClaw, and OpenCode

This makes Multica a practical implementation of [[concepts/harness-engineering]] at the *team orchestration* layer, versus the per-agent configuration layer that his CLAUDE.md occupies.

## Co-founder: Jiayuan Zhang

Multica was co-founded with **Jiayuan (JY) Zhang** (X: [@jiayuan_jy](https://x.com/jiayuan_jy), ~119K followers). Zhang's self-description: *"Building @MulticaAI. Ex-@devv_ai. Ex-@tiktok_us."* — i.e. previously at Devv AI (developer-focused AI search/context tooling) and TikTok US. Zhang publishes essays at [blog.jiayuanzhang.com](https://blog.jiayuanzhang.com/), including "How to Build AI Agents That Manage Other AI Agents."

*(Note: GitHub attribution across the two founders is partially entangled in the `multica-ai` org; the canonical skills repo lives under the org rather than a personal account.)*

## Notable Quotes

> "LLMs are very bad at handling ambiguity. They will make assumptions and run with them."
> — Forrest Chang, 2025-12-27 (quoted in [kaborov/podcasts](https://x.com/kaborov/podcasts/))

> "LLMs are surprisingly good at writing code to solve the problem once they understand the problem."
> — Forrest Chang, 2025-12-27 (quoted in [kaborov/podcasts](https://x.com/kaborov/podcasts/))

## Cross-References

- [[concepts/claude-code/claude-md-rules]] — the concept page analyzing his CLAUDE.md rules in depth
- [[entities/andrej-karpathy]] — the observations the skills file is derived from
- [[concepts/harness-engineering]] — Multica and the CLAUDE.md file as harness-layer artifacts

## Sources

- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — canonical repo, 209K stars (verified via GitHub API 2026-09-01)
- [Multica](https://multica.ai/) — product site and docs (scraped 2026-09-01)
- [@forrestchang](https://x.com/forrestchang) / [@jiayuan_jy](https://x.com/jiayuan_jy) — X accounts
- [kaborov/podcasts](https://x.com/kaborov/podcasts/) — quote source
- [[raw/articles/2026-05-09_mnilax_claude-md-12-rules]] — third-party article on the rules' impact

## Key Contribution

The `CLAUDE.md` file distilled Karpathy's complaints about AI coding agents into actionable, machine-readable guidelines:
1. Think Before Coding
2. Simplicity First
3. Stay in Scope
4. Goal-Driven Execution

The repo hit 5,828 stars in its first day, 60,000 bookmarks in two weeks, and 120,000+ stars by May 2026 — demonstrating that a 65-line markdown file with zero dependencies can be more impactful than many full frameworks. Released under the MIT license.

## Related

- [[concepts/claude-code/claude-md-rules]] — The CLAUDE.md behavioral guidelines
- [[entities/andrej-karpathy]] — Originator of the observations
- [[entities/claude-code]] — Claude Code
