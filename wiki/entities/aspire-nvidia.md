---
title: ASPIRE (NVIDIA GEAR Lab)
type: entity
created: 2026-10-17
updated: 2026-10-17
related:
  - "[[entities/jim-fan]]"
  - "[[entities/nvidia]]"
  - "[[concepts/robotics]]"
  - "[[concepts/embodied-ai]]"
tags:
  - nvidia
  - robotics
  - ai-agents
  - open-source
sources:
  - raw/articles/nvidia-aspire-agentic-skills-discovery-robotics-2026.md
  - https://research.nvidia.com/labs/gear/aspire/
  - https://github.com/nvlabs/aspire
---

# ASPIRE (NVIDIA GEAR Lab)

**ASPIRE: Agentic Skills Discovery for Robotics** — a self-improving, code-as-policy robot
manipulation system from NVIDIA's GEAR Lab (led by [[entities/jim-fan]]), announced Oct 16, 2026
and open-sourced.

- Project page: https://research.nvidia.com/labs/gear/aspire/
- Code: https://github.com/nvlabs/aspire

## Overview

ASPIRE is a self-improving continual learning system in which a coding agent writes and refines
code-as-policy robot control programs from execution feedback: it inspects rollout traces,
diagnoses failures, repairs programs, validates corrected behaviors by re-execution, and saves
reusable skills for future tasks.

Three components form an open-ended learning loop:

1. **Closed-Loop Robot Execution Engine** — records observations, inputs, outputs, and visual
   evidence for each perception/planning/grasping/control call. Multimodal traces let the agent
   inspect primitive logs, localize failures, and validate repairs through re-execution.
2. **Continually Expanding Skill Library** — distills validated fixes into modular, transferable
   robotic knowledge, retrievable as in-context guidance for future tasks.
3. **Evolutionary Search Over Programs** — generates diverse task sequences and control programs,
   exploring beyond single-trajectory self-improvement via iterative debugging and parallel
   refinement.

## Key results

- **Benchmarks:** LIBERO-Pro (Object/Goal/Spatial under position + task perturbations; 160 tasks
  × 50 held-out seeds), Robosuite (contact-heavy tabletop; 100 seeds/task), BEHAVIOR-1K
  (long-horizon mobile manipulation; 25 seeds/task). Baseline: CaP-Agent0, which regenerates a
  program per seed with test-time reasoning and retries.
- **Model scaling:** evaluated across GPT-6 Astra, Claude Opus 5.5, Claude Sonnet 5.5, Claude
  Fable 5.1, Kimi K3, Qwen 3.8 Max with fixed environment/robot API/protocol — ASPIRE improves
  with stronger models (success-vs-cost frontier reported).
- **Skill transfer:** skills learned on LIBERO-90 carry over zero-shot to held-out long-horizon
  tasks; success rises as the skill library grows. On real robots, retrieving a sim-discovered
  skill reduces tokens to first success and raises held-out success rate.
- **Real-robot online learning:** the coding agent acts as a system-2 calling executable
  perception/action tools — demonstrated Rubik's cube solving (GPT-6 Astra), bottle-cap
  unscrewing/pill-bottling, and cup stacking. Tokens and wall-clock per completed task fall
  across episodes as skills accumulate.

## Limitations (author-stated)

- Not yet fully autonomous in the real world — still requires robust success detection, safe
  resets, safety monitoring, and calibration.
- Depends on a frozen frontier LLM (Claude Opus 4.6); whether smaller/weaker LLMs can sustain
  the debugging loop is unverified.
- Expressible behaviors are bounded by a predefined primitive API (perception/planning/control),
  which keeps debugging safe but limits generality.
- Long-term memory management of the skill library is incomplete — entries can become stale,
  overly specific, or redundant as the library grows.

## Related

- [[entities/jim-fan]] — GEAR Lab lead
- [[entities/nvidia]]
- [[concepts/robotics]] · [[concepts/embodied-ai]]
