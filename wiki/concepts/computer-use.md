---
title: "Computer Use Agents"
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [computer-use, agents, automation, benchmark, pointer]
sources:
  - https://www.pointer.ai/blog/sota
  - https://uncensoredhub.ai/news/2026-05-29-claude-opus-4-8-orchestrates-hundreds-of-parallel-subagents-hits-84-on-browser-a
---

# Computer Use Agents

**Computer use agents** are AI systems that operate computers the same way humans do — clicking, typing, navigating — to accomplish tasks across multiple applications.

## OSWorld Benchmark

OSWorld is the standard benchmark for computer use agents, spanning 360+ tasks across:
- Web browsing (Chrome)
- Coding (VS Code)
- Photo editing (GIMP)
- Document/spreadsheet work (LibreOffice)
- Media playback (VLC)
- Email (Thunderbird)
- Operating system tasks

**Human baseline: 72.4%**

## Current State of the Art (May 2026)

| System | Model | OSWorld Score | Notes |
|---|---|---|---|
| [[entities/pointer-ai|Pointer AI]] | Claude Opus 4.7 | **83.6%** | Highest verified score |
| [[entities/pointer-ai|Pointer AI]] | Claude Sonnet 4.6 | 81.5% | Second place |
| [[entities/anthropic|Anthropic]] | Claude Opus 4.8 | 84% | Online-Mind2Web (browser) |
| Previous best | — | ~78% | Before Pointer results |

## Pointer AI Architecture

- **Lightweight task controller** + 3 specialized agents
- Generator-validator loop: one subsystem makes changes, another validates by reviewing diffs
- Different models excel at different domains (Opus > Sonnet on most, Sonnet > Opus on VS Code, Impress, VLC)
- Multi-apps category: +15 point jump with Opus 4.7
- Fully open source release

## Phantom Tools Phenomenon

5% of Opus 4.7 tool calls in OSWorld were to **tools that were never provided** — ingrained "computer use primitives" from heavy reinforcement during training. The model hallucinated tools it had been trained to use.

## Dynamic Workflows Impact

[[concepts/dynamic-workflows|Dynamic Workflows]] in [[concepts/claude-opus-4-8|Claude Opus 4.8]] extends computer use to codebase-scale migrations across hundreds of thousands of lines, with parallel subagent orchestration.

## Related Pages
- [[entities/pointer-ai]] — Pointer AI, SOTA computer use agent developer
- [[concepts/dynamic-workflows]] — Dynamic Workflows for parallel subagent orchestration
- [[entities/anthropic]] — Anthropic's Claude Opus 4.8 computer use capabilities
- [[concepts/agent-orchestration]] — Agent orchestration patterns
