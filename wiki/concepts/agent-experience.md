---
title: "Agent Experience (AX)"
created: 2026-07-09
updated: 2026-07-09
type: concept
tags:
  - concept
  - infrastructure
  - ai-agents
  - cloud-infrastructure
  - developer-experience
sources:
  - raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-modal-cto.md
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

## Related Concepts

- [[concepts/agentic-web]] — The paradigm shift from human-centric to agent-centric web
- [[concepts/modal-sandboxes]] — Example of agent-native sandbox infrastructure
- [[concepts/harness-engineering]] — The discipline of building agent execution frameworks
