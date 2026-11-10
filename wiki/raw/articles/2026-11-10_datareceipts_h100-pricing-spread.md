---
title: "109 — What an H100 actually costs per hour (datareceipts)"
url: "https://github.com/datareceipts/data-receipts/tree/main/109-gpu-pricing"
source: "github.com/datareceipts"
fetched_at: 2026-11-10T12:15:00+00:00
type: article
tags: [raw]
sha256: 22f17a95c515a1eac722b4cbb605452e649f8486b363d9d851cb7eb9b1ea3836
---

# 109 — What an H100 actually costs per hour

Source: https://github.com/datareceipts/data-receipts/tree/main/109-gpu-pricing
(HN 170pts/87c, item 50427085)

On-demand GPU rental prices across AWS, Azure and the neoclouds, normalised to dollars per GPU per hour and
grouped so only identical GPUs are compared.

## Result

| H100 SXM 80GB | $/GPU-hr | A month (730 h) |
|---|---|---|
| RunPod Community | $2.69 | $1,964 |
| RunPod Secure | $3.99 | $2,913 |
| AWS p5.48xlarge | $6.88 | $5,022 |
| Azure ND96isr_H100_v5 | $12.29 | $8,972 |

4.57x between cheapest and dearest, for the same chip. One GPU running continuously for a month is $1,964 or
$8,972 depending only on where you rent it.

## The comparison is grouped, deliberately

"An H100" is three different products: SXM 80GB, PCIe 80GB, NVL 94GB all get marketed as H100s and do not
cost the same. Putting them in one chart manufactures a spread that isn't there, so every comparison is within
a single (model, memory) group. Same within a vendor: Azure lists the same A100 PCIe 80GB at one, two and
four GPUs per VM for $3.67, $4.78 and $4.78 per GPU-hour. The spread uses each vendor's cheapest route to a
given GPU, so an Azure-vs-Azure gap never shows up as a market gap. RunPod Secure and Community counted as
one company.

## What the 4.57x is not

It is not pure margin. Going from Azure's ND series to RunPod Community gives up:

- InfiniBand. Azure's ND SKU has 400 Gbps per GPU of Quantum-2 InfiniBand with GPU Direct RDMA, which is what makes multi-node training work. That is the reason the ND series is priced above Azure's own single-H100 NC SKU ($6.98).
- A datacentre SLA. RunPod Community is third-party hosts renting out their own hardware.
- Enterprise compliance, committed capacity, and the rest of the hyperscaler surface.

If you are fine-tuning on one node, you are giving up comparatively little for the 4.57x.
