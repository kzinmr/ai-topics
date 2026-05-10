---
title: "Semantic Modeling: How to Build a Single Source of Truth | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/semantic-modeling/"
scraped: "2026-05-10T01:29:13.806192+00:00"
lastmod: "2026-02-13"
type: "sitemap"
---

# Semantic Modeling: How to Build a Single Source of Truth | Hex 

**Source**: [https://hex.tech/blog/semantic-modeling/](https://hex.tech/blog/semantic-modeling/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
Semantic modeling: how to build a single source of truth for your data
Three departments, three revenue numbers, zero confidence in any of them — semantic modeling is how you fix that.
The Hext Team
Data
February 13, 2026
Share:
twitter
linkedin
In this article
What happens without a semantic model
The building blocks of a semantic model
How to build your semantic model
Where to go from here
Get started for free
You've seen it happen. Someone asks "What was our revenue last quarter?" and three departments produce three different numbers. Finance has one figure, Sales has another, and Marketing is working from something else entirely. A semantic model, sometimes called a semantic layer, is the fix: a business translation layer that sits between your raw data and the people who use it. The physical database schema defines
how
data is stored: tables, columns, foreign keys. A semantic model defines
what
that data means to the business. It knows that "Monthly Revenue" is the sum of completed order amounts, divided by 100, filtered to the current month. The database speaks SQL. The CFO speaks finance. The semantic model translates between them.
You're likely feeling pressure from two directions at once. More people across your org want direct access to data, and
self-service analytics
is the goal, not the exception. But without shared definitions, that access just multiplies the inconsistency. At the same time, AI agents generating SQL without sufficient semantic context (the combination of warehouse descriptions, workspace rules, endorsed tables, and semantic models that guides how agents interpret your data) tend to produce plausible-sounding answers that encode the wrong business logic. Semantic modeling addresses the consistency problem. Paired with the rest of your semantic context, it gives agents the governed definitions they need for your most important metrics.
What happens without a semantic model
Without a semantic model, you get metric drift. When someone asks for "revenue by customer segment," different analysts write their own SQL, making slightly different choices about what counts as revenue. One handles refunds one way, another treats subscription renewals differently, a third applies currency conversions with different logic. Dashboards diverge. Reports conflict. And your team spends weeks reconciling numbers that should have matched from the start.
This drift happens organically. Each analyst's logic is defensible on its own, but the inconsistencies compound into system-wide confusion that erodes trust across the org. Finance defines "revenue" by GAAP recognition principles, while Sales counts it at contract signing. Both are correct by their own standards, but they're contradictory in the same meeting. A single metric like "churn rate" splinters into customer churn, revenue churn, logo churn, and user churn, each legitimate but incompatible when your VP gets conflicting reports using the same term.
This played out at
Calendly
, where the analytics team was stretched thin delivering fast responses to stakeholder requests but struggling to maintain a trusted source of truth. They built a Standardized Metric Library as company-wide KPI documentation, creating the consistent definitions they needed to resolve conflicting interpretations and get new team members up to speed.
The costs go beyond wasted time. Once stakeholders lose trust in the numbers, they stop using data for decisions, or worse, they build shadow systems that create even more inconsistency.
The building blocks of a semantic model
If you've worked with dbt, the structure will feel familiar. A semantic model is defined in code, typically YAML, in tools like
dbt
MetricFlow, though other semantic layers use different syntaxes. Four core components together create a shared vocabulary for your analytics.
You define
entities
(the business objects your tables join on: customers, orders, products),
dimensions
(the attributes people group and filter by: region, channel, acquisition source),
measures
(the aggregatable numbers: sums, counts, averages), and
metrics
that combine measures with your business logic. "Net Revenue," for instance, might be gross revenue minus refunds minus discounts, filtered to completed orders only.
In practice, a metric definition in YAML might look something like this:
metrics:
- name: net_revenue
type: derived
label: "Net Revenue"
description: "Gross revenue minus refunds and discounts, filtered to completed orders"
calculation: "{{ metric('gross_revenue') }} - {{ metric('refunds') }} - {{ metric('discounts') }}"
filter:
- "{{ dimension('order_status') }} = 'completed'"
You write that definition once, specifying what counts as revenue, which orders to include, and how to handle refunds. Every downstream consumer gets the same number.
These components work together through a hub-and-spoke architecture. The semantic model sits at the hub, and every downstream consumer (dashboards, notebooks, AI agents, data apps) queries the same centralized definitions.
A compilation engine like
MetricFlow
takes those YAML definitions and generates the correct SQL for each query, handling join paths and applying business logic so that consumers don't need to understand the underlying table structure.
When a metric definition changes, say finance decides refunds should be handled differently, that update propagates everywhere at once. Every dashboard, report, and AI-generated analysis reflects the change without anyone tracking down individual queries.
To see the difference concretely: without a semantic model, two analysts might query revenue like this —
Both queries are defensible. Neither is wrong. But when your CFO sees two numbers in the same meeting, trust erodes. A semantic model eliminates this by encoding one canonical definition that both analysts, and every AI agent, use automatically.
How to build your semantic model
Building a semantic model doesn't need a big upfront investment. Successful implementations start small and expand coverage as the team validates the approach.
Start with your most contentious metrics.
Pick the two or three metrics that cause the most reconciliation headaches, usually revenue, churn, or active users. Define those first, including all the edge cases that currently cause disagreement. If your finance team and sales team produce different revenue numbers, the process of writing a single YAML definition forces the conversation about which calculation is canonical. Be realistic about the timeline here: getting cross-functional agreement on a metric like "revenue" can take weeks of discussion, especially when multiple teams have built workflows around their own definitions. That alignment work is worth doing, but it's organizational as much as technical.
Build on well-normalized staging models.
Your semantic model should sit on top of clean, transformed data, not raw tables. If you're using dbt, your staging and mart models are the natural foundation. The semantic model adds business meaning to what dbt has already structured.
Adopt incrementally, in parallel with production.
Don't try to migrate everything at once. Run your semantic model alongside existing dashboards and queries. As people validate that the governed metrics match expectations, gradually shift traffic to the semantic layer. This parallel approach reduces risk and builds confidence with stakeholders who are skeptical of change.
Validate through continuous integration (CI).
Treat your semantic model definitions the same way you treat dbt models: test them in CI, review changes through pull requests, and version-control everything. Once a metric passes validation and review, anyone can use it without additional approval. This is where governance shifts from reviewing every analysis at consumption time to validating definitions once at the source, a distinction that matters more as your team grows.
Close the feedback loop.
The hardest part isn't the initial build; it's maintaining accuracy as the business evolves. New products launch, definitions shift, edge cases emerge. You need visibility into how metrics are being used and where definitions are falling short. Hex's
Context Studio
helps here: it shows what questions people are asking, where agents or analysts are hitting ambiguity, and where governance needs tightening, so you can prioritize what to model next.
One thing worth keeping in mind: semantic models are one layer within a broader semantic context. You can start lighter, by endorsing tables and adding warehouse descriptions, or by writing workspace rules that guide how agents and analysts approach your data. Semantic models add codified business logic on top of that foundation, and observability tools like Context Studio close the loop. Each layer strengthens the others, and you don't need all of them to get started.
Hex's AI agents can query your warehouse using schema metadata, endorsed tables, and workspace rules before you've defined a single governed metric. Those sources of context already go a long way toward accurate answers. Semantic models deepen that accuracy for your most important metrics, the ones where "close enough" isn't good enough. But they're not the only thing agents rely on, and they shouldn't be positioned as a prerequisite for getting started.
Where to go from here
Semantic modeling isn't something you finish. It's infrastructure that evolves with your business: new products, new metrics, new edge cases, new questions. The goal isn't perfection on day one. It's building a foundation that lets your org speak a common data language, whether the questions come from analysts, executives, or AI agents. Start where you are, deepen as you go.
If you want to see how semantic modeling works in practice,
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
