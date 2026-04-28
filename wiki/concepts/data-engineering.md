---
title: "Data Engineering"
type: concept
tags: [data-engineering, data-pipeline, etl, data-infrastructure]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Data Engineering, Data Pipeline, ETL, ELT, Modern Data Stack]
related: [[concepts/cloud-data-warehouses]], [[concepts/event-driven-architecture]], [[concepts/ai-observability]], [[concepts/durable-execution]]
sources: [https://www.dagster.io/, https://airbyte.com/, https://www.dbtlabs.com/]
---

# Data Engineering

## Summary

Data engineering is the practice of designing, building, and maintaining the infrastructure that collects, stores, processes, and makes data available for analysis and machine learning. It encompasses data pipelines (ETL/ELT), data warehousing, data quality monitoring, and the orchestration of complex data workflows. The 2025-2026 era's Modern Data Stack has converged around a core toolchain — dbt (transformation), Airbyte/Fivetran (ingestion), Snowflake/BigQuery (storage), Dagster/Airflow (orchestration) — with the major evolution being AI-native data engineering where LLMs assist with pipeline generation, data quality checks, and schema mapping.

## Key Ideas

- **The Modern Data Stack**: The canonical toolchain has stabilized around: ingestion (Airbyte, Fivetran, Confluent) → storage/query (Snowflake, BigQuery, Databricks) → transformation (dbt) → orchestration (Dagster, Airflow) → BI (Looker, Tableau, Power BI)
- **ELT over ETL**: The shift from Extract-Transform-Load (transform before loading) to Extract-Load-Transform (load raw data first, transform in the warehouse) — enabled by cheap cloud storage and powerful warehouses
- **dbt as Standard**: dbt (data build tool) has become the de facto standard for data transformation, treating SQL transformations as version-controlled, testable, and documented code — "analytics engineering"
- **Data Quality as Code**: dbt tests, Great Expectations, and Soda enable automated data quality monitoring — data pipelines that fail on quality violations rather than silently producing bad data
- **AI-Enhanced Data Engineering (2025-2026)**: LLMs assist with writing dbt models, generating SQL transforms, mapping source schemas to target schemas, and auto-generating data quality tests
- **Real-Time Data**: The move from batch-only to hybrid batch/streaming architectures — Kafka, Flink, and Delta Live Tables enable real-time data products alongside traditional nightly batches
- **Data Contracts**: Formal agreements between data producers and consumers defining schemas, freshness SLAs, and quality guarantees — enforced through schema registries and pipeline validation

## Terminology

- **dbt**: The standard SQL transformation tool — models are written in SQL (or Python), version-controlled, tested, and documented
- **ELT (Extract-Load-Transform)**: Loading raw data first, then transforming it in the data warehouse — the dominant modern pattern
- **Data Pipeline**: A series of processing steps that move data from source systems to target systems (warehouse, lake, API)
- **Orchestrator**: System managing pipeline execution, dependencies, retries, and scheduling (Dagster, Airflow, Prefect)
- **Data Contract**: Formal specification of data schema, format, quality rules, and SLAs agreed between producers and consumers
- **Semantic Layer**: A business-friendly view of data that abstracts warehouse complexity (dbt Metrics, Looker LookML)

## Examples/Applications

- **E-Commerce Analytics Pipeline**: Raw clickstream data → ingestion (Kafka) → landing in S3 → dbt transformations into user sessions, conversion funnels, and revenue attribution
- **Machine Learning Pipeline**: Feature engineering pipeline that transforms raw event data into training features, with dbt for SQL transforms + Python for ML features
- **Financial Reporting**: Strict SLAs on data freshness and accuracy — dbt tests enforce data quality; Dagster orchestrates with alerting on failures
- **Customer Data Platform**: Unifying data from CRM, support, billing, and product analytics into a single customer 360 view

## Related Concepts

- [[cloud-data-warehouses]]
- [[event-driven-architecture]]
- [[ai-observability]]
- [[durable-execution]]
- [[ragas]]

## Sources

- [dbt Labs: Transform Data in Your Warehouse](https://www.dbtlabs.com/)
- [Dagster: Orchestration Platform for Data Engineering](https://dagster.io/)
- [Airbyte: Open-Source Data Integration](https://airbyte.com/)
