---
title: "Merge.dev"
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [company, testing, ai-agents, developer-tooling]
aliases: ["Merge"]
sources:
  - raw/articles/merge.dev--blog-testing-ai-agents--8daf268c.md
---

# Merge.dev

**URL:** https://merge.dev
**Blog:** merge.dev/blog
**Founded:** 2021
**Leadership:** Not publicly disclosed
**Key Products:** Unified API platform for integrations, AI agent testing tools
**Focus:** Testing infrastructure for AI agents, integration automation

## Overview

Merge.dev is an API integration platform that has expanded into **AI agent testing infrastructure**. Their recent blog posts focus on systematic approaches to testing AI agents, particularly around MCP server tool calls, non-deterministic LLM behavior, and agent evaluation methodologies.

## AI Agent Testing Contributions (May 2026)

Merge.dev published a comprehensive guide on **how to test AI agents effectively** with 5 key tips:

### 1. Measure Hit Rate
- **Hit rate**: percentage of times an agent calls the correct tool for a given scenario
- Define reference scenarios with expected tool calls
- Use semantic equivalence checking (not exact string matches)
- Reveals whether MCP server tools have exhaustive, appropriate names and descriptions

### 2. Track Pass/Fail Outcomes
- Define specific prompts and expected output labels
- Mark certain labels as passing, others as failing
- Example: "Website is down" → expected: "Create Jira issue, High Priority" = pass

### 3. Re-test After Model Changes
- Re-run all existing tests when underlying models change
- Newer models may phrase tool arguments differently or interpret instructions more loosely
- Identifies where certain models underperform (e.g., invoke wrong tools)

### 4. Test Multiple Models
- Test every LLM your agents might use
- Isolate potential issues by model
- Enable comparison across different model capabilities

### 5. MCP Server Testing
- Official MCP servers often deployed with gaps (missing/inconsistent tool metadata, weak auth)
- Test against projected prompts including edge cases, malformed inputs, permission constraints
- Include adversarial scenarios (e.g., prompt injection attempts)

## Related Concepts
- [[concepts/testing-ai-agents]] — Testing AI Agents: systematic evaluation methodologies
- [[concepts/mcp]] — Model Context Protocol standard
- [[concepts/agent-development-lifecycle]] — Agent development lifecycle

## References
- [How to test AI agents effectively (5 tips)](https://merge.dev/blog/testing-ai-agents) — May 2026
