---
title: "Exploring one question with three workflows  | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/one-business-question-three-analytics-workflows/"
scraped: "2026-05-10T01:29:13.446908+00:00"
lastmod: "2024-09-03"
type: "sitemap"
---

# Exploring one question with three workflows  | Hex 

**Source**: [https://hex.tech/blog/one-business-question-three-analytics-workflows/](https://hex.tech/blog/one-business-question-three-analytics-workflows/)

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
Multi-modal in action: Exploring one question with three workflows
With a multi-modal analytics tool, there's less friction and more possibility.
Izzy Miller
Product
September 3, 2024
Share:
twitter
linkedin
In this article
The question
Workflow one: SQL-first
Workflow two: No code
Workflow three: Hybrid
Multi-modal accelerates the efficiency of data teams
Get started for free
Data teams shouldn’t have to switch tools in the middle of an analysis to get their work done and discover actionable insights. But they do —
all
the time. This quote from Jordan East at Workrise sums up this common reality quite well:
Some analysts preferred writing Python and some preferred SQL. And for each language, analysts would use different tools. After exploratory work, you had to prepare a finished data set and then recreate the visuals in the visualization tool.
— Jordan East, Senior Data Manager at Workrise
The problem is that most data tools enforce just one specific workflow or language — one
modality
— of working with data.
Prefer SQL, but your team works in notebooks? That’s a bummer. You’re a Python whiz, but the entire team is standardized on spreadsheets? It’s going to be tough to create efficient workflows that involve code.
There’s no “right” or “wrong” way to work with data — you can pivot a dataset just as well in a spreadsheet as you can with Python or SQL! The unique preferences, skillsets, and opinions of data teams are what should drive their data workflow, not a tool’s limitations.
Hex takes a different approach: it’s a truly
multi-modal
analytics workspace
that puts all these ways of working on one level playing field. In Hex, it doesn’t matter if you prefer to work in SQL or Python, spreadsheets or no-code UIs, with AI assistance or without — all of these different modalities for analyzing data work equally well and all work together, in one place.
We consistently hear from teams using Hex that critical data projects are
orders of magnitude quicker
because of their new hybrid, multi-modal workflow:
The process of building a new segmentation model would take weeks to do in a notebook and then even longer for an engineer to deploy to production.
With Hex, we’ve been able to launch a new model every two days on average for the last year.
— Matt Sievert, Director of Analytics at Paytronix
So what does this actually look like? To illustrate the power of a multi-modal workspace, we’ll do the same exact data project in Hex three times, with three very different workflows.
The question
My favorite demo dataset is the “Dumpling Shack,” which indexes customers and orders at a small, made-up dumpling restaurant. This data lives in our Snowflake warehouse where it’s modeled out and documented with dbt, just like a real-world business dataset.
Let’s imagine the Dumpling Shack is hiring a new celebrity chef and they want to add a new dish to the menu.
Based on historical menu item performance, what kind of dish should we have them add, that's not a repeat?
Workflow one: SQL-first
We’ll start off by demonstrating how to answer this question with a standard SQL-forward workflow. This is probably how a lot of analysts would tackle the challenge using other tools, because they’re generally most familiar with SQL.
You can probably imagine doing this using a standard BI SQL runner or IDE! Lots of tabs, lots of intermediate csv downloads, screenshots, and copy/pasting queries into text documents for safekeeping. Even seemingly simple questions inevitably get complicated pretty fast. We’ve all been in endless tab-land:
In Hex, instead of opening a bunch of different tabs or editing and re-running the same queries over and over again, we’ll work across multiple SQL cells
in the same Hex project.
Hex supports chaining SQL queries together, running new queries against the results of a previous one without having to manually construct CTEs or subqueries each time. You get full visibility into the intermediate results for debugging, and can easily explore down branches without having to refactor queries.
Here’s the full video of answering our question with a SQL-only workflow. In about 7 minutes (with commentary) we were able to run a chain of SQL queries that ID’d our most profitable & popular dishes and got a sense of what might be a good next dish.
We used a few key Hex features to do this efficiently in just SQL:
Chained SQL queries
Integrated charts
for quick visualization of SQL results
Text cells
for context
Workflow two: No code
Now, we’ll explore a completely different way to solve the same puzzle: by relying on Hex’s no-code cells to answer the same question without writing a single line of code.
Hex’s multi-modal notebook interface is designed to be
just as efficient
for no-code users as it is for those working in SQL or Python. The coolest part is that we aren’t going to use a different tool, or even a different section or mode of Hex. It's the exact same notebook-based interface and overall project flow, just with different building blocks.
Instead of SQL or Python cells, we're using pivots, filters, charts, and data cells to query, transform, and visualize data.
In roughly the same amount of time as a purely SQL workflow, we were able to answer the same question without writing any code; instead we relied only on no-code cells to query, transform, and visualize data.
Here’s the report we built at the end of this process. You’ll notice that it’s functionally indistinguishable from the SQL-based project. You’d never know that a business analyst who doesn’t know SQL built it, just like you’d never know that the first one was built with nothing but SQL.
1Q3W embed
We used five specific no-code tools to get this done and there’s lots more that we didn’t get to highlight, from data writeback to user inputs and single value displays.
Data Browser
Chart cells
Spreadsheet Calculations
Filter cells
Pivot cells
Workflow three: Hybrid
If there did exist an officially “hexy” way of doing things, it would be a hybrid workflow.
The most efficient way to get work done is almost always to mix and match all of the modalities you’re familiar with, using specific languages or tools for specific parts of a project and setting them aside when they aren’t necessary. This is the way most people
wish
they could work, but because of the siloed and single modality nature of most tools, changing languages usually means completely switching tools, which is inefficient and complicated. With Hex, it can all stay in the same workspace.
To answer this question as efficiently as possible, I’ll use SQL, Python, and no-code tools, picking and choosing what feels most useful without worrying about why or how to make it work.
Looking at the structure of this project makes it clear just how multi-modal these hybrid workflows are. The cells I created followed this flow:
Data Browser → SQL → Chart → SQL → Pivot → Chart → SQL → SQL → Chart → Python → Table Display
.
There’s no rhyme or reason to that flow other than: it was what felt natural to me. But that’s actually a
great
reason! If I’d been using a more limiting, single-modality tool that confined me to
SQL → SQL → SQL → SQL
I would have got the same answer
eventually
, but it would have taken significantly longer.
Multi-modal accelerates the efficiency of data teams
The question we answered is a classic
exploratory or “ad hoc” data question
. There’s probably not an existing report that answers it
perfectly
— maybe there are reports on overall best selling dishes, but to actually understand the
why
behind their performance and make a recommendation, we needed to drill down a little further and get our hands a bit dirtier in the data than a simple dashboard or report will support.
This type of ad-hoc exploration is where Hex shines, regardless of your preferred workflow or language. In the three examples above, the iterative, modular way of working in Hex makes it efficient to explore rabbit holes, test hunches, and piece together insights — regardless of your preferred language or workflow.
Each of these workflows took me approximately the same amount of time because I'm very familiar with all of them. But for many users, SQL might be totally inaccessible. Others might be comfortable with SQL but still find building complex queries frustrating and slow. And some data analysts might just prefer to work primarily in Python or use no-code tools.
Hex’s multi-modal design
means everyone can use the exact same workspace to get their work done faster, without being penalized for their individual preferences or having to adapt their workflow just to support arbitrary tool choices.
And over time, as teams get used to having easy access to other modalities, they tend to adopt an efficient “hybrid” workflow that doesn’t just speed things up, but makes it easy to tackle projects that were time-consuming or flat-out impossible in other tools.
We're amazed at how useful Hex has been for the needs of Greenhouse's data team.
It bridges that gap with the powerful and flexible notebook environments that also integrates easy SQL querying and native chart abilities.
-
Mona Khalil, Data Scientist at Greenhouse
That’s the beauty of multi-modal. There’s less friction, more possibility and everything is more efficient.
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
