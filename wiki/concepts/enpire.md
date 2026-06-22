---
title: "ENPIRE — Agentic Robot Policy Self-Improvement"
created: 2026-06-18
updated: 2026-06-18
type: concept
tags:
  - coding-agents
  - robotics
  - embodied-ai
  - nvidia
  - ai-agents
  - autoresearch
  - agent-loop
  - self-improving
  - lab
  - research-lab
sources:
  - raw/articles/2026-06-18_enpire-nvidia-gear.md
  - https://research.nvidia.com/labs/gear/enpire/
---

# ENPIRE — Agentic Robot Policy Self-Improvement

## Overview

**ENPIRE** (Agentic Robot Policy Self-Improvement) is a system developed by **NVIDIA GEAR Lab** (led by [[entities/jim-fan|Jim Fan]]), in collaboration with CMU and UC Berkeley, that bridges frontier coding agents with physical robotics. ENPIRE enables coding agents to **autonomously develop manipulation policies for real-world dexterous tasks** through a fully automated environment loop — marking the first system where coding agents perform autonomous research in the physical world rather than purely digital environments.

**Authors**: Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, et al.

The core insight: achieving dexterous robotic manipulation has historically depended on heavy human supervision and algorithmic engineering. ENPIRE's key contribution is the **repeatable environment loop with automated evaluation and reset** — the missing abstraction that allows coding agents, which had previously been confined to digital tasks, to operate effectively on real-world robotics problems.

## Architecture

### The Environment Loop

ENPIRE's architecture revolves around a self-contained environment loop that enables autonomous research without human intervention:

| Component | Function |
|-----------|----------|
| **Auto Evaluation** | Automated success/failure detection for each task attempt. The system programmatically determines whether a robot action achieved its goal. |
| **Auto Reset** | Robots reset themselves to a known starting state between attempts, eliminating the need for human repositioning of objects or recalibration. |
| **Verification Scaffold** | Automated testing infrastructure that ensures policy correctness. The coding agents construct task-specific interfaces (`env.reset`, `env.get_reward`, etc.) as part of their workflow. |

The combination of these three components creates a closed loop: the agent proposes an algorithmic change → the environment evaluates it → the robot resets → the agent receives feedback → the cycle repeats. This is the critical scaffolding that makes autonomous physical-world research tractable.

### Coding Agent Fleet

ENPIRE employs a fleet of frontier coding agents working in parallel:

- **Agents tested**: Codex, Claude Code, Kimi Code — three leading coding agents as of mid-2026
- **Fleet scaling**: Up to 8 Codex agents running concurrently, with dynamic GPU allocation and token budgets
- **Algorithmic exploration**: Agents autonomously propose diverse algorithmic hypotheses including heuristic learning, behavior cloning, offline RL, and online RL approaches
- **Task-specific interface construction**: Coding agents first construct their own interfaces (`env.reset`, `env.get_reward`, etc.) for each task before beginning the improvement loop

### Metrics

ENPIRE introduces two novel metrics for fleet-managed autonomous research:

- **Mean Robot Utilization (MRU)** — measures how effectively physical robot hardware is kept busy across the fleet
- **Mean Token Utilization (MTU)** — measures the efficiency of LLM token expenditure per policy improvement

These metrics reflect a key operational reality: both physical robots and LLM inference are scarce resources that must be managed jointly in autonomous physical-world research.

## Tasks and Results

ENPIRE demonstrated autonomous policy development across four increasingly complex dexterous manipulation tasks:

| Task | Description | Result |
|------|-------------|--------|
| **PushT** | Pushing a T-shaped object to a target position | **99% success rate** (pass@8) |
| **Pin Insertion** | Organizing pins into a pin box | High success rate |
| **Zip-Tie Cutting** | Using a cutter to sever a zip tie | High success rate |
| **GPU Insertion** | Complex industrial manipulation (inserting a GPU into a PCIe slot) | Demonstrated |

The 99% success rate on PushT is particularly notable — coding agents autonomously discovered policies that achieve near-perfect performance on a real-world dexterous manipulation task, without human intervention in the improvement loop.

## Significance and Implications

### Bridging Coding Agents and Physical Reality

ENPIRE represents a landmark convergence of two previously separate trajectories in AI research:

1. **Coding agents** — systems like [[concepts/coding-agents/coding-agents|Codex, Claude Code, and Kimi Code]] that can autonomously write and iterate on code — had been confined to digital domains (software engineering, data analysis, benchmark optimization).

2. **Robotics** — the field of [[concepts/robotics|real-world robot learning]] — had remained dependent on human researchers for algorithm design, hyperparameter tuning, and physical experiment management.

ENPIRE bridges these domains by providing the **missing abstraction**: a repeatable environment loop. This is the same insight that made digital coding agents viable — the ability to run code, observe results, and iterate automatically — now extended to the physical world.

### The Scaffold is the Heavy Lift

