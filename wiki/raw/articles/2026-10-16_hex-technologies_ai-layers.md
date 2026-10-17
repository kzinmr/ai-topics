---
title: "What are AI layers? And 5 essential AI layers for data teams"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/ai-layers/"
scraped: "2026-10-16T06:00:52.877766+00:00"
lastmod: "2026-02-19"
type: "sitemap"
---

# What are AI layers? And 5 essential AI layers for data teams

**Source**: [https://hex.tech/blog/ai-layers/](https://hex.tech/blog/ai-layers/)

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
What are AI layers? And 5 essential AI layers for data teams
Five layers that determine whether AI compounds or fragments your data stack
The Hex Team
Data
February 19, 2026
Share:
twitter
linkedin
In this article
What are AI layers? And why they matter for data teams
Layer 1: Infrastructure
Layer 2: The foundation models
Layer 3: Orchestration and tooling
Layer 4: Interface and applications
Layer 5: Governance
Bringing the layers together
Get started for free
If you've spent the last year fielding requests to "add AI" to your data stack, you're not alone. Every tool seems to have added a chatbot, a copilot, or some flavor of "intelligence." But beneath the surface of these features sits something more concrete — a structured set of layers that make AI actually work in production environments.
Whether you're building, buying, or evaluating AI tools, knowing how the layers connect helps you make better decisions about where to invest time, budget, and trust. The technology isn't magic, it's architecture.
What are AI layers? And why they matter for data teams
AI layers are the components that make an analytics tool AI-native rather than AI-adjacent. Think of them like the interconnected systems in a car: engine, transmission, fuel, electronics, and controls. Each serves a specific purpose, but they only produce motion when they work together.
Many tools have added AI features to existing interfaces. But there's a difference between AI as an appended feature and AI as architecture.
An AI-native analytics platform has these capabilities built in from the start:
Infrastructure connections:
How the tool connects to your warehouse, data sources, and compute
Foundation models:
Pre-trained models powering text-to-SQL, code assistance, and natural language interfaces
Orchestration and tooling:
Workflow management and automation that keep AI-generated outputs current
Interface and applications:
Where users interact with AI capabilities through notebooks, chat, and APIs
Governance:
Consistent definitions, access controls, and auditability of AI-generated insights
When these layers are integrated from the start, your warehouse stores the data, foundation models generate queries using governed definitions, orchestration keeps outputs current, and interfaces serve both technical and business users from the same source of truth. When they're added separately, gaps emerge. Business users may get inconsistent definitions. Technical users can't always verify AI-generated logic. Governance becomes harder to maintain.
Hex shows how these layers work together in practice. When business users ask questions in
Threads
, foundation models generate SQL that queries your warehouse (infrastructure) using metric definitions from
Semantic Modeling
and many other context artifacts, including endorsed statuses, warehouse descriptions, and workspace guides (see all of them in
this guide
). Technical users can review and verify the generated SQL innotebooks, ensuring both technical and non-technical users work with the same definitions and access controls.
Layer 1: Infrastructure
Infrastructure is the
compute, storage, and networking capacity
that determines whether your AI systems can scale from prototype to production without rebuilding everything. Without sufficient infrastructure, the other layers can't function, regardless of how sophisticated your models or tools are. In fact, when you move from sample data to production scale, infrastructure either handles it smoothly or forces a rebuild.
Your infrastructure generally includes:
Data warehouse
(Snowflake, BigQuery, Redshift) where your structured data lives
Compute resources
for running models, including GPUs and cloud machine learning (ML) services
Data lakes and
storage systems
(S3, GCS) with formats like
Apache Iceberg
and Delta Lake
Cloud provider services
(AWS, Azure, GCP) that tie it all together
The infrastructure decisions you make early shape what becomes easy later. Modern data warehouses like
Snowflake
and
BigQuery
handle structured analytics well, while platforms like
Databricks
integrate ML workflows more naturally.
AI workloads benefit from infrastructure that supports faster iteration, which spins up compute when you need it, connects to multiple data sources, and handles both SQL queries and Python model training without switching environments.
Teams working effectively with AI tend to consolidate rather than fragment because fewer platforms mean less context-switching, more consistent governance, and simpler workflows from exploration through production.
Layer 2: The foundation models
Foundation models are large-scale ML models trained on broad, generalized data that serve as starting points for AI applications. Rather than building intelligence from scratch, data scientists use these pre-trained models to develop applications more quickly and cost-effectively.
Today's foundation models (Claude, GPT-5, Gemini, Llama) perform diverse tasks like generating text, writing code, analyzing images, and answering questions out of the box. They also accept plain English inputs, making them accessible to anyone, even users without deep ML expertise.
Pre-trained models change the economics of AI projects entirely. Instead of needing a dedicated ML team and months of training, a small analytics team can tap into capabilities that would have required millions in R&D just a few years ago.
That said, while the barrier to entry has dropped, the need to understand how these models fit into your broader stack hasn't gone away. For analytics teams, foundation models enable three practical capabilities:
Text-to-SQL translation:
Non-technical users query databases using plain English while data teams maintain SQL execution control
Code assistance:
Helps analysts write and debug SQL and Python, compressing the cycle time between idea and test
Data exploration:
Conversational interfaces open advanced analytics to business users who know the right questions but lack SQL expertise
Hex's AI
takes this further by understanding your
warehouse schema and semantic models
. That way, when business users ask questions in
Threads
, the AI generates SQL that technical users can review, modify, and verify. The questions happen in natural language, but the execution stays controlled and transparent. An AI-assisted platform where data teams and business users work side-by-side enables collaboration without sacrificing technical oversight.
These capabilities
make analytics more collaborative
. Technical and non-technical users can explore data together, each working at their own level of expertise.
Layer 3: Orchestration and tooling
Orchestration determines whether your data work runs reliably without constant manual intervention. It manages the recurring workflows data teams depend on, like refreshing dashboards, running transformations, updating reports, and keeping everyone working from current data.
The orchestration layer handles three core functions:
Scheduling:
Running jobs at specific times or intervals (refreshing a dashboard every morning, updating a model weekly)
Dependency management:
Ensuring tasks run in the right order (transformation A completes before dashboard B refreshes)
Failure handling:
Detecting when something breaks, retrying automatically, and alerting the right people
Tools like
Apache Airflow
,
Prefect
, and
Dagster
provide these capabilities at different scales and with different tradeoffs. Airflow dominates at enterprise scale, while Prefect and Dagster offer more developer-friendly experiences for smaller teams.
The tooling layer includes the infrastructure that connects your workflows, like
dbt
for transformations, data quality checks, version control, and deployment platforms. These tools need to work together smoothly so analysts can focus on analysis rather than manually coordinating updates across disconnected systems.
This played out at
Whatnot
, where the live shopping platform modernized its data infrastructure and streamlined workflow coordination. By adopting dbt and Hex together with SQL as the common language, the team automated repetitive tasks and reduced time spent on maintenance, letting them focus on building new capabilities rather than manually coordinating workflows across disconnected tools.
Layer 4: Interface and applications
The interface layer determines how people across your organization interact with AI, and whether those interactions compound into something useful or scatter across disconnected tools.
Notebooks
are where deep analysis happens.
They combine code execution, visualizations, and narrative in interactive environments built for complex, multi-step work. Hex has the world’s more powerful and collaborative notebook where teams write SQL and Python, visualize results, and document their thinking — with real-time multiplayer editing, commenting, and version control built in. And with native agentic features like the
Notebook Agent
, notebooks are becoming accessible to less technical users who can build analyses with AI assistance rather than writing every query from scratch.
Conversational interfaces
are how people get quick answers to data questions.
Instead of filing a ticket or building a dashboard, someone asks a question in natural language and gets SQL-backed results with charts and deep insights. Data teams can see and verify the logic behind every answer, so both quick questions and deep analyses stay connected to the same source of truth.
Embedded workflows bring analytics into the tools people already use.
Through integrations like the
Hex MCP server
, AI analytics can surface directly in Cursor, Slack, Claude, and ChatGPT — so people get answers where they work instead of switching to a separate analytics tool.
The challenge is supporting all these modes of work without fragmenting the workflow. When deep analysis, quick questions, and embedded insights live in separate tools, collaboration breaks down and work gets duplicated. An analyst builds a dashboard in one tool, then a PM asks a follow-up question in another. Without shared context, someone rebuilds the same logic from scratch — or worse, builds something slightly different and calls it the same thing.
There's also a compounding cost: every question asked in a disconnected tool is context that never flows back to the data team and is unavailable to agents — no signal on what people are asking, what analyses already exist, or where definitions need tightening. When everyone works on the same platform, that context accumulates. Agents get more accurate over time because they draw on a growing body of real questions, vetted analyses, and governed definitions — not just a static schema.
A unified AI Analytics platform like Hex addresses both problems by enabling all of these human-agent work modes in one governed system: deep work in SQL and Python, conversational interfaces for business users, and an MCP for working elsewhere without sacrificing trusted data context. Every interaction feeds context that makes the next answer better.
Layer 5: Governance
Governance is the set of controls that ensure AI-generated insights use the right data, follow the right definitions, and respect access permissions. Without it, AI can amplify existing problems — if five teams define "revenue" differently, AI may confidently generate five different answers to the same question. In practice, that means defining metrics consistently, tracking data lineage, controlling access, and auditing what AI systems do with your data.
The
NIST framework
provides structure through three core functions — Map (identify and contextualize risks), Measure (evaluate using metrics and monitoring), and Manage (prioritize and respond throughout the lifecycle) — with Governance as a crosscutting function to provide oversight, policies, and accountability.
Practical governance for data teams means:
Data quality management:
Automated validation that catches errors before they reach users
Lineage tracking:
Connecting every metric to its source so you know where numbers come from
Security architecture:
Access controls that determine who can see which data, with audit trails showing who accessed what and when
Consistent definitions:
Semantic models that define metrics once and use them everywhere
Hex gives data teams multiple ways to govern how AI agents behave. Lighter-weight options like endorsing tables and adding a
workspace rules guide
let teams get started quickly.
Semantic Modeling
adds governed metric definitions on top — define revenue once, and every agent uses the same calculation. And
Context Studio
closes the loop: data teams can see what questions are being asked, how often agents produce quality issues, and what actions to take to improve responses over time.
When an analyst builds a dashboard using "revenue" and a business user asks about "revenue" in Threads, they're using the same definition. No more five versions of the same metric creating confusion. This governance layer works because it operates within the same unified workspace where both technical and non-technical users collaborate: Threads generates SQL that respects the semantic models and access controls your data team has defined.
Governance ensures controls that let teams explore data confidently. When everyone knows the metrics are consistent and the access controls work, teams can move faster instead of questioning every number.
Bringing the layers together
Understanding the AI stack means seeing it as an architecture, not a checklist. Each layer depends on the others, meaning problems in one layer
can
ripple through the rest.
The teams getting real value from AI have infrastructure that connects smoothly to foundation models, orchestration that keeps workflows running reliably, interfaces serving both technical and business users, and governance ensuring everyone works from consistent definitions. When these layers integrate well, data teams spend less time managing tools and more time generating insights.
Hex demonstrates this integration in practice. Data teams and business users work within the same workspace, with AI embedded throughout, and everyone operating within shared governance boundaries.
If you're looking to see how these layers come together in practice, you can
sign up for Hex
or
request a demo
.
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
Platform
AI and agents
Agentic notebooks
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
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
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Connect
Request a demo
Technical support
Contact us
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
