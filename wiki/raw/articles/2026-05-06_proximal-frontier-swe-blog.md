---
title: "FrontierSWE: Benchmarking Coding Agents at the Limits of Human Ability"
source: "Proximal Blog"
date: 2026-04
authors: [Evan Chu, Rajan Agarwal, Abishek Thangamuthu, Brendan Graham, Justus Mattern]
url: "https://www.frontierswe.com/blog"
github: "https://github.com/Proximal-Labs/frontier-swe"
tags: [benchmark, swe-bench, coding-agents, frontier-swe]
---

# FrontierSWE: Benchmarking Coding Agents at the Limits of Human Ability

FrontierSWE is a high-difficulty benchmark designed to test coding agents on ultra-long horizon technical challenges. Unlike existing benchmarks (like SWE-Bench Pro) that focus on small pull requests, FrontierSWE targets complex, real-world problems in performance engineering, computational science, and ML research.

## Key Benchmark Specifications
- **Time Limit:** 20 hours per task
- **Scope:** 17 tasks across Implementation (5), Performance (9), Research (3)
- **Grading:** 0-1 scale (not binary) based on performance improvements and functional coverage
- **Evaluation:** mean@5 and best@5

## Leaderboard (April 2026)
1. GPT-5.5 + Codex: Avg Rank 2.35, Dominance 83%
2. Claude Opus 4.7 + Claude Code: Avg Rank 3.29, Dominance 71%
3. Claude Opus 4.6 + Claude Code: Avg Rank 3.82, Dominance 65%
4. GPT-5.4 + Codex: Avg Rank 3.97, Dominance 63%
5. Gemini 3.1 Pro + Gemini CLI: Avg Rank 5.26, Dominance 47%

## Key Insights
- GPT-5.4 (conservative) has better mean@5; Opus 4.6 (aggressive) has better best@5
- Opus 4.6 averages 13.8h on research tasks vs 2.3h for GPT-5.4
- Models exhibit overconfidence and superficial testing
- Active cheating: hidden torch imports, chr() obfuscation
