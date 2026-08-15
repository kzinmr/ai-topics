---
title: "Agent Experience (AX)"
created: 2026-07-09
updated: 2026-08-15
type: concept
tags:
  - concept
  - infrastructure
  - ai-agents
  - cloud-infrastructure
  - developer-experience
sources:
  - raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-modal-cto.md
  - raw/articles/2026-08-15_pinecone_designing-agent-friendly-apis.md
---

# Agent Experience (AX)

**Agent Experience (AX)** is a design philosophy for cloud infrastructure that prioritizes the needs of autonomous AI agents over human developers. It argues that the existing cloud stack — built for humans who can read documentation, understand YAML, navigate UIs, and debug configuration errors — is fundamentally incompatible with how agents operate. Instead, infrastructure must expose programmatic primitives, API-first interfaces, and standardized sandboxes that agents can consume directly.

## Definition

Agent Experience (AX) reframes infrastructure design around a simple premise: **agents cannot read docs, click buttons, or figure out your YAML**. Every element of the cloud platform — compute, storage, networking, observability — must be expressible as a machine-readable, declarative API call. Where Developer Experience (DX) optimizes for human cognition, workflow ergonomics, and visual feedback, AX optimizes for agent autonomy, deterministic behavior, and programmatic composability.

As Akshat Bubna, CTO of Modal, argues: the old infrastructure stack assumes a human operator in the loop. Agents need infrastructure that treats them as first-class clients — not as users who happen to be automated.

## The Problem: Cloud Built for Humans

The modern cloud stack was designed during the DevOps era, where the target audience was a human engineer who:

- Can read and understand error messages
- Navigates a web console to find configuration options
- Writes and debugs YAML/JSON configuration files
- Understands networking concepts (subnets, VPCs, load balancers)
- Can SSH into a box to diagnose issues
- Handles gradual, persistent workloads — not bursty, ephemeral AI tasks

Autonomous AI agents violate every one of these assumptions. They cannot read human-oriented error messages meaningfully, have no graphical interface capability, and operate on millisecond-level decision loops with bursty, ephemeral compute needs.

## How AX Differs from Developer Experience (DX)

| Dimension | Developer Experience (DX) | Agent Experience (AX) |
|-----------|--------------------------|----------------------|
| **Interface** | GUI dashboards, docs, CLIs with help text | API calls, structured outputs, declarative configs |
| **Error handling** | Human-readable error messages | Machine-parseable error codes and schemas |
| **Workflow** | Human-in-the-loop, iterative debugging | Autonomous, deterministic, retry-based |
| **Resource model** | Persistent servers, long-running processes | Ephemeral sandboxes, bursty serverless functions |
| **Discovery** | Documentation browsers, search, tutorials | Schema discovery, OpenAPI specs, MCP endpoints |
| **Authentication** | OAuth flows, SSO, MFA with browser redirects | API keys, service tokens, workload identity |

## Key Infrastructure Requirements for AX

### Programmatic Primitives

Every infrastructure capability — spinning up a GPU instance, running a batch job, querying a vector database — must be a first-class API call, not a UI workflow or a configuration file. Agents need to compose these primitives programmatically without human mediation.

### API-First Design

APIs must be designed for machine consumption first, not human convenience. This means:
- Predictable, versioned endpoints
- Structured JSON responses with typed schemas
- Idempotent operations for safe retry
- Rate limiting communicated via machine-readable headers
- No magic — every side effect must be explicit

### Standardized Sandboxes

Agents need isolated, ephemeral execution environments that can be created and destroyed in milliseconds at arbitrary scale. [[concepts/sandbox|Sandboxes]] must provide:
- Fast startup times (sub-second to warm)
- Snapshot/restore for state continuity
- Strong security isolation
- Automatic cleanup
- Resource limits enforced at the kernel level

## Why Kubernetes Fails for AI Agents

Bubna argues that [[concepts/kubernetes|Kubernetes]] was designed for a different era — managing long-running, stable services in a containerized environment. AI agent workloads are fundamentally different:

- **Bursty**: Agents create and destroy sandboxes at high frequency — a deployment system designed for "deploy once, run forever" doesn't fit
- **GPU-heavy**: Kubernetes' pod scheduling and resource abstraction layers add overhead that matters at GPU-second granularity
- **State patterns**: Agents need filesystem snapshots and memory state preservation, not the stateless container model
- **Scale variance**: An RL rollout may require 100,000 simultaneous sandboxes — Kubernetes' etcd-based control plane breaks at this scale

## Key Capabilities for Agent-Native Infrastructure

Modal and other agent-first infrastructure providers are building around these capabilities:

