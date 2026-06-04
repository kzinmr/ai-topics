---
title: "ETL Pipelines: Architecture, Examples, and Where They Break"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/etl-pipeline/"
scraped: "2026-06-04T06:00:28.880422+00:00"
lastmod: "2026-05-21"
type: "sitemap"
---

# ETL Pipelines: Architecture, Examples, and Where They Break

**Source**: [https://hex.tech/blog/etl-pipeline/](https://hex.tech/blog/etl-pipeline/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
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
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
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
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
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
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
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
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
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
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
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
What is an ETL pipeline? Architecture, examples, and where they break
The pipeline works. The data lands on schedule. And the question that's been in the backlog for three weeks still doesn't have an answer.
The Hex Team
Data
May 21, 2026
Share:
twitter
linkedin
In this article
What is an ETL pipeline?
ETL vs. ELT vs. data pipeline
5 ETL pipeline examples
Processing modes: batch, streaming, and CDC
Common ETL tools and where they fit
Where ETL pipelines break
How AI is changing ETL pipelines
Getting value from the pipeline
Frequently Asked Questions
Get started for free
You know where the data is. Customer records in Salesforce, payment events in Stripe, product telemetry streaming from your app, marketing spend scattered across platforms. The data is easy enough to find. The hard part is that nobody can query it in one place, and the question that's been sitting in the backlog for three weeks still doesn't have an answer.
ETL pipelines solve that by pulling data from sources, reshaping it into something usable, and delivering it to a destination where your team can work with it. But the real payoff shows up downstream, when someone can finally
run the analysis
, make a decision, and clear that backlog item.
What is an ETL pipeline?
An ETL pipeline is an automated system that extracts data from source systems, transforms it into a consistent format, and loads it into a destination (typically a
data warehouse
) where teams can query and analyze it. The three stages work together to turn scattered, inconsistent data into something you can trust enough to act on.
Extract
Connectors pull data from your source systems: APIs, databases, flat files, SaaS platforms. They handle authentication, pagination, and rate limits, then pull updates on a schedule or in response to events.
Transform
This is where you clean, deduplicate, and reshape raw data to match your analytical needs. It's also where business logic lives — defining what counts as an "active customer" or how you calculate "revenue."
Load
Transformed data lands in its destination: a cloud warehouse like Snowflake or BigQuery, a data lake, or a specialized store. The goal is making the data available where your team already works.
ETL vs. ELT vs. data pipeline
ETL vs. ELT comes down to where transformations happen. ETL transforms data before loading it into the warehouse. ELT loads raw data first and transforms it inside the warehouse using the warehouse's own compute. A "data pipeline" is the broader category that can include either pattern, plus streaming, conditional routing, and more complex orchestration.
When the distinction matters
ETL
works well when you need to enforce strict data quality before data enters your warehouse. This comes up in regulated industries like healthcare and finance, where compliance mandates govern what data gets stored and how.
ELT
has become the default for most modern data teams. Cloud warehouses have enough compute to handle transformations directly, and you keep the raw data. So when someone asks a question your transformations didn't anticipate, you can reshape the data without re-extracting.
When it matters less
For most teams, the ETL vs. ELT choice rarely determines whether data work moves fast. The bigger bottleneck is usually downstream: someone outside the data team needs an answer, and they can't get it without filing a ticket. How you manage transformations matters less than whether people can actually use the output.
5 ETL pipeline examples
1. E-commerce data consolidation
The situation
An online retailer has order data in Shopify, payment records in Stripe, customer profiles in Salesforce, and marketing spend across Google Ads and Meta. Each system uses different customer IDs, timestamp formats, and definitions of basic concepts like "order."
How the pipeline works
Extract:
Connectors pull from Shopify's API, Stripe webhooks, Salesforce exports, and ad platform APIs on an hourly or daily schedule.
Transform:
The system deduplicates contacts by email, matches payments to customer IDs, attributes marketing spend to acquisition channels, and normalizes all timestamps to UTC.
Load:
Everything lands in a cloud warehouse built for analytical queries.
Once the data is in one place, teams can ask cross-system questions without manual stitching.
What you learn
The merchandising team can now see which acquisition channels produce the highest lifetime-value customers, not just the most customers. A product manager notices that customers acquired through Instagram have 3x higher return rates than those from email. That signal stayed hidden when data lived in separate systems.
2. Financial reporting and compliance
The situation
A finance team at a publicly traded company spends days manually downloading data from their ERP, budgeting tools, and operational databases to produce budget variance analysis. Previous automation attempts failed for years.
How the pipeline works
Extract:
Automated connectors pull data from the core ERP, budgeting platform, and operational databases.
Transform:
The pipeline standardizes financial dimensions and hierarchies, then consolidates budget vs. actual data across departments. Validation rules enforce accuracy, and audit trails track every transformation for SOX compliance.
Load:
A centralized data warehouse serves as the single source for all financial reporting.
When your transformations are standardized and every step leaves an audit trail, the reporting process stops being a fire drill.
What you learn
The bigger story here is what happens to the audit. Before automation, auditors spent weeks tracing numbers across spreadsheets and exports. With transformations tracked in code, every figure has a lineage from warehouse back to source system. Many digital banks implement similar patterns using dbt, where analytics teams own the transformation logic directly rather than waiting on engineering. The compliance benefit is almost a side effect of well-structured data engineering.
3. ML feature engineering
The situation
A fraud detection team needs to score transactions in real time. The features powering their model — like "average transaction amount over the last 24 hours" — need data from multiple sources with different latency requirements.
How the pipeline works
In practice, teams often split this into pipelines with different cadences:
Feature pipelines
ingest transaction data and compute aggregations over time windows, then store the results for model training and serving.
Training pipelines
pull historical features with strict time boundaries so the model only learns from data that was actually available at prediction time. Without that discipline, the model trains on future information it won't have in production.
Serving pipelines
pull the latest computed features from a low-latency store to score live transactions, typically in under 10 milliseconds.
That way, you can retrain the model on its own schedule without touching the real-time scoring path.
What you learn
Each pipeline runs at its own cadence. You don't retrain the model every time features update. This pattern, used at scale in systems like Uber's
Michelangelo platform
, means data scientists spend time on model quality instead of plumbing. If your team doesn't need real-time scoring, the same principle still applies at a smaller scale: separating feature computation from model training keeps both pipelines simpler and easier to debug.
4. Cross-team self-serve analytics
The situation
The data team is buried. Product managers need retention cohorts, marketing wants campaign attribution, and finance needs revenue breakdowns. The backlog is three months deep.
How the pipeline works
Extract:
Connectors pull from the product database, marketing platforms, payment processor, and CRM.
Transform:
dbt models build a semantic layer that defines key metrics like "active user," "revenue," and "churn" with consistent definitions and automated data quality tests.
Load:
The pipeline loads transformed, tested data into the warehouse and exposes it through the semantic layer.
With that foundation, questions shift from "can you pull this for me" to "what do we want to learn next?"
What you learn
The pipeline and the semantic layer are necessary but not sufficient. In Hex's
State of Data Teams
2026 report, enabling self-serve dropped out of data teams' top focus areas as AI implementation took over — yet the last-mile problem remains. The data is clean and centralized, yet it still takes a SQL-fluent analyst to pull answers out. The backlog doesn't shrink until non-data teams can explore the output themselves.
This played out at
Mercor
, where the operations team needed to track 60+ metrics across hundreds of active projects but had no data team for most of the company's growth. By connecting their Snowflake warehouse to Hex, team members who'd never written SQL built their own dashboards, contributing to more than $100M in revenue. Strong pipeline infrastructure plus a usable consumption layer turns ETL work into day-to-day decision-making.
5. Real-time inventory and operations
The situation
An e-commerce company with multiple warehouses needs accurate, real-time stock levels across its website, mobile app, and third-party marketplaces. Batch updates every few hours lead to overselling and overstocking.
How the pipeline works
Extract (change data capture):
Debezium reads from the warehouse management system's transaction log, capturing every inventory change without querying the production database.
Transform (streaming):
Apache Kafka streams changes through transformation logic that updates quantities, triggers reorder alerts below thresholds, and calculates allocation across channels.
Load:
The online store consumes from Kafka for immediate updates, and the same data feeds the warehouse for demand forecasting.
That design keeps the website accurate without waiting for the next batch job.
What you learn
When a flash sale drains a product category faster than expected, the system triggers reorder alerts within seconds instead of discovering the stockout in tomorrow's report. Historical data still powers weekly demand forecasting, while the streaming layer handles the urgent updates.
Processing modes: batch, streaming, and CDC
The five examples above use different processing modes, and the choice comes down to how fresh your data needs to be.
Most organizations end up with a hybrid: streaming for time-sensitive events, batch for deeper historical analysis. CDC reads directly from database transaction logs instead of querying the source, giving you the freshest data without putting load on production systems. That's why Example 5 above uses
change data capture
for inventory sync.
Common ETL tools and where they fit
In practice, teams mix and match tools across pipeline stages rather than building everything from scratch. The choice at each layer depends on your data volume, team size, and how much infrastructure management you want to own.
Extraction and loading.
Managed connector platforms like Fivetran, Airbyte, and Stitch handle the plumbing of pulling data from SaaS APIs, databases, and event streams. They manage authentication, schema detection, and incremental updates. If your team is spending weeks building custom connectors, these tools give that time back.
Transformation.
dbt has become the default transformation layer for teams running ELT. Analytics engineers write transformation logic in SQL, define data quality tests alongside models, and version everything in Git. For teams that need Python alongside SQL, notebook environments let data scientists build transformations, statistical models, and visualizations in the same workspace.
Orchestration.
Airflow, Dagster, and Prefect manage scheduling, dependency resolution, and failure handling. When a pipeline step fails, you configure whether to retry, alert, or skip downstream jobs. Pick based on how much configuration-as-code your team wants to manage vs. how much you want the framework to handle.
Warehousing.
Snowflake, BigQuery, Databricks, and Redshift are where transformed data lands. The warehouse you pick affects cost structure and concurrency limits, but all four handle standard analytical workloads well. This choice matters less than what you do with the data once it's there.
Consumption.
Pipeline investments either pay off or stall at this layer. You've done the work to clean and centralize the data, but teams still need a way to explore it, define governed metrics, and share results without rebuilding in another tool.
Hex
lets teams write SQL or Python against their warehouse, ask questions in natural language, and publish findings as interactive apps, all without leaving the workspace where the analysis started. That's the layer that turns pipeline output into something people actually use.
Where ETL pipelines break
You usually find out your pipeline is broken at the worst possible moment: when someone's already made a decision based on bad data. Here are the failure modes that show up most often.
Schema drift
A source system adds a column, renames a field, or changes a data type, usually without telling anyone downstream. Dashboards show null values, joins silently drop records, or aggregations return wrong totals. The most dangerous cases happen when permissive schema handling lets corrupted data flow through undetected.
Stale data loads
A pipeline job fails silently at 3am. Nobody notices until decisions are made based on yesterday's numbers. Stale data is insidious because it often looks correct: plausible numbers, valid formats, but timestamps reveal the data stopped updating hours ago.
Silent quality degradation
A source system starts sending slightly malformed records. A transformation handles them permissively instead of rejecting them. Over weeks, the drift compounds until reports stop matching source systems.
If any of these sound familiar, you're not alone. The common thread is that they're all cheaper to catch early. Automated tests, freshness monitors, and
semantic layers
that enforce consistent metric definitions go a long way toward preventing the trust erosion that makes stakeholders stop believing any number the data team produces.
How AI is changing ETL pipelines
Teams are already using large language models (LLMs) to generate and review dbt models, suggest schema mappings, and draft data quality tests. Some are exploring pipelines that detect and resolve common failures like schema changes automatically, though that approach is still maturing. And data quality checking is moving from static, rule-based validation toward anomaly detection that learns what "normal" looks like and flags deviations.
The engineering changes are real but incremental. The bigger shift is downstream. AI agents now translate natural-language questions into governed SQL against the same warehouse your ETL pipelines feed. That's changing who gets value from the infrastructure, and how quickly. In the State of Data Teams 2026 report, AI surged from 4% to 27% as a top goal for data teams in a single year. Teams have moved from experimentation to active implementation of
AI analytics
.
Getting value from the pipeline
A reliable ETL pipeline gets data into one place. What turns that infrastructure into decisions is what happens next: defining metrics consistently, giving non-data teams a way to explore on their own, and creating an environment where data scientists and business users can actually work together. Without that last mile, you're maintaining pipelines that load tables nobody queries.
Hex connects directly to your warehouse so the data flowing through your pipelines becomes analysis, not shelfware. Sign up for a
free trial
or
request a demo
to see how it works with your existing stack.
Frequently Asked Questions
How do I know if my ETL pipeline is actually working correctly?
Most teams find out their pipeline is broken when an analyst gets a wrong number, not when an alert fires. To build confidence, you need automated freshness checks, volume monitoring, schema validation, and data quality tests on your transformation logic. Tools like dbt's built-in testing and semantic models that enforce consistent metric definitions catch issues before they reach stakeholders. If you're not sure where to start, begin by monitoring freshness.
How do I decide between building custom ETL pipelines and using managed tools?
It depends on your team's size and where you want to spend engineering time. Managed extraction and loading tools like Fivetran or Airbyte handle the undifferentiated work of connecting to source systems, managing schema changes, and running incremental syncs. That frees your engineers to focus on the transformation logic that's specific to your business. Most teams start with managed connectors and only build custom pipelines for sources that aren't well supported or for data volumes that need fine-grained control over batching and error handling.
Do I need a dedicated data engineering team to run ETL pipelines?
Not necessarily. Managed ELT tools handle extraction and loading with minimal engineering, and dbt lets analytics engineers own transformation logic in SQL. Mercor grew to over 200 employees with no dedicated data team, relying on managed tools and Hex to put data directly in operators' hands. As your data sources multiply and pipeline complexity grows, having someone who understands orchestration and monitoring becomes increasingly important, but you don't need a full team to get started.
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
