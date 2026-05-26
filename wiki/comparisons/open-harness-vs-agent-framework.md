---
title: "Open Harness vs Agent Framework/SDK — Essential Differences as Investment Targets"
created: 2026-05-14
updated: 2026-05-15
type: comparison
tags:
  - comparison
  - harness-engineering
  - ai-agents
aliases: ["harness-vs-framework", "harness-vs-sdk"]
sources:
  - "raw/articles/2026-05-14_kzinmr_open-harness-vs-agent-framework.md"
  - "raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis.md"
  - "raw/articles/2026-05-15_kzinmr_why-runtime-centric-now-control-flow-ownership.md"
related:
  - concepts/agent-harness
  - concepts/harness-engineering
  - comparisons/agent-harnesses
  - entities/atal-upadhyay
---

# Open Harness vs Agent Framework/SDK — Essential Differences as Investment Targets

## Summary

**Open Harness systems and Agent Framework/Runtime systems may look like the same "AI Agent infrastructure," but they are quite different as investment targets.**

- **Open Harness** = Investment in the operating environment, execution environment, and work surface for **humans using** AI Agents
- **Agent Framework / Runtime** = Investment in the control infrastructure for **integrating** AI Agents into systems

The most robust strategy is not to choose between them adversarially, but to **separate their roles and use them together**.

---

## 1. Essential Differences

### 1.1 Definition

| Axis | Open Harness | Agent Framework / Runtime |
|------|-------------|---------------------------|
| **Purpose** | Work surface for humans to operate and execute AI Agents | Control surface for embedding AI Agents into applications/business systems |
| **Primary users** | Developers, operators, individuals, small teams | Product development teams, business system teams |
| **Mental model** | "Give a task and run it" | "Design as a system with state transitions" |
| **Control flow** | Fixed `while` loop + escape hatches | User-defined graph / state machine |
| **Abstraction level** | Finished product (ready to use) | Components (assembly required) |

### 1.2 Different Kinds of Flexibility

| | Open Harness (Broad Flexibility) | Framework / Runtime (Deep Flexibility) |
|---|---|---|
| **What's flexible** | Model switching, CLI/chat/IDE choice, file/shell operations, MCP additions, prompt changes | Typed state management, graph transitions, checkpoint persistence, side-effect control, approval flow codification, tenant boundaries |
| **Best for** | Exploration, development, operational support, individual work, small teams | Productization, business system integration, production operations |
| **Initial cost** | Low (ready to use) | High (design and implementation required) |
| **Expression** | Flexibility to **use** | Flexibility to **build and operate** |

### 1.3 Different Quality of Security / Control / Ops

| | Open Harness | Framework / Runtime |
|---|---|---|
| **Type of Security** | **Operator Safety** (operational safety for trusted humans) | **Product / Tenant Safety** (safety for untrusted users and multiple tenants) |
| **What it protects** | File, shell, MCP misuse prevention | PII management, permission separation, audit, SLA |
| **Evaluation axis** | Operator Workbench Readiness | Untrusted Product Runtime Readiness |
| **Representative tool strengths** | OpenClaw: gateway/control plane, Hermes: persistent personal agent, OpenCode: coding workbench | LangGraph: stateful durable execution, Pydantic AI: typed application framework |

---

## 2. Open Harness Details

### 2.1 Common Characteristics

Elements handled by the Open Harness family:
- Interfaces: chat, CLI, IDE, Web UI
- Session management, file read/write, shell execution
- MCP, custom tools, sandbox, approval flows
- Local/remote execution environments, long-term memory, skills
- AGENTS.md, SYSTEM.md, custom prompts

**Strengths**: Highly effective for improving human productivity.
**Risks**: Business logic and state tend to scatter inside the harness. Even if open source, **harness lock-in** can occur.

Assets constituting harness lock-in:
- Session history, memory, skills, custom commands
- Approval operations, sandbox configuration, MCP configuration
- Workspace layout, agent routing, chat identity mapping
- Chat channel-to-user-ID mapping, gateway routing/approval rules

