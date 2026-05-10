---
title: "Introducing Semantic Model Sync in Hex | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/introducing-semantic-model-sync/"
scraped: "2026-05-10T01:29:09.943390+00:00"
lastmod: "2025-03-05"
type: "sitemap"
---

# Introducing Semantic Model Sync in Hex | Hex 

**Source**: [https://hex.tech/blog/introducing-semantic-model-sync/](https://hex.tech/blog/introducing-semantic-model-sync/)

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
Introducing Semantic Model Sync in Hex
Governed metrics for trusted self-serve analytics
Barry McCardel
Product
March 5, 2025
Share:
twitter
linkedin
In this article
The fragmented state of semantic modeling
Our interoperable approach to semantic models in Hex
Getting started with Semantic Model Sync
Towards a more unified world for data teams
Get started for free
Today, we’re excited to launch the public beta of Semantic Model Sync for a faster, easier self-serve experience in Hex! You can connect semantic models from dbt MetricFlow and Cube to use pre-defined measures, dimensions, joins, and more.
Data teams are dealing with tough tradeoffs. They want to keep up with the infinite demand for insights in their organization, while making sure results are generated in an accurate and consistent way. They want flexible tools that don’t lock them into a vendor-specific spec, but also want a way to create governed metrics without having to redefine them every time.
This is a tricky situation — and it’s why we’ve taken a novel approach when it comes to semantic modeling in Hex,
with a focus on flexibility, interoperability, and openness.
As a next step, we’re introducing
Semantic Model Sync
, which lets you leverage trusted metrics and business logic from
dbt MetricFlow
and
Cube
. Measures, dimensions, and joins from your imported semantic models show up in Hex’s
Explore
experience, allowing stakeholders to self-serve governed concepts in an intuitive way.
Drag and drop measures and dimensions from your imported semantic models in Explore.
knowledge
Semantic Model Sync is available on
Team and Enterprise plans
.
The fragmented state of semantic modeling
If you’re not familiar, a semantic model is basically “instructions for use” for a given set of tables. How should you calculate measures based on the columns? What are valid joins and aggregations? Semantic models encode this up front, so everyone knows how to use the data correctly downstream.
This is an immensely useful concept especially for “self-serve” analytics, where you want a broader set of users in the organization to leverage data in a consistent, standardized way.
The current state of semantic modeling in the data stack, however, is a little weird.
On one hand, you have fully-laminated, locked-in modeling solutions integrated into BI tools like Looker. These are popular and effective, but leave you stuck defining vendor-specific logic that’s hard to reuse or repurpose. We knew early on that the
wrong
approach would be forcing everyone to re-define their logic in a closed, proprietary “HexML” format.
On the other hand, there are standalone modeling solutions like dbt MetricFlow or Cube. These are both powerful and expressive specs that are still developing compatibility ecosystems — and not every team wants to pay for another cloud service to host them.
What we’ve seen and heard is that data teams are stuck between a rock and a hard place, trying to figure out how to bring semantic modeling into their organizations without getting locked into a path they’ll regret.
Enter Semantic Model Sync!
Development and deployment is so speedy. Seeing my semantic model changes immediately rendered in Hex was a joy.
Peter Ray
— Data Engineer, Notion
Our interoperable approach to semantic models in Hex
Today, we’re allowing data teams to have the best of both worlds: an integrated, first-class experience for leveraging semantic models, without compromising the flexibility of ad hoc analysis or getting locked into a proprietary spec.
Semantic models in Hex persistently sync datasets, measures, dimensions, and joins from popular third-party semantic models. This allows users to do analyses based on these governed concepts in Explore.
knowledge
Check out our
guide on data curation
for a better self-serve experience in Explore.
Now, data teams can model what’s needed without getting boxed in. When you want to go off-road, the
Hex notebook
is built for agile exploratory data analysis. No need to submit a pull request to answer a one-off question or crank out LookML code for single-use logic.
Hex made setting up a connection to MetricFlow a breeze! The intuitive UI empowers our stakeholders to perform self-serve analysis.
Mercedes Wu
— Data Scientist at Weights & Biases
Getting started with Semantic Model Sync
In three steps, Admins can set up a sync via GitHub, and Hex will directly parse the underlying semantic code without needing to go through a third-party API.
Add a new model on the
Settings
page by specifying the data connection and generating a new API token.
In your GitHub repository where your semantic model files live, add the API token, create a new folder, and paste in the script provided by Hex.
Every time you merge new code, it will automatically trigger a GitHub action that sends the contents of your repository to Hex. (Behind the scenes, Hex reads your files and translates the specs into measures, dimensions, and joins.)
Once the integration is complete, you can browse the datasets in your model and quickly jump into Explore to visually analyze your data using measures and dimensions. Hex discovers joinable datasets automatically, and we also built error-free, fan-out tolerant aggregations, so you do less modeling work and get consistently accurate results.
Traditionally, measures, dimensions, and joins have only been accessible to BI users, but these pre-defined units of logic can also cut repetitive work for data teams. With semantic models in Hex, you can use semantically-enriched
Explore cells
in notebooks, and
chain them
into SQL and Python cells.
Want to dive in today? Get started with our
S
emantic Model Sync documentation
.
Towards a more unified world for data teams
At Hex, we’re on a mission to bring together
fragmented data workflows
. To us, this means helping organizations consolidate tooling, but it also means interoperability and allowing you to
leverage your semantic models no matter where they’re defined
.
We believe the biggest challenges facing data teams today can’t be fixed by superficial changes in UI or UX. Our platform’s unique atomic building blocks — cells, dataframes, and DAGs — imbue flexibility and modularity into everything we build, including our semantic models.
Whether you’re looking for an all-in-one platform to combat tool sprawl or a powerful data science notebook that integrates with your semantic layer, Hex is built differently, so you can work differently.
Share:
twitter
linkedin
New to Hex and want to try Explore enriched with semantic models?
Request a demo
Learn about Explore
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
