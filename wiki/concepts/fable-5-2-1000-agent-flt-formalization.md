---
title: "Fable 5.2 1,000-Agent Team FLT Formalization"
type: concept
created: 2026-11-13
updated: 2026-11-27
tags:
  - ai-agents
  - multi-agent
  - anthropic
  - safety
sources:
  - "raw/articles/claude.dev--safely-scaling-multi-agent-teams-with-claude-fable--5b21667c.md"
  - "https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/"
  - "raw/articles/2026-11-25_ai-engineer_lance-martin-1000-claude-agents-fermat.md"
related:
  - "[[concepts/claude/fable-5]]"
  - "[[concepts/claude/fable-safety-classifiers-critique]]"
  - "[[concepts/claude-fable-jacobian-conjecture]]"
  - "[[concepts/multi-agents/multi-agent-systems]]"
---

# Fable 5.2 1,000-Agent Team FLT Formalization

Anthropic's November 2026 toy experiment (published on claude.dev): **1,000 agents
running an early version of Claude Fable 5.2 reproduced a formal Lean proof of Fermat's
Last Theorem** with no Prove2Me platform and no researcher steering — using only
general-purpose tools (shell, editor, Git, a shared Postgres DB) inside layered safety
controls.

## Comparison with the September Formalization

| | Sept 2026 (Fable 5.1-class) | Nov 2026 (early Fable 5.2) |
|---|---|---|
| Team | dozens of agents + 1 researcher | 1,000 agents, no researcher |
| Scaffolding | Prove2Me shared proof graph | general tools: Git + shared Postgres |
| Duration | 11 days | **28.7 hours** |
| Output tokens | ~6B | **1/3 of original** |
| Proof size | 13M lines of Lean | **1/7 the length** |

Inputs given: 60 statements (theorem + 59 milestones), a one-sentence sketch of the
classical route, definitions, 47 previously proved lemmas, and a lead/helper role
assignment. No other guidance on proving or self-organization.

## Coordination Without Scaffolding

Without Prove2Me, the team **built its own coordination system**: agents claimed tasks,
shared notes, and logged finished work in the shared SQL DB (chosen for transactional
concurrency from 1,000 writers and Claude's familiarity); work flowed through personal Git
branches + merge requests, with a separate job merging to main. Each agent ran on its own
lightweight VM — a single shared machine hit its limits at ~100 agents. Only structure:
one lead + 999 helpers; the lead split problems and assigned; the harness sent the lead 19
time-remaining reminders.

## Safety Architecture (3 layers)

1. **Sandboxing**: no network (single pipe to a gateway), kernel lockdown, no loadable
   modules/kexec/raw memory, unprivileged user, no sudo, agents can't touch their own
   agent loop, DB under shared unprivileged role with 5s statement limit / 256 MiB write
   cap, push only to own branch.
2. **Real-time monitoring**: prompted LLM classifier checks every shell command and file
   edit pre-execution; a block halts the whole team pending human review. Red-team
   sabotage evals (decomposition attacks) were all caught by CoT+interagent-communication
   monitors; this run used the action-based monitor only.
3. **Offline monitoring**: post-hoc analysis with cross-agent action lookup.

Across 1M+ tool calls, **zero met the block bar**; replay against the CoT monitor and
today's rubric flagged only one near-miss (a root-access check). Experiments run on models
that may not have completed pre-release alignment assessment, so monitoring assumes
possible misalignment.

## Significance

- Demonstrates ambitious long-horizon multi-agent work **inside carefully designed safety
  boundaries** — the flagship use case for Fable 5.2's Orchestrator positioning
  ([[concepts/claude/fable-5]]).
- The coordination substrate shifted from a bespoke math platform (Prove2Me) to
  **commodity infrastructure** (SQL + Git): an agent-team bitter-lesson data point.
- Connects to the Formalizing Fermat workshop thread and the Jacobian conjecture
  discovery ([[concepts/claude-fable-jacobian-conjecture]]).

## Lance Martin's AI Engineer talk elaboration (Nov 25, 2026)

Lance Martin ([[entities/lance-martin]]) presented the result live at AI Engineer with additional detail (transcript: `raw/articles/2026-11-25_ai-engineer_lance-martin-1000-claude-agents-fermat.md`): each of the 1,000 agents ran in its own sandbox with restricted network access to exactly **two endpoints — Git and the SQL database**; real-time monitoring inspected every tool call for escapes, offline monitoring re-examined all runs every 10 minutes. Prompting was minimal: one lead + 999 helpers, awareness of Git/DB, and the problem statement. Within ~5 minutes the lead had created the orchestration schema itself — an *announcements* table (global broadcasts), *roles* (worker assignment across the proof's 60 statements), *notes/subtasks* (progress sharing), and *landed* (merged Lean code) — none of it specified. Runs lasted ~30 hours; on hard sub-problems (e.g., a Lagrange-related task tree) agents **invented their own abstractions** and reallocated themselves as statements closed. One agent note read: "total freeze of the origin, effective now, magnificent work all 999 of you."

## See Also

- [[concepts/claude/fable-5]] — model release context (FLT "formalized in 30 hours" claim)
- [[concepts/claude/fable-safety-classifiers-critique]] — external critique of classifiers
- [[concepts/multi-agents/multi-agent-systems]] — general multi-agent patterns
