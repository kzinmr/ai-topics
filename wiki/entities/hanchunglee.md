---
title: "Hanchung Lee (Han Lee, @hanchunglee)"
created: 2026-05-23
updated: 2026-05-23
type: entity
tags:
  - person
  - agent-runtime
  - sandbox
  - isolation
  - architecture
  - agent-safety
  - technical-debt
  - infrastructure
sources:
  - "https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/"
  - "raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime.md"
  - "https://leehanchung.github.io/about/"
  - "https://www.linkedin.com/in/hanchunglee"
---

# Hanchung Lee (Han Lee, @hanchunglee)

> **Comprehensive profile**: [[entities/han-lee]] includes full biography, article catalog, monitoring configuration, and contributions taxonomy. This page focuses on the Agent Runtime analysis and core ideas from his "Hidden Technical Debt" series.

## Overview

Hanchung Lee (Han Lee) is an AI/ML engineer and **Senior Director of Data + AI at Moody's Analytics**, based in the San Francisco Bay Area. He writes the blog **"Han, Not Solo"** (leehanchung.github.io), covering ML engineering, compound AI systems, LLM agents, data science, and AI adoption.

His April 2026 blog post **"Hidden Technical Debt of AI Systems: Agent Runtime"** is a comprehensive analysis of agent runtime architecture, sandboxing, isolation primitives, and state management. The article explicitly re-draws Sculley et al.'s 2015 "Hidden Technical Debt in Machine Learning Systems" diagram for AI agent systems, arguing that the **agent runtime** is the largest, most expensive, and most under-invested layer in the modern AI stack.

The post has become foundational in agent infrastructure discourse, directly shaping how practitioners think about sandboxing, isolation, and the runtime layer that sits between the model and the world.

## Core Ideas

### 1. The Agent Runtime as Primary Technical Debt

Lee's central thesis: **the agent runtime is the single most under-invested layer of the AI stack.** In the classic Sculley et al. diagram, the ML model code is the small black box at the center, surrounded by massive infrastructure. Lee re-draws this for agent systems, showing the agentic model call as a tiny box surrounded by the much larger agent runtime.

> *"The agent is not the model. The agent is the harness plus the model, running inside the runtime. And almost nobody is treating it that way."*

The runtime encompasses six components:
- **Compute substrate** — container, microVM, or full VM
- **Filesystem** — with snapshot/rollback semantics
- **Tools** — shell, code interpreter, browser, file editor, MCP servers
- **Network boundary** — defines reachability both ways
- **State model** — persistence across turns, episodes, users
- **Lifecycle controller** — start, suspend, snapshot, resume, tear down

### 2. Sandboxing Necessity (Four Reasons)

Lee argues sandboxing is not optional, giving four first-class reasons:

1. **Isolation against the model's mistakes** — filesystem isolation, copy-on-write snapshots, per-session ephemerality
2. **Isolation against prompt injection** — tool outputs are attacker-controlled; sandbox prevents compromised output from reaching production data
3. **Multi-tenancy at training scale** — thousands of concurrent RL rollouts each need their own filesystem, process tree, network namespace
4. **Reproducibility** — snapshotted sandboxes enable replay for debugging and regression testing

> *"A sandbox is the only thing standing between an injected instruction and your production database. This is the agent-systems version of the SQL injection lesson, and we are at roughly the 2003 stage of learning it."*

### 3. The Isolation Primitive Stack

Lee produced the most comprehensive public comparison of five isolation primitives for agent workloads, with production evidence from Cognition, Manus, and Ramp:

| Primitive | Isolation model | Cold start | Workload fit | Notable users |
|---|---|---|---|---|
| **Linux containers** | Shared host kernel | ~100 ms | Trusted code, internal CI | Docker, Kubernetes default |
| **Firecracker** | KVM-based microVM, dedicated kernel per VM | ~125 ms boot, sub-second from snapshot | Untrusted code at high density | AWS Lambda, Fargate, E2B, Fly.io, Vercel Sandbox |
| **gVisor** | Userspace kernel intercepting syscalls; runc-compatible | Container-class | Defense in depth where microVM is overkill | Google Cloud Run, App Engine, Modal |
| **Kata Containers** | Lightweight VM per pod, OCI-compatible | Few hundred ms | Multi-tenant Kubernetes | Confidential Containers, some managed K8s |
| **V8 isolates** | Per-tenant JS heap inside a single process | Sub-millisecond | JavaScript-only, no arbitrary binaries | Cloudflare Workers, Deno Deploy |

