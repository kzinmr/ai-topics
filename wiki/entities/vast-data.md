---
title: "VAST Data"
type: entity
created: 2026-07-20
updated: 2026-07-20
tags: [company, ai-infrastructure, storage, data-layer, active]
sources:
  - raw/newsletters/2026-07-19-you-re-wasting-a-lot-of-money-exclusive-interview-with-vast-data-s-sven-breuner-.md
---

# VAST Data

## Overview

VAST Data is a data storage and AI infrastructure company valued at $30B. The company has developed a data-centric platform designed to eliminate GPU starvation — the problem where expensive GPUs sit idle waiting for data — by rethinking the storage and data layer for AI workloads.

## Sven Breuner

Sven Breuner is VAST Data's Field CTO. Before joining VAST Data, he spent 10 years at Fraunhofer as the lead architect of the BeeGFS parallel file system, giving him deep expertise in high-performance storage for compute-intensive workloads.

## Data Layer Philosophy

VAST Data's core thesis is that the data layer determines whether GPU investments pay off. The company's data-centric design philosophy addresses the "GPU starvation" problem, where expensive GPUs remain idle because the data layer cannot feed them fast enough. As Breuner puts it: "You're wasting a lot of money" if the data pipeline is not optimized for AI workloads.

## AI Infrastructure

Breuner describes the cold archive as the "crown jewel of enterprise AI" — the underutilized long-term data stores that contain the most valuable training material. VAST Data's vision includes an AI Operating System that orchestrates across the full data lifecycle, and addresses how security requirements are changing the intersection of training and inference pipelines.

## Related

- [[concepts/gpu-cluster-tco-goodput]]
- [[concepts/ai-infrastructure-circular-financing]]
