---
title: "Multi-Agent Systems"
created: 2026-04-25
updated: 2026-05-29
type: concept
tags:
  - concept
  - multi-agent
  - orchestration
  - agent-architecture
  - agent-coordination
  - ai-agents
  - agents
  - coding-agents
  - subagents
  - verification
  - test-time-scaling
  - reliability
aliases:
  - multi-agent-systems
  - mas
related:
  - structured-test-time-scaling
  - multi-agent-orchestration-architecture
  - rlm-recursive-language-models
  - agent-architecture-decomposition
  - subagent-patterns
  - agent-swarm
  - agent-team-swarm
  - agent-orchestration-frameworks
sources:
  - raw/articles/2026-02-10_xinmingtu-cn_hierarchical-mas-theory.md
  - https://xinmingtu.cn/blog/2026/hierarchical-mas-theory/
---

# Multi-Agent Systems

Multi-Agent Systems (MAS) are AI architectures where multiple independent agents — each with its own context and capabilities — collaborate to solve problems that exceed the capacity of any single agent.

## Why Multi-Agent?

The theoretical foundation is explained by [[structured-test-time-scaling]]: single-agent linear reasoning faces **exponential collapse** — P_success = (1−ε)^W ≈ exp(−εW) — because errors compound along a length-W control path. Multi-agent systems bypass this ceiling through:

1. **Topology compression**: Hierarchical decomposition reduces span from Θ(W) to Õ(log W)
2. **Scope isolation**: Each agent operates in a clean, bounded context, suppressing atomic error rates
3. **Decoupled verification**: Independent agents can check each other's work

## The Three-Layer Structural Decoupling

As formalized in [[structured-test-time-scaling]] (Tu & Ye, 2026), multi-agent systems gain their advantage through a causal chain:

> **Topology** creates decomposition boundaries → **Isolation** manufactures verifiable atomic units → **Verification** suppresses residual errors

Each mechanism creates the structural preconditions for the next. Bolting verification onto a monolithic system provides limited benefit (errors are not verifiable); decomposition without verification still suffers work-driven collapse (errors are verifiable but unchecked).

## Key Patterns

See [[subagent-patterns]] for Chieng's four-pattern taxonomy (hierarchical, peer-to-peer, swarm, manager-worker).

### Explicit Orchestration
Frameworks like AOrchestra spawn sub-agents as runtime tuples ⟨Instruction, Context, Tools⟩, creating genuine hierarchical decomposition.

### Recursive Architectures
[[rlm-recursive-language-models|RLMs]] achieve span compression via functional recursion — the purest instantiation of topology + isolation.

### Coding Agents
SWE-agent, Claude Code, and Codex leverage compilers/test suites as powerful verifiers (classical verification regime: c_v ≪ c_g).

## Dynamic Topology vs. Topology Compression

A critical distinction: not all dynamic systems achieve true span compression. Systems like DyTopo and DyLAN optimize *who communicates with whom* among flat peer agents, but all agents remain at the same abstraction level. True span compression requires **recursive decomposition** into a hierarchy.

## System Mapping

| System | Topology | Isolation | Verification |
|--------|----------|-----------|--------------|
| CAMEL, MetaGPT, AutoGen | ○ (static roles) | ○ | ○ |
| AOrchestra | ● (hierarchical) | ● (file-based) | ○ |
| DyTopo, DyLAN | ○ (peer routing) | ○ | ○ |
| RLM | ● (recursive) | ● (return-value) | ○ |
| Claude Code task tool | ○ | ● (filesystem) | ○ |
| Aletheia (Gemini) | — | ○ | ● (decoupled) |

> ● = structurally present, ○ = implicit/partial, — = absent. The framework predicts convergence toward the full three-layer architecture.

## Practical Constraints

1. **Managerial capacity**: A manager must synthesize k logical branches — an O(k) reasoning task bounded by active attention. Deep hierarchies (large D) are necessary for large W.
2. **Scope boundaries**: Context hygiene and non-leaky interfaces are essential — if isolation fails, ε_leaf rises toward ε_mono.
3. **Verification advantage**: Requires δ_+ < 1 (verifier not blind to error modes) and error mode orthogonality.

## Related Pages

- [[structured-test-time-scaling]] — The unified theoretical framework
- [[subagent-patterns]] — Four subagent coordination patterns
- [[multi-agent-orchestration-architecture]] — Architectural approaches
- [[rlm-recursive-language-models]] — Recursive LM paradigm
- [[agent-architecture-decomposition]] — Agent architecture components
- [[agent-swarm]] / [[agent-team-swarm]] — Swarm and team patterns
- [[reduce-offload-isolate]] — Context engineering taxonomy
