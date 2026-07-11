---
title: "Provisioned Throughput"
created: 2026-07-08
updated: 2026-07-09
type: concept
tags:
  - inference
  - infrastructure
  - pricing
  - open-source
  - llm-inference
  - token-economics
  - cost-optimization
  - ai-infrastructure
  - production-ml
  - serverless
sources:
  - raw/articles/2026-07-08_together-ai_provisioned-throughput.md
---

# Provisioned Throughput

Provisioned Throughput is a reserved-capacity inference form factor that bridges the gap between serverless (best-effort) and dedicated (GPU-hour) inference. Introduced by [[entities/together-ai]] in July 2026, it offers token-based pricing with a 99% uptime SLA for frontier open-weight models, without requiring users to manage serving infrastructure or negotiate GPU reservations.

## The Market Gap

Before Provisioned Throughput, teams using open-weight models in production faced an uncomfortable choice:

- **Serverless inference**: Convenient, pay-per-token, but best-effort — no latency guarantees, cold starts, unsuitable for production workloads with predictable demand.
- **Dedicated inference**: Guaranteed capacity on reserved GPU clusters, but requires capacity planning, GPU-hour math, and configuring serving stacks like [[concepts/vllm]] or SGLang.

Closed-model APIs (OpenAI, Anthropic, Google) offered the desired middle ground — token-based pricing with capacity guarantees — but only for proprietary models. Provisioned Throughput brings this same operating model to open-weight models.

## Key Features

- **Token-based pricing with reserved capacity**: You pay per input/output token, not per GPU-hour. No capacity planning required.
- **99% uptime SLA**: Production-grade reliability for open-model inference.
- **Pre-optimized models**: No serving infrastructure to configure — models come pre-deployed on Together's optimized inference stack.
- **Global availability**: Capacity in North America, EMEA, and additional regions.
- **One-month minimum term**: Lower commitment than long-term GPU reservations.
- **Initial model support**: MiniMax M3 and GLM-5.2 at launch, with more expected.

## Cost Advantage

Provisioned Throughput pricing runs up to **90% below Claude Opus 4.8 list price**. Companies using Together AI for open-model inference report **6-20x cost savings** compared to equivalent proprietary APIs. This has made inference spend "a line item the board asks about" and driven rapid migration of workloads from closed APIs to open alternatives.

## Market Context

Together AI's inference token volume grew from **30 billion to over 400 trillion tokens per month** in nine months, with a substantial share of that traffic representing workloads that previously ran on closed-model APIs. This growth signals that open-model inference is not just a cost-saving measure but an increasingly viable production infrastructure layer.

The launch of Provisioned Throughput represents the maturation of the [[concepts/llm-inference]] market from "best effort" to "production SLA," positioning open-weight models as first-class citizens in enterprise AI stacks. See also: [[concepts/ai-industry-economics]] for the broader financial context driving this shift.

## Relationship to Other Inference Approaches

| Approach | Pricing | Capacity | SLA | Management Overhead |
|---|---|---|---|---|
| Serverless | Per-token | Best-effort | None | None |
| **Provisioned Throughput** | **Per-token** | **Reserved** | **99%** | **None** |
| Dedicated | Per GPU-hour | Reserved | Custom | High |

Provisioned Throughput sits at an optimal point for production teams: the simplicity of serverless with the guarantees of dedicated.

## Strategic Significance

As companies adopt [[concepts/open-source-ai]] models for coding agents, financial analysis, marketing automation, and workflow orchestration, the need for predictable inference economics becomes critical. Provisioned Throughput removes the operational burden that previously made open-model inference a second-class option relative to proprietary APIs.

For deeper technical context on the serving infrastructure this abstracts away, see [[concepts/llm-inference-optimization-performance]].

## Open Questions

- Will other inference providers (Fireworks, Groq, Replicate) offer similar reserved-token-capacity products?
- How will Provisioned Throughput pricing evolve as model architectures become more efficient (see: [[concepts/token-economics]])?
- Does the 99% SLA extend to latency guarantees, or only availability?
- When will the model catalog expand beyond MiniMax M3 and GLM-5.2?
