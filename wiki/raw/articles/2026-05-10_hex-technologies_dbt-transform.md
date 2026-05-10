---
title: "Metrics layers: past, present, future | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/dbt-transform/"
scraped: "2026-05-10T01:28:59.503100+00:00"
lastmod: "2023-02-08"
type: "sitemap"
---

# Metrics layers: past, present, future | Hex 

**Source**: [https://hex.tech/blog/dbt-transform/](https://hex.tech/blog/dbt-transform/)

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
Metrics layers: past, present, future
Why dbt Labs’ acquisition of Transform is great for data stacks
Claire Carroll
Data
February 8, 2023
Share:
twitter
linkedin
In this article
The past: the metrics mess
2021: dbt entering the metrics-space
2023: Where are they now?
The future: the dbt + Transform announcement
Get started for free
News broke today that
dbt Labs has signed a definitive agreement to acquire Transform Data
. What does this move mean? What does this tell us about where the data stack is going? And is it a good outcome for both teams?
Spoiler: I
1
think it's a great move — to understand why, we have to start with some background.
The past: the metrics mess
Long before any of us were actually working in data, back in the age of
OLAP hypercubes
, a data team would use a single, on-premises software solution to extract, transform, load, and analyze their data.
This all changed around 2010, when
data teams started adopting what we refer to now as the Modern Data Stack™.
Data from source systems were loaded into warehouses like Redshift (and later BigQuery and Snowflake) via tools like Stitch and Fivetran.
At first, this raw data was consumed directly by BI tools. But often, the data wasn’t quite yet usable to a business user – it needed to be cleaned up (or…
transformed
) to accurately represent a business. And there needed to be a way for users who didn’t know SQL to fetch the data from the warehouse.
Some BI tools unlocked these workflows with a no-code GUI. Others relied on users learning SQL. Looker took a different approach, with their “LookML” language. In this language, data teams could define:
Which tables
may
be consumed by an end user (is this business-user ready data?)
How these tables relate to each other (what are valid joins?)
Valid operations to perform on these columns (e.g., aggregations, date truncations)
And…
the transformations that were required to clean up, a company’s data
Armed with this information, a business user could issue a request for a dataset (“give me revenue by country”, “I want all the customers who have ordered 10 products in the last month”) in their data tool of choice. This request gets compiled to the correct SQL, is executed against the warehouse, and the dataset is returned to the business user. This opens up analytical workflows to a much broader population of users, since it removes the need to know SQL,
and
ensures everyone is calculating numbers the same way.
LookML was, in many ways, the first metrics layer. But it was tightly coupled with Looker itself — as soon as you wanted to do an analysis outside of Looker, you might struggle to make your numbers match.
Around 2016, dbt hit the scene.
Born from a simple idea, dbt allows data teams to build complex transformations in pure SQL, right in their data warehouse, and outside of their BI tool. As dbt gained popularity, analysts started to
wonder
what should exist in the transformation layer, versus the consumption layer.
While more business logic started shifting to the transformation layer, dbt didn’t fully solve the metric definition problem. It was good at creating
models
– tables of data – but didn’t have any facility for defining how this data should be aggregated, joined, or understood. As such, it was possible to have everything beautifully modeled in dbt, but still end up with mismatched numbers — one analyst might be calculating weekly revenue based on UTC weeks, another in PT, while another might forget to add a where clause to filter out canceled orders.
It started to feel like having the tables in the warehouse, ready for consumption, wasn’t the full solution.
We also needed a way to define
how
to consume these tables.
The solution: a standalone
metrics layer
(or, later, “semantic” layer), that would live on top of dbt, and integrate with every BI tool, providing this much-needed standardization and opening up data workflows to more users.
The metrics layer concept took hold of the data zeitgeist —
everyone
was
writing
about
them. To some, this felt like a glaring gap, and startups came along to fill it –
Transform
,
Cube
,
Supergrain
(since pivoted!), and others.
While the idea of a metrics layer seemed to resonate,
the category seemed stuck in a chicken-and-egg situation.
To gain adoption, metrics layers needed frontend analytics products to build compelling, first-class integrations. But the analytics products (including us!) wanted to see a lot of adoption for it to be interesting to build integrations. It was hard to jump-start this.
2021: dbt entering the metrics-space
And then, in October 2021 dbt declared its intent to enter the metrics layer space via a GitHub
issue
titled “dbt should know about metrics.” It’s a doozy: everyone, and his
2
coworker, feels the need to have their say on it.
Was this a good move for dbt?
In one sense, no – they were in the midst of
keeping up with some crushing scaling issues
(a good problem!) and a complete UI redesign, so taking on a new, ambitious engineering project like this was… a lot.
In another sense, however, yes!
It makes a lot of sense that a single codebase should define both data models,
and
encode the instructions on how to consume those models.
After all, on teams using a metrics layer (like LookML or Transform’s metrics layer), it’s often the same person developing dbt models as writing metric definitions. Jumping to another tool – especially a standalone BI tool – to do this doesn’t really make sense. Changes to the underlying data structure will
certainly
affect the metric definition – should we really make you command-tab to another window, and open a separate PR, to do that?
And, if metrics are defined at the transformation layer, it means
all downstream tools
3
can consume the same definitions
, rather than requiring teams redefine the logic in multiple, separate places.
Finally, this move also made sense for the shareholders of dbt Labs – if a metrics layer was valuable to the tens of thousands of companies using dbt Core,
those users would become dbt Cloud customers,
since the architecture to compile metric requests to datasets would rely on a hosted product (a dbt Server), which would be part of the dbt Cloud offering.
2023: Where are they now?
Fast forward to today.
dbt has made progress on their Semantic Layer,
releasing it publicly last year
, and
steadily introducing additional features
. But dbt has a lot of other things they’re focused on – scale, reliability, enterprise – and building out a best-in-class metrics layer was clearly a strain. Their metrics layer doesn’t yet support joins, or non-Snowflake warehouses, and is missing significant API surface area.
But, what dbt
do
have (which other solutions lacked) is
distribution
– thousands of teams that rely on it to process their data every day. Even though their metrics layer is fairly nascent, the idea of this being integrated into dbt is clearly appealing, and was apparently enough to make it tough sledding for other metrics startups.
Over at Transform, they have something great: an
open-source
, feature-mature MetricFlow, a hosted server for compiling metric requests, and a UI for exploring metrics. The team has shipped quickly, and built a lot of tech in a short period of time, including
a more expressive metrics spec that encodes joins
, a server that works with
most warehouses
, and
a performant caching layer
.
Their API interfaces include a CLI, SQL, GraphQL, and a Python package
. It’s
very
complete – and would have taken dbt a while to get to.
But it seemed like they remained in that chicken-and-egg loop. Indeed, this led Transform to decide the best way to break this cycle was to
build the frontend
themselves, basically pivoting to BI, as a way to make adoption of the metrics layer tangibly useful. Even so, it didn’t seem they have been able to build the kind of distribution they’d need to make a standalone MetricFlow a critical piece of the modern data stack.
The future: the dbt + Transform announcement
So, it’s pretty simple:
the best product, pairing with the best distribution.
It makes a
ton of sense
for metrics to live at the transformation layer, and by joining forces with Transform, dbt can accelerate that journey. MetricFlow can serve as a strong foundation for metrics in the modern data stack, on top of dbt’s dominant distribution.
So, yeah we think this is great for everyone! We are super happy to see them joining forces. Congratulations all around 🎉 📈
↩
Some disclaimers: I used to work for dbt Labs, and own stock in the company. It’s in my personal interest to see dbt Labs succeed. 2. I’m also personal friends with folks on both teams. 3. I’m now a PM at
Hex
, a product that has integrations with Transform
and
with dbt.
So, I’m biased as heck.
↩
Literally
his
! Apparently only men replied to this issue? As the saying goes: “Men will literally reply to an open source GitHub issue instead of going to therapy”
↩
Including Hex!
–
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
