---
title: "Thin BI (薄くなるBIツール)"
type: concept
created: 2026-04-27
updated: 2026-04-27
tags: [bi-tools, data-engineering, cloud-dwh, data-visualization]
aliases: ["thin-bi", "light-bi", "modern-bi"]
sources:
  - "https://stable.co.jp/blog/introduction-lightdash"
  - "https://stable.co.jp/blog/introduction-steep"
---

# Thin BI (薄くなるBIツール)

> **Core Thesis:** Modern BI tools are "becoming thin" as cloud data warehouses take over data ingestion and transformation roles.

## Overview

The evolution of BI tools from "comprehensive analysis platforms" to "thin interfaces" reflects a fundamental shift in data architecture.

### Era 1: Comprehensive Platform (Pre-2010)

In the Tableau era (2004+), before cloud data warehouses were prevalent:

- **Data Ingestion**: BI tools directly connected to Excel, CSV, on-prem databases
- **Data Transformation**: Built-in ETL, data cleaning, normalization
- **Visualization**: Charts, dashboards, ad-hoc analysis

The BI tool was the **single platform** for all data operations.

### Era 2: Thin Interface (2010+)

With the rise of cloud DWHs (BigQuery 2010, Snowflake, Redshift):

- **Data Ingestion** → Moved to the DWH
- **Data Transformation** → dbt, SQL in the DWH
- **Visualization** → BI tool becomes a thin interface

Modern BI tools focus on **visualization and analysis**, not data plumbing.

## Modern Thin BI Tools

| Tool | DWH Integration | Key Feature |
|---|---|---|
| **Lightdash** | dbt | SQL-as-code analytics, CI/CD for metrics |
| **Steep** | Snowflake | Streamlit-based embedded analytics |
| **Looker Studio** | Google Cloud | Data credentials, embedded dashboards |
| **Metabase** | Multi-DWH | Open-source, self-hosted |
| **Mode** | Multi-DWH | SQL + visualization + notebooks |

## Impact on Data Engineering

This shift means:

1. **Data engineers** focus on DWH pipeline quality, not BI tool configuration
2. **Analysts** focus on metrics and insights, not data wrangling
3. **BI tools** become composable, embeddable widgets rather than monolithic platforms

## Related Articles

- [「薄くなる」BIツール](../raw/articles/2033336956961308721_薄くなるbiツール.md) — @ikki_stable, stable株式会社 (2026-03-16, 128 bookmarks)

## See Also

- [[concepts/data-engineering]]
- [[concepts/cloud-data-warehouses]]
