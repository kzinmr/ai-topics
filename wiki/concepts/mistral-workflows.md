---
title: "Mistral Workflows"
type: concept
created: 2026-05-11
updated: 2026-05-26
tags:
  - orchestration
  - durable-execution
  - workflow
  - ai-agents
aliases:
  - Mistral Workflows
  - Workflows (Mistral AI)
related:
  - concepts/agent-orchestration-frameworks
  - concepts/agentic-workflow-patterns
  - concepts/human-in-the-loop
  - entities/mistral-ai
  - entities/temporal
sources:
  - raw/articles/2026-05-10_mistral-ai_workflows.md
---

# Mistral Workflows

Mistral Workflows is **Mistral AI's enterprise AI orchestration layer.** Released as a public preview in April 2026. Built on Temporal's durable execution engine, it provides a platform for running multi-step AI processes — including LLM calls, tool use, external APIs, and human approvals — in production with resilience to crashes, restarts, and individual step failures.

**In one sentence**: Not an AI demo that runs in a notebook, but an execution foundation for AI workflows that keep running in the real world of business.

## Architecture

### Hybrid Deployment Model

Mistral Workflows adopts **control plane / data plane separation:**

| Layer | Location | Role |
|---|---|---|
| **Control Plane** | Mistral (or customer's private cloud) | Temporal cluster, Workflows API, Studio UI — manages state, history, task dispatch |
| **Data Plane** | Customer environment (Kubernetes / VM / local) | Worker processes run actual code. All LLM calls, tool execution, and business logic remain within the customer's perimeter |

Workers are deployed to Kubernetes via Helm charts and connect to Mistral's cluster via outbound connections. The orchestrator never makes inbound connections to the customer's network.

### Temporal Foundation

Internally uses [Temporal](https://temporal.io/)'s durable execution engine (the same foundation as Netflix/Stripe/Salesforce). Mistral extends Temporal for AI workloads with added support for streaming, payload handling, multi-tenancy, and OpenTelemetry-based observability.

## Core Features

### 1. Durable Execution

Every step is recorded in an event history. If a process crashes, times out, or a Worker restarts, **a different Worker replays the history and resumes from the last completed step.**

- Normal application code leaves multi-step processes half-finished on network timeouts
- Workflows sustain long-running processes spanning minutes to hours to months
- Developers can focus on **business logic** instead of recovery logic

### 2. Human-in-the-Loop (Approval Workflows)

With a single line of `wait_for_input()`, a workflow can pause for approval:

```python
approval = workflow.wait_for_input("Review required")
```

- The workflow pauses, consuming no compute resources
- The reviewer receives a notification and can respond via Le Chat / Webhook / API
- When the reviewer responds, execution resumes from the exact point it paused
- Full execution history is recorded in Studio for auditability

### 3. Observability

- All branches, retries, and state changes are recorded in Studio
- Native OpenTelemetry support (no additional configuration needed)
- Complete timeline for auditing decisions months later
- Drill-down into each routing decision, model call, and approval step

### 4. AI Primitives

AI-specific primitives usable directly within workflows:
- **Agent loop**: Iterative agent execution (observe→think→act loop)
- **LLM streaming**: Relay token streaming to clients
- **Mistral API integration**: Call models without additional integration code
- **Tool use**: External API, database, and file operations as activities

### 5. Multi-Surface Triggers

One workflow can be triggered from 3 entry points:

| Trigger Method | Target Users |
|---|---|
| **Mistral API** (`POST /v1/workflows/{name}/execute`) | Developers, external systems |
| **Mistral AI Studio** | Operations teams (auto-generated input forms + live execution timeline) |
| **Le Chat** | Business users (launch workflows conversationally as an assistant) |

## Python SDK

Developers write workflows as code in Python. SDK v3.0 was released alongside the public preview.

**Core concept**: Separation of Workflows (deterministic orchestration) and Activities (external processing with side effects):

- **Workflow**: Step coordination, state retention, branching, waiting, next action determination (deterministic)
- **Activity**: LLM calls, HTTP requests, DB writes, file reads, tool execution (side effects)

The SDK handles retry policies, tracing, timeouts, and rate limiting with decorators and single-line configuration.

## Production Use Cases

### Cargo Release Automation (CMA-CGM, etc.)

- Automate customs declarations, dangerous goods classification, safety inspections, and regulatory checks across multiple jurisdictions
- Requires timeout resilience, mid-process pauses for human review, and precise root cause identification on failure
- `wait_for_input()` suspends for human approval and resumes exactly where it left off

### Document Compliance (KYC Verification)

- Identity document extraction → sanctions list / PEP DB cross-reference → cross-jurisdictional regulatory requirement checks → structured risk assessment
- Previously hours of analyst work per case → reduced to minutes
- Studio displays all steps as a structured timeline with OpenTelemetry tracing for full drill-down

### Customer Support Routing

- Automated classification and routing for refunds, technical issues, billing disputes, account escalations
- Correctability on misclassification is a key requirement
- Each routing decision is visualized and traceable in Studio. If classification is wrong, the team can correct at the workflow level

## When to Use

### Appropriate Cases

- Multi-step LLM pipelines that must survive crashes and restarts
- Human-in-the-loop processes with approval waits spanning hours to days
- Scheduled or one-shot recurring AI tasks
- Multi-agent orchestration with handoffs and shared state
- Anything currently built with queues, state machines, and retry code

### When Not Needed

- Single LLM endpoint call without orchestration → standard SDK call is sufficient

## Differences from Competing and Related Technologies

- **[[concepts/agent-orchestration-frameworks]]** (LangGraph, CrewAI, etc.) — These focus on inter-agent coordination. Mistral Workflows provides durable execution, Human-in-the-loop, and enterprise auditability as a foundation, with agents running on top.
- **[[concepts/agentic-workflow-patterns]]** — Anthropic's 5 patterns (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer) are design patterns. Mistral Workflows is the **execution foundation** implementing them.
- **Temporal standalone** — Mistral Workflows is a managed layer on top of Temporal with AI-specific extensions (streaming, payload handling, multi-tenancy, OpenTelemetry, Le Chat integration).
- **AWS Step Functions / Azure Durable Functions** — General-purpose workflow engines. Mistral Workflows differentiates with native AI primitive integration (agent loops, LLM streaming, model calls).

## Adopting Companies (as of Public Preview)

ASML, ABANCA, CMA-CGM, France Travail, La Banque Postale, Moeve
