---
title: "Model Training as Code"
created: 2026-06-29
updated: 2026-06-29
type: concept
tags: [model-training-as-code, model-training, training, post-training, pretraining, mlops, ml-engineering, workflow, experiment-tracking, developer-tooling, automation, reliability, flyte, weights-and-biases]
sources: [raw/articles/2026-05-22_aleph-alpha_model-training-as-code.md]
---

## Discriminative Summary

Model Training as Code (MTaC) is an engineering paradigm that expresses the entire model training pipeline — pre-training, supervised fine-tuning (SFT), reinforcement learning (RL), evaluation, and artifact management — in imperative code rather than as a sequence of manual hand-offs between specialized teams. Unlike [[mlops]], which focuses on the operational infrastructure around model deployment and monitoring, MTaC codifies the training recipe itself as a collaborative software artifact. Unlike experiment tracking tools (e.g., [[weights-and-biases]]), which log metrics after the fact, MTaC makes the pipeline’s logic, configuration, and provenance first-class citizens of the codebase from the start. And unlike Infrastructure as Code, which provisions cloud resources declaratively, MTaC expresses the full training workflow — data ingestion, training loops, checkpoint evaluation, and sweeps — as composable functions under version control.

MTaC was pioneered at Aleph Alpha through their internal model factory, Savanna, which implements post-training pipelines as async functions with typed inputs/outputs, enabling one-click end-to-end runs, hermetic reproducibility, and trunk-based collaboration across capability-oriented teams.

## Overview

Modern model training has grown beyond the capacity of any single team. Pre-training alone involves data curation, architecture design, distributed orchestration, and mid-training evaluation. Post-training adds SFT and RL stages, each with distinct tools, skillsets, and hyperparameter spaces. In a manual lab, these stages are glued together by Slack messages, filesystem paths, and institutional memory — a process that introduces three hidden costs:

1. **Human error**: Every manual step (copying a checkpoint path, setting a flag, clearing disk space) is an opportunity for a costly mistake.
2. **Lost learnings**: Without a durable record, teams repeat experiments and forget the rationale behind hyperparameter choices.
3. **Fragmented ownership**: When teams only own their slice of the pipeline, integration happens rarely and divergence accumulates.

MTaC addresses all three by lifting the pipeline into code — a shared, version-controlled, executable artifact that every team can read, modify, and run.

## Core Principles

### Composability

In MTaC, each pipeline stage is a function with typed inputs and outputs. This transforms manual steps into building blocks that can be composed into end-to-end pipelines:



Composability enables:
- **One-click launches**: The full pipeline runs from a single entry point.
- **Programmatic experimentation**: Sweeps over hyperparameters require only a nested loop calling the pipeline function with different configs.
- **Subset testing**: Downscaled or partial runs for validation without touching production code.

### Consensus

Consensus comes from version control. The main branch represents the team’s collective best understanding of how to train a model. The code contains the full training recipe — configuration, hyperparameters, data references, and environment specifications — so there is no setup to reconstruct or flag to forget when launching a run. This eliminates the “reconstruction from memory” anti-pattern that plagues manual labs.

Trunk-based development (see [[main-branch-development]]) is essential: changes land on main in small increments so teams can build on each other’s work immediately. Long-lived branches recreate the same integration debt that MTaC is designed to eliminate.

### Provenance

Provenance comes from code comments, commit history, and immutable artifact registries. Every training run is linked to a specific git commit, making past runs reproducible by checking out the code and relaunching. Decision lineage — why a hyperparameter has its current value, which dataset a model was trained on — lives in `git blame` and the artifact lineage graph, not in Slack search.

Savanna extends this with artifact lineage: all non-code artifacts (datasets, models, tokenizers) are immutable and versioned in a registry. When a run completes, the referenced artifacts, training logs, metrics, and evaluation results are all linked to that run and its output checkpoint.

## Comparison to MLOps and Infrastructure as Code

| Dimension | Model Training as Code | [[mlops]] | Infrastructure as Code |
|---|---|---|---|
| **Primary focus** | The training pipeline logic, configuration, and execution | Operational lifecycle of ML models (deployment, monitoring, retraining) | Provisioning and managing cloud/server infrastructure |
| **What is codified** | Training recipe: data mix, architecture, hyperparameters, evaluation, sweeps | Model serving, CI/CD for ML, feature stores, model registry, monitoring | Compute, networking, storage resources (VMs, clusters, DBs) |
| **Version control role** | Source of truth for how a model is trained; each run pinned to a commit | Versioning for models, datasets, and pipeline definitions (often YAML/DAGs) | Declarative desired state for infrastructure (Terraform, Pulumi) |
| **Key benefit** | Eliminates manual hand-offs between teams; enables capability-oriented teams | Standardizes the path from experimentation to production | Reproducible, auditable infrastructure provisioning |
| **Team structure** | Capability-oriented (teams own model behaviors end-to-end) | Temporal/stage-oriented (data eng → ML eng → DevOps) | Platform engineering / SRE teams |
| **Example tooling** | Savanna (Aleph Alpha), flyte, custom Python pipelines | MLflow, Kubeflow, SageMaker, LangSmith | Terraform, Pulumi, CloudFormation, Ansible |
| **Scope of "run"** | End-to-end training from data ingestion to final evaluation checkpoint | Model deployment, monitoring, and retraining triggers | Infrastructure apply/destroy lifecycle |

