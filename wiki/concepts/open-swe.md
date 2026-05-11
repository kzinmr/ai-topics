---
title: "Open SWE"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [coding-agents, langchain, agent-harness, open-source, agent-architecture, sandbox]
sources: [raw/articles/2026-03-17_langchain_open-swe-framework.md]
aliases: ["OpenSWE", "open-swe"]
---

# Open SWE

Open SWE is an open-source framework by LangChain for building internal coding agents that operate alongside development teams. Released March 2026, it distills architectural patterns observed across multiple production deployments — Stripe's Minions, Ramp's Inspect, and Coinbase's Cloudbot — into a customizable, MIT-licensed framework.

**GitHub**: [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe)
**Built on**: [Deep Agents](https://github.com/langchain-ai/deepagents) + [LangGraph](https://langchain-ai.github.io/langgraph/)

## Architectural Patterns (Convergent Design)

Three elite engineering orgs independently converged on the same architecture:

| Pattern | Description | Stripe | Ramp | Coinbase |
|---------|-------------|--------|------|----------|
| **Isolated sandboxes** | Tasks run in dedicated cloud VMs, full permissions, zero blast radius to prod | ✅ | ✅ | ✅ |
| **Curated toolsets** | ~500 tools, carefully selected and maintained, not accumulated | ✅ | ✅ | ✅ |
| **Slack-first invocation** | Engineers trigger agents from Slack, meeting them where they work | ✅ | ✅ | ✅ |
| **Rich context at startup** | Full Linear issue / Slack thread read before agent starts working | ✅ | ✅ | ✅ |
| **Subagent orchestration** | Complex tasks decomposed into child agents with isolated context | ✅ | ✅ | ✅ |

## Open SWE Architecture

### 1. Agent Harness — Composed on Deep Agents
Rather than forking an existing agent, Open SWE composes on Deep Agents (similar to Ramp building Inspect on OpenCode). Benefits:
- **Upgrade path**: Deep Agents improvements propagate automatically
- **Customization without forking**: Org-specific tools/prompts/workflows are configuration, not code modifications

### 2. Sandbox Infrastructure
Dedicated cloud sandboxes provisioned per-task via LangSmith Sandboxes. Full Linux environment with sudo, network, git. Post-task teardown.

### 3. Tool Integration
- Linear (read issues, post comments)
- Slack (thread replies, mentions)
- GitHub (clone, branch, commit, open PR)
- Filesystem (read, write, edit, search, execute)

### 4. Context Engineering — `AGENTS.md`
The repo-level `AGENTS.md` file is read from the sandbox and injected into the system prompt — equivalent to Stripe's rule files. This encodes conventions, testing requirements, and architectural decisions that every agent run follows. Combined with full Linear/Slack thread context at startup.

### 5. Middleware for Reliability
Deterministic safety nets around the agentic loop: `ToolErrorMiddleware`, message queue checking before model invocation, ensuring PRs get opened even if the LLM forgets.

## Significance

- **Open SWE is a validation that internal coding agent architectures have converged** — the design space is narrower than expected
- **The `AGENTS.md` pattern** is the simplest form of context engineering for coding agents
- **Entry cost has collapsed**: a year ago, building a production coding agent required significant infrastructure; now it's a weekend project
- **LangSmith Sandboxes** provide the cloud sandbox infrastructure that previously required custom DevOps

## Related

- [[entities/langchain]] — LangChain
- [[concepts/deep-agents]] — Deep Agents framework
- [[entities/inspect]] — Ramp's Inspect
- [[concepts/claude-md-rules]] — CLAUDE.md — analogous to AGENTS.md for Claude Code
- [[concepts/coding-agents]] — Coding agents overview
- [[concepts/agentic-engineering]] — Agent-centric engineering
