---
title: "Anti-patterns in Agentic Engineering"
type: concept
aliases:
  - anti-patterns
  - agentic-anti-patterns
created: 2026-04-13
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/"
---

# Anti-patterns in Agentic Engineering

**Anti-patterns in coding agent usage** as warned by Simon Willison. The act of "inflicting unreviewed code" on others is a particularly serious problem.

## The Biggest Anti-pattern: Unreviewed Code Infliction

> "Don't file pull requests with code you haven't reviewed yourself."

Submitting PRs with hundreds to thousands of lines of agent-generated code **without reviewing them yourself**. This is effectively "delegating the actual work to others."

### Core of the Problem
- Reviewers are forced to do the verification work on behalf of the agent
- Developer's added value becomes zero
- Damages team trust and morale

## Characteristics of a Good PR

Features of **good agentic engineering PRs** as defined by Willison:

### 1. Confidence in Correctness
> "The code works, and you are confident that it works."

- Verify the code actually works yourself
- Be in a state where you can confidently say "it works"

### 2. Appropriate Change Size
> "Several small PRs beats one big one."

- Break into small changes
- Consider reviewer cognitive load
- Delegate Git operations to the agent for granular commits

### 3. Sufficient Context
> "Agents write convincing looking pull request descriptions. You need to review these too!"

- Explain the high-level purpose of the change
- Link to related issues or specifications
- Also verify the PR description written by the agent

### 4. Verification Evidence
> "Notes on how you manually tested it, comments on specific implementation choices or even screenshots and video of the feature working go a long way."

- Manual testing methods and results
- Comments on specific implementation choices
- Screenshots or videos of the feature working

## Relationship to Cognitive Debt

Anti-patterns immediately accumulate **cognitive debt**:
- Code that nobody understands gets merged
- Future maintenance and fixes become difficult
- Overall team productivity declines

## Prevention

### Developer Responsibilities
1. **Always read the code yourself** — Don't blindly trust agent output
2. **Run tests** — Never skip verification
3. **Make small changes** — Don't change large amounts of code at once
4. **Document context** — Explain why the change is needed

### Reviewer Rights
- Right to refuse reviewing unverified code
- Right to demand verification evidence
- Right to demand small, well-segmented PRs

## Related Concepts

- [[concepts/cognitive-debt]] — Accumulation of unverified code becomes cognitive debt
- [[concepts/red-green-tdd]] — TDD as an anti-pattern avoidance strategy
- [[concepts/agentic-manual-testing]] — Importance of manual testing
- [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] — Techniques for small atomic commits

## References

- [[entities/simon-willison]] — Originator of the concept
- [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