MTaC is complementary to both: it can use MLOps infrastructure (model registries, artifact stores) and IaC-provisioned compute, but its distinctive contribution is codifying the training logic itself as the primary collaborative artifact.

## Implementation

### Flyte Workflow Engine

Aleph Alpha’s Savanna uses flyte as the workflow orchestration layer. Flyte runs on Kubernetes and provides durable execution, sequencing, parallelism, automatic retries, and intelligent caching. When a pipeline stage completes, Flyte recognizes if subsequent stages share identical inputs and serves cached outputs, avoiding redundant GPU computation during sweeps.

Key workflow features:
- **CI as entrypoint**: Pushing to a branch triggers a Flyte job via GitHub Actions. Training the best model is as simple as triggering CI on main.
- **PR validation**: Small-scale end-to-end runs complete in under 5 minutes on pull requests, providing fast feedback.
- **Nightly regression**: Larger-scale training runs validate that the pipeline logic still produces models achieving measurable improvement on evaluation suites.
- **Incremental checkpoint evaluation**: For long-running pre-training or RL jobs, intermediate checkpoints are emitted and evaluated automatically.

### Weights and Biases Integration

[[weights-and-biases]] serves as the artifact registry and experiment tracking backbone. Model and data artifacts are stored immutably in on-prem object storage and versioned in W&B. This provides:
- **Immutable artifact references**: Training runs reference specific artifact versions, ensuring hermetic reproducibility.
- **Artifact lineage UI**: Interactive exploration of which datasets produced which models.
- **Automated cleanup policies**: Object storage lifecycle management via W&B artifact versioning.
- **Real-time metrics streaming**: Training metrics flow to a monitoring system for live progress tracking and alerting.

### Trunk-Based Development

MTaC’s full value depends on [[main-branch-development]]: changes merge to main frequently and in small increments. This enables:
- **Fast integration**: Teams build on each other’s work at the earliest opportunity.
- **Fail-fast experimentation**: A branch that runs CI with a new dataset or hyperparameter can be evaluated and merged within hours.
- **Reduced integration debt**: Avoids the month-long divergence that occurs with long-lived feature branches.

Savanna’s CI validates every pull request with a small-scale end-to-end training run, and nightly larger-scale tests catch semantic regressions. This mirrors standard software engineering practices applied to model training.

## Benefits

### Capability-Oriented Teams

Traditional labs decompose model training temporally: one team owns pre-training, another owns SFT, another owns RL. Each team optimizes for its own stage, and integration is a manual, infrequent hand-off.

MTaC enables a capability-based decomposition: teams own a **model behavior** (e.g., multilinguality, reasoning, safety) from end to end. A multilinguality team builds the SFT datasets, RL environments, and evaluation suites needed to make the model excel at a specific language and culture. Because any team can run the full pipeline, they can iterate on the model as a whole rather than just their slice.

This shifts the organizational bottleneck from coordination to execution, increasing the lab’s learning rate as teams grow.

### LLM Agent Auto-Research

With the entire pipeline in code, an LLM agent can read, modify, and run it autonomously. MTaC provides the structured interface — typed function signatures, version-controlled recipes, CI-based validation — that makes [[auto-research]] feasible. An agent can:

1. Read the current training recipe from the codebase.
2. Propose a change (new data mix, modified architecture, different hyperparameter).
3. Push to a branch and trigger CI.
4. Analyze the small-scale validation results.
5. Merge if improvements are confirmed, or iterate.

Aleph Alpha describes this as a key enabler for models that can self-improve via their own training factory. This connects MTaC to broader themes in [[agentic-engineering]], where the codebase becomes the interface between human researchers and autonomous experimentation agents.

## Related Topics

- [[mlops]] — Operational lifecycle management for ML models; MTaC focuses upstream on training logic
- [[main-branch-development]] — The version control practice essential to MTaC’s consensus principle
- [[post-training]] — The SFT and RL stages that MTaC pipelines typically orchestrate
- [[auto-research]] — Autonomous experimentation agents that MTaC makes feasible
- [[agentic-engineering]] — Engineering culture and practices for agent-native codebases
- [[weights-and-biases]] — Artifact registry and experiment tracking used in Savanna’s implementation
- flyte — Kubernetes-native workflow engine for durable training orchestration
