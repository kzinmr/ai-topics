---
title: "What You Need to Know About Tableau Next in 2026"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/tableau-next/"
scraped: "2026-07-18T06:00:57.432696+00:00"
lastmod: "2026-06-19"
type: "sitemap"
---

# What You Need to Know About Tableau Next in 2026

**Source**: [https://hex.tech/blog/tableau-next/](https://hex.tech/blog/tableau-next/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
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
how Mercor unlocked $100M in revenue
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
how Mercor unlocked $100M in revenue
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
how Mercor unlocked $100M in revenue
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
how Mercor unlocked $100M in revenue
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
how Mercor unlocked $100M in revenue
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
What you need to know about Tableau Next in 2026
The TC26 keynote made Tableau Next sound like the future of analytics. The gap between that keynote and what ships today is worth understanding before you commit.
The Hex Team
Data
June 19, 2026
Share:
twitter
linkedin
In this article
What Tableau Next actually is
What migration to Tableau Next involves
What the new pricing model means
The semantic layer Tableau Next needs, and what happens without it
Agentic analytics: announced versus available
Where Tableau Next fits and where the gaps show
Alternatives to Tableau Next
Where to start your Tableau Next evaluation
Frequently asked questions
Get started for free
If you sat through the Tableau Conference 2026 keynote and walked away unsure what you'd actually be buying, you're not alone. Tableau Next has been announced and demoed across recent Salesforce events, and the distance between "here's what's coming" and "here's what ships today" is wide enough that a lot of data teams are confused about what the product is.
That confusion matters if you're mid-conversation with a Salesforce AE, because you're probably being asked to commit to rebuilding your analytics foundation. Before you do, it helps to understand what Tableau Next is, what migrating to it involves, and what the new architecture asks of your team. This guide walks through that honestly, then looks at where Tableau Next fits and where it doesn't, including alternatives worth having in the same evaluation. (If you're
evaluating AI tools
more broadly, the same questions apply.)
What Tableau Next actually is
Tableau Next is a new cloud deployment option for Tableau, built natively on the Salesforce platform. It runs on the Agentforce 360 Platform and is positioned as the first BI platform with a workflow engine connecting the full analytics journey from raw data to insights to action. Salesforce also frames the shift as a move toward business orchestration.
The product identity gets fuzzy because Tableau Next is a separate deployment option from Tableau Cloud and Tableau Server. Tableau Server is the self-managed option and runs on your infrastructure. Tableau Cloud is the managed SaaS option. Tableau Next is a third, distinct option hosted on the Salesforce platform itself.
That architecture depends on three Salesforce components that legacy Tableau never needed. Tableau Next runs on Hyperforce, Salesforce's cloud infrastructure. Its data layer is Data 360 (rebranded from Data Cloud in
October 2025
), and all data must be a Data 360 object. AI interactions route through Agentforce and Einstein.
Existing customers have a reasonable question: Does this retire what I'm already on? Salesforce says existing analytics products will continue to be invested in, and that for many use cases today, the existing products will help you achieve your data and analytics goals. Tableau Next is meant to work alongside them, not replace them overnight.
What migration to Tableau Next involves
For many teams, migration to Tableau Next looks more like re-platforming the data foundation than running a standard software upgrade. The work falls into three areas.
Hyperforce infrastructure migration
Tableau Cloud already runs on Hyperforce infrastructure, and customers must use HTTP/1.1 or higher after migration. Salesforce provides a Hyperforce Assistant tool to check for hard-coded references before you move. The migration uses a Bill of Materials approach, and debugging can take anywhere from a few hours to a few days.
Extract conversion
If you have older workbooks using .tde extracts, this is real work. Starting in
March 2023
, .tde extracts were deprecated, and version 2024.2 is the last that can open them. Upgrading means opening each workbook, selecting Extract > Upgrade, and saving. That functionality only exists in Tableau Desktop 2024.2 and older. New extracts use the .hyper extension.
Data source reconfiguration
This is the heaviest lift. Setup starts with Data 360 configuration, then moves into ingestion or federation patterns and Tableau Semantics. For Server-to-Cloud moves, the Tableau Migration SDK is the recommended tool, but it's API-driven, needs Python or .NET development, and is built for one-time migration events.
Many of the components that make Tableau Next compelling aren't generally available yet. According to
Salesforce's 2026.2 release notes
(June 9, 2026), Personal Orgs, Dashboard Summaries, Admin Insights, Auto Semantic Model Creation, Q&A Calibration, and the Salesforce Connector all remain in Beta. The platform itself is commercially available, but a good number of the experiences that define its value are still shipping.
The TC26 keynote broadly claimed that the demonstrated features were available now. For migration planning, per-feature release status matters more than the keynote framing. Salesforce's own release notes carry a GA date caveat for features described in the document.
What the new pricing model means
Tableau Next uses per-user, per-month pricing billed annually, starting at $40 per user per month according to Salesforce's published pricing. There are two license types: Standard Creator (consume, create, publish) and Standard Consumer (consume only), with at least one Creator needed per deployment.
The $40 starting point sits below Tableau Cloud Standard Creator at $75 per user per month, though the comparison has limits. Standalone Tableau Next excludes Tableau Desktop, Prep Builder, and traditional Tableau Cloud capabilities. The full Tableau+ Bundle that combines Cloud+ and Tableau Next is Contact Sales only, with no published list price.
Unmetered AI usage is a real positive, with a boundary worth understanding. In Tableau Next, unmetered AI covers analytical queries, data transforms, and AI usage, replacing consumption-based Flex credits for those operations.
What's still metered: Data 360 storage and certain other costs, plus Data Cloud Credits consumed by the Audit Trail feature when AI features in Tableau Cloud+ (outside Tableau Next) use it. "Unmetered" applies specifically to Tableau Next, not to every AI feature in the broader bundle.
For total cost of ownership, the confirmed components are per-user licenses, Data 360 storage overage, and Data Cloud Credits for certain features. Third-party estimates exist but aren't official; one analyst source estimates the Tableau+ Bundle at +$100K–$400K over Cloud+ alone. Practitioners have noted the broader concern: when you move from a fixed-cost model to a credit-burning model for AI and Data Cloud features, your BI budget becomes harder to predict. Role-based pricing addresses part of that, but storage and credit consumption still need budgeting.
The semantic layer Tableau Next needs, and what happens without it
Tableau Next's AI value is gated by Tableau Semantics, and this is the most important technical dependency to understand before you commit. Tableau Semantics is a semantic layer deeply integrated with Tableau Next and Data Cloud that translates your data into your business language. Within the stack, Data 360 is the data layer, and Tableau Semantics sits on top as the semantic layer.
This isn't optional plumbing. Tableau's MCP documentation describes the semantic data model as the layer that defines how tables relate, what metrics mean, how KPIs are calculated, and what terminology maps to what fields. When an agent queries through it, it operates at the level of business concepts rather than raw SQL or object fields. The Agentforce for Analytics subagents all depend on this layer.
So what happens when the foundation isn't ready? Without that context, agents provide less accurate responses. Tableau's own framing puts it directly: your semantics are the brains behind AI agents. The broader question of
trusting AI analytics
isn't unique to Tableau Next, but the architectural bet is: if the semantic layer lives inside one vendor's cloud, so does your trust framework.
If you don't already have a well-modeled semantic foundation, you're looking at meaningful investment: Data 360 setup, ingestion pipeline work, and ongoing curation, all before any of the agentic features deliver. This matches what data teams are telling researchers. Hex's
State of Data Teams
2026 report found that no one is questioning the value of semantic models now, but many teams that adopted standalone semantic layers did so specifically fearing vendor lock-in. That tension matters when the semantic layer in question lives inside one vendor's cloud. Hex has taken the opposite position on portability, supporting
open semantic interchange
across tools rather than locking definitions to a single platform.
Agentic analytics: announced versus available
Salesforce describes agentic analytics as a BI approach where agents orchestrate tasks autonomously with humans in the loop. The term is
worth defining carefully
because what ships under the label varies widely across vendors. At TC26, the company announced the Agentic Analytics Platform would evolve Tableau into a decision engine for the agentic enterprise.
Strip the conference language and look at what's GA. (For a practitioner-focused take on what agentic analytics looks like in production, Hex's
agentic analytics playbook
maps the landscape.) The MCP server is generally available, letting AI agents query Tableau's engine. Guided Setup and health monitoring alerts are GA. Several related experiences are still Beta or Pilot, including Tableau Agent in Dashboards, Dashboard Narratives, Q&A Calibration, and Auto Semantic Model Creation.
Practitioner feedback is still anecdotal and more cautious than the marketing. Early adopters have described Tableau Agent as limited, noting that the functionality lags behind the promise of the demos. Public examples of Tableau Next's agentic capabilities remain sparse. Tableau Next may become valuable, but today it remains early, and that distinction matters when you're planning a migration around its differentiators.
Where Tableau Next fits and where the gaps show
Tableau Next targets business users and analysts for
self-serve analytics
. Its core skills are Data Pro (prepare, model, visualize), Concierge (conversational analytics), and Inspector. Its documented asset types are semantic models, vizzes, metrics, and dashboards.
For teams that do analysis in code, there are clear gaps. The official overview does not present Tableau Next as a notebook or Python execution environment. Diagnostic and causal analysis are explicitly unsupported: when asked a "why" question comparing two regions, the Tableau Next Agent responded that root-cause and correlation analysis aren't yet supported. The same review found the Agent performs well for summary and comparison questions, but not yet for diagnostic or predictive insights. (
Analytics agents break differently
than general-purpose LLMs, and these limitations tend to be architectural.)
When deeper analysis is needed, the documented path is to leave Tableau Next and work in Cloud or Desktop via a connector. That design choice makes sense for a presentation and self-service layer, but teams doing SQL, Python, and notebook-based work will need another environment for that analysis.
That gap, combined with the migration reality, is why the evaluation window is worth keeping open. If you're rebuilding your analytics foundation anyway, it's a fair moment to ask whether that foundation should live inside one vendor's cloud at all.
Alternatives to Tableau Next
Hex
The most direct contrast with Tableau Next's architecture is the question of where your data lives. Tableau Next routes everything through Data 360 as a mandatory abstraction layer. Hex is an
AI-native analytics
platform that works directly on the warehouse you already have. If the migration question is "do I want to route my analytics through a new vendor's data layer," Hex is the answer that says you don't have to.
Hex connects directly to Snowflake, Databricks, BigQuery, and ClickHouse with Tier 1 support and enforces user-specific
data connections
from the warehouse itself via OAuth. The access controls your team already manages stay in place.
Where Tableau Next splits self-service and deep analysis into separate tools, Hex keeps them in one connected workspace. The Notebook Agent handles deep analysis in
agentic notebooks
: generating SQL and Python, building charts, and chaining multi-step analyses.
Threads
handles conversational self-serve, letting business users ask plain-language questions with multi-step reasoning and follow-ups. Think of it as
natural language BI
backed by governed context rather than a generic chatbot. Technical users can inspect and edit every query the AI generates, so analysis stays reviewable rather than a black box. Every Thread is backed by an inspectable notebook, so AI outputs become editable, publishable assets rather than one-time answers.
On the semantic layer question that makes Tableau Next's setup so heavy, Hex takes a different approach. Teams don't need a fully modeled semantic layer before AI delivers value. You can start by endorsing key tables and adding warehouse descriptions, layer in workspace rules, then deepen into full semantic models authored in Hex or synced from dbt, Snowflake, or Cube via
semantic model sync
.
Context Studio
closes the loop by surfacing where agents hit quality issues and where context gaps exist. That progressive path means teams can start getting value from AI today and invest in governance depth over time, rather than treating a full semantic layer as a prerequisite.
This played out at Topline Pro, where only the operations team knew Tableau. Every data request flowed through them, business users were blocked, and the Ops team was overwhelmed. After
switching to Hex
, PMs comfortable with SQL but lacking schema confidence started investigating issues in minutes using the Notebook Agent. Work that had taken tickets, hours of collaboration, and days of turnaround collapsed to minutes. Teams across skill levels, from PMs to analytics engineers, now work in the same environment.
Ramp's AI adoption
tells a similar story: the team consolidated from multiple tools into a single workspace where applied AI, analytics, and business stakeholders collaborate side by side.
Two tradeoffs worth weighing. Teams whose entire stack is already inside Salesforce may find that a warehouse-native tool adds a connection point they'd otherwise consolidate. But the flip side is that your analytics layer isn't locked inside an ecosystem whose primary focus isn't analytics and whose product velocity reflects that sprawl. And pixel-perfect static enterprise reporting isn't Hex's primary focus: it's built for exploration, AI-assisted analysis, and
interactive data apps
, which means the product moves faster on the capabilities that actually change how teams work with data.
Hex offers tiered pricing with plans for individuals, teams, and
Hex Enterprise
. See
Hex pricing
for current plan details.
Tableau Cloud
Tableau Cloud is Tableau's fully hosted SaaS deployment, and the key difference from Tableau Next is architectural: it doesn't route data through Data 360 or sit on the Salesforce platform. Your existing Tableau workbooks, data sources, and connectors carry over without re-platforming. It remains an actively invested product with its own roadmap and is the lower-friction path for teams already on Tableau who aren't ready to rebuild their data foundation.
Tableau Cloud delivers the mature visualization and dashboarding experience Tableau is known for, with the full Tableau Desktop and Prep Builder authoring tools included in Creator licenses. Tableau Pulse provides KPI change summaries, and the Cloud+ Edition adds Tableau Agent for conversational analytics. For Server customers, moving to Tableau Cloud can be a stepping stone before considering Tableau Next.
The tradeoff: Tableau Agent for Cloud is gated by tier. Standard and Enterprise editions don't include it; only Cloud+ does. And native code-first workflows remain limited, with SQL and Python work happening largely outside the core product.
According to Salesforce's published pricing, Tableau Cloud Standard Edition runs $15/user/month (Viewer), $42 (Explorer), and $75 (Creator). Enterprise Edition runs $35, $70, and $115, respectively. All prices are per user, per month, billed annually.
Tableau Cloud fits teams committed to Tableau's visualization strengths who want managed hosting without the Data 360 dependency that Tableau Next introduces. Teams doing heavy code-first analysis or wanting fully unmetered AI will find the tiered gating and per-seat costs limiting.
Tableau Server
Tableau Server is Tableau's self-hosted, on-premises deployment. It remains supported with its own roadmap and suits organizations with strict data residency or security constraints that rule out fully hosted options. You get complete control over hosting, network configuration, and data residency, but infrastructure costs, patching, and scaling are your responsibility.
Newer AI and agentic features are cloud-first, and practitioners have noted that Server customers should plan to migrate to Tableau Cloud as a stepping stone before considering Tableau Next. Tableau Agent in Server also needs you to bring your own LLM.
Tableau Server supports role-based Creator, Explorer, and Viewer licensing alongside a core-based option. Infrastructure and operational costs are separate.
Tableau Server fits organizations with data residency or air-gap constraints that make hosted SaaS a non-starter. Teams wanting the latest agentic features or lower operational overhead are better served by a cloud option.
Where to start your Tableau Next evaluation
Tableau Next is a purchasable product built around consolidating analytics into the Salesforce platform alongside CRM and AI. But much of the offering isn't out of beta yet, and there's little publicly available user feedback to help purchasers evaluate what they're committing to. The features that are available are gated behind a Data 360 and Tableau Semantics foundation that takes real work to build. If you're being asked to commit to that migration, you're being asked to re-platform your analytics onto one vendor's cloud while several of the headline features are still shipping.
Your analytics stack doesn't have to live inside one vendor's cloud just because your CRM does. If you're rebuilding your analytics foundation anyway, the window is already open. Hex works on the Snowflake, Databricks, BigQuery, ClickHouse, and dbt investments you've already made, with a connected workspace where a Thread flows into a Notebook Agent analysis and out to a published app. The
Tableau vs Hex
comparison maps the differences in detail. You can start lightweight, sync your existing dbt models, and deepen context over time.
Request a demo
to see how Hex works on your existing stack.
Frequently asked questions
What's the difference between Tableau Next and Tableau Cloud?
Architecture. Tableau Cloud is Tableau's managed SaaS deployment, hosted on Hyperforce, that connects to your existing data sources and carries over your current workbooks and connectors. Tableau Next is a separate deployment built natively on the Salesforce platform, where all data must route through Data 360 and AI features run through Agentforce. Cloud includes Tableau Desktop and Prep Builder in Creator licenses; standalone Next does not. Cloud gates AI features by tier (Tableau Agent is Cloud+ only), while Next includes unmetered AI for analytical queries. The practical difference: moving to Tableau Cloud is a hosting migration, while moving to Tableau Next is a re-platform of your data foundation.
Is Tableau Next replacing Tableau Cloud and Tableau Server?
No. Salesforce says existing analytics products, including Tableau Cloud, Tableau Server, and CRM Analytics, will continue to be invested in. Tableau Next is a third deployment option built to work alongside the others rather than retire them. If you're on Tableau Server, the recommended migration path is to move to Tableau Cloud first before evaluating Tableau Next, since the newer AI capabilities are cloud-first. The products have distinct architectures and licensing, so the choice depends on your team's constraints and where you want your data layer to live.
How much of Tableau Next is actually available versus still in beta?
The platform is commercially available, but feature availability is mixed. As of the 2026.2 release (June 9, 2026), Personal Orgs, Dashboard Summaries, Admin Insights, Auto Semantic Model Creation, Q&A Calibration, and the Salesforce Connector are all Beta. Tableau Agent in Dashboards is Beta in Cloud and Pilot in Server. The Tableau Next MCP server and Guided Setup are GA. When planning a migration, the per-feature release notes are a more reliable guide than keynote claims, since Salesforce's own notes caution that demonstrated features don't become generally available until an announced GA date.
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
🔊
🎧
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
