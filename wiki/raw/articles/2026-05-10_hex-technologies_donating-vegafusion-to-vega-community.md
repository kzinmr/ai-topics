---
title: "Donating VegaFusion to the Vega community | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/donating-vegafusion-to-vega-community/"
scraped: "2026-05-10T01:29:39.847330+00:00"
lastmod: "2024-07-11"
type: "sitemap"
---

# Donating VegaFusion to the Vega community | Hex 

**Source**: [https://hex.tech/blog/donating-vegafusion-to-vega-community/](https://hex.tech/blog/donating-vegafusion-to-vega-community/)

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
Donating VegaFusion to the Vega community
We’re still supporting VegaFusion, but you can now find it under the official Vega umbrella
Caitlin Colgrove
Product
July 11, 2024
Share:
twitter
linkedin
In this article
Why VegaFusion?
The future of the project
Get started for free
We’re excited to announce that we are donating the
VegaFusion
project back to the Vega community, maintaining the BSD-3 license we added after acquiring the project in 2022. We will continue to support development and maintenance of VegaFusion, and hope that this new official home makes it the first choice for Vega developers looking to add server-side acceleration to their charts.
Why VegaFusion?
At Hex, we’ve always relied on the Vega ecosystem to power our visualizations and keep those eternally cookie-hungry viz mice well fed. Build nice legends? Easy. Make them 50% opacity and float inside the top left of the chart? Sure! Our charts are all
Vega-Lite
under the hood, which supports a
dizzying
array
of
config
options
and lets Hex users make beautiful, interactive visualizations with just a couple of clicks.
knowledge
🧠 Want to nerd out about using LLMs to generate accurate Vega-Lite charts? Read our recent blog “
Making AI Charts go brrrr
”.
But one long-standing problem that Vega doesn’t solve out of the box is
data
scale.
You might have bumped into error messages before in tools that warned you about charting more than 5,000 rows, or 10,000, or some other arbitrary but relatively small limit.
This limitation is really an architecture problem, not a viz library problem. Interactive visualizations need to run on the frontend, which means computation happens
in your browser,
on your computer. And no matter how performant and beautiful the Vega codebase might be, your little browser will always start to sweat if you load millions of rows of data into memory. It’s just not designed for that! Cue fans whirring, pages glitching, and the spinny beachball of death.
But sometimes — actually, a lot of times!— you really need to work with more than 5,000 rows of data.
So when we saw
VegaFusion
, which seamlessly integrates with Vega to push aggregation to the
backend
while still allowing for frontend interactivity, we jumped at the chance to integrate it into Hex. We wound up liking it so much that we brought
Jon Mease
and the VegaFusion project directly onto the team to invest in the project, and incorporate it deeply into the Hex viz architecture.
Thanks to VegaFusion, Hex charts can now push aggregation to the backend, letting users visually explore data of any size. The interactive chart below showing month-aggregated bike trip counts is being computed over 20 million rows of raw data:
Hex chart plotting 20M rows
The future of the project
Over the past two years of stewardship, we’ve contributed a ton of new VegaFusion features, from:
Supporting many additional Vega transforms including stack, pivot, and impute.
Support for faceted charts.
Most importantly, we've integrated VegaFusion as an optional dependency into
Vega-Altair
itself. VegaFusion is now the
recommended
approach to scaling Vega-Altair charts to large datasets.
We feel great about the state of the project now, and are excited to donate it back to the Vega community along with the new BSD-3 open source license we’ve been using. You can now find
VegaFusion over in the Vega Github organization
!
Jon will continue to be a maintainer of the project, so we’re still dedicated to supporting and growing VegaFusion. This change just means more people will have access to the tools they need to build highly scalable and beautiful visualizations.
We can’t wait to see what you build 😄.
Share:
twitter
linkedin
If you made it this far, and are interested in working on stuff like this, drop us a line at
[email protected]
— we would love to hear from you.
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
