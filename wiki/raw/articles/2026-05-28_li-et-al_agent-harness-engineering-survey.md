---
title: "Agent Harness Engineering: A Survey"
source: https://picrew.github.io/LLM-Harness/
authors:
  - Junjie Li (Carnegie Mellon)
  - Xi Xiao (UAB)
  - Yunbei Zhang (Tulane)
  - Chen Liu (Yale)
  - Lin Zhao (Northeastern)
  - Xiaoying Liao (JHU)
  - Yingrui Ji (UAB)
  - Janet Wang (Tulane)
  - Jianyang Gu (Ohio State)
  - Yingqiang Ge (Amazon)
  - Weijie Xu (Amazon)
  - Xi Fang (Amazon)
  - Xiang Xu (Amazon)
  - Tianchen Zhao (Amazon)
  - Youngeun Kim (Amazon)
  - Tianyang Wang (UAB)
  - Jihun Hamm (Tulane)
  - Smita Krishnaswamy (Yale)
  - Jun Huan (Amazon)
  - Chandan K Reddy (Virginia Tech, Amazon)
date: 2026-05-28
publication: OpenReview / arXiv
tags:
  - harness-engineering
  - ai-agents
  - survey
  - taxonomy
  - coding-agents
paper_url: https://openreview.net/pdf?id=eONq7FdiHa
github: https://github.com/picrew/Awesome-Agent-Harness
huggingface: https://huggingface.co/Awesome-Agent-Harness
extraction: full
---

# Agent Harness Engineering: A Survey

## Abstract

The rapid deployment of large language model agents in production has revealed a recurring pattern: task execution reliability depends less on the underlying model than on the infrastructure layer that wraps it, the **agent execution harness**.

This survey presents agent harness engineering as an independent system layer, proposes the seven-layer **ETCLOVG** taxonomy (Execution, Tooling, Context, Lifecycle, Observability, Verification, Governance), and maps a broad corpus of open-source projects onto that taxonomy to expose ecosystem patterns, coverage gaps, and emerging design principles.

## Three Claims

**CLAIM 1 — Harnesses are independent system layers.**
Real-world reliability is shaped by execution controls, feedback loops, governance, evaluation, and operational design, not only by model capability.

**CLAIM 2 — ETCLOVG separates production concerns.**
Execution, Tooling, Context, Lifecycle, Observability, Verification, and Governance expose architectural boundaries that earlier frameworks often conflate.

**CLAIM 3 — A broad ecosystem map reveals gaps.**
A systematic mapping of the open-source ecosystem surfaces adoption patterns across sandboxes, protocols, memory systems, orchestrators, observability platforms, benchmarks, and governance stacks.

## Three Engineering Phases

Read across 2022–2026, agent engineering has gone through a coherent shift in where the marginal effort lands. The three phases overlap in time and concept; they describe what the field has chosen to engineer, not a clean sequence of replacements.

**2022–2024: Prompt engineering.** The primary lever is the input prompt text: instructions, few-shot examples, and reasoning templates, all optimized for a single model call.

**2025: Context engineering.** The question shifts from "what is the input?" to "what should the model see at each step?" The scope expands to retrieval, compaction, tool-result ranking, and managing context-window saturation across turns.

**2026–: Harness engineering.** As models become capable enough to attempt long-running tasks, the engineering focus expands to the full infrastructure wrapper: execution environment, tool interface, context, lifecycle, observability, verification, and governance.

## Timeline of Agent-Harness Systems

The same shift is visible in the systems themselves. The ReAct era of 2022–2023 wrapped a single model loop with a while-loop, a prompt template, and a small tool dispatch table; AutoGPT and BabyAGI exposed the resulting failures, including execution runaway, context blowout, state loss, and unmonitored side effects, as infrastructure problems rather than prompt problems. Tool integration and multi-agent coordination from 2023–2024 added learned tool use (Gorilla, ToolLLM, Toolformer), role-playing organizations (CAMEL, ChatDev, MetaGPT, Mixture-of-Agents), the first agent benchmarks (SWE-bench, AgentBench, WebArena, GAIA), and the beginnings of protocol standardization (MCP, A2A). By 2025–2026 enough deployment experience had accumulated that "harness engineering" began to be named as a discipline of its own, accompanied by automated harness optimization and a wave of results in which only the harness was varied.

## The ETCLOVG Taxonomy

We organize the harness into seven layers. The first four describe the structural core of a harness; the last three describe the control plane around it. Compared with earlier six-component frameworks, **Observability** and **Governance** appear here as independent layers because, in production deployments, each has its own tooling stack and is owned by a different team.

