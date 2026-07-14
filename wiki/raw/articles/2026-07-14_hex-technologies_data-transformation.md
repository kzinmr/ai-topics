---
title: "A Guide to Data Transformation"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-transformation/"
scraped: "2026-07-14T06:00:44.144295+00:00"
lastmod: "2026-05-22"
type: "sitemap"
---

# A Guide to Data Transformation

**Source**: [https://hex.tech/blog/data-transformation/](https://hex.tech/blog/data-transformation/)

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
A guide to data transformation: techniques, debt, and delivery
Two SQL queries, written months apart by different people, both technically correct, producing different revenue numbers. Data transformation isn't the hard part, keeping it trustworthy as teams grow is.
The Hex Team
Data
May 22, 2026
Share:
twitter
linkedin
In this article
What data transformation is (and isn't)
Core transformation techniques in SQL and Python
Who owns transformation now (and why that's complicated)
What transformation debt looks like in practice
The gap between transforming data and sharing results
Making transformation work visible and collaborative
Start with documented logic, not more tools
Frequently Asked Questions
Get started for free
You've had a version of this morning: someone pings you on Slack asking why the revenue numbers in the board deck don't match the ones in the product dashboard. You trace the discrepancy back to two different SQL queries, written months apart by different people, using slightly different filters. Both queries are technically correct. Neither is documented. And now you're spending your Tuesday defending numbers instead of doing actual analysis.
Data transformation prevents this drift by taking raw source data and turning it into something trustworthy: clean tables, consistent metrics, reliable models that people can build decisions on. Most analysts can write a solid common table expression (CTE) or a pandas groupby in their sleep. The breakdown happens around the logic: scattered files, missing documentation, business rules that live in one person's head, and the repeated copy-paste-export routine that strips away context as analysis moves from a notebook to a stakeholder's inbox.
What data transformation is (and isn't)
Data transformation is the "T" in ELT (extract, load, transform), and it turns raw warehouse data into analysis-ready models. Raw data lands in your warehouse first, via tools like Fivetran or Airbyte, and then you prepare it inside the warehouse using SQL, Python, or both.
You rename columns, cast data types, join tables across sources, filter rows, split fields, and aggregate values. You're turning raw data into analysis-ready models that represent business reality as metrics, reports, and dashboards.
In a dbt project, this work typically follows a three-layer pattern.
Staging
creates the atomic building blocks from source data: renamed columns, normalized strings, cast types.
Intermediate
stacks layers of logic with specific purposes, preparing staging models for joining.
Marts
bring modular pieces together into the wide, rich views of business entities that stakeholders actually care about.
You start with whatever shape your source systems hand you and end with something that matches how the business thinks about customers, orders, and revenue.
Because ELT preserves raw data in the warehouse, you can reshape it again when requirements change. No need to touch your ingestion pipelines or re-sync from source systems.
The concepts are straightforward. The hard part is keeping transformation logic in one place, reviewed, tested, and documented as more people add models over time. Without that, each new project spawns its own ad hoc queries, debugging turns into guesswork, and "revenue" starts meaning three different things to three different departments.
Core transformation techniques in SQL and Python
Cleaning, reshaping, joining, and aggregating are the core operations, and each one maps to specific patterns in dbt, SQL, and Python.
Cleaning.
In dbt, you handle cleaning in the staging layer. Your staging models should rename columns, normalize strings with lower(), and cast types in CTEs before any downstream joins touch the data. If you're reaching for SELECT DISTINCT to clean up duplicates, that often signals a join problem upstream. Use ROW_NUMBER() within a CTE to filter the most relevant records before joining.
Reshaping and pivoting.
These rely on a small set of repeatable SQL patterns. You'll use ROW_NUMBER() often for ordering and deduplication. LAG() and LEAD() are your tools when you need to compare a row against the one before or after it. In dbt's intermediate layer, pivoting is structured as its own explicit step. The model name int_payments_pivoted_to_orders.sql follows the convention of naming models after both the technique and the data flow direction.
Joining.
Joining usually concentrates in the dbt marts layer. If you're bringing together more than four or five concepts, adding intermediate models helps. Simple joins across many staging models may be fine, but fewer concepts with heavy window functions can overwhelm a single model.
Aggregating.
Aggregating changes row grain, which is what separates GROUP BY from window functions. GROUP BY collapses rows; window functions don't. A running total shows the difference:
SUM(sales) OVER(PARTITION BY region ORDER BY date) AS running_sales
CTEs as the structural backbone.
CTEs are one of the easiest ways to improve SQL code quality because they give your logic a readable structure. In dbt, the {{ ref() }} function extends this across models, building the DAG that connects derived tables without custom scripting.
Who owns transformation now (and why that's complicated)
Analytics engineers now own most data transformation work, sitting between data engineers and analysts. Data engineers handle the E and L. Analytics engineers handle the T. That shift happened because ELT split extraction from preparation, and cloud warehouses made it practical to load raw data first and prepare it in the warehouse with SQL.
That shift also created new pressures.
Metric definitions drift apart. Your team calculates monthly recurring revenue one way. The product team calculates it another. One includes trial customers in user counts; the other doesn't. According to Hex's
State of Data Teams
report, 31% of data leaders cite trust as the top concern around AI adoption, nearly twice as much as any other concern. That trust problem starts with transformation: if metric definitions aren't consistent, nothing downstream can be.
Documentation falls off when deadlines hit. Analytics engineers are explicitly expected to write thorough documentation, including data catalogs for self-service access. Documentation can be added directly to models and published automatically with each deployment, but that only solves propagation. It doesn't address whether anyone actually writes the documentation in the first place.
The same logic gets built three times. In large organizations, data consumers struggle to find existing datasets, which leads to duplicate work and inconsistent metrics. When many people can build data prep logic with no central registry of what exists, each iteration introduces its own definitional choices.
The industry responded with the semantic layer, a centralized definition layer sitting between your prepared data and the tools that consume it. A semantic layer locks down business metrics so that when different teams ask questions of data, they get the same answers. But in 2025, 57% of teams that invested in a semantic layer were already considering switching their BI tool. The semantic layer addresses metric consistency without resolving overall tool satisfaction.
What transformation debt looks like in practice
Transformation debt looks like shortcuts, undocumented decisions, and fragile design choices that quietly make your data less trustworthy. Unlike software bugs that crash builds, this kind of debt fails silently.
The bus factor of one.
Most teams have at least one person whose departure would break multiple dashboards. The pipeline works because that person understands it. Their mental model is the documentation. When they leave, the transformation becomes archaeology. Transformation debt can occupy capacity that would otherwise go toward analysis.
The silent schema break.
A developer on the product team renames a column or changes a data type. They don't notify the data team. The pipeline doesn't crash. It starts producing wrong output. Without automated handling, schema drift creates constant maintenance headaches, and you never know if your reports are complete or based on a broken feed.
Five definitions of "revenue."
Finance reports one churn number. Product reports another. The CEO asks which one is right. Nobody answers confidently. When two departments report different numbers for the same key performance indicator (KPI), the mismatch usually comes from refresh timing, metric logic, or filters that diverged quietly over time. Teams respond by building their own copies and treating their version as canonical. Soon nobody can resolve the conflicting reports.
The gap between transforming data and sharing results
The gap between transforming data and sharing results shows up in a string of manual steps that nobody tracks and nobody can reproduce. When you need to get analysis into someone else's hands, you rerun queries, export charts, paste screenshots into slides, and answer follow-up questions without the original logic attached.
Every handoff strips away context. When analysis moves from a notebook to a presentation tool, the query logic, the caveats, the data lineage, and the assumptions stay behind. What arrives in the stakeholder's hands is a chart or a number, divorced from everything that would help them interpret it correctly.
Follow-up questions trigger full rework cycles. When a stakeholder receives a static chart with no live connection to the analytical environment, any follow-up means re-running the analysis and re-exporting. In 2025, 53% of respondents to Hex's State of Data Teams reported being unhappy with their BI platforms, and the rework loop is a major reason.
Even BI investment doesn't close the gap entirely. Teams with mature BI tooling still perform manual exports to produce the formatted, narrative-driven outputs that executives actually receive. BI tools support exploration and monitoring, but teams still end up doing extra work to turn that output into executive-ready reporting.
Making transformation work visible and collaborative
Make transformation work visible by putting code, documentation, and delivery in the same governed workflow. Version control lets one analyst or dozens work without chaos. Code review creates accountability and establishes a foundation for automated testing and CI. Treating transformation code like software, with changes going through pull requests and peer review before merging, creates an audit trail of who changed what and why.
In dbt, model documentation is generated from project metadata files and published when you run documentation generation or a dbt Cloud job. This practice carries growing urgency: documentation quality now directly affects AI query accuracy. As AI agents increasingly generate SQL against warehouse schemas, the descriptions in your .yml files aren't just for your teammates. They're the context that determines whether an AI agent writes a correct query or a plausible-sounding wrong one.
When transformation and delivery happen in the same environment, the notebook, the published result, version history, and stakeholder follow-up all stay tied to the same work. Environments that keep analysis, visualization, and publishing in one place solve the handoff problem by eliminating it. Instead of exporting CSVs and rebuilding charts in a separate tool, analysts iterate and publish from the same
collaborative notebooks
where the transformation logic lives. When a stakeholder asks a follow-up question, the analyst iterates in the same environment where the original work lives.
This played out at Workrise, the energy workforce management company, where multiple analytics tools made collaboration difficult and analysts had to recreate visuals after exploratory work. After consolidating into Hex, over 50 people now create analyses in one place with far less tool fatigue and faster analytics cycles.
Keeping work in fewer places also makes tests and ownership easier to maintain. dbt's two primitive test types (generic/schema-style tests for uniqueness, not-null, accepted values, and referential integrity, plus singular/data tests for business rule validation) help surface problems early in development before deployment. Data contracts between producers and consumers, covering schema, freshness, and reliability, reduce friction and prevent silent breakages.
You don't need a major overhaul to start. Start with style conventions and naming standards before the project scales. Identify structural deviations early. Assign explicit ownership of metric definitions before they proliferate. Over a few months, those practices turn transformation from one person's knowledge into a shared, maintainable system.
Start with documented logic, not more tools
Whether your metrics are trustworthy or merely directional comes down to how you handle transformation. The techniques are well-understood and the tooling has matured. The hard part is making sure the same definitions, tests, and outputs survive contact with real team workflows.
Version control and peer review are the floor. Every model change should go through a pull request. This catches errors, yes, but more importantly it distributes knowledge across the team. When three additional people have reviewed a revenue model, the bus factor increases from one to four.
Keep metric definitions with the code that implements them. If your metric definitions live in a Confluence page that hasn't been updated since Q2, they don't exist. Write descriptions in your .yml files, publish them automatically with each deployment, and treat them as part of the deliverable. With AI agents increasingly connected to data infrastructure, this documentation does double duty: it helps your teammates and it helps AI tools query your data accurately.
Reduce the manual work between analysis and the final deliverable. The time your team spends exporting CSVs, reformatting charts, and rebuilding work in presentation tools is time spent on mechanics, not insight. Hex brings AI into day-to-day data analysis in a way that keeps the underlying work visible. People can explore data using natural language, with or without code, in one workspace where transformation and stakeholder delivery stay connected. If you want to see how that changes day-to-day data work,
request a demo
.
Frequently Asked Questions
How do I decide whether transformation logic belongs in dbt models or in a notebook?
If the logic will be reused by multiple consumers (dashboards, reports, other models), it belongs in dbt where it can be version-controlled, tested, and documented as part of your project's DAG. If you're doing exploratory work, one-off investigation, or prototyping a new metric definition, a notebook environment gives you faster iteration with SQL and Python side by side. Many teams develop and validate transformation logic in notebooks, then promote the final version into a dbt model once it's stable. The two workflows complement each other rather than competing.
How does a semantic layer relate to my existing dbt transformation work?
A semantic layer sits on top of your transformed data, defining how business metrics are calculated and making those definitions available to consuming tools, including BI workspaces and AI agents. If you're already building dbt models, you've done the hard part of cleaning and structuring the data. The semantic layer adds a consistent vocabulary layer so that "revenue" or "active user" means the same thing regardless of who's querying or which tool they're using. Some analytics platforms can surface dbt-documented model metadata directly in the data browser, so you don't have to choose between building in one place and consuming in another.
What's a practical first step if my team has significant transformation debt?
Start by identifying the two or three most business-critical metrics that different teams define differently, then centralize those definitions in version-controlled dbt models with schema tests and documentation. You don't need to audit every pipeline or refactor your entire project at once. Pick the metrics that cause the most confusion in stakeholder meetings, apply not_null and unique tests, write clear descriptions in your .yml files, and need peer review before changes merge. That small surface area gives you a foundation to expand from, and it immediately reduces the number of "which number is right?" conversations.
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
