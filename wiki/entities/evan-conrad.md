---
title: "Evan Conrad"
created: 2026-10-21
updated: 2026-10-21
type: entity
tags:
  - person
  - company
  - gpu
  - ai-infrastructure
  - ai-economics
sources:
  - raw/newsletters/2026-10-20-the-programmable-data-center-evan-conrad-sf-compute.md
related:
  - entities/sf-compute
  - concepts/gpu-compute-market
---

# Evan Conrad

Founder of [[entities/sf-compute]], the compute-markets company building a physical-settlement spot + forwards order book for GPU capacity. Formerly founder of **Junark**, the cluster-sublease company SF Compute grew out of. Appeared on Latent Space twice: an original episode ~2 years before Oct 2026, and "The Programmable Data Center" (2026-10-20).

## Key ideas

- **Physical settlement first**: compute is not as fungible as financial markets assume; building financialization (cash-settled derivatives) before physical settlement infrastructure exists creates manipulable markets with basis risk — the CDS-vs-bonds (12x) and "made-up OpenAI shares" analogies. Cash settlement should be *derived from* physical settlement.
- **You can't standardize before you operate**: the path to standardized compute contracts runs through operating all the operations identically first (his earlier attempt to standardize contracts with the CFTC era failed because operations weren't yet uniform — e.g., two VM types from one operator differing 40% in GPU kernel-launch performance).
- **Neutrality requires giving up the money**: whoever runs the exchange must not own hardware or inference revenue, or they could manipulate the forwards market — which is why NVIDIA/clouds/inference companies structurally cannot build it.
- Markets framing from his derivatives-trading background: backwardation/contango of the compute forward curve, order-book dimensionality reduction, commodity-grade analogies (light sweet crude vs. "compute SKUs").

## Related

- [[entities/sf-compute]] — his company
- [[concepts/gpu-compute-market]] — market thesis

## Sources

- Latent Space: "The Programmable Data Center — Evan Conrad, SF Compute" (2026-10-20) — https://www.latent.space/p/sfcompute2
