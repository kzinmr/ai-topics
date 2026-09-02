---
title: "What is dbt (Data Build Tool)? How It Works and Where It Stops"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-build-tool/"
scraped: "2026-09-02T06:00:23.091011+00:00"
lastmod: "2026-05-08"
type: "sitemap"
---

# What is dbt (Data Build Tool)? How It Works and Where It Stops

**Source**: [https://hex.tech/blog/data-build-tool/](https://hex.tech/blog/data-build-tool/)

Skip to main content
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
What is dbt (data build tool)?
Two analysts query the same table and land two different revenue numbers in front of the same executive. dbt exists because of that gap, but its job has a clear boundary worth understanding.
The Hex Team
Data
May 8, 2026
Share:
twitter
linkedin
In this article
What dbt is and why it became the default
How dbt models, tests, and documentation work together
Where dbt fits in the data stack
dbt Core vs. dbt Cloud: honest trade-offs
Where dbt's job ends and what breaks next
How the dbt Semantic Layer addresses metric consistency
Start with governance, then make it the easiest path
Frequently Asked Questions
Get started for free
Every data team has a version of this story. You write a query to calculate revenue. It looks right, it runs fast, and it answers the question. A week later, another analyst writes a slightly different version of the same query. Different JOIN conditions, a different filter on order status, and a
COUNT
where the first used
COUNT(DISTINCT)
. Both numbers land in front of an executive. Neither matches.
dbt (short for data build tool) exists because of that gap. It started as an open-source project at a consulting firm called Fishtown Analytics, built to bring software engineering discipline to the SQL work that turns raw data into the tables everyone queries. Fishtown later rebranded to dbt Labs and built a commercial product (dbt Cloud) on top of the open-source core. For many data teams, it worked.
But dbt's job has a clear boundary. What happens on the other side of that boundary determines whether all that governance actually reaches the people making decisions. And with agents doing more of the coding work, dbt is becoming a critical investment for more and more data teams.
What dbt is and why it became the default
dbt is a compiler and runner for SQL-based data transformations. The name stands for "data build tool," and the scope matches: you write
SELECT
statements, dbt compiles them, handles materialization, manages schemas, resolves dependencies, and runs everything against your warehouse. That scope is deliberately narrow: dbt does not extract or load data. It is the T in ELT.
That narrowness is the point. Before dbt, nobody owned the transformation layer. Data engineers owned pipeline infrastructure but not business logic. Analysts used SQL to produce analyses but didn't apply version control, testing, or documentation to their code. The result was predictable. Smartsheet's analytics engineering team documented a common pattern: undocumented transformation databases where "one table became two, became fifteen, became too many to count." Analysts who built key tables left the company. Incoming analysts re-created or duplicated those tables. Business logic lived in dashboard workbooks rather than in the database itself.
dbt solved this by treating SQL transformations like software. You get modularity through the
ref()
function, so changes to upstream models propagate downstream automatically. You also get testing baked into the build process, documentation generated from the same codebase, and standard software engineering workflows like version control, pull requests, and CI/CD.
It also helped that the timing was right. Cloud warehouses made in-database transformation economical. The
release of Amazon Redshift
in November 2012 kicked off the era where running SQL transformations inside the warehouse was cheaper and simpler than processing data externally.
Warehouse architecture
matured in parallel, and dbt arrived as that infrastructure solidified. The two grew together.
How dbt models, tests, and documentation work together
dbt's governance starts with a design choice most people overlook: models, tests, and documentation aren't separate systems. They're co-located in the same YAML property files. A single
schema.yml
simultaneously declares what a model is, what it must satisfy, and what it means:
One block documents the model, describes columns, and declares data quality assertions. That's what makes the governance stick. There's no separate documentation system that falls out of sync six months after launch.
Models
support several governance primitives. Access controls (
private
,
protected
,
public
) enforce boundaries between groups and projects. Contracts, introduced in dbt v1.5, enforce schema shape at build time so downstream consumers can trust that column types won't silently change. Versioning lets teams evolve models without breaking consumers who depend on the previous version.
Tests
are SQL
SELECT
statements that seek failing records. If a test returns zero rows, the assertion passes. Four built-in generic tests (
unique
,
not_null
,
accepted_values
,
relationships
) cover common constraints. Singular tests let you write custom SQL for business-logic assertions. These tests fill a gap specific to analytical databases: BigQuery, Snowflake, and Redshift often don't enforce NOT NULL or UNIQUE at the database level.
Documentation
is generated from those same YAML files via
dbt docs generate
, producing a browsable site with model descriptions, column definitions, and test results. The doc() function lets you write long-form descriptions once and reference them across multiple models, so documentation doesn't drift as the project grows.
These three layers have explicit limits worth knowing. Contracts don't govern what arrives from source systems. Access controls don't enforce warehouse-level permissions. And model versioning doesn't apply to snapshots, seeds, or sources. These are deliberate product scope decisions, and they matter when you're deciding what governance work belongs in dbt versus elsewhere in your stack.
Where dbt fits in the data stack
dbt occupies one layer in a pipeline that typically involves three or four others. Knowing where it starts and stops saves you from expecting things dbt was never designed to do.
In a modern ELT workflow, extraction and loading tools like Fivetran, Airbyte, or Meltano move raw data from source systems into your warehouse. dbt takes over after landing. It transforms that raw data into clean, tested, business-ready tables. Downstream, BI tools, notebooks, and AI interfaces consume those tables to answer questions. dbt sits between ingestion and consumption, and it's designed to stay there.
This means dbt doesn't orchestrate pipelines end-to-end. Teams that need cross-system coordination still pair dbt with Airflow, Dagster, or Prefect. dbt doesn't manage warehouse infrastructure, handle reverse ETL, or control how downstream tools query the tables it builds. Each of these responsibilities belongs to a different layer of the stack, and dbt's value comes precisely from not trying to absorb them.
The role and ecosystem dbt created
dbt also helped define a role. The "analytics engineer" emerged alongside dbt as the person who owns the transformation layer: writing modular SQL, maintaining data models, enforcing testing and documentation standards, and bridging the gap between data engineers focused on infrastructure and analysts focused on questions. Before this role had a name, the work still happened. It just didn't have an owner.
The ecosystem around dbt reflects this adoption. dbt Hub hosts community-maintained packages (dbt-utils for cross-database macros, dbt-expectations for data quality testing, audit-helper for comparing model changes). The annual Coalesce conference draws thousands of practitioners. And the community Discourse and Slack channels are among the most active in data infrastructure, which matters because a tool's practical value is shaped by the documentation and patterns its community produces.
The landscape is shifting, though. In October 2025, dbt Labs and Fivetran announced an
all-stock merger
expected to close in 2026. The combined company would unify extraction, loading, and transformation under one organization, with dbt Core remaining open-source. For teams evaluating the data build tool today, the merger doesn't change how dbt works or what it does. But it signals that the boundary between "move data" and "transform data" is blurring at the vendor level, even as the tools themselves stay distinct. How this affects pricing, roadmap priorities, and the dbt Cloud product remains to be seen.
dbt Core vs. dbt Cloud: honest trade-offs
Both dbt Core and dbt Cloud run the same transformation engine. The decision comes down to how much operational infrastructure your team wants to own.
dbt Core
is free and open-source (Apache 2.0). It's CLI-based, runs in any environment you control, and places no limits on developer seats, models built, or projects. The trade-off is that you own everything else: CI/CD pipelines, orchestration, secret management, IDE setup, and environment configuration are your team's responsibility. dbt Labs released an official VS Code extension powered by the Fusion engine in 2025, which narrowed the developer experience gap, but Core remains a bring-your-own-infrastructure proposition.
dbt Cloud
starts with a free Developer plan (1 seat, 3,000 models/month, 1 project), moves to Starter at $100/user/month (up to 5 seats, 15,000 models/month), and scales to Enterprise with custom pricing. For that price, you get a browser-based IDE, native job scheduling, and Slim CI, which automatically tests only modified models and their downstream dependencies on pull requests. Practitioners often say the Slim CI functionality alone justifies the cost.
Enterprise-tier exclusives include dbt Mesh for cross-project references, the visual Canvas interface, advanced orchestration, audit logging, and SSO/SAML. Enterprise+ adds PrivateLink, IP restrictions, and unlimited projects. The hosted Semantic Layer needs at least a Starter plan.
Where dbt's job ends and what breaks next
dbt builds tested, documented, governed tables in your warehouse. Then it stops. A lot of real-world pain lives on the other side of that line.
dbt can tell you that
dim_customers
has the right schema and passes all its tests. It can't tell you whether the analyst querying that table used the correct aggregation, the right filters, or the same definition of "active customer" that finance agreed on last quarter. And it doesn't enforce that anyone actually uses the governed tables instead of querying raw sources directly.
That last point matters more than it sounds. One practitioner described a common workaround in the dbt Labs analyst guide: "If I need data from a source in a staging model, at least where I can query it in Hex, sometimes I'll try to do that myself if our analytics engineers don't have capacity." That's a bypass at the staging layer, before any business logic has been applied. And it happens because governed paths are often slower than ungoverned ones.
When that pattern repeats across a team, three problems compound.
Metric drift
is the revenue scenario from the top of this article, scaled across an organization: analysts query the same tables but write slightly different SQL, producing divergent numbers.
Shadow analytics
emerges when getting a new metric means rewriting formulas from scratch rather than referencing a central definition.
And
trust erosion
reinforces itself from there. As one dbt Labs post on modular data modeling put it, if the people consuming data don't trust it, the governance work upstream stops mattering. They silo their work in spreadsheets and bury business logic in one-off dashboard filters. A single trust failure can turn a one-time bypass into a permanent parallel system.
This matters even more as AI enters the picture. When LLMs generate SQL from natural language, the same gap that previously produced inconsistent dashboard numbers now produces incorrect AI outputs. If business rules like revenue recognition live outside the schema, naive text-to-SQL translations will frequently get them wrong.
In Hex's
State of Data Teams
2026 report, 31% of data leaders now cite trust as their top concern around AI adoption, nearly double any other barrier. That finding tracks with what dbt practitioners already know: building governed tables is necessary but not sufficient.
How the dbt Semantic Layer addresses metric consistency
The dbt Semantic Layer, powered by MetricFlow, relocates metric definitions from BI tools into the dbt modeling layer. You define measures, dimensions, and entities in YAML on top of your dbt models. MetricFlow then constructs SQL dynamically at query time, generating the correct joins, filters, and aggregations so nobody downstream has to write them from scratch.
The architecture relies on a semantic graph. Semantic models define entities, dimensions, and measures. MetricFlow uses entities as graph edges and performs automatic joins, so analysts request metrics with dimensions rather than writing join SQL. The constraint is that this governance only holds when downstream tools actually query through the Semantic Layer rather than writing SQL directly against mart tables.
The dbt Semantic Layer currently integrates with Tableau, Power BI, Google Sheets, Excel, Hex, and several other platforms.
MetricFlow
itself was open-sourced under Apache 2.0 at Coalesce 2025, alongside dbt Labs' commitment to the
Open Semantic Interchange
initiative with Snowflake and Salesforce. Cloud platforms are beginning to embed semantic layer capabilities natively, and the direction looks like interoperability rather than lock-in.
Adoption has shifted meaningfully. The State of Data Teams 2026 report also found that semantic layers, once controversial, are now seen as essential. Previous skeptics have adopted standalone layers, citing fears of vendor lock-in from BI-bundled alternatives. The AI pressure described in the previous section was the driving force: once LLMs began generating SQL from governed definitions, the case for a semantic layer became harder to dismiss.
From governed definitions to governed queries
The practical question for most teams is whether the tools that consume dbt's output actually respect those definitions. Hex's agents work from your warehouse schema out of the box, so you don't need a full semantic model to get started. Syncing dbt semantic models via
Semantic Model Sync
adds governed definitions on top of that baseline, so measures and joins defined in your dbt project are available for exploration without anyone rewriting the underlying logic.
An analyst asking a question through
Threads
gets SQL grounded in those governed definitions, which means more consistent results across the team. And the
Notebook Agent
can extend that same governed context into deeper technical analysis.
Start with governance, then make it the easiest path
dbt gave data teams a governed, tested, documented transformation layer with clear ownership. The semantic layer extends that governance into metric definitions. And the ecosystem provides the community and packages to support adoption at scale.
But the open question most teams face is whether that governance carries through to the place where people actually ask questions. The teams that close this gap connect dbt's definitions to their consumption layer, so the governed path is also the most convenient one. When finding the agreed-upon definition of "active customer" is faster than writing your own, people stop working around the system.
Hex approaches this by syncing dbt metadata directly into the analyst's workspace, so governed context is available at the point where questions get asked.
Request a demo
to see how it connects to your dbt models, or
sign up for a free trial
to try it yourself.
Frequently Asked Questions
Do I need a semantic layer if my dbt models are already well-tested and documented?
Testing and documentation confirm that columns aren't null, keys are unique, and SQL models produce expected results. What they don't govern is how downstream consumers aggregate and interpret that data. Two analysts can query the same well-tested
fct_orders
model and still produce different revenue numbers because they used different filters or aggregation logic. A semantic layer addresses that gap by defining how metrics should be calculated, so the aggregation logic lives in one place rather than being reimplemented in every query and dashboard. If your team is small and communicates constantly, you might get by without one. As your team size or tool count grows, the drift becomes harder to manage through convention alone.
How does dbt's governance connect to AI-generated SQL in downstream tools?
AI tools that generate SQL from natural language need context about your data: what tables exist, how they join, and what business terms mean. Without a semantic layer, those systems guess at join paths, filter conditions, and metric definitions, and each guess can produce a different result. When you sync dbt semantic models into a consumption tool, AI-generated queries can reference governed definitions rather than inferring logic from raw schema. Hex uses those synced definitions so that
AI analytics
produces results grounded in the same metric definitions your data team maintains. The practical effect is that AI outputs become auditable against known definitions rather than opaque SQL that may or may not match what your team intended.
What's the best way to evaluate whether dbt Cloud is worth the cost over dbt Core?
Start by mapping the infrastructure your team currently manages: CI/CD, orchestration, environment configuration, and secret rotation. If your team already has reliable systems for all of these and prefers to maintain them, Core continues to be a strong choice with no licensing cost. The features that most often tip the cost-benefit analysis toward Cloud are Slim CI (which saves significant build time on larger projects by testing only what changed) and the hosted Semantic Layer (needed if you want downstream tools to query governed metrics via the dbt Semantic Layer APIs). The Hybrid Projects feature, currently in preview for Enterprise plans, also lets teams automatically upload Core artifacts into Cloud, so the decision doesn't have to be all-or-nothing.
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
✨
🔊
🎧
🌊
🍀
🤠
🎷
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
You have opted out of data tracking
