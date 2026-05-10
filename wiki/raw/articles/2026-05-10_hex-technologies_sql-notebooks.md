---
title: "SQL Notebooks > SQL Runners | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/sql-notebooks/"
scraped: "2026-05-10T01:29:01.517499+00:00"
lastmod: "2022-04-13"
type: "sitemap"
---

# SQL Notebooks > SQL Runners | Hex 

**Source**: [https://hex.tech/blog/sql-notebooks/](https://hex.tech/blog/sql-notebooks/)

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
SQL Notebooks > SQL Runners
SQL finally gets literate programming
Izzy Miller
Product
April 13, 2022
Share:
twitter
linkedin
In this article
SQL runner workflows are broken
Notebooks are the best tool for analytics, but SQL is left out
How does Hex make it better?
Get started for free
knowledge
People love to argue about SQL and Python. Which is better? Which one should I use for 'insert data analytics task here'? Which one should I get tattooed on my forehead?
We opt for the “por que no los dos?” approach— Hex lets you
use Python and SQL interchangeably
in the same environment, and we are completely agnostic as to which tasks you use each language for. We’re pretty confident that this polyglot approach is a more efficient way to do data work!
But this week we've decided to pick favorites, with a bunch of posts on using SQL in Hex— and only SQL. We want to emphasize that
you can build amazing data applications in Hex using just SQL.
In fact, we think Hex is
still the best tool for data work even if you're only using SQL
.
For more, see
Building Data Apps with SQL
.
SQL runner workflows are broken
There's four big problems that most SQL runners and IDEs don't solve very well:
Organization:
How do you keep track of queries while working?
Versioning:
How do you track changes to queries and record previous versions of analysis?
Collaboration:
How do you work together with teammates or get feedback from stakeholders?
Delivery:
How do you deliver or present results? (we won't cover delivery in this piece— see
Building Data Apps with SQL
for the scoop.)
This isn't organized, versioned, or collaborative.
Too often the answer to these questions is "keep it in a scratchpad" or "check a bunch of loose .sql files into git" or even "just open a lot of browser tabs". This precludes any kind of useful collaboration, and anything that you can muster happens more or less asynchronously via slack or github PR comments. It's really hard to do great analytics work if you feel disorganized and are misplacing queries.
State of the art SQL organization and collaboration.
Notebooks are the best tool for analytics, but SQL is left out
Someone important once said "notebooks are
the worst tool for analytics
— except for all
the others that have been tried
". Their literate and self-documenting format lends itself perfectly to exploratory analytics work that requires context and commentary, Their linear, cell-based layout makes even complex projects fairly manageable.
And despite being imperfect (although we've actually
fixed most of their problems in Hex
), they certainly have better solutions to organization and versioning than anything that exists for SQL. They are self contained, neatly organized, and fairly portable.
The problem is that SQL workflows in existing notebooks are half-baked at best, and end up being more trouble than they're worth. No autocomplete, writing SQL in block quotes and iterating over DB cursors to return results— not to mention the need to write Python to access the SQL query results.
This is not an acceptable SQL editing experience.
It's just not worth it, and analysts wind up trudging back to their dozens of SQL runner browser tabs.
How does Hex make it better?
Hex addresses the challenges of organization, versioning, and collaboration just as elegantly for SQL-only workflows as it does for polyglot ones.
Here, check out
the SQL notebook Logic View
for a data application that I made in ~10 minutes with Hex. It's self-documenting, neatly organized, easy to understand, and entirely SQL.
Don't believe me? Here’s a one-take video of me building the app you see embedded above, taking just over 10 minutes (with lots of ums and hmms), using no code besides good old SQL.
Some of the key features
There's a handful of specific Hex features that make it the best SQL notebook for doing data analytics.
Organization:
Hex’s Logic view works just as well with SQL as it does with Python or R, so all your queries are neatly organized into cells and organized in a linear fashion. It’s easy to add context with markdown or charts interspersed between SQL cells, and all dependencies are charted in a familiar DAG UI.
SQL cells organized in the Logic View and Graph
Unlike typical notebooks though,
every Hex SQL cell is a complete SQL IDE
, with a schema browser, autocomplete, syntax highlighting, and query caching all built in.
Dataframe SQL
also makes it easy to write smaller, more ergonomic queries, breaking up CTEs into individual cells. You can even write SQL directly against an uploaded .csv!
Hex's cell-based SQL IDE
Versioning:
There's built-in versioning right in each project, so you can quickly see what changes others have made and restore to previous versions. Every version of a query is auto-saved, and app snapshots make it possible to version not just code, but results as well.
Rich SQL diff view in Hex (this feature is currently in beta)
You can also version control Hex projects with git, to fit right into your existing workflows and infrastructure.
Collaboration:
Working in a Hex project, you can collaborate live with colleagues on SQL queries and see changes in real-time as they're made. Cells auto-lock to prevent typeover, so you never have to worry about stepping on anyone's toes.
Working in a Hex project together
Built-in commenting works both for the backend Logic View and the published App View, so both teammates and stakeholders can give feedback throughout the process, tightening feedback loops and preventing extra work.
Commenting back and forth with a stakeholder, right where work is being done
Delivery:
Once you have something to share, the SQL notebook layout of a Hex project can be easily turned into a flexible, interactive
data application
that anyone with a web browser can use— without anyone writing a single line of non-SQL code. See
Building Data Apps with SQL
for more details on this process.
Embedded below is an example of a SQL only data app made with Hex. It has rich text that's dynamically parameterized, beautiful display tables, a time-series chart, and an interactive input.
This app is intentionally simple. It was built from scratch in 10 minutes!
Once you try writing SQL in a notebook, you'll wonder how you ever managed to stay organized without it.
Share:
twitter
linkedin
Ready to try out a better SQL notebook experience? Click below to get started for free.
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
