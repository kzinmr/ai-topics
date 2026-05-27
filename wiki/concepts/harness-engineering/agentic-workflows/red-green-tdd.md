---
title: "Red/Green TDD"
type: concept
aliases:
  - red-green-tdd
  - test-driven-development
  - tdd
created: 2026-04-12
updated: 2026-05-27
tags:
  - concept
  - methodology
  - testing
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/"
---

# Red/Green TDD

A pattern for applying test-first development when working with coding agents. Core concept of Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/).

## Definition

> "Use red/green TDD" is a pleasingly succinct way to get better results out of a coding agent.

The strictest form of TDD (Test Driven Development):
1. **Red**: Write automated tests first, confirm they fail
2. **Green**: Iterate on implementation until tests pass

## Why It Works for Coding Agents

### Risk Reduction
Key risks for coding agents:
- **Writing non-functional code** → Tests catch this early through failure
- **Writing unnecessary code** → Tests force implementation of only needed functionality
- **Future regression** → Comprehensive test suite provides protection

### Importance of Failure Confirmation
> "It's important to confirm that the tests fail before implementing the code to make them pass. If you skip that step you risk building a test that passes already, hence failing to exercise and confirm your new implementation."

Without confirming that tests fail first, you risk testing existing behavior rather than exercising the new implementation.

## Implementation Patterns

### Concise Prompt
```
Build a Python function to extract headers from a markdown string. Use red/green TDD.
```

The four words "Use red/green TDD" encompass the much longer instruction:
> "use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass"

### Model Understanding
> "Every good model understands 'red/green TDD' as a shorthand for the much longer 'use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass'."

Major LLMs understand this shorthand and can apply the appropriate TDD workflow without detailed instructions.

## Martin Alderson: Agentic TDD Re-evaluation

Martin Alderson ([martinalderson.com](https://martinalderson.com/posts/turns-out-i-was-wrong-about-tdd/)) reversed his TDD skepticism after adopting coding agents. His experience validates the TDD pattern but adapts it for agent workflows:

### Key shifts with agents
- **E2E tests are too slow for agent loops** — browser-based tests and full infrastructure spins cause agents to waste cycles waiting and misinterpret screenshots
- **Prefer unit + integration tests (mocked infrastructure)** — agents can write these in seconds, and they provide tighter feedback loops
- **Testing plan before implementation** — Alderson asks agents to produce a testing plan *before* writing code, debating the approach upfront rather than strict TDD
- **Bug-driven test augmentation** — when encountering bugs, the agent explains *why* the test suite missed it, then adds specific test cases for that edge case
- **Review tests first** — when reviewing agent PRs, start with test files to verify the agent didn't "cheat" by removing/simplifying tests that block its desired implementation

> "Turns out the TDD folks were right all along. They just needed a mass-produced army of robotic junior devs to make it practical."

This confirms [[concepts/cognitive-cost-of-agents]] — agents shift the economic calculus of testing by making test creation near-free.

## Related Patterns

- [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] — A four-word prompt to run the test suite first as a precursor to TDD
- [[concepts/agentic-manual-testing]] — Manual exploratory testing after automated tests
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept
- [[concepts/cognitive-cost-of-agents]] — How agents change the economics of testing

## References
- [[entities/simon-willison]] — Creator of Agentic Engineering Patterns
- [[entities/martin-alderson]] — Agentic TDD re-evaluation, sysadmin with Claude Code
