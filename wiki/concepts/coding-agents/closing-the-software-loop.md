---
title: "Closing the Software Loop"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags:
  - agentic-engineering
  - coding-agents
  - ai-agents
  - workflow
  - software-engineering
  - ai-adoption
sources:
  - "[[raw/articles/2026-01-25_benedict_closing-software-loop]]"
related:
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/autonomous-agents]]"
  - "[[concepts/background-agents]]"
---

# Closing the Software Loop

A concept pioneered by Benedict Brady (Meridian): an **autonomous software improvement loop**. Inspired by Andrej Karpathy's vision of "Tesla's self-driving team going on vacation while the car keeps improving."

## Software Development Loop Evolution

### Phase 1: Traditional (days to weeks per iteration)

```
User feedback → Product team specs it → 
Engineers implement → Code review → Deploy
```

### Phase 2: Agent-Assisted (hours to days per iteration)

```
User feedback → Product team specs it → 
Coding agent implements (overnight) → Human reviews
```

- Weekly features can be implemented overnight
- Product teams must maintain **detailed specs and bug boards**
- Give agents a **Laboratory**: log inspection, dev environment deployment, browser/mobile simulators

### Phase 3: Full Self-Improving (future)

```
Autonomous bug detection → Autonomous spec generation → Autonomous implementation → Autonomous review → Deploy
```

**Missing pieces**: autonomous bug report generation and feature request understanding

#### Data Collection Pathways

| Method | Description | Example |
|------|------|-----|
| Telemetry | Auto-detect bugs from legacy system logs, create bug board entries | Datadog, Sentry |
| Chat Products | Turn user feature requests from chat into specs | Meridian investment strategy requests |
| Autonomous Interviews | Agents conduct user interviews | Listen Labs |

## Meridian Practice Example

User request: "Buy $100 of BTC weekly only when below $75k":
- Traditional: Product team specs → Engineers build price monitoring service → Weeks
- Agent-Assisted: Give agent detailed specs, it tries multiple implementations → Days

## Changing Role of Humans

| Role | Traditional | Closed Loop |
|------|------|------------|
| Product Manager | Write specs | Validate and prioritize auto-generated specs |
| Engineer | Implement | Architecture design + agent code review |
| QA | Test | Audit agent testing strategy |

## References

- [Closing the Software Loop — Benedict Brady](https://www.benedict.dev/closing-the-software-loop) (2026-01-25)
- [Give your agent a laboratory — Brian Lovin](https://brianlovin.com/writing/give-your-agent-a-laboratory-jH5ryjC)
