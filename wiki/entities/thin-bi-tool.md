---
title: thin-bi-tool
description: "薄くなるBIツール — The trend of BI tools transitioning from comprehensive analysis platforms to lightweight, visualization-focused tools that rely on cloud DWH and semantic layers"
url: https://note.com/ikki_mz/n/n3382a648c6c5
type: entity
created: 2026-04-25
updated: 2026-04-30
tags:
  - entity
  - developer-tooling
  - infrastructure
aliases:
  - 薄くなるBIツール
  - Thin BI Tool
  - Light BI
sources:
  - https://note.com/ikki_mz/n/n3382a648c6c5
  - https://stable.co.jp/blog/introduction-lightdash
  - https://stable.co.jp/blog/introduction-steep
---
# Thin BI Tool

**Thin BI Tools** refer to the trend of BI tools transitioning from traditional "comprehensive analysis platform" models toward lightweight, visualization-focused tools native to cloud data warehouses. The concept originated from a March 2026 note article by ikki, CEO of stable Co., Ltd.

## Author

**ikki** — CEO of stable Co., Ltd. Provides enterprise data engineering support (hands-on support for data utilization and infrastructure development).

## Traditional BI Tools: Comprehensive Analysis Platforms

When Tableau emerged around 2004, cloud DWH (BigQuery was released in 2010) was not yet widespread, and BI tools were expected to serve as "comprehensive analysis platforms."

### Three Roles
1. **Data Ingestion** — Import scattered data from Excel, CSV, on-prem DB, etc. into the BI tool
2. **Data Processing** — JOIN, custom SQL, dimension/measure definitions, etc.
3. **Data Visualization** — Dashboard and report creation

## Recent Trend: Visualization-Focused BI Tools

New-generation BI tools (Lightdash, Steep, etc.) are, in contrast to traditional tools, **simpler with fewer features**:

### Key Changes
1. **Elimination of data ingestion** — Instead of importing into the BI tool, query the DWH directly for data
2. **Minimization of data processing** — Retrieve pre-defined data directly from dbt's semantic layer
3. **Focus on visualization** — The BI tool functions purely as a visualization layer

### Drivers of This Change
1. **Adoption of cloud DWH** — BigQuery, Snowflake, Redshift, etc. handle data aggregation, processing, and management
2. **Spread of dbt** — dbt models manage the semantic layer (dimension/metric definitions) as code

### Benefits of dbt Semantic Layer Integration
- Centralized code-based management of metric definitions
- Minimal processing on the BI tool side (just select pre-defined data)
- Functions as a common language between engineering and analyst teams

## Representative Thin BI Tools

### Lightdash
- Uses dbt model definitions directly as the semantic layer
- Defines dimensions and metrics in yaml files
- Open source, self-hostable

### Steep
- Modern BI tool with beautiful design
- Supports integration with dbt Semantic Layer
- Characterized by simple operability

## The Future of DWH-Native Visualization

If DWHs themselves (the ability to directly visualize BigQuery query results) continue to evolve, the standalone value of BI tools may further diminish. Benefits such as cost reduction and centralized permission management are expected.

## Related Concepts
- [[concepts/business-intelligence]] — Basic BI concepts
- [[concepts/dbt]] — Data transformation and semantic layer management
- [[concepts/cloud-data-warehouse]] — Cloud DWH architecture
- [[concepts/semantic-layer]] — Semantic layer design

## Related Entities
- [[entities/lightdash]] — Lightdash BI tool
- [[entities/dbt-labs]] — Company developing dbt
- [[entities/tableau]] — Representative traditional comprehensive BI tool

## References
- [Thin BI Tools — note (ikki / stable Co., Ltd.)](https://note.com/ikki_mz/n/n3382a648c6c5)
- [Lightdash Introduction — stable Co., Ltd.](https://stable.co.jp/blog/introduction-lightdash)
- [Steep Introduction — stable Co., Ltd.](https://stable.co.jp/blog/introduction-steep)