---
title: "Introducing: Components | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/introducing-components/"
scraped: "2026-05-10T01:29:32.616088+00:00"
lastmod: "2023-01-04"
type: "sitemap"
---

# Introducing: Components | Hex 

**Source**: [https://hex.tech/blog/introducing-components/](https://hex.tech/blog/introducing-components/)

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
Introducing: Components
Stop repeating yourself repeating yourself reaepting yuroslef rpaetnig ouylefs
Tom Santinelli
Product
January 4, 2023
Share:
twitter
linkedin
In this article
Don’t repeat yourself!
Meet components
Creating components
Get started with components today
Get started for free
Today we’re launching an exciting new way to build and collaborate in Hex:
Components
.
Components are groups of cells your team can write once and re-use across projects. They make data work more consistent, efficient, and less error-prone. They also make it easier for users of all technicality levels to take advantage of logic written by experts. It's a huge upgrade to how teams work together and collaborate in Hex!
Check out a quick demo here, or read more below:
Don’t repeat yourself!
If you’re anything like us, you’ve probably thought
“haven’t I seen this before?”
… or worse,
“haven’t I
done
this before??”
as you have worked on a data project. Teams everywhere rewrite the same queries and code over and over, leading to rework, variation, and error.
There are some existing - but limited - ways to get around this. Factoring code out into shared Git repos (
already supported in Hex!
) is great for stuff like shared utility functions, but not for SQL. Metrics stores like
dbt Semantic Layer
,
MetricFlow
, and
Cube
(
already supported in Hex!
) are helpful for query-like calculations, but are not useful for Python code or other elements, like visualizations or no-code cells. Shared docs with code that you copy-and-paste out is… well, that’s not really a solution, but I know many of us have resorted to this.
All-in-all, this re-work is a staple of many data workflows, and a pain point that we heard about all the time from our customers.
Meet components
So, we built Components: a new feature that empowers teams to operate with better collaboration and consistency.
Components are reusable groups of cells, and bring the
DRY
model from software development to analytics. Editors can easily publish new components, and import existing ones into projects. Changes to a component can be made once, and then propagate down into projects that rely on it.
Over time, your team can build up a centralized repository of consistent, usable logic, and empower others to do great things with data.
Creating components
You can easily promote any group of cells in a project to be a component. Simply use the (new!) multi-select feature to select a chunk of logic, and select “Create Component” at the bottom. You’ll be able to set some metadata, publish your new component, and replace the existing cells with the new component.
Create a component from cells in any existing project
Like Projects, Components can also be created from the new Components view, either from scratch or through copy-pasting groups of cells in.
Using components
It’s fast and easy to browse for available components and add them to a project:
Browse published components and add to your project
Hex’s reactive compute engine automatically picks out the defined variables in the component, and makes them available for reference in downstream cells.
If a change is made to the component source, Hex will indicate that an update is available, and you can quickly view the diff and pull a new version:
View changes and update components to keep projects in sync
Need to make project-specific changes to your component? No problem - you can opt to import a component as detached cells, or later “eject” cells from an already-imported component:
Get started with components today
Components are now available on all paid plans of Hex. Users on Pro can share up to 3 components with their workspace, with Teams and Enterprise allowing for unlimited shared components.
And, if you’re not using Hex yet, you can start a free-forever account
here
.
Share:
twitter
linkedin
Welcome to the bottom of the post! You made it. Click below to get started, or to join our team and help us make Hex even more magical.
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
