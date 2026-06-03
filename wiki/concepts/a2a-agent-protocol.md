---
title: "Agent2Agent (A2A) Protocol"
created: 2026-06-03
updated: 2026-06-03
type: concept
tags:
  - agent-communication
  - agent-communication-protocol
  - multi-agent
  - google
  - protocol
  - open-source
  - ai-agents
  - mcp
sources:
  - raw/articles/2025-04-09_google-developers_a2a-agent-protocol.md
---

# Agent2Agent (A2A) Protocol

## Overview

**Agent2Agent (A2A)** is an open protocol launched by Google on April 9, 2025, that enables AI agents to discover, communicate, and coordinate with each other across different frameworks, vendors, and platforms. A2A tackles the fundamental challenge of siloed enterprise agents: without interoperability, autonomous agent productivity gains are limited to single-system boundaries. With A2A, agents built by different organizations and using different underlying technologies can securely exchange information and coordinate actions across enterprise applications.

A2A launched with support and contributions from **50+ technology and service partners**, including Atlassian, Box, Cohere, Intuit, LangChain, MongoDB, PayPal, Salesforce, SAP, ServiceNow, UKG, Workday, and leading consultancies (Accenture, BCG, Capgemini, Cognizant, Deloitte, KPMG, McKinsey, PwC, and others). In August 2025, IBM's Agent Communication Protocol (ACP / BeeAI) merged into A2A under the Linux Foundation, cementing it as the industry standard for agent-to-agent communication. See [[concepts/agent-communication-standards]] for the broader convergence timeline.

## Design Principles

A2A was designed around five key principles:

1. **Embrace agentic capabilities** — Agents collaborate in natural, unstructured modalities without being forced into "tool" interfaces. A2A enables true multi-agent scenarios where agents don't share memory, tools, or context.

2. **Build on existing standards** — Built atop HTTP, SSE, and JSON-RPC, making integration easy with existing enterprise IT stacks.

3. **Secure by default** — Enterprise-grade authentication and authorization at launch, with parity to OpenAPI authentication schemes.

4. **Support for long-running tasks** — Designed for tasks spanning everything from quick completions to hours-long deep research with humans in the loop. Provides real-time feedback, notifications, and state updates throughout.

5. **Modality agnostic** — Supports text, audio, and video streaming — acknowledging that agent communication isn't limited to text.

## Relationship with MCP

A2A **complements** Anthropic's [[Model Context Protocol (MCP)|concepts/model-context-protocol-mcp]]. They serve different layers of the agent stack:

| Protocol | Purpose | Layer |
|----------|---------|-------|
| **MCP** | Provides tools, resources, and context to individual agents | Agent ↔ Tools/Data |
| **A2A** | Enables agent-to-agent discovery, communication, and coordination | Agent ↔ Agent |

**Decision heuristic:** Use MCP when you need to give an agent access to databases, APIs, or filesystem tools. Use A2A when you need agents to delegate work to each other across organizational or vendor boundaries. They are often used together in production architectures: MCP handles tool integration, A2A handles cross-agent orchestration. See [[concepts/agent-communication-protocols]] for a detailed comparison.

## Key Features

### Agent Cards (Capability Discovery)
Agents advertise their capabilities via JSON "Agent Cards," allowing client agents to discover which remote agent is best suited for a given task. This enables dynamic delegation without hardcoded routing.

### Task Lifecycle Management
Communication is task-oriented. Each "task" is a protocol-defined object with a lifecycle — from creation through completion. For long-running tasks, agents stay synchronized with status updates. The output of a completed task is called an "artifact."

### Streaming & Real-Time Feedback
A2A supports streaming via SSE for real-time progress updates, notifications, and state changes — critical for long-running workflows and human-in-the-loop coordination.

### Multimodal Content
Messages contain "parts" — fully formed content pieces (e.g., generated images) with specified content types. Client and remote agents negotiate formats and UI capabilities (iframes, video, web forms), enabling rich user experience negotiation.

## Enterprise Adoption & Partner Ecosystem

A2A's launch partner ecosystem was notable for spanning both technology/platform companies and global systems integrators, signaling boardroom-level interest in agent interoperability:

**Technology & Platform Partners:** Atlassian (Rovo agents), Box, Cohere, Confluent, C3 AI, Datadog, DataStax (Langflow), Elastic, Harness, Intuit, JetBrains, JFrog, LangChain, MongoDB, PayPal, Salesforce, SAP, ServiceNow, UKG, Workday, and others.

**Service Providers:** Accenture, BCG, Capgemini, Cognizant, Deloitte, HCLTech, Infosys, KPMG, McKinsey, PwC, TCS, Wipro.

A production-ready version was planned for late 2025. As of 2026, A2A has become the default standard for multi-agent communication in enterprise settings, particularly after the ACP merger under the Linux Foundation. For a real-world example, the article describes candidate sourcing: a hiring manager's agent coordinates with specialized agents for candidate matching and interview scheduling across systems — illustrating how A2A enables cross-application agent workflows.

## See Also

- [[concepts/mcp-protocol]] — Model Context Protocol for agent-to-tool communication
- [[concepts/agent-communication-protocols]] — MCP vs A2A comparison and decision guide
- [[concepts/agent-communication-standards]] — Timeline of ACP, A2A, and BeeAI convergence
- [[model-context-protocol-mcp|concepts/model-context-protocol-mcp]] — MCP overview and relationship to agent communication
