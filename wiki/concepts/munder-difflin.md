---
title: "Munder Difflin"
created: 2026-08-26
updated: 2026-08-26
type: concept
tags: [agent-harness, multi-agent, autonomous-agents, local-llm, open-source, security]
sources:
  - raw/articles/2026-08-22_munder-difflin.md
  - https://munderdiffl.in/
---

# Munder Difflin

**Munder Difflin** (munderdiffl.in) is a free, open-source (MIT) **multi-agent harness** that "runs an office of your clones" — it was **#1 on GitHub Trending (Repository of the Day)** the week of Aug 22, 2026 and drew 311 HN points / 146 comments. The pitch: wrap the CLI coding agents you already use (Claude Code, Codex, Grok, Kimi Code, Antigravity, Qwen, Gemini CLI, OpenCode, Crush, Pi, Copilot, Cursor — 12 providers off the shelf), capture your personal workflow/memory, and run persistent 24/7 "clones" of yourself (and your teammates) that work in parallel and message each other.

## Core design

- **Local-first node**: each clone is a node on its owner's laptop (everything at 127.0.0.1). Code, keys, and personal context never leave the machine; it works with existing subscriptions (hourly limits), not API keys you buy separately.
- **Clone = person, not bot**: rather than one shared team bot, each teammate gets a clone that emulates *their* workflow, standards, and knowledge ("reviews like you would," "answers for you at 3am").
- **Per-node architecture**: a **GOD orchestrator** (reads/plans/routes) plus role agents — research, build, review, sell, draft — each in its own isolated **git worktree**; **MemPalace** stores "their memory · their machine · nowhere else."
- **Clone-to-clone E2E messaging**: X25519 / AES-256-GCM, same-org only; clones unblock each other overnight (e.g. "need the invoice-state tokens" → tokens sent → PR #147 open by morning).
- **Deterministic "office" simulation UI**: monitor agents in a The-Office-themed office (Michael/Jim/Pam/Dwight as nodes) or a clean fullscreen mode; the simulation itself consumes no tokens.

## Role coverage

Everything scriptable via CLI: developers (PR review, CI babysitting), designers (design-system audits, asset export), PMs (specs, triage, standup preps), sales/GTM (outreach, CRM hygiene), and "everyone else" (reports, spreadsheets, scheduling).

## Security posture (vendor-claimed)

Local-first by default; E2E-encrypted inter-clone mail; versioned shared org knowledge base that new clones inherit (shared ≠ personal); fully open source so the node, protocol, and crypto can be audited. Cloud + Network license moves clones to dedicated sandbox VMs 24/7 with the same encryption.

## Commercial model

Free core; PRO from $20/mo (or $200/yr) with optional 24/7 sandboxes (+$19–$78/mo tiers); TEAMS from $39/seat/mo with E2E clone-to-clone and shared org knowledge; $20 one-time "Founding Supporter" plaque. Founding-supporter pricing: first 100 get 50% off PRO + 1 free month.

## Why it matters for the wiki

Munder Difflin is a concrete data point for three trends the wiki tracks:
1. **Agent-harness consumerization** — harnesses are moving from dev-tool CLIs to personal "digital employee" products with consumer UX (office simulation, Slack triggers).
2. **Clone/agent-employee pattern** — persistent per-person agent identities that emulate an individual's workflow and persist across sessions, closest in the wiki to agent-employees and personal-ai.
3. **Local-first multi-agent security** — E2E-encrypted clone mail + local-only memory as an alternative to cloud agent platforms; pairs with the sandbox/agent-security pages.

All performance/feature claims are vendor-published marketing; treat as unverified.

## Related

- [[concepts/agent-harnesses]] — the harness category this product belongs to
- [[concepts/multi-agents/multi-agent-systems]] — multi-agent coordination patterns
- [[concepts/self-evolving-agents]] — persistent agents that accumulate knowledge over time (MemPalace memory-sharing)
- [[concepts/sandbox]] — sandboxed-agent deployment; Munder Difflin's cloud plan uses dedicated sandbox VMs
- [[concepts/coding-agents/coding-agents]] — the 12 wrapped CLI coding agents are the workload
- [[concepts/agent-harness-primitives]] — harness building blocks (orchestrator + role agents + memory)

Raw source: [[raw/articles/2026-08-22_munder-difflin]]
