---
title: "ST-WebAgentBench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - safety
  - web-development
sources:
  - https://arxiv.org/abs/2410.06703
related_concepts:
  - concepts/ai-benchmarks/webarena
  - concepts/ai-benchmarks/online-mind2web
  - concepts/agent-safety
---

# ST-WebAgentBench

**ST-WebAgentBench** (Safety and Trustworthiness Web Agent Benchmark) is a benchmark for evaluating safety and trustworthiness in web agents. Introduced by Levy, Shlomov, Wiesel et al. from IBM Research (arXiv 2410.06703), it goes beyond task completion to assess whether web agents obey safety constraints and policy rules during execution. With 375 enterprise tasks carrying 3,057 explicit safety/policy constraints, it introduces metrics for Completion-under-Policy and Risk Ratio.

**Paper**: [arXiv 2410.06703](https://arxiv.org/abs/2410.06703)

## What It Measures

- **Domain**: Safety and trustworthiness of web agent actions
- **Task type**: Enterprise web tasks with explicit safety constraints and policy rules
- **Format**: Agents must complete web tasks while adhering to safety policies — not just achieving goals, but doing so safely
- **Evaluation**: Two novel metrics:
  - **Completion-under-Policy (CuP)**: Whether the agent successfully completes the task while respecting all safety constraints
  - **Risk Ratio**: The degree to which agent actions violate safety policies
- **Key distinction**: Grades whether agents **obey rules**, not just whether they succeed — a web agent that completes a task by violating safety policies scores poorly

## Data/Methodology

ST-WebAgentBench comprises **375 enterprise tasks** with **3,057 explicit safety/policy constraints**:

**Constraint Types**:
- Data access restrictions (don't share personal information)
- Action authorization limits (don't delete without confirmation)
- Navigation policies (don't access unauthorized pages)
- Compliance requirements (follow organizational workflows)

**Methodology**:
1. Tasks are set in enterprise web application contexts
2. Each task carries multiple explicit safety constraints
3. Agents are evaluated on both task completion AND constraint adherence
4. **Completion-under-Policy** measures whether the task was done correctly AND safely
5. **Risk Ratio** quantifies the degree of policy violation across the agent's trajectory

## Key Results

- **Scale**: 375 tasks with 3,057 explicit safety constraints
- **Safety-first evaluation**: Establishes that task completion alone is insufficient — safety compliance must be a first-class evaluation criterion
- **Enterprise focus**: Tasks reflect real enterprise web application scenarios where safety and compliance are critical
- **Novel metrics**: Completion-under-Policy and Risk Ratio provide nuanced safety assessment beyond binary pass/fail

## Related Benchmarks

- [[concepts/ai-benchmarks/webarena|WebArena]] — Web agent benchmark focused on task completion; ST-WebAgentBench extends evaluation to include safety constraints
- [[concepts/ai-benchmarks/online-mind2web|Online-Mind2Web]] — Live-website evaluation; ST-WebAgentBench adds safety dimension to web agent assessment

## Connections to Other Wiki Concepts

- [[concepts/agent-safety|Agent Safety]] — ST-WebAgentBench is a direct implementation of agent safety evaluation principles, measuring whether agents respect policy boundaries
- [[concepts/security-and-governance/agent-security-landscape-2026|Agent Security Landscape 2026]] — The benchmark addresses the growing need for safety-aware evaluation as web agents are deployed in enterprise contexts with compliance requirements
