---
title: "Lance Martin (@rlancemartin)"
created: 2026-05-23
updated: 2026-07-06
type: entity
tags:
  - person
  - anthropic
  - claude-code
  - ai-agents
  - agent-runtime
  - sandbox
  - developer-experience
  - developer-tooling
sources:
  - raw/articles/2026-05-19_cloudflare_claude-managed-agents.md
  - raw/articles/2026-05-19_modal_claude-managed-agents-sandboxes.md
  - raw/articles/2026-05-19_vercel_claude-managed-agents-sandbox.md
  - raw/articles/2026-05-19_daytona_claude-managed-agents.md
  - raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md
  - https://github.com/anthropics/skills/tree/main/skills/claude-api
  - https://github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
---

# Lance Martin (@rlancemartin)

**Lance Martin** is a Developer Relations and Developer Experience engineer at [[entities/anthropic|Anthropic]], where he works at the intersection of Claude Code, Claude Managed Agents, and Anthropic's agent platform. He is the public-facing technical voice for Anthropic's self-hosted sandbox initiative, authoring integration guides, cookbook examples, and X threads that bridge product engineering with the developer community. He also maintains the broader `claude-api` skill in Anthropic's official skills repository.

## Overview

Lance Martin holds a unique dual role at Anthropic: he serves as both an **Applied AI researcher** (Member of Technical Staff, authoring foundational work on context engineering and agent design patterns) and a **developer experience engineer** responsible for making Anthropic's agent platform accessible to external developers. His X account (@rlancemartin) functions as an informal developer relations channel, where he announces SDK updates, shares architecture decisions behind Claude Managed Agents, and demonstrates self-hosted sandbox patterns.

His most visible work in May 2026 centers on the launch of **Claude Managed Agents self-hosted sandboxes** — a platform that lets developers run the Claude agent loop on Anthropic's infrastructure while executing code in sandboxes on Cloudflare, Modal, Vercel, or Daytona. Martin authored the `claude-api` skill that provides SDK patterns and orchestration examples for this architecture.

## Core Ideas

### "Decouple the Brain from the Hands"

Martin has been the primary evangelist for Anthropic's core architectural insight behind Claude Managed Agents: **separating the agent reasoning loop** ("brain," running on Anthropic's side) from **code execution and tool calls** ("hands," running in developer-controlled sandboxes). This pattern gives enterprise teams the security, observability, and customization they need while preserving Anthropic's performance-optimized agent harness (prompt caching, compaction, session management).

### Self-Hosted Sandboxes as the Default Pattern

His May 19, 2026 X thread announced updates to the `claude-api` skill for self-hosted sandboxes, positioning them as the **recommended production deployment model** for Claude Managed Agents. Martin argued that self-hosted environments provide:

- **Security boundaries**: Credentials never enter the sandbox (brokered at proxy/firewall level)
- **Infrastructure control**: Teams choose their sandbox provider (Cloudflare, Modal, Vercel, Daytona) based on scale, GPU needs, and security posture
- **Observability**: Full access to sandbox logs, metrics, and SSH sessions
- **Customizability**: Custom sandbox images, tools, and network policies

### Skills as Developer Onboarding Surface

Martin maintains the `claude-api` skill — a modular package in Anthropic's skills repository that provides SDK patterns in Python, TypeScript, Go, Java, Ruby, PHP, C#, and curl. The skill embodies his DevRel philosophy: **provide working code in the developer's language of choice** rather than abstract documentation. The `claude-api` skill ships with `SKILL.md` documentation and shared orchestration patterns that work across all self-hosted sandbox providers.

### Context Engineering for Production Agents

Co-author of Anthropic's "Effective Context Engineering for AI Agents" (see [[entities/lance-martin|full profile]]), Martin's context engineering framework — the **Write/Select/Compress/Isolate taxonomy** — directly informs his work on Managed Agents. Self-hosted sandboxes embody the "Isolate" strategy: physically separating execution context from reasoning context.

### Designing Loops with Fable 5 (June 2026)

Martin's June 9, 2026 X article "Designing loops with Fable 5" articulates two core patterns for maximizing Claude Fable 5's capabilities:

1. **Self-correction loops**: Using `/goal` in Claude Code and Outcomes in Claude Managed Agents as primitives that provide environment feedback for model hillclimbing. Fable 5 excels at self-correcting when given well-designed goals or rubrics.

