---
title: "Cloud Data Warehouses"
type: concept
tags: [data-warehouse, snowflake, bigquery, databricks, cloud-analytics]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Cloud DW, Cloud Data Warehouse, Modern Data Warehouse, CDW]
related: [[concepts/data-engineering]], [[concepts/event-driven-architecture]], [[concepts/ai-observability]]
sources: [https://www.snowflake.com/en/, https://cloud.google.com/bigquery, https://www.databricks.com/product/data-warehouse]
---

# Cloud Data Warehouses

## Summary

Cloud data warehouses are fully managed, scalable analytics databases built for cloud infrastructure, enabling organizations to store and query massive datasets using standard SQL without managing hardware. The major platforms — Snowflake, Google BigQuery, Amazon Redshift, and Databricks — have evolved from pure analytics engines into unified data platforms incorporating AI features, real-time streaming, and multi-format support. The 2025-2026 era is defined by the convergence of data warehousing with AI/ML workloads, native support for Iceberg/Delta Lake open formats, and data warehouse-native AI analytics.

## Key Ideas

- **Separation of Compute and Storage**: The defining architecture of modern cloud data warehouses — compute clusters can be scaled independently from storage, enabling elastic scaling and cost optimization
- **The Open Table Format War**: Apache Iceberg has emerged as the dominant open table format (2025-2026), adopted by Snowflake, AWS, and Google. Databricks continues to push Delta Lake. The unification around Iceberg via the Iceberg REST Catalog API is the major trend
- **AI-Native Data Warehouses**: Snowflake's Cortex AI, BigQuery ML, and Databricks' MLflow integration enable running LLMs, embedding generation, and ML inference directly within SQL queries — no data movement required
- **Real-Time Analytics**: Streaming ingestion via Kafka, Kinesis, and change data capture (CDC) enables sub-second data freshness for real-time dashboards and operational analytics
- **Multi-Cloud & Cross-Cloud**: Snowflake's cross-cloud replication and Google's BigQuery Omni enable querying data across AWS, Azure, and GCP from a single interface
- **Data Warehouse + Lakehouse Convergence**: The distinction between data warehouses (structured, SQL) and data lakes (unstructured, files) is blurring as warehouses support semi-structured data and lakes support ACID transactions via table formats

## Terminology

- **Separation of Compute/Storage**: Architecture where storage (S3/GCS/ADLS) is separate from compute clusters, enabling independent scaling
- **Apache Iceberg**: Open table format providing ACID transactions, time travel, and schema evolution on data lakes
- **Snowflake Cortex AI**: Snowflake's built-in AI/ML capabilities including vector search, LLM inference, and classification functions
- **BigQuery ML**: Google's SQL-based ML platform for training and running models directly in BigQuery
- **Lakehouse Architecture**: Hybrid data platform combining data lake flexibility with warehouse ACID transactions and performance
- **Zero-Copy Cloning**: Instantly creating writable copies of databases without duplicating underlying data storage

## Examples/Applications

- **Business Intelligence**: Interactive dashboards and reports on terabytes of sales, marketing, and operations data with sub-second query times
- **AI Feature Engineering**: Generating and storing embedding vectors for recommendation systems, search, and RAG directly in the warehouse
- **Real-Time Fraud Detection**: Streaming transaction data into the warehouse, with ML models scoring each transaction against historical patterns
- **Customer 360**: Unifying customer data from CRM, support, billing, and web analytics into a single queryable view
- **Data Sharing**: Snowflake's Data Sharing and Google's Analytics Hub enable secure cross-organization data sharing without data copying

## Related Concepts

- [[data-engineering]]
- [[event-driven-architecture]]
- [[ai-observability]]
- [[cloud-data-warehouses]]

## Sources

- [Snowflake: The AI Data Cloud](https://www.snowflake.com/en/)
- [Google BigQuery: Enterprise Data Warehouse](https://cloud.google.com/bigquery)
- [Databricks Data Intelligence Platform](https://www.databricks.com/product/data-warehouse)
