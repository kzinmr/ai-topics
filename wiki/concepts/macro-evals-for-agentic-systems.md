---
title: "Macro Evals for Agentic Systems"
type: concept
created: 2026-05-25
updated: 2026-05-26
tags:
  - evaluation
  - trace-analysis
  - bertopic
  - clustering
  - promptfoo
  - infrastructure
  - multi-agent
  - methodology
sources:
  - raw/articles/2026-05-19_openai_macro-evals-for-agentic-systems.md
  - https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
related:
  - evals-for-ai-agents
  - infrastructure-noise-agent-evals
  - harness-engineering
  - ai-resistant-evaluations
  - active-observability
status: active
---

# Macro Evals for Agentic Systems

A methodology for **discovering population-level behavioral patterns (macro evals) from lower-level evaluations of individual traces** in multi-agent systems. Published as a joint OpenAI × Slalom Cookbook.

> Agent-level evaluations tell you "which local behaviors are risky"; macro evaluations tell you "what that risk becomes at system scale."

## 2-Layer Architecture

```
Lower-level evals (per-agent)
  ├─ Grades individual agents, handoffs, tools, and executions
  └─ Eval tools like Promptfoo generate pass/fail
         ↓
Macro evals (cross-population)
  ├─ Cross-analyses large numbers of lower-level findings
  ├─ Discovers recurring patterns (BERTopic-style clustering)
  ├─ Prioritizes by impact score
  └─ Diagnoses upstream causes (AgentTrace-style execution graph analysis)
```

In multi-agent systems, the final answer is merely the last event in a long workflow. A seemingly reasonable release recommendation might, on trace inspection, reveal that the pricing agent ignored incentives, the supply agent missed stockouts, or the orchestrator bypassed required review steps.

## 4-Label Chain

A labeling system connecting individual traces to population-level patterns:

| Label | Scope | Meaning |
|-------|-------|---------|
| `case_type` | Input | Generated business scenario (clean, validation block, supplier substitution, pricing exception, ...) |
| `run_outcome` | Output | Execution result (completed, awaiting review, blocked, failed) |
| `eval_finding` | Local | Lower-level evaluation signal (`final_decision_quality`, `policy_compliance_correctness`, ...) |
| `behavior_pattern` | Population | Recurring pattern discovered through clustering |

> `case_type` is the setup, `run_outcome` is the ending, `eval_finding` is the local symptom, `behavior_pattern` is the population pattern.

## Lower-Level Evals: 5 Rubrics via Promptfoo

| Rubric | Evaluation Content |
|--------|-------------------|
| `final_decision_quality` | Does the final decision match the identified problem and terminal state? |
| `policy_compliance_correctness` | Are pricing/tariff/incentive/regional constraints being followed? |
| `routing_specialist_activation` | Was the appropriate specialist agent activated for the case? |
| `market_drift_awareness` | Does it recognize changing market conditions (tariffs, supply fluctuations)? |
| `review_appropriateness` | Is review/escalation proportional to risk? |

Each rubric produces pass/fail per trace. Failed rubrics become `eval_finding`.

In a 1000-case synthetic dataset, a typical trace includes ~170 events, ~15 handoffs, ~15 tool calls, ~8 agents, and ~4 environmental signals. Promptfoo failures concentrated in `final_decision_quality`.

## Analysis Dataset Construction

Normalized into 2 tables:

| Table | Granularity | Content |
|-------|-------------|---------|
| `traces_df` | Per run (1 row/run) | Metadata, results, findings, trace document |
| `events_df` | Per event (1 row/event) | Handoffs, tool calls, status, responses, review markers |

**Trace document**: Compressed text passed to clustering. Contains business setup, execution results, key handoffs, finding markers, and state transition digest.

**Impact score** (for prioritization):

```
impact_score = severity_weight × (1 + findings_count) × (1 + loop_count / 4)
```

Severity mapping:

| Outcome Group | Severity | Weight |
|--------------|----------|--------|
| successful_completion | low | 1.0 |
| review_escalation | medium | 2.0 |
| in_progress | medium | 1.5 |
| blocked | high | 2.5 |
| hard_failure | high | 3.0 |

## BERTopic-Style Macro Discovery Pipeline

Run only on traces with failures, reviews, or Promptfoo signals, using a modular pipeline:

```
Embed (vectorize) → Reduce (UMAP dimensionality reduction) → Cluster (HDBSCAN) → Label (characteristic term extraction)
```

