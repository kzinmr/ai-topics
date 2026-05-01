---
title: Jason Liu — Context Engineering
type: entity-subpage
parent: jason-liu
created: 2026-04-27
updated: 2026-04-27
tags:
  - context-engineering
  - rag
  - agents
  - llm-engineering
---

# Jason Liu: Context Engineering

From [Beyond Chunks: Context Engineering is the Future of RAG](https://jxnl.co/writing/2025/08/27/facets-context-engineering/) (Aug 2025), Liu extends RAG to agentic systems:

> \"The breakthrough came when we realized chunks themselves were the limitation. When search results showed multiple documents, agents couldn't strategically decide which to load or how to explore further.\"

## Four Levels of Context Engineering

1. **Minimal Chunks** — Basic tool responses without metadata
2. **Chunks with Source Metadata** — Enables citations and strategic document loading
3. **Multi-Modal Content** — Optimizes tables, images, structured data for agents
4. **Facets and Query Refinement** — Reveals the complete data landscape for strategic exploration

> \"Tool results become prompt engineering — Metadata teaches agents how to use tools in future calls\"

## Agent Peripheral Vision

Providing agents with structured metadata about the broader information space beyond top-k results. This is the key insight: agents need to know what they *don't* know.

> \"We've moved far beyond prompt engineering. Now we're designing portfolios of tools (directory listing, file editing, search) and the context engineering that makes them work together.\"

## Key Concepts

- **Tool Response as Prompt Engineering** — Metadata teaches agents how to use tools in future calls
- **Agent Peripheral Vision** — Structured hints about the broader information space beyond top-k results
- **Context Pollution** — Noisy, low-signal outputs (logs, traces) that crowd out useful reasoning context
- **Context Rot** — Performance degradation as input length increases
- **Slash Commands vs Subagents** — \"Bad context is cheap but toxic.\" Use subagents to isolate noisy operations

## Form Factor Decision Framework

- **Chatbots** — Conversational, audit trail as experience
- **Workflows** — Side-effect engines, deterministic outcomes
- **Research Artifacts** — Reports, summaries, data tables with consistent quality standards

## \"In Distribution\" Theory & Sandbox Engineering (2026-04)

Jason's work on the OpenAI Agents SDK sandbox features and \"in distribution\" theory:

- **\"In Distribution\"**: Built-in tools (shell, compaction, memory) exist within the model's training distribution, acting as native interfaces rather than prompt tricks
- **Harness/Compute Separation**: Clear separation between Brain (Harness: reasoning & planning) and Hands (Compute: file I/O & command execution)
- **Tool Naming Impact**: Naming conventions like `bash` vs `shell` vs `run_command` actually affect model performance
- **Security by Isolation**: Run model-generated code in sandboxes to reduce credential leakage risk from orchestration machines
- **Pragmatic Sandbox Use**: Lightweight tasks don't need sandboxes; heavy tasks get provisioned appropriately — \"think without turning the laptop on\"

## Related Blog Posts

- **[Slash Commands vs Subagents](https://jxnl.co/writing/2025/08/29/context-engineering-slash-commands-subagents/)** — Context pollution kills agent performance. Subagent architecture solves this — burn tokens in specialized workers, preserve focus in the main thread.
- **[Agent Frameworks and Form Factors](https://jxnl.co/writing/2025/09/04/context-engineering-agent-frameworks-and-form-factors/)** — Three form factors (chatbot, workflow, research artifact) and autonomy spectrum. \"Ask your team for specific results, not just 'agents.'\"
- **[Rapid Agent Prototyping](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Use Claude Code's project runner as a testing harness. \"Get one passing test before you write any orchestration code.\"
- **[AI Agent Compaction Experiments](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — \"If in-context learning is gradient descent, then compaction is momentum.\"

## See Also

- [[jason-liu--key-work]] — Jason Liu's career, RAG Master Series, and consulting practice.
- [[jason-liu--instructor]] — Structured outputs library by Jason Liu using Pydantic validation.
- [[retrieval-augmented-generation]] — Core RAG concepts and architecture patterns.
- [[context-engineering]] — Designing information environments for AI agents.
- [[coding-agents]] — AI agents for software engineering tasks.
