---
title: "DevOps"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - devops
  - ci-cd
  - software-engineering
sources: []
aliases:
  - devops
  - DevOps
---

# DevOps

**DevOps** is the engineering culture and toolchain practice of merging development and operations: shared ownership of production, automation of the path from commit to deployment (**CI/CD**), infrastructure-as-code, observability, and blameless incident response. Coined around 2009 (Patrick Debois, the first "DevOps engineer" at a government contractor; the O'Reilly *DevOps Handbook* codified it with Gene Kim et al.). Its core mechanisms — version control of everything, automated pipelines, small batch sizes, fast rollback — are the direct intellectual ancestors of [[concepts/mlops]] and, in the AI era, **agent ops**.

## The core loop

```
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor
  ▲                                                        │
  └──────────────── feedback (metrics, incidents) ◀───────┘
```

| Practice | Canonical tooling | AI-era echo |
|---|---|---|
| CI/CD | GitHub Actions, GitLab CI, ArgoCD | eval-gated model/prompt deploys |
| IaC | Terraform, Pulumi, CloudFormation | agent-managed infra (AWS Agent Toolkit) |
| Containers/orchestration | Docker, Kubernetes ([[concepts/kubernetes]]) | agent sandboxes, Firecracker microVMs |
| Observability | Prometheus, Grafana, OpenTelemetry | LLM trace/eval observability ([[concepts/observability-monitoring-tracing-opentelemetry-llm-agents-debugging]]) |
| SRE practice | SLOs, error budgets (Google SRE book) | token/cost budgets, agent reliability budgets |

## DevOps in the AI-agent era

Two active threads in this wiki connect DevOps to AI:

1. **AI-assisted DevOps** — coding agents operating CI pipelines, incident response, and infra (see [[concepts/managed-agents-sre-incident-response]], and the *sre-deskilling* concern about junior SRE pipelines drying up).
2. **DevOps-for-agents** — treating agent fleets as production systems: versioned prompts/harness configs, canary agent rollouts, trace-based debugging, and cost SLOs. This is what [[concepts/agent-deployment-engineering]] and [[concepts/mlops]]'s "agent ops" section cover. Chip Huyen ([[entities/chip-huyen]]) frames ML systems similarly: deployment and reliability dominate the work, not modeling.

## Related

- [[concepts/mlops]] — DevOps applied to ML lifecycles
- [[concepts/kubernetes]] — the container-orchestration substrate
- [[concepts/agent-deployment-engineering]] — agent-era successor
- [[concepts/observability-monitoring-tracing-opentelemetry-llm-agents-debugging]] — tracing LLM apps
- [[concepts/ci-cd]]-adjacent coverage in [[concepts/agent-deployment-engineering]]