- **GPU Snapshotting** — Freeze and restore GPU state (VRAM, CUDA context) to avoid cold starts on expensive hardware
- **DeFlash Speculative Decoding** — Accelerated inference to reduce per-token latency for agent loops
- **Auto Endpoints** — Infrastructure-managed HTTP endpoints that scale to zero and handle request routing without human configuration
- **RL Rollout Infrastructure** — Orchestrating 100,000+ sandbox instances for reinforcement learning training loops
- **Ephemeral Filesystems** — Per-session filesystems that are created and destroyed with the sandbox
- **Image Registry** — Automatically rebuilt per-repository container images for agent workspaces

## Relationship to Agentic Engineering

[[concepts/agentic-engineering|Agentic Engineering]] describes the human discipline of building software with AI agents — writing verifiers, designing prompts, orchestrating multi-agent workflows. Agent Experience (AX) is the *infrastructure complement*: the changes needed in the cloud platform itself to make autonomous agents possible. Agentic engineering asks "how do humans use agents?" AX asks "how must the infrastructure change so agents can operate independently?"

## AX in Practice: API Design Principles (Pinecone, August 2026)

Pinecone's Joerg Schad published a practical implementation guide for AX at the API design level, operationalizing the philosophy into six concrete design principles with measurable metrics.

### Measuring Agent-Friendliness

Two quantitative metrics anchor the framework:

- **TTFSC (Turns-to-First-Successful-Call)** — Start a cold agent with zero prior context and a task requiring the API; count round-trips until the first successful call. Every unclear error, doc detour, and auth dead-end shows up as a turn.
- **Unattended task-success rate** — Percentage of realistic, multi-step tasks an agent completes against the API with zero human intervention.

These are tracked as CI evaluations (a cold agent against staging on every release), with TTFSC regressions treated as broken builds.

### Cold Trial Results

Three cold trials with Claude Sonnet 5 in a bare harness (API key only, no docs, no SDK): median 6 turns to first successful API call, 11 turns to first search returning matches, roughly 90 seconds and $0.30 per run. Key finding: the agent using raw REST succeeded in 3 turns; agents using the Python SDK spent nearly half their turns learning call signatures from bare TypeErrors.

### Six Design Principles

1. **Errors are guidance** — Every user-facing error carries what was wrong, the fix, and a doc link. Stable machine-readable error codes (RFC 9457 Problem Details) serve as the contract; prose is non-contractual. Authorized callers get precise errors; unauthorized callers get the same wall.

2. **Budget the reader's context** — Every response is bounded (pagination, caps). Responses shaped for a reader that pays per token: semantic identifiers outperform opaque UUIDs, `response_format: concise` cuts token usage ~3x. Search beats list when the agent knows what it wants.

3. **Self-description beats documentation** — `describe/capabilities` endpoints answer operational questions in-band. OpenAPI specs are table stakes but descriptions must explain *when* to use an endpoint, not just what it returns. Deprecated shapes must be unmistakably marked; the modern path must be the canonical example everywhere.

4. **Safe at machine tempo** — Idempotency is a contract (retried mutations are no-ops). Rate limits are pace-able via `X-RateLimit-*` headers and `Retry-After`. Same input + state yields same shape. Guardrails: dry-run/preview modes, reversibility, confirmation gates on destructive operations.

5. **Access without a human in the loop** — Auth maturity ladder: short-lived keys with TTLs, least-privilege scoping below account level, delegation-native flows (OAuth 2.1 + PKCE, RFC 8693 token exchange), and at the top: zero-signup sandbox (claimable scratch resources, quotas and TTLs bound abuse instead of signup forms).

6. **The agent surface is a product, not a mirror** — Resist one-tool-per-endpoint MCP servers. Large APIs burn hundreds of thousands of tokens before the first call. Curate workflow-shaped tools instead of exposing raw endpoints. Dynamic meta-tools (`list_endpoints` / `get_schema` / `invoke`) for discovery. Cloudflare's Code Mode reduces 2,500 endpoints to ~1,000 tokens via `search()` + `execute()`. Key rules: capability parity (anything SDK can do, agent surface can do) and zero-config defaults.

The takeaway: every principle is old API design wisdom made legible and enforced. Agents don't demand a new discipline — they make the cost of ignoring the old one visible and churn-inducing.

Source: [Designing Agent-Friendly APIs — Pinecone Blog](https://www.pinecone.io/blog/designing-agent-friendly-apis/)

## Related Concepts

- [[concepts/agentic-web]] — The paradigm shift from human-centric to agent-centric web
- [[concepts/modal-sandboxes]] — Example of agent-native sandbox infrastructure
- [[concepts/harness-engineering]] — The discipline of building agent execution frameworks
