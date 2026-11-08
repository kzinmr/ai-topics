---
title: "Source-Grid-Load-Storage (SGLS)"
created: 2026-11-08
updated: 2026-11-08
type: concept
tags:
  - infrastructure
  - data-center
  - china
  - ai-energy
  - sustainability
  - architecture
sources:
  - raw/articles/2026-11-07_semianalysis-we-visited-chinas-stargate-inner-mongolia.md
related:
  - [[concepts/china-datacenter-buildout]]
  - [[entities/envision-group]]
  - [[concepts/ai-energy]]
  - [[concepts/data-center-local-backlash]]
---

# Source-Grid-Load-Storage (SGLS)

A Chinese project model (source-grid-load-storage) in which a single project builds its **own wind and/or solar farm ("source"), a dedicated line ("grid"), its computing load ("load"), and battery storage ("storage")**, linking them through a private line instead of the public grid. For hyperscalers the appeal is long-term power at a largely fixed cost; wind/solar generation also counts toward green targets. Approvals in China increasingly favor SGLS-style projects under the national "Compute Power Coordination" push.

## How the wind share is engineered (Galaxy case)

SemiAnalysis's September 2026 visit to [[entities/envision-group|Envision]]'s Galaxy campus ([[concepts/china-datacenter-buildout]]) shows three levers that let an SGLS project self-supply **>60%** of the first two phases' power:

1. **Siting** — windy sites chosen even ~2 hours' drive away; two wind farms ~80km apart, decorrelating calm hours.
2. **Scale** — 420MW of wind vs a 240MW datacenter load (~1.75× oversizing), so even light-wind hours cover much of the load. (1:1 wind-to-load on a good Ulanqab site covers only ~40% of annual power.)
3. **Storage** — a 4-hour battery shifts surplus from windy to calm hours (cannot cover multi-day lulls). Better wind/load matching pushes the share higher.

Regional basis: Inner Mongolia holds ~57% of China's usable wind resources; capacity factors ~32% regionally, 35–40% at Ulanqab; all-in power ~$0.055/kWh.

## Precedents and variants

- **Chifeng (Envision)**: 2GW off-grid wind+solar+storage feeding a green-ammonia plant and a pilot datacenter on Tencent T-Block modular units — runs entirely on power electronics, no synchronous generator.
- Convergence with the West: US developers bridge power gaps with on-site gas turbines/fuel cells/batteries; Southeast Asian governments now push bring-your-own-power; Malaysia requires ≥30% renewables. "Access to energy is becoming part of what a datacenter developer sells."

## Why it matters for AI infrastructure

SGLS converts the grid-connection queue — the binding constraint on US AI buildout (see [[concepts/ai-energy]]) — into a private generation problem, and pairs compute with green power for permitting. Combined with local political resistance to grid-connected campuses in the US ([[concepts/data-center-local-backlash]]), it positions Chinese interior regions to scale GW campuses without the "local consent" bottleneck.

## Sources

- [We Visited China's Stargate in Inner Mongolia — SemiAnalysis](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) (Nov 7, 2026; paywalled — free portion only)
