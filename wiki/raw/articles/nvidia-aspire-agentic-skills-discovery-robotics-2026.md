---
title: "ASPIRE: Agentic Skills Discovery for Robotics"
url: https://research.nvidia.com/labs/gear/aspire/
github: https://github.com/nvlabs/aspire
author: NVIDIA GEAR Lab (Jim Fan / @drjimfan)
date: 2026-10-16
scraped: 2026-10-17
source: x-accounts-scan (tweet 2111128798645416006 by @drjimfan)
---

# ASPIRE: Agentic Skills Discovery for Robotics

- Project page: https://research.nvidia.com/labs/gear/aspire/
- Code: https://github.com/nvlabs/aspire
- Announced 2026-10-16 by Jim Fan (@drjimfan), Director of AI at NVIDIA / GEAR Lab.
- Tagline: "Self-improving code-as-policy robot manipulation with a continually growing skill library."

## What it is

ASPIRE is a self-improving continual learning system for robotics that writes and refines
**code-as-policy** robot control programs from execution feedback. It inspects rollout traces,
diagnoses failures, repairs programs, validates corrected behaviors, and saves reusable skills
for future tasks.

Three key components in an open-ended learning loop:

1. **Closed-Loop Robot Execution Engine** — records observations, inputs, outputs, and visual
   evidence for each perception/planning/grasping/control call. Rich multimodal traces let the
   agent inspect primitive logs, localize failures, and validate repairs through re-execution.
2. **Continually Expanding Skill Library** — distills validated fixes into modular, transferable
   robotic knowledge, retrievable as in-context guidance for future tasks.
3. **Evolutionary Search Over Programs** — generates diverse task sequences and control programs,
   exploring beyond single-trajectory self-improvement via iterative debugging and parallel
   refinement.

## Capabilities shown

- Cross-embodiment sim-to-real, long-horizon tasks (table bussing) — Claude Opus 4.6 (sim), GPT-5.5 (real)
- Online learning on a real robot: solve the Rubik's Cube (GPT-6 Astra), unscrew bottle cap,
  put pill in bottle and screw cap, stack cups upside-down.
- Coding agent acts as a "system-2" calling executable perception/action tools, recording what it
  learns as text skills.

## Benchmarks

- Model suite (environment/robot API/eval protocol fixed): GPT-6 Astra, Claude Opus 5.5, Claude
  Sonnet 5.5, Claude Fable 5.1, Kimi K3, Qwen 3.8 Max. ASPIRE improves with stronger models.
- **LIBERO-Pro**: Object/Goal/Spatial under position + task perturbations; 160 tasks × 50 held-out
  seeds. ASPIRE learns on a small debug split; baseline CaP-Agent0 regenerates a program per seed
  with test-time reasoning/retries.
- **Robosuite**: contact-heavy tabletop manipulation, 100 held-out seeds/task.
- **BEHAVIOR-1K**: long-horizon mobile manipulation, 25 held-out seeds/task (Opus 5.5 not evaluated).
- **Zero-shot skill transfer**: skills learned on LIBERO-90 carry over to held-out long-horizon
  tasks; success rises as the skill library grows.
- **Real-robot cross-embodiment transfer**: retrieving a sim-discovered skill reduces tokens to
  first real-robot success and raises held-out success rate.
- Efficiency: tokens and wall-clock per completed task fall across episodes as skills accumulate
  (amortized incl. failures, recovery, context compaction).

## Limitations (author-stated)

- Not yet fully autonomous in the real world: still needs robust success detection, safe resets,
  safety monitoring, calibration.
- Depends on a frozen frontier LLM (Claude Opus 4.6); smaller/weaker LLMs unverified for the
  debugging loop.
- Bounded by a predefined primitive API (perception/planning/control set) — keeps debugging safe
  but limits expressible behaviors.
- Incomplete long-term memory management: as the library grows, entries may become stale, overly
  specific, or redundant.
