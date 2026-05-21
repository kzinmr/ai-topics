# Google ADK 2.0 (Agent Development Kit)

**Source:** GitHub Releases (May 19, 2026) + adk.dev/2.0/ | [GitHub](https://github.com/google/adk-python/releases/tag/v2.0.0) | [Docs](https://adk.dev/2.0/)

## Overview

ADK 2.0 is the General Availability release (May 19, 2026) of Google's open-source, code-first Python toolkit for building, evaluating, and deploying AI agents. It introduces a graph-based Workflow Runtime replacing the hierarchical executor, with deterministic routing, dynamic workflows, and collaborative multi-agent patterns. 20K GitHub stars.

## Key Features

- **Graph-Based Workflows**: Deterministic routing and execution of tasks as graph nodes
- **Dynamic Workflows**: Code-based logic for iterative loops and complex branching
- **Collaborative Workflows**: Coordinator agents with multiple sub-agents working together
- **Multi-Agent Workflow Engine**: Model-agnostic engine for non-linear, conditional, cyclical execution patterns
- **Intelligent Task Delegation**: Parallel sub-agent workers, nested hierarchical teams, resilient dynamic scheduling
- **Native Inter-Agent Routing**: Seamless orchestration for inter-agent messaging, control state handoffs, context variable propagation

## Breaking Changes from ADK 1.x

1. **Event Schema**: New `node_info` and `output` fields — custom session databases must update schemas
2. **BaseAgent → BaseNode**: Agents are now graph nodes; custom `_run_async_impl()` overrides are bypassed
3. **Context Mutation**: Manual event appending circumvents graph engine; yield events explicitly
4. **Error Handling**: Automatic retries and HITL pauses; don't catch `BaseException`
