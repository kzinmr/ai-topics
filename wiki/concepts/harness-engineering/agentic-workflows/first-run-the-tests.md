---
title: "First Run the Tests"
type: concept
aliases:
  - first-run-the-tests
  - run-the-tests
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - methodology
  - testing
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/"
---

# First Run the Tests

The **first four-word prompt** to give a coding agent when handing over a project. Coined by Simon Willison as the minimal instruction to switch an agent into testing mindset.

## Definition

> "Any time I start a new session with an agent against an existing project I'll start by prompting a variant of the following: First run the tests"

For Python projects (`pyproject.toml` + `uv`):
```
Run "uv run pytest"
```

## Four Effects

### 1. Makes the Agent Aware of the Test Suite
> "It tells the agent that there is a test suite and forces it to figure out how to run the tests. This makes it almost certain that the agent will run the tests in the future to ensure it didn't break anything."

The agent internalizes that running tests is the expected behavior.

### 2. Proxy for Project Complexity
> "Most test harnesses will give the agent a rough indication of how many tests they are. This can act as a proxy for how large and complex the project is, and also hints that the agent should search the tests themselves if they want to learn more about the codebase."

More tests imply a larger, more complex codebase.

### 3. Switches to Testing Mindset
> "It puts the agent in a testing mindset. Having run the tests it's natural for it to then expand them with its own tests later on."

After running tests, the agent naturally starts adding its own tests.

### 4. Learns from Existing Tests
> "Tests are also a great tool to help get an agent up to speed with an existing codebase. Watch what happens when you ask Claude Code or similar about an existing feature - the chances are high that they'll find and read the relevant tests."

Agents tend to read tests to understand existing code.

## Why "Automated Tests Are No Longer Optional"

> "Automated tests are no longer optional when working with coding agents. The old excuses for not writing them - that they're time consuming and expensive to constantly rewrite while a codebase is rapidly evolving - no longer hold when an agent can knock them into shape in just a few minutes."

The traditional excuse that "writing tests takes time" no longer holds in the age of coding agents.

## Implementation Notes

- **No tests exist**: The agent must first build the test suite
- **Tests are broken**: First fix the tests (confirm Red state)
- **Test framework choice**: Use standard commands like `uv run pytest` or `npm test`

## Related Patterns

- [[concepts/red-green-tdd]] — Next step in the Red/Green cycle
- [[concepts/agentic-manual-testing]] — Manual exploratory testing after automated tests
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept

## References
- [[entities/simon-willison]] — Originator of this pattern
