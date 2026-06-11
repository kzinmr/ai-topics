---
title: "Dark Factory Software Factory"
type: concept
created: 2026-04-13
updated: 2026-05-26
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
---

# Dark Factory Software Factory

**Source:** Simon Willison's Weblog (2026-01-28, 2026-02-07)
**Practitioners:** StrongDM AI Team (Justin McCarthy, Jay Taylor, Navan Chauhan)
**Related:** [[concepts/agent-team-swarm/agent-team-swarm]], [[concepts/openai/symphony]], [[concepts/anthropic/managed-agents]]

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

## Related

- [[concepts/agent-team-swarm/agent-team-swarm]] — Higher-level concept of multi-Agent coordination
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