A central takeaway from ENPIRE is captured in the observation: **"The agents are the small part; the load-bearing work is the scaffold around them."** This echoes the broader [[concepts/harness-engineering|harness engineering]] principle that in production AI systems, the harness (evaluation, verification, state management, feedback loops) does more work than the model itself. ENPIRE applies this principle to robotics: the auto-evaluation, auto-reset, and verification infrastructure is the true innovation; the coding agents are a component within that scaffold.

### From Model Labs to Agent Labs in the Physical World

ENPIRE extends the industry shift from "model labs to agent labs" (see [[concepts/coding-agents/pi-autoresearch|pi-autoresearch]]) into physical robotics. Just as coding agents can autonomously optimize build times, test speeds, and search ranking functions, ENPIRE shows they can optimize robot manipulation policies — pointing toward a future where [[concepts/recursive-self-improvement|recursive self-improvement]] loops operate not only in software but in the physical world.

## Comparison with Other Coding Agent Systems

ENPIRE extends coding agent capabilities into a domain that other systems do not reach:

| System | Domain | Autonomous Loop | Physical-World Tasks |
|--------|--------|----------------|---------------------|
| **ENPIRE** | Robotics manipulation | Full (auto-eval + auto-reset) | **Yes** |
| [[concepts/coding-agents/coding-agents|Devin]] | Software engineering | Interactive, not fully autonomous | No |
| Claude Code | Code generation and editing | Interactive pair-programming | No |
| Codex | Software engineering, data analysis | Task-based with human review | No |
| [[concepts/coding-agents/pi-autoresearch|pi-autoresearch]] | Arbitrary metric optimization | Full (metric-driven loop) | No |
| [[concepts/karpathy-loop|Karpathy Autoresearch]] | ML model training | Full (training loop) | No |

ENPIRE is unique in bringing the fully autonomous, closed-loop research paradigm — previously demonstrated only in digital domains — to **real-world physical manipulation**. The auto-reset and auto-evaluation scaffold is what makes this possible; without it, physical-world experiments require a human in the loop to reset the environment and judge outcomes.

## Relation to Embodied AI and Physical AI

ENPIRE sits at the intersection of several active research trajectories:

- **[[concepts/embodied-ai|Embodied AI]]** — ENPIRE operationalizes embodied AI research by letting coding agents directly interact with physical robots through the environment loop, rather than relying on pre-programmed sim-to-real pipelines.
- **[[concepts/physical-ai|Physical AI]]** — ENPIRE demonstrates a practical path toward autonomous improvement of physical-world AI systems, addressing the "bits vs atoms" gap that [[entities/jim-fan|Jim Fan]] has long highlighted.
- **[[concepts/self-evolving-agents|Self-Evolving Agents]]** — ENPIRE's coding agent fleet represents Level 2-3 self-evolution (strategy adaptation + capability expansion) operating on physical hardware rather than purely in software.

## Key Design Decisions

1. **Agent-constructed interfaces**: Rather than providing a pre-built API, ENPIRE requires coding agents to construct their own task-specific interfaces (`env.reset`, `env.get_reward`). This forces the agent to understand the task structure and builds toward general-purpose physical world interaction.

2. **Fleet parallelism**: By running 8 coding agents simultaneously with managed GPU allocation and token budgets, ENPIRE achieves exploration diversity — different agents discover different algorithmic strategies, and successful approaches propagate through the shared feedback signal.

3. **Scaffold over model**: The system deliberately treats the coding agent as a replaceable component. The auto-evaluation, auto-reset, and verification infrastructure is the durable investment — consistent with the [[concepts/harness-engineering|harness > model]] principle established across production agent systems in 2026.

## Open Questions

- **Generalization to novel tasks**: How well does ENPIRE's scaffold generalize to manipulation tasks far outside its training distribution?
- **Scaling limits**: What is the marginal benefit of adding more coding agents to the fleet? Is 8 agents near the sweet spot?
- **Safety implications**: As autonomous physical-world research scales, what guardrails are needed to prevent coding agents from proposing dangerous physical experiments?
- **Token economics**: At what point does MTU (Mean Token Utilization) become the binding constraint, and how can it be optimized?

## See Also

- [[entities/nvidia]] — NVIDIA corporation, GEAR Lab's parent organization
- [[entities/jim-fan]] — Jim Fan, lead of NVIDIA GEAR Lab
- [[concepts/coding-agents/coding-agents]] — Coding agents overview (Codex, Claude Code, Kimi Code)
- [[concepts/robotics]] — Robotics concept page
- [[concepts/embodied-ai]] — Embodied AI concept page
- [[concepts/harness-engineering]] — The harness > model principle that ENPIRE's scaffold exemplifies
- [[concepts/recursive-self-improvement]] — Recursive self-improvement in AI systems
- [[concepts/coding-agents/pi-autoresearch]] — pi-autoresearch, a similar autonomous optimization loop for digital metrics
- [[concepts/physical-ai]] — Physical AI and the bits vs atoms distinction
- [[concepts/self-evolving-agents]] — Self-evolving agent architectures
