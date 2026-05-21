# Microsoft Agent Framework v1.0

**Source:** Microsoft DevBlogs, April 8, 2026 | [Link](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)

## Overview

Microsoft Agent Framework 1.0 is the production-ready release unifying Semantic Kernel foundations with AutoGen orchestrations into a single open-source SDK for .NET and Python. It provides enterprise-grade multi-agent orchestration, multi-provider model support, and cross-runtime interoperability via A2A and MCP.

## Key Features (v1.0 Stable)

1. **Single Agent & Service Connectors**: Production-ready agent abstraction. First-party connectors for Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic Claude, Amazon Bedrock, Google Gemini, Ollama.

2. **Middleware Hooks**: Intercept, transform, extend agent behavior — content safety filters, logging, compliance policies.

3. **Agent Memory & Context Providers**: Pluggable memory architecture — conversational history, key-value state, vector retrieval. Backends: Foundry Agent Service memory, Mem0, Redis, Neo4j, custom stores.

4. **Agent Workflows**: Graph-based workflow engine — branching, parallel fan-out, checkpointing, hydration for long-running processes.

5. **Multi-Agent Orchestration**: Patterns from Microsoft Research: sequential, concurrent, handoff, group chat, Magentic-One. All support streaming, checkpointing, human-in-the-loop.

6. **Declarative Agents (YAML)**: Define instructions, tools, memory, topology in version-controlled YAML. Load and run with single API call.

7. **A2A and MCP Protocols**: MCP for dynamic tool discovery/invocation. A2A 1.0 (coming) for cross-runtime agent collaboration.

8. **Migration Assistants**: Tools for teams migrating from Semantic Kernel or AutoGen.

## Preview Features

- **DevUI**: Browser-based local debugger for real-time agent execution visualization
- **Foundry Hosted Agent Integration**: Run agents as managed services on Microsoft Foundry or Azure Durable Functions
