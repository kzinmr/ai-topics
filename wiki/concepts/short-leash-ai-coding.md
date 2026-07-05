---
title: "Short Leash AI Coding"
created: 2026-07-05
updated: 2026-07-05
type: concept
tags: [ai-coding, coding-agents, human-in-the-loop, code-quality, vibe-coding, code-review]
sources: [raw/articles/2026-07-02_okturtles_short-leash-ai-coding.md]
---

# Short Leash AI Coding

The **Short Leash** method is a 12-principle approach to [[concepts/coding-agents/ai-coding-reliability]] that keeps the AI coding agent on a tight, incremental workflow with continuous [[concepts/human-in-the-loop]] review at every step. Developed by the okTurtles team (Greg Slepak / taoeffect) and published in July 2026, it is a direct response to AI [[concepts/coding-agents/coding-agents]] going "off the rails" during extended sessions and the rise of [[concepts/vibe-coding]] — where multiple agents run in parallel with little to no human oversight, producing slop.

## Overview

The method treats the AI as a junior developer who needs constant supervision. Instead of delegating large tasks and walking away, the developer stays present, issues small, tightly-scoped instructions, reviews every proposed diff via permission prompts, and commits after each subtask. The "leash" metaphor is literal: diff permission prompts act as the leash, keeping the AI constrained and the developer's mental model current.

The method was informed by direct experience with Fable 5 producing inefficient, ugly code in niche domains where training data is sparse, demonstrating that even frontier models need guardrails in [[concepts/code-review]].

## The 12 Principles

1. **Planning phase**: Research the task, formulate a plan, and use a task tracker to break the work into discrete steps before any code is written.

2. **Never use YOLO mode**: Do not enable "dangerously skip permissions" or any equivalent that bypasses the approval gate. Every change must go through review.

3. **AI never works while you're away**: Contrary to popular YouTuber trends, do not let the AI code unsupervised while you do something else. Stay present.

4. **Use a coding agent that shows diffs**: Choose a tool that surfaces proposed changes via permission prompts with clear, reviewable diffs.

5. **Actually analyze proposed changes**: Sit there and review every diff. Passive approval defeats the method.

6. **Keep yourself in the loop at all times**: Maintain continuous awareness of what the AI is doing. This is the opposite of "set it and forget it."

7. **Use diff permissions as a leash**: The permission prompt is not a speed bump — it is the primary mechanism that keeps your understanding of the codebase current and the AI working within bounds.

8. **DENY permissions proactively**: Any time the AI is about to do something unwanted, reject the change immediately. This prevents cascading errors from early missteps.

9. **Intervene frequently**: Correct the AI's course before it goes off the rails. Frequent, small interventions are cheaper than fixing large tangents.

10. **AI is always "kept on a short leash"**: The instruction-to-review cycle should be tight. Hand off small pieces of work and validate each one before continuing.

11. **Commit after every subtask**: Version control checkpoints protect against the AI accidentally deleting or overwriting previous work. Each commit is an undo point.

12. **Review phase**: Both human and AI review every change. Neither is sufficient alone — the human catches high-level architectural issues, while the AI catches mechanical errors.

## Contrast with Vibe Engineering

| Dimension | Short Leash | Vibe Engineering |
|---|---|---|
| **Agent count** | Single agent, serial workflow | Multiple agents in parallel |
| **Human oversight** | Continuous, at every diff | Minimal or none |
| **Task granularity** | Small, incremental subtasks | Large, loosely defined goals |
| **Commit strategy** | Commit after every subtask | Often ad-hoc or deferred |
| **Code quality** | Reviewed at each step | Variable; prone to slop |
| **Developer awareness** | High — developer stays current | Low — developer may be unaware of what was produced |
| **Risk profile** | Low derailment risk | High derailment risk |

The Short Leash method is positioned as a deliberate rejection of [[concepts/vibe-coding]] trends, arguing that the productivity gains of unattended parallel agents are offset by the cost of reviewing, debugging, and rewriting low-quality output.

## AI Review Protocol

The okTurtles post also defines a specific review protocol for AI-assisted pull requests:

- **Dual review required**: Every PR must be reviewed by both a human reviewer and an AI reviewer. The combination is stronger than either alone — the AI acts as a "linter" catching common mistakes, while the human catches high-level design and architectural issues.
- **AI Disclosure heading**: Every PR description must include an `## AI Disclosure` section listing the exact models used (e.g., "Fable 5, Claude Code").
- **Author self-review**: The PR author must review their own AI-assisted PR line-by-line before submitting it for external review. This ensures the author takes full responsibility for AI-generated code and maintains [[concepts/coding-agents/ai-code-quality]].

## Related Pages

- [[concepts/coding-agents/ai-coding-reliability]] — AI-assisted coding techniques and paradigms
- [[concepts/coding-agents/coding-agents]] — AI agents designed for software engineering tasks
- [[concepts/human-in-the-loop]] — Design pattern where humans remain in the decision cycle
- [[concepts/vibe-coding]] — Unsupervised, parallel-agent coding approach that Short Leash opposes
- [[concepts/code-review]] — Practices and tools for reviewing code changes
- [[concepts/coding-agents/ai-code-quality]] — Standards and metrics for code quality in AI-assisted development
