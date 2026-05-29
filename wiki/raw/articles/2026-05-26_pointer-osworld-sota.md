---
title: "Pointer - A new state of the art for computer use"
source: https://www.pointer.ai/blog/sota
date: 2026-05-26
---

# Pointer – A New State of the Art for Computer Use

Pointer achieved the two highest verified scores on the OSWorld benchmark: 83.6% with Claude Opus 4.7 and 81.5% with Claude Sonnet 4.6, surpassing the human baseline of 72.4%. The system is fully open-source.

## Architecture
A task controller orchestrates three specialized agents:
- **Feasibility Gate** (Sonnet 4.6): Decides task feasibility before work begins
- **Planner** (Sonnet 4.6): Breaks goals into state-based milestones
- **Executor** (Opus 4.7 / Sonnet 4.6): Does the actual work with unified tools (GUI, code, browser, background execution)

Key principles: GUI-first approach, "two strikes then switch" strategy, feasibility gate with 85.7% recall on impossible tasks and 99.4% specificity.

## Results
- Holds top score in 7 of 10 OSWorld domains
- VS Code: 95.7%, Multi-apps: 74.4% (vs field mean ~10pts lower)
- Both Opus 4.7 and Sonnet 4.6 runs clear all previous agents
