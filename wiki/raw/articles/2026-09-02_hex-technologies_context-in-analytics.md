---
title: "Context in Analytics: Turning Raw Data Into Actionable Insight"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/context-in-analytics/"
scraped: "2026-09-02T06:00:20.965098+00:00"
lastmod: "2026-08-13"
type: "sitemap"
---

# Context in Analytics: Turning Raw Data Into Actionable Insight

**Source**: [https://hex.tech/blog/context-in-analytics/](https://hex.tech/blog/context-in-analytics/)

Skip to main content
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
Blog
Context and analytics: how it works and why AI makes it essential
Your dashboards show the numbers. Contextual analytics is what makes those numbers trustworthy.
The Hex Team
Data
August 13, 2026
Share:
twitter
linkedin
In this article
What context actually means for analytics
Why tool sprawl destroys context
Why AI makes context the bottleneck
What changes when data teams invest in building context on their data
How context compounds at scale
Getting started
Frequently Asked Questions
Get started for free
You've seen the dashboards. Dozens of them, maybe hundreds, scattered across your organization. Each shows metrics. Each is technically accurate. And each somehow fails to tell anyone what's actually going on.
Our view: the problem was never a shortage of data or dashboards. It's a shortage of context. When someone looks at a metric, they should be able to trust it, to understand what it means, where it came from, and why it matters for the decision they're trying to make. In Hex's
State of Data Teams
2026 report, 31% of data leaders cite trust as their top concern with AI adoption, nearly twice any other response. Not because the data is missing, but because the meaning around it is.
That's what contextual analytics addresses: the practice of ensuring that metrics carry their definitions, lineage, quality signals, and business rules wherever they go, so the people and AI systems consuming them can act with confidence.
What context actually means for analytics
Context in analytics shifts from observing metrics in isolation to understanding the environment around them. It means seeing that customer acquisition cost spiked
and
knowing which definition of CAC you're looking at, how it was calculated, what channels it includes, and whether the underlying data is reliable.
Traditional reporting gives you the
what
. Contextual analytics adds the
why
, the
how
, and the
according-to-whom
.
In practice, that means several layers working together that usually live in separate places: semantic context (what terms actually mean), lineage context (where data came from and how it was transformed), operational context (quality signals and reliability indicators), and policy context (privacy regulations, compliance constraints, and usage rules). When these layers work together, both you and the AI tools you're using can reliably interpret and act on your data.
Traditional data stacks operate in distinct horizontal layers: storage, transformation, visualization. Each does its job, but none carries business meaning across boundaries. A context layer cuts vertically through all of these: the business understanding that travels with the data wherever it goes.
Why tool sprawl destroys context
The deeper problem with fragmented tool stacks goes beyond coordination cost. It's what happens to business logic when it crosses tool boundaries.
When a finance analyst defines "active user" in one system, a product manager calculates it slightly differently in another, and a data scientist uses a third interpretation in their notebook, you don't have a tooling problem. You have a context destruction problem. Each tool boundary becomes a place where meaning gets lost, assumptions go undocumented, and definitions drift.
Even sophisticated transformation frameworks can't fully prevent this. Data teams often find that fragmentation creeps in even with tools like dbt, and it's hard to pinpoint where things diverged. The transformation layer handles technical execution well, but it can't bridge context gaps created by architectural isolation.
At a certain point, you stop solving data problems and start managing the tools that were supposed to solve them.
Why AI makes context the bottleneck
Large language models (LLMs) are changing how people interact with data, but they have a limitation worth understanding: they don't inherently know what your data means.
When an LLM encounters "churn rate" in a query, it doesn't know whether you mean logo churn, revenue churn, trailing-30-day churn, or cohort-based churn. Without explicit guidance, it generates responses based on patterns in its training data: responses that look authoritative but aren't grounded in your business definitions. This is hallucination applied to analytics, and it's dangerous precisely because the outputs look right.
The risk is predictable. The same metric term can mean different things to different teams, and without semantic context specifying which interpretation applies, AI fills the gap with training-data assumptions. Human analysts face the same ambiguity, but at least they know to ask. LLMs don't. And when LLMs write SQL without understanding your underlying relationships and business rules, the queries are syntactically valid but semantically wrong. They run fine. The answers just aren't yours.
Governed context layers address this directly. When a semantic model provides one authoritative definition of "churn rate," the AI queries that definition rather than guessing its way to a plausible-but-wrong answer. When business rules are documented as constraints, the model operates within verified logic rather than inferring from statistical patterns alone. That's why many teams now treat the context layer as table stakes for
AI analytics
trust rather than a nice-to-have abstraction.
What changes when data teams invest in building context on their data
McKinsey research
suggests only about one in three companies achieve AI at scale, with the majority remaining in experimenting or piloting stages rather than systematically integrating these technologies across the enterprise. Contextual analytics addresses the root cause of that gap: you can't scale AI-driven insights if the AI doesn't understand your metrics.
When you invest in context (governed semantic models, shared metric definitions, quality signals), the work changes. Instead of building every report yourself, you're building the models and
governance practices
that make self-service actually work. The conversations with stakeholders shift from "what do you need built?" to "which metrics matter most, and how do we make them accessible?"
This played out at
Calendly
, where the data team built a Standardized Metric Library in Hex as company-wide KPI documentation. That single source of truth now helps tie-break conflicting reports and ramp new analysts faster.
The shift matters just as much for the people asking those questions. Direct access within governed frameworks replaces ticket submission and waiting. Stakeholders can explore data, refine their thinking iteratively, and ask follow-ups without filing a new request each time. When your involvement is needed, the full exploration context is right there, not lost in an email thread.
How context compounds at scale
The architectural pattern that makes contextual analytics work is hub-and-spoke: a centralized context layer as the hub, with metric definitions accessed by whatever tools people use. You define "customer lifetime value" once, and every notebook, dashboard, conversational interface, and AI agent queries the same definition. When governance is part of the context layer itself (access controls, lineage, quality standards), it becomes something the system enforces rather than something you maintain through process.
The compounding effect is what sets this apart. Every question someone asks, every metric definition your team creates, every business rule you document becomes part of the shared context that future queries draw on. Disconnected tools can't accumulate this signal because it's scattered across silos.
Context Studio
makes this compounding visible: it surfaces which questions are being asked, where context is thin, and where the next improvement will have the most impact. Each interaction makes the next answer a little more grounded.
Hex integrates
semantic authoring
directly into this workflow. When someone asks a question, the AI draws on your database schemas, team-defined metrics, documented business rules, and previous analytical patterns, all visible to you, all improvable. Analysts can go deep in agentic notebooks with SQL and Python, or stakeholders can get a quick answer through natural language in
Threads
. The Semantic Model Agent helps build the semantic context that governs everything. And because all of this happens in one workspace, every question asked and every definition created compounds. Future answers get more accurate in ways that disconnected tools can't match.
Getting started
Investing in context for your data is a decision to treat business meaning as infrastructure rather than documentation.
You don't need a full context layer on day one. Start by endorsing your most important tables, adding warehouse descriptions, and setting workspace rules. Build semantic models for the metrics that cause the most confusion. Layer in lineage tracking and observability as your needs become clearer. Go deeper over time as usage patterns reveal where context gaps hurt most.
The data exists. What's usually missing is the systematic habit of attaching meaning and trust to it. When your code, logic, and visualizations share the same trusted context, you spend less time translating between tools and more time on the work that actually matters.
Sign up for Hex
or
request a demo
to see how it works.
Frequently Asked Questions
Do we need a full semantic model before contextual analytics delivers value?
No. Start with endorsed tables and warehouse descriptions so AI agents know which data to trust. Add workspace rules for the terms that cause the most cross-team confusion. Semantic models formalize metric definitions for higher-stakes use cases as adoption grows. Each layer of context you add makes every answer more consistent, and you can start seeing value from the lightest layers immediately.
How is contextual analytics different from data governance?
Data governance defines the policies: who can access what, how data should be handled, and what compliance requirements apply. Contextual analytics makes those policies actionable at the point where questions get asked. It attaches definitions, lineage, and quality signals directly to the data so that both people and AI systems can interpret metrics correctly without needing to consult a separate governance document. The two are complementary: governance without context lives in a wiki nobody reads, and context without governance has no authority behind it.
What's the fastest way to see whether context gaps are hurting our analytics?
Look at how often your team fields the same clarifying questions: "which revenue number is this?" or "does this include returns?" Those recurring questions are context gaps. Context Studio surfaces this pattern systematically by showing which questions users ask, where the AI's answers lack confidence, and where adding a definition or endorsing a table would have the most impact. Start there rather than trying to document everything upfront.
Share:
twitter
linkedin
Get "The Data Leader’s Guide to Agentic Analytics"  — a practical roadmap for understanding and implementing AI to accelerate your data team.
Download
Request a demo
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
✨
🔊
🎧
🌊
🍀
🤠
🎷
on
🌎
.
Company
About
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
You have opted out of data tracking
