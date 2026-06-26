---
title: "AndroidWorld"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - multimodal
sources:
  - https://arxiv.org/abs/2405.14573
related_concepts:
  - concepts/ai-benchmarks/osworld
  - concepts/ai-benchmarks/windowsagentarena
  - concepts/ai-benchmarks/webarena
---

# AndroidWorld

**AndroidWorld** is a dynamic benchmarking environment for evaluating autonomous agents on real Android devices. Introduced by Rawles et al. from Google DeepMind and Google Research (ICLR 2025, arXiv 2405.14573), it provides a live Android environment with durable reward signals derived from device system state. With 116 parameterized tasks across 20 apps, AndroidWorld is the standard mobile-GUI agent benchmark.

**Paper**: [arXiv 2405.14573](https://arxiv.org/abs/2405.14573)

## What It Measures

- **Domain**: Mobile GUI agent capabilities on real Android devices
- **Task type**: Multi-step tasks requiring app navigation, system interaction, and goal completion on Android
- **Format**: Agents interact with real Android devices through screenshots and touch/swipe/type actions
- **Evaluation**: **Durable reward signals from device system state** — tasks are verified by checking the actual Android system state (app data, settings, files, etc.) rather than relying on trajectory matching
- **Key distinction**: Runs on real Android devices/emulators rather than simulated environments, providing authentic mobile interaction challenges

## Data/Methodology

AndroidWorld comprises **116 parameterized tasks** across **20 Android apps**:

| App Category | Examples | Task Types |
|-------------|----------|------------|
| Productivity | Calendar, Email, Notes | Scheduling, message composition, note-taking |
| System | Settings, Files | Configuration changes, file management |
| Social | Messaging, Contacts | Communication tasks, contact management |
| Utilities | Calculator, Clock | Calculation, timer/alarm setup |

**Methodology**:
1. Tasks run on real Android device environments (physical or emulated)
2. Agents observe device screenshots and issue touch/swipe/type actions
3. Tasks are **parameterized** — each task template can generate multiple instances with different parameters
4. Reward signals are derived from **durable device system state** (not fragile screen comparisons)
5. Initial state is set up programmatically for each task

## Key Results

- **Scale**: 116 parameterized tasks across 20 apps
- **ICLR 2025**: Published at a top ML venue, establishing academic credibility
- **Dynamic environment**: Parameterized tasks prevent overfitting to fixed test instances
- **Durable evaluation**: System-state-based rewards are more robust than visual or trajectory-based evaluation
- **Standard mobile benchmark**: Widely adopted as the reference benchmark for mobile GUI agent evaluation

## Related Benchmarks

- [[concepts/ai-benchmarks/osworld|OSWorld]] — Desktop counterpart evaluating multimodal agents on Ubuntu/Windows/macOS (369 tasks)
- [[concepts/ai-benchmarks/windowsagentarena|WindowsAgentArena]] — Windows-specific desktop agent evaluation (154 tasks)
- [[concepts/ai-benchmarks/webarena|WebArena]] — Web-focused agent benchmark; AndroidWorld extends the agent evaluation paradigm to mobile platforms

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — AndroidWorld demonstrates system-state-based evaluation for mobile agents, a more durable approach than trajectory or visual matching
- [[concepts/ai-benchmarks/swe-bench|SWE-bench]] — Both use environment state verification: SWE-bench checks test pass/fail, AndroidWorld checks device system state
