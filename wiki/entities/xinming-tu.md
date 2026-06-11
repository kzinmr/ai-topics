---
title: "Xinming Tu"
created: 2026-05-29
updated: 2026-05-29
type: entity
tags:
  - entity
  - person

  - multi-agent
  - test-time-scaling
  - agent-architecture
sources:
  - https://xinmingtu.cn/
  - https://xinmingtu.cn/blog/2026/hierarchical-mas-theory/
  - raw/articles/2026-02-10_xinmingtu-cn_hierarchical-mas-theory.md
related:
  - structured-test-time-scaling
  - multi-agent-systems
  - test-time-scaling
  - rlm-recursive-language-models
---

# Xinming Tu

Xinming Tu is a researcher at the **University of Washington** working on theoretical foundations of AI inference architectures. He is the lead author of the [Structured Test-Time Scaling](https://xinmingtu.cn/blog/2026/hierarchical-mas-theory/) framework (Feb 2026), co-authored with Guanghao Ye.

## Research

### Structured Test-Time Scaling Framework

Tu's primary contribution is a **unified theoretical framework** for structured test-time scaling that explains why multi-agent systems, recursive architectures, and coding agents bypass the exponential collapse of linear reasoning. The framework applies the **work–span lens** from classical parallel computation to inference-time compute organization, revealing a **three-layer structural decoupling**:

1. **Topology** — compresses sequential control span from Θ(W) to Õ(log W) via hierarchical decomposition
2. **Scope Isolation** — decouples persistent state from ephemeral context to suppress intrinsic atomic errors
3. **Decoupled Verification** — suppresses residual failure tails by independent error-correction

See [[structured-test-time-scaling]] for the full framework.

### Key Ideas

- **Causal dependency chain**: Topology → Isolation → Verification — each mechanism creates structural preconditions for the next, rather than operating as independent improvements
- **Work-span formalism**: Borrowed from Brent's parallel computation theory (1974) to model test-time compute as a computation graph
- **Exponential collapse of linear reasoning**: P_linear = (1−ε)^W ≈ exp(−εW) — the mathematical ceiling on unstructured scaling
- **Context hygiene as permanent design principle**: Scope isolation is not a temporary patch for limited context windows — it addresses cognitive bandwidth degradation that occurs even with unlimited windows
- **Error mode orthogonality**: Verification advantage comes from complementary competence (verifier's failure modes orthogonal to generator's), not from verifier accuracy per se

### Systems Analysis

The framework maps 13+ inference patterns (from linear CoT to Aletheia's strict decoupled verification) onto the three mechanisms, revealing that most existing approaches leave at least one mechanism unengaged. The framework predicts convergence toward the full three-layer architecture.

## Related People

- **Alex Zhang** — Creator of [[rlm-recursive-language-models|RLMs]], acknowledged in the paper
- **Omar Khattab** — RLM co-author (MIT), acknowledged
- **Hao Sun** — Acknowledged feedback contributor

## Related Concepts

- [[structured-test-time-scaling]] — The full theoretical framework
- [[test-time-scaling]] — Broader test-time scaling landscape
- [[concepts/multi-agents/multi-agent-systems]] — Multi-agent systems
- [[rlm-recursive-language-models]] — Recursive Language Models
