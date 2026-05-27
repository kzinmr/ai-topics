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

## General Availability (May 2025)
- Team expanded to ~10 engineers
- Already recording high growth rates as of July 2025

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
This leak fully exposed Claude Code's internal design, significantly impacting understanding of AI coding agent architecture. See [[claude-code--architecture]] for details.
