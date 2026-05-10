---
title: "Deepening Our Snowpark Integration | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowpark-integration-polyglot/"
scraped: "2026-05-10T01:29:05.251782+00:00"
lastmod: "2023-10-10"
type: "sitemap"
---

# Deepening Our Snowpark Integration | Hex 

**Source**: [https://hex.tech/blog/snowpark-integration-polyglot/](https://hex.tech/blog/snowpark-integration-polyglot/)

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
Deepening Our Snowpark Integration
Switch between SQL, Python, and visual cells while using a Snowpark dataframe
Armin Efendic
Product
October 10, 2023
Share:
twitter
linkedin
Building upon our blog
Introducing Snowpark for Python in Hex
, we are excited to introduce new enhancements to our Snowpark integration! Now in Hex data scientists can move between SQL, Python, and visual cells while leveraging a Snowpark dataframe. More on this later!
Before we delve into the details, let's take a moment to recap what Snowpark is all about. At a high level,
Snowpark
extends Snowflake’s capabilities by empowering developers to write custom code against their data in various non-SQL programming languages including Java, Scala, and Python. Hex’s Snowpark integration specifically supports
Snowpark for Python
,
which is what we will be focusing on in this post.
Hex’s
Existing Snowpark Integration
Our existing integration brings enhanced security and an incredibly straightforward way to create a Snowpark session. Set up is a breeze - all you need to do is
toggle
the Snowpark option within your Snowflake data connection in Hex. Hex will then leverage this Snowflake connection to create a Snowpark session. We affectionately call this Hex’s
Snowpark Easy Button
!
With the Easy Button, users don't need to
expose their credentials
in plain text or manage hidden files just to create a Snowpark session. We piggyback off the existing Snowflake connection that has been created. This connection is created and managed by a Hex Admin. For those interested in how this works, it’s all seamlessly managed by our trusty built-in package,
hextoolkit
.
Here is an example of what is required to create a Snowpark session outside of Hex vs in Hex:
vs.
In terms of simplicity, Hex takes the hassle out of pre-installing packages in your local environment. We've already pre-baked Hex projects with all the essential packages needed to run Snowpark, and we diligently keep them up-to-date with the latest stable releases.
Moreover, we've allowed users to use a first-class SQL cell and still return a Snowpark dataframe. This provides auto-complete, syntax highlighting, and formatting in SQL while working with a Snowpark dataframe. If you're wondering how this works, don't worry; we'll review it below!
Exploring What’s New
Snowpark
employs lazy evaluation
, making it ideal for working with big data. Under the hood, it actually translates Snowpark code into SQL to leverage Snowflake’s SQL Engine. That’s how we get the distributed compute - let's see this in action!
Here is a link to the
notebook
above!
SQL, Python, and visual cells with Snowpark
If you're new to Hex one thing you'll learn to love is the ability to switch between different cell types. Imagine you're working on a SQL cell, performing complex table joins, and suddenly, you want to switch to a Python cell, and later, perhaps to a visual cell. You can do this effortlessly because, under the hood, you're working with a Pandas dataframe.
You may have seen this ability referred to as a
polyglot workflow
. Wouldn't it be great to have this flexibility between SQL, Python, and visual cells while leveraging a Snowpark dataframe? Well, as it turns out, we thought so too!
Here is a link to the
notebook
above!
In addition to our deepened integration with Snowpark, we also wanted to account for the users that are a bit more security conscious. With the Snowpark toggle enabled, you get all the benefits of our Snowpark integration with the security benefits of OAuth. You can read more about our
Snowflake OAuth
configuration in our documentation.
When To Use Snowpark?
You might be wondering when to use Snowpark. Let’s first start with a basic use case. You've likely encountered memory limits in any notebook environment, including Hex. With our Snowpark integration, you can now perform traditional analyses without worrying about memory consumption in the kernel. Say you perform a
select * from my_large_table
and your kernel runs out of memory. You can simply select a Snowpark dataframe as your return mode. Then, leverage that same dataframe in any other SQL, Python, or visual cells and enjoy all the Hex features you love.
Once you have a solid understanding of how to work with Snowpark dataframes, explore more advanced use cases of Snowpark, such as data engineering and machine learning workloads:
Develop comprehensive data pipelines using Snowpark dataframes.
Explore Snowflake Streams for a robust
Change Data Capture (CDC)
pipeline.
Schedule your pipeline using
Hex’s built-in scheduling
or integrate with orchestration tools like Airflow or Dagster through our
integrations
.
Leverage
Snowpark ML
for a streamlined approach to machine learning in Snowflake.
For a detailed demonstration, explore the
Snowpark ML + Stored Procedure Tutorial
.
In summary, Hex has deepened our Snowpark integration. We now provide users the flexibility to switch between SQL, Python, and visual cells all while leveraging your Snowflake warehouse. Under the hood, this is done using Snowpark dataframes. In addition, we support OAuth while working with a Snowpark session. If you want to take Snowpark + Hex for test drive, you can start a
free trial
!
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
