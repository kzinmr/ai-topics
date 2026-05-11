---
title: "Open SWE: An Open-Source Framework for Internal Coding Agents"
source: "LangChain Blog"
date: 2026-03-17
scraped: 2026-05-11
type: blog
url: https://blog.langchain.com/open-swe-an-open-source-framework-for-internal-coding-agents/
authors: ["LangChain Team"]
tags: [coding-agents, langchain, agent-harness, open-source, agent-architecture]
---

# Open SWE: An Open-Source Framework for Internal Coding Agents

**Source**: LangChain Blog
**Date**: 2026-03-17
**URL**: https://blog.langchain.com/open-swe-an-open-source-framework-for-internal-coding-agents/
**GitHub**: https://github.com/langchain-ai/open-swe

## Summary

Over the past year, several engineering organizations built internal coding agents that operate alongside their development teams. Stripe developed Minions, Ramp built Inspect, and Coinbase created Cloudbot. These systems integrate into existing workflows (Slack, Linear, GitHub) rather than requiring engineers to adopt new interfaces.

While developed independently, they converged on similar architectural patterns: isolated cloud sandboxes, curated toolsets, subagent orchestration, and integration with developer workflows.

Open SWE is LangChain's open-source framework capturing these patterns, built on Deep Agents and LangGraph.

## Patterns from Production Deployments

1. **Isolated execution environments**: Tasks run in dedicated cloud sandboxes with full permissions inside strict boundaries. Isolates blast radius from production.
2. **Curated toolsets**: Stripe's agents have ~500 tools, carefully selected and maintained. Tool curation matters more than quantity.
3. **Slack-first invocation**: All three systems integrate with Slack as primary interface, meeting developers in existing workflows.
4. **Rich context at startup**: Pull full context from Linear issues, Slack threads, or GitHub PRs before beginning work.
5. **Subagent orchestration**: Complex tasks decomposed and delegated to specialized child agents with isolated context.

## Open SWE Architecture

### 1. Agent Harness — Composed on Deep Agents
Rather than forking, Open SWE composes on Deep Agents. Similar to how Ramp built Inspect on OpenCode. Advantages: upgrade path (Deep Agents improvements propagate), customization without forking.

### 2. Sandbox Infrastructure
Dedicated cloud sandboxes provisioned per-task via LangSmith Sandboxes. Full Linux environment with sudo, network, git. Blast radius contained. Post-task teardown.

### 3. Tool Integration
- Linear integration (read issues, post comments)
- Slack integration (thread replies, mentions)
- GitHub integration (clone, branch, commit, PR)
- File system tools (read, write, edit, search, execute)

### 4. Context Engineering — AGENTS.md + Source Context
- AGENTS.md at repo root read from sandbox and injected into system prompt — equivalent to Stripe's rule files
- Full Linear issue or Slack thread assembled and passed to agent for rich startup context

### 5. Middleware for Reliability
Deterministic safety nets around the agentic loop: ToolErrorMiddleware, message queue checking before model invocation, ensuring PRs get opened even if the LLM "forgets."

## Getting Started
- GitHub: github.com/langchain-ai/open-swe
- Built on: Deep Agents (docs.langchain.com/oss/python/deepagents)
- Sandboxes: LangSmith Sandboxes (waitlist)

## Related
- [[concepts/open-swe]]
- [[entities/langchain]]
- [[concepts/deep-agents]]
- [[concepts/coding-agents]]
