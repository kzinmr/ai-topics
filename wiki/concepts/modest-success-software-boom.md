---
title: "The Modest-Success Boom — Where AI Software Growth Actually Shows Up"
created: 2026-10-17
updated: 2026-10-17
type: concept
tags: [ai-economics, ai-industry, productivity, developer-tooling, ai-slop]
aliases: [modest-success boom, missing software boom, hobbyist software boom]
sources:
  - raw/articles/2026-10-17_seangoedecke_ai-is-driving-a-boom-in-modestly-successful-software.md
confidence: medium
related:
  - "[[concepts/ai-slop-productivity-paradox]]"
  - "[[concepts/code-review-bottleneck]]"
  - "[[concepts/ai-coding-effectiveness-debate]]"
  - "[[concepts/vibe-coding]]"
---

# The Modest-Success Boom — Where AI Software Growth Actually Shows Up

## One-line claim

Sean Goedecke (GitHub, Oct 2026) measured ~20 install-count-generating registries and
found AI-driven software growth is **concentrated in modestly successful projects
(~2x), with zero growth in wildly successful ones** — resolving the long-running
"where is all the new software?" question.

## The measurement

Comparison window: **2022-24 (pre-agentic-coding) vs. 2025-26 (post)** across
marketplaces, plugin registries, and modding platforms that expose installation counts.
Goedecke deliberately used addons/mods/plugins, not repos, so "made" is distinguished
from "actually installed/used" — and to exclude software *about AI* (the
[[concepts/vibe-coding|shovel-selling]] category).

| Registry | Modest-success tier | Wild-success tier |
|---|---|---|
| NVDA screen-reader addons | **>2x** new addons (>1,000 downloads) | **no change** (>10,000 downloads) |
| HACS home-automation plugins | **2x** new (>100 installs) | **no change** (>1,000 installs) |
| New Steam games | **~+60%** (>100 reviews) vs. pre-2024 | — |
| Obsidian / Firefox / Chrome / Nexus / Blender | same pattern | — |
| Google Play, WordPress plugins | **no pattern** | — |

Background rate: total projects grew **~10x** over the same period; only a
fraction survived into the "used by hundreds/thousands" band.

## Why it matters

- **It reframes [[concepts/ai-slop-productivity-paradox|the slop paradox]].** Marcus
  reads a rising output/quality gap as AI inflating nominal productivity. Goedecke
  reads the same data as a *distribution shift*: real, small, used software exists —
  it just doesn't look like a hit product, so headline-driven observers don't see it.
- **It is the supply-side mirror of [[concepts/code-review-bottleneck]].** The Jellyfish
  telemetry (700 firms) says enterprise output is capped by senior human review;
  hobbyist registries have no review gate at all — which is exactly where the
  new software surfaces.
- **Big incumbent software is feature-saturated and feature-paralyzed.** New features in
  mature products (Gmail, macOS) are subtle and internal; coding agents add little
  where the visible feature list is already finished.

## Open questions

- Is the wild-success tier merely **lagging** (thousand-user tools maturing into
  hundred-thousand-user tools), or does product taste not compound with cheap code?
- Registry-selection bias: does the pattern hold in non-plugin, standalone commercial software?
- Attribution: no voluntary AI-disclosure data is usable (disclosure invites backlash),
  so the causal link to AI rests on the timing coincidence plus the 10x total-project growth.

## Sources

- Sean Goedecke, "AI is driving a boom in modestly successful software projects" (2026-10-15).
- Raw: `raw/articles/2026-10-17_seangoedecke_ai-is-driving-a-boom-in-modestly-successful-software.md`
