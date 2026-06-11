---
title: "AGENTS.md Evaluation — Do Context Files Help Coding Agents?"
created: 2026-06-08
updated: 2026-06-08
type: concept
tags: [coding-agents, context-engineering, evaluation, benchmark, swere-bench, agents-md]
aliases: ["AGENTS.md evaluation", "Evaluating AGENTS.md paper", "AGENTBENCH"]
sources: [raw/articles/2026-06-07_karpathy-do-agents-md-help.md, https://arxiv.org/abs/2602.11988]
related: [[concepts/claude-md-rules]], [[concepts/context-engineering|Context Engineering]], [[concepts/agent-skills]], [[entities/andrej-karpathy]]
---

# AGENTS.md Evaluation — Do Context Files Help Coding Agents?

> **Paper:** "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" (arXiv:2602.11988). Reviewed by [[entities/andrej-karpathy|Andrej Karpathy]] in a June 2026 X Article.

The paper evaluates whether repository-level instruction files — `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` — actually improve coding agent performance, or whether the agent harness generates equivalent context on the fly.

## Key Findings

| Finding | Detail | Surprise Level |
|---------|--------|---------------|
| **LLM-generated context files don't help** | Compared to no context file, LLM-generated context files reduce task success slightly or make no difference on average | ★★★ |
| **Developer-written files are better** | Developer-written context files outperform LLM-generated ones — domain expertise matters | ★ |
| **No context file is cheapest** | Using no context files was cheaper AND more efficient in benchmarks | ★★★★★ |

The most surprising result: **no context file was the most cost-efficient condition**, contradicting the intuition that context files reduce token waste by front-loading instructions.

## Experiment Design

### Two Evaluation Settings

1. **SWE-bench Lite**: Authors generate context files because original repos lack developer-written ones. Tests the gap between LLM-generated context and no context.

2. **AGENTBENCH** (new benchmark): 138 Python tasks from 12 repositories that ALREADY have developer-provided context files. Three conditions tested:
   - No context file
   - LLM-generated context file
   - Developer-written context file (where available)

## Interpretation

Karpathy's synthesis: The agent harness itself generates necessary context information on the fly during task execution. Context files are primarily about **efficiency between independent sessions**, not about improving per-task success rates.

This implies a **two-axis model** for context files:

| Axis | Context File Value | When It Matters |
|------|-------------------|----------------|
| **Per-task accuracy** | Low (agent generates context dynamically) | Single-shot coding tasks |
| **Cross-session efficiency** | High (avoids re-deriving conventions) | Multi-session development workflows |

## Practical Implications

1. **For single-shot tasks**: Skip context files — the agent figures it out
2. **For ongoing development**: Write developer-authored context files, not LLM-generated ones
3. **Cost optimization**: No context file is cheapest; context files add token overhead
4. **Quality matters**: Human-written context files beat LLM-generated ones — domain expertise is the differentiator

## Comparison: CLAUDE.md Rules vs AGENTS.md Evaluation

| Aspect | [[concepts/claude-md-rules]] | This Paper |
|--------|------------------------------|------------|
| **Focus** | Behavioral guardrails (simplicity, scope) | Instruction files (repo conventions, setup) |
| **Finding** | Rules reduce mistake rate 41% → 3% | Context files don't improve task success |
| **Cost** | Free (injected at session start) | Adds token overhead |
| **Key insight** | Behavioral constraints > feature checklists | Agent generates context dynamically |

These findings are **not contradictory** — they address different types of context files. CLAUDE.md rules are behavioral (how to work), while AGENTS.md files are instructional (what the codebase is about). The paper suggests the latter is what agents can figure out on their own.

## Graph Structure Query

```
[agents-md-evaluation] ──author──→ [[entities/andrej-karpathy]]
[agents-md-evaluation] ──contrasts──→ [[concepts/claude-md-rules]]
[agents-md-evaluation] ──relates-to──→ [[concepts/context-engineering|Context Engineering]]
[agents-md-evaluation] ──relates-to──→ [[concepts/agent-skills]]
[agents-md-evaluation] ──embodies──→ [[concepts/context-engineering|Context Engineering]]
```

## Related Concepts

- [[concepts/claude-md-rules]] — Karpathy's behavioral guidelines for coding agents (rules ≠ context)
- [[concepts/context-engineering|Context Engineering]] — The broader discipline of managing agent context
- [[concepts/agent-skills]] — Skills as an alternative to static context files
- [[concepts/evaluation-coding-agents]] — Coding agent evaluation benchmarks and methodologies

## Sources

- Karpathy, A. (2026). [Do AGENTS.md Files Actually Help Coding Agents?](https://x.com/i/article/2063647807437705216) — X Article
- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) — arXiv:2602.11988
