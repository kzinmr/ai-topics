---
title: "Dark Factory Software Factory"
type: concept
created: 2026-04-13
updated: 2026-06-16
tags:
  - concept
  - multi-agent
  - automation
related: [agent-team-swarm, openai-symphony, anthropic-managed-agents, sairahul1]
sources:
  - https://simonwillison.net/2026/Feb/7/software-factory/
  - https://simonwillison.net/2026/Jan/28/
  - https://github.com/strongdm/attractor
  - https://github.com/strongdm/cxdb
  - raw/articles/2026-05-25_sairahul1_claude-code-software-factory-7-agents.md
  - raw/articles/2026-06-15_factory-ai_software-factory-2.0.md
---

# Dark Factory Software Factory

**Source:** Simon Willison's Weblog (2026-01-28, 2026-02-07)
**Practitioners:** StrongDM AI Team (Justin McCarthy, Jay Taylor, Navan Chauhan)
**Related:** [[concepts/multi-agents/agent-team-swarm]], [[concepts/openai/symphony]], [[concepts/anthropic/managed-agents]]

---

## Overview

A **"Dark Factory"** is the highest level of automation in software development, where **humans write no code and perform no reviews**. The term is a metaphor derived from Fanuc's unmanned factories (robot-operated factories need no lighting = dark).

Simon Willison introduced the concept on January 28, 2026, via Dan Shapiro's "5 Levels of AI-Assisted Programming" model, and elaborated on StrongDM's practical implementation on February 7.

---

## Dan Shapiro's 5-Level Model

| Level | Name | Description |
|---|---|---|
| **Level 1** | Spicy Autocomplete | Early GitHub Copilot, code completion |
| **Level 2** | Chat-Assisted | Ask ChatGPT then copy-paste |
| **Level 3** | Agent-Assisted | Claude Code/Codex executes tasks (human monitors) |
| **Level 4** | The Engineering Team | Write specs and plans, Agent implements. Human acts as manager |
| **Level 5** | Dark Factory | **Fully autonomous development with no humans needed** |

### Level 5 Definition

> At level 5, it's not really a car any more. You're not really running anybody's software any more. And your software process isn't really a software process any more. It's a **black box that turns specs into software**.
>
> Why Dark? Maybe you've heard of the Fanuc Dark Factory, the robot factory staffed by robots. It's dark, because it's a place where **humans are neither needed nor welcome**.
> — Dan Shapiro

---

## StrongDM's Practice

### Team Composition
- **3 members** (Justin McCarthy, Jay Taylor, Navan Chauhan)
- Formed July 2025, achieved working demo in a few months
- Claude 3.5 Sonnet (October 2024 revision) capability improvements were the catalyst

### Key Characteristics

1. **Nobody reviews AI-produced code, ever.** Humans never look at generated code
2. **The goal is to prove the system works.** Resources are heavily invested in testing/validation
3. **Humans design the system.** The human role is to discover new patterns where Agents work effectively

### Digital Twin Universe

StrongDM's most striking concept:

> [The Digital Twin Universe is] behavioral clones of the third-party services our software depends on. We built twins of Okta, Jira, Slack and more. How do you clone the important parts? **With coding agents!**

By using Agents to clone the behavior of dependent services (Okta, Jira, Slack, etc.) and building a complete test environment, StrongDM achieves:
- Test execution independent of external services
- 24/7 automated test operation
- Quality assurance for agent-generated code

---

## Attractor: Non-Interactive Coding Agent

StrongDM's core product released as open source:

- **[github.com/strongdm/attractor](https://github.com/strongdm/attractor)** — The repository contains no code, only Markdown files describing specifications
  - "Have your favorite coding agent read these specs"
- **[github.com/strongdm/cxdb](https://github.com/strongdm/cxdb)** — AI Context Store
  - 16,000 lines of Rust + 9,500 lines of Go + 6,700 lines of TypeScript
  - A system for saving conversation history and tool outputs

### Open Source Ecosystem

Hundreds of open-source implementations appeared within a month of Attractor's release:
- Language-specific forks
- Custom harness implementations
- Property testing / fault injection / fuzz testing integration

---

## Simon Willison's Observations

> "Honestly, six months ago, I thought that was crazy, and today, probably 95% of the code that I produce, I didn't type it myself."
> — Simon Willison, Lenny's Podcast (2026-04)

While Willison positions the Dark Factory as "a vision of the future," he highlights important caveats:

- He doesn't write 95% of his own code, but **the remaining 5% of design decisions are critically important**
- AI writing code has become easy, but the judgment of **"what to build and why"** remains a human responsibility
- The design of testing and validation infrastructure is the key to Dark Factory success

---

## Conditions for Achieving Dark Factory

Extracted from StrongDM and Willison's observations:

| Condition | Description |
|---|---|
| **Powerful Harness** | Agent execution environment, tool integration, guardrails are essential |
| **Automated Test Network** | Property testing, fault injection, E2E tests |
| **Digital Twin** | Cloned environments for dependent services |
| **Spec-Driven** | Detailed specification documents are the sole input to Agents |
| **Proof of Work** | Quality is proven by test pass and CI success, not by the code itself |
| **Human System Design** | Humans focus on system design and pattern discovery |

---

## 5-Level Model and Agent Team/Swarm Relationships

```
Level 1-2: Individual productivity tools (Copilot, ChatGPT)
Level 3: Harness Engineering (single Agent + execution environment)
Level 4: Agent Team / Swarm (multi-Agent coordination, Symphony/Managed Agents)
Level 5: Dark Factory (fully autonomous, humans design only)
```

OpenAI Symphony and Anthropic Managed Agents provide Level 4 infrastructure, while StrongDM's practice points the way toward Level 5.

---

## Case Study: @sairahul1's Claude Code 7-Agent Factory (May 2026)

@sairahul1 ([[entities/sairahul1|Rahul]]) presents a practical guide to a personal-developer Dark Factory using Claude Code. A pipeline of 7 specialized agents that overcomes the limitations of vibe coding.

### 7-Agent Configuration

| # | Agent | Role | Tool Restrictions |
|---|-------|------|-----------|
| 1 | **Codebase Researcher** | Codebase investigation, pattern documentation | Read, Grep, Glob (read-only) |
| 2 | **Story Writer** | User story and acceptance criteria creation | Read (read-only) |
| 3 | **Spec Writer** | Technical design document (blueprint) creation | Read, Grep, Glob (read-only) |
| 4 | **Backend Builder** | API, service, DB, and unit test implementation | Read, Edit, Write, Bash (backend only) |
| 5 | **Frontend Builder** | Component, page, and UI test implementation | Read, Edit, Write, Bash (frontend only) |
| 6 | **Test Verifier** | Acceptance test creation against criteria | Read, Edit, Write (test files), Bash |
| 7 | **Implementation Validator** | Diff report between implementation and spec (no edits) | Read, Grep, Glob (read-only) |

### Pipeline Design Highlights

- **3 human checkpoints**: Story approval → Design doc approval → PR review (everything else is fully automated)
- **Importance of CLAUDE.md**: 100-300 line repository root Markdown — add rules each time AI makes a mistake, evolving as the team's collective knowledge
- **Context isolation**: Each agent operates with a clean context window containing only necessary information — preventing propagation of false assumptions
- **Context Drift rules**: Inline fix for small typos, discard entire conversation and restart for wrong architectural assumptions
- **Setup in 2-3 hours**: A practical factory that individual developers can build in a weekend

### Comparison with StrongDM

| Aspect | StrongDM Attractor | @sairahul1 7-Agent Factory |
|------|-------------------|--------------------------|
| Target | Team (3 people) | Individual developer |
| Code review | Humans never look | Validator auto-checks, human only for PR |
| Testing strategy | Digital Twin Universe | Acceptance tests + Validator |
| Setup | Large-scale infrastructure (cxdb, attractor) | 2-3 hours, CLAUDE.md + 7 agent definitions |
| Autonomy level | Level 5 (fully autonomous goal) | Level 4 (coordinated team with human supervision) |

Source: [[raw/articles/2026-05-25_sairahul1_claude-code-software-factory-7-agents]]

## Case Study: Factory.ai Software Factory 2.0 (June 2026)

**Factory.ai** ([[entities/factory-ai|Factory]]) announced **Factory 2.0: From coding agents to software factories** in June 2026, expanding from standalone coding agents to an interconnected, agent-native, end-to-end software factory system. This represents a commercial enterprise interpretation of the Dark Factory concept.

### Spectrum of Autonomy

Factory 2.0 introduces a graduated **spectrum of autonomy** — acknowledging that organizations don't start at Level 5 but progress through deliberate stages:

| Tier | Name | Description | Autonomy Level |
|------|------|-------------|----------------|
| 1 | **Droids** | Task-level autonomous agents | Level 3 (Agent-Assisted) |
| 2 | **Automations** | Recurring workflow coordination with shared objective and memory | Level 3-4 transition |
| 3 | **Droid Computers** | Remote and persistent execution for long-running or local agents | Level 4 (Engineering Team) |
| 4 | **Missions** | Multi-agent autonomous execution solving complex tasks over hours/days via parallel decomposition | Level 5 (Dark Factory) |

### Three Core Requirements

Factory 2.0 argues a robust software factory must have:

1. **Model Independence** — Every model has different trade-offs of cost, performance, and speed. No single model fits every enterprise need. The factory must allow deliberate model selection or rely on a **Router** to automatically choose the best model per task.

2. **Sovereign Intelligence** — Organizations must own their factory: cloud-hosted, bring-your-own-key, self-hosted data plane, EU-specific, or completely air-gapped. Sovereignty means owning a system that learns from itself — every agent session, code review, and resolved incident feeds back into the loop. Capability stays inside the organization's walls.

3. **Continual Learning and Self-Improvement** — Every SDLC stage must be instrumented. When code review, security analysis, documentation, QA, and incident response run on the same platform, they share the same agent core, model router, and organizational context. A security finding informs code review; a deployment triggers a documentation update; an incident correlates with the PR that caused it.

### Enterprise Production Customers

Factory 2.0 is live with enterprise customers including **NVIDIA, EY, Adobe, Palo Alto Networks, Adyen, Blackstone, Wipro, and Comarch**. This demonstrates that Dark Factory concepts have moved beyond early adopters into Fortune 500 deployment.

### Comparison with Other Approaches

| Aspect | StrongDM Attractor | @sairahul1 7-Agent Factory | Factory.ai 2.0 |
|--------|-------------------|--------------------------|----------------|
| Target | Team (3 people) | Individual developer | Enterprise organizations |
| Autonomy | Level 5 goal (humans design) | Level 4 (coordinated with checkpoints) | Spectrum (Droids → Missions) |
| Model strategy | Claude 3.5 Sonnet | Claude Code | Model-independent Router |
| Infrastructure | Digital Twin Universe | CLAUDE.md + agent definitions | Full SDLC platform |
| Sovereignty | Open source (attractor, cxdb) | Personal setup | Air-gapped / self-hosted options |
| Continual learning | Implicit via test feedback | Explicit CLAUDE.md evolution | Platform-wide feedback loops |

Source: [[raw/articles/2026-06-15_factory-ai_software-factory-2.0]]

## Related

- [[concepts/multi-agents/agent-team-swarm]] — Higher-level concept of multi-Agent coordination
- [[concepts/openai/symphony]] — Orchestrator enabling Level 4
- [[concepts/anthropic/managed-agents]] — Platform foundation for Level 4
- [[concepts/harness-engineering]] — Foundation for execution environment design across all levels
- [[entities/sairahul1]] — Originator of the 7-Agent Factory

---

## Sources

- [Simon Willison: The Five Levels](https://simonwillison.net/2026/Jan/28/) (2026-01-28)
- [Simon Willison: How StrongDM's AI team build serious software](https://simonwillison.net/2026/Feb/7/software-factory/) (2026-02-07)
- [StrongDM Attractor](https://github.com/strongdm/attractor)
- [StrongDM CXB](https://github.com/strongdm/cxdb)
- [Business Insider: Simon Willison says the 'dark factory' is the next big thing in AI](https://tech.yahoo.com/ai/articles/simon-willison-says-dark-factory-224709005.html) (2026-04-04)
