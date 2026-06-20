---
title: "Design Arena"
type: entity
created: 2026-06-20
updated: 2026-06-20
tags:
  - benchmark
  - evaluation
  - frontend
  - web-development
related:
  - concepts/ai-benchmarks-and-evals
  - concepts/llm-evaluation
  - entities/glm-5-zai
  - concepts/claude/fable-5
sources:
  - raw/articles/2026-06-19_designarena_glm-52-beat-fable-5-website-design.md
---

# Design Arena

## Overview

Design Arena (designarena.ai) is an LLM evaluation platform that ranks models on **HTML web design** quality through head-to-head human preference voting (Elo-based). It focuses specifically on single-turn, non-agentic frontend code generation — a distinct evaluation axis from coding benchmarks like [[concepts/ai-benchmarks/swe-bench|SWE-bench]] or terminal-focused benchmarks like Terminal-Bench.

## Evaluation Methodology

- **Format:** Head-to-head human preference voting (Chatbot Arena-style Elo)
- **Scope:** Single-turn HTML/CSS/JS web design generation
- **Non-agentic:** Evaluates one-shot generation, not multi-step agent workflows
- **Leaderboard categories:**
  - Web Design (overall) — main leaderboard
  - Game Dev
  - Data Visualization
  - 3D Design
  - UI Component
- **Metrics:** Elo rating, win rate, head-to-head matchup records

## Analysis Methodology

Design Arena publishes detailed behavioral analyses of top-performing models, examining:
- **Template similarity:** Clustering generated websites by visual similarity to detect "template bias"
- **Dependency usage:** Tracking library adoption (chart.js, three.js, TailwindCSS, font-awesome) and its impact on win rate
- **Output characteristics:** Code length, generation time, character/line counts
- **Error case analysis:** Identifying common failure modes (broken library calls, layout issues, missing interactivity)

## Notable Findings (as of June 2026)

- GLM-5.2 ranked #1 overall (Elo 1360), surpassing Claude Fable 5 — first open-weight model to hold the top spot
- GLM-5.2's success attributed to: high-quality "expert templates," reliable library usage (TailwindCSS 91%, chart.js/three.js), and more intricate output generation
- Trade-off: GLM-5.2 generates 25% more code with 2x longer generation time vs Fable 5
- Fable 5 produces more diversified outputs (less template bias) but lower average quality
- Ideal output length sweet spot: 46K–57K characters

## Key Benchmarks Compared

| Model | Web Design Elo | Pricing (in/out per MTok) | Notes |
|-------|---------------|--------------------------|-------|
| GLM-5.2 | 1360 (#1) | $1.40/$4.40 | MIT licensed, 744B MoE |
| Claude Fable 5 | — (#2) | $10/$50 | Previously held #1 for months |
| Opus 4.6/4.7 | — | — | Top-tier proprietary |

## Relationship to Other Benchmarks

Design Arena complements coding-focused benchmarks:
- [[concepts/ai-benchmarks/swe-bench|SWE-bench]] — real-world software engineering (issue resolution)
- [[concepts/ai-benchmarks/terminal-bench|Terminal-Bench]] — terminal/shell task completion
- **Design Arena** — visual design quality and frontend code generation
- Code Arena — broader coding evaluation (includes frontend and backend)

## Website

- https://www.designarena.ai/
- https://www.designarena.ai/leaderboard
