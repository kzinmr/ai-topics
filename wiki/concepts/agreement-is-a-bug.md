---
title: Agreement is a Bug
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [agentic-engineering, controversy]
sources:
  - raw/articles/2026-03-19-claude-agents-disagree-experiment.md
---

# Agreement is a Bug

The thesis that consensus among AI agents can be a failure mode in multi-agent systems. When all agents converge on the same answer, the diversity benefit of multi-agent architecture is lost — agreement itself becomes a bug to detect and fix.

## Experiment

- Forced 11 Claude Code agents to disagree with each other
- Purpose: extract diverse perspectives, avoid groupthink
- Demonstrates that sycophancy (agents agreeing with each other/the user) is a systemic risk

## Connection to Sycophancy

Agreement as a bug connects directly to [[ai-sycophancy]] — the tendency of LLMs to produce agreeable rather than correct outputs. In multi-agent systems, this compounds: if Agent A has a sycophantic tendency, Agent B will amplify it, creating consensus on incorrect answers.

## Implications for Multi-Agent Systems

1. **Diversity as Signal:** Disagreement is valuable information, not noise
2. **Pareto Frontiers:** Connects to [[gepa]] which uses disagreement/pareto optimality as an optimization signal
3. **Agent Architecture:** Requires deliberate mechanisms to prevent convergence (temperature variation, different system prompts, adversarial roles)

## Related

- [[ai-sycophancy]]
- [[gepa]]
- [[agent-swarms]]
- [[agentic-conflict-resolution]]
- [[multi-agent-systems]]
