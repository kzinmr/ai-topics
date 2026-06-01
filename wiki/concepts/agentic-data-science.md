---
title: Agentic Data Science
created: 2026-06-01
updated: 2026-06-01
type: concept
tags:
  - concept
  - data-science
  - ai-agents
  - bayesian
  - agent-orchestration
  - verification
  - orchestration
sources:
  - raw/newsletters/2026-06-01-the-agentic-data-science-research-lab.md
---

# Agentic Data Science

**Agentic data science** is the paradigm of using AI agents to perform data science work — including data exploration, statistical analysis, causal inference, Bayesian modeling, visualization, and reporting — with humans in a supervisory "Principal Investigator" role. It represents the application of [[concepts/agentic-engineering|agentic engineering]] to the data science domain.

## Definition

Agentic data science is the discipline of delegating data science workflows to AI agents while maintaining rigorous verification and scientific standards. Unlike traditional data science (where a human analyst does all the work) or vibe coding (where AI output is accepted without verification), agentic data science treats agents as skilled research assistants that can work autonomously under expert supervision.

Thomas Wiecki of [[entities/thomas-wiecki|PyMC Labs]] articulated this vision in the June 2026 Vanishing Gradients newsletter, drawing on his experience building Bayesian models and the PyMC ecosystem.

## The 4-Layer Stack

Agentic data science operates on a four-layer architecture:

### 1. Harness / Runtime
The foundation layer providing execution environment, tool access, sandboxing, and the agent loop. Examples include Claude Code, OpenClaw, and Hermes Agent. This layer provides:
- Code execution (Python/R/Julia)
- Package management and environment isolation
- File system access and data loading
- API connectivity to databases and external services

### 2. Skills
Reusable, structured documents that teach agents how to perform specific data science tasks. Skills encode professional judgment as reusable artifacts:
- Data cleaning and validation skills
- Exploratory data analysis (EDA) skills
- Statistical modeling skills (regression, Bayesian, causal)
- Visualization skills
- Reporting and documentation skills

### 3. Orchestration
The layer that coordinates multiple agents and tools to execute complex data science workflows:
- Task decomposition: breaking analysis into sub-problems
- Agent delegation: assigning specialized agents to sub-tasks
- Parallel execution: running multiple analyses in parallel (key for the garden of forking paths)
- State management: tracking progress across long-running analyses
- Stakeholder mediation: translating business questions into analytical tasks

### 4. Observability
Monitoring, tracing, and evaluation of agent-driven data science processes:
- Trace logging: recording every analytical step
- Result aggregation: collecting outputs across parallel analyses
- Verification gates: programmatic, agentic, and human checks
- Decision dashboards: surfacing results to stakeholders (see [[entities/decision-lens|Decision Lens]])

## The PI Model: Human as Principal Investigator

Thomas Wiecki frames the human-agent relationship as analogous to a Principal Investigator (PI) with grad students:

- **PI (Human)**: Sets research direction, designs studies, approves methods, reviews results, makes final decisions
- **Grad Students (Agents)**: Execute analyses, write code, explore data, run models, draft interpretations
- **Key principle**: The PI is accountable for the work — agents increase throughput, but the human maintains scientific responsibility

This model explicitly rejects the "vibe science" approach where agents run analyses without verification.

## Garden of Forking Paths Architecture

The garden of forking paths, operationalized in [[entities/decision-lab|Decision Lab]], is a structured approach to robust analysis:

1. **Fork**: At every analytical decision point (how to clean data, which model to use, which covariates to include), the system forks into multiple parallel paths
2. **Execute**: Each path runs its full analysis independently
3. **Compare**: Results are aggregated and compared across all paths
4. **Assess robustness**: Findings that hold across many paths are robust; findings sensitive to analytical choices are flagged

This architecture is particularly powerful when combined with AI agents because agents can:
- Automatically identify forking points
- Spawn and manage hundreds of parallel analyses
- Aggregate results programmatically
- Surface robustness assessments to human PIs
- Scale the garden of forking paths far beyond what human analysts could do manually

## Daemon Agent

The Daemon agent refers to an always-on background agent built using the Claude Code Agent SDK that participates in multiplayer chat sessions. In Thomas Wiecki's vision:

- The Daemon runs continuously in a Slack or similar channel
- It listens to data science discussions and proactively contributes analyses
- Team members can ask the Daemon to run quick analyses, check assumptions, or explore data
- It represents the shift from "ask an analyst, wait for results" to "ask the Daemon, get results in real-time"

## Three-Tier Verification

Agentic data science requires rigorous verification at three levels to escape "vibe science":

### 1. Programmatic Verification
Automated checks built into the analysis pipeline:
- Unit tests for data transformations
- Statistical tests for model assumptions
- Reproducibility checks (same data + same code = same results)
- Sensitivity analyses across model specifications

### 2. Agentic Verification
AI agents review each other's work:
- One agent runs the analysis, another audits the methodology
- Cross-validation of findings across independent agent runs
- Automated peer review with structured critique rubrics

### 3. Human Verification
The PI reviews and signs off:
- High-level review of methods and conclusions
- Spot-checking of key results
- Final decision-making authority
- Escalation of ambiguous or contested findings

## Escaping "Vibe Science"

"Vibe science" — the application of [[concepts/vibe-coding|vibe coding]]'s trust-the-output approach to data analysis — is an anti-pattern that agentic data science explicitly rejects. Key differences:

| Aspect | Vibe Science | Agentic Data Science |
|---|---|---|
| Verification | Minimal or none | Three-tier (programmatic, agentic, human) |
| Reproducibility | Not guaranteed | Built into the pipeline |
| Uncertainty | Ignored or implicit | Quantified via Bayesian methods |
| Analytical choices | Hidden | Tracked via garden of forking paths |
| Human role | Passive consumer | Active Principal Investigator |
| Stakeholder access | Static reports | Interactive Decision Lens |

## Related Concepts

- [[concepts/agentic-engineering]] — The disciplined practice of building with AI agents
- [[concepts/bayesian-methods]] — Probabilistic modeling approach central to the stack
- [[concepts/causal-reasoning]] — Causal inference frameworks
- [[concepts/vibe-coding]] — The less rigorous counterpart
- [[concepts/agent-orchestration]] — Coordinating multiple agents
- [[concepts/agent-skills]] — Reusable patterns for agent tasks
- [[concepts/verification]] — Verification strategies for AI outputs
- [[concepts/harness-engineering]] — Building agent infrastructure
- [[concepts/decision-centric-architecture]] — Decision-oriented design

## Related Entities

- [[entities/thomas-wiecki]] — CEO of PyMC Labs, primary advocate
- [[entities/hugo-bowne-anderson]] — Vanishing Gradients host, co-developer
- [[entities/decision-lab]] — Garden of forking paths tool
- [[entities/decision-lens]] — Agentic stakeholder dashboard
- [[entities/pymc-labs]] — Bayesian consulting firm building these tools

## Sources

- raw/newsletters/2026-06-01-the-agentic-data-science-research-lab.md
