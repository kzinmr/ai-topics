---
title: "LangChain"
type: entity
tags:
  - langchain
  - orchestration
  - framework
  - agentic-engineering
  - deep-agents
  - state-management
created: 2026-04-27
updated: 2026-06-18
aliases: [LangChain Framework, LangChain AI]
sources: [https://www.langchain.com/, https://github.com/langchain-ai/langchain, https://en.wikipedia.org/wiki/LangChain, raw/articles/2025-04-20_langchain-how-to-think-about-agent-frameworks.md, raw/articles/2026-04-29_langchain-harness-profiles.md, raw/articles/2026-05-12_langchain-delta-channels.md, raw/articles/2026-05-21_langchain_auth-proxy-langsmith-sandboxes.md, raw/articles/2026-06-15_langchain_building-100x-cheaper-trace-judge-fireworks.md]
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
| Apr 2026 | Launched **Harness Profiles** for Deep Agents — model-specific prompt/tool/middleware tuning (+10-20pt benchmark gains) |
| May 2026 | Released **DeltaChannel** (LangGraph v1.2 beta) — incremental checkpoint storage for long-running agents |

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
- See also [[concepts/wiki-memory]] — Chase's thesis on file-based agent memory (June 2026)

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

## Harness Profiles (Apr 2026)

LangChain introduced **harness profiles** for Deep Agents — model-specific configurations that tune prompts, tools, and middleware for optimal performance with each LLM family. Profiles ship out of the box for OpenAI, Anthropic, and Google models.

On tau2-bench: GPT 5.3 Codex jumped from 33% → 53% (+20pt), Claude Opus 4.7 from 43% → 53% (+10pt). This builds on earlier work where gpt-5.2-codex went from 52.8% to 66.5% on Terminal-Bench 2.0 through harness-layer changes alone.

See [[concepts/harness-profiles|Harness Profiles]] for details.

## Delta Channels (May 2026)

**DeltaChannel** is a new LangGraph channel type (beta v1.2) that writes only incremental updates at each checkpoint, with full snapshots every K steps. This bounds resume costs for agents running thousands of steps — enabling production-grade, long-running agents.

See [[concepts/delta-channels|Delta Channels]] for details.

## LangSmith Sandbox Auth Proxy (May 2026)

LangSmith Sandboxes introduced an **Auth Proxy** to control the network boundary between agent-generated code and external services. Instead of putting API keys into sandboxes as environment variables, the proxy sits on the outbound network path and enforces policy for which destinations are allowed and how authentication is applied.

### Key Design Decisions

| Aspect | Design |
|--------|--------|
| Credential storage | **Outside the runtime** — workspace secrets, opaque encrypted, or dynamic callbacks |
| Network enforcement | **Infrastructure-level** (not HTTP_PROXY) — transparent regardless of runtime/SDK |
| Default posture | **Fail-closed** — if callback fails, reject the sandbox request |
| Scope | Per-destination rules (e.g., only api.openai.com + api.github.com/repos/*) |

### Header Types
- `workspace_secret`: References a secret in LangSmith workspace settings
- `plaintext`: Stored as-is for non-sensitive headers
- `opaque`: Write-only, encrypted at rest, never returned by API

### Dynamic Credentials (Callbacks)
For OAuth tokens, per-user-scoped tokens, and credentials that need refresh, the proxy supports a callback pattern. The proxy calls a configured endpoint → receives `{"headers": {...}}` → injects and caches for TTL. Fails closed on error.

### Future Directions
- **DNS remapping**: Redirect requests to internal package mirrors
- **Network logging**: Audit trail of agent service calls and domain access
- **Request transformation**: PII redaction, organization metadata injection

This design follows the principle that agent infrastructure needs **control planes outside the runtime** — not exposed to agent instructions and decisions.

See [[concepts/security-and-governance/agentic-security]] for broader agent security patterns.

## Related Concepts
- [[concepts/langgraph]] — Low-level agent orchestration framework
- [[entities/langsmith]] — Observability and evaluation platform for LLM apps
- [[concepts/multi-agents/agent-orchestration-frameworks]] — Comparative analysis of agent frameworks
- [[entities/llamaindex]] — Competing data framework for LLM applications
- [[entities/dspy]] — Declarative LM programming framework (alternative paradigm)
- [[agent-engineering]] — The discipline of building reliable AI agents
- [[concepts/mcp]] — Model Context Protocol for tool interoperability
- [[concepts/deep-agents]] — Long-running autonomous agent pattern

## Sources
- [LangChain Official Site](https://www.langchain.com/)
- [GitHub Repository](https://github.com/langchain-ai/langchain)
- [Wikipedia: LangChain](https://en.wikipedia.org/wiki/LangChain)
- [LangChain Blog: Series B Announcement](https://blog.langchain.com/series-b)
- [LangChain Documentation: Component Architecture](https://docs.langchain.com/oss/python/langchain/component-architecture)
- [Sequoia Podcast: Harrison Chase on Building the Orchestration Layer](https://sequoiacap.com/podcast/training-data-harrison-chase)
- [AINews: The Inference Inflection](raw/newsletters/2026-04-30-ainews-the-inference-inflection.md)

## Trace Judge — Perceived Error Detection (June 2026)

LangChain Labs collaborated with **Fireworks AI** on a study fine-tuning **Qwen-3.5-35B** to detect *Perceived Error* — situations where a user *believes* the assistant made a mistake, judged from production traces on LangSmith. The work demonstrates that small, fine-tuned models can match or exceed frontier LLMs as evaluators at **10-100x lower cost**.

See also: [[concepts/llm-as-judge]], [[concepts/evaluation]].

### Key Findings

| Aspect | Detail |
|--------|--------|
| **Dataset** | chat-langchain (Docs Q&A agent, 885 traces) + Fleet (no-code agent builder, 911 traces). Multi-turn traces selected because judging perceived error requires observing human response to AI results. |
| **Labeling** | Multi-model panel + human review. All models agreed → ground truth. Disagreement → second panel. Still disagreement → human annotation. |
| **Training** | Qwen-3.5-35B base via LoRA SFT on Fireworks. Trained only on chat-langchain data to test cross-domain transfer. |
| **Design choice** | Only Human and AI messages included; tool calls ignored. Open design lever for future work. |

### Accuracy Results

| Condition | Accuracy | vs Claude Opus | vs GPT-5.5 |
|-----------|----------|----------------|------------|
| chat-langchain SFT | **96.1%** | 91.6% | 98.9% |
| Fleet SFT | **91.3%** | 90.2% | 89.1% |
| chat-langchain SFT → Fleet (zero-shot) | **90.8%** | — | — |

The cross-domain transfer result is particularly notable: a model fine-tuned *only* on chat-langchain traces outperformed **all frontier models** on Fleet data without ever seeing Fleet training examples.

### Cost & Generality

- **10-100x cheaper** than frontier API-based judges, with the advantage growing as trace volume increases.
- **Perceived Error rates**: 24% of chat-langchain traces, 18% of Fleet traces.
- The concept of *perceived error* generalizes across domains — a fine-tuned model trained on one application's traces can detect errors in a completely different application.

### Future Work

- Continual learning for trace understanding.
- Helping teams build their own evaluator models.

*People: @Vtrivedy10 (LangChain), @jakebroekhuizen (LangChain), @hwchase17 (LangChain), @chahvivi (Fireworks), Yi Su (Fireworks)*

## References

- 2026-04-25-langchain-anatomy-agent-harness