### 2.2 OpenClaw — Agent Control Gateway / Operator Workbench

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | Agent gateway / control plane. Rather than building agents themselves, it **connects humans, chat channels, agent harnesses, workspaces, approvals, sandboxes, and tool policies** |
| **Strengths** | Supports Slack/Telegram/Discord/Google Chat/iMessage/Matrix/Teams/Signal/WhatsApp. Session routing, transcript mirror, approval, tool policy, sandbox configuration, model fallback/live switching, agent runtime swap capability |
| **Operator Workbench Readiness** | ★★★★☆ High (strong for trusted operators/teams) |
| **Untrusted Product Runtime** | ★★☆☆☆ Low (additional design needed for tenant isolation, credential isolation, audit, RBAC, policy enforcement) |
| **Overall** | Should be evaluated as an **agent control gateway / operator workbench**, not an agent product runtime |

### 2.3 Hermes Agent — Persistent Personal Agent / Self-Improving Workbench

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | A **persistent ops agent** that resides permanently, has memory, accumulates skills, and can be operated from multiple channels. Not a one-shot coding agent |
| **Strengths** | Supports Telegram/Discord/Slack/WhatsApp/Signal/Email/CLI. Persistent memory, auto-generated skills, cron, isolated subagents, container isolation, checkpoint/rollback, MCP credential filtering |
| **Operator Workbench Readiness** | ★★★★★ Very high (promising as an AI operating layer for individuals or trusted teams) |
| **Risks** | Long-term memory, self-improvement, auto-skill generation, cron, and subagents cause **state bloat and reduced behavioral explainability**. Requires management of which memory affected behavior and which skill was generated/modified when |
| **Overall** | Should be evaluated as a **personal or trusted-team AI operating layer**, not a customer-facing product runtime |

