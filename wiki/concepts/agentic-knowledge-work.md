---
title: Agentic Knowledge Work
type: concept
created: 2026-06-25
updated: 2026-06-25
tags:
  - agents
  - productivity
  - enterprise-ai
  - codex
  - openai
  - ai-agents
aliases:
  - agent-centric work
  - long-horizon task delegation
sources:
  - raw/articles/2026-06-25_openai-agents-transforming-work.md
  - raw/papers/2026-06-25_openai-shift-to-agentic-ai.md
  - https://openai.com/index/how-agents-are-transforming-work/
  - https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf
---

# Agentic Knowledge Work

The paradigm shift in knowledge work from short, self-contained chatbot interactions to **delegated, long-horizon agentic tasks**. Agents operate independently for minutes or hours, orchestrating tool calls, interacting with environments, and iterating towards solutions — fundamentally changing the unit of productive work.

## Core Thesis

> Agentic AI changes the unit of knowledge work from single interactions to delegated, long-horizon tasks.

This shift has three dimensions:

1. **Temporal expansion**: Tasks grow from seconds-long queries to hours-long autonomous execution
2. **Role expansion**: Non-developer roles adopt coding agents for cross-functional work
3. **Organizational expansion**: Agent usage spreads from engineering to every department

## Evidence: OpenAI Internal Adoption (June 2026)

OpenAI's internal Codex adoption data provides the strongest empirical evidence for this shift ([source](https://openai.com/index/how-agents-are-transforming-work/)):

### Long-Horizon Task Growth

| Threshold | Share of Individual Users (May 2026) |
|-----------|--------------------------------------|
| >30 min human-equivalent work | 80.6% |
| >1 hour | 70.2% |
| >8 hours | 25.6% (fastest growth) |

By June 2026, users at the 99th percentile generated **60+ hours of agent turns per day** across multiple parallel agents.

### Department-Level Adoption Timeline

| Department | Majority Codex Adoption | Output Token Share |
|------------|------------------------|-------------------|
| Engineering | Dec 2025 | 99% |
| Legal | ~Apr 2026 | >85% |
| Finance | ~Apr 2026 | >85% |
| Recruiting | ~Apr 2026 | >85% |

Overall: Codex accounts for **99.8% of weekly output tokens** generated within OpenAI.

### Non-Developer Growth (Aug 2025 → Jun 2026)

| User Group | Growth Factor |
|------------|---------------|
| Individual non-developers | 137× |
| Organizational non-developers | 189× |
| OpenAI internal non-developers | 12× |

### Cross-Functional Work Expansion

Non-technical workers use agents to do work outside their job description. Over **25% of Codex work by business function workers** was engineering or coding — agents lower the cost of moving across task boundaries.

## Key Patterns

### From Chatbot to Agent as Primary Tool

Within OpenAI, the transition from ChatGPT to Codex as the primary AI tool followed an S-curve:
- Engineering moved first (gradual, Aug–Dec 2025)
- Non-engineering departments transitioned faster but later (~Apr 2026)
- By Jun 2026, **every department** uses agents as primary AI tool

### Intensity Deepening

Among active internal users, output token growth (Nov 2025 → Jun 2026):
- Research: **56×**
- Customer Support: **32×**
- Engineering: **27×**
- Legal: **13×**

### Parallel Agent Orchestration

The heaviest users shifted from single-agent queries to orchestrating **multiple parallel agents** throughout the day, representing a new mode of knowledge work.

## Four Stylized Facts (Research Paper)

The underlying research paper ([[raw/papers/2026-06-25_openai-shift-to-agentic-ai|Johnston et al. 2026]]) formalizes four stylized facts:

1. **Rapid but uneven shift**: Codex WAU grew >5× in H1 2026, but remains much less broadly used than ChatGPT. Shift is smallest among individual users, largest among OpenAI workers.
2. **Delegated production, not consultation**: Users ask Codex to do work (debugging, refactoring, drafting, analyzing), not just provide advice. Contrasts with conversational AI usage patterns.
3. **Anchored in software, broader where adoption is deepest**: Software tasks dominate overall, but OpenAI workers extend into research, planning, communication, recruiting, sales.
4. **Large, repeatable, parallel workflows**: Intensive users run 3+ concurrent agents, use skills (26.6%), and delegate tasks estimated >8 hours (nearly tenfold increase since start of 2026).

### Cross-Population Comparison

| Metric | Individual | Organizational | OpenAI |
|--------|-----------|---------------|--------|
| Codex output token share | 16.5% | 63.3% | 99.8% |
| Used Codex in last 28 days | <1% | 17.3% | ~100% |
| WAU growth (H1 2026) | Moderate | Large | Largest |

### Task Complexity Distribution

- >30 min human-equivalent: 80.6% of individual users (May 2026)
- >1 hour: 70.2%
- >8 hours: 25.6% (fastest growth, nearly tenfold since Jan 2026)

### Methodology Note

The paper uses an automated, privacy-protecting pipeline with request-level classifiers on a 4% user sample. Job titles classified via gpt-5-mini. Task taxonomy has two levels (first-level: 14 categories; second-level: granular activities).

## Implications

### For Organizations
- Workflow redesign around agent delegation rather than direct AI interaction
- Technical expertise becomes less of a bottleneck for non-technical departments
- Agent literacy becomes a company-wide skill, not just an engineering tool

### For Workers
- Skills in task decomposition and agent orchestration become more valuable
- Cross-functional capability expands — agents enable "adjacent work" previously requiring specialists
- The definition of "technical work" expands to include non-technical roles

### For the AI Industry
- Agent adoption follows a different pattern than chatbot adoption — faster spread, deeper integration
- Token economics shift dramatically when agents become primary tools (99.8% of output)
- The "coding agent" category expands into "general knowledge work agent"

## Relationship to Existing Concepts

- [[concepts/agentic-engineering]] — Agentic knowledge work is the broader organizational pattern; agentic engineering is the developer-focused subset
- [[concepts/simulacrum-of-knowledge-work]] — Contrasting view: agents may produce work that simulates quality proxies without substance
- [[concepts/ai-economics-post-scarcity]] — Agent-driven productivity as a step toward post-scarcity knowledge work
- [[concepts/loop-engineering]] — The technical patterns that enable long-horizon agent execution

## Related Entities

- [[entities/openai-codex]] — The agent product driving this transformation
- [[entities/openai]] — Publisher of the research data
