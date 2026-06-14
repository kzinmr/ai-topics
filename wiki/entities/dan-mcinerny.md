---
title: Dan McInerney
created: 2026-06-14
updated: 2026-06-14
type: entity
tags:
  - entity
  - developer
  - coding-agents
  - open-source
  - agent-harness
  - agent-architecture
sources:
  - raw/articles/2026-06-14_danmcinerny_architect-loop-fable-codex.md
  - https://github.com/DanMcInerney/architect-loop
---

## Overview

**Dan McInerney** is an open-source developer and the creator of [[concepts/architect-loop|Architect Loop]], a cross-vendor agent loop pattern that pairs [[concepts/claude/fable-5|Claude Fable 5]] as architect/planner with [[entities/codex|OpenAI Codex]] (GPT-5.5) as builder. His work addresses the practical engineering challenges of coordinating multiple AI coding agents across vendor boundaries.

## Key Work

### Architect Loop (June 2026)

Dan McInerney created architect-loop as an open-source (MIT) Claude Code skill system after seeing a post by [@jumperz on X](https://x.com/jumperz/status/2065454404623384859) about using Fable with Codex subagents. He built it because no easy way existed to run that pattern, and because "it seemed useful to add a few extra operational best practices on top of what Fable can already do when calling Codex subagents."

The system is source-backed: its [[concepts/architect-loop#the-twelve-design-rules|twelve design rules]] cite Anthropic engineering posts, Fable 5 documentation, Codex CLI docs, and widely used community harness skills. The DESIGN.md file documents every prescriptive claim with evidence.

The loop reduces token costs by 58–74% by running the expensive model (Fable 5) only for judgment minutes while using the flat-rate model (GPT-5.5) for typing hours. It runs on consumer subscriptions — no API keys required by default.

## See Also

- [[concepts/architect-loop|Architect Loop]] — The cross-vendor agent pattern created by Dan McInerney
- [[concepts/claude/fable-5|Claude Fable 5]] — The architect model
- [[entities/codex|OpenAI Codex]] — The builder tool
- [[concepts/coding-agents/coding-agents]] — Coding agent ecosystem
