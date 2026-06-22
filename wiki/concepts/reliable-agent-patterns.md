---
title: "Reliable Agent Patterns"
type: concept
created: 2026-06-21
updated: 2026-06-21
tags:
  - ai-agents
  - rag
  - infrastructure
  - methodology
  - text-to-sql
  - human-in-the-loop
sources:
  - path: raw/articles/2026-06-19_martinfowler_reliable-agentic-ai-systems.md
status: active
---

# Reliable Agent Patterns

Engineering patterns for building production-reliable AI agent systems, as illustrated by Bayer's PRINCE (Preclinical Information Center) platform. These patterns were documented by Martin Fowler and Sarang Sanjay Kulkarni of Thoughtworks in June 2026, drawing on real-world experience deploying an agentic RAG system in pharmaceutical drug development.

## Context: PRINCE Platform

Bayer's PRINCE platform is a cloud-hosted agentic AI system that helps preclinical researchers query decades of safety study reports using natural language. It integrates [[concepts/agentic-rag]] with Text-to-SQL to bridge unstructured PDF reports and structured study metadata. Built with LangGraph orchestration over FastAPI, it employs OpenAI, Anthropic, and Google models through a unified internal GenAI platform.

The system evolved through three phases: **Search** (unified gateway to structured metadata), **Ask** (RAG-based QA on unstructured PDFs), and **Do** (multi-agent task execution including regulatory document drafting).

## Key Reliability Patterns

### 1. Layered Guardrails

PRINCE implements defense-in-depth through multiple validation layers rather than a single safety check:

- **Clarify User Intent**: Proactive disambiguation before any retrieval begins. When a query is ambiguous across domains (e.g., toxicology vs. pharmacology), the system asks clarifying questions rather than guessing. This "fail-fast" mechanism prevents wasted execution on vague queries.
- **SQL Validation**: Generated Text-to-SQL queries are validated to ensure only SELECT operations are permitted; DELETE, INSERT, and UPDATE are explicitly blocked.
- **Response Citations**: Every answer includes citations linking back to specific chunks in source documents, enabling traceability.

### 2. Deterministic Validation Wrappers

Non-deterministic LLM outputs are wrapped in deterministic validation. The Text-to-SQL pipeline includes:

- Schema injection: only relevant schema components are dynamically injected into the LLM's context, reducing hallucination surface.
- Dynamic few-shot prompting: curated examples of correct SQL are retrieved from a vector store and included in prompts.
- An earlier LLM-review step for generated SQL was removed when it was found to introduce more noise than signal — an example of pragmatic simplification.

### 3. Structured Output Enforcement

The system enforces structured outputs at key boundaries:

- The Researcher Agent produces structured intermediate results that the Reflection Agent can validate before the Writer Agent synthesizes a final answer.
- The Think and Plan step uses structured process reflection (inspired by Anthropic's Think tool) to evaluate whether the agent is on the right trajectory, not just whether data is correct.
- Response generation uses a state-of-the-art reasoning model with explicit citation requirements.

See also: [[concepts/structured-outputs]].

### 4. Graceful Degradation and Fallback Chains

Robustness is built through multiple fallback mechanisms:

- **LLM-level retries**: If a specific LLM call fails, the system retries several times before falling back to an alternative model or platform.
- **Node-level retries**: Beyond individual LLM calls, entire logical steps (LangGraph nodes) can be retried.
- **Error-aware replanning**: Agents receive error context so they can chart an alternative trajectory rather than blindly retrying the same path.
- **Model diversity**: The internal GenAI platform hosts models from multiple providers via a unified OpenAI-compatible endpoint, enabling hot-swapping.

### 5. Text-to-SQL for Factual Accuracy

For queries requiring precise filtering, aggregation, or comparison of structured data (e.g., "Give me 50 example studies done on RAT"), the system routes to Text-to-SQL rather than relying solely on semantic retrieval. This pattern replaces approximate vector search with deterministic database queries where ground truth matters.

Key techniques:
- Dynamic schema selection (only relevant tables/columns injected into context)
- Vector-store-backed few-shot example retrieval for SQL generation
- Mandatory inclusion of study ID and title columns for downstream traceability

### 6. Human-in-the-Loop Checkpoints

PRINCE integrates human judgment at critical decision points:

- **Domain selection**: Users can pre-filter valid tools upfront via domain-level UI selection.
- **Source recommendations**: The model suggests relevant data sources based on query intent, but the user retains full control to accept, adjust, or override.
- **Reflection gating**: The Reflection Agent evaluates data completeness and sufficiency before the Writer Agent synthesizes a response, effectively creating a quality gate.

See also: [[concepts/human-in-the-loop]].

### 7. Monitoring and Observability for Agent Chains

Production observability is treated as a first-class concern:

- **Langfuse**: Primary observability tool providing detailed traces of all production traffic, enabling debugging of multi-step agent chains.
- **Cloudwatch**: General system health and metrics tracking.
- **RAGAS evaluation**: Both daily live-traffic evaluation and dataset-based evaluation on significant changes to workflow, prompts, or models.
- **State persistence**: LangGraph checkpointer persists execution state to PostgreSQL after each logical step, enabling recovery and debugging.

### 8. Context Discipline

A cross-cutting pattern: larger context windows did not reduce the need to be selective about what each agent sees. PRINCE assigns different context to different stages:

- **Planning context** for Think and Plan
- **Retrieval context** for the Researcher Agent
- **Evidence context** for the Reflection Agent
- **Synthesis context** for the Writer Agent

This reduces context pollution and makes each stage easier to debug, evaluate, and improve independently.

## Architecture: Agents and Coordination

The PRINCE agentic workflow (built on [[concepts/langgraph]]) coordinates specialized agents:

1. **Clarify User Intent** — disambiguates query domain and scope
2. **Think and Plan** — process reflection; decides tool selection and multi-step strategy
3. **Researcher Agent** — hybrid retriever: RAG for unstructured PDFs + Text-to-SQL for structured metadata. Evolving toward domain-specific sub-agents (toxicology, pharmacology) each with their own toolset.
4. **Reflection Agent** — validates data completeness and sufficiency before synthesis
5. **Writer Agent** — synthesizes final answer with citations

## Engineering Lenses

Martin Fowler frames these patterns through two lenses:

- **Context Engineering**: Shaping what information each model receives and how context flows between specialized steps.
- **Harness Engineering**: Building the scaffolding around models — orchestration, tool boundaries, state persistence, retries, fallbacks, validation, reflection loops, observability, and human review.

## Related Pages

- [[concepts/agentic-rag]] — Core agentic RAG architecture used by PRINCE
- [[concepts/ai-agents]] — AI agents overview
- [[entities/martin-fowler]] — Martin Fowler, co-author of the PRINCE case study
- [[concepts/human-in-the-loop]] — Human-in-the-loop integration patterns
- [[concepts/langgraph]] — LangGraph orchestration framework
- [[concepts/structured-outputs]] — Structured output enforcement in LLM systems
- [[concepts/ai-agent-architecture]] — General AI agent architecture patterns
