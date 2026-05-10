---
title: "snowpark under the hood | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowpark-under-the-hood/"
scraped: "2026-05-10T01:29:01.417616+00:00"
lastmod: "2024-04-08"
type: "sitemap"
---

# snowpark under the hood | Hex 

**Source**: [https://hex.tech/blog/snowpark-under-the-hood/](https://hex.tech/blog/snowpark-under-the-hood/)

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
A Look Under The Hood Of Snowpark
Dive into the workings of Snowpark and how it pertains to Hex's Snowpark integration
Armin Efendic
Product
April 8, 2024
Share:
twitter
linkedin
In this article
Unwrapping Snowpark Queries:
Conclusion:
Get started for free
Snowpark has brought the world of data engineering pipelines and machine learning into Snowflake. Its initial release focused more so on data engineering pipelines and with the release of Snowpark ML we now have an end-to-end ML experience. This has provided capabilities down stream in terms of data ingestion up to the advanced use cases around ML development.
But, what about the work loads in between, such as ad-hoc analytics, visualizations, exploratory data analysis (EDA), and just getting answers to those pesky business questions? This blog will focus on those types of workloads and how we can harness the power of Snowpark in Hex. We will be exploring what Snowpark commands look like in Snowflake and how Hex’s integration tailors to not just the data engineering and machine learning use case, but also everything in between.
This blog assumes that you have a basic understanding of what Snowpark is. If you would like a refresher or an introduction to Snowpark give
Snowpark Is Your Data Librarian
a read. We’ll start by exploring Snowpark Queries and Hex’s Snowpark integration in detail.
Unwrapping Snowpark Queries:
If you are reading this blog, you probably have some familiarity or at least a desire to learn more about Snowpark dataframes. In this section, I want to dive deep into the query profile of a simple snowpark query and see how it is being processed in Snowflake.
Let’s start with a simple query using Hex and I’ll make sure to ask for a Snowpark dataframe:
Under the hood Hex passes the following Snowpark query since I requested a Snowpark dataframe:
Copy
session.sql('select * from SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.STORE_SALES').show()
This is a glimpse at how Hex provides users the ability to use native SQL cells while still working with Snowpark dataframes. From a native SQL cell in Snowpark return mode, Hex will construct the Snowpark code on your behalf. I’ll also run the Snowpark code in a python cell just so we can see that the query is the same.
Let’s continue this exploration and find the two queries above from the SQL cell in Snowflake find this
From Hex’s Native SQL Cell:
Hex adds metadata for queries coming from a SQL cell so its easy for me to identify where the query is coming from.
From the Python cell using pure Snowpark code:
Notice it is the exact same query just without the metadata.
Both queries above employ lazy evaluation and show a preview of the data via the LIMIT 10 clause.
.show()
can also be referred to as an action call. I take the reference to the query and ask that an action takes place, meaning the query is run. In this case, only 10 rows are scanned. You can run
.collect()
and this brings the entire dataset to memory and performs as a regular
select *
query would. Use caution with this as it can cause an expensive query and even use all of your memory in a Hex project.
Let's explore the Query Profile of the query made from the Hex native SQL cell from above:
Notice that with the Snowpark query only 1 partition is scanned even though our query performed a select star with no limit clause in Hex. Under the hood, Hex constructs the appropriate Snowpark query like we saw above.
We didn’t hit any Snowflake result cache as this was our first query but this still only took ~600ms
The vast majority of the query was the Remote Disk I/O which was the reading of data
Since this result will now be cached as our result cache, subsequent runs will hit the result cache, otherwise known as
Query Result Reuse
This is at the core of what makes working with Snowpark dataframes so powerful and is a concept called lazy evaluation. Hex utilizes this, by providing previews of your data in a native experience without actually bringing all the data into Hex. We only bring in a preview of the data, and in most cases its just 10 rows.
You might ask, why is this helpful - particularly with those use cases in between data engineering and machine learning. Let’s revisit the example query from above, the table contains 29 billion rows of data. Performing any sort of analysis on that size of data in traditional notebooks, let alone in a SQL cell, is impossible and requires other tooling like Spark. This means your entire data set now has to be moved to another platform just to start analyzing it. With Hex’s Snowpark integration this becomes incredibly easy.
Let’s take a simple example of a null check of our customer column,
SS_CUSTOMER_SK
from
store_sales
. Better yet, I will use Hex Magic to write the Snowpark query for me in Python:
Let’s see what this query translates to in Snowflake:
Notice the same metadata is passed to the snowflake query since we called
store_sales
. This ability to switch between different cell types is all managed for you by Hex. We even support visual cells like charts, where the aggregation is completed in Snowflake and only the result set is brought back to Hex.
Conclusion:
In summary, Snowpark frees data scientists from memory constraints. Hex’s integration enables users of all skill levels to work with Snowpark. Whether you want to join tables with SQL, calculate a moving average with Python, and then visualize the result - all can be done in Hex while seamlessly leveraging a Snowpark dataframe! You can also rely on using Hex Magic in Python and SQL cells to help fix pesky bugs and even self-train on Snowpark syntax.
At the end of the day, its all about getting value out of your data and here at Hex we believe the tools used should never limit you but rather accelerate the work that you can do.
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
