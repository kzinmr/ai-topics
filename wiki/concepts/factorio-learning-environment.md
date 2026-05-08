---
title: "Factorio Learning Environment (FLE)"
type: concept
created: 2026-05-08
tags:
  - benchmark
  - game-based-agent
  - coding-agents
  - long-term-planning
  - spatial-reasoning
  - resource-optimization
  - agent-evaluation
  - evaluation
aliases:
  - fle
  - factorio-le
  - factorio-agent-env
status: active
sources:
  - https://arxiv.org/abs/2503.09617
  - https://jackhopkins.github.io/factorio-learning-environment/
  - https://github.com/JackHopkins/factorio-learning-environment
related_concepts:
  - concepts/ai-benchmarks-evals-overview
  - concepts/swe-bench
related_entities:
  - entities/florian-brand
---

# Factorio Learning Environment (FLE)

The **Factorio Learning Environment (FLE)** is an open-ended agent evaluation framework built on top of the popular factory-building simulation game [Factorio](https://factorio.com/). Introduced by Jack Hopkins, Mart Bakler, and Akbir Khan in March 2025 (NeurIPS 2025 Datasets and Benchmarks Track), FLE tests AI agents on long-term planning, program synthesis, spatial reasoning, and resource optimization — all without requiring computer vision.

**Paper**: [arXiv 2503.09617](https://arxiv.org/abs/2503.09617) | **Website**: [jackhopkins.github.io/factorio-learning-environment](https://jackhopkins.github.io/factorio-learning-environment/) | **GitHub**: [JackHopkins/factorio-learning-environment](https://github.com/JackHopkins/factorio-learning-environment) | **Leaderboard**: [FLE Leaderboard](https://jackhopkins.github.io/factorio-learning-environment/leaderboard)

## What It Measures

- **Domain**: Long-horizon engineering, factory automation, resource management
- **Task type**: Agent-based code synthesis via REPL (Read-Eval-Print Loop)
- **Interaction model**: Agents interact exclusively by writing Python code using a provided API. No computer vision is required — the agent observes program outputs (stdout/stderr), not pixels
- **Two evaluation settings**:
  1. **Lab-play**: 24 structured tasks where agents must build fully automatic production lines for specific target entities (e.g., "Electronic circuit," "Engine unit," "Sulfuric acid") to a target throughput, with fixed starting inventory and 128 API calls per trajectory
  2. **Open-play**: Unbounded task on a procedurally generated map to "build the largest factory possible" with 5,000 steps. The metric is median production score across 8 independent runs

## Data Sourcing Method

FLE is not a dataset benchmark — it is an **interactive environment**. There are no pre-defined question-answer pairs. Instead:

1. **Factorio game engine**: The environment runs Factorio servers that agents interact with via API calls
2. **REPL interface**: Agents write Python code → code executes in the game → agent reads output → agent writes more code. This mirrors the day-to-day workflow of human programmers
3. **Python namespace persistence**: Agents can define variables, classes, and functions that persist across interactions, enabling cumulative strategy development
4. **Time penalties**: API commands that take physical game time to execute create realistic planning constraints
5. **OpenAI Gym compatibility** (v0.3.0+): Standardized interface for integration with existing agent research frameworks
6. **Manual verification**: The benchmark authors manually verified successful production lines to check that agents didn't cheat (e.g., through API exploits)

## Key Numbers

| Metric | Value |
|--------|-------|
| Lab-play tasks | 24 (v1) → 33 (v2, across three difficulty settings) |
| Lab-play trajectory length | 128 API calls per task |
| Lab-play evaluation | Mean success rate across 8 runs per task |
| Open-play step limit | 5,000 steps |
| Open-play evaluation | Median production score across 8 runs |
| Agent interaction mode | Python REPL (no vision needed) |
| API calls with time penalties | Yes — actions cost in-game time |
| State | Unbounded sandbox (Factorio maps are procedurally generated) |
| Top frontier models (lab-play, late 2025) | GPT-5, Claude Opus ~15-40% depending on task complexity |

## @xeophon's Key Insight

> **"Game-based agent eval. Models write code and interact through REPL, no vision needed. Tests long-term planning, program synthesis, and resource optimization in an exponentially scaling challenge space."** — @xeophon, Part 18 of the Benchmarks & Evals series (2025-05-27)

Xeophon highlights FLE's unique position as a game-based agent evaluation that doesn't require computer vision — a major practical advantage. The REPL interaction pattern elegantly mirrors how human programmers work, and the "no vision" design choice means evaluation focuses purely on reasoning and planning rather than visual perception.

## Strengths

- **No vision requirement**: Unlike most game-based benchmarks (Minecraft, web browsing), FLE requires no computer vision. Agents interact purely through code and text output, dramatically lowering the barrier to evaluation
- **Exponentially scaling challenges**: Factorio's tech tree creates genuinely open-ended difficulty — from simple automation to factories processing millions of resource units per second
- **REPL mirrors real programming**: The Read-Eval-Print Loop interaction pattern simulates how human programmers iteratively probe, test, and refine their understanding of a system
- **Two complementary settings**: Lab-play provides structured, comparable results; open-play tests truly unbounded capability
- **Anti-cheat verification**: Human verification of successful production lines ensures agents actually built what they claim
- **OpenAI Gym compatibility**: Standardized interface simplifies integration with existing agent research frameworks
- **Active development**: Rapid iteration from v0.1 through v0.4.3, with Discord community and growing leaderboard
- **Non-saturating by design**: The open-ended nature of Factorio means there is always a harder challenge available (bigger factory, more complex production chains)
- **Clean measurement of non-vision capabilities**: By removing visual perception from the equation, FLE isolates spatial reasoning, planning, and error correction

## Weaknesses

- **Narrow domain**: Tests only factory automation skills. High FLE performance doesn't transfer to general agentic competence
- **Complex setup**: Requires running Factorio server clusters, making evaluation more operationally complex than standard benchmarks
- **API knowledge dependency**: Agents must learn and use the FLE Python API effectively — performance confounds reasoning ability with API proficiency
- **Spatial reasoning still weak**: The paper's central finding is that even frontier models lack strong spatial reasoning, limiting current performance
- **Limited model coverage**: Relatively few models have formal FLE scores compared to mainstream benchmarks like SWE-Bench or HLE
- **Resource-intensive**: Lab-play requires 24 × 8 = 192 full trajectories; open-play requires 8 × 5,000 step runs — significant compute cost
- **Young benchmark**: Still maturing; methodology and leaderboard norms not yet fully established

## Key Findings from Original Paper

The original FLE paper evaluated six frontier LLMs and found:

1. **Short-horizon competence, long-horizon failure**: Models showed promising skills in individual API calls and simple configurations, but couldn't sustain effective operation across dozens of steps
2. **Spatial reasoning deficit**: Even advanced models struggled to coordinate more than ~6 machines when producing items with 3+ ingredients, even after 128 interactions
3. **Error analysis limitation**: Models failed to effectively debug and recover from their own mistakes in constrained environments
4. **Electric-powered drilling discovery**: In open-play, LLMs did independently discover certain automation strategies (e.g., switching to electric-powered drilling), showing genuine creative problem-solving
5. **Complex automation failure**: Models consistently failed at complex automation goals (e.g., electronic-circuit manufacturing) despite succeeding at simpler ones

## Related Pages

- [[concepts/ai-benchmarks-evals-overview|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
- [[concepts/swe-bench|SWE-Bench]] — Another agent-based evaluation, focused on software engineering bug fixes
- [[concepts/frontier-swe-benchmark|FrontierSWE]] — Ultra-long-horizon coding benchmark (20 hours per task)

## Sources

- Hopkins, J., Bakler, M., Khan, A. (2025). "Factorio Learning Environment." NeurIPS 2025 Datasets and Benchmarks Track. [arXiv:2503.09617](https://arxiv.org/abs/2503.09617)
- [FLE Official Website](https://jackhopkins.github.io/factorio-learning-environment/)
- [FLE GitHub Repository](https://github.com/JackHopkins/factorio-learning-environment)
- [FLE Leaderboard](https://jackhopkins.github.io/factorio-learning-environment/leaderboard)
- [Epoch AI FLE Overview](https://epoch.ai/benchmarks/factorio-learning-environment)
- @xeophon (Florian Brand), "AI Benchmarks & Evals — Part 18: Factorio Learning Environment" (2025-05-27)
