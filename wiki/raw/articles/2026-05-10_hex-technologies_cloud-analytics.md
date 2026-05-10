---
title: "What is cloud analytics? Benefits, architecture & how to choose | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/cloud-analytics/"
scraped: "2026-05-10T01:29:07.128566+00:00"
lastmod: "2025-12-12"
type: "sitemap"
---

# What is cloud analytics? Benefits, architecture & how to choose | Hex 

**Source**: [https://hex.tech/blog/cloud-analytics/](https://hex.tech/blog/cloud-analytics/)

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
What is cloud analytics?
How elastic infrastructure changes the way data teams work
R.H.
Data
December 12, 2025
Share:
twitter
linkedin
In this article
What is cloud analytics?
Why data teams should use cloud analytics
How cloud analytics works
Choosing a cloud analytics approach
Where cloud analytics is heading
Get started for free
Your analyst needs to run a heavy query, but the data warehouse is already maxed out serving dashboards. In the old world, you'd either wait for off-hours or start a procurement process for more hardware. With cloud analytics, you can spin up a dedicated compute cluster in seconds, run the query, and shut it down when you're done.
Cloud analytics separates storage from compute, so scaling analysis doesn't mean fighting for shared infrastructure. This guide explains how cloud analytics works, why the architecture matters, and what to look for when choosing a platform.
What is cloud analytics?
Cloud analytics is a service model where data storage and analysis happen on vendor-managed cloud infrastructure rather than servers you maintain yourself. Instead of tuning indexes, managing storage arrays, or configuring cluster parameters, you let the cloud provider handle optimization while you focus on the actual analysis.
Consider how this plays out in practice. Your analyst needs to answer a capacity planning question. In a traditional setup, they write SQL against an on-premise database that's also handling production traffic. The query times out because someone else is running a heavy report. They try again at 6 pm when the load is lighter, get results, export the data to CSV, build projections in Excel, and copy charts into Slides. Three days later, someone asks about a different region. And they have to start over.
With cloud analytics, your analyst runs the query against a dedicated compute cluster. Production traffic isn't affected, so the results come back in minutes. She iterates through follow-up questions in the same session because she's not competing for shared resources.
The architecture that makes this possible separates storage from compute. Your data lives in cheap cloud object storage while compute resources spin up and down based on query demand. This separation creates the elastic scaling and cost efficiency that define cloud analytics.
Why data teams should use cloud analytics
The business case for cloud analytics comes down to three things: you move faster, you spend less time on infrastructure, and you scale without procurement cycles.
Speed that improves workflows
Query performance directly impacts how you work. With cloud analytics, the analyst who used to wait for off-peak hours to run heavy queries now runs them whenever they need to,  without slowing down the dashboards everyone else depends on.
AllTrails saw this firsthand. Their analysts used to cobble together CSVs, SQL files, and Jupyter notebooks using a workflow that made even routine analysis slow and painful. After moving to cloud-based notebooks with direct BigQuery integration, processes that took hours
now take minutes
.
Cloud analytics platforms make this possible through architecture designed for concurrent workloads. Your ETL (Extract, Transform, Load) job gets its own compute, and your executive dashboard gets another. The analyst running heavy ad hoc queries doesn't slow down everyone else. The ROI comes from eliminating exactly this kind of friction — not from any single feature, but from removing the bottlenecks that slow down decisions.
Scalability without infrastructure overhead
The elastic compute model behind cloud analytics means you can run concurrent analysis workloads during business hours, then scale down to minimal infrastructure overnight.
Think about what happens when your data science team needs to train a model. In traditional setups, they either compete for shared compute (slowing everyone down) or wait weeks for dedicated hardware. With cloud analytics, they spin up a large compute cluster for the training job, run it for four hours, then shut it down. They pay for what they used, and don't have to deal with procurement meetings or capacity planning cycles.
The real savings come from eliminating idle "just in case" capacity. Teams that migrate to cloud analytics platforms typically find they were paying for far more infrastructure than they actually needed.
Enterprise adoption shows production readiness
If you're wondering whether cloud analytics is ready for serious workloads, look at who's already adopted the new tech. Most enterprise data now lives in the cloud, and adoption is remarkably consistent across
regulated industries
like financial services and manufacturing.
Even healthcare organizations have moved patient data to the cloud while maintaining
HIPAA compliance
, and financial services have migrated transactional data with security controls in place. If those industries have solved compliance concerns, yours probably can too.
How cloud analytics works
Most people think of cloud platforms as magic boxes where data goes in, and answers come out. But understanding the
data architecture
helps you use it better and avoid expensive mistakes.
Storage layer: where your data lives
The storage layer is where your data physically lives. In cloud platforms, this layer is separate from the compute that processes queries, which is the key architectural difference from traditional databases where storage and processing are tightly coupled on the same machine.
The storage layer holds your data and makes it available to whatever compute resources need it. It scales independently, meaning you can store petabytes without provisioning any processing power, and you only pay for the space you use. When compute clusters spin up to run queries, they read from this shared storage layer, which means multiple teams can access the same data simultaneously without creating copies.
Compute layer: elastic clusters that scale with demand
The compute layer is the processing power that runs your queries. These are the CPUs and memory that do the actual work of reading data, filtering rows, joining tables, and returning results. In cloud platforms, compute resources are provisioned on demand and billed by usage rather than owned as fixed hardware.
Clusters spin up when you start working and shut down automatically when idle, so you pay for minutes used, not servers sitting waiting. You can run multiple clusters simultaneously, so your ETL jobs, dashboards, and ad hoc analysis each get dedicated resources without competing for the same capacity.
Services layer: the invisible coordinator
The services layer is the control plane that coordinates everything else. It decides how to execute your query, manages user access, and keeps the system running smoothly. You never interact with it directly, but it's what makes the platform feel like a single coherent system rather than a collection of storage buckets and compute clusters.
The services layer handles authentication, optimizes your queries, and manages metadata so the system knows where everything is. It automatically decides the fastest way to execute each query, coordinates access so multiple users can work with the same data simultaneously, and keeps the whole system running without you tuning anything.
Choosing a cloud analytics approach
You can build on raw cloud infrastructure, adopt a managed data warehouse, or use an analytics platform that handles both storage and collaboration. The right choice depends on your team's skills and what you're trying to accomplish.
Start with where your data lives
If you're already on Snowflake, BigQuery, or Redshift, you don't need to move your data to get cloud analytics benefits. Look for platforms that connect directly to your existing warehouse. Moving data creates security headaches, governance complexity, and sync problems. The best analytics tools query your warehouse directly.
Match the platform to your team
Some platforms assume that everyone writes SQL. Others assume no one does. The reality for most organizations is that you have both: technical practitioners who want full control and business users who need guided exploration.
Platforms that force everyone into the same interface fail one group or the other. Your data scientist doesn't want a dumbed-down drag-and-drop tool. Your marketing director doesn't want to learn Python. Look for platforms that serve both, where technical users build analyses that business users can explore through a variety of methods that accommodate their skills and preference..
Notion's data team
built exactly this
. Their data scientists work in notebooks with Snowpark and Python, while their CX team uses published apps as a simple UI for pulling customer details. Sales combines Salesforce and Snowflake data without writing queries. Same platform, different interfaces.
Figma
has a similar story. After the data team set up Hex, the research team was also able to spin up NPS and Product Health programs using the Notebook Agent, which serves as a collaborative partner for users with slightly more technical skill levels.
Evaluate AI capabilities
Every vendor claims AI features now. Most are thin wrappers around chat APIs that generate SQL of questionable quality. Ask pointed questions:
How easy is it to debug or extend an analysis started by an agent?
How easy is it to fix incorrect answers when users report them?
How strong are the observability workflows — can you see and flag incorrect responses?
How easy is it for people to share analytical conversations with the data team?
How well does the tool integrate with the rest of your ecosystem?
See our Head of Product’s full recommendation on
how to evaluate AI analytics tools
.The difference between useful AI and demo-ware is whether it actually knows your data. AI that generates generic SQL isn't much better than asking ChatGPT to write queries. AI that understands your business definitions, your table relationships, and your data quality rules can genuinely accelerate work.
Don't underestimate collaboration
Data work is collaborative
, but most tools force awkward handoffs. The analyst builds something in one tool, exports it, shares via email, gets feedback via Slack, rebuilds with changes, exports again. Hours disappear into coordination overhead.
Look for platforms where multiple people can work simultaneously — where an analyst can build an analysis in the morning and a stakeholder can explore it that afternoon without anyone exporting anything. Real-time collaboration is what lets you move at the speed the business actually needs.
When Infinite Lambda
built an emissions report
for the World Health Organization, they needed both: full technical transparency for data validation, and an intuitive interface for policy stakeholders. The same notebook that let analysts audit every transformation step could be shared as an interactive report, no rebuilding required.
Where cloud analytics is heading
The infrastructure shift is just the foundation. Cloud analytics is evolving toward platforms that integrate AI natively — not as a bolted-on ChatGPT wrapper, but as a core part of how teams interact with data.
Hex
brings cloud infrastructure and
AI-native collaboration
together in one workspace.
Notebook
-based analytics that combine code and no-code in one collaborative workspace. Data scientists write Python and SQL when they need control. Business users interact through natural language when they need answers. Everyone works in real-time together, and no one is left emailing notebooks or wondering which version is current.
The platform connects directly to your cloud data warehouse. No copying data. No security headaches. The analysis happens where the data already lives, with AI assistance built into every workflow.
Try Hex
to see how AI-native notebooks work with your cloud data, or
request a demo
to explore how data teams and business users collaborate in the same environment.
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
