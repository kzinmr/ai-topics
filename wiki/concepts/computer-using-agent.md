---
title: "Computer-Using Agent"
type: concept
aliases:
  - computer-using-agent
  - CUA
  - computer-use-agent
created: 2026-04-25
updated: 2026-11-11
tags:
  - concept
  - computer-use
  - desktop-automation
  - browser-agent
  - agent-tooling
related:
  - "[[entities/openai-cua]]"
  - "[[entities/anthropic-computer-use]]"
  - "[[concepts/browser-agent/death-of-browser]]"
sources: []
status: active
---

# Computer-Using Agent (CUA)

A **Computer-Using Agent (CUA)** is an AI agent that operates a computer the way a human does:
it perceives the screen (screenshots / accessibility tree), reasons about the interface, and
acts through generic input primitives — mouse clicks, typing, scrolling — rather than through
APIs or purpose-built integrations. The term was popularized by OpenAI's **CUA** model
(powering Operator, later ChatGPT Agent), but now names the whole paradigm.

## Core Loop

```
screenshot / AX tree ──→ VLM perception ──→ reasoning (what to do next)
        ▲                                          │
        │                                          ▼
   new screen  ◀── OS/browser ◀── action (click, type, scroll, key)
```

1. **Perceive** — capture the current display state (pixels, optionally a11y tree / DOM)
2. **Decide** — the model plans the next atomic GUI action toward the goal
3. **Act** — emit a low-level action (coordinates + click type, keystrokes)
4. **Verify** — re-observe and self-correct; guardrails intercept risky steps

## Canonical Implementations

| System | Org | Released | Surface | Notes |
|--------|-----|----------|---------|-------|
| [[entities/openai-cua]] | OpenAI | Jan 2025 (Operator) → ChatGPT Agent Jul 2025 | Browser + VM | GPT-4o vision + RL trained on GUI states; OSD (Online Screenshot Detection) guardrails |
| [[entities/anthropic-computer-use]] | Anthropic | Oct 2024 (beta) | Ubuntu VM | Claude 3.5 Sonnet computer use; screenshot + mouse/key API |
| [[entities/manus]] | Butterfly Effect | Mar 2025 | Cloud VM | General autonomous agent built on CUA-style browsing/execution |
| [[entities/browser-use]] | open source | 2025 | Browser | DOM-first alternative to pure pixel-based control |

## CUA vs. API-First Agents

| Aspect | CUA (GUI control) | API / tool-calling agent |
|--------|-------------------|--------------------------|
| Interface | Human UI (pixels) | Structured APIs / MCP tools |
| Coverage | Anything a human can do | Only what is integrated |
| Speed/cost | Slower, token-heavy screenshots | Fast, cheap |
| Reliability | Brittle to UI changes | Stable contracts |
| Safety surface | Needs human-in-the-loop, confirmations | Scoped by tool permissions |

The practical 2025–2026 pattern is **hybrid**: prefer structured tools (APIs, MCP) when
available, fall back to CUA-style GUI control when no integration exists — "the browser is
now an execution environment for agents" ([[concepts/browser-agent/death-of-browser]]).

## Key Benchmarks

- **OSWorld** — real-OS task completion (Ubuntu/Windows/macOS)
- **WebArena / WebVoyager / Online-Mind2Web** — browser task success
- OpenAI CUA reported 58.1% OSWorld / 87% WebArena at launch (human baseline ~72% / 76%),
  detailed in [[entities/openai-cua]].

## Graph Structure Query

```
[computer-using-agent] ──embodies──→ [concept: browser-agent/death-of-browser]
[computer-using-agent] ──implemented-by──→ [entity: openai-cua]
[computer-using-agent] ──implemented-by──→ [entity: anthropic-computer-use]
[computer-using-agent] ──contrasts──→ [concept: tool-use / API-first agents]
```

## Related Concepts

- [[entities/openai-cua]] — the model that coined the "CUA" name
- [[entities/anthropic-computer-use]] — Anthropic's computer-use tool API
- [[concepts/browser-agent/death-of-browser]] — the browser-as-agent-runtime framing
- [[entities/manus]] — general-purpose agent relying on CUA-style execution

## Sources

- [OpenAI: Computer-Using Agent](https://openai.com/index/computer-using-agent/) — Operator launch (Jan 2025)
- [Anthropic: Computer use](https://www.anthropic.com/news/3-5-models-and-computer-use) — Oct 2024
