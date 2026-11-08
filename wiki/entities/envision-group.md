---
title: "Envision Group"
created: 2026-11-08
updated: 2026-11-08
type: entity
tags:
  - company
  - infrastructure
  - data-center
  - china
  - ai-infrastructure
  - sustainability
  - ai-energy
sources:
  - raw/articles/2026-11-07_semianalysis-we-visited-chinas-stargate-inner-mongolia.md
related:
  - [[concepts/china-datacenter-buildout]]
  - [[concepts/source-grid-load-storage]]
  - [[entities/semianalysis]]
  - [[concepts/nvidia-45c-data-center-cooling]]
---

# Envision Group

Chinese renewable systems integrator and, increasingly, an AI datacenter developer. SemiAnalysis's September 2026 site visit (published Nov 7, 2026) describes Envision as "one of the most vertically integrated players we have ever seen" in AI infrastructure.

## Profile

- Core business: designs, integrates and manages power systems across the full chain — generation, storage, computing loads. **100GW+ of wind turbines installed worldwide**; builds its own turbines, converters, and control software; blade factories sit adjacent to its datacenter campuses.
- Affiliate **Envision AESC**: batteries, energy storage systems (BESS), power electronics and software — cells to PCS to software built in-house, factory pre-configured and tested as a whole system before shipping (vs the industry norm where on-site commissioning of mismatched HV/LV/generator parts takes 3–6 months).
- Path into datacenters: energy management — a route SemiAnalysis notes many industrial groups (energy, construction, electrical equipment) are taking into AI infrastructure in China.

## Datacenter activities

- **Galaxy campus, Ulanqab (Inner Mongolia)**: planned up to **800MW IT** ("China's Stargate" — comparable to Stargate Abilene's ~820MW core IT). First 120MW phase delivered within a year at ~1/5 US costs (live Aug 2026); full campus expected by end 2027; built-to-suit for two internet giants. Details: [[concepts/china-datacenter-buildout]].
- Total Inner Mongolia datacenter plans: **3GW**.
- Power strategy: [[concepts/source-grid-load-storage|SGLS]] — own wind farms (420MW combined, ~1.75× the 240MW DC load, sited ~80km apart) + 4-hour AESC battery + dedicated line, targeting >60% self-supplied power for the first two phases.
- Inside the campus: designed/integrated the low-voltage power modules and a **5MW SST-based 800V DC pilot** (10kV AC → 800V DC straight to rack) running at a live hyperscaler site; co-designed a factory-modular prefabricated substation (<3 months vs ~6 conventional).
- Cooling: liquid+air servers on one water loop, **no central chiller plant** — a northern-China-standard design that prefigures the US debate over NVIDIA's 45°C water claim ([[concepts/nvidia-45c-data-center-cooling]]).
- Chifeng precedent: 2GW off-grid wind/solar/storage feeding a green-ammonia plant plus a pilot datacenter on Tencent T-Block modular units, running entirely on power electronics (no synchronous generator).

## Positioning

In a market where DC rents halved to ~$40/kW/month and capex sits below $3mm/MW, Envision's vertical integration is a differentiation playbook familiar from China's EV market (BYD). Counter-model: CATL's equity/partnership web (VNET, Zhongheng Electric). SemiAnalysis judges it too early to tell whether integration wins hyperscaler orders, but power access and in-hall power-system redesign could make it decisive.

## Sources

- [We Visited China's Stargate in Inner Mongolia — SemiAnalysis](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) (Nov 7, 2026; paywalled — free portion only)