- **E — Execution environment.** Determines where agent code runs and what sandbox constraints bound it: managed sandboxes, microVMs, code-specialized runtimes, computer-use environments, browser sandboxes, and OS-level permission models.
- **T — Tool interface and protocol.** Specifies how external capabilities are described, discovered, and invoked, including protocol standards (MCP, A2A), tool description and selection, tool-augmented training, and session management.
- **C — Context and memory management.** Controls what the model can see across short-term, session-level, and persistent horizons, including long-horizon context techniques and mitigations for context drift.
- **L — Lifecycle and orchestration.** Organizes the control flow that reads and writes state, from the single-agent inner loop to multi-agent patterns and full issue-to-pull-request task pipelines.
- **O — Observability and operations.** Captures traces, costs, failures, and reliability signals through tracing platforms, agent-specific operations tools, cost tracking, and unified observability.
- **V — Verification and evaluation.** Turns tasks and traces into evaluation, failure attribution, and regression feedback, including benchmark grounding, controlled execution, multi-level judgement, and deployment-time evaluation loops.
- **G — Governance and security.** Constrains behavior across model-level, system-level, and organizational-level sub-layers: permission models, lifecycle hooks, component hardening, declarative constitutions, and audit infrastructure.

## Mapping Open-Source Projects

To make the taxonomy concrete, the survey codes a broad corpus of open-source agent-harness projects against ETCLOVG, using the public artifact itself (README files, documentation, papers, examples, release notes) as the evidence. The corpus is maintained as a living catalog at [Awesome-Agent-Harness](https://github.com/picrew/Awesome-Agent-Harness).

### Corpus Construction Protocol
Candidates are gathered from GitHub, papers, curated lists, package registries, and engineering blogs, then deduplicated, checked against inclusion criteria, and coded against the seven ETCLOVG layers using public documentation.

### Primary Layer Assignments

| Layer | Scope | Primary Projects |
|-------|-------|-----------------|
| E | Execution environment & sandbox | 20 |
| T | Tool interface & protocol | 12 |
| C | Context & memory management | 9 |
| L | Lifecycle & orchestration | 47 |
| O | Observability & operations | 15 |
| V | Verification & evaluation | 21 |
| G | Governance & security | 14 |

**Total: 138 projects coded (current snapshot)**

Reading the corpus in aggregate: Execution, Tooling, Lifecycle, and Verification have the densest visible coverage. Context and memory appear across many projects but are often embedded inside larger frameworks rather than released as standalone components. Observability and Governance are thinner in open source and more often live inside commercial platforms, SDK features, or engineering writeups.

## Cross-Layer Synthesis

Composing the seven layers creates system-level constraints that no single layer can resolve alone. Three recurring patterns:

1. **Cost–quality–speed trilemma.** Stronger sandboxes, richer context, and deeper evaluation improve quality but cost tokens, latency, and infrastructure. Production harnesses cannot treat quality as a scalar objective.
2. **Capability–control tradeoff.** Larger tool menus, persistent memory, and permissive sandboxes broaden task coverage but enlarge the blast radius of misaligned or compromised actions.
3. **Harness coupling problem.** Harness layers are coupled in ways that make local optimization fragile. A prompt, tool, sandbox, verifier, or monitor may look beneficial in isolation while degrading the whole rollout.

A related shift: from **agent frameworks**, which package local abstractions (agents, tools, memory, execution loops), to **agent platforms**, which add durable workspaces, identity, observability, evaluation, governance, and human handoff across many runs and many users.

## Open Problems

Five questions remain open across the taxonomy:

1. **Hardening and scaling execution environments.** Common security evaluations; cost models between containers, microVMs, OS permission boundaries, full desktop VMs, browser environments, and learned surrogates; portability across self-hosted, cloud, and hybrid deployments.
2. **Reliable state in long-running agents.** Recasting context management as state estimation: characterizing information loss at each compression step; adding provenance, contradiction handling, and explicit staleness markers; recovering from durable artifacts rather than compressed history.
3. **Trace-native failure diagnosis.** Traces should be the primary object from which systems compute outcome scores, trajectory quality, failure attribution, and regression tests — not just after-the-fact debugging material.
4. **Standard handoffs across agents, tools, and humans.** Handoffs should transfer not only a text summary but intent, constraints, permissions, artifacts, provenance, budget state, risk level, trace history, and unresolved decisions.
5. **Adaptive simplification as models improve.** Every wrapper encodes an assumption about what the model cannot do reliably. As models improve, future harnesses need mechanisms for ablating, optimizing, and simplifying themselves under joint quality, latency, cost, and risk constraints.

## Companion Resources

- **Paper**: https://openreview.net/pdf?id=eONq7FdiHa
- **GitHub**: https://github.com/picrew/Awesome-Agent-Harness (747 stars, 220 entries)
- **HuggingFace**: https://huggingface.co/Awesome-Agent-Harness
- **Website**: https://picrew.github.io/LLM-Harness/

## Citation

```bibtex
@misc{li2026agentharness,
  title={Agent Harness Engineering: A Survey},
  author={Li, Junjie and Xiao, Xi and Zhang, Yunbei and Liu, Chen and
          Zhao, Lin and Liao, Xiaoying and Ji, Yingrui and Wang, Janet and
          Gu, Jianyang and Ge, Yingqiang and Xu, Weijie and Fang, Xi and
          Xu, Xiang and Zhao, Tianchen and Kim, Youngeun and
          Wang, Tianyang and Hamm, Jihun and Krishnaswamy, Smita and
          Huan, Jun and Reddy, Chandan},
  url={https://openreview.net/pdf?id=eONq7FdiHa},
  year={2026}
}
```
