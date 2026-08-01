---
title: "Alex Ellis"
type: entity
created: 2026-08-01
updated: 2026-08-01
tags:
  - person
  - founder
  - entrepreneur
  - open-source
  - go
  - kubernetes
  - developer-tooling
  - local-llm
  - coding-agents
  - self-hosted
  - infrastructure
aliases: ["alexellis", "Alex Ellis (OpenFaaS)"]
sources:
  - raw/articles/2026-06-18_alexellis_local-qwen-vs-opus.md
  - https://blog.alexellis.io/
  - https://openfaas.com/
---

# Alex Ellis

**Alex Ellis** is a UK-based open-source maintainer and founder of OpenFaaS Ltd, best known as the creator of [[concepts/kubernetes|Kubernetes]]-era developer tools: **OpenFaaS** (serverless functions), **k3sup** (Kubernetes installer), **arkade** (CLI app marketplace), **inlets** (tunnels), and **Actuated** (self-hosted CI runners). Since 2025-2026 he has become a prominent practitioner voice on **local LLMs** — running quantized open-weight models like Qwen on in-house GPUs for real business workloads and publishing candid, data-rich assessments of their strengths and failure modes.

## Overview

Ellis began his open-source journey in 2016 building OpenFaaS entirely by hand, then joined VMware (2017-2019) to fund the work. After market changes in 2019 he moved to open-core and bootstrapped OpenFaaS Ltd. His product line centers on low-level infrastructure and Linux primitives — containers, Firecracker microVMs, network protocols, tunnels, CLIs, and Kubernetes — all written in Go, all opinionated about efficiency, user experience, control, and autonomy.

As a developer, he reports living in tmux 12 hours per day and letting Claude/Codex do the majority of his coding while insisting on doing his own writing. He wrote **Superterm** (2026) — a free tool to track tmux sessions, notes, and get visual feedback from coding agents — which was 100% written by coding agents.

## Projects

| Project | Description |
|---------|-------------|
| **OpenFaaS** | Open-source serverless functions platform for Kubernetes (2016-) |
| **k3sup** | "ketchup" — one-command Kubernetes installer for k3s/any K8s |
| **arkade** | CLI app marketplace and installer (with AGENTS.md-driven local-model experiments) |
| **inlets** | Self-hosted HTTP/TCP tunnels ("the missing API for Linux") |
| **Actuated** | Self-hosted CI runners for GitHub/GitLab |
| **SlicerVM** | AI sandboxes / Firecracker microVM service — "the missing API for Linux" for agent workloads |
| **Superterm** | tmux session tracker with visual feedback from coding agents (2026) |
| **faas-cli / faasd** | OpenFaaS CLI and single-node distribution |

## Local AI Thesis (June 2026)

Ellis's deep-dive "[Local Qwen isn't a worse Opus, it's a different tool](https://blog.alexellis.io/local-ai-is-not-opus/)" (2026-06-18) is a founding-practitioner document for [[concepts/local-qwen-vs-claude-opus|the local-vs-cloud model comparison]] in this wiki. Core positions:

- **Different tool, not worse model**: treating a local model inside a coding harness the same way as Claude/Codex leads to disappointment; matching it to specialized tasks produces genuine business value.
- **Benchmark gap is real but misleading**: Qwen 3.6 27B scores 77.2 SWE-Bench Verified vs Claude Opus 4.8's 88.6 (~12% behind on paper), but [[concepts/ai-benchmarks/benchmaxxing|benchmaxxing]] and Go-vs-Python workload mismatch widen the practical gap.
- **Cost matters**: coding plans are subsidized; local models pay for themselves on heavy, loop-heavy, or data-sensitive workloads. His $12K RTX 6000 Pro paid for itself in 2-3 months via a single revenue-recovery analysis on customer telemetry.
- **Sovereignty / vendor risk**: enterprise data controls and events like the removal of [[concepts/claude/fable-5|Claude Fable 5]] make local models the answer to "What if the frontier labs do X?"
- **Looping is the worst trait**: the model gets stuck repeating itself (burning 600W for 30+ minutes), overshooting goals like a blade tempering past the straw color. Never leave it unattended on long-horizon tasks.
- **Ops becomes the hard part**: identity, access control, metering, quotas, model routing, and power monitoring — he built the vibe-coded **Toilgate** provider for opencode to manage team access to local models.
- **Practical wins**: AGENTS.md instructions dramatically improve local model output (local Qwen added new CLIs to arkade faster than human contributors); local models can quickly read/explain codebases even when they can't write them.

## Writing Style & Philosophy

Ellis writes long-form, first-person, receipt-based analysis ("I have skin in the game, but no incentive to push either cloud or local models"). He uses craft analogies (tempering steel for model reliability), publishes concrete infrastructure details (llama.cpp command lines, nvidia-smi output, MTP speculative decoding acceptance rates), and is unusually transparent about failures (hallucinated filenames, corrupted files, looping behavior).

## Cross-References

- [[concepts/local-qwen-vs-claude-opus]] — His June 2026 article is the primary source for this comparison
- [[concepts/qwen]] — Qwen model family he runs locally (Qwen 3.6 27B)
- [[concepts/claude/fable-5]] — Vendor risk example that motivates local models
- [[concepts/ai-benchmarks/benchmaxxing]] — His critique of benchmark over-optimization
- [[entities/claude-code]] — Cloud coding agents he uses for the majority of his coding
- [[concepts/inference/llama-cpp]] — His local serving engine of choice
- [[concepts/inference/vllm]] — Rejected for prosumer use (3 tok/s slower for single-user generation)
- [[concepts/opencode]] — Open-source coding agent harness he built Toilgate for

## Sources

- [Local Qwen isn't a worse Opus, it's a different tool (blog.alexellis.io, 2026-06-18)](https://blog.alexellis.io/local-ai-is-not-opus/) — [[raw/articles/2026-06-18_alexellis_local-qwen-vs-opus.md]]
- [Alex Ellis Blog](https://blog.alexellis.io/)
- [OpenFaaS](https://openfaas.com/)
- [SlicerVM](https://slicervm.com/)
