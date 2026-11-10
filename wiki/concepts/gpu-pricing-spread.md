---
title: "GPU Pricing Spread (same H100, 4.57x price range)"
type: concept
created: 2026-11-10
updated: 2026-11-10
confidence: high
tags:
  - gpu
  - ai-infrastructure
  - cloud-infrastructure
  - economics
  - pricing
  - cost-optimization
sources:
  - raw/articles/2026-11-10_datareceipts_h100-pricing-spread.md
  - https://news.ycombinator.com/item?id=50427085
related:
  - "[[concepts/gpu-cloud-rankings]]"
  - "[[concepts/gpu-cluster-tco-goodput]]"
  - "[[concepts/ai-compute-pricing-paradox]]"
  - "[[entities/semianalysis]]"
---

# GPU Pricing Spread (same H100, 4.57x price range)

The **datareceipts** dataset (repo `datareceipts/data-receipts`, entry 109) normalized on-demand rental
prices for identical GPUs across hyperscalers and neoclouds into dollars per GPU-hour, and found a
**4.57x spread for the same chip**. HN 170pts/87c ([item 50427085](https://news.ycombinator.com/item?id=50427085), 2026-11-09).

## The numbers (H100 SXM 80GB)

| Provider | $/GPU-hr | Month (730h) |
|---|---|---|
| RunPod Community | **$2.69** | $1,964 |
| RunPod Secure | $3.99 | $2,913 |
| AWS p5.48xlarge | $6.88 | $5,022 |
| Azure ND96isr_H100_v5 | **$12.29** | $8,972 |

One H100 running a month costs $1,964 or $8,972 **depending only on where you rent it**.

## Methodology matters more than the headline

- **Grouped comparisons**: "an H100" is really three products (SXM 80GB, PCIe 80GB, NVL 94GB); mixing them manufactures fake spread. Every comparison is within a single (model, memory) group.
- **Cheapest-route normalization**: uses each vendor's cheapest path to a given GPU, so intra-vendor gaps (e.g. Azure listing the same A100 PCIe at $3.67–$4.78 depending on VM size) don't masquerade as market gaps.
- **The spread is not pure margin**: Azure ND's premium buys 400 Gbps/GPU Quantum-2 InfiniBand with GPUDirect RDMA (what makes multi-node training work), a datacentre SLA, enterprise compliance, and committed capacity. RunPod Community is third-party hosts renting personal hardware. Single-node fine-tuners give up comparatively little for 4.57x.

## Why it matters for the AI cost debate

The spread quantifies how much of "AI compute is expensive" is a **procurement-tier artifact** rather than a
hardware reality — a demand-side footnote to [[concepts/ai-compute-pricing-paradox]] (which argues inference
costs rise as models improve) and adjacent to the credit-stress thread in [[entities/coreweave]]: if
commodity GPU hours clear at <$3, neocloud debt at 16% yields is pricing a very different world than the
spot market for single-node workloads. Compare structured rankings in [[concepts/gpu-cloud-rankings]]
(ClusterMAX) and TCO/goodput accounting in [[concepts/gpu-cluster-tco-goodput]].

## Sources

- https://github.com/datareceipts/data-receipts/tree/main/109-gpu-pricing (raw: raw/articles/2026-11-10_datareceipts_h100-pricing-spread.md)
- https://news.ycombinator.com/item?id=50427085
