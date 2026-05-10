---
title: "What are data pipelines? How they work & how to choose | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-pipeline/"
scraped: "2026-05-10T01:29:02.806979+00:00"
lastmod: "2025-12-10"
type: "sitemap"
---

# What are data pipelines? How they work & how to choose | Hex 

**Source**: [https://hex.tech/blog/data-pipeline/](https://hex.tech/blog/data-pipeline/)

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
What are data pipelines?
The invisible infrastructure behind every data-driven decision
The Hex team
Data
December 10, 2025
Share:
twitter
linkedin
In this article
What are data pipelines?
How data pipelines work
3 types of data pipelines
Criteria to choose the right data pipeline
Build a pipeline that actually delivers answers
Get started for free
Every company runs on data scattered across dozens of systems, from their customer relationship management (CRM) systems and payment processors to their product databases and marketing tools. The challenge is turning that scattered mess into something you can actually use to make decisions.
That's what data pipelines do. They're the tech that pulls data from sources, transforms it into usable formats, and delivers it somewhere your team can find and use it.
Data pipelines matter to anyone who depends on data to do their job (i.e., everyone). For data engineers, they're the foundation you build and maintain. For analysts, they're what make your queries possible. For business users, they're the invisible layer that determines whether you get trustworthy numbers or conflicting reports from every department.
In this article, we'll cover what data pipelines are, how they actually work, various types of data pipelines, and what to look for when choosing or building your own.
What are data pipelines?
Data pipelines are automated systems that pull data from various sources and turn that data into usable formats. The pipelines also consolidate data into a single dashboard that you can more easily work with. A data pipeline usually logs every step, so you can trace exactly how the raw records became the metrics on your dashboard.
Let’s say your team is away on that long-awaited offsite. Even though you’re away, your Salesforce connector continues to pull in customer records, your payment processor logs transactions, and your app servers record user events. All these data points arrive at your data pipeline in different formats — Salesforce's API, Stripe webhooks, and raw log files.
Your data pipeline takes these scattered pieces and assembles them into something you can work with. Raw Salesforce contacts get deduplicated by email. Stripe payments get matched to customer IDs. Application events get parsed into structured fields. All so that when someone asks, "how did we calculate this?", you just have to show them the records in your data pipeline.
Data pipelines are a valuable part of any company's data infrastructure because they give you one authoritative path from raw data to metrics. When marketing reports 12% customer growth, but finance sees revenue decline, you trace both numbers back through the pipeline. The problem could be that your marketing team is counting all new signups while finance is measuring paid conversions. Both numbers are correct — just measuring different things. The pipeline makes this visible.
How data pipelines work
Most people think of pipelines as a black box where data goes in and data comes out. But under the hood, there’s a sequence of components working together like clockwork. Here are the highlights:
Connectors pull data from your sources
Connectors are integrations that link your pipeline to external systems. They authenticate with your sources, handle their APIs, and pull updates in the background. You set them up and they do their job without you needing to write authentication code or manage tokens that expire.
Transformations clean and reshape raw data
Raw data almost always arrives messy, containing duplicates, missing fields, and incompatible formats. Transformations are the rules and logic that standardize, deduplicate, and restructure that data into something usable.
The most commonly used transformation pattern is ELT (Extract, Load, Transform). It lets you load raw data directly into your warehouse and run transformations right there using SQL. Need to change how you calculate customer lifetime value? Update the SQL, rerun, and done. You don't have to deal with the headaches associated with managing separate infrastructure.
Orchestration runs tasks in the right order
Orchestration is the scheduling layer that makes sure each step in your pipeline runs at the right time, in the right sequence, with the right dependencies. Task 2 runs before task 1 finishes and fails; you restart manually, and since task 3 depends on 2, it also fails. It's carts-before-horses on repeat.
With orchestration tools, you only have to encode dependencies once: task 2 waits for task 1, and task 3 waits for 2. This way, when Salesforce's API hits a rate limit at 2 am, the system just waits and retries. You get to sleep through the routine stuff and wake up only when you’re needed to oversee something actually critical.
Collaboration lets everyone work together in real time
Collaboration tools are the shared environments where data engineers, analysts, and business users can build, review, and iterate on data work together. These platforms bring workflows together: your data scientist writes the transformation logic, your analyst immediately queries the results to build a dashboard, and your business user explores the data through
conversational queries
, all in the same environment. No waiting for the BI team and absolutely no exporting CSVs between tools.
Notebooks are another popular approach to data collaboration. Notebooks let data scientists work with the same tools as analysts. When your data scientist builds a churn prediction model, your analyst can fork that
notebook
to test regional variations without waiting for a meeting or handoff.
3 types of data pipelines
This is where pipeline decisions get expensive. Pick the wrong architecture, and you're either burning money on infrastructure you don't need or catching data anomalies hours after they’ve died down. The choice comes down to one question: how fresh does your data need to be?
1. Batch processing pipelines
Batch processing collects data over a set time window (hourly, daily, or weekly) and then processes everything together in a single job. Instead of handling each record as it arrives, the pipeline waits until the batch window closes, runs all transformations at once, and outputs the results. This approach works well for warehousing, ML training, quality checks, and complex transformations. Basically, anything where waiting a few hours isn't a big deal.
For example, your marketing analyst can afford to batch process the weekend campaign's performance. Saturday's Facebook ads get joined with Sunday's conversions, aggregated by campaign, and enriched with customer segments. For their use cases, thorough analysis is more important than immediate response. Learn how to
bring all of your lead signals together
.
2. Streaming processing pipelines
Streaming pipelines process data continuously, record by record, as soon as it arrives. Rather than waiting to accumulate a batch, the pipeline ingests each event in real time, applies transformations immediately, and pushes results downstream within seconds or milliseconds. This is necessary for use cases where you need to know what's happening
now
. For instance, IoT sensors monitoring a manufacturing line need to trigger alerts the instant something looks off, not in tomorrow's batch report.
The tradeoff: streaming pipelines run around the clock, and that can get expensive. Your team needs to know how to handle distributed systems, out-of-order events, and state management to an extent that batch processing doesn't require.
3. Hybrid pipelines
Hybrid pipelines combine both approaches, routing data to batch or streaming paths based on the use case. Time-sensitive events flow through the streaming layer for immediate action, while the same data also feeds into batch jobs for deeper historical analysis. For example, an e-commerce site streams clickstream data for real-time personalization while batch jobs run nightly to train recommendation models on complete purchase history.
Criteria to choose the right data pipeline
You can build pipelines from scratch, stitch together open-source tools, or adopt a platform that handles the infrastructure for you. There's no universally right answer, but there are decisions you'll regret if you don't think them through early.
While you’re choosing, platforms like
Hex
— an AI-powered workspace where data scientists and business users work side by side — show what's possible when you don't have to choose between technical depth and accessibility. But the principles apply regardless of which tools you pick.
Scalability
Your pipelines need to grow with your data. Today's 100GB might become 10TB as your business scales. When evaluating platforms, look for:
Horizontal scaling
: Can the system add more nodes to handle increased load, or are you stuck upgrading to a bigger single machine?
Concurrent user support
: How many analysts, dashboards, and scheduled jobs can run queries simultaneously without performance degrading?
Compute flexibility
: Can you spin up additional processing power for heavy jobs (like ML training) without affecting day-to-day queries?
Storage separation
: Does the platform separate storage from compute, so you're not paying for idle resources when data sits unused?
The goal is a platform that handles growth without forcing a painful migration or complete re-architecture down the line.
Governance and data quality
When you're racing to get a pipeline running, governance and data quality checks often get pushed to "we'll add that later." The thing is, bad data compounds over time. A duplicate record in your source becomes duplicate revenue in your dashboard, which becomes a flawed forecast in your board deck. By the time someone catches it, the error has spread across dozens of reports and eroded trust in everything the data team produces.
Retrofitting governance is painful because it means you have to audit existing pipelines, track down undocumented transformations, and convince teams to change workflows they've already built around. It's far easier to build these guardrails in from the start.
Starting out, look for platforms with features that catch quality issues before they hit production:
Automated tests flag bad records.
Lineage tracking shows where transformations break.
Semantic layers
ensure everyone uses the same definitions.
These features turn governance from an afterthought into something that runs automatically alongside your data work.
Collaboration
Data work has always been collaborative, but legacy tools forced teams into clunky handoffs. The old-school "build and export" system breaks down when you need to move fast.
Back in the day, your data scientist would build a churn model and export it to PowerPoint for your VP of Sales. When the VP wants regional filters, it’s back to the data scientist. Rinse and repeat for every question.
In Hex, your data scientist builds the churn model in a
Notebook
in the morning. By afternoon, your analyst has forked that same notebook to test regional variations (
real-time multiplayer editing
means no exports, no meetings, no waiting). The next day, your VP explores the results through
natural language
: "Show me churn risk by customer segment," and gets instant visualizations without waiting for the BI team.
Let’s say your VP needs more info and asks for a custom ROI calculator that pulls live data from your warehouse. Your analyst builds it as a
Data App
: an interactive interface with dropdowns and sliders that business users can operate without touching code. The app queries your pipeline's output directly, ensuring everyone works from the same source of truth. You can even
embed these analytics
directly into customer-facing products. It’s all running on the same pipeline, the same data, and no rebuilding.
DataOps practices
People make mistakes, overwrite each other's work, and forget what they changed last week. That's why the platform you choose needs version control (so you can roll back when something breaks), automated testing (so errors get caught before they reach production), and lineage tracking (so you can trace a bad number back to the transformation that caused it).
Hex bakes these practices in by default: version history on every notebook, status workflows for promotion from draft to production, and lineage that shows exactly how data flows through your transformations.
Build a pipeline that actually delivers answers
Here's a quick test: time how long it takes your team to answer a new business question that requires them to join data sources or change the way a metric is defined. If it's days instead of hours, your pipeline needs attention.
The teams who've fixed this chose integrated environments — one place for workflows instead of fragmented tools. Data scientists build models. Analysts query results immediately. Business users explore through conversational interfaces. No one waits for the BI team to build another dashboard.
Ready to see the difference?
Book a demo with Hex
, and we'll show you how our platform connects to your existing data stack — so you can stop reconciling spreadsheets and start answering questions.
Share:
twitter
linkedin
Learn what you need to build context for AI analytics, in our guide: The Data Leader's Guide to AI
Download guide
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
