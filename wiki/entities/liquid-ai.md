---
title: "Liquid AI"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - company
  - non-transformer
  - llm
  - shopify
  - ai-infrastructure
aliases:
  - Liquid
  - Liquid Foundation Models
sources:
  - raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--32394213.md
  - https://www.liquid.ai/
---

# Liquid AI

**Liquid AI** is a company developing **non-transformer neural network architectures** for large language models. Their technology is notable for being deployed in production at [[entities/shopify|Shopify]], where CTO [[entities/mikhail-parakhin|Mikhail Parakhin]] has called it "the first genuinely competitive non-transformer architecture" he has used in practice.

## Architecture

Liquid AI develops **Liquid Foundation Models (LFMs)** — neural architectures that diverge from the standard Transformer design. Key characteristics:

- **Recurrent/continuous-time dynamics** — unlike Transformers' parallel attention, Liquid's architecture processes sequences through stateful recurrence
- **Efficient inference** — lower latency than Transformer equivalents at comparable capability
- **Scalable** — the architecture can handle large-scale workloads

## Shopify Deployment

At Shopify, Liquid AI models are used for:

| Workload | Description |
|----------|-------------|
| **Low-latency query understanding** | Real-time search query processing where response time matters |
| **Large-scale catalog workloads** | Processing millions of product entries efficiently |
| **Sidekick Pulse tasks** | Shopify's AI assistant infrastructure |

CTO Mikhail Parakhin's assessment:
> "Liquid AI is the first genuinely competitive non-transformer architecture I've used in practice."

He remains pragmatic about model choice — if Liquid can scale to frontier-level with enough compute, Shopify would adopt it. The key question is whether Liquid's architecture can compete at the scale of 100B+ parameter models.

## Market Position

Liquid AI competes in the emerging "post-Transformer architecture" space alongside:
- **Mamba/SSM** (State Space Models) — Albert Gu, Tri Dao
- **RWKV** — Bo Peng
- **RetNet** — Microsoft Research
- **Hyena** — Stanford

The competitive advantage of non-Transformer architectures is typically **inference efficiency** — linear scaling with sequence length vs. quadratic for attention.

## Relationship to Shopify

Shopify is both a customer and a public advocate for Liquid AI. Mikhail Parakhin has spoken publicly about Liquid's performance in production, which is unusual — most companies keep their model vendor choices private. This public endorsement signals Shopify's confidence in the technology and helps validate non-Transformer architectures for the broader industry.

## Key People

- **Ramin Hasani** — CEO/Co-founder, researcher in neural ODEs and liquid time-constant networks (MIT background)
- **Mathias Lechner** — Co-founder/CTO, creator of Liquid Time-Constant Networks
- **Alexander Amini** — Co-founder

The company originated from research at MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL), where the founders developed **Liquid Time-Constant Networks (LTCs)** — a class of neural ODEs inspired by biological neural circuits (specifically, the nematode *C. elegans* connectome).

## Technical Origins

Liquid AI's architecture is based on **Liquid Time-Constant Networks**, introduced in a 2021 Nature Machine Intelligence paper. LTCs are continuous-time recurrent neural networks where each neuron's time constant is learned dynamically, allowing the network to adapt its temporal dynamics to the input. This is fundamentally different from both Transformers (fixed attention windows) and standard RNNs (fixed time constants).

## Cross-References

- **[[entities/mikhail-parakhin]]** — Shopify CTO, public advocate for Liquid AI
- **[[entities/shopify]]** — Customer and deployment platform
- **[[concepts/transformer-alternatives]]** — Liquid is a key player in the post-Transformer architecture space
- **[[concepts/ai-agent-engineering]]** — Liquid's efficiency matters for agent inference workloads

## Sources

- [Latent Space: Shopify's AI Phase Transition](https://open.substack.com/pub/latent_space/p/shopifys-ai-phase-transition) — Mikhail Parakhin on Liquid AI at Shopify (Apr 2026)
- [Liquid AI](https://www.liquid.ai/) — Company website
- "Liquid Time-Constant Networks" (Nature Machine Intelligence, 2021) — Hasani, Lechner, Amini et al.
