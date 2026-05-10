---
title: "An all-new, interactive visualization experience for Hex | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/new-chart-cells/"
scraped: "2026-05-10T01:29:10.684135+00:00"
lastmod: "2022-12-15"
type: "sitemap"
---

# An all-new, interactive visualization experience for Hex | Hex 

**Source**: [https://hex.tech/blog/new-chart-cells/](https://hex.tech/blog/new-chart-cells/)

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
Introducing: an all-new, interactive visualization experience for Hex
Point-and-click visual filtering, an all-new chart cell, custom color palettes, and more
Claire Carroll
Product
December 15, 2022
Share:
twitter
linkedin
In this article
Interactive visual filtering
… built on top of a new, intuitive UI for editors
… and styled with your brand colors.
...powered by the Vega ecosystem
Get started for free
Charting is one of - if not
the
- most important part of the analytics workflow. Humans are visual creatures, and a well-built chart can make the difference between confusion and comprehension.
Building beautiful charts, however, can be challenging, especially in code-based environments like notebooks, where the only option is to write verbose Python code. Building charts this way can feel clunky, and is inaccessible to many data practitioners.
Our
original chart cell
in Hex made this workflow far more accessible, providing a point-and-click way to construct visualizations, and has been used by thousands of users to bring data to life.
Today we’re taking this experience further, introducing three big steps forward:
interactive visual filtering, an all-new editor UI, and custom color palettes.
Interactive visual filtering
Let’s say you have built a report in Hex with some charts, and want to allow users to filter down to specific time frames and see just those records. Previously, you’d have to wire up input parameters for start and end times, reference them in a SQL, filter, or code cell, and then into a new display table. It’s a pretty tedious workflow, both for creators and consumers, who really just want to point-and-click on the data that looks interesting.
Enter: visual filtering. Now, Hex chart cells allow users to to select datapoints of interest, creating new filtered sets of results.
On the editor side: each cell returns a dataframe, just like our
no-code Filter cells
. The dataframe is responsive to chart selections — click and drag across a range of values, individually select columns of interest, or interact with the legend to filter the data. This turns charts into a tool for interactive, visual exploration: you can display the resulting records in a table, or further slice-and-dice them in another visualization.
Interact with the chart and use the filtered data downstream
Visual filtering shines in app mode, allowing end-users to directly interact with reports, dashboards, or tools you publish in Hex. This can completely replace complex workflows with multiple input parameters and filter steps. Just point, click, and go.
Filtering a dashboard using charts
… built on top of a new, intuitive UI for editors
Part of the magic of Hex is that things Just Work — the UI should feel intuitive, yet extensible.
Unfortunately, our old chart cell didn’t live up to this promise. It let users create basic charts without writing code, but often required a lot of configuration to get the visualization you wanted. Some basic plots, like a grouped column chart or a histogram, were way more frustrating to build than they should have been.
Our new chart cell is a complete, from-scratch rebuild.
In every part of the UI, we’ve strived to provide an intuitive interface, and sensible default behaviors. It’s easier than ever to build the chart you want, with fewer clicks.
The new chart cell also provides finer-grained styling options, letting user configure specific colors for each series, switch the order of these series, and customize the axes, legends, gridlines and tooltips to make things feel polished.
We could tell you more about it, but honestly you should just try it and see for yourself.
… and styled with your brand colors.
And finally, one of our most-requested features: custom color palettes. Admins can configure a color palette that gets picked up by our new chart cells, creating on-brand charts by default.
...powered by the Vega ecosystem
We did keep one thing from our old chart cell: it's backed by
Vega-Lite
, which has provided us flexible, beautiful building blocks for visualization.
Behind the scenes, we're also using
VegaFusion
to power orders-of-magnitude larger data scale for visualization. By generating the aggregated data server-side, we avoid client-side rendering limitations, and allow users to plot near-infinite size dataframes in Hex. We're looking forward to sharing more about how we're doing this - and where we're taking it next! - soon.
We can't wait to see all the beautiful visualizations you build with this. May your charts be ever up and to the right 📈!
Share:
twitter
linkedin
Wow you made it all the way to the end? You must really be into this stuff. Click below to get started, or to join our team and help us make Hex even more magic.
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
