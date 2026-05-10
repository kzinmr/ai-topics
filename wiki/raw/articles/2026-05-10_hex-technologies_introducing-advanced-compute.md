---
title: "Introducing Advanced Compute Profiles | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/introducing-advanced-compute/"
scraped: "2026-05-10T01:28:56.600375+00:00"
lastmod: "2024-12-12"
type: "sitemap"
---

# Introducing Advanced Compute Profiles | Hex 

**Source**: [https://hex.tech/blog/introducing-advanced-compute/](https://hex.tech/blog/introducing-advanced-compute/)

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
Introducing Advanced Compute Profiles
Powerful compute to power data science and ML workflows
Jo Engreitz
Product
December 12, 2024
Share:
twitter
linkedin
In this article
New power for your most complex workflows
Only pay for what you use
Bring it all together in Hex
Get started for free
One of the magical things about Hex is its
"multi-modality"
– the ability to stitch together various ways of working with data into one platform.
Our unique compute architecture
makes this possible by expressing all cell types as interoperable “lazy dataframes“ that can be executed across different backends, including our DuckDB-powered in-memory engine,
pushed down to a data warehouse
, or in the Python kernel. This flexibility means you aren't constrained to the Python kernel's memory if you're working in SQL or no-code.
But many data science and ML workflows do require more kernel compute. Model training, for instance, can involve massive training datasets and often benefits from distributing training jobs across multiple cores to speed iteration cycles. Our original 8GB RAM, single-CPU compute profile isn’t always up to the task.
New power for your most complex workflows
That’s why we’re introducing Advanced Compute Profiles in Hex. Now Team and Enterprise customers have access to more firepower – up to “4XL” (16 CPUs and 128GB RAM) and “V100 GPU” (1 V100 GPU, 16GB GPU RAM, 6 CPUS, 56GB CPU RAM).
Together with our warehouse, S3, and Google Drive integrations, advanced compute gives you everything you need to take on model development (or any compute-intensive workflow) from the comfort of your Hex notebook. No need to export millions-of-rows datasets to another tool or struggle with environment reconfiguration.
Advanced Compute Profiles in Hex come with a new “idle timeout” setting, which adjusts how long notebook kernels stay alive after the project run has completed. You can reduce it down to 15 minutes if you’re already pickling or writing your Python state to CSVs and looking to minimize compute costs — or if you need a longer grace period, you can extend idle timeout up to 24 hours.
This is just one of many options for powering compute-intensive workflows in Hex.
Snowpark ML
and
Modelbit
, for instance, are two great solutions that we’ll continue to support, among others. You can also mix-and-match: for example, use out-of-the-box Hex advanced compute to quickly prototype and test different models, features, and training datasets, before pushing the end result to another system to run inference workloads.
Only pay for what you use
Advanced compute is charged on a simple, pay-per-minute model. Need the firepower? Up the compute profile size and get to work. Done with the heavy stuff? Scale down, or stop your kernel and your bill will too!
Of course, we also built new Admin controls to ensure predictable spend and observability. Admins can set per-billing cycle spend limits, view detailed usage logs, and restrict advanced compute access to certain user groups (for example, your data science team). For more details on all of this,
check out our docs.
Bring it all together in Hex
Our new compute options help you minimize tool sprawl and streamline your advanced data science and ML workflows. It's easy to set up, effortless to collaborate, and makes iterating on resource-intensive projects fast.
Admins can enable advanced compute for their workspace in
Settings > Compute
.
Advanced compute profiles are only available on Team and Enterprise plans.
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
