---
title: "Mixture of Agents (MoA)"
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [mixture-of-agents, agents, multi-agent, agent-architecture, llm, model, ensemble, reasoning, chain-of-thought]
sources:
  - raw/papers/2024-09-04_2409.07487_mixture-of-agents.md
  - raw/papers/2026-05-27_2605.29116_beyond-consensus-moa.md
---

# Mixture of Agents (MoA)

Mixture of Agents is an architecture pattern where multiple LLM instances collaboratively produce a response by generating independent outputs that are then synthesized by an aggregator model. Unlike simpler ensembling approaches that only combine final answers, MoA operates on full reasoning traces, allowing the aggregator to recover correct intermediate steps from minority or even unanimously-wrong agent outputs.

## Overview

MoA sits at the intersection of [[multi-agent-systems]], model [[concepts/inference]] ensembles, and layered LLM architectures. The key insight is that aggregating at the reasoning-trace level rather than the answer level unlocks a form of cross-agent complementarity: different agents (or differently-perturbed runs of the same model) may each contribute partial correct insights, and a capable aggregator can assemble these fragments into a solution no single agent produced.

Two complementary formulations of MoA have emerged:

1. **Layered RAG MoA** (Chen et al., 2024): A production-oriented framework for financial-domain RAG where specialized small language models collaborate in a layered proposer-aggregator network, matching or exceeding single large model quality at lower cost.
2. **Self-Consistent MoA** (Fadnavis et al., 2026): A research finding that trace-level synthesis from a single model with perturbation-induced diversity outperforms heterogeneous model pools, with an aggregation paradox -- the aggregator can correct errors even when all agents unanimously agree.

## How MoA Works

### The Proposer-Aggregator Pattern

The core architectural pattern is a layered network:

1. **Proposer Layer**: Multiple LLM instances (often [[concepts/small-language-models]]) independently process the same query, each generating a response with its full reasoning trace. In the layered RAG variant, each proposer may have access to different retrieval sources. In the self-consistent variant, proposers receive semantically-equivalent but perturbed versions of the same input.

2. **Aggregator Layer**: A separate LLM receives all proposer outputs (including their reasoning traces) and synthesizes a final response. The aggregator is not voting -- it reads and reasons over the full traces, selectively adopting intermediate steps that collectively produce a better answer.

The 2024 paper uses heterogeneous small models as proposers; the 2026 paper shows that a single model with input perturbation can produce sufficient trace diversity, and that the aggregator's gain stems from trace-level complementarity rather than model heterogeneity.

### Trace-Level Synthesis vs. Consensus

The 2026 paper identifies an **aggregation paradox**: an aggregator that reads complete reasoning traces can recover correct solutions even when agents unanimously agree on a wrong answer. This is because:

- Majority voting has a ceiling that perturbation diversity does not raise (error correlations remain identical across runs).
- The aggregator's advantage comes from assembling correct intermediate steps from minority chains that voting discards.
- Never gating on consensus -- always synthesizing -- produces strictly better results.

This contrasts with [[multi-agent-consensus-patterns]] which treat agreement as a finishing condition. The 2026 paper introduces **anchored refinement** with provable non-degradation guarantees: the aggregator is constrained to produce output at least as good as the majority result.

## Comparison to MoE and Ensembles

| Dimension | Mixture of Agents (MoA) | Mixture of Experts (MoE) | Model Ensembles |
|---|---|---|---|
| **Granularity** | Full LLM instances as proposers | Sub-networks (experts) within a single model | Independent models |
| **Diversity Source** | Input perturbation or heterogeneous models | Learned routing to specialized FFN layers | Different architectures / training runs |
| **Aggregation Level** | Reasoning traces (intermediate steps) | Token-level gating (during forward pass) | Output-level (voting / averaging) |
| **Training Requirement** | No joint training needed (post-hoc composition) | Jointly trained with load-balancing loss | Independent training |
| **Cost Scaling** | Linear in number of proposers + aggregator overhead | Sub-linear (sparse activation per token) | Linear in number of models |
| **Key Advantage** | Trace-level complementarity; corrects unanimous errors | Compute-efficient scaling during training/inference | Simple; reduces variance |
| **Key Limitation** | Aggregator must be capable enough to synthesize traces | Training instability; expert collapse | Cannot recover from unanimous errors |

MoA is fundamentally different from [[concepts/mixture-of-experts]]. MoE operates inside a single model's forward pass, routing tokens to specialized sub-networks (experts) with a learned gating mechanism. MoA operates at a higher level of abstraction: full LLM instances generate independent reasoning traces, and a separate aggregator synthesizes them. MoA requires no joint training and can be assembled post-hoc from existing models.

Compared to model ensembles, MoA differs in aggregation depth: ensembles typically combine at the output level (vote, average), while MoA combines at the reasoning-trace level, enabling recovery of correct reasoning from minority outputs.

## Key Papers

- **"MoA is All You Need: Building LLM Research Team using Mixture of Agents"** (Chen et al., 2024, arXiv:2409.07487): Introduces layered MoA for financial-domain RAG using small language models. Demonstrates higher quality grounded responses at lower cost than single large models.
- **"Beyond Consensus: Trace-Level Synthesis in Mixture of Agents"** (Fadnavis et al., 2026, arXiv:2605.29116): Shows that trace-level aggregation outperforms consensus, demonstrates the aggregation paradox, and introduces Self-Consistent MoA with perturbation-induced diversity and anchored refinement. A single model with trace variation outperforms heterogeneous model pools across structured reasoning, PhD-level science, competition mathematics, and competitive programming.

## Practical Implementations

MoA can be implemented as a post-hoc composition pattern without joint training:

1. **Heterogeneous MoA**: Deploy a pool of specialized small models (e.g., domain-specific fine-tuned SLMs) as proposers, with a stronger general model as aggregator. The 2024 paper's layered RAG MoA follows this approach for cost-efficient enterprise deployments.

2. **Self-Consistent MoA**: Use a single model with semantic-preserving input perturbations to generate diverse reasoning traces, then aggregate. This simplifies deployment (one model) while achieving state-of-the-art performance through trace-level synthesis.

Key implementation considerations include aggregator capability (must be strong enough to distinguish good from bad intermediate steps), perturbation design (preserving semantics while inducing useful trace diversity), and cost management (linear proposer scaling can be offset by using smaller proposer models).

## Related Topics

- [[concepts/mixture-of-experts]]: Token-level expert routing within a single model during forward pass
- [[multi-agent-systems]]: Broader class of systems where multiple agents collaborate, of which MoA is a specific aggregation architecture
- [[concepts/chain-of-thought]]: Individual reasoning traces are the unit of aggregation in MoA
- [[concepts/small-language-models]]: Key enabler for cost-effective heterogeneous MoA deployments
- [[concepts/reasoning-models]]: Self-Consistent MoA shows strong results on structured reasoning benchmarks
- [[multi-agent-consensus-patterns]]: MoA deliberately moves beyond consensus to trace-level synthesis
- [[concepts/retrieval-augmented-generation]]: The 2024 MoA paper applies the pattern within RAG workflows
- [[concepts/ai-agents]]: MoA is an orchestration pattern for collaborative agent reasoning
