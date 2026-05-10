---
title: "Introducing Snowpark for Python in Hex | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowpark-hex/"
scraped: "2026-05-10T01:29:06.183467+00:00"
lastmod: "2022-06-14"
type: "sitemap"
---

# Introducing Snowpark for Python in Hex | Hex 

**Source**: [https://hex.tech/blog/snowpark-hex/](https://hex.tech/blog/snowpark-hex/)

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
Introducing Snowpark for Python in Hex
Plus, Snowflake Partner Connect and Premier Partner status
Ariel Zahler
Product
June 14, 2022
Share:
twitter
linkedin
In this article
Snowpark for Python
Hex: The Snowpark for Python Easy Button
Snowflake Partner Connect
Get started for free
Every day, thousands of people use
Hex and Snowflake together
to query, analyze, and explore their data.
Today we’re excited to announce that we’ve made Hex and the Snowflake data warehouse work even better together. We’ve built
first-class support for Snowpark into Hex
, giving users a new and powerful interface to their data. We’ve added Hex to
Snowflake Partner Connect
, so it’s only one click to set up a new trial with preconfigured access to your Snowflake instance.
With our newly minted Premier Partner status, this is just the tip of the iceberg of what Hex and Snowflake can do together. Let’s dig in!
Snowpark for Python
Hex now comes with built-in support for Snowflake’s new
Snowpark for Python API
, which lets users write familiar Python code that’s executed
on Snowflake
, taking advantage of the massive scalability and distributed compute of the cloud data warehouse.
Under the hood, Snowpark operates with DataFrames just like those used by pandas or other Hex cells, with one major difference:
Snowpark DataFrames are executed
lazily,
so data isn’t pulled into Hex until a user runs an evaluation on it
. This means that for many workflows,
Snowpark DataFrames
are more efficient than Pandas DataFrames, and can help avoid memory limits common in traditional notebook workflows.
The below example uses the Snowpark API to calculate the min and max order date. But the data isn’t actually pulled into Hex just yet.
Copy
from snowflake.snowpark import functions as F
min_max_date = hex_snowpark_session.table("PUBLIC.SUPERSTORE_DATASET").select(F.min('ORDER_DATE'), F.max('SHIP_DATE'))
When we run .collect() to evaluate the DataFrame and return the results, it doesn’t matter how large the underlying dataset is; the query is quickly executed on Snowflake’s infrastructure, and only the bite-sized rolled-up final results are pulled into Hex.
Copy
min_max_date.collect()
Hex: The Snowpark for Python Easy Button
With packages to install and environments to configure, the road to getting started with Snowpark can be time consuming and technically complex. With the great power of Python also comes great frustration.
Hex sidesteps this by auto-magically installing the Snowpark API in any project connected to Snowflake, making it the easiest way to get started with Snowpark and Python. There’s no worrying about hosting a notebook, configuring environment variables, or downloading anything locally.
Here’s a step-by-step walkthrough (complete with live demo video!) of just how easy it is:
Assume I’m a business analyst for
Superstore
. I’ve been asked to pull a list of our top 100 customers for a special promotion. I’ll use Snowpark to solve the problem.
Snowpark + Hex
1. Start a free
trial
of Hex and establish a
data connection
with Snowflake and flip the “Enable Snowpark” toggle. You can also leverage
Partner Connect
to create a free trial of Hex with a pre-configured data connection, straight from the Snowflake console. Our data connections are extremely secure and reusable across the entire organization, so you only need to enter credentials once.
2.
Create a new project, open the Snowflake connection in the schema browser, and click “Get Snowpark session” from the Query dropdown. This
will automatically insert a Python cell and the required code to create a Snowpark session. All Snowpark package dependencies are already installed, so all you have to do is hit “Run”.
💡 This example uses
hextoolkit
, a special python package usable only from Hex Python projects. It supports programmatic access to data connections and (in the future) other Hex functionality.
Prefer prototyping in SQL? As always, Hex supports a polyglot workflow for Snowpark. You can return the results of any Snowflake SQL cell into a Snowpark DataFrame.
Watch as I find my top customers ranked by sales using Snowpark, live!
If you want to take a look at the notebook yourself, check it out
here
.
At Hex, we talk a lot about having a
low floor and a high ceiling
for our users. For folks who are new to the data science and analytics space, it’s pretty scary to think about all the overhead you might need to get started with Snowpark without Hex. We’re excited to support Snowflake SQL-savvy users who are new entrants into Python and data science, while also ensuring we provide a seamless experience for the Python jockeys of the world.
Snowflake Partner Connect
That’s just one milestone we hit. We’re also proud to announce that Hex is now a
Snowflake Premier Technology Partner
and a recent addition to
Snowflake’s Partner Connect
ecosystem.
Snowflake Partner Connect gives Snowflake customers a one-click button to trial Hex with immediate preconfigured access to your underlying data in Snowflake.
Check out our tile on the Partner Connect landing page (top right corner of the Snowflake UI). Snowflake will auto-generate objects that you can use for the Hex connection OR easily select the database(s) to power your Hex project and you’re off to the races.
Share:
twitter
linkedin
Love Snowflake? Us too! Try Snowpark for Python in Hex and let us know what you think.
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