2. **Memory as outer loop**: Memory spans across sessions — Claude writes to memory during a session and retrieves it in future sessions. Fable 5 demonstrates superior memory progression: fail → investigate → verify → distill → consult.

Key findings from his experiments:
- **Parameter Golf benchmark**: Fable 5 improved the training pipeline ~6x more than Opus 4.7, betting on larger structural changes and showing resilience through regressions.
- **Verifier sub-agent**: A verifier sub-agent outperforms self-critique because grading happens in an independent context window.
- **Memory progression**: Fable 5 achieves up to 73% verification coverage (vs Opus 4.7's 7-33%) and distills learnings into general rules for future tasks.

## Key Work

### claude-api Skill (2026) & Sonnet 5 Migration

Anthropic's official skill for building applications with the Claude Agents API. Maintained by Martin, it provides:

- SDK code snippets in 8 languages
- Full orchestration examples for self-hosted sandbox environments
- Shared patterns for polling-based and webhook-based control planes
- An `SKILL.md` guide that Claude Code itself can read to assist developers
- **Sonnet 5 migration support**: Martin tweeted about the `/claude-api` skill in Claude Code, which includes migration guidance for moving to Claude Sonnet 5. The skill provides updated SDK patterns and API references aligned with the [Sonnet 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5).

**Repository**: [github.com/anthropics/skills/tree/main/skills/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api)

### Self-Hosted Sandbox Cookbooks (May 2026)

Martin authored the reference implementations in Anthropic's managed agents cookbook repository, demonstrating the full self-hosted sandbox architecture:

- **Control plane patterns**: Polling-based (long-poll Anthropic's work queue) and webhook-based (FastAPI/Express receiver triggered by session events)
- **Sandbox runner patterns**: In-sandbox tool dispatchers that attach to the session event stream
- **Provider-specific examples**: Cloudflare Workers control plane, Modal Python sandboxes, Vercel Next.js functions, Daytona orchestrators
- **Credential brokering**: Environment key scoping and firewall-level injection patterns

**Repository**: [github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes](https://github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes)

### Sandbox Partner Launch (May 19, 2026)

Martin announced and detailed the four sandbox partnerships:

| Provider | Sandbox Technology | Key Differentiator |
|----------|-------------------|-------------------|
| **Cloudflare** | Dual: microVMs + V8 isolates | Extreme scale (10K+ concurrent), built-in browser/email |
| **Modal** | Firecracker microVMs + GPUs | 100K concurrent, H100 GPUs, burst pricing |
| **Vercel** | Firecracker microVMs | Firewall-level credential brokering, TypeScript-native |
| **Daytona** | Docker containers | Full container ownership, 30-day lifecycle |

## X Activity Themes

Lance Martin's X presence (@rlancemartin) centers on:

1. **Claude Managed Agents architecture** — Deep dives into session lifecycle, work queues, polling vs webhook, credential brokering
2. **Self-hosted sandbox patterns** — Comparing Cloudflare isolates vs Firecracker microVMs vs Docker containers
3. **SDK and skill announcements** — New language support in `claude-api`, cookbook updates, breaking changes
4. **Context engineering** — Writing about prompt caching, compaction strategies, and agent memory design
5. **Developer advocacy** — Amplifying community projects built on Claude Agents API, sharing enterprise adoption stories
6. **Agent platform philosophy** — The "brain/hands" separation, why self-hosted is the default, and the future of agent infrastructure

## Related People/Entities

- [[entities/lance-martin]] — His broader research profile (context engineering, agent design patterns)
- [[entities/anthropic]] — His organization and employer
- [[concepts/anthropic/managed-agents]] — The platform he evangelizes and documents
- [[entities/claude-code]] — The coding agent central to his DevRel work
- [[entities/cloudflare-sandbox]] — Cloudflare sandbox integration for Managed Agents
- [[entities/modal-sandbox]] — Modal sandbox integration for Managed Agents
- [[entities/vercel-sandbox]] — Vercel sandbox integration for Managed Agents
- [[entities/daytona-sandbox]] — Daytona sandbox integration for Managed Agents
- [[entities/cat-wu]] — Head of Product at Anthropic, Claude Code product strategy
- [[concepts/context-engineering|Context Engineering]] — The concept he co-developed
