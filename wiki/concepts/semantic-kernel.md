---
title: "Microsoft Semantic Kernel"
created: 2026-07-19
updated: 2026-07-19
type: concept
tags: [semantic-kernel, agent-framework, microsoft, open-source, dotnet, python, product]
sources:
  - "raw/articles/2026-07-19_microsoft-semantic-kernel.md"
  - "raw/articles/2026-07-19_microsoft-semantic-kernel-readme.md"
---

# Microsoft Semantic Kernel

## Overview

**Semantic Kernel (SK)** is Microsoft's open-source SDK for integrating large language models (LLMs) into applications. It provides an orchestration layer that connects AI models with existing code, APIs, and plugins — enabling developers to build AI-native applications with enterprise-grade reliability.

First released in 2023, SK has evolved from a prompt orchestration toolkit into a full-featured **agent framework** supporting multi-agent coordination, process automation, and hybrid execution (local + cloud). It is Microsoft's counterpart to frameworks like [[entities/langchain|LangChain]], [[concepts/ag2-autogen|AutoGen]], and [[concepts/crewai|CrewAI]].

## Key Features

- **Multi-language SDK**: Native support for .NET (C#), Python, and Java
- **Plugin architecture**: AI functions, native functions, and OpenAPI-based plugins
- **Process framework**: Business process automation with stateful multi-step workflows
- **Agent framework**: Multi-agent chat, agent groups, and agent delegation
- **Memory & vector search**: Built-in connectors for vector databases (Azure AI Search, Chroma, Pinecone, etc.)
- **Enterprise integration**: Deep integration with Azure, Microsoft 365, and enterprise authentication
- **Model agnostic**: Supports OpenAI, Azure OpenAI, Anthropic, Google, Ollama, and any OpenAI-compatible endpoint

## Architecture

Semantic Kernel's architecture centers on the **kernel** as the orchestration hub:

| Component | Description |
|-----------|-------------|
| **Kernel** | Central orchestrator that manages services, plugins, and execution |
| **AI Services** | Connectors to LLM providers (chat completion, text generation, embeddings) |
| **Plugins** | Reusable functions: native (C#/Python code), semantic (prompt templates), and OpenAPI |
| **Memory** | Vector stores and text search for RAG patterns |
| **Process Framework** | Business process automation with DAG-based workflows |
| **Agent Framework** | Multi-agent coordination with group chat and delegation patterns |

## Comparison to Other Agent Frameworks

| Dimension | Semantic Kernel | LangChain | AutoGen | CrewAI |
|-----------|----------------|-----------|---------|--------|
| **Primary language** | .NET, Python, Java | Python, JS | Python | Python |
| **Enterprise focus** | Azure/Microsoft ecosystem | Cloud-agnostic | Microsoft Research | Agnostic |
| **Process automation** | Built-in Process Framework | LangGraph | Group chat | Sequential/ hierarchical |
| **Plugin model** | Native + OpenAPI | Tools | Tools + agents | Tools |
| **Multi-agent** | Agent Framework (v1.x) | LangGraph multi-agent | Core feature | Core feature |
| **License** | MIT | MIT | MIT | MIT |

## Recent Developments (2026)

- **Process Framework**: Introduced business process automation with stateful, DAG-based workflows for enterprise scenarios
- **Agent Framework GA**: Multi-agent support graduated from experimental to production-ready
- **Azure integration**: Deeper Azure AI Foundry and Azure Functions triggers
- **Quality improvements**: Focus on reliability, error handling, and telemetry for production deployments

## Significance

Semantic Kernel occupies a unique position in the agent framework ecosystem as the **Microsoft-endorsed solution** for enterprise AI development. While LangChain dominates the Python/JavaScript developer community, SK is the default choice for organizations invested in the .NET ecosystem and Azure cloud infrastructure. Its MIT license and multi-language support make it a viable alternative for polyglot enterprise environments.

## Related Pages

- [[entities/langchain]] — Python-dominant LLM application framework
- [[concepts/ag2-autogen]] — Microsoft Research's multi-agent conversation framework
- [[entities/microsoft]] — Microsoft's AI strategy and products
- [[concepts/ai-agent-architecture]] — Agent architecture patterns
- [[concepts/rag-systems]] — Retrieval-augmented generation (SK's memory integration)
