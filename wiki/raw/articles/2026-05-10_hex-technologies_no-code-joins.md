---
title: "You can now do no-code joins in Hex — no SQL required | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/no-code-joins/"
scraped: "2026-05-10T01:29:33.710908+00:00"
lastmod: "2024-11-06"
type: "sitemap"
---

# You can now do no-code joins in Hex — no SQL required | Hex 

**Source**: [https://hex.tech/blog/no-code-joins/](https://hex.tech/blog/no-code-joins/)

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
No SQL? No problem. New no-code joins keep you in the flow of analysis.
... and open up a whole new world of insights for stakeholders.
Kevin Marr
Product
November 6, 2024
Share:
twitter
linkedin
In this article
Smart joins with guardrails
Why you might opt for no-code joins in Hex
Other tools have no-code joins. What makes Hex’s different?
No-code joins keep you in the flow of analysis, not in the weeds of SQL
Get started for free
Most strategic business questions need data from multiple sources — like,
Which products are most frequently purchased together?
or
What channels brought users with the highest lifetime value (LTV)?
Let’s take a specific example — the Head of Growth Marketing wants to understand how churn varies across subscription plans.
They start exploring data and realize they need two different tables, but have questions like:
What table do I use? How does the join syntax work? Do I do an inner or outer join? Which columns do I need to join?
Any of these questions can lead our stakeholder right back to the data team’s ticket request queue, pulling them out of their analytics flow and leaving them waiting for answers before they can come to a conclusion on strategy. That’s why, in our recent
Explore release
, we
launched no-code joins
— to give our low-code and no-code friends the ability to do joins without knowing SQL or tapping the data team. With intuitive guardrails, our joins let stakeholders stay in the flow of analysis and provide results they can trust.
Smart joins with guardrails
Hex’s no-code joins combine intuitive UI with technical guardrails that keep you from unsuspecting misconfigured results. Now you can start with a point-and-click interface and get suggestions for join keys, warnings about mismatches, and accurate calculations even in the midst of fan-outs (when rows from one of the tables get duplicated through a SQL join). See how it works in our video:
Instead of working through complex SQL queries, just select a table in Hex that has the information you want and hit ‘Join table’ to get started.
Hex is smart enough to suggest join keys — or identify columns that might be good for joining — by using a combination of AI and some good old-fashioned column profiling. It double-checks that the tables relate in a sensible way, kind of like making sure puzzle pieces fit before you try to force them. And here's the best part: it automatically ensures your numbers still come through accurately even when a fan-out occurs.
Basically, it’s like having a data wizard by your side, making joins easier for everyone, whether you know SQL well or are just getting started with data analysis.
Why you might opt for no-code joins in Hex
If you’re not a SQL-pro, there’s a handful of potential speed bumps that can land you back in the data team waiting queue when it comes to SQL-based joins:
It’s hard to write code.
Writing correct joins is a notoriously difficult aspect of the SQL workflow. It’s not just about understanding the syntax; it requires a strong grasp of relational databases, the structure of the data tables and how they relate.
It’s hard to know if columns actually match.
A user might see columns like
ORDERS.USER_ID
and
USERS.UUID
and assume that they are join keys, but they might be entirely different IDs from disconnected systems that never match. They run the query and get zero rows in the result.
It’s hard to make sure tables relate in the way you think they do.
Two columns might match up
sometimes
but not consistently in the way the user was expecting. This will cause the query result to have some data, but not all of it.
It’s hard to prevent
fan-outs
— or multiple matches — when you aggregate joined data.
A row from one table might match with multiple rows from the other, based on the join criteria. When this happens in SQL, a new row is created for
each match
. This is particularly notorious for aggregations, such as `sum(revenue)` or `average(age)`. Careful and experienced SQL writers can avoid these issues by writing some auxiliary queries to check the validity of a join predicate before blindly charging ahead.
Our no-code joins are built so that you have the information to approach the join differently if needed, letting you focus on the analysis at hand.
Other tools have no-code joins. What makes Hex’s different?
The concept of no-code joins might be familiar (which is generally a good thing for curious stakeholders looking to try Hex), but we did two things that most vendors don’t:
There's no upfront modeling
- No prep or complex modeling is required to do a join. This is helpful because usually by the time you realize you need to do a join, you're already in the middle of an analysis. Our no-code joins can be applied in real-time so you can adjust your data model on-the-fly. With other tools, if you realize mid-analysis that your data model is wrong, you have to start over and do prep and modeling.
(Note: Hex's no-code joins are designed to combine tables during ad hoc data exploration. In some cases, you'll want a more rigorous, curated model that you can re-use across all analyses. Today, Hex can connect to data via dbt's semantic layer and we are working on expanding our semantic sync capabilities to allow MetricFlow to enhance Explore.)
Built-in safety features
- With smart join tests, Hex can steer users away from misconfigured joins. Additionally, Hex’s advanced SQL generation logic can maintain accurate aggregations even when a join duplicates rows through a fan-out, keeping you on track for trustworthy results.
No-code joins keep you in the flow of analysis, not in the weeds of SQL
No-code joins help keep analysis flowing, so your data team can focus on insights — not troubleshooting joins. With built-in safety measures, they open up a whole new world of answers and exploration, empowering business users to answer more complex data questions with confidence.
Learn more about Explore and no-code joins at our
upcoming live event.
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
