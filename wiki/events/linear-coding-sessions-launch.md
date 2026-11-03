---
title: "Linear Coding Sessions Launch"
created: 2026-11-03
updated: 2026-11-03
type: event
tags:
  - announcement
  - coding-agents
  - ai-agents
  - developer-tooling
sources:
  - https://linear.app/coding-sessions
  - raw/articles/linear.app--coding-sessions--2026-11-03.md
  - https://x.com/karrisaarinen/status/2117673828046553097
---

# Linear Coding Sessions Launch (Nov 2026)

## What happened

Linear launched **Coding Sessions**: "Linear Agent can now write code. Triage, plan, build, and review all in one place." Announced/promoted on 2026-11-03 by CEO [[entities/karri-saarinen]] on X, recommending it over the older Codex-in-Linear integration: "try Linear coding session (you can use it with codex). Linear sets up environments and works lot faster" — the reply context was a user complaint that Linear-launched Codex agents broke after OpenAI's "new Codex Cloud experience" change.

## Product summary

- Sessions are powered by **Claude Code and Codex**, configured at the workspace level (page demo shows a "Linear Opus 5.5" session working 32s and opening a draft PR).
- Start a session from an issue, chat, comment, or Slack thread; Linear gathers context automatically.
- Delegate or automate: assign issues directly, or let Linear pick them up from Triage — "Bugs can be investigated and fixed before anyone touches a keyboard."
- Every session runs in a **secure cloud sandbox**; output is a reviewable diff/draft PR.
- **Multiplayer sessions**: steer the agent while it runs, iterate from the diff, or point the agent at a project spec.
- Full workspace context: issues, projects, documents, discussions, customer requests.

## Context

This extends [[entities/linear]]'s agent trajectory (Linear Diffs, May 2026; [[concepts/linear-agent-code-intelligence]]) from code *understanding/review* to code *generation*, closing the triage→plan→build→review loop inside the issue tracker. Notable that Linear hosts the execution (its own sandboxes) while wrapping third-party harnesses (Claude Code, Codex) — contrast with [[entities/devin]] and GitHub's Copilot coding agent. The Codex breakage in the reply thread illustrates the fragility of depending on a vendor's cloud-agent surface.

## Related

- [[entities/linear]] — product page
- [[entities/karri-saarinen]] — announced
- [[entities/openai]] — Codex harness + the Codex Cloud change that broke the old integration
- [[concepts/coding-agents/coding-agents]] — category
