---
title: "Prompt-Driven Development"
type: concept
aliases:
  - prompt-driven-development
  - prompt-driven-design
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - methodology
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/#prompt-driven-development"
---

# Prompt-Driven Development

A **prompt-centered software development methodology** advocated by Simon Willison. A workflow where detailed specifications are written as prompts for AI coding agents, which then implement them.

## Core Principle

> "You write a prompt describing what you want, the agent implements it, you review the implementation, and iterate."

It transforms the traditional "write code, then test" cycle into a "write prompts, then review" cycle.

## 5 Key Steps

### 1. Write Detailed Prompts
Describe what you want implemented **clearly and specifically**. Characteristics of good prompts:
- Clarify goals and constraints
- Specify expected output format
- Mention edge cases

### 2. Agent Implementation
Input the prompt into agents like Claude Code, Cursor, or GitHub Copilot to generate code.

### 3. Review Implementation
**Carefully review** the generated code. This is where the concept of [[concepts/cognitive-debt]] becomes critical — never merge code you don't understand.

### 4. Feedback and Iteration
Based on review results, revise and refine the prompt, then have the agent implement again.

### 5. Test and Verify
Verify the final implementation meets specifications using the existing test suite.

## Comparison with Traditional Development

| Dimension | Traditional Development | Prompt-Driven Development |
|------|-----------|---------------------------|
| Starting point | Code specification | Prompt text |
| Implementer | Developer | AI agent |
| Review | PR review | Prompt refinement + code review |
| Iteration | Code fixes | Prompt improvements |
| Quality assurance | Tests | Tests + prompt clarity |

## Relationship to Cognitive Debt

> "If you don't understand the code the agent wrote, you've incurred cognitive debt."

In Prompt-Driven Development, **merging agent-generated code without understanding it creates significant debt** for future maintenance. Willison recommends:
1. Iterate in small steps
2. Review code every time
3. Ask the agent to explain unclear parts

## Practical Tips

### Prompt Design Patterns
- **Function unit**: 1 feature = 1 prompt
- **Gradual refinement**: Framework → Details → Edge cases
- **Reference existing code**: Increase specificity with "refer to this function in this file"

### Effective Feedback
- ❌ "It doesn't work" → ✅ "Here's the error with this input"
- ❌ "Make it better" → ✅ "Improve this specific part like this"
- ❌ "Write tests" → ✅ "Write pytest tests for normal and edge cases of this function"

## Related Concepts

- [[concepts/cognitive-debt]] — The accumulated debt from merging code you don't understand
- [[concepts/red-green-tdd]] — Combining with test-driven development
- [[concepts/context-window-management]] — Managing prompt length
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept

## References

- [[entities/simon-willison]] — Proponent
- [Agentic Engineering Patterns — Prompt-Driven Development](https://simonwillison.net/guides/agentic-engineering-patterns/#prompt-driven-development)
