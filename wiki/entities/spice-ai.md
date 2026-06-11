---
title: "Spice AI"
created: 2026-06-08
updated: 2026-06-09
type: entity
tags:
  - company
  - infrastructure
  - developer-tooling
  - coding-agents
  - verification
  - agentic-engineering
  - open-source
  - sql
  - search
  - llm-inference
  - data-platform
aliases:
  - Spice.ai
  - Spice AI
  - spice-ai
sources:
  - https://spice.ai/
  - https://spice.ai/blog
  - https://github.com/spiceai/spiceai
  - raw/articles/2026-06-08_linkedin-ido-pesok_verifying-agentic-development-at-scale.md
description: "Data and AI platform combining federated SQL query, hybrid search, and LLM inference in a portable, open-source runtime. Also built real-time code verification for agentic development."
---

# Spice AI

**Spice AI** (founded 2021) is a data and AI platform company that provides a portable, open-source runtime combining **federated SQL query**, **hybrid search**, and **LLM inference** in a unified engine. Written in Rust and licensed under Apache-2.0, the platform powers data-grounded AI applications and agents. The company also developed a pioneering real-time code verification system for agentic development, led by [[entities/ido-pesok]].

## Platform

Spice AI's core product is a unified SQL query, search, and LLM inference engine (2,950+ GitHub stars):

- **SQL Federation & Acceleration** — Query across operational and analytical data sources with local acceleration, supporting PostgreSQL, MySQL, DuckDB, SQLite, Apache Iceberg, S3, and 30+ other connectors
- **Hybrid SQL Search** — Combine vector similarity, full-text (BM25), and keyword search in a single SQL query using Reciprocal Rank Fusion (RRF)
- **LLM Inference** — Call local or hosted LLMs from the Spice query engine
- **MCP Server & Gateway** — Run MCP servers locally or over SSE for agentic AI architectures
- **Spice Cayenne** — Next-generation data accelerator built on Vortex for high-scale data lake workloads
- **Real-Time Change Data Capture** — Sync accelerated datasets with DynamoDB Streams and other CDC sources
- **Edge to Cloud Deployments** — Portable runtime deployable anywhere

The platform was rebuilt from the ground up in Rust in 2024, delivering performance, safety, and portability for production data infrastructure. Partners include AWS, Databricks, NetApp, and NVIDIA.

## Verification Stack

Beyond the core platform, Spice AI built a pioneering multi-layered verification system for AI-generated code that operates at three levels:

1. **Syntax and Type Checking** — immediate compilation and type-checking of generated code
2. **Semantic Verification** — LLM-based verification that generated code matches the intent of the request, checking API usage, data flows, and pattern adherence
3. **Architectural Compliance** — enforcement of architectural rules including dependency policies, service boundaries, and approved patterns

### Key Design Principle

Verification happens **during generation, not after**. This creates a tight feedback loop where agents self-correct in real time:

- Non-existent API calls trigger immediate correction
- Contract violations provide the contract definition for regeneration
- Security policy violations surface approved alternatives

## Team-Scale Verification

The platform supports organization-wide deployment with:

- **Team-specific rule sets** — per-team coding standards and architectural constraints
- **Shared infrastructure rules** — org-wide security policies and compliance requirements
- **Priority-based verification** — stricter checks on critical paths (payments, auth) vs. internal tools

## Reported Metrics

- **94% catch rate** before code review
- **<3% false positive rate**
- **87% self-correction rate** within two agent attempts

## Relation to Agentic Engineering

Spice AI's approach embodies the [[concepts/agentic-engineering]] principle that verification — not code reading — is the critical skill in agent-driven development. The company's verification stack is a concrete implementation of the multi-layer verification pipeline described in the agentic engineering literature.

See also: [[concepts/coding-agents/code-review-agents]], [[concepts/vibe-coding]]

> **Note**: Ido Pesok led the verification initiative at Spice AI and later joined [[entities/cognition-ai]] to work on verification capabilities in [[entities/devin]]'s virtual machine. Official founders (per Spice AI's structured data): Luke Kim and Phillip LeBlanc.

## Company Info

- **Founded**: 2021
- **Founders**: Luke Kim, Phillip LeBlanc
- **Core Stack**: Rust (Apache DataFusion, Apache Arrow, Vortex)
- **License**: Apache-2.0 (open source)
- **GitHub**: [github.com/spiceai/spiceai](https://github.com/spiceai/spiceai) — 2,950+ stars, 200+ forks
- **X/Twitter**: [@spice_ai](https://x.com/spice_ai)
- **Slack**: [spiceai.org/slack](https://spiceai.org/slack)
- **SOC 2**: Type II compliant
- **Partners**: AWS, Databricks, NetApp, NVIDIA

## Related

- [[entities/ido-pesok]] — Led verification initiative at Spice AI
- [[entities/cognition-ai]] — Company he later joined for Devin work
- [[entities/devin]] — The AI software engineer with autonomous verification
- [[concepts/agentic-engineering]] — The discipline his verification work exemplifies
- [[concepts/coding-agents/code-review-agents]] — Adjacent concept
- [[concepts/vibe-coding]] — Related development paradigm
