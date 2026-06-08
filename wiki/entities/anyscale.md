---
title: "Anyscale"
type: entity
created: 2026-05-08
updated: 2026-06-03
tags:
  - company
  - infrastructure
  - open-source
  - developer-tooling
sources:
  - https://www.anyscale.com
  - raw/articles/anyscale.com--blog-aks-support-multi-cloud-global-resource-scheduler--1149a504.md
  - https://www.anyscale.com
---

# Anyscale

Anyscale is the company behind Ray, the open-source unified framework for scaling AI and Python applications from a laptop to a cluster. It provides a managed platform for distributed computing, enabling developers to build, train, and serve ML models at any scale without distributed systems expertise.

| | |
|---|---|
| **Type** | AI Infrastructure / Distributed Computing |
| **Founded** | 2019 |
| **Leadership** | Keerti Melkote (CEO), Robert Nishihara (Co-Founder) |
| **Key Products** | Ray (open-source framework), Anyscale Platform, Anyscale Agent Skills |
| **Website** | [anyscale.com](https://www.anyscale.com) |
| **Tech Blog** | [anyscale.com/blog](https://www.anyscale.com/blog) |

## Key Facts
- Founded by Ray creators Robert Nishihara, Philipp Moritz, Ion Stoica, and Michael I. Jordan from UC Berkeley RISELab.
- Keerti Melkote (formerly founder of Aruba Networks) appointed CEO in July 2024.
- Ray is used by companies including Amazon, Microsoft, Ant Financial, and Intel.
- Raised $20.6M Series A in 2019 led by Andreessen Horowitz.

## Products & Technology
- **Ray**: Open-source unified compute framework for scaling Python/ML workloads across clusters.
- **Anyscale Platform**: Managed Ray service with enterprise features, scheduling, and observability.
- **Agent Skills for Ray**: GA capability for deploying AI agent workflows on Ray infrastructure.

## Multi-Cloud & Platform Expansion (June 2026)

Anyscale announced a major multi-cloud expansion (June 2026) to address the growing need for cross-cloud AI workload flexibility:

| Capability | Description |
|------------|-------------|
| **AKS First-Class Support** | Full support for Azure Kubernetes Service with Blob Storage integration, advanced logging, and monitoring within Anyscale console. Completes support across all three major CSPs. |
| **Global Resource Scheduler (GRS)** | Intelligent workload allocation across GPU capacity commitments to maximize utilization and prevent premium hardware from sitting idle. |
| **Multi-Deployment Management** | (Coming soon) Unified control plane for deploying across multiple providers, regions, and compute stacks from a single interface. |

The expansion is driven by GPU scarcity and cost optimization needs — organizations must run AI workloads wherever the latest, most cost-effective, or available hardware resides. Anyscale's approach positions Ray as the common compute framework across heterogeneous cloud environments.

Source: raw/articles/anyscale.com--blog-aks-support-multi-cloud-global-resource-scheduler--1149a504.md

## Related
- [[entities/openai]] — AI model provider; Ray often used for training/scaling models
- [[entities/anthropic]] — another AI infrastructure consumer
- [[concepts/distributed-computing]] — core paradigm of Ray
