---
title: "WebGames"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - web-development
sources:
  - https://arxiv.org/abs/2502.18356
related_concepts:
  - concepts/ai-benchmarks/webarena
  - concepts/ai-benchmarks/real-benchmark
  - concepts/ai-benchmarks/browsecomp
---

# WebGames

**WebGames** is a benchmark of challenging general-purpose web-browsing AI agent tasks. Introduced by Thomas et al. from Convergence AI (arXiv 2502.18356), it provides a suite of 50+ client-side challenges that isolate specific browser interaction skills with verifiable pass/fail outcomes. The benchmark reveals a sharp diagnostic gap: best agents achieve 41% while humans score 96%.

**Paper**: [arXiv 2502.18356](https://arxiv.org/abs/2502.18356)

## What It Measures

- **Domain**: General-purpose browser interaction skills
- **Task type**: Client-side web challenges that isolate specific browser capabilities
- **Format**: Self-contained web-based challenges, each testing a specific skill (drag-and-drop, form filling, multi-tab management, canvas interaction, etc.)
- **Evaluation**: Verifiable pass/fail — each challenge has a clear, programmatically-checkable success criterion
- **Key distinction**: Unlike multi-step web agent benchmarks, WebGames isolates individual browser interaction skills, providing sharp diagnostic signals about specific agent weaknesses

## Data/Methodology

WebGames comprises **50+ client-side challenges** covering diverse browser interaction skills:

**Challenge Categories**:
- GUI interactions (drag-and-drop, slider manipulation, dropdown selection)
- Form handling (multi-field input, validation, submission)
- Multi-tab and multi-window management
- Canvas and visual element interaction
- Dynamic content handling (AJAX, animations)

**Methodology**:
1. Each challenge is a self-contained web page with a specific interaction goal
2. Challenges are client-side only — no server dependencies
3. Success/failure is programmatically verifiable
4. Challenges isolate specific skills to enable targeted diagnosis
5. Human baseline established at 96% for comparison

## Key Results

- **Scale**: 50+ client-side browser interaction challenges
- **Human performance**: 96%
- **Best agent performance**: 41%
- **Diagnostic gap**: The 55-point gap between human and agent performance highlights fundamental browser interaction skill deficits in current web agents
- **Skill isolation**: Enables identification of specific interaction types where agents struggle most

## Related Benchmarks

- [[concepts/ai-benchmarks/webarena|WebArena]] — Multi-step web tasks on realistic websites (812 tasks); WebGames provides more granular, skill-isolated evaluation
- [[concepts/ai-benchmarks/real-benchmark|REAL]] — Deterministic website simulations (112 tasks); WebGames takes a different approach with client-side challenges
- [[concepts/ai-benchmarks/browsecomp|BrowseComp]] — Information-retrieval focused browsing (1,266 questions); WebGames focuses on interaction skills rather than information finding

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — WebGames demonstrates the skill-isolation approach to agent evaluation, breaking down complex web tasks into discrete, diagnosable components
- [[concepts/ai-benchmarks/osworld|OSWorld]] — Both reveal large human-agent gaps (WebGames 55pts, OSWorld 60pts), suggesting fundamental challenges in GUI-based agent interaction across web and desktop domains
