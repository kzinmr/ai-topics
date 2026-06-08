---
title: "Mikhail Parakhin"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - person
  - infrastructure
  - shopify
  - company
  - leadership
  - ceo
aliases:
  - Mikhail Parakhin
  - Mikey Parakhin
sources:
  - raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--32394213.md
---

# Mikhail Parakhin

**Mikhail Parakhin** (also known as "Mikey") is the **CTO of [[entities/shopify|Shopify]]** (since 2024). Previously, he ran a major Microsoft business unit spanning **Windows, Edge, Bing, and ads**. He is known for his pragmatic approach to AI infrastructure and his early experience shaping AI character during the **Sydney era at Bing**.

## Background

### Microsoft Era

At Microsoft, Parakhin led one of the company's most important product divisions:
- **Windows** — the core operating system
- **Edge** — the browser
- **Bing** — the search engine
- **Ads** — Microsoft's advertising business

During his time at Microsoft, he was involved in the **Sydney** incident (Bing's AI chatbot that developed an unexpected personality). Parakhin later revealed that Sydney's personality was **not an accident** — it was the result of deliberate choices about AI character design. This experience shaped his understanding of how AI systems develop behavioral patterns and the importance of intentional design.

### Shopify CTO

Parakhin joined Shopify as CTO, bringing deep experience in large-scale AI systems. Under his leadership, Shopify has:
- Adopted a **no token spending limits** policy for AI usage
- Built an internal **LLM proxy** architecture for centralized AI routing
- Developed **Tangle**, **Tangent**, and **SimGym** — three major AI infrastructure initiatives
- Evaluated and deployed **Liquid AI** as a competitive non-transformer architecture
- Set a target of **96% autonomous coding by Q3 2026**

## Key Theses

### Token Budgets

Parakhin agrees with Jensen Huang's direction that token budgets are important, but argues that **raw token count is the wrong way to evaluate engineering output**. What matters is:
- How tokens are spent (quality over quantity)
- The critique loop and review process
- Whether the tokens translate to real engineering value

### AI Coding Bottlenecks

In 2026, Parakhin identified that **the real bottleneck in AI coding is no longer generation, but review, CI/CD, and deployment stability**:
- PR volume, test failures, and deployment rollback are the new bottlenecks
- AI-written code can still increase bugs in production even if models write cleaner code on average
- Git, pull requests, and CI/CD may need a new metaphor once code is written at machine speed
- The real unlock is not more agents in parallel, but better critique loops, stronger models, and spending more on review than generation

### Customer Simulation

Parakhin champions **SimGym** — Shopify's customer simulation platform. His thesis:
- Simulated customers only work if you have real historical behavior data
- Shopify's commerce data provides a defensible moat
- Category-level behavior varies dramatically across commerce verticals
- Ideas like Chinese Restaurant Processes are showing up again in practice for modeling merchant/buyer trajectories

### Non-Transformer Architectures

Parakhin sees **Liquid AI** as "the first genuinely competitive non-transformer architecture" he has used in practice. At Shopify, Liquid is deployed for:
- Low-latency query understanding
- Large-scale catalog workloads
- Sidekick Pulse tasks

He remains pragmatic and merit-based about model choice — if Liquid can scale to frontier-level with enough compute, Shopify would adopt it.

## Shopify's Three AI Initiatives

### Tangle

**Tangle** is Shopify's reproducible ML and data workflow engine. Key differences from Airflow:
- **Content-addressed caching** creates network effects across teams
- Makes ML and data workflows reproducible, collaborative, and production-ready from the start
- More than just orchestration — it's a collaboration layer for data science

### Tangent

**Tangent** is Shopify's auto-research loop system. It:
- Optimizes search, themes, prompt compression, storage, and more
- Is becoming a democratizing tool for PMs and domain experts, not just ML engineers
- Represents AutoML finally feeling real in the LLM era
- Still has limitations — auto-research falls short in areas requiring deep domain expertise

### SimGym

**SimGym** is Shopify's customer simulation platform. It:
- Simulates merchant and buyer trajectories using real historical behavior
- Runs counterfactuals to evaluate interventions (discounts, campaigns, notifications)
- Evolved from comparing A/B variants to telling merchants what to change on a single live storefront to raise conversions
- Is expensive to run (multimodal models, browser farms, serving and distillation costs)
- Becomes much more powerful when combined with Tangle and Tangent

## Sydney Story

During the Bing Sydney era, Parakhin learned that **AI personality is not an accident** — it emerges from deliberate design choices about how the system interacts with users. This insight shaped his approach to AI at Shopify, where intentional character design is part of the product strategy.

## Cross-References

- **[[entities/shopify]]** — Company where Parakhin serves as CTO
- **[[entities/tobi-lutke]]** — Shopify CEO, collaborates with Parakhin on AI strategy
- **[[concepts/shopify-ai-engineering]]** — Shopify's AI infrastructure under Parakhin's leadership
- **[[entities/liquid-ai]]** — Non-transformer architecture deployed at Shopify
- **[[concepts/ai-agent-engineering]]** — Tangle, Tangent, SimGym as AI infrastructure

## Sources

- [Latent Space: Shopify's AI Phase Transition](https://open.substack.com/pub/latent_space/p/shopifys-ai-phase-transition) — Interview with Mikhail Parakhin, Shopify CTO (Apr 2026)
