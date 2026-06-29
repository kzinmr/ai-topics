---
title: SkillsBench
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
sources:
  - https://github.com/benchflow-ai/skillsbench
related_concepts:
  - agent-evaluation
  - ai-agents
---

# SkillsBench

SkillsBench is a benchmark developed by BenchFlow for evaluating agent skill acquisition and application. It tests an AI agent's ability to learn new skills from demonstrations or instructions and then apply those skills effectively in novel situations.

## What It Measures

SkillsBench measures an agent's capability along two key dimensions:

- **Skill acquisition**: How effectively an agent can learn new skills from demonstrations, documentation, or examples
- **Skill application**: How well an agent can apply acquired skills to new, previously unseen tasks
- **Transfer learning**: The ability to generalize learned skills to different contexts and scenarios
- **Skill composition**: Whether agents can combine multiple acquired skills to solve complex tasks
- **Learning efficiency**: How quickly and accurately agents acquire new capabilities from limited examples

## Data/Methodology

SkillsBench uses a structured evaluation framework within the BenchFlow ecosystem:

- **Skill learning tasks**: Scenarios where agents must acquire new capabilities from provided examples or documentation
- **Application tests**: Novel tasks that require the agent to apply previously learned skills
- **Dockerized execution**: Runs within the [[benchflow-tool]] framework for reproducible evaluation
- **Open-source**: Available on GitHub at benchflow-ai/skillsbench for community contribution
- **Standardized skill definitions**: Well-defined skill specifications that enable consistent evaluation across agents

## Key Results

- SkillsBench reveals significant variation in agents' ability to acquire and apply new skills
- Current agents show stronger performance on skill application than on skill acquisition from limited examples
- The benchmark highlights the gap between agents that memorize specific task solutions and those that genuinely learn transferable skills
- Results inform the development of more capable and adaptable [[ai-agents]] systems

## Related Benchmarks

- [[clawsbench]] — BenchFlow's benchmark for agent clawback/recovery testing
- [[benchflow-tool]] — The BenchFlow evaluation framework that hosts SkillsBench
- [[hal-leaderboard]] — Princeton's aggregated agent evaluation leaderboard
- [[trail]] — Agent trace reasoning and issue localization

## Connections to Other Wiki Concepts

SkillsBench addresses a fundamental question in [[agent-evaluation]]: can agents genuinely learn new capabilities, or do they merely apply existing knowledge? This connects to broader [[ai-agents]] research on adaptability and generalization. As part of the BenchFlow ecosystem alongside [[clawsbench]], SkillsBench contributes to a comprehensive view of agent capabilities that feeds into aggregated evaluations like [[hal-leaderboard]].
