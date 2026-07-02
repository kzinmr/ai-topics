---
title: "Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding"
source_url: "https://deep-reinforce.com/ornith_1_0.html"
date: 2026-06-25
tags: [model, open-source, coding-agents, agentic-rl, self-scaffolding, reinforcement-learning]
---

# Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding

Source: https://deep-reinforce.com/ornith_1_0.html

## Summary

DeepReinforce's official release page for Ornith-1.0. Introduces the self-improving training framework, benchmark results, and reward hacking defenses.

## Key Technical Details

### Self-Improving Training Framework

The core innovation is a two-stage RL loop per step:
1. Given task + previous scaffold → model proposes a refined scaffold
2. Given refined scaffold + task → model generates a solution rollout
3. Reward from rollout is propagated to BOTH stages

This means the scaffold (orchestration logic) co-evolves with the policy (solution generation). Scaffolds are "continually mutated and selected toward those that induce higher-reward trajectories."

### Reward Hacking Defense (3 layers)

1. **Fixed trust boundary**: environment, tool surface, test isolation are immutable — model only evolves inner policy scaffold (memory, error-handling, orchestration logic)
2. **Deterministic monitor**: flags attempts to read withheld paths, modify verification scripts, or invoke unsanctioned actions → zero reward + exclusion from advantage computation
3. **Frozen LLM judge**: vetoes verifier results for intent-level gaming within allowed tool surface

### Asynchronous RL Training

Uses pipeline-RL strategy for long rollouts. Staleness weight downweights tokens by age, drops them past threshold. Token-level GRPO loss with staleness weighting.

### Benchmark Results (397B)

- Terminal-Bench 2.1 (Terminus-2): **77.5** (vs Claude Opus 4.7: 70.3, Claude Opus 4.8: 85)
- SWE-Bench Verified: **82.4** (vs Claude Opus 4.7: 80.8, Claude Opus 4.8: 87.6)
- SWE-Bench Pro: **62.2** (vs Claude Opus 4.7: 64.3)
- NL2Repo: **48.2**
- ClawEval Avg: **77.1**

### Benchmark Results (35B)

- TB-2.1: **64.2** (vs Qwen3.5-397B: 53.5 — 35B surpasses 397B base!)
- SWE-Bench Verified: **75.6**

### Benchmark Results (9B)

- TB-2.1: **43.1** (vs Gemma4-31B: 42.1 — 9B matches 31B base)
- SWE-Bench Verified: **69.4**

### Evaluation Details

- TB-2.1 (Terminus-2): Harbor/Terminus-2, parser=json, temp=1.0, top_p=1.0, 128K context, 4h timeout, 32 CPU/48GB RAM, 5 runs avg
- TB-2.1 (Claude Code): Claude Code 2.1.126, same params, 5 runs avg
- SWE-Bench: OpenHands harness, temp=1.0, top_p=0.95, 256K context
- NL2Repo: temp=1.0, top_p=1.0, 400K context, 48K output, anti-hacking filters
- ClawEval: real-user task distributions, temp=0.6, 256K context