### 2.4 OpenCode — Practical Coding Harness

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | The most practical coding harness. Terminal/desktop app/IDE extension |
| **Strengths** | 75+ LLM provider support (low model lock-in), MCP/custom tools, permission (bash/edit/read/external_directory), plan mode, undo/redo, AGENTS.md |
| **Operator Workbench Readiness** | ★★★★☆ High (powerful as a developer's coding workbench) |
| **Caution** | Relatively permissive by default. Should be evaluated with hardened config. AGENTS.md, MCP config, custom commands, permission policy, and provider config accumulate as **OpenCode-specific operational assets** |
| **Overall** | Strong as a developer's coding workbench; should have a separate runtime for production agent backend |

### 2.5 Pi — Minimal Core + Extension Harness Platform

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | A **harness platform** for building custom agent harnesses via extensions, while maintaining a minimal core |
| **Strengths** | Minimal terminal coding harness, multi-provider support, AGENTS.md/SYSTEM.md, customizable compaction, skills, extensions, MCP integration, sandboxing, TypeScript extensions for tool call/session lifecycle intervention |
| **Operator Workbench Readiness** | ★★★☆☆ Medium (a platform to build your own control plane, not a finished one) |
| **Risks** | Extensions with full system permissions make untrusted extensions dangerous. Team use requires extension governance, review, signing, distribution, and permission separation |
| **Overall** | More of a **harness platform for building your own control plane** than a standard safe finished control plane |

---

## 3. Agent Framework / Runtime Details

### 3.1 Common Characteristics

Areas covered by Agent Framework / Runtime:
- Agent loop, tool calling, function calling, handoff
- Graph / workflow, typed state, session
- Durable execution, retry, checkpoint
- Human-in-the-loop, guardrails
- Tracing, evaluation, observability
- Deployment, tenant/user/role separation, audit log

**Strengths**: Suitable for production operations, audit, reproducibility, testing, failure recovery, and quality assurance.
**Weaknesses**: Heavier initial design than Open Harness.

Scenarios where Framework / Runtime is needed:
- Need to separate state per customer
- Want to audit agent decisions and operations
- Need to embed human approval as business rules
- Want to resume long-running processes mid-way
- Need to manage side effects of tool calls
- Want to continuously measure quality with evaluation datasets
- Need regression testing for model/prompt changes
- Want to provide agent functionality with production SLAs

### 3.2 Claude Agent SDK — Claude Code Harness Embedding SDK

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | SDK to **embed** Claude Code's agent loop, tools, session, permissions, subagents, hooks, MCP, and filesystem operations into your own application. Not a model-agnostic framework |
| **Strengths** | Leverages Claude Code-level coding agent capability. No need to build agent loop from scratch. Fast path to building software engineering agents |
| **Lock-in** | **High**. Deeply dependent on Claude Code runtime and tool behavior. Difficult to port to other models/SDKs |
| **Overall** | **Strong if betting on Claude, but be cautious for core infrastructure where vendor lock-in is a concern.** State, tool API, eval dataset, and approval records should be kept outside the SDK |

### 3.3 OpenAI Agents SDK — Lightweight Agent Primitive Framework

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | Lightweight framework handling agents, handoffs, guardrails, function tools, MCP, sessions, HITL, tracing, realtime/voice |
| **Strengths** | Relatively thin abstractions, strong integration with OpenAI API, easy embedding of tracing/guardrails, can build product agents in short time |
| **Lock-in** | **Medium**. Advanced features (hosted tools, Responses API, tracing, guardrails, realtime) depend on OpenAI |
| **Overall** | **Strong for product agent development centered on OpenAI.** To mitigate lock-in, keep tool schema, business state, approval policy, audit log, and eval dataset outside the SDK |

### 3.4 Google ADK — Google Ecosystem Agent Framework

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | Agent development framework focused on Google Cloud / Gemini / enterprise deployment |
| **Strengths** | Supports Python/TypeScript/Go/Java, multi-agent, workflow agents, deployment path to Cloud Run/GKE/Agent Runtime |
| **Lock-in** | **High** (Google Cloud). Claims model-agnostic, but most comfortable within Google ecosystem |
| **Overall** | **Natural choice for companies using Google Cloud as strategic infrastructure.** Limit adoption of ADK-specific features when cloud neutrality is a priority |

### 3.5 Strands Agents — Lightweight Model-Driven Agent SDK

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | Lightweight agent SDK with AWS/Bedrock affinity, model-driven philosophy. Emphasizes leveraging model planning/reasoning over heavy workflow frameworks |
| **Strengths** | Lightweight, model-driven, good compatibility with Bedrock/AWS, supports Anthropic/Ollama/LiteLLM, MCP/A2A/multi-agent configuration, thin orchestration code |
| **Risks** | Model-driven design may entrust too much business determinism and auditability to the model. LangGraph-style explicit state machines are better for complex business workflows |
| **Overall** | **A strong lightweight AWS-friendly agent SDK.** Needs careful design when used as a rigorous workflow runtime |

### 3.6 LangGraph — Production-Grade Stateful Agent Runtime

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | Production runtime for designing **stateful long-running agents/workflows as explicit graphs** |
| **Strengths** | Stateful graphs, durable execution, checkpoint, thread/session management, HITL, streaming, memory, retry/resume, persistence, debugging. Relatively high model independence |
| **Lock-in** | **Medium**. Observability/deployment dependency on LangSmith/LangGraph Platform possible, but graph state and checkpoint concepts are durable |
| **Overall** | **Core candidate for production agent workflows requiring long-running execution, audit, HITL, and state management.** High learning cost but solid long-term technical investment |

### 3.7 Pydantic AI — Type-Safe Python Agent Application Framework

| Evaluation axis | Judgment |
|----------------|----------|
| **Essence** | Framework that brings LLM agents **closer to normal typed Python application development** |
| **Strengths** | Python-centric, model-agnostic, typed deps, structured output, Pydantic type safety, strong FastAPI compatibility, MCP support, HITL approval, durable execution, Pydantic Evals, Logfire/OpenTelemetry, graph support |
| **Lock-in** | **Low to medium** (low model lock-in, but dependency on Pydantic ecosystem/Logfire) |
| **Overall** | **A very strong choice for building type-safe Python product agents.** LangGraph is stronger as a "stateful workflow runtime," while Pydantic AI is stronger as a "type-safe Python agent application framework" |

---

## 4. Cross-Tool Comparison Matrix

### 4.1 Operator Workbench Readiness (Open Harness)

| Tool | Essence | Workbench Readiness | Key Risk |
|------|---------|-------------------|----------|
| **OpenClaw** | Agent control gateway | ★★★★☆ | Additional design needed for multi-tenancy |
| **Hermes Agent** | Persistent ops agent | ★★★★★ | State bloat, reduced explainability |
| **OpenCode** | Coding harness | ★★★★☆ | Default permissive, harness lock-in |
| **Pi** | Harness platform | ★★★☆☆ | Extension permission management needed |

### 4.2 Untrusted Product Runtime Readiness (Framework / Runtime)

| Tool | Essence | Runtime Readiness | Lock-in Level |
|------|---------|------------------|---------------|
| **LangGraph** | Stateful agent runtime | ★★★★★ | Medium (concepts universal, platform dependency exists) |
| **Pydantic AI** | Typed Python framework | ★★★★☆ | Low to medium (ecosystem dependency) |
| **OpenAI Agents SDK** | Lightweight agent primitive | ★★★★☆ | Medium (OpenAI ecosystem dependency) |
| **Claude Agent SDK** | Claude Code embedding | ★★★☆☆ | High (Claude-specific) |
| **Google ADK** | GCP agent framework | ★★★★☆ | High (Google Cloud dependency) |
| **Strands Agents** | Lightweight model-driven | ★★★☆☆ | Medium (AWS/Bedrock dependency) |

---

## 5. Four Quadrants of Vendor Lock-in

| Lock-in Type | Affected Tools | Mitigation |
|-------------|---------------|------------|
| **Model lock-in** | Claude Agent SDK (Claude-dependent), OpenAI Agents SDK (Responses API-dependent), Google ADK (Gemini-dependent) | Separate model routing layer, standardize tool schema |
| **SDK lock-in** | All Frameworks (abstractions like handoff, guardrail, graph state) | Lock-in to good abstractions is acceptable. Keep state, eval dataset outside SDK |
| **Harness lock-in** | OpenCode (AGENTS.md, permissions), Pi (extensions), Hermes (memory, skills), OpenClaw (gateway routing) | Keep core business logic and state outside harness (DB, API, object storage) |
| **Cloud lock-in** | Google ADK (GCP), Strands (AWS/Bedrock) | Don't confine agent state, tool API, eval dataset, audit log to cloud-specific features |

---

## 6. Recommended Architecture

The most balanced configuration separates roles and uses both Harness and Framework together:

```
Human Interface / Harness Layer
  OpenClaw / Hermes Agent / OpenCode / Pi
        ↓
Tool Boundary
  MCP / HTTP APIs / typed function tools / internal service APIs
        ↓
Agent Control Layer
  LangGraph / Pydantic AI / OpenAI Agents SDK / Google ADK / Strands / Claude Agent SDK
        ↓
State & Governance Layer
  DB / object storage / audit logs / eval datasets / traces / approval records
        ↓
Execution Layer
  containers / sandbox / serverless / Kubernetes / CI runners / isolated workspaces
```

**Design principle**: Ensure **business logic survives even if the Harness is discarded**. This makes it easier to adapt when the following change in the future:
- The model, agent harness, framework, or cloud provider
- The observability platform, chat interface, or IDE
- The MCP server, pricing model, or vendor terms

---

## 7. Practical Selection Guidelines

### Open Harness Priority Cases (Want to put AI Agent into human work environment)
- Improving developer coding productivity
- Agent operation via CLI/IDE/Slack/Telegram
- Building personal/team AI workbench
- Flexible use of local files, shell, MCP, browser
- Frequent model/provider trial-and-error
- Prioritizing exploration speed over production SLA

→ Use OpenCode/Pi for developer environments, OpenClaw/Hermes as operator/personal agent

### Framework / Runtime Priority Cases (Want to embed AI Agent into product/business systems)
- Customer-facing agent features, business workflow integration
- Tenant state isolation, audit logs, approval flows, PII/sensitive data
- Long-running execution / mid-resume, eval/trace quality management
- Regression testing for model changes, production SLA

→ Core candidates: LangGraph, Pydantic AI, OpenAI Agents SDK, Google ADK, Strands Agents

### Optimal Scenario Per Tool

| Scenario | Recommended Tool | Reason |
|----------|-----------------|--------|
| Embed software engineering agent into your app | Claude Agent SDK | Reuses Claude Code capability |
| Python/FastAPI-centric type-safe agent | Pydantic AI | Typed deps + structured output + FastAPI affinity |
| Production workflow needing long-running execution / HITL | LangGraph | Stateful graph + durable execution |
| Lightweight product agent on OpenAI ecosystem | OpenAI Agents SDK | Thin abstraction + tracing/guardrails integration |
| Google Cloud strategic infrastructure company | Google ADK | GCP/Gemini integration |
| AWS-centric lightweight model-driven | Strands Agents | Bedrock affinity + thin orchestration |

---

## 8. Final Assessment

- **Open Harness should be invested in as the operational surface for humans using AI Agents**
- **Framework / Runtime should be invested in as the control surface for embedding AI Agents into systems**
- **Core assets should not be locked into either — they should be maintained as company-owned tool APIs, state, audit logs, eval datasets, prompt registries, and approval records**
- With this separation, you get both the speed and flexibility of Open Harness and the reliability and reproducibility of Framework / Runtime

It is equally wrong to underestimate the Control/Security/Ops of the Harness family as it is to overestimate them in the same way as the Framework family. The correct approach is to evaluate **what kind of Security it protects**.

---

## 9. Runtime-Centric vs Workflow-Centric: The Fundamental Axis

Beyond the Operator Workbench vs Product Runtime axis (§4), there is an even more fundamental architectural distinction (kzinmr, 2026-05-15): **runtime-centric systems** vs **workflow-centric systems**.

| Axis | Runtime-Centric (Harness) | Workflow-Centric (Framework) |
|------|--------------------------|------------------------------|
| **Core abstraction** | Runtime — manages *execution* | Workflow — describes *orchestration* |
| **Primary concern** | How execution proceeds continuously and safely | What execution topology should be |
| **Control center** | Runtime (autonomous) | Developer (explicit) |
| **State model** | Runtime-managed (implicit, across turns) | Graph-managed (explicit, designed) |
| **Environment coupling** | Strong (direct mediation of browser/shell/GUI) | Weak (abstracted through tool layer) |
| **Opinionatedness** | High (runtime makes decisions) | Medium (developer makes decisions) |
| **Extensibility** | Runtime extension (hooks, plugins, custom tools) | Workflow composition (nodes, edges, state transitions) |
| **Mental model** | Agent OS | Orchestration library |
| **Determinism** | Low (model-driven autonomy) | High (explicit state machine) |
| **Best for** | Autonomous execution, exploration, operator workbench | Production workflows, audit, deterministic business logic |

### The Runtime-Centric Family

A key insight: ClaudeCode, Codex CLI, PI, OpenClaw, and Hermes Agent are **all in the same architectural family** — they are runtime-centric systems despite their differences in openness and environment type.

| System | Nature |
|--------|--------|
| **ClaudeCode** | Closed runtime (vendor-optimized, co-trained with model) |
| **Codex CLI** | Closed runtime (vendor-optimized, multi-model) |
| **PI** | Programmable runtime substrate (minimal core, extension-based) |
| **OpenClaw** | Open runtime (multi-channel gateway + control plane) |
| **Hermes Agent** | Open runtime (persistent, self-improving, multi-backend) |

LangGraph and PydanticAI are **workflow-centric systems** — their primary abstraction is the orchestration topology, not the execution substrate.

### The PI Distinction: Runtime Substrate, Not an Agent SDK

PI occupies a unique position in this taxonomy. Unlike LangGraph/PydanticAI — which are developer-centric orchestration libraries (graph construction, node orchestration, deterministic workflow composition) — PI is doing **runtime system work**:

- Execution loop management
- State management across turns
- Task runtime with tool orchestration
- Environment mediation (filesystem, shell, browser via extensions)
- Event handling and streaming
- Interruption and recovery

This is closer to an **"Agent OS"** than an orchestration library. PI is not in the Harness↔Framework middle ground — it is firmly on the harness/runtime side. PI is trying to build an **application runtime**; LangGraph/PydanticAI are closer to **agent topology DSLs**.

| Axis | PI | LangGraph / PydanticAI |
|------|----|------------------------|
| **Core abstraction** | Runtime | Workflow |
| **Primary concern** | Execution | Orchestration |
| **State model** | Runtime-managed | Graph-managed |
| **Environment coupling** | Strong | Weak |
| **Extension model** | Runtime extensions (TypeScript SDK) | Workflow composition (nodes, edges) |
| **Mental model** | Agent OS / application runtime | Orchestration library / topology DSL |

This distinction matters because it changes the evaluation criteria. PI should not be compared to LangGraph on "workflow modeling capability" — that's not what it's trying to do. PI should be evaluated as a **runtime substrate**: how well does it manage execution, mediate the environment, and provide a programmable foundation for agent behavior?

### Why the Shift Now: Control Flow Ownership

The runtime-centric shift is not simply "models got smarter." The deeper structural change (kzinmr, 2026-05-15) is **who can safely own control flow**:

- **Workflow-centric era (2023)**: Models were unreliable primitives — tool misuse, context drift, loop collapse. Developers had to hold control flow authority via explicit graphs. LangGraph's worldview was correct for its time.
- **Runtime-centric era (2025+)**: Models can now *maintain execution semantics* — tool continuation, long-horizon tasks, retry adaptation, context tracking, subtask decomposition, failure recovery. When the model can safely own control flow, the bottleneck shifts from "how do we constrain flow?" to "how do we execute safely?"

The ReAct loop always existed — even LangChain could do `while True: thought=llm(...); result=tool(action)`. The presence of a loop is not the structural difference. The difference is that the loop is no longer an unreliable primitive that needs a developer-authored graph to contain it; it's a reliable execution substrate that the runtime can mediate.

#### The Framework Irrelevance Thesis: Half Right, Half Wrong

> "As models improve, frameworks become irrelevant."

- **Half right**: Workflow-centric abstraction (graph topology, explicit routing, structured transitions) declines as models internalize decomposition, planning, and recovery.
- **Half wrong**: Runtime abstraction (observability, state management, permissions, scheduling, isolation, memory, policies) becomes **more** important — the bottleneck shifts from orchestration logic to execution runtime design.

The future is not a "workflow compiler" but an **agent operating runtime**. ClaudeCode and Codex's advantage is not just model quality — it's **model × runtime co-design**.

See [[concepts/agent-runtime#why-now-control-flow-ownership-and-the-real-shift]] and [[concepts/agent-runtime#what-dies-and-what-survives-the-future-of-agent-infrastructure]] for the full analysis. See also [[concepts/runtime-opinionated-sdk]] for the analysis of Claude/OpenAI Agents SDKs as **mini runtimes** that embed a specific execution model (reactive tool loop, runtime-owned tool orchestration, composable actors, native observability).

**Source**: kzinmr, "Agent Stack Architecture & Comparative Analysis" (2026-05-15), [[raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis]].
