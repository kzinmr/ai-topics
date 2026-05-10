---
title: "Getting the most out of dbt docs | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/getting-the-most-out-of-dbt-docs/"
scraped: "2026-05-10T01:28:56.400959+00:00"
lastmod: "2022-08-03"
type: "sitemap"
---

# Getting the most out of dbt docs | Hex 

**Source**: [https://hex.tech/blog/getting-the-most-out-of-dbt-docs/](https://hex.tech/blog/getting-the-most-out-of-dbt-docs/)

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
Getting the most out of dbt docs
Bringing all the power of dbt’s documentation site, straight into Hex
Claire Carroll
Product
August 3, 2022
Share:
twitter
linkedin
In this article
All your dbt descriptions, where you’re actually working
Finding value in data documentation
Get started for free
knowledge
TLDR:
Hex now surfaces descriptions from a dbt Cloud project directly in the database schema browser in Hex. Read on to learn a bit about why we built this and our thoughts on writing valuable docs, or head straight to
our docs
to set up the integration.
You’re a good data analyst — a great one, even. You transform your data with dbt, and take the time to come up with clear and understandable names for your columns and tables. When you discovered the in-built
dbt docs site
, your mind was blown, and since then, you’ve spent hours documenting your sources and models, crafting beautiful descriptions for the columns and tables your team use in analyses.
You deploy the dbt docs site at a URL that everyone on your team can access, and even run data onboarding sessions to train people, showing them how to find the definition of a column without ever needing to ask for help. If anyone on your team wants to know what a column means, the information is right there, in the docs.
So why do you still get messages like this?!?
This isn’t some fable I’ve constructed for the sake of a blog post: this was actually happening internally at Hex. No matter how much effort our incredible data team put in to their data docs, people were still pinging them asking what various columns and tables meant.
And honestly — I don’t blame them! Asking users to visit a separate docs site to open a new tab, remember a login, and navigate a UI to get the answer to their question is too much friction, especially when they can
cmd + tab
to another app and send you a message in a fraction of the time.
So, rather than try to lead our team members to the docs, we decided to
bring the docs straight to them
.
All your dbt descriptions, where you’re actually working
With the latest set of improvements to our dbt integration, model, source, and column descriptions are now surfaced directly in the database schema browser in Hex.
Alongside the docs, Hex also shows what tests are on each column, and the status of those tests. And if your users do want to see more context, there’s a handy, in-line link that will take them directly to the dbt docs site.
The Hex schema browser, complete with dbt documentation
We turned this feature on for our internal dbt docs a couple of months ago, and its impact was immediate. Gone were the messages about what a column meant, and in their place were compliments on how well our data was documented.
Now that’s a Slack message I like to see!
The
missing piece all along was bringing docs into the UI people were actually using
.
Finding value in data documentation
This story had a happy ending, but not all stories of data documentation efforts do. I’m a huge fan of dbt, and the inbuilt docs site. Back in 2018, when I first saw an early prototype of the documentation, I was using a poorly-maintained spreadsheet for my data definitions. The docs site blew my mind: being able to write descriptions in the same repo, and as part of the same process as my data transformations, and then have a documentation site automatically generated for me was a game-changer. I envisioned a future where everyone in the org would use the docs site to understand how to use the datasets I was creating.
Since then I’ve seen countless data teams go through the same thing, whether it’s with dbt docs, or another data documentation tool — they invest hours writing definitions in the hopes that they’ll empower downstream users to discover and understand datasets; after all, that’s what these tools are promising. But most docs solutions don’t live up to this promise, and a lot of the effort of data teams is wasted.
I’m not saying data documentation isn’t valuable — there
is
value in writing descriptions to explain that complicated column, in understanding the lineage of data, and even in seeing where data is consumed. It’s just that most of this value today isn’t realized by the data consumer, it’s realized by the team producing the datasets.
We never really got to the Utopia these tools promised. If we do truly want to empower the consumers of our data to understand and discover datasets, we have to bring this metadata to the tools that our data consumers are using. The dbt docs integration in Hex is one part of that, and I’m excited to share more on this front as we continue to build Hex.
Share:
twitter
linkedin
Hex integrates with dbt to pull metadata on freshness and tests right into the flexible notebook environment where you're writing queries.
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
