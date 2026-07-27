---
title: "Claude Opus 5"
type: concept
created: 2026-07-25
updated: 2026-07-25
tags:
  - anthropic
  - model
  - coding-agents
  - proactive
  - security
sources:
  - raw/articles/2026-07-24_simonwillison_introducing-claude-opus-5.md
---

# Claude Opus 5

**Claude Opus 5** is a frontier LLM released by **Anthropic on July 24, 2026**. It is the successor to [[concepts/claude/opus-4-8|Claude Opus 4.8]], described as a "thoughtful and proactive model that comes close to the frontier intelligence of Claude Fable 5 at half the price."

## Release Information

- **Release date**: July 24, 2026
- **Predecessor**: Claude Opus 4.8 (May 28, 2026)
- **Pricing**: Same as Opus 4.8 — $5/M input, $25/M output tokens
- **Fast mode**: $10/M input, $50/M output (2× base pricing)
- **Positioning**: Near-Fable-5 intelligence at half the price; currently leading the Artificial Analysis leaderboard ahead of Fable 5

## Key Capabilities

### Proactive Problem-Solving

Opus 5 exhibits notably **proactive** behavior — it takes initiative beyond explicit instructions. On a Frontier-Bench task, when asked to write code to rebuild a machine part from a drawing, Opus 5 was intentionally given no way to directly view the drawing. It responded by **writing its own computer vision pipeline** to extract geometry from raw pixels, then reconstructed the full machine part — entirely autonomously.

### Cybersecurity

Opus 5 has **not been trained on cyber exploitation**, but shows substantial improvement in vulnerability discovery as a byproduct of general capability gains:

| Capability | Relative to Mythos 5 |
|------------|---------------------|
| Finding vulnerabilities | Comes close |
| Exploiting vulnerabilities | Substantially behind |

This deliberate asymmetry — strong at finding, weak at exploiting — reflects Anthropic's safety-conscious approach to frontier model capabilities.

### Effort Routing

As with the broader Claude 5 generation, Opus 5 supports **effort routing** — dynamically allocating compute between "fast mode" and deeper reasoning depending on task complexity. This architecture treats frontier intelligence deployment as a routing problem rather than a fixed-capability model.

## Platform Features

- Available via Claude API, claude.ai, Claude Code, and Cowork
- Supports the Claude 5 generation context engineering paradigm (see [[concepts/harness-engineering/context-engineering]])
- Prompting guide published alongside release
- Thariq Shihipar authored companion piece on "new rules of context engineering for Claude 5 generation models"

## Model Position in Claude Family

| Model | Release | Positioning |
|-------|---------|-------------|
| [[concepts/claude/opus-4-6|Opus 4.6]] | April 2026 | Frontier coding |
| [[concepts/claude/opus-4-7|Opus 4.7]] | April 2026 | Expanded agent capabilities |
| [[concepts/claude/opus-4-8|Opus 4.8]] | May 2026 | Dynamic Workflows, Effort Control |
| **Opus 5** | July 2026 | Near-Fable-5 intelligence, proactive behavior |
| Claude Fable 5 | 2026 | Maximum intelligence frontier |

## Related Pages

- [[concepts/claude/opus-4-8]] — Predecessor model
- [[concepts/claude/fable-5|Claude Fable 5]] — Frontier intelligence sibling
- [[concepts/harness-engineering/context-engineering]] — Claude 5 generation prompting paradigm
- [[entities/anthropic]] — Anthropic (developer)
- [[entities/claude-code]] — Claude Code coding agent
- [[concepts/frontier-models-comparison-april-2026]] — Frontier model landscape