**Term score** (characteristic degree of term t in cluster k):

```
score(t, k) = tf(t, k) × log((1 + N) / (1 + df(t)))
```

**Pattern prioritization**:

```
impact_score(k) = prevalence_share(k) × severity_weighted_prevalence(k)
```

High-frequency, high-severity patterns with concentrated traces yield high impact. This is a practical triage score, not a universal risk formula.

**3 output views:**
1. **Topic leaderboard**: Pattern ranking by impact
2. **Trace scatter map**: Each trace colored by behavior pattern on UMAP-reduced space
3. **Lift heatmap**: Concentration of behavior patterns per `case_type` (which scenarios trigger which patterns)

## AgentTrace-Style Root Cause Diagnosis

While discovery answers "what repeats," diagnosis asks "where to investigate first."

For a selected behavior pattern, the execution graph `G = (V, E)` is reconstructed. A backward walk from the focus event (anchor) yields weighted suspect scoring:

```
suspect_score = 0.4·proximity + 0.3·frequency + 0.2·bridge + 0.1·role
```

| Component | Weight | Meaning |
|-----------|--------|---------|
| Proximity | 0.4 | Distance to focus event |
| Frequency | 0.3 | Recurrence across sample traces in the same behavior pattern |
| Bridge | 0.2 | Degree of connection between parts of the execution graph |
| Role | 0.1 | Relevance of agent/tool role to findings |

> This is not proof of causation, but a translation from "this pattern matters" to "investigate these agents, tools, handoffs, and review policies first."

## Simulation: EV Order Workflow

Synthetic EV ordering and post-configuration workflow built on the OpenAI Agents SDK. Reflects real-world constraints:

- Component availability and supplier substitution
- Factory capacity and production scheduling
- Pricing exceptions, promotions, and incentives
- Tariffs and dated market signals
- Regional compliance constraints
- Escalation and review thresholds

Specialist agents: Orchestrator → validation, supply risk, procurement, capacity, factory routing, pricing, compliance, customer communications, release review. Full audit trail maintained via handoffs, function tools, guardrails, structured outputs, and tracing.

## Practical Application Steps

**For AI engineering teams:**
1. Promote the clearest lower-level eval failures to regression suites
2. Review samples of automated grades to calibrate rubric strictness
3. Track behavior patterns by model version, prompt version, and orchestration mode
4. Assign business owners to highest-impact patterns
5. Investigate top suspects (agents, tools, handoffs) before making system changes

**For business stakeholders:**
- Judge whether generated case types match real operational risks
- Confirm that high-impact patterns correspond to important customer or operational outcomes
- Verify that review thresholds produce intended business behaviors
- Prioritize policy and process design via Sankey and heatmap views

## Relationship to Other Evaluation Approaches

| Approach | Scope | Relationship |
|----------|-------|-------------|
| [[evals-for-ai-agents]] (Anthropic) | Basic structure, pitfalls, and scoring methods for agent evaluations | Foundation. Macro evals build the population layer on top |
| [[infrastructure-noise-agent-evals]] | Impact of infrastructure noise on agent evaluations | Complementary perspective on evaluation infrastructure reliability |
| [[ai-resistant-evaluations]] | Robustness design of evaluations themselves | Lower-level eval design principles |
| [[comparisons/evals-skills]] | Evaluation skills for coding agents | Different approach: MCP + skills for evaluation automation |
| [[concepts/harness-engineering]] | OpenAI's AI-assisted development approach | Inspiration source for self-verification using traces |

## Tool Stack

| Tool | Role |
|------|------|
| **[[promptfoo]]** | Agent-level lower-level eval (rubric evaluation) |
| **OpenAI Agents SDK** | Multi-agent system construction (handoffs, guardrails, structured outputs, tracing) |
| **BERTopic** (BERTopic family) | Topic modeling via UMAP + HDBSCAN + c-TF-IDF |
| **AgentTrace** | Root cause diagnosis via execution graph backward walk |
| **Plotly / Sankey** | Label chain visualization, heatmaps, scatter plots |

## References

- [Macro Evals for Agentic Systems — OpenAI Cookbook](https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems) — Shikhar Kwatra, Will Thieme, Bradley Strauss (OpenAI × Slalom)
- [BERTopic Documentation](https://maartengr.github.io/BERTopic/)
- [Promptfoo: OpenAI Agents Provider](https://www.promptfoo.dev/docs/providers/openai-agents/)
- [AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems](https://arxiv.org/abs/2505.12345)
