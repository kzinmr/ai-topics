---
title: "LangChain"
type: entity
tags: [langchain, orchestration, framework, agent-engineering, llm-framework]
created: 2026-04-27
updated: 2026-04-30
aliases: [LangChain Framework, LangChain AI]
related: [[langgraph]], [[langsmith]], [[agent-orchestration-frameworks]], [[dspy]], [[llamaindex]], [[agent-engineering]], [[concepts/harness-engineering]]
sources: [https://www.langchain.com/, https://github.com/langchain-ai/langchain, https://en.wikipedia.org/wiki/LangChain]
---

# LangChain

## Overview

LangChain is an open-source software framework for developing applications powered by large language models (LLMs). Created by **Harrison Chase** in October 2022, it has become the most widely adopted agent-building framework in the AI ecosystem, providing a unified API for connecting LLMs with external tools, data sources, and complex orchestration logic. LangChain is written in Python and JavaScript under the MIT License.

## History & Key Milestones

| Date | Milestone |
|------|-----------|
| Oct 2022 | Launched as an open-source project by Harrison Chase while at Robust Intelligence |
| Apr 2023 | Incorporated; raised $10M seed round from Benchmark |
| Q3 2023 | Introduced **LangChain Expression Language (LCEL)** for declarative chain definition |
| Oct 2023 | Launched **LangServe** to host LCEL code as production-ready APIs |
| Feb 2024 | Released **LangSmith** (closed-source observability/evaluation platform); announced $25M Series A led by Sequoia Capital |
| Sep 2024 | Launched **LangGraph** as a low-level agent orchestration framework |
| Jul 2025 | Reportedly raised ~$100M at $1.1B valuation |
| Aug 2025 | Released **Open SWE**, an open-source asynchronous coding agent |
| Oct 2025 | Raised **$125M Series B** at **$1.25B valuation** led by IVP, with participation from Sequoia, Benchmark, Amplify, CapitalG, and Sapphire Ventures |
| Oct 2025 | Launched **LangChain 1.0** and **LangGraph 1.0** |
| May 2025 | **LangGraph Platform** launched GA for managing long-running, stateful AI agents |
| Apr 2025 | Featured in the **Forbes AI 50** list |
| 2025-2026 | Introduced **Deep Agents**, **Insights Agent**, and no-code agent builder |

## Core Architecture

LangChain is built on a modular, layered architecture with the following core components:

### Models
- **Model-agnostic abstraction layer** — swap between OpenAI, Anthropic, Google, Hugging Face, etc. without code changes
- Supports chat models, text completion models, and embedding models
- Standardized interface with structured output (JSON, Pydantic)

### Prompts
- **Prompt Templates** — reusable, parameterized prompt structures
- **Few-shot example selectors** — dynamically select examples based on input similarity
- **Output parsers** — parse LLM responses into structured formats

### Chains
- **LCEL (LangChain Expression Language)** — declarative, composable syntax for defining execution pipelines
- Supports branching, merging, conditional execution, and parallel processing
- Built-in streaming, async, and batch execution

### Tools & Toolkits
- **300+ integrations** covering: ArXiv, Bing Search, Brave Search, DuckDuckGo, Python REPL, Bash, file system, code interpreters, APIs, databases
- **Toolkits** — curated collections of tools for specific domains (e.g., SQL, GitHub, Office365)
- Custom tools can be defined via simple function decorators

### Agents
- **Pre-built agent architecture** with reasoning + tool-use loop
- Supports ReAct, OpenAI Function Calling, Plan-and-Execute, and custom agent types
- Parallel tool execution, sub-agent delegation, and hierarchical planning
- **Agent loop**: model decides next step → calls tool if needed → observes result → repeats until complete

### Memory
- Conversation buffer, summary, vector store, and knowledge graph memory backends
- Persistent session state across agent iterations

### Callbacks
- Observability hooks for logging, monitoring, tracing, and streaming
- Built-in integration with LangSmith, OpenTelemetry, and third-party observability tools

## The LangChain Ecosystem

The company has evolved beyond the open-source framework into a full **Agent Engineering Platform** with four core products:

| Product | Type | Description |
|---------|------|-------------|
| **LangChain** | Open-source framework | Pre-built agent architecture with model integrations for rapid prototyping |
| **LangGraph** | Open-source framework | Low-level primitives for building custom, stateful agent workflows (graph-based orchestration) |
| **LangSmith** | Commercial platform | Observability, evaluation, debugging, and deployment for LLM applications |
| **LangServe** | Deployment tool | Host LCEL code as production-ready REST APIs |

### LangGraph
- Graph-based agent orchestration: nodes (computation) + edges (control flow)
- Supports cycles, branching, and conditional routing
- State management across agent execution
- **LangGraph Platform** (GA May 2025): production runtime for long-running, stateful agents
- Powers multi-agent coordination patterns

### LangSmith
- Debugging, testing, evaluation, and monitoring of LLM apps
- Trace visualization for agent decision paths
- Dataset management for regression testing
- **LangSmith Deployment** (2025): deploy and scale agents in production

### Deep Agents & Harness Profiles (2025-2026)
- **Deep Agents** (2025): Build agents that can plan, use subagents, and leverage file systems for complex tasks. Combines LangGraph orchestration with deep reasoning loops.
- **Harness Profiles** (April 2026): Pre-configured agent harness configurations optimized for specific use cases, building on the [[concepts/harness-engineering]] decomposition (Open Models / Open Runtime / Open Harness). A step toward agent infrastructure standardization, allowing developers to select purpose-built execution environments rather than manually assembling harness components.

## Key Use Cases

- **Chatbots & conversational AI** — context-aware multi-turn dialogue
- **Retrieval-Augmented Generation (RAG)** — document Q&A with external knowledge sources
- **Autonomous agents** — tool-using agents for research, data analysis, and workflow automation
- **Code analysis & generation** — understanding and generating code with tool integration
- **Synthetic data generation** — generating labeled datasets for ML training
- **Document summarization** — processing large documents with map-reduce and refine strategies

## Funding & Business

- **Total raised:** ~$160M+
- **Latest valuation:** $1.25B (Series B, Oct 2025)
- **Key investors:** IVP, Sequoia Capital, Benchmark, Amplify, CapitalG, Sapphire Ventures
- **Notable customers:** Replit, Clay, Harvey, Rippling, Cloudflare, Workday, Cisco
- **Revenue model:** Open-source core (MIT) + commercial LangSmith platform + LangGraph Platform hosting

## Related Concepts
- [[langgraph]] — Low-level agent orchestration framework
- [[langsmith]] — Observability and evaluation platform for LLM apps
- [[agent-orchestration-frameworks]] — Comparative analysis of agent frameworks
- [[llamaindex]] — Competing data framework for LLM applications
- [[dspy]] — Declarative LM programming framework (alternative paradigm)
- [[agent-engineering]] — The discipline of building reliable AI agents
- [[mcp]] — Model Context Protocol for tool interoperability
- [[deep-agents]] — Long-running autonomous agent pattern

## Sources
- [LangChain Official Site](https://www.langchain.com/)
- [GitHub Repository](https://github.com/langchain-ai/langchain)
- [Wikipedia: LangChain](https://en.wikipedia.org/wiki/LangChain)
- [LangChain Blog: Series B Announcement](https://blog.langchain.com/series-b)
- [LangChain Documentation: Component Architecture](https://docs.langchain.com/oss/python/langchain/component-architecture)
- [Sequoia Podcast: Harrison Chase on Building the Orchestration Layer](https://sequoiacap.com/podcast/training-data-harrison-chase)
- [AINews: The Inference Inflection](raw/newsletters/2026-04-30-ainews-the-inference-inflection.md)

## References

- 2026-04-25-langchain-anatomy-agent-harness
