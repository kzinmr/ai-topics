---
title: "SF Compute"
created: 2026-10-21
updated: 2026-10-21
type: entity
tags:
  - company
  - gpu
  - data-center
  - ai-infrastructure
  - ai-economics
  - market-dynamics
  - cloud-infrastructure
  - ai-industry
sources:
  - raw/newsletters/2026-10-20-the-programmable-data-center-evan-conrad-sf-compute.md
related:
  - entities/evan-conrad
  - concepts/gpu-compute-market
  - entities/coreweave
  - entities/nvidia
---

# SF Compute

SF Compute is a compute-markets company founded by [[entities/evan-conrad]] that operates a spot + forwards **order book for GPU capacity**, built around the thesis of "physical settlement" — delivering usable compute to the buyer rather than a cash payment against an index. Featured on Latent Space ("The Programmable Data Center", Oct 20 2026).

## What it does

- **Order book for compute capacity**: buyers/sellers attach constraints (time window, chip generation, interruption tolerance, storage, location) and SF Compute's matching engine matches them. Deliberately avoids premature contract standardization — heterogeneous SKUs are matched programmatically (e.g., "Blackwells at ≤$6/hr" can match GB300s or B300s).
- **Physical settlement**: borrowed from futures markets (oil, power). The buyer receives actually-usable compute. SF Compute co-designed physical settlement and the order book simultaneously.
- **Supercomputing-as-a-service**: SF Compute runs the entire operating stack of a cloud ("we do all the things a cloud does without being the cloud") — site visits, bill-of-materials design, OEM supply-chain relationships, cluster architecture, rack rollout supervision, backplane management (PDUs, switches, DPUs, UFM, BMC) — but **does not own the hardware**. Partners supply the data center / powered land; SF Compute supplies the supercomputing layer and the San Francisco offtake demand, including for sovereign-compute customers.
- **Programmable data center**: customers can subdivide their InfiniBand fabric on demand without asking the operator — "virtualizing the data center and making it programmable" (described as the last analogous shift being the cloud itself). Also described as "Palantir for compute".

## Key facts (Oct 2026 podcast)

- Liquidity metric: a customer spending $100 to buy capacity gets back ~$25 on average when it is resold; ~5% of total capacity is on the order book, expanding.
- Closed **several hundred million dollars of volume**; new clusters on the way; partner announcements pending.
- Cluster financing terms in the broader market: 3–5 years. Forward curve shape: a "hump" (near-term unsold capacity must drop to clear, then rises, then declines further out).
- Arbitrage cited: a B300 running inference earns ~$40/hr gross (~$25/hr at 50% utilization) while B300 capacity can be bought at $5–6/hr — "one of these numbers has to change".
- Competitors/partners: **Silicon Data** and Compute Exchange take the **cash-settled** path; SF Compute sees physical + cash settlement as complementary (cash derivatives should be *derived* from physical settlement). Ecosystem forming around standards (SemiAnalysis), residual-value insurance, and deposit/credit lending.

## Independence thesis

No incumbent can build a neutral compute exchange: NVIDIA, Crusoe, CoreWeave, Lambda, hyperscalers, BasisAI/Fireworks/Modal all have demand or hardware positions and could manipulate the forwards market — "you have to kill your business in order to make this". SF Compute must "be Switzerland": it deliberately does not own hardware. Precedent: **Nicira** (SDN startup, acquired by Nicira→VMware at $1.3B after Cisco $600m-scale networking M&A era) as the networking-market analog; negative oil futures (2020) as the physical-settlement weirdness cautionary tale; LIBOR manipulation as the index-manipulation risk warning for compute price indices.

## Related

- [[entities/evan-conrad]] — founder
- [[concepts/gpu-compute-market]] — the market structure SF Compute operates in
- [[entities/coreweave]] — GPU cloud (can't operate a neutral exchange per SF Compute's thesis)
- [[entities/nvidia]] — "800-pound gorilla" that benefits from but can't run the exchange

## Sources

- Latent Space (swyx): "The Programmable Data Center — Evan Conrad, SF Compute", 2026-10-20. https://www.latent.space/p/sfcompute2 — raw: `raw/newsletters/2026-10-20-the-programmable-data-center-evan-conrad-sf-compute.md`
