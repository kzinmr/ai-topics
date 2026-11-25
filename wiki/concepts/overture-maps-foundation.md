---
title: "Overture Maps Foundation"
type: concept
created: 2026-04-25
updated: 2026-11-25
tags:
  - concept
  - open-data
  - geospatial
  - infrastructure
  - data-platform
  - ai-industry
aliases:
  - Overture Maps
  - Overture Maps Foundation
  - GERS
  - Global Entity Reference System
sources:
  - raw/articles/2026-05-10_hex-technologies_the-poles-of-brand-inaccessibility.md
  - https://overturemaps.org
  - https://overturemaps.org/blog/2024/towards-standardizing-place/
related:
  - "[[entities/drew-breunig]]"
---

# Overture Maps Foundation

**The Overture Maps Foundation** is a Linux Foundation-hosted industry consortium whose goal is to build and maintain a single, high-quality, **open** global map dataset — an open alternative to proprietary basemaps (Google Maps, HERE, TomTom, Mapbox's licensed data). Member companies contribute proprietary map data to a common open dataset rather than each re-mapping the world independently; the founding contributors include Meta (OpenStreetMap-derived places/imagery basemaps), Microsoft (building footprints, transportation), Amazon (roads), and TomTom.

## Data Model: Themes and Parquet-on-S3

Overture publishes data in **themes**, released versioned as partitioned **Parquet files on S3** (free to read, no API key, no rate limit) — a deliberately analytics-native distribution model rather than a tiles-and-tickets basemap service:

| Theme | Content |
|---|---|
| `places` | ~1.3 billion POI/place records with names, categories, brand, addresses, confidence |
| `buildings` | ML-derived building footprints with height/level attributes |
| `transportation` | road and path network, segmentation |
| `base` | land cover / water / land use |
| `elevations` | terrain |

Because the data is Parquet with hive partitioning, the canonical access pattern is DuckDB (or Spark/DuckDB-in-a-notebook) reading S3 directly:

```sql
install httpfs; load httpfs;
SET s3_region='us-west-2';
select names['common'][1][1]['value'][1] as name,
       json(brand) as brand,
       categories['main'] as category,
       geometry
from read_parquet('s3://overturemaps-us-west-2/release/<VERSION>/theme=places/type=*/*',
                  filename=true, hive_partitioning=1)
where addresses[1]['country'][1] = 'US';
```

This exact query shape — including the trial-and-error needed to reach it — came from Simon Willison's write-ups of exploring the release, and was reused directly by the Hex *Poles of Brand Inaccessibility* project (`raw/articles/2026-05-10_hex-technologies_the-poles-of-brand-inaccessibility.md`), which used Overture's `places` theme to map the most remote locations for hundreds of retail/restaurant chains — a descendant of Stephen Von Worley's *McFarthest Spot* series. That case is the clearest illustration of Overture's actual value: **global, category- and brand-tagged, queryable place data that a single analyst with DuckDB can join against commercial brand lists**, which previously required a licensed basemap contract.

## GERS — The Strategic Contribution

Overture's most consequential artifact is arguably not the map data but **GERS (Global Entity Reference System)**: a persistent, stable **128-bit (32-character) identifier for every entity** in the dataset. GERS is designed as join infrastructure, not map infrastructure:

- A stable ID that survives dataset re-releases (no re-derivation on each version).
- Two other datasets carrying a GERS column can be joined with a plain column join — no spatial joins, no fuzzy name matching, no coordinate-distance heuristics.
- Position: the geospatial analogue of what ISIN/LEI/GTIN are to finance, corporate registry, and retail — which is why it attracts standardization advocacy rather than just GIS interest.

[[entities/drew-breunig]] (GERS Evangelist at Overture, formerly VP Strategy at Precisely where he led the Overture collaboration) is the wiki's main source on the thesis:

> "Standardizing location with WGS 84 hasn't proven sufficient. Every organization can benefit from geospatial intelligence."

His practical demonstrations include mapping Overture GERS IDs to US Census FIPS codes with DuckDB, and the "Towards Standardizing Place" advocacy line (see [[entities/drew-breunig--projects|Drew Breunig — Projects]]).

## Why It Matters for AI / Agents

- **Grounding data for agents.** Free, structured, queryable world data (places → coordinates → categories → brands) removes the licensed-API dependency from agents and analytics tools that need location grounding.
- **No-schema-argument joins.** Persistent identifiers are what let an LLM/agent reliably connect "the entity mentioned in the prompt" to "the row in the enterprise dataset" — the entity-resolution half of retrieval.
- **Open-data economics.** A nonprofit-hosted, member-contributed commons undercuts the per-call basemap pricing model, and (like DuckDB's embedded-analytics story, cf. [[events/2026-08-26-aws-acquires-ducklabs]]) concentrates value in tooling and joins rather than in data ownership.

## Related Concepts

- [[entities/drew-breunig]] — GERS Evangelist; geospatial standardization and context-engineering writer
- [[entities/drew-breunig--projects]] — GERS demos and `drskill` tooling
- [[entities/hex-technologies]] — notebook analytics tool used in the Poles of Brand Inaccessibility case
- [[entities/simon-willison]] — early DuckDB-on-Overture-S3 exploration write-ups
- [[concepts/open-source-sustainability]] — the commons/funding-model question for open data
- [[concepts/spec-driven-development]] — Breunig's other main line of work

## Sources

- [overturemaps.org](https://overturemaps.org) — official site (Linux Foundation project)
- [Overture Maps Foundation releases (S3 / Parquet)](https://docs.overturemaps.org/) — docs
- Hex Technologies, [The Poles of Brand Inaccessibility](https://hex.tech/blog/the-poles-of-brand-inaccessibility/) — raw: `raw/articles/2026-05-10_hex-technologies_the-poles-of-brand-inaccessibility.md`
- Drew Breunig, *Towards Standardizing Place* — GERS advocacy
