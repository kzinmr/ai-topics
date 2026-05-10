---
title: "What is embedded analytics? Types, architecture & uses | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/embedded-analytics/"
scraped: "2026-05-10T01:27:11.662042+00:00"
lastmod: "2025-12-12"
type: "sitemap"
---

# What is embedded analytics? Types, architecture & uses | Hex 

**Source**: [https://hex.tech/blog/embedded-analytics/](https://hex.tech/blog/embedded-analytics/)

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
What is embedded analytics?
How to integrate data analysis directly into your applications
The Hex Team
Data
December 12, 2025
Share:
twitter
linkedin
In this article
What is embedded analytics?
Types of embedded analytics
How embedded analytics works
How you can use embedded analytics
The future of embedded analytics is AI-native
Get started for free
Your team
needs data
to make decisions — but they're stuck bouncing between tools. They export from one system, log into another, and wait for dashboards that are already stale by the time they load.
Sound familiar?
Embedded analytics
solves this by putting analysis directly into the applications people already use. No context switching, waiting on the data team, or separate logins to slow your team down
This guide covers what embedded analytics is, the different types, how it works under the hood, and how AI-native platforms like
Hex
are changing what's possible.
What is embedded analytics?
Embedded analytics
is the integration of data analysis capabilities directly into the applications your team already uses, so they can explore data, generate insights, and make decisions without switching to separate tools.
Instead of pulling data out of your systems, transforming it somewhere else, and presenting it in yet another tool, embedded analytics keeps everything in context. Users ask questions and get answers where they already work. The analytics live inside your product, not adjacent to it.
This accessibility matters for everyone who touches data. With embedded analytics, your sales rep can check pipeline metrics inside the CRM, your product manager can see cohort analysis right in the admin dashboard, your data scientist builds a model in Python, and stakeholders can explore the results without scheduling a meeting or asking for a walkthrough.
Business users get self-service, data teams escape the request queue, and nobody has to wait for someone to "get to it."
Types of embedded analytics
Where you embed analytics influences almost everything, including your security approach, how much customization you need, and how well the system scales. In practice, there are three main ways teams embed analytics:
Internal embedded analytics
: Reports and KPIs embedded directly into employee-facing tools like CRMs, ERP platforms, and intranet portals. Designed for internal decision-making without context-switching between systems.
Customer-facing embedded analytics
: Customers see their own usage metrics, benchmarks, and reports without leaving your app. Candidly is a great example of
how embedded analytics empowers users
.
Partner and portal embedded analytics
: Controlled access for external stakeholders like suppliers, distributors, or franchisees through dedicated portals. Partners see only their data, governed by your security model.
The type you choose determines your
architecture decisions
, particularly around authentication, multi-tenancy, and data isolation.
How embedded analytics works
Under the hood, embedded analytics enables authentication that respects your existing security, query processing that keeps tenants isolated, and UI rendering that feels native. Here's how it works:
Authentication
Embedded analytics needs to know who the user is and what they're allowed to see. This typically happens by passing user context (identity, role, permissions) from your application to the embedded component through secure tokens or API calls. Users never see the handoff; they just see dashboards that work.
Semantic layers
A semantic layer sits between your raw data and the people asking questions. It translates database structures into terms that business users actually understand. When someone asks for "midwest revenue," the semantic layer knows exactly which tables and columns that means. No SQL required.
Query optimization
Analytical queries behave differently from transactional ones. Embedded analytics platforms handle this with execution mode optimization, parallel processing, and execution plan caching.
Multi-tenant security
Security is enforced at the data layer, not just the UI. Before any SQL runs, the system checks which tenant owns the session and automatically appends the right filters. Customer A never sees Customer B's data. Security is built into the data itself, not around it.
How you can use embedded analytics
The real test is whether embedded analytics actually changes how your teams work. Here's where it tends to make the biggest difference:
Operational decision-making
Embedded analytics puts real-time metrics directly into operational tools like CRMs, support platforms, supply chain systems, and marketing dashboards. Teams see what's happening as it happens, without switching contexts or waiting on reports. The cycle from question to action shrinks from days to minutes.
Product intelligence
Embedded analytics surfaces feature adoption, error rates, and user behavior directly in the tools teams use to build and
launch products
. Instead of pulling reports from a separate BI tool after the fact, teams see what's happening in real time, alongside the deployment tools, admin dashboards, and monitoring systems where they already work.
Customer enablement
Embedded analytics turns data into a product feature. Customers access their own usage patterns, benchmarks, and reports directly inside your app without submitting support tickets or waiting on custom reports. Self-service analytics reduces support load while giving customers the insights they expect from modern software.
Compliance and audit workflows
Embedded analytics integrates compliance metrics and audit trails directly into risk management and documentation systems. Instead of compiling data from multiple sources for regulatory reporting, teams work from a single, always-current view. Audit trails get cleaner and reporting gets more reliable.
The future of embedded analytics is AI-native
AI is
shifting how all of this works
, and fast. But here's the thing: not all so-called “AI-powered analytics tools” are built the same.
Some platforms bolt AI on top of existing architecture. It works — sort of. But the AI doesn't really understand your data model. Doesn't know your security rules. Doesn't get that "revenue" means something different in your company than the generic definition. You end up babysitting it constantly.
Hex
is different. It's an AI-powered analytics platform that unifies notebooks, data apps, and natural language exploration in one workspace. And AI is built into the architecture from the start. That means it can understand your metric definitions, respect row-level security automatically, and generates SQL your technical users can actually inspect and refine.
The result? Your data scientists and analysts work in
collaborative Notebooks
. Your business users ask questions in natural language
Threads
. Everyone accesses results through the same embedded interface. No more emailing notebook files back and forth, no more "which version is this," and no more rebuilding the same analysis in three different tools.
That's the real AI shift, and it's already happening.
Try Hex free
to see how AI-native architecture changes what's possible, or
request a demo
to walk through implementing embedded analytics with your team.
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
