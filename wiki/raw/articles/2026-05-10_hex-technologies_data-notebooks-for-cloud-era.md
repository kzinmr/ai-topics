---
title: "Bringing data notebooks into the cloud era | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-notebooks-for-cloud-era/"
scraped: "2026-05-10T01:28:58.970793+00:00"
lastmod: "2022-06-23"
type: "sitemap"
---

# Bringing data notebooks into the cloud era | Hex 

**Source**: [https://hex.tech/blog/data-notebooks-for-cloud-era/](https://hex.tech/blog/data-notebooks-for-cloud-era/)

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
Bringing data notebooks into the cloud era
Query mode, Chained SQL, and Python pushdown for everyone
Barry McCardel
Product
June 23, 2022
Share:
twitter
linkedin
In this article
∞ Query mode
⛓ Chained SQL
🐍 Pushing Python to Snowpark
📈 Bonus: infinite-scale charts
Get started for free
We’re living in an era of infinitely-scalable cloud data infrastructure, but computational notebooks — a mainstay of data science workflows — haven’t caught up. The in-memory kernel model limits the amount of data you can work with, and the ephemeral, disorganized nature of notebooks holds data teams back from doing their core job: asking and answering questions.
We built Hex, however, to be
cloud-native
, and today we’re
introducing three new features that allow you to work with data at any scale: Query mode, Chained SQL, and Python pushdown.
∞ Query mode
First, we’re launching Query mode for SQL cells, which lets you work with effectively infinitely-sized data —
no more worrying about memory overhead or limits.
In
Query mode
, Hex leaves the data in the warehouse instead of bringing it into the in-memory kernel. It’s not just a
limit
preview though: like all cells in Hex, Query mode cells still return an object (in this case, a Query, in lovely purple). A Query object can be used downstream in other cells, and is represented in the DAG, but is just a
pointer
to the full result set.
When it’s time to build visualizations, or run in-memory operations over the full dataset, you can easily flip the SQL cell back into Dataframe mode (which is the original, and still default, behavior).
knowledge
🕵️‍♀️ Real world example:
you're working with a new dataset that has 200M rows. You want to explore it iteratively and aggregate it down as you go, but it's too big to even get started with. Query mode will let you keep results in the warehouse until they're small enough to work with in-memory, while still manipulating and iterating on the data.
⛓ Chained SQL
Next, we’re introducing the ability to reference previous queries with other SQL cells, and Hex will
automatically combine the queries into common table expressions (CTEs) on the fly.
1
To use this, just reference any SQL cell result (a Query or Dataframe) in a downstream query using the same data connection. In the background, Hex will build the
with...as
statements for you, and you can see the fully-compiled query right there in the cell:
These “Chained SQL” queries work great with Query mode, allowing you to do multiple-step operations without pulling each intermediate result into memory. Then, at the end, you can flip the last cell into Dataframe mode and have a result set ready to use.
Chained SQL is complementary to
Dataframe SQL
, which lets you query any dataframe, including other query results, Pandas dfs, or even CSVs. And of course, all of this works great with Hex’s existing
first-class SQL support
, including a schema browser, typeahead, dbt Docs, Jinja, and auto-formatting.
knowledge
🕵️‍♀️ Real world example:
you're writing a giant SQL query with 10 CTEs, and all those WITHs and parentheses are getting tough to follow. The query starts erroring, but you're not sure which CTE is causing it. Breaking this up into 10 distinct chained SQL queries, it's easy to see which SQL cell is erroring and debug it individually from the rest.
🐍 Pushing Python to Snowpark
That’s all great for SQL, but what about Python? Well, that’s becoming cloud-native too.
Last week, we introduced
support for Snowpark
, allowing you to run Python code right in Snowflake. Think of this like Query mode, for Python: Hex is running the operation in the warehouse, working with the data where it lives instead of shuttling it back and forth to an in-memory kernel.
In Hex, this support is truly first class – any existing Snowflake data source can turn on Snowpark, and then with one click create a connection in a project.
For many use cases, Snowpark is far more efficient and performant than shuttling data over the internet and executing the code in a kernel.
knowledge
🕵️‍♀️ Real world example:
you're running a model training step in Python over a large dataframe from Snowflake. With Snowpark, you can push that Python operation down, and run the compute in the
same place
as the data, netting better performance and less data transfer.
📈 Bonus: infinite-scale charts
Historically Hex, like many visualization products, had limits to the number of points that could be rendered in charts, because web browsers tend to fail when you try and render too much data.
Today, we're upgrading our charts to use server-side acceleration and aggregation, so they can handle data at any scale.
3
You can pass a dataframe of any size into a chart cell and aggregate it for display right from the chart configuration. Here's an example using a 900k row dataset:
⏩ Notebooks, meet the modern data stack
“Modern data stack” can be an ill-defined buzzphrase, but to me the simplest definition is “a set of tools that assume modern data warehouses”, and the most profound consequence of this is the ability to work with much larger scale data than was previously possible.
With these new features in Hex, we’re bringing notebook workflows to the Modern Data Stack™, and enabling data practitioners to ask and answer questions of all of their data.
↩
Some of you might think of this like a “predicate pushdown”
↩
Under the hood, we're using
VegaFusion
to power this!
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.

If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨ Get started for free
👩‍💻 Open roles
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
