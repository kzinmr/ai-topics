---
title: "What Is Data Federation? How It Works, When It Breaks"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-federation/"
scraped: "2026-07-21T06:00:40.866151+00:00"
lastmod: "2026-05-22"
type: "sitemap"
---

# What Is Data Federation? How It Works, When It Breaks

**Source**: [https://hex.tech/blog/data-federation/](https://hex.tech/blog/data-federation/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
Blog
What is data federation? Here's how it works and when it breaks
Your customer data lives in PostgreSQL, product analytics in BigQuery, and sales pipeline in Snowflake, and the question that just landed touches all three. Data federation is the pattern that lets you query across them without building a pipeline first, but the trade-offs are real.
The Hex Team
Data
May 22, 2026
Share:
twitter
linkedin
In this article
How data federation works
How federation compares to ETL, ELT, and replication
Where federation makes practical sense
What tends to break
What federation doesn't solve on its own
Start with access, layer in governance
Frequently Asked Questions
Get started for free
You have customer data in PostgreSQL, product analytics in BigQuery, and a sales pipeline in Snowflake. A stakeholder asks a question that touches all three. The "right" answer involves building a pipeline to centralize everything first. The honest answer is that nobody has time for that right now, and the question needs an answer by Thursday.
Data federation lets you query across multiple databases, warehouses, or lakes through a single interface without copying data into one place first. The data stays where it is. You write one query, and the federation engine figures out which sources to hit, how to combine the results, and what to send back.
That sounds simple. The mechanics matter, though, and understanding them is what separates a useful federation setup from a slow, unreliable one.
How data federation works
Data federation places a middleware layer between you and the underlying sources. You write SQL against a single logical schema. The federation engine decomposes that query into sub-queries, dispatches them to the relevant sources, collects the results, and assembles a unified response.
The data never moves into a centralized store. It stays where it lives, and the engine visits it at query time (sometimes called in situ querying).
The schema hierarchy
The federation engine maintains a layered schema model to translate between your query and the physical reality of each source. Local schemas describe each source's native structure: a PostgreSQL table definition, Parquet files in S3, or a DynamoDB key structure. Component schemas translate each local schema into a common data model. The unified schema is what you actually query against.
That's a lot of translation layers. But it's what lets you write one query instead of three.
Schema mapping resolves the mismatches between sources. cust_id in one database and customer_identifier in another both map to customer_id in the unified schema. TIMESTAMP in PostgreSQL and a Unix epoch integer in DynamoDB both map to a canonical datetime type.
Source-specific connectors
Each source needs an adapter that translates the federation engine's query language into whatever that source speaks natively. Trino supports sources like PostgreSQL, MongoDB, Kafka, and S3-backed Parquet data via connectors such as Hive. Athena uses Lambda for DynamoDB, RDS, and JDBC-compliant sources. BigQuery federated queries use EXTERNAL_QUERY with AlloyDB, Spanner, or Cloud SQL. Databricks Lakehouse Federation uses Unity Catalog as the metadata layer with JDBC to push queries to external systems.
The query execution lifecycle
The execution path explains where many federated performance problems begin. The engine parses your SQL into logical operations, checks its metadata catalog to find the relevant registered sources, and splits the work into sub-queries for each one. The optimizer then decides what to push down to source systems versus what to handle at the federation layer, and how much of the work can run in parallel.
The engine translates each sub-query into the source's native dialect through its connector and sends it off. Sources execute independently and in parallel where the plan allows. The federation layer then collects the result sets, applies any remaining operations that couldn't be pushed down (cross-source joins, final sorts, aggregations over combined results), and returns a unified result.
Pushdown optimization
The single biggest factor in federated query performance is how much computation the optimizer can push down to the source systems rather than pulling raw data back to the federation layer for processing.
Pushdown can apply to filters in WHERE clauses, selected columns, aggregations such as SUM and COUNT, joins, limits, and top-N queries. AWS documents a concrete example: with predicate pushdown on a MySQL table of 5,157 rows, only one matching record is scanned instead of transferring all 5,157 rows to Athena for filtering.
But there's a hard constraint. In Trino, join pushdown only works within the same catalog. Cross-catalog joins, the defining use case of multi-source federation, are often constrained and may only be pushed down under specific conditions or within a single source, depending on the engine. That limit is worth understanding early.
How federation compares to ETL, ELT, and replication
Federation overlaps with other data integration patterns, but the trade-offs are distinct.
ETL pulls data from sources, transforms it on a secondary server, and loads it into the destination warehouse. ELT loads raw data directly into the warehouse, then transforms it there using the warehouse's native compute. Replication continuously copies source data to a target with minimal transformation, optimized for near-real-time synchronization, disaster recovery, and offloading query load from production systems.
Federation queries data where it lives. No copies, no staging, no sync jobs to monitor.
The core trade-off is freshness versus performance. Federation gives you the freshest data (current at query time) but not necessarily the fastest response. Performance depends on source system responsiveness, network latency, and pushdown quality. ETL and ELT optimize for query performance by pre-computing transformations, at the cost of data that's only as fresh as the last pipeline run.
In practice, the most mature architectures don't choose one pattern exclusively. ELT handles historical and batch analytical workloads where query performance on materialized data matters. Federation handles real-time queries against live sources and exploratory work where building a
data pipeline
would be premature. They complement each other.
Where federation makes practical sense
Cross-database analytics
Operational data lives in multiple systems, and analysts need to join across them. AWS Athena Federated Query supports single SQL queries across relational, non-relational, object, and custom data sources. BigQuery's federated queries can run an aggregation against AlloyDB and join the result with BigQuery tables with no data movement.
Regulated environments where data can't move
Privacy regulations sometimes prohibit copying data across borders or into centralized systems. Researchers studying federated analysis describe the core tension well: federation "balances the needs of data stewards to restrict access to regulated data with the needs of the scientific and clinical community to gain new insights from data that cannot be transferred for legal, ethical, or technical reasons." The World Economic Forum documented a four-country federation for rare disease diagnosis where data never leaves the holding organization. Only computed answers return to the federation system.
Multi-cloud setups
According to IDC's Cloud Pulse 2024 survey, 79% of organizations use multiple cloud providers, rising to 90% among cloud-mature organizations. Cross-cloud analytics becomes relevant when data is split across AWS, Azure, and GCP through acquisitions or workload placement. BigQuery Omni lets you query data stored in Amazon S3 or Azure Blob Storage without moving it. AWS documents using Athena for Synapse for direct cross-cloud querying.
Exploratory work before a pipeline exists
A data scientist needs to join a new data source with the existing warehouse data. The ETL pipeline to bring that source into the warehouse hasn't been built yet, and the question can't wait for one.
Federation lets you query the source system directly at runtime. Databricks has published materials discussing Bayer's use of Lakehouse Federation and Delta Lake for this pattern. More broadly, when analysts need to explore data across multiple data connections before anyone's built a pipeline, tools like Hex let them write SQL against connected sources and chain Python transformations on the results in a single
notebook environment
, keeping the exploratory work in one place instead of scattered across tabs and terminals.
What tends to break
Latency compounds across sources
A federated query can't complete until every source responds. One slow source gates the entire result. There's a deeper structural issue here: there is no pipelining of data among query operators across sites. Operators at the consuming site hold allocated resources (particularly memory) while waiting for data from the producing site or for a slow communication link. This resource-holding behavior doesn't exist in centralized systems where pipelining between operators is standard. When a query needs sequential lookups, where a result from one source determines what to fetch from a second, each operation adds a full round-trip, and parallelism disappears entirely.
Cross-source joins hit a wall
When joins can't be pushed down, raw data from both sides must transfer to the federation engine over JDBC for processing. Joins across systems are often fragile and slow. For most use cases, if data needs to be queried regularly, joined with other sources, or analyzed deeply, loading it into a centralized platform usually performs better.
Schema drift causes silent failures
Databricks documentation and user reports indicate that complex types such as STRUCT and MAP may not be exposed cleanly in some contexts and can instead appear as string types. The query didn't error. It succeeded and returned data, but the data was wrong. Nested structures came back as opaque strings. This happened within a single vendor's setup, not a cross-vendor scenario. Without enforced consistency between systems, these failures surface at query time, potentially after incorrect results have already been consumed.
Security doesn't coordinate itself
A federated architecture has at least two enforcement boundaries: the federation layer's access policies and each source system's native policies. These don't automatically coordinate. Research in healthcare settings found that standard RBAC faces limitations in cross-organizational settings, and that adaptations are needed for interdomain federation scenarios. When federated sources are autonomous systems each with their own admin, there is no single authority to enforce a unified role hierarchy.
What federation doesn't solve on its own
Federation solves a data access and integration problem: it lets you query across multiple autonomous data sources without moving them into one place. Getting consistent, trustworthy answers across those connected sources is a governance problem, and federation surfaces it rather than fixes it.
Metric definitions don't unify themselves
"Customer lifetime value" in your CRM and "CLV" in your ERP might use different calculation logic. A federated query that joins across them will run fine and return a number. The number just won't mean what you think it means. The query engine can't detect this. When different teams calculate the same metric using different logic, stakeholders lose confidence in data-driven insights.
This is where governed context becomes important. Teams can start with the lightest interventions: endorsing specific tables as trusted sources, adding warehouse descriptions, and setting workspace rules for how key terms should be interpreted. As governance matures,
semantic authoring
in Hex lets teams formalize metric definitions through the Modeling Agent, and those definitions carry across notebooks, apps, and self-serve experiences. Combined with observability through
Context Studio
, which surfaces where definitions are missing or inconsistent, teams can close the gap between "technically correct query" and "trustworthy answer" progressively rather than all at once.
Data quality is inherited, not enforced
Federation has no native mechanism to validate, normalize, or quarantine low-quality data before it enters a query result. Quality issues in source systems flow through federated queries and affect the results.
Lineage and auditability need deliberate investment
Lineage across federated systems is structurally harder than in centralized architectures because data provenance spans multiple independent systems, each with its own logging, versioning, and access model. A dataset that doesn't publish lineage information back to the platform can be flagged as unfit for consumption. But that's a platform governance capability, not something federation provides by default.
Federation, semantic modeling, and governance work at different levels
Federation routes queries. Semantic modeling defines what data means. A governance framework establishes who owns it, what quality it must meet, and how its movement gets recorded. You need all three for trustworthy answers across distributed sources.
Teams that get the most out of federation pair it with governed metric definitions and quality controls rather than treating the federation layer as the full solution. The access pattern is solved; the meaning problem isn't.
Start with access, layer in governance
Federation exists on a spectrum rather than as a binary choice. The most mature architectures use it alongside ETL/ELT, not instead of it. The practical question for any dataset is how frequently it will be queried, how much volume is involved, and how mature its governance is. Data that's queried daily and joined with other sources belongs in a centralized warehouse. Data that's queried occasionally, can't be moved, or needs validation before a pipeline investment is justified is a good fit for federation.
The teams who get the most from federation treat it as a starting point for exploration and as a permanent solution only where data movement is genuinely impractical. They pair it with semantic modeling for metric consistency and governance frameworks for quality and access control.
Request a demo
to see how Hex brings governed context to your analytical workflows, whether your data lives in one warehouse or across many.
Frequently Asked Questions
How do I know when a dataset should move from federated queries into a proper pipeline?
The clearest signal is query frequency. If an analyst queries the same federated source more than a few times a week, or if cross-source joins involving that data become part of a recurring report or dashboard, the latency and reliability trade-offs of federation start to outweigh the convenience. At that point, building an ELT pipeline to materialize the data in your warehouse gives you predictable performance and more control over transformations. Federation works best as a proving ground: use it to validate whether a source is worth the pipeline investment, then promote the data when the answer is yes.
Can I use federation and semantic modeling together, or do they conflict?
They complement each other. Federation handles the connectivity layer: routing queries to the right sources and combining results. Semantic modeling handles the meaning layer: defining what "active user" or "monthly recurring revenue" actually means so those definitions stay consistent regardless of which source the data comes from. Without semantic modeling, federation gives you technically correct results that may be semantically inconsistent across sources. Without federation, semantic modeling only covers the data you've already centralized. Pairing them gives you both broad access and consistent definitions, which is what most cross-source analytics actually need.
Does federation add risk to our data security posture?
It adds complexity that needs to be managed deliberately. Federation creates multiple enforcement boundaries: the federation layer's access controls and each source system's native policies. These don't coordinate automatically, so permissions granted at one layer don't necessarily carry through to another. The practical step is to audit access controls at both the federation engine and each registered source, and to test that restricted data remains restricted when accessed through the federated path.
Share:
twitter
linkedin
Get "The Data Leader’s Guide to Agentic Analytics"  — a practical roadmap for understanding and implementing AI to accelerate your data team.
Download
Request a demo
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
