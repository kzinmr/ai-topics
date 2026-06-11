---
title: "code-review"
type: concept
aliases:
  - code-review
created: 2026-04-25
updated: 2026-05-29
tags:
  - concept
  - coding-agents
  - developer-tooling
  - agent-native
status: active
sources:
  - raw/articles/linear.app--code-review-should-be-fast--2026-05-28.md
  - https://linear.app/now/code-review-should-be-fast
---

# Code Review in the Agent Era

Code review is the practice of inspecting code changes before merging them into a codebase. With the rise of AI coding agents generating increasing volumes of pull requests, code review is undergoing a transformation — shifting from line-by-line correctness checking to architectural judgment and problem-fit evaluation.

## Traditional Code Review
- Manual inspection of diffs for bugs, style, and design
- Often bottlenecked by reviewer availability and attention span
- Tools: GitHub PR review, GitLab MR review, Gerrit, Phabricator

## The Agent Era Shift

AI coding agents (Claude Code, Codex, Cursor) now handle much of the line-by-line correctness work. This shifts the reviewer's job to:
1. **Architectural fit**: Does this change fit the system's design?
2. **Problem validation**: Does it solve the problem the customer actually reported?
3. **Judgment work**: The layer above the code itself

As [[entities/linear|Linear]]'s Diffs announcement puts it: "the speed gained from using agents gets swallowed in review."

## Key Innovations

### Linear Diffs (May 2026)
[[entities/linear|Linear]] launched Diffs, a code review experience built directly into the Linear workspace:
- **Guided reviews**: Diffs broken into chapters following the work's reasoning order
- **Structural diff highlighting**: Strips formatting-only changes
- **Integrated context**: Issue, project, and customer signal alongside the diff
- **Priority-aware queue**: Reviews compete with other tasks in Linear's priority system

### Code Review Agents
AI-assisted code review tools that automatically analyze PRs for:
- Security vulnerabilities
- Performance issues
- Style violations
- Test coverage gaps
See [[concepts/coding-agents/code-review-agents]]

## Related Pages
- [[entities/linear]] — Linear Diffs brings code review into the Linear workspace
- [[concepts/coding-agents/code-review-agents]] — AI-powered automated code review
- [[concepts/linear-agent-code-intelligence]] — Linear's codebase-aware AI agent
- [[concepts/programmatic-tool-calling]] — Code execution in agent contexts
