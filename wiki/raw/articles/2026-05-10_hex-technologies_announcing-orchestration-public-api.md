---
title: "Announcing: Orchestration integrations and the Hex public API | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/announcing-orchestration-public-api/"
scraped: "2026-05-10T01:27:17.636611+00:00"
lastmod: "2022-09-22"
type: "sitemap"
---

# Announcing: Orchestration integrations and the Hex public API | Hex 

**Source**: [https://hex.tech/blog/announcing-orchestration-public-api/](https://hex.tech/blog/announcing-orchestration-public-api/)

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
Announcing: Orchestration integrations and the Hex public API
Trigger Hex apps right from Airflow and Dagster— or plug into the API and build something completely custom
Jared Lorince
Product
September 22, 2022
Share:
twitter
linkedin
In this article
Hex + Orchestration
Powered by Hex’s public API
Get building!
Get started for free
Today we’re launching two new capabilities for Hex:
First-class integrations with popular orchestration tools
Airflow
and
Dagster
A
public API
, allowing you to programmatically run Hex projects from other systems
Together, these are an incredibly customizable set of tools for integrating Hex into the rest of your stacks, workflows, and systems. We can’t wait to see where you take it!
Hex + Orchestration
While of course everyone thinks of Hex as the indispensable cornerstone of any data workflow, the reality is that we are but one piece in a larger stack. ETL,
reverse
ETL, custom internal services, model inference – all of these things get thrown in together, and need to work together seamlessly to provide high impact and great experiences to users.
This is why Orchestration tools like Airflow and Dagster exist. These tools let you build Directed Acyclic Graphs (or, DAGs), with nodes of jobs and dependencies that can run in scheduled, sequenced orders. This lets you, for instance, trigger a data transformation, and then a model inference run based on that data, and then update a visualization to show those outputs.
Historically, many people would also include legacy Python notebooks as part of DAGs, as a way to trigger logic or refresh outputs.
We've been hard at work
modernizing every piece of the notebook interface
, and now that extends to orchestration support as well: we’re announcing two new integrations with Hex for
Dagster
and
Airflow
. These enable you to add Hex projects to your DAGs (yes,
a DAG in your DAG
), programmatically triggering project runs.
This lets you do things like:
Trigger a Hex app to update cached values after an upstream transformation completes
Run a Hex project with passed-in input parameters based on a form submission in another app
Automatically kick off a model re-run through Hex when new source data lands
And, honestly, probably a million things we haven’t thought of, because you all are creative, crazy, beautiful people who continually blow our minds with what you do in Hex.
Note: this feature is available on
Hex Teams plans
and above.
Powered by Hex’s public API
These awesome integrations are both powered by our new public API. If you’re using another orchestration solution, or want to be able to do other kinds of automations with Hex, this new endpoint lets you run projects programmatically.
Here's a quick embedded demo of a Hex app that uses the Hex API to trigger a custom run of another app (which uses
another
powerful API,
The Cat API
).
Hex API Example
There are four endpoints in v1.0.0:
RunProject
,
GetRunStatus
,
CancelRun
, and
GetProjectRuns
. Like the orchestration integrations,
RunProject
can be used both to trigger runs that set the user-facing cache of an app, and to generate custom one-off runs with specific input parameters.
See the
full API docs here
for more information and examples.
Note: this feature is available on
Hex Teams plans
and above.
Get building!
We hope you’re as excited about these features as we are, and we can’t wait to see what you build with them. There's no demo too small or janky, and no integration proposal too outlandish— we want to hear about it all. Hit us up on
Twitter
or send an old fashioned email to
[email protected]
.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.

If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
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
