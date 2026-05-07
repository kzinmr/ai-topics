---
source: https://platform.claude.com/docs/en/managed-agents/multi-agent
title: "Multi-agent Sessions: Managed Agents Orchestration"
author: Anthropic
date: 2026-05-07
tags: [claude, managed-agents, multi-agent, orchestration]
---

# Multi-agent Sessions: Managed Agents Orchestration

Multi-agent orchestration allows a single **coordinator agent** to manage multiple specialized agents within a single session. This architecture enables parallel task execution, domain specialization, and isolated context management.

> **Beta Requirement:** All Managed Agents API requests require the `managed-agents-2026-04-01` beta header.

## Core Architecture & Mechanics
- **Shared Environment:** All agents share the same container and filesystem.
- **Isolated Contexts:** Each agent runs in its own **session thread** (event stream) with its own conversation history.
- **Persistence:** Threads are persistent; agents retain context from previous turns if called again by the coordinator.
- **No Sharing:** Tools, system prompts, and specific contexts are **not** shared between agents.
- **Hierarchy:** The coordinator can only delegate to one level of agents (depth > 1 is ignored).

### Effective Delegation Patterns
- **Parallelization:** Fanning out independent subtasks (e.g., searching multiple sources simultaneously).
- **Specialization:** Routing to agents with domain-specific tools (e.g., a "Security Agent").
- **Escalation:** Using a more capable model (e.g., Claude 3.5 Sonnet to Claude 4 Opus) for complex subtasks.

## Configuration and Setup

### Defining the Coordinator
To enable multi-agent capabilities, set the `multiagent` property and include the `agent_toolset_20260401` tool.

### Constraints
- **Roster Limit:** Maximum of **20 unique agents** in the roster.
- **Concurrency Limit:** Maximum of **25 concurrent threads** per session.

## Thread Management

### Thread Types
1. **Primary Thread:** The session-level stream (`/v1/sessions/:id/events/stream`). Provides a high-level summary of all activity.
2. **Session Threads:** Individual streams for each agent. Used to inspect detailed reasoning and specific tool calls.

### Actionable Operations
- **List Threads:** Retrieve all threads; the primary thread has a `null` `parent_thread_id`.
- **Interrupt:** Send `user.interrupt` with a `session_thread_id` to stop a specific agent.
- **Archive:** Use `archive` on an `idle` thread to free up space against the 25-thread limit.

## Event Monitoring
Events allow tracking the "flow" of work without monitoring every sub-thread:
- `session.thread_created` — New thread started for a specific agent.
- `session.thread_status_idle` — Agent is waiting; includes `stop_reason`.
- `agent.thread_message_received` — Sub-agent delivered results to the coordinator.
- `agent.thread_message_sent` — Coordinator sent a follow-up to a sub-agent.

### Tool Permissions & Custom Tools
If a sub-agent requires a tool result or permission (e.g., `always_ask`), the request is cross-posted to the **primary thread**.
