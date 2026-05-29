---
title: "Macro Evals for Agentic Systems"
type: concept
created: 2026-05-26
updated: 2026-05-29
tags:
  - concept
  - evaluation
  - ai-agents
  - trace-analysis
  - clustering
  - observability
  - openai
sources:
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
  - https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
---

# Macro Evals for Agentic Systems

**Macro Evals** is a framework developed by OpenAI × Slalom for extracting behavioral patterns from thousands of agent events in multi-agent systems. Published as an OpenAI Cookbook (May 2026). It bridges the gap between low-level eval pass/fail signals and actionable system-level insights.

## Core Idea

The framework introduces a two-layer evaluation hierarchy:

1. **Lower-level evals**: Grade individual agents, handoffs, tools, and executions (pass/fail per rubric)
2. **Macro evals**: Cross-cut thousands of lower-level results to discover *what kinds of problems recur, where they concentrate, and what to investigate first*

## Four-Label Taxonomy

| Label | Meaning |
|-------|---------|
| `case_type` | Generated business scenario (clean, validation-blocked, alternative, pricing-exception, etc.) |
| `run_outcome` | Execution result (completed, awaiting review, blocked, failed) |
| `eval_finding` | Lower-level signal (e.g., `final_decision_quality`, `policy_compliance_correctness`) |
| `behavior_pattern` | Population-level recurring pattern discovered via clustering |

The chain flows: `case_type → run_outcome → eval_finding → behavior_pattern`.

## BERTopic-Based Discovery Pipeline

Only traces with failures, reviews, or Promptfoo signals:

1. **Embed**: Each trace document → vector e_i
2. **Reduce**: UMAP dimensionality reduction → z_i
3. **Cluster**: HDBSCAN density-based clustering (outliers = noise)
4. **Label**: tf×idf-style scoring assigns characteristic terms per cluster

### Prioritization

```
impact_score(k) = prevalence_share(k) × severity_weighted_prevalence(k)
```

High-frequency + high-severity patterns score highest.

**Output**: Topic leaderboard (impact-ranked), Trace scatter map (colored by behavior pattern), Lift heatmap (pattern concentration per case_type)

## Lower-Level Rubrics (Promptfoo)

Five evaluation rubrics for agent traces:
1. `final_decision_quality` — final decision matches problem + terminal state
2. `policy_compliance_correctness` — pricing/tariffs/regional constraints
3. `routing_specialist_activation` — appropriate specialists activated
4. `market_drift_awareness` — recognizes changing market conditions
5. `review_appropriateness` — review/escalation proportional to risk

Each trace document is a compressed, comparable text preserving business setup, execution results, key handoffs, review markers, and state transition digests.

## AgentTrace-Style Diagnosis

For selected behavior patterns, reconstructs a lightweight execution graph G = (V, E) and walks backward from focus events (anchors) to score upstream suspects:

```
suspect_score = 0.4·proximity + 0.3·frequency + 0.2·bridge + 0.1·role
```

## Practical Implications

| For AI eng teams | For business stakeholders |
|---|---|
| Escalate clearest eval failures to regression suite | Determine if generated case types match real operational risk |
| Review auto-grade samples to calibrate rubric strictness | Verify high-impact patterns correspond to customer outcomes |
| Track patterns per model/prompt/orchestration version | |
| Assign business owners to highest-impact patterns | |

**Core lesson**: Agent-level evaluation tells you *which local actions are risky*; macro evals tell you *what that risk amounts to at system scale*.

## Related

- [[concepts/agent-evaluation]] — Broader evaluation frameworks for AI agents
- [[entities/openai]] — OpenAI as evaluation methodology source
- [[concepts/heterogeneous-intelligence]] — Complementary paradigm for system architecture
- [[entities/promptfoo]] — Low-level eval tool used in the framework
