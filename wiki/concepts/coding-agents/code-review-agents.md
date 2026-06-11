---
title: "Code Review Agents"
created: 2026-05-26
updated: 2026-05-26
type: concept
tags:
  - coding-agents
  - ai-agents
  - multi-agent
  - software-engineering
  - methodology
  - verification
aliases:
  - ai-code-review
  - multi-agent-code-review
  - agentic-code-review
related:
  - [[concepts/agentic-engineering]]
  - [[concepts/subagent-patterns]]
  - [[concepts/coding-agents/ai-coding-reliability]]
  - [[entities/nolan-lawson]]
  - [[entities/roborev]]
sources:
  - raw/articles/2026-05-25_nolanlawson_using-ai-to-write-better-code-slowly.md
  - raw/articles/2026-05-12_hugobowne_agentic-engineering-verification.md
description: "Using AI agents — individually or in parallel — to systematically find bugs, review code quality, and verify correctness in pull requests. Ranges from background daemons to multi-agent orchestrated review pipelines."
---

# Code Review Agents

**Code review agents** are AI-powered systems that systematically examine code changes for bugs, quality issues, security vulnerabilities, and architectural problems. They represent one of the most impactful applications of AI in software engineering — leveraging LLMs' ability to catch issues that human reviewers miss.

The practice ranges from simple background daemons ([[entities/roborev]]) reviewing every commit, to sophisticated **multi-agent parallel review pipelines** that cross-check multiple models against each other for near-zero false positive rates.

## Multi-Agent Parallel Review

The most advanced pattern, articulated by [[entities/nolan-lawson]] in May 2026: running **multiple bug-finding agents in parallel** on the same PR, then cross-checking results.

### Architecture

```
PR diff → ┬─ Claude sub-agent (custom bug definitions)
          ├─ Codex (OpenAI)
          └─ Cursor Bugbot
                ↓
         Main agent: cross-check, deduplicate, rank
                ↓
         Final report: critical/high/medium/low
```

### Key Principles

1. **Parallel independent agents** — Each agent reviews the PR independently with its own context. No inter-agent communication to prevent groupthink or bias.

2. **Custom bug definitions** — The orchestrating skill defines what "bug" means for the project (KISS/DRY violations, inaccessible HTML/JSX, missing SQL indexes, misleading comments, etc.)

3. **Context clearing** — The main orchestrating agent waits for ALL sub-agents to finish before doing its own analysis. This prevents anchoring bias where early results influence later judgment.

4. **Cross-validation** — Discrepancies between agents reveal hallucinations and false positives. An issue flagged by only one agent is suspect; issues flagged by multiple agents are highly reliable.

### False Positive Rate

> **Near zero.** Running multiple models against the same PR dramatically reduces false positives compared to single-model review.

The cost is that the review finds **so many bugs** that triaging becomes the bottleneck — not discovery.

## Workflow Patterns

### 1. Triage-First Review Cycle

```
1. Run parallel agents → bug report (critical/high/medium/low)
2. Fix all criticals + highs (developer-guided)
3. Re-run agents → verify fixes
4. Repeat until no criticals/highs remain
5. Skip mediums where fix effort > benefit
6. Abort PR if fundamental flaws emerge
```

### 2. Background Daemon (RoboRev Pattern)

[[entities/roborev]] (GPT-5.5) reviews every commit continuously as a background process. Used by [[entities/wes-mckinney]] to ensure every line of generated code is read by an agent 4-5 times before merge.

### 3. Comprehension Agents (Not Just Bug Finding)

Agents can also be used to **understand** a PR before merging:
- Ask the agent to explain how the PR works
- Generate Mermaid diagrams and documentation
- Use [[entities/matt-pocock]]'s `/grill-me` skill to interrogate the changes until fully understood

## Comparison with Other Approaches

| Approach | Agents | Review Depth | Speed | False Positives |
|----------|--------|-------------|-------|-----------------|
| Human-only review | 0 | Variable | Slow | Variable |
| Single-agent review | 1 | Good | Fast | Moderate |
| Background daemon (RoboRev) | 1 (continuous) | Good | Real-time | Moderate |
| **Multi-agent parallel** | **3+** | **Very deep** | **Moderate** | **Near zero** |
| Vibe coding | 1 (write only) | None | Very fast | N/A |

## Related Concepts

- [[concepts/agentic-engineering]] — The broader discipline of agent-driven software development, where code review agents are a core component
- [[concepts/subagent-patterns]] — The multi-agent parallel review is a concrete instantiation of the Inline Tool subagent pattern
- [[concepts/coding-agents/ai-coding-reliability]] — Addresses the reliability crisis that code review agents help mitigate
- [[concepts/generator-evaluator-workflow]] — Generator-evaluator architecture, of which code review agents are the evaluator side

## Key Practitioners

- **[[entities/nolan-lawson]]** — Pioneered the multi-agent parallel review pattern, author of "Using AI to Write Better Code More Slowly"
- **[[entities/wes-mckinney]]** — RoboRev background reviewer, 4-5x per-line review before merge
- **[[entities/randy-olson]]** — Verifier skills, Tufte-encoding for code quality rules
