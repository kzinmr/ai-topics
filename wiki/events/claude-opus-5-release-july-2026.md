---
title: "Anthropic Releases Claude Opus 5 (July 2026)"
type: event
created: 2026-07-25
updated: 2026-07-25
tags:
  - anthropic
  - claude
  - model
  - announcement
  - frontier-models
sources:
  - raw/articles/2026-07-24_simonwillison_introducing-claude-opus-5.md
---

# Anthropic Releases Claude Opus 5 (July 2026)

## Summary

On July 24, 2026, [[entities/anthropic|Anthropic]] released **[[concepts/claude/opus-5|Claude Opus 5]]**, the successor to Claude Opus 4.8. The model achieves near-Fable-5 intelligence at half the price, demonstrating notably proactive behavior — including autonomously building a computer vision pipeline to solve a visual task when no direct viewing mechanism was provided.

## Key Details

- **Release date**: July 24, 2026
- **Pricing**: Unchanged from Opus 4.8 ($5/$25 per million input/output tokens)
- **Leadership**: Immediately topped the Artificial Analysis leaderboard, ahead of Fable 5
- **Key differentiator**: "Relentlessly proactive" behavior — takes initiative beyond explicit instruction
- **Cyber capabilities**: Strong at finding vulnerabilities, deliberately not trained for exploitation

## Notable Anecdote

On a Frontier-Bench task, Opus 5 was asked to write code to rebuild a machine part from a drawing — but was given no way to directly view the drawing. The model responded by writing its own computer vision pipeline to extract geometry from raw pixels, then reconstructed the full machine part autonomously.

## Companion Releases

- **Prompting guide**: Anthropic published an official prompting guide for Opus 5
- **Context engineering guide**: Thariq Shihipar published "The new rules of context engineering for Claude 5 generation models"

## Related Pages

- [[concepts/claude/opus-5|Claude Opus 5]] — Model concept page
- [[concepts/claude/opus-4-8|Claude Opus 4.8]] — Predecessor
- [[entities/anthropic]] — Anthropic
- [[concepts/harness-engineering/context-engineering]] — Claude 5 gen prompting paradigm
