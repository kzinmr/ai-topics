---
title: "MLOps"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - mlops
  - ml-engineering
  - devops
  - production-ml
  - infrastructure
sources: []
aliases:
  - mlops
  - ML Ops
---

# MLOps

**MLOps** is the application of DevOps/SRE practice to machine-learning systems: treating models, datasets, and training pipelines as production artifacts with versioning, automation, monitoring, and rollback. In the LLM era the term has broadened from "model deployment pipelines" to cover **the full lifecycle of training, serving, evaluating, and observing LLM-based applications**.

## The classic pipeline

```
Data ──▶ Feature/ingest ──▶ Training ──▶ Evaluation ──▶ Registry ──▶ Serving
  │            │                │             │             │          │
  └── versioning (datasets)     │             │             │          └── A/B, canary, rollback
                     experiment tracking       │        model cards
                (MLflow, W&B)                  │
                              eval harnesses / gates
```

| Concern | Classic MLOps | LLM-era MLOps |
|---|---|---|
| Artifact | Trained weights + feature transform | Model + prompt + eval suite + harness config |
| Validation | Offline metrics (AUC, RMSE) gate deploys | Evals/LLM-as-judge + regression suites ([[concepts/evaluation/ai-evaluation]]) |
| Serving | Batch or low-latency RPC | Token streaming, KV-cache management, batching ([[concepts/vllm]], [[concepts/inference]]) |
| Monitoring | Drift in features/predictions | Token cost, latency, hallucination/quality probes, user-feedback loops |
| Rollback | Redeploy prior model | Swap model/prompt/route ([[concepts/model-routing]] territory) |

## Tooling landscape (as covered in this wiki)

- **Orchestration/pipelines**: Flyte, Airflow, Dagster, Metaflow
- **Experiment tracking**: MLflow, Weights & Biases
- **Serving**: vLLM, SGLang, TGI, tensorizer-based loaders
- **Data**: Databricks/Snowflake platforms, data-versioning tools (Dolt — [[entities/dolt]])
- **Eval**: [[concepts/ai-benchmarks/lighteval|LightEval]], lm-evaluation-harness, LangSmith-style traces

## MLOps vs. agent ops

A recurring 2025–2026 distinction: classical MLOps manages *models*; **agent ops** (observability, tracing, sandboxing, cost governance) manages *loops* — multi-step tool-using systems whose failure modes are behavioral, not statistical. See [[concepts/observability-monitoring-tracing-opentelemetry-llm-agents-debugging]] and [[concepts/agent-deployment-engineering]]. Chip Huyen's [[entities/chip-huyen|Chip Huyen]] (Designing Machine Learning Systems) remains the standard systems-level framing; [[concepts/model-training-as-code]] covers the "pipelines as code" extreme.

## Related

- [[concepts/devops]] — parent discipline
- [[concepts/production-ai-agents]] — agent-era successor concerns
- [[concepts/evaluation/ai-evaluation]] — evals as the deploy gate
- [[concepts/inference]] — serving layer
- [[entities/chip-huyen]] — canonical textbook author