Key judgments:
- **Containers are not a sandbox for agent code** — they are packaging + resource control; a kernel exploit breaks isolation completely
- **Firecracker is the de facto industry primitive** — strong isolation, ~5 MB VMM, boots a stripped-down Linux kernel in ~125 ms
- **gVisor** offers stronger isolation than namespaces without full VM cost, but some syscalls are slower/unsupported
- **Kata Containers** enables untrusted workloads on Kubernetes but inherits pod-lifetime assumptions
- **V8 isolates are wrong for general agent workloads** that need arbitrary Python, package installs, browsers, or compiled binaries

### 4. Runtime Shift — A New Flavor of Distributional Shift

Lee identified **runtime shift**: agents learn their runtime's quirks (tool latencies, failure modes, shell output formats), and moving to a different runtime causes silent quality regressions. Three paths to address it: co-locate train and prod on the same runtime, define a runtime contract, or train against production noise.

### 5. Web App vs Agent Runtime

Lee contrasts the two paradigms:

| Concern | Web App Runtime | Agent Runtime |
|---|---|---|
| User drives interaction | Yes | No — agent is autonomous |
| Refresh fixes most things | Yes | No — state must persist correctly |
| Session isolation | Nice to have | Mandatory |
| Network boundary | Firewall rules | Per-session network policy |
| State snapshot | Rarely needed | Foundation of debugging |
| Multi-tenancy | Request-level | Session-level with complete isolation |

> *"A web app's runtime can be sloppy because the user is the one driving and a refresh fixes most things. An agent's runtime cannot, because the agent will keep going long after a human would have stopped to ask a question."*

## Key Work

### Hidden Technical Debt Series (2026)

- **"A Taxonomy of RL Environments for LLM Agents"** (Mar 2026) — First article in the series. Formally defines the RL environment as $E = \{T, H, V, S, C\}$: tasks, agent harness, verifier, state management, configuration. Establishes the $H$ (harness) and $S$ (state) framework.

- **"Hidden Technical Debt of AI Systems: Agent Runtime"** (Apr 24, 2026) — The definitive article on agent runtime architecture. Covers: isolation primitive stack, sandbox vendor landscape, experiment-vs-production runtime divergence, runtime shift, runtime debt. [[raw/articles/2026-04-24_leehanchung_hidden-technical-debt-agent-runtime]]

- **"Hidden Technical Debt of AI Systems: Agent Harness"** (May 2026) — Third in the series. Deconstructs the agent harness: system prompts, tool surfaces, rollout protocols, context managers, memory, sub-agent topologies, guardrails, verifiers, observability.

### AI Adoption & Infrastructure

- **"Data Aggregation Is Not a Moat"** (May 2026) — AI agents collapse the cost structure of data aggregation businesses. Value shifts from data collection to decision-quality answers.
- **"Don't Outsource Your Understanding"** (May 2026) — Distinguishes cognitive offloading from cognitive surrender with cross-domain examples.
- **"'Determinism' is the Biggest Cope in AI Adoption"** (Apr 2026) — Determinism was never guaranteed in software; the real shift is from code verification to continuous evaluation.

## X Activity Themes

Lee's X/Twitter presence ([@HanchungLee](https://x.com/HanchungLee)) centers on:
- **Agent infrastructure** — runtime design, sandboxing, isolation, Firecracker microVMs
- **Technical debt in AI systems** — extending classic ML engineering concepts to agent systems
- **AI adoption patterns** — cognitive offloading vs surrender, determinism myths
- **Data moats and defensibility** — why data aggregation is not a durable advantage
- **ML engineering practice** — bridging research and production, evaluation methodology

## Related People/Entities

- [[entities/han-lee]] — Comprehensive entity page with full biography, article catalog, and monitoring
- [[concepts/agent-runtime]] — The concept page built from Lee's Agent Runtime article, with execution semantics, isolation analysis, and vendor landscape
- [[concepts/agent-harness]] — The harness layer that runs inside the runtime
- [[entities/cognition]] — Devin's VM-level isolation (cited in Lee's article)
- [[entities/manus]] — Agent runtime snapshotting for replay (cited)
- [[entities/modal]] — Sandbox infrastructure with gVisor isolation (Ramp Inspect case study cited)
- [[concepts/reduce-offload-isolate]] — Anthropic's context engineering framework, complementary to runtime isolation
- [[concepts/rl-environments-for-llm-agents]] — The formal $E = \{T, H, V, S, C\}$ taxonomy foundational to the Hidden Technical Debt series
