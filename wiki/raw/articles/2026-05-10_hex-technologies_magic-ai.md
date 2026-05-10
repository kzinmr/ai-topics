---
title: "Data is better with a little magic | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/magic-ai/"
scraped: "2026-05-10T01:29:27.600382+00:00"
lastmod: "2024-03-21"
type: "sitemap"
---

# Data is better with a little magic | Hex 

**Source**: [https://hex.tech/blog/magic-ai/](https://hex.tech/blog/magic-ai/)

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
Data is better with a little magic
New updates to Hex’s AI tools for data analysis
Olivia Koshy
Product
March 21, 2024
Share:
twitter
linkedin
In this article
What’s new
Limitations of AI
Take it for a spin
Get started for free
Today we’re introducing some updates to our Magic AI assistant that make it more powerful, intuitive, and faster.
We built our Magic AI tools to help
humans
do their data work— writing queries, futzing with Python code, digging up answers— faster and with more confidence. Our goal is to augment, not replace, human insight. This is
not
an "AI data analyst", because honestly, we don’t really think that should be a thing.
The first version of these tools has been available for almost a year now, and we’re excited about how useful it's been for our users. Thousands of people each week are using Magic to get more done with data: editing complex SQL queries, debugging confusing Python code, and speeding up the most tedious parts of their jobs (
cough
pandas
cough
regex).
Scott Chacon, Github cofounder
Early users are telling us that it “shaves hours off their analytical workflows”, they “don’t have to circle back after meetings anymore, because Hex can help get answers before the end of a call”, and that their “keyboard life is being extended by years from the saved keystrokes.”
Today, we’re introducing a big upgrade that makes Hex’s AI tools even more helpful, updates and polishes the UX, and introduces some powerful new functionality.
If you'd rather watch a video than read a blog post, here's a summary of the new features. Otherwise, read on.
What’s new
Magic is getting three major upgrades. Of course, we’ve also been making lots of speed and accuracy improvements along the way, so that your AI generations are both faster and smarter! But here's the big stuff:
Generate mode
Magic can now generate multiple cells at a time in your notebook, chaining together SQL, Python, and Chart cells to answer complex questions or kickstart a new analysis.
It’s easy to generate new cells from anywhere in a project: just hit
Cmd+G
, use
↓
from an edit mode prompt bar, or click the “Add with Magic” button between cells.
For example, you can get started quickly in a new project without having to forage for initial data:
Notice that Magic cleverly maps “Appetizers” to “Quick Bites” in the WHERE clause, thanks to rich metadata and dbt context.
Or generate new cells in the middle of an existing project to help with complex questions or new directions:
Hex’s cell-based UI really shines here! This upgrade lets Magic work in your notebook just like you would, using multiple cells to run queries, build charts, and iteratively construct complex logic. New cells are all created as drafts, so you can inspect, edit, and validate AI generated code before accepting it. Once accepted, the new cells seamlessly integrate into the notebook flow.
More powerful, streamlined prompting
To support new cell generation and more complex instructions, we’ve rebuilt the prompt bar, unifying all Magic actions into one simple interface. You can activate it on a cell with
Cmd+Shift+M
, and seamlessly switch between editing existing cells or generating new cells with the
↑
and
↓
keys.
The new design also supports more complex multi-line instructions and gives more power to auto-fixes. You can choose to auto-fix a problem with one click, or use the prompt bar and provide specific direction to guide a fix. I like to use this to both fix
and
edit a query in the same step!
Auto-fix can run with or without additional instructions. Here we provide specific guidance.
Mentioning data
The prompt bar now supports "@ mentioning" datasets to specify what resources it should use. This is a simple addition, with a huge impact on prompting efficiency and accuracy.
This example uses warehouse tables, but you can also mention dataframes.
You can use this to point at a specific database table (handy if you're off-roading and using some unusual, undocumented resources) or if you're in a complex project, to direct Hex towards a particular dataframe.
One you get into the routine of @'ing datasets, you'll wonder how you lived without it. And it will have a huge impact on the accuracy and quality of your generated code, so you're well incentivized to remember.
Improved SQL generation
Over the last few months, we’ve put in a ton of work on our state-of-the-art metadata retrieval pipelines, and seen steady improvement in Hex’s ability to accurately generate accurate SQL queries.
One important note is that no matter how good the models, or our prompt engineering around them,
context is critical!
The more metadata you can provide about your tables and columns, the better Hex can effectively prompt the model and maximize completion quality.
You can do this in three main ways:
dbt Docs:
if you’re using dbt Cloud, all you have to do is update the metadata in your models, and
it’ll automatically flow into Hex
and be used to help inform query generation.
Support for warehouse metadata:
ditto if you update information about your columns and tables in Snowflake, BigQuery, or Redshift.
via Hex’s
built-in Data Manager
, which lets you edit additional metadata as well as promote or exclude schemas and tables.
An overview of adding custom metadata in the Data Browser. Note the already present details automatically synced from dbt.
Limitations of AI
Amongst all the hype about what AI can do, it’s worth taking a moment to acknowledge the current state of LLMs and tools built around them.
Working with AI tools can be funny – they blow your mind one moment, and then the next you're shaking your head, wondering how they could possibly be so silly.
So, as we build and iterate on Hex's AI features, our north star has always been "are people finding this useful?" Our big target isn't 100% code perfection (though we're getting better all the time), and it's
certainly
not the construction of some “AI analyst” that replaces people. It's about being simple, useful, and solving the real problems data practitioners face every day.
But make no mistake – it’s not perfect, and definitely not a replacement for human judgement.
Take it for a spin
Magic AI is available for all Hex customers, including those on our community plan or in active trials. Community users are limited to 100 monthly requests per user.
Got some privacy and security questions? The important stuff: neither Hex or our model partners train models on customer data, and all metadata is stored in a secure vector database running inside Hex’s architecture. If you have other questions, you can l
earn more in our documentation.
Ready to try it out?
Click here
to jump directly into a project and see it in action.
Share:
twitter
linkedin
Want to give Hex a spin? Click below to create a free forever Hex account. Or, check out our open roles, and come join us building the future of data.
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
