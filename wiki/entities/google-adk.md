---
title: Google Agent Development Kit (ADK)
created: 2026-05-21
updated: 2026-05-21
type: entity
tags:
  - google
  - ai-agents
  - multi-agent
  - framework
  - open-source
  - architecture
  - developer-tooling
  - orchestration
sources: [raw/articles/2026-05-19_google-adk-v2.md]
---

# Google Agent Development Kit (ADK)

ADK is Google's open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents. **ADK 2.0** reached General Availability on **May 19, 2026** (20K GitHub stars), introducing a graph-based Workflow Runtime that replaces the hierarchical executor.

## ADK 2.0 Key Features

### Graph-Based Workflows
Deterministic routing and execution of tasks where agents, tools, and functions are nodes in a workflow graph. Replaces the hierarchical executor from 1.x.

### Dynamic Workflows
Code-based logic enabling iterative loops, conditional branching, and complex execution patterns beyond static DAGs.

### Collaborative Workflows
Coordinator agents with multiple sub-agents working together, supporting:
- Parallel sub-agent workers
- Nested hierarchical team structures
- Resilient dynamic scheduling across complex tasks
- Native inter-agent routing with control state handoffs and context variable propagation

### Multi-Agent Workflow Engine
Model-agnostic engine for orchestrating non-linear, conditional, and cyclical agent execution patterns.

## Breaking Changes from ADK 1.x

### 1. Event Schema
New `node_info` and `output` fields added to core Event schema. Custom session databases with rigid columns must update schemas. Serialized JSON blob storage unaffected.

### 2. BaseAgent → BaseNode
Agents now inherit from `BaseNode` and execute as graph nodes. Custom overrides of `_run_async_impl()` or `generate_content()` are **bypassed** by the Workflow Graph engine — custom telemetry and state management in those overrides is silently ignored.

**Migration**: Move custom execution logic into `BeforeAgentCallback` / `AfterAgentCallback` interfaces.

### 3. Context Mutation
Manual event appending via `context.session.events.append()` circumvents the graph engine and breaks determinism. Yield events explicitly from nodes so the framework handles persistence, routing, and streaming.

### 4. Error Handling
ADK 2.0 automatically catches exceptions for retries, telemetry, and Human-in-the-Loop pauses. Broad `except Exception:` blocks inside tools mask failures, disabling automatic retries. Catching `BaseException` traps `NodeInterruptedError`, breaking HITL pausing.

**Migration**: Let standard exceptions propagate. Configure retries via `RetryConfig(max_attempts=3)`.

## Installation

```bash
pip install google-adk --pre  # ADK 2.0
# or
pip install "google-adk~=1.0"  # ADK 1.x (if not upgrading)
```

Requirements: Python 3.11+ (2.0) or 3.10+ (1.x).

## Ecosystem Position

ADK 2.0 competes in the rapidly growing agent framework space alongside [[entities/microsoft-agent-framework]], [[entities/mastra]], [[entities/langchain]], and [[entities/openai-agents-sdk]]. Its graph-based execution model and Google ecosystem integration (Gemini, Vertex AI) differentiate it from callback-centric frameworks.

## Related Pages

- [[entities/google]] — Google's AI ecosystem
- [[concepts/gemini/gemini-enterprise-agent-platform]] — Google Cloud's enterprise agent platform
- [[entities/microsoft-agent-framework]] — Microsoft's competing agent framework
- [[concepts/multi-agent]] — Multi-agent AI systems
- [[concepts/agent-framework]] — AI agent frameworks landscape
- [[concepts/agent-architecture]] — Agent architecture patterns
