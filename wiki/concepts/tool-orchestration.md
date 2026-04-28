---
title: "Tool Orchestration"
type: concept
tags: [tool-orchestration, mcp, function-calling, agent-tools]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Tool Orchestration, Tool Use, Agent Tool Orchestration]
related: [[concepts/agent-harness-primitives]], [[concepts/agent-communication-protocols]], [[concepts/cli-over-mcp-pattern]], [[concepts/agentic-scaffolding]]
sources: [https://modelcontextprotocol.io/, https://docs.anthropic.com/en/docs/agents-and-tools/]
---

# Tool Orchestration

## Summary

Tool orchestration is the architectural pattern governing how AI agents discover, select, invoke, and manage external tools and APIs. As agents have evolved from single-turn question-answer systems to multi-step autonomous workers, tool orchestration has become the central challenge — the agent must not only know which tool to use and when, but also handle errors, manage authentication, compose tool chains, and recover from failures. The 2025-2026 era has converged on MCP (Model Context Protocol) as the universal standard for agent-tool communication.

## Key Ideas

- **Tool Discovery & Selection**: The agent must find the right tool for a task from a potentially large tool catalog — this involves tool descriptions, parameter schemas, and relevance matching
- **Tool Composition (Chaining)**: Complex tasks often require multiple tool calls in sequence — the output of one tool becomes the input of another. The agent must plan and execute these chains without error propagation
- **Error Handling & Retry**: Tools fail — APIs time out, databases reject queries, files are missing. Robust tool orchestration includes retry logic, fallback strategies, and graceful degradation
- **MCP as Standard (2025-2026)**: The Model Context Protocol has emerged as the universal interface between agents and tools, replacing ad-hoc integrations. MCP servers expose tools via a standardized protocol with authentication, streaming, and error reporting
- **CLI Over MCP**: A design philosophy that standard Unix CLI tools, wrapped in MCP servers, are superior to custom API tools — leveraging decades of battle-tested command-line interfaces
- **Tool Safety & Guardrails**: Not all tools should be available to all agents — tool orchestration includes authorization checks, rate limiting, input validation, and output sanitization

## Terminology

- **MCP (Model Context Protocol)**: Anthropic-originated protocol standardizing agent-tool communication — tools are exposed as MCP servers with discoverable capabilities
- **Tool Schema**: Structured description of a tool's parameters, return types, and expected behavior — used by the LLM to understand how to invoke the tool
- **Tool Chain**: A sequence of dependent tool calls where each step consumes the output of the previous step
- **Parallel Tool Execution**: Invoking multiple independent tools simultaneously to reduce latency — requires the agent to identify non-dependent tool calls
- **Tool Ambiguity**: A failure mode where the agent cannot determine which tool to use for a task, or where multiple tools claim to solve the same problem
- **Code Mode**: Cloudflare/Anthropic pattern where the agent writes Python code (instead of calling many tools) and executes it in a sandbox — simplifying orchestration at the cost of runtime safety

## Examples/Applications

- **Research Pipeline**: Agent discovers relevant search terms → queries web search API → reads articles → extracts entities → queries database for related information → compiles summary
- **Deployment Pipeline**: Agent formats code → runs linter → runs tests → builds artifact → deploys to staging → requests human approval → deploys to production
- **Data Analysis**: Agent queries database → loads results into Python → visualizes data → detects anomalies → generates report → sends to stakeholders via email
- **Incident Response**: Agent receives alert → queries monitoring system → inspects logs → identifies root cause → applies fix → verifies resolution → posts incident report

## Related Concepts

- [[agent-harness-primitives]]
- [[agent-communication-protocols]]
- [[cli-over-mcp-pattern]]
- [[agentic-scaffolding]]
- [[code-mode]]

## Sources

- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/)
- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/)
- [CLI Over MCP Pattern | Simon Willison](https://simonwillison.net/2025/mcp-cli-pattern/)
