---
title: "Introducing VegaFusion 1.0: now a Hex OSS project | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/vegafusion/"
scraped: "2026-05-10T01:29:01.233860+00:00"
lastmod: "2023-01-24"
type: "sitemap"
---

# Introducing VegaFusion 1.0: now a Hex OSS project | Hex 

**Source**: [https://hex.tech/blog/vegafusion/](https://hex.tech/blog/vegafusion/)

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
Introducing VegaFusion 1.0: now a Hex OSS project
Infinitely scalable data visualization, with a more permissive license
Caitlin Colgrove
Data
January 24, 2023
Share:
twitter
linkedin
In this article
Enter: VegaFusion
VegaFusion is joining Hex!
Announcing VegaFusion 1.0
Re-licensing for fun
Get started for free
Building great visualization products is hard.
The first obvious challenge is the UI. Building an intuitive, yet flexible, interface for visualization isn’t as easy as slapping a frontend on a plotting library. At Hex, we actually just
completely re-built our chart cell
, because our first attempt wasn’t cutting it.
Even
harder
, however, is getting the backend right. There are two basic ways to approach this:
Static visualization libraries like
Matplotlib
,
Seaborn
, or
GGPlot
render charts on the server side, and display them as static images. This means they can render large-scale data, but the outputs aren’t interactive.
Interactive visualization libraries, like
Vega
,
Plotly
, and
Bokeh
send all of the data points to the local client (i.e., the user’s computer), where the chart is then rendered using JavaScript. These outputs can be richly interactive, but are constrained by the memory of the client: if you try to visualize data tables over a few thousand rows, your browser is likely to slow down or crash.
This presents a difficult tradeoff between scale and interactivity. If you want things like tooltips, zooming, and drill-down, you are limited to only a few thousand points. If you want massive data scale, you’re limited to boring .png files.
Enter: VegaFusion
But what if you didn’t have to decide between interactivity and scale? In the words of
the immortal Taco Bell commercial
, “¿por que no los dos?”
This is the magic of
VegaFusion
.
It allows interactive data visualizations to work at much, much higher scale.
VegaFusion accomplishes this by pushing the aggregation for charts down to server-side operations, allowing operations on large datasets while also minimizing the amount of data pushed to the client, and still enabling full frontend interactivity.
We have long been fans and users of
Vega-Lite
– a powerful, high-level visualization grammar – and built our original chart cell around it. So
when VegaFusion first came on the scene
, we quickly incorporated it into the product, and were thrilled with the results. When you use a Chart Cell in Hex, you don’t have to worry about the scale –
just pick a dataframe, build a chart, and it will Just Work™, even if it’s millions of rows.
Here’s an example of rendering a 1,000,000 point dataset:
VegaFusion is joining Hex!
As we got deeper with the VegaFusion technology - and started working with
Jon Mease
, the human behind it - we realized that the best way to scale our contributions would be incorporating both of them into our team.
Today, we’re announcing that VegaFusion is now part of Hex,
and the project is becoming a Hex open source project. Jon has joined us full-time to lead our data visualization architecture, and continue his contributions to the Vega ecosystem.
Announcing VegaFusion 1.0
We’re
also
thrilled to share the
first major version of VegaFusion: 1.0
. This brings much of the work we did to back our new interactive chart editor into VegaFusion core, including better support for
Altair
– the VegaLite bindings for Python.
Now, it’s possible for Altair users – whether in Hex, or other notebooks like Jupyter – to take advantage of VegaFusion to automatically pre-evaluate and optimize their charts, all without requiring a clunky Jupyter Widget extension.
It also contains a ton of other great stuff, and lays the foundation for what’s next – including aggregate pushdown to SQL!
Re-licensing for fun
As part of this, we’re re-licensing VegaFusion to be much more permissive (to BSD-3 from AGPL). Our hope is that this will spur creativity and unlock the power of VegaFusion for others in the community (yes, including competitors 😄).
We’d love to see everyone who is interested join
the community
, and consider contributing to the project. There’s tons to do!
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
