---
title: "China Datacenter Buildout"
created: 2026-11-08
updated: 2026-11-08
type: concept
tags:
  - infrastructure
  - data-center
  - china
  - ai-infrastructure
  - geopolitics
  - ai-energy
  - us-china-ai-race
  - company
sources:
  - raw/articles/2026-11-07_semianalysis-we-visited-chinas-stargate-inner-mongolia.md
related:
  - [[entities/envision-group]]
  - [[concepts/source-grid-load-storage]]
  - [[entities/semianalysis]]
  - [[entities/dylan-patel]]
  - [[concepts/nvidia-45c-data-center-cooling]]
  - [[concepts/subprime-data-center-crisis]]
  - [[concepts/data-center-local-backlash]]
  - [[concepts/us-china-ai-competition]]
---

# China Datacenter Buildout

First-hand account of China's hyperscale AI datacenter construction, from SemiAnalysis's September 2026 site visit to Inner Mongolia (published November 7, 2026, paywalled; this page captures the free portion only). The thesis: Inner Mongolia is "the West Texas of China" — but unlike Texas, which faces its highest-ever anti-datacenter sentiment (see [[concepts/data-center-local-backlash]]), Inner Mongolia is accelerating with no local backlash.

## Galaxy Campus, Ulanqab (the "China's Stargate")

- Owner: [[entities/envision-group|Envision Group]], a renewable systems integrator with 100GW+ of wind turbines installed worldwide; entered datacenters from energy management.
- Planned scale: **up to 800MW of IT capacity** — comparable to Stargate Abilene's core campus (~820MW critical IT out of Crusoe's 1.2GW, leased to Oracle for OpenAI). A later phase (converting the adjacent wind-turbine factory) could take Galaxy to ~1GW.
- **First 120MW phase delivered within a year at ~1/5 of US costs**; initial phase live August 2026, full campus expected complete by end of 2027. All four phases are built-to-suit for two (unnamed) internet giants.
- Surrounding Chahar High-tech Zone: ~30,000 construction workers across 22 datacenter projects (local report). Chinese datacenters rarely go fully modular — abundant labor keeps costs falling anyway.
- Envision's datacenter plans in Inner Mongolia total **3GW**; Galaxy is the first.

## Vertical integration as the differentiator

Envision supplies nearly every layer in-house: wind farms + dedicated power line (see [[concepts/source-grid-load-storage]]), its own turbines/converters/control software, AESC battery storage (cells → PCS → software, factory pre-configured), low-voltage power modules, the 800V system, and a co-designed prefabricated substation (<3 months vs ~6 months for a conventional indoor substation). Its blade factory sits across the road from the campus.

Comparison case: the **CATL × VNET × Zhongheng Electric** tie-up — in 2026 CATL became colocation operator VNET's largest shareholder and agreed to take a 49% stake in Zhongheng's controlling shareholder (Zhongheng = China's largest HVDC power-system supplier, working with Alibaba and ByteDance). CATL is also one of **DeepSeek's largest outside investors**, extending its reach to the model layer. Envision builds pieces in-house; CATL links them via partnerships and equity.

## Power economics

- Inner Mongolia holds ~57% of China's usable wind resources; ~2,800 full-load hours/year (CF ~32%) regionally, 35–40% at Ulanqab.
- Power ~**$0.055/kWh all-in** in Inner Mongolia — among the lowest in the world.
- DC rents roughly **halved in five years to ~$40/kW/month** (excluding power); capex down ~25% to **<$3mm/MW**. Market is hyper-competitive; IRRs are squeezed, so integrators' reward often comes from equipment demand or capital-markets effects, not DC margins.
- Region has **25GW of announced projects**, including several GW-scale campuses. SemiAnalysis disputes the "empty datacenter halls" narrative and analyzes the real constraints (power, land, water) in the paid section.
- Policy: approvals increasingly favor projects pairing compute with green power ("Compute Power Coordination"); Chifeng precedent — Envision's 2GW off-grid wind/solar/storage system feeding a green-ammonia plant plus a pilot datacenter on Tencent T-Block units, running entirely on power electronics with no synchronous generator.

## Power architecture: China's DC lead

- China Telecom 240V DC pilots (2007) → Alibaba Panama power system (2018) → today **~25% of Chinese datacenters built in the past decade run on DC**, while **~97% of US datacenters still use AC UPS**.
- Galaxy runs a **5MW solid-state-transformer (SST) pilot**: 10kV AC from the grid converted straight to **800V DC to the rack** at a live hyperscaler site, eliminating low-voltage transformers, UPS, and rectifier stages. This is the architecture NVIDIA is pushing for ~600kW Kyber racks; in the US it is still on the roadmap. A larger SST deployment is planned for Galaxy's next phase.
- Global convergence: US developers bridge power gaps with on-site gas turbines/fuel cells/BBUs; Malaysia requires ≥30% renewables and encourages on-site generation; "access to energy is becoming part of what a datacenter developer sells."

## Cooling: no central chiller

Galaxy uses a design common in Inner Mongolia: liquid- and air-cooled servers share one water loop with **no central chiller plant**. NVIDIA says Vera Rubin can run on 45°C water without chillers (see [[concepts/nvidia-45c-data-center-cooling]]), yet most US datacenters keep a chiller for air-cooled equipment and load-flexibility; Galaxy drops it while retaining much of that flexibility — a design running at scale in northern China for years, and a reference point for the US chiller debate.

## Open questions

- Whether vertical integration becomes a real ordering advantage (hyperscalers still choose on resources and track record).
- What actually limits Inner Mongolia development (power/land/water) — covered in the paywalled section and the promised follow-up report on the region's market.
- Speed/cost breakdown from land auction to customer acceptance — paywalled.

## Related

- [[entities/envision-group]] — Galaxy owner, SGLS pioneer
- [[concepts/source-grid-load-storage]] — source-grid-load-storage power model
- [[concepts/data-center-local-backlash]] — the US contrast: local consent as a new hard limit
- [[concepts/subprime-data-center-crisis]] — US financing-side risk analysis
- [[concepts/us-china-ai-competition]] — compute infrastructure dimension

## Sources

- [We Visited China's Stargate in Inner Mongolia — SemiAnalysis](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) (Everlyn Tan, Jeremie Eliahou Ontiveros, Xiaopeng Laoban, Dylan Patel; Nov 7, 2026). Paywalled: free preview only captured in raw.
