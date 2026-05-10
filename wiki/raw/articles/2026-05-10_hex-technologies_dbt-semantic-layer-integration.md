---
title: "Introducing Hex’s Integration with the dbt Semantic Layer | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/dbt-semantic-layer-integration/"
scraped: "2026-05-10T01:29:17.643279+00:00"
lastmod: "2022-10-17"
type: "sitemap"
---

# Introducing Hex’s Integration with the dbt Semantic Layer | Hex 

**Source**: [https://hex.tech/blog/dbt-semantic-layer-integration/](https://hex.tech/blog/dbt-semantic-layer-integration/)

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
Introducing Hex’s Integration with the dbt Semantic Layer
A new Metrics cell, dbt-flavored SQL in Hex, and more!
Claire Carroll
Company
Product
October 17, 2022
Share:
twitter
linkedin
In this article
Bringing governed metrics to the data stack
Making analytics consistent, fast, easy
But wait, there’s more: dbt-flavored SQL in Hex
dbt + Hex
Get started for free
Today we’re releasing a powerful, first-class integration with the dbt Semantic Layer.
At the heart of it is a new Metrics Cell: an easy-to-use UI that lets anyone access trusted, governed metrics, without writing any code. Users can specify metrics, dimensions, and time grains, and get back a data frame that they can use to analyze, visualize, and share.
Configuring the Metrics cell
But there’s more – connecting to the dbt Proxy Server unlocks another superpower: the ability to write dbt-flavored SQL, right in Hex. Now you can use refs, macros, and sources directly in your queries.
We’re so excited to unleash the full potential of the work Analytics Engineers do every day, and empower thousands of users to more easily ask and answer questions of data.
Bringing governed metrics to the data stack
For the last few months, our friends at dbt Labs have been working on their new Semantic Layer – a way for Analytics Engineers to define consistent, governed metrics as part of their transformation pipelines. You can read a ton more about it
here
.
Hex’s integration
makes those metrics usable for everyone to ask and answer questions, with high trust that they’re looking at the data the right way.
For example, let’s say the Head of Sales Ops wants to analyze last quarter’s revenue, by month, by location, broken down by rep. Previously, they’d have to understand the underlying data schemas, and know how to write a fairly complex query. And even if they are a SQL master, there’s no guarantee that they’re going to build it in a consistent way – they could well get the incorrect answer.
Now, if their data team is using the dbt Semantic Layer, they can just add a Metrics cell to a Hex project, specify the “revenue” metric, time grain and location, without having to know how to write any SQL themselves. If they choose to switch to looking at the results by week, or add another dimension to slice by, they don’t need to fuss with the SQL and adjust
group by
statements; a quick UI change updates the query for them.
Making analytics consistent, fast, easy
Hex workflows using the dbt Semantic Layer mean that everyone can do more with data together:
Current SQL-literate users in Hex can save time by pulling data through the Metrics cell, instead of having to adjust lines of SQL for every new request.
Users of all technical levels are able to participate in analytics workflows in a way they simply couldn’t before – no code necessary.
Everyone can have confidence that they’re building their analyses on consistent, governed metrics defined by their data team. No more re-writing queries or getting different answers!
And in Hex the analysis doesn’t stop there. Just like SQL cells, the Metrics cell returns a data frame, which can be used downstream in any of Hex’s cells. You can visualize the results in a
Chart
or
Map cell
, transform the data frame in the
Filter or Pivot cell
, reshape it using
Dataframe SQL
, or even use a Python package like Prophet to produce a forward forecast, like in
this project
.
The results of a Metric cell can be used downstream, like any other data frame.
But wait, there’s more: dbt-flavored SQL in Hex
As soon as we started playing with the dbt Server, we realized that this integration could unlock
another
superpower:
the ability to write dbt-flavored SQL, right in Hex.
No more swapping out table names when switching between a dbt project and SQL IDE – refs, sources and macros are all available where you’re already doing your work.
With dbt-SQL, Hex editors can:
Query dbt models directly via the ref function, making it clear which models are used in your Hex projects
Quickly prototype models that can be transferred to a dbt project later with minimal editing.
Access useful macros in your dbt project, unlocking workflows like comparing two tables in a warehouse using the
audit-helper
package.
You’re even able to mix and match Jinja: if your SQL cell contains Jinja that references a variable in your Hex project, we’ll compile that, and leave the rest for dbt.
All of this adds to our
existing, powerful integration for enriching schemas with dbt docs, freshness, and metadata right in Hex
:
The Hex schema browser, complete with dbt documentation
dbt + Hex
We’re pumped to have our dbt Semantic Layer integrations out in the wild, and can’t wait to see what you all build with it. We’d love to hear feedback, or ideas on what you want to see next – get in touch at
[email protected]
.
Share:
twitter
linkedin
💡 If you’re attending dbt’s Coalesce this week in New Orleans, swing by the Hex Diner at Booth #313 to get a live demo of the Metrics cell! Or if you’re attending virtually, check out our sessions.
👩‍💻 Find us at Coalesce
✨ Try Hex for free
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
