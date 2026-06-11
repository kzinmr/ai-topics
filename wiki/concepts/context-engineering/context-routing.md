---
title: "Context Routing — Query-Based Context Distribution"
type: concept
created: 2026-04-22
updated: 2026-05-27
tags: [concept, optimization, context-management]
status: active
sources:
  - "Vellum AI — Agentic Workflows in 2026 (Dec 2025)"
  - "https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns"
aliases:
  - context-routing
  - query-routing
  - context-dispatch
---
---

# Context Routing

> A pattern that classifies queries and routes them to the appropriate context source before loading into the context window.

**Summary:** Prevents multi-domain agents from loading irrelevant knowledge bases, tool sets, and instructions every time, improving token efficiency and accuracy.

## Problem

Multi-domain agents load knowledge, tool sets, and instructions from all domains for every query. This wastes context and causes attention fragmentation.

## Solution

Classify queries and send directly to the appropriate context source. This ensures only necessary information is loaded, keeping the context window minimal.

## Four Implementation Approaches

| Approach | Speed | Intelligence | Debuggability | Use Case |
|-----------|------|--------|-----------|--------|
| **Rule-Based** | Very Fast | Low | High | Fixed-category queries |
| **LLM Purge** | Slow | High | Low | Complex classification with edge cases |
| **Hierarchical** | Moderate | Moderate | Moderate | Lead agent → Sub-agent |
| **Hybrid** | Moderate | High | Moderate | Production default |

## Token Savings

- Context usage before routing: Typically 30-50% of information is irrelevant
- After routing: Only the minimum necessary context is loaded
- Agent response quality: Improves as noise from irrelevant information is removed

## Challenges

1. **LLM routing misclassification:** Misclassification loads the wrong context
2. **Additional layer overhead:** Routing itself consumes latency and tokens
3. **Dynamic domain handling:** New domains require routing rule updates

## Relationship with Harness Engineering

As a cross-cutting technique of [[concepts/context-engineering|Context Engineering]], Context Routing is a pattern that automates the design decision of "what to show the agent."

## Related Concepts

- [[concepts/context-engineering|Context Engineering]] — Integrated framework for context optimization
- [[concepts/context-engineering/context-compression|Context Compression]] — Context compression techniques
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — Advanced tool use
- [[concepts/agentic-rag]] — Agent-controlled search loops
