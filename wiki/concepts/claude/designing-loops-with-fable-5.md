---
title: "Designing loops with Fable 5"
type: concept
slug: designing-loops-with-fable-5
status: complete
tags:
  - claude-fable-5
  - loops
  - self-correction
  - memory
  - anthropic
  - agent-harness
  - context-engineering
  - eval-loops
  - agent-loop
  - managed-agents
  - claude-code
created: 2026-06-09
updated: 2026-06-09
aliases: [fable-5 loops, self-correction loops, memory loops, designing loops]
sources:
  - raw/articles/2026-06-09_rlancemartin_designing-loops-with-fable-5.md
  - raw/articles/2026-06-09_eliebakouch_fable-5-mythos-debated-research.md
  - https://x.com/rlancemartin/status/2064397389189071163
---

# Designing loops with Fable 5

> **Definition:** A design pattern for maximizing Claude Fable 5's capabilities through self-correction loops and memory-managed sessions, where the model improves by iterating on environment feedback rather than direct prompting.

## Overview

Lance Martin's June 2026 X article "Designing loops with Fable 5" articulates two core patterns for getting the most out of Mythos-class models like Claude Fable 5. Rather than directly prompting and steering the model, Martin advocates for **designing loops** that let the model self-correct in response to environment feedback and manage its own context via memory.

## Core Patterns

### 1. Self-Correction Loops

Self-correction loops leverage the model's ability to iterate on feedback. The key insight: **a well-designed goal or rubric adds feedback to the environment that Claude is running in**, enabling it to run, collect feedback, self-correct, and proceed until satisfied.

**Primitives:**
- **`/goal` in Claude Code**: Provides a goal that Claude can iterate toward
- **Outcomes in Claude Managed Agents**: Defines success criteria that spawn a grader sub-agent

**Key finding:** A **verifier sub-agent** outperforms self-critique because grading happens in an independent context window. This avoids the well-known problem where models struggle to critique their own outputs.

### 2. Memory as Outer Loop

Memory creates an outer loop that spans across sessions. Claude writes to memory during a session, and those memories can be retrieved in future sessions.

**Memory Progression (optimal pattern):**
1. **Fail** — Get something wrong and document it
2. **Investigate** — Before moving on, figure out why
3. **Verify** — Turn the diagnosis into a checked fact
4. **Distill** — Turn verification into a general rule
5. **Consult** — Read the rule instead of re-deriving it

## Model Comparison (Parameter Golf Benchmark)

Martin tested Fable 5 against Opus 4.7 on **Parameter Golf** — an open-source ML engineering challenge to train the best model in a 16MB artifact in <10 minutes on 8xH100s.

| Model | Behavior | Result |
|-------|----------|--------|
| **Fable 5** | Bet on larger structural changes (architecture, quantization), showed resilience through regressions | ~6x more improvement than Opus 4.7 |
| **Opus 4.7** | First experiment produced a small win, then followed the same template: adjust scalar → measure → keep if positive | Incremental improvements only |

## Memory Comparison (Continual Learning Bench 1.0)

Martin tested memory capabilities on a sequential SQL question-answering task from Continual Learning Bench 1.0.

| Model | Memory Progression | Verification Coverage |
|-------|-------------------|----------------------|
| **Sonnet 4.6** | Exits at step 1: stores failure notes and open guesses, rarely consults prior notes | Low (task-specific instructions needed) |
| **Opus 4.7** | Exits at step 3: creates schema reference with uncertainty flagged | 7-33% (median ~17%) |
| **Fable 5** | Completes full progression: distills learnings into general rules | Up to 73% (22 of 30 questions) |

## Design Principles

1. **Environment feedback over direct prompting**: Design loops that let the model self-correct rather than trying to steer it with detailed instructions
2. **Independent verification**: Use verifier sub-agents instead of self-critique
3. **Memory progression**: Encourage the full fail → investigate → verify → distill → consult cycle
4. **Goal/rubric design**: Well-designed success criteria are more effective than detailed step-by-step instructions

## Implementation

### Claude Code
- Use `/goal` to define success criteria
- Claude iterates toward the goal, collecting feedback from the environment

### Claude Managed Agents (CMA)
- Define **Outcomes** — success criteria that spawn a grader sub-agent
- Use **self-hosted sandboxes** for long-running tasks with GPU access
- Enable **memory** via mounted filesystem shared across sessions

## Community Response

The Fable 5 announcement and Martin's design patterns article generated significant community discussion:

### Capability Limitation Critique
[[entities/elie-bakouch|Elie Bakouch]] (Prime Intellect) raised a fundamental concern about Fable 5's deployment: Mythos-class models are **deliberately weakened on "frontier LLM research" tasks**, and this restriction is **not visible to end users**. This creates a tension between:
- Martin's design patterns (which assume full model capability for loops and memory)
- Anthropic's safety-driven restrictions (which may limit the model's effectiveness on certain research tasks)

The critique (3,800+ likes, 1.2M impressions) highlights that the design patterns described here may operate within a capability envelope that is intentionally constrained — users cannot distinguish between "model can't do this" and "model is restricted from doing this."

### Design Pattern Adoption
Martin's article was well-received by the agent engineering community, with the self-correction loop pattern and memory progression framework becoming reference material for Claude Code and Managed Agents users.

## Related Concepts

- [[concepts/harness-engineering/agentic-loop]] — The canonical agent execution pattern that loops build upon
- [[concepts/eval-loops]] — Evaluation-driven improvement cycles
- [[concepts/context-engineering|Context Engineering]] — The broader discipline of managing agent context
- [[concepts/anthropic/managed-agents]] — The platform that implements these loop patterns
- [[concepts/agent-loop-orchestration]] — Patterns for orchestrating multiple loops
- [[entities/rlancemartin]] — Author of the original article
- [[concepts/claude/fable-5]] — The model these patterns are designed for
- [[entities/elie-bakouch]] — Critic of capability limitation transparency

## References

- [Designing loops with Fable 5 (X Article)](https://x.com/rlancemartin/status/2064397389189071163)
- [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- [Claude Managed Agents](https://www.anthropic.com/engineering/managed-agents)
- [Define Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)
- [Memory](https://platform.claude.com/docs/en/managed-agents/memory)
- [Parameter Golf](https://github.com/openai/parameter-golf)
- [Autoresearch](https://github.com/karpathy/autoresearch)
- [Claude Code /goal](https://code.claude.com/docs/en/goal)
