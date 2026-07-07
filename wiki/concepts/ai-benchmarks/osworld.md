---
title: "OSWorld"
type: concept
created: 2026-06-26
updated: 2026-07-07
tags:
  - benchmark
  - evaluation
  - ai-agents
  - multimodal
sources:
  - https://arxiv.org/abs/2404.07972
  - https://osworld-v2.xlang.ai/
  - raw/newsletters/2026-07-06-import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation.md
related_concepts:
  - concepts/ai-benchmarks/windowsagentarena
  - concepts/ai-benchmarks/androidworld
  - concepts/ai-benchmarks/webarena
---

# OSWorld

**OSWorld** (Operating System World) is a benchmark for evaluating multimodal agents on open-ended tasks in real computer environments. Introduced by Xie et al. from the University of Hong Kong and collaborators (arXiv 2404.07972), it provides 369 real-computer tasks running in virtual machines across Ubuntu, Windows, and macOS. OSWorld is the canonical computer-use benchmark, featuring per-task execution-based evaluation scripts and initial-state setup.

**Paper**: [arXiv 2404.07972](https://arxiv.org/abs/2404.07972)

## What It Measures

- **Domain**: Multimodal agents operating in real desktop computer environments
- **Task type**: Open-ended tasks requiring GUI interaction, application usage, and multi-step reasoning across operating systems
- **Format**: Agents receive task descriptions and interact with real desktop screenshots + programmatic controls in VMs running Ubuntu, Windows, or macOS
- **Evaluation**: Per-task execution-based evaluation scripts verify whether the agent achieved the correct system state — combining real desktop screenshots for visual grounding with programmatic verification for correctness
- **Key distinction**: Tasks are genuinely open-ended, requiring agents to navigate real OS interfaces rather than simplified sandbox environments

## Data/Methodology

OSWorld comprises **369 tasks** across three operating system environments:

| OS Environment | Task Types |
|----------------|------------|
| Ubuntu | File management, terminal operations, application configuration |
| Windows | Office productivity, system settings, multi-application workflows |
| macOS | Cross-application tasks, preferences, file organization |

**Methodology**:
1. Tasks run in real virtual machine environments with full OS installations
2. Agents observe **real desktop screenshots** (multimodal input) and can issue GUI actions
3. Each task includes a per-task **initial-state setup script** ensuring reproducibility
4. Evaluation uses **programmatic verification scripts** that check the final system state
5. Tasks span multiple difficulty levels and require diverse computer skills

## Key Results

- **Scale**: 369 tasks across Ubuntu, Windows, and macOS
- **Human performance**: ~72% accuracy
- **Best agent performance**: ~12% accuracy (as of initial publication)
- **Massive human-agent gap**: The 60-point gap between human (72%) and best agent (12%) performance established OSWorld as one of the most challenging computer-use benchmarks
|- **Multimodal requirement**: Agents must process real desktop screenshots, making this a true multimodal evaluation

## OSWorld 2.0

In July 2026, OSWorld 2.0 was released with significant updates:

- **108 long-horizon tasks** with a median completion time of **1.6 hours** for skilled humans
- **31 self-hosted websites** enabling realistic web application testing
- **69.6%** of tasks estimated to take a skilled human user more than **one hour**
- Real-world software integrations: **Slack, LinkedIn, Shortcut, REAPER, MuseScore, WPS, GitLab, Overleaf, LabPlot, Zotero, AWS**
- Best agent performance: **Claude Opus 4.8** reaches only **20.6% binary accuracy** — demonstrating the massive gap between human and AI capability on long-horizon computer tasks

Source: [osworld-v2.xlang.ai](https://osworld-v2.xlang.ai/), raw/newsletters/2026-07-06-import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation.md

## Related Benchmarks

- [[concepts/ai-benchmarks/windowsagentarena|WindowsAgentArena]] — Windows-specific counterpart with 154 tasks, parallelizable in Azure
- [[concepts/ai-benchmarks/androidworld|AndroidWorld]] — Mobile counterpart evaluating agents on real Android devices (116 tasks)
- [[concepts/ai-benchmarks/webarena|WebArena]] — Web-focused benchmark; OSWorld extends the agent evaluation paradigm to full operating systems

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — OSWorld demonstrates the programmatic verification approach for complex, multi-step agent evaluation in real environments
- [[concepts/ai-benchmarks/swe-bench|SWE-bench]] — Both benchmarks evaluate agents on realistic computing tasks; SWE-bench focuses on code while OSWorld focuses on GUI-based OS interaction
