---
title: "Claude Code — Development History"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-05-27
tags:
  - product
  - timeline
sources:
  - https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works
  - https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/
---

# Claude Code: Development History

Back to main profile: [[entities/claude-code]]

## Origins (Sep 2024)
[[entities/boris-cherny]] joined Anthropic and began prototyping with the Claude 3.6 model. The first prototype was a CLI tool that identified and modified music via AppleScript.

## Internal Dogfooding (Nov 2024)
- **20% of engineers** adopted it on day one
- **50% adoption within 5 days**
- 60-100 internal releases per day
- 70-80% of technical staff used it daily

## Sonnet 3.7 and the First Wave of Practical Adoption (Feb 2025)
Claude Sonnet 3.7 (Feb 2025) marked a turning point for Claude Code's practical utility. The model's improved instruction following and code generation capabilities made Claude Code viable for real-world development tasks beyond prototyping. This was the first model where Claude Code began to feel like a reliable coding partner rather than an experimental tool.

Key developments during this period:
- Internal adoption at Anthropic became near-universal
- Early external users began reporting consistent productivity gains
- The "parallel agents" pattern (running multiple Claude Code sessions simultaneously) emerged as a key workflow

## General Availability and Opus 4 Agentic Shift (May 2025)
Claude Code reached General Availability in May 2025, coinciding with the release of Claude Sonnet 4 and Opus 4. This was a critical inflection point:

- **Opus 4 introduced ASL-3** and significantly improved agentic capabilities — longer task execution, better tool use, more reliable multi-step reasoning
- **Claude Code became viable for autonomous workflows**: engineers began delegating entire features, not just individual prompts
- **The "strategy-first" shift**: organizations like Shopify began reporting that engineers spent 70% of time on strategy vs 30% on execution (inverted from the previous 30/70 ratio)
- **Dynamic Workflows concept emerged**: the idea that Claude Code could plan, execute, and verify entire codebase-scale tasks autonomously

## Team Growth (Jul 2025)
The team expanded to about 10 people. Boris Cherny continued development at Anthropic as Head of Claude Code.

## Agent Teams GA (2026)
Multi-agent coordination reached General Availability. Multiple Claude Code instances can work in parallel with role division.

## Source Code Leak Incident (Mar 31, 2026)

### What Happened
Security researcher Chaofan Shou discovered references to unobfuscated TypeScript source code through sourcemap files included in the Claude Code npm package. A zip archive on Anthropic's Cloudflare R2 storage was downloadable.

### Impact
- Source code backup was **forked over 41,500 times** on GitHub
- Caused by sourcemap files in the npm package
- Anthropic's build chain referenced unobfuscated TypeScript source

### Significance
This leak fully exposed Claude Code's internal design, significantly impacting understanding of AI coding agent architecture. See [[entities/claude-code--architecture]] for details.
