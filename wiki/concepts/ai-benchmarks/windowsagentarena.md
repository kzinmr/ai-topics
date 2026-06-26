---
title: "WindowsAgentArena"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - multimodal
sources:
  - https://arxiv.org/abs/2409.08264
related_concepts:
  - concepts/ai-benchmarks/osworld
  - concepts/ai-benchmarks/androidworld
  - concepts/ai-benchmarks/webarena
---

# WindowsAgentArena

**WindowsAgentArena** is a benchmark for evaluating multi-modal OS agents at scale on the Windows operating system. Introduced by Bonatti et al. from Microsoft (arXiv 2409.08264), it provides 154 realistic multi-step Windows-OS tasks across applications with programmatic success checks. Designed for efficient evaluation, it supports parallel execution in Azure (~20 minutes for a full run), making it the Windows desktop counterpart to [[concepts/ai-benchmarks/osworld|OSWorld]].

**Paper**: [arXiv 2409.08264](https://arxiv.org/abs/2409.08264)

## What It Measures

- **Domain**: Multi-modal agent capabilities on Windows desktop environments
- **Task type**: Realistic multi-step tasks requiring Windows application interaction, file management, and system navigation
- **Format**: Agents observe Windows desktop screenshots and issue keyboard/mouse actions to complete tasks
- **Evaluation**: **Programmatic success checks** verify task completion through system state inspection
- **Key distinction**: Highly parallelizable infrastructure (~20 min full run in Azure) enables rapid iteration and large-scale evaluation

## Data/Methodology

WindowsAgentArena comprises **154 tasks** across the Windows operating system:

| Task Category | Examples |
|--------------|----------|
| Application usage | Word, Excel, PowerPoint, browser tasks |
| File management | File creation, organization, search |
| System operations | Settings changes, app installation, configuration |
| Multi-app workflows | Tasks requiring coordination across multiple applications |

**Methodology**:
1. Tasks run in Azure-hosted Windows VMs with full OS installations
2. Agents observe desktop screenshots (multimodal input) and issue GUI actions
3. Programmatic success scripts verify the final system state
4. Infrastructure supports **parallel execution** — all 154 tasks can run simultaneously in Azure
5. Full evaluation completes in approximately 20 minutes

## Key Results

- **Scale**: 154 realistic multi-step Windows tasks
- **Efficiency**: Full evaluation in ~20 minutes via Azure parallelization
- **Programmatic verification**: Automated success checks ensure consistent, reproducible evaluation
- **Microsoft backing**: Developed by Microsoft Research with direct access to Windows internals for robust evaluation

## Related Benchmarks

- [[concepts/ai-benchmarks/osworld|OSWorld]] — Multi-OS counterpart evaluating agents on Ubuntu/Windows/macOS (369 tasks)
- [[concepts/ai-benchmarks/androidworld|AndroidWorld]] — Mobile counterpart for Android agent evaluation (116 tasks)
- [[concepts/ai-benchmarks/webarena|WebArena]] — Web-focused agent benchmark; WindowsAgentArena focuses on the desktop OS layer

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — WindowsAgentArena demonstrates scalable, parallelizable evaluation infrastructure for OS-level agent testing
- [[concepts/ai-benchmarks/swe-bench|SWE-bench]] — Both evaluate agents in realistic computing environments; SWE-bench targets code-level tasks while WindowsAgentArena targets GUI-level OS tasks
