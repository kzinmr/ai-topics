---
title: "Hoard Things You Know How to Do"
type: concept
aliases:
  - hoard-things-you-know
  - knowledge-hoarding
  - knowledge-repository
created: 2026-04-13
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
  - information-retrieval
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know/"
---

# Hoard Things You Know How to Do

The concept of **hoarding and reusing knowledge** as proposed by Simon Willison. In the agent era, recording and accumulating what you "know how to do" becomes a powerful weapon.

## Core Principle

> "Hoard things you know how to do. The more you know how to do, the more you can recombine into new solutions."

By accumulating **concrete implementation methods** as knowledge, developers improve the precision and speed of giving instructions to agents.

## Types of Knowledge

### 1. Implementation Patterns
- Best practices for specific tech stacks
- Solutions to common problems
- Library/API usage

### 2. Configuration & Environment Setup
- Development environment setup procedures
- Optimal tool configurations
- Deployment pipelines

### 3. Debugging Techniques
- Troubleshooting specific errors
- Performance optimization techniques
- Finding security vulnerabilities

## Value in the Agent Era

### Why Hoard "Things You Know"

1. **Improved Instruction Precision**
   - Give specific, accurate instructions to agents
   - Tacit knowledge ("that way") becomes explicit

2. **Quality Judgment**
   - Can judge whether agent output is correct
   - Avoid cognitive debt (see [[concepts/anti-patterns]])

3. **Power of Recombination**
   - Combine different knowledge to create new solutions
   - Insights that agents alone cannot reach

## Practical Methods

### Recording Knowledge
- **Blog posts**: Document what you've learned
- **Code snippets**: Reusable code fragments
- **Config files**: Environment setup templates
- **Checklists**: QA items

### Organizing Knowledge
- Tagging and categorization
- Storing in searchable formats
- Regular updates and deletion of stale knowledge

## Willison's Practice

Willison uses knowledge cultivated across diverse projects (Datasette, sqlite-utils, llm, etc.):
- Published as blog posts
- Saved as code in GitHub repositories
- Implemented and shared as tools

These form the **foundation of his agentic engineering** practice.

## Related Concepts

- [[concepts/cognitive-debt]] — Merging code without understanding creates debt
- [[concepts/anti-patterns]] — Knowledge gaps breed anti-patterns
- [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — The compounding knowledge growth cycle
- [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] — Knowledge determines prompt quality

## References

- [[entities/simon-willison]] — Originator of the concept
- [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know/)
