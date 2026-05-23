---
title: Warp Terminal
created: 2026-05-01
updated: 2026-05-23
type: entity
tags: [product, tool, coding-agents, open-source, platform]
sources:
  - https://www.warp.dev/blog/warp-is-now-open-source
  - https://open.substack.com/pub/bensbites/p/building-gets-easier
  - raw/articles/2026-05-20_warp_multi-harness-cloud-agent-orchestration.md
  - raw/articles/2026-05-23_warp_bring-your-own-inference-to-warp.md
---

# Warp Terminal

**Warp** is an AI-native terminal and **Agentic Development Environment (ADE)** used by nearly a million developers. Built in Rust, it combines a modern terminal UX with integrated AI agents. In April 2026, Warp open-sourced its client under AGPLv3 with OpenAI as the founding sponsor.

## Key Facts

| Field | Detail |
|-------|--------|
| **Tech Blog** | [warp.dev/blog](https://www.warp.dev/blog) |
| **Founded** | 2020 (New York, NY) |
| **CEO & Co-Founder** | Zach Lloyd (former Principal Engineer at Google, Google Sheets/Docs) |
| **Total Raised** | ~$73M across 3 rounds |
| **Funding Rounds** | Seed: $6M (2020) • Series A: $17M (Apr 2022, led by Dylan Field) • Series B: $50M (Jun 2023, led by Sequoia) |
| **Notable Investors** | Sequoia, GV, BoxGroup, Neo, Sam Altman, Jeff Weiner, Marc Benioff, Elad Gil |
| **Estimated Valuation** | $200–300M (Dealroom) |
| **Employees** | ~44 (2026) |
| **License** | AGPLv3 (core), MIT (UI framework) — open-sourced April 2026 |
| **Founding Sponsor** | [[entities/openai]] |

### Paraform Context

Warp operates in the hypercompetitive developer tools space, vying for senior engineering talent in New York and San Francisco against well-funded peers. The company's lean team (~44 employees serving nearly 1M developers) reflects an engineering-heavy headcount typical of companies recruiting through platforms like [[entities/paraform]]. Warp's open-source pivot and "agent-first" contribution model also create demand for niche roles — DevRel, Rust systems engineers, and AI/agent infrastructure engineers — which are the kind of hard-to-fill positions that Paraform's recruiter marketplace specializes in. With OpenAI as founding sponsor, Warp also competes for talent against [[entities/openai]], [[entities/cursor-3]], and [[entities/anthropic]].

## Products

### Warp Terminal

The core terminal client with:
- **Terminal and Agent modes**: Switch between clean command-line and dedicated agent conversation view
- **Modern UX**: Block-based navigation, multi-line editing, syntax highlighting, rich completions
- **Code editor**: File tree, LSP support, interactive code review
- **Third-party CLI agents**: Run Claude Code, Codex, OpenCode with Warp's agent toolbelt

### Oz

**Oz** is Warp's cloud agent orchestration platform, powering the agent-first contribution model for the open-source repository. It provides:
- Skills and verification loops baked in for Warp development
- Multi-agent orchestration for code review, testing, and deployment
- Rules and context management for consistent agent behavior


### Oz Upgrade (May 2026)

On May 19, 2026, Warp launched major upgrades to Oz, making it the first truly **multi-harness control plane** for cloud agents. Key capabilities:

| Feature | Description |
|---------|-------------|
| **Multi-harness orchestration** | Launch, track, and control Claude Code, Codex, and Warp Agent in a single unified control plane. Oz sits a level above, enabling cross-harness comparison and task-to-harness matching. |
| **Automatic multi-agent orchestration** | Deploy and track multiple parallel subagents (across harnesses) for long-horizon tasks: large feature builds, code migrations, production deployments. Includes auto-tracking and progress dashboard. |
| **Cross-harness Agent Memory** | An index over organizational knowledge that Oz pulls into context for any agent task. Supports pluggable data sources (files/skills, MCPs, databases, enterprise apps) and is writable — Oz auto-adds to knowledge as it completes tasks. Agents learn team coding style, deployment topology, data structure across sessions and harnesses. In research preview. |
| **Kubernetes self-hosting** | Run agents in Kubernetes pods or via direct execution, with or without Docker. No development setup changes required. |
| **Granular cost controls** | Per-team billing, individual credit caps, visibility into team usage and outcomes. |
| **Least-privilege permissions** | Individual agents get granular permissions to internal services — production agents have different access than CRM agents. |
| **API/SDK-first** | Extended API with return values from agent sessions (artifacts, raw conversations); session handoff across local/remote/cloud environments. |

This positions Oz as a **harness-agnostic orchestration layer** — the company's philosophy is that teams shouldn't bet their future on a single model or harness.
## Open Source (April 2026)

On April 28, 2026, Warp open-sourced its client at [github.com/warpdotdev/warp](https://github.com/warpdotdev/warp):

- **License**: AGPLv3 for core, MIT for UI framework (warpui_core, warpui crates)
- **Founding sponsor**: OpenAI
- **Agent workflows**: Powered by GPT models (GPT-5.5)
- **Contribution model**: Agent-first — agents handle implementation; humans focus on speccing, direction, and verification

> "Open source has long been central to how developers learn, build, and push the field forward. We're excited to support experiments that explore how AI can help maintainers and contributors collaborate more effectively at scale." — Thibault Sottiaux, Engineering Lead, OpenAI

## Agent-First Contribution Model

Warp's open-source process inverts traditional contribution:
- GitHub issues are the source of truth for feature tracking
- Oz agents handle implementation (coding, planning, testing)
- Human contributors focus on ideas, direction, and verifying agent output
- Public roadmap and technical discussions happen in the open

This model exemplifies the [[concepts/agentic-engineering]] thesis: humans provide taste and direction, agents handle implementation.

## Strategic Context

Warp's open-sourcing is framed as "how software will be built in the future" — humans managing agents at scale to build production-grade software. The founding sponsorship by OpenAI signals alignment with GPT models as the underlying agent runtime.

Warp is competing in the **agentic development environment** space alongside:
- [[entities/cursor-3]] — IDE-native agent platform
- [[entities/openai-codex]] — OpenAI's coding agent platform
- [[entities/claude-code]] — Anthropic's CLI coding agent

## Relationships

- [[entities/openai]] — Founding sponsor; GPT-5.5 powers agent workflows
- [[entities/cursor-3]] — Competitor in agentic development environments
- [[entities/anthropic]] — Competitor via Claude Code; shares talent pool
- [[entities/google]] — Zach Lloyd's former employer (Google Sheets/Docs)
- [[entities/paraform]] — Recruiting platform context; Warp competes for niche developer-tool talent
- [[entities/ghostty]] — Mitchell Hashimoto's terminal; Ghostty left GitHub as Warp went open-source
- [[concepts/agentic-engineering]] — Embodies the agent-first workflow pattern
- [[concepts/harness-engineering]] — Oz provides the orchestration harness

## Sources

- [Warp: Warp is now open-source](https://www.warp.dev/blog/warp-is-now-open-source)
- [Warp Documentation](https://docs.warp.dev/)
- [Ben's Bites: Building gets easier (Apr 30, 2026)](https://open.substack.com/pub/bensbites/p/building-gets-easier)
- [PitchBook: Warp Company Profile](https://pitchbook.com/profiles/company/455184-10)
- [Tracxn: Warp Company Profile](https://tracxn.com/d/companies/warp/)
- [Dealroom: Warp Company Profile](https://app.dealroom.co/companies/warp_1_2)
