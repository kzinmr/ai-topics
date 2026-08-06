---
title: Superpowers
type: entity
aliases: [superpowers-framework, obra-superpowers]
created: 2026-06-05
updated: 2026-08-06
status: L3
tags:
  - ai-agents
  - framework
  - harness-engineering
  - agent-design-patterns
  - open-source
  - coding-agents
  - testing
  - developer-tooling
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
  - https://github.com/obra/superpowers
  - https://blog.fsck.com/2025/10/09/superpowers/
---

# Superpowers

**Agent skills framework created by Jesse Vincent ([@obra](https://github.com/obra)), developed commercially by Prime Radiant Inc.** Superpowers provides a complete software development methodology for coding agents, built on composable skills and bootstrap instructions that make the agent use them. Used prominently by [[entities/wes-mckinney|Wes McKinney]] as the foundation of his agentic software factory.

## Overview

| | |
|---|---|
| **GitHub** | [obra/superpowers](https://github.com/obra/superpowers) |
| **Creator** | Jesse Vincent ([@obra](https://github.com/obra)) |
| **Maintainer** | Prime Radiant Inc (commercial support: sales@primeradiant.com) |
| **Type** | Agent skills framework + software development methodology |
| **License** | MIT |
| **Users** | Wes McKinney, and growing community |
| **Harnesses** | Claude Code, Antigravity, Codex App/CLI, Cursor, Factory Droid, Gemini CLI, GitHub Copilot CLI, Kimi Code, OpenCode, Pi |

## Core Design

### Progressive Disclosure

Skills reveal complexity only when needed. A skill has two visible fields (name + description) that are always in the agent's context. The full body is hidden until the agent invokes the skill.

### Thin Drivers

Minimal wrappers that call tools, not fat abstractions. The harness should be minimal; skills encode specific behaviors and judgments.

### Spec Interview

Superpowers runs a **long, detailed spec interview** before any code is written. The agent asks questions about scope, constraints, and architecture. The human answers and shapes the plan, then hands off to a sub-agent execution skill.

> *"One of the pros and cons of Superpowers is it generates amazing software, but it also takes a long time to generate very detailed implementation plans. The idea is that it doesn't really trust leaving that much up to the agent in terms of making decisions."* — Wes McKinney

## The Basic Workflow

Superpowers encodes a mandatory 7-step methodology — "the agent checks for relevant skills before any task; mandatory workflows, not suggestions":

1. **brainstorming** — Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.
2. **using-git-worktrees** — Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.
3. **writing-plans** — Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.
4. **subagent-driven-development** / **executing-plans** — Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.
5. **test-driven-development** — Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.
6. **requesting-code-review** — Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.
7. **finishing-a-development-branch** — Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

## Skills Library

**Testing**
- **test-driven-development** — RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**
- **systematic-debugging** — 4-phase root cause process (root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** — Ensure it's actually fixed

**Collaboration**
- **brainstorming** — Socratic design refinement
- **writing-plans** — Detailed implementation plans
- **executing-plans** — Batch execution with checkpoints
- **dispatching-parallel-agents** — Concurrent subagent workflows
- **requesting-code-review** — Pre-review checklist
- **receiving-code-review** — Responding to feedback
- **using-git-worktrees** — Parallel development branches
- **finishing-a-development-branch** — Merge/PR decision workflow
- **subagent-driven-development** — Fast iteration with two-stage review (spec compliance, then code quality)

**Meta**
- **writing-skills** — Create new skills following best practices (includes testing methodology)
- **using-superpowers** — Introduction to the skills system

## Philosophy

- **Test-Driven Development** — Write tests first, always
- **Systematic over ad-hoc** — Process over guessing
- **Complexity reduction** — Simplicity as primary goal
- **Evidence over claims** — Verify before declaring success

The methodology is deliberately opinionated: it "doesn't really trust leaving that much up to the agent" (McKinney), favoring a plan detailed enough for "an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow."

## McKinney's Usage

McKinney has used Superpowers to run **parallel spec interviews** across multiple git worktrees:

- **Single plan for 14 hours straight** with 45 tasks
- **4-5 projects in flight** simultaneously
- Spec interviews run in parallel while implementation grinds unattended

The structure makes parallel projects possible: a slow plan is something you can step into and out of while it's being formed, and a long implementation runs unattended.

### The Workflow

1. **Spec interview** — Answer agent's questions about scope and constraints
2. **Leave it planning** — Agent continues planning while you work on other things
3. **Implementation** — Sub-agent grinds for hours; you don't watch
4. **Ready to merge** — Check dashboard, fold RoboRev findings, merge what's clean

## Quote

> *"The difference between vibe coding and agentic engineering is planning, architecture, and caring about the output."* — Jesse Vincent, as quoted by Wes McKinney

## Ecosystem Notes

- Superpowers is installed per-harness; using multiple agents means installing separately for each.
- Available via official Claude plugin marketplace (`/plugin install superpowers@claude-plugins-official`) and the Codex plugin marketplace.
- The **superpowers-evals** repo (github.com/prime-radiant-inc/superpowers-evals) provides the `drill` eval harness for skill-behavior tests.
- Telemetry is minimal and optional: the visual companion loads a logo from the Prime Radiant website including the Superpowers version, with no project details. Disable via `SUPERPOWERS_DISABLE_TELEMETRY`.

## Related

- [[entities/wes-mckinney]] — Primary user
- [[entities/roborev]] — Review layer that validates Superpowers output
- [[concepts/agentic-engineering]] — The discipline Superpowers enables
- [[entities/randy-olson]] — Fellow agent-skills practitioner on Show Us Your Agent Skills Ep. 1
- [[entities/jeremiah-lowin]] — Skills-as-polite-notes framing

## References

- [GitHub: obra/superpowers](https://github.com/obra/superpowers)
- [Original release announcement](https://blog.fsck.com/2025/10/09/superpowers/) (fsck.com, Oct 2025)
- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial entity page created.
- **2026-08-06**: Enriched from GitHub README: 7-step workflow, skills library, philosophy, multi-harness support, Prime Radiant/ecosystem notes. Promoted L2→L3.
