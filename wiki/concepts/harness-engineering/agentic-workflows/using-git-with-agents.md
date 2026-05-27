---
title: "Using Git with Coding Agents"
type: concept
aliases:
  - using-git-with-agents
  - git-integration-patterns
created: 2026-04-12
updated: 2026-05-27
tags:
  - concept
  - agentic-engineering
  - developer-tooling
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/"
---

# Using Git with Coding Agents

Patterns for integrating Git with coding agents. Detailed in Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/).

## Core Philosophy

### Agent Fluency Over Memorization
> "Coding agents deeply understand Git jargon and operations. Developers don't need to memorize commands—just know what's possible and prompt accordingly."

Developers do not need to memorize Git commands — they just need to know **what is possible** and instruct the agent in natural language.

### History as a Curated Narrative
> "Don't think of the Git history as a permanent record of what actually happened - instead consider it to be a deliberately authored story that describes the progression of the software project."

Git history is not "a record of what actually happened" — think of it as a **deliberately authored narrative of the project's progression**.

### Zero-Risk Experimentation
> "Everything in Git can be undone. Agents safely handle complex operations (rebases, conflict resolution, history rewriting), making advanced Git accessible to all skill levels."

All Git operations are reversible. Agents can safely handle complex operations.

## Practical Prompt Library

| Prompt | Agent Action | Strategic Benefit |
|----------|-----------------|-------------|
| `Start a new Git repo here` | `git init` | Instant project start |
| `Commit these changes` | `git commit -m "..."` | Version snapshot |
| `Review changes made today` | `git log` | **Session context seeding** |
| `Sort out this git mess for me` | Merge conflict resolution, staging fixes | Automatic handling of complex Git errors |
| `Find and recover my code that does ...` | `reflog`, branch search, `git stash` search | Recovery of uncommitted work |
| `Use git bisect to find when this bug was introduced: ...` | Binary search through commits | Pinpoint bug origin |

## Context Seeding Pattern

> "Starting a session with `Review changes made today` loads the agent's context with recent work, enabling seamless continuation, targeted fixes, or next-step proposals."

Running `Review changes made today` at the start of a session lets the agent understand recent work, enabling continuous development.

## Democratizing git bisect

`git bisect`, which historically had a steep learning curve and was often avoided, has been transformed by agents into an on-demand debugging tool.

> "Agents handle the test-condition boilerplate, transforming it into an on-demand debugging tool."

## reflog as a Safety Net

> "Captures uncommitted/stashed changes. Agents can search it to recover work that wasn't formally committed."

`reflog` records uncommitted/stashed changes. Agents can search it to recover "lost" code.

## Advanced Operations: History Rewriting

### Commit Surgery
- Undo last commit: `git reset --soft HEAD~1`
- Delete specific files: fine-grained commit editing
- Squash commits and rewrite messages

> "I've found that frontier models usually have really good taste in commit messages. I've accepted that the quality they produce is generally good enough, and often even better than what I would have produced myself."

### Module Extraction
Agents can extract a module as an independent library while preserving original commit metadata.

## Related Concepts

- [[concepts/agentic-engineering]] — Parent concept
- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — How agents work internally
- [[concepts/harness-engineering/agentic-workflows/subagents]] — Multi-agent patterns
