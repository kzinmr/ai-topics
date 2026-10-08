---
title: "Best BI tools for Snowflake Semantic Views"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowflake-semantic-views/"
scraped: "2026-10-07T06:00:33.401604+00:00"
lastmod: "2026-10-01"
type: "sitemap"
---

# Best BI tools for Snowflake Semantic Views

**Source**: [https://hex.tech/blog/snowflake-semantic-views/](https://hex.tech/blog/snowflake-semantic-views/)

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
Best BI tools for Snowflake semantic views
Snowflake Semantic Views give AI agents governed business context to reason over. The right BI platform should help you get as much leverage as possible from that investment.
The Hex Team
Data
October 1, 2026
Share:
twitter
linkedin
In this article
What compatibility with Snowflake Semantic Views actually needs
The best BI tools for Snowflake semantic views
Choose a BI tool that maximizes your Snowflake Semantic Views investment.
Frequently Asked Questions
Get started for free
Snowflake is increasingly more than the warehouse where your data lives. With products like
Semantic Views
, Snowflake is also becoming a place where teams define the business context that applications and AI agents use to understand that data.
Snowflake Semantic Views are schema-level objects that define metrics, dimensions, facts, and entity relationships directly in Snowflake's
warehouse architecture
. The data definition language became generally available at Summit 2025, and standard SQL querying followed in 2026. Cortex Analyst can generate SQL from the same object.
That means governed definitions can live close to the underlying data and become available to multiple downstream tools, instead of being rebuilt independently inside every BI platform. This shared-definition model is part of what makes
open semantic interchange
increasingly important in the AI era.
And the timing matters. As
frontier models get better at real-world data analysis
, the limiting factor is increasingly the context they have access to, not simply whether they can generate SQL.
At the same time, better model capability doesn't solve the trust problem on its own. Hex's
State of Data Teams
research found AI quickly rising as a priority for data leaders, while 31% cited data quality and lack of trust as their biggest barrier to AI adoption.
That combination is exactly why Semantic Views matter. As agents become more capable, the quality and portability of the business context they can reason over becomes more important.
For teams investing in Snowflake Semantic Views, that creates an important downstream question:
which analytics platform will give that context the most leverage?
Connecting to Snowflake is table stakes. Even technical support for Semantic Views only tells you part of the story. The real evaluation is whether a platform preserves Snowflake as the source of truth, makes those definitions useful across a broad set of analytics and AI workflows, lets agents supplement them with other trusted context, and gives the data team a feedback loop for improving answer quality over time.
What compatibility with Snowflake Semantic Views actually needs
The differentiator isn't simply whether a tool can connect to Snowflake. It's what happens to the context you've built once that connection is made.
Does it read metric definitions or just tables?
A standard connector can see base tables without necessarily understanding the metrics and relationships you've defined. Some tools query or sync Snowflake Semantic Views directly. Others import a copy or ask you to recreate logic in DAX, LookML, YAML, or another proprietary layer. If Snowflake is where you've chosen to maintain governed metrics, understand whether it remains authoritative or whether you now own two definitions that can drift.
Does Snowflake governance carry through?
Snowflake evaluates row-access and masking policies at query time against the identity and role associated with the session. Per-user OAuth can allow each viewer's query to run under their own Snowflake identity, while extracts and shared service accounts behave differently. If the point of the Semantic View is governed reuse, make sure the BI layer doesn't weaken the governance underneath it.
How broadly can you use the context you've built?
If you've defined revenue, customers, dimensions, and relationships once, those definitions should ideally support more than a single chat experience. Can they ground self-service questions? Dashboard and app building? Deeper analysis? Slack? MCP and external agents? The more workflows that can draw from the same context, the more leverage you get from your investment.
Can the Semantic View sit alongside other business context?
Metrics and modeled relationships are important, but they won't contain everything an agent needs to answer every question. Useful context also lives in warehouse metadata, documentation, business terminology, code, endorsed assets, and existing analysis. Pressure-test whether the Semantic View is one powerful source of context or the boundary of what the agent can understand.
Can usage help you improve the model?
Once people start asking questions against your Semantic Views, they're generating valuable signals about what's missing. Which questions fail? Which definitions create ambiguity? Which relationships keep coming up? Look for platforms that help the data team observe real-world usage, identify context gaps, run evals, and validate improvements instead of relying on manual log review.
Those are the criteria that matter if you're investing in Snowflake Semantic Views as part of a broader AI analytics strategy.
The best BI tools for Snowflake semantic views
Hex
Hex is an
AI analytics platform
spanning
conversational self-service analytics
, dashboards and
data apps
, and deeper analysis. Hex was an early partner for
Snowflake Semantic Views
, and
Semantic Model Sync
lets teams bring Snowflake-defined models, dimensions, measures, and relationships into Hex while keeping Snowflake as the source of truth.
Key features
Hex's
Semantic Model Sync
can bring definitions maintained in Snowflake into Hex's broader semantic layer, with dedicated support for
Snowflake Semantic Views
. Those definitions can then be used in
Threads
,
semantic-model exploration
, notebooks, and published apps.
That gives the work invested in Snowflake more places to create value instead of limiting it to a single consumption surface. Business users can ask questions in natural language, analysts can continue into SQL or Python, and the same analytical capabilities can extend into external agent workflows through the
Hex MCP server
, including tools like Claude, Cursor, ChatGPT, and Codex.
For questions that require more than modeled metrics and relationships, Hex can also draw on other forms of organizational context through
Context Management
, including
Guides
,
Endorsements
, warehouse metadata, reference repositories, and existing analytical assets. That lets Semantic Views remain an important governed foundation without requiring every question to fit inside the model.
Context Studio
closes the loop by giving data teams visibility into what people are asking, where agents perform well or struggle, and which context sources need improvement over time.
Pros
Hex's strengths center on governed context and BI workflows that stay connected end to end.
Snowflake Semantic Views can support self-service, dashboard/app building, deeper analysis, and external agent workflows from the same context.
Business users can ask questions in plain language while analysts retain access to inspect and extend the underlying work.
Guides
,
Endorsements
, and other context can sit alongside Snowflake definitions instead of requiring every instruction to be encoded inside the semantic model.
Context Studio
provides an improvement loop around real-world usage, answer quality, and context gaps.
Per-user Snowflake OAuth can preserve user-level permissions so row-access and masking policies continue to apply when people query through Hex.
Cons
Rollout planning needs to account for beta coverage and pricing visibility.
The sync is beta and covers standard aggregations; derived metrics, inner joins, and filters defined in the view aren't supported yet.
Hex doesn't publish Explorer seat pricing, so sizing the read-only side of a rollout means a conversation with sales.
Pricing
Hex pricing
lists a free Community plan, Professional at $36 per Editor per month, Team at $75 per Editor per month, and custom Enterprise. Semantic models and OAuth database connections start on Team; Enterprise adds audit logs, OpenID Connect (OIDC) single sign-on (SSO), bring your own key (BYOK), and a single-tenant option.
Who is Hex best for?
Hex is a strong fit for teams that want to use Snowflake Semantic Views as part of a broader AI analytics strategy: self-service analytics questions, dashboards and apps, deeper analyst workflows, and external agents all drawing from the same governed context.
Omni
Omni
is a semantic-model-first BI platform with a bidirectional integration for Snowflake Semantic Views. Snowflake Semantic Views can be brought into Omni as Topics for exploration and AI, while Omni Topics can also be published back to Snowflake as Semantic Views.
Key features
When a Snowflake Semantic View is imported, Omni creates a corresponding Topic using its fields, relationships, and supported AI instructions. Changes made in Snowflake can be pulled into Omni through subsequent schema refreshes.
Omni's semantic layer then sits on top of that imported context, allowing teams to add metrics, relationships, and additional AI context inside Omni. Its AI evaluation tooling lets teams test representative questions against that model before changes are deployed.
Omni also supports the reverse path, allowing teams to push an Omni Topic to Snowflake as a Semantic View.
Pros
Bidirectional integration gives teams flexibility to bring Snowflake Semantic Views into Omni and publish Omni-modeled definitions back to Snowflake.
Per-user OAuth can preserve Snowflake permissions and row-level security for individual users.
Omni’s eval tooling gives data teams a structured way to test how the agent answers known questions before model changes ship.
Strong fit for teams that want a governed, semantic-model-first BI workflow.
Cons
Bidirectional modeling can create ambiguity around which system is authoritative. If metrics are extended independently in Snowflake and Omni, teams can end up maintaining conflicting definitions across the two layers.
Filters still need Omni-side YAML (bind_to) even for fields sourced from a Snowflake semantic view, so the semantic view gets you started but Omni's own modeling language is where most day-to-day definition work still happens — a soft lock-in on top of the warehouse object, not a replacement for it.
Omni’s AI is constrained to the Topics, relationships, and context defined in its semantic model. As users ask more open-ended questions, the data team may need to keep expanding that model to maintain coverage, increasing the modeling burden over time.
More advanced or exploratory analysis sits outside Omni’s core BI workflow, so teams may still need another environment when analysis goes beyond modeled BI use cases.
Pricing
Omni does not publish plan prices, so every plan starts with a sales conversation.
Who is Omni best for?
Omni is a strong fit for teams that want a semantic-model-first BI workflow and value being able to move definitions between Snowflake and Omni. If the goal of investing in Snowflake Semantic Views is to create a portable context layer across analytics and AI tools, test how much additional modeling ends up living in Omni and how the two systems stay aligned as definitions evolve.
Sigma
Sigma
is a warehouse-native BI platform built around a spreadsheet-style interface. Its Snowflake Semantic Views integration lets teams work with warehouse-governed definitions through Sigma's familiar workbook experience.
Key features
Sigma queries Snowflake live, and its Semantic Views integration can expose Snowflake-defined metrics for exploration without requiring teams to recreate the same metric definition inside Sigma.
Sigma also supports per-user Snowflake OAuth, allowing queries to run under an individual's Snowflake identity and existing warehouse permissions.
For AI workflows, Sigma Assistant helps users explore data and work inside the workbook experience. Sigma can also connect to warehouse-native AI capabilities, while Input Tables support write-back for planning and operational workflows.
Pros
Direct access to Snowflake Semantic Views helps preserve Snowflake-defined metrics without requiring a second metric definition in Sigma.
Live warehouse querying and per-user OAuth fit naturally with Snowflake-centric governance.
Spreadsheet-style interaction is familiar to business users and analysts already comfortable with Excel-like workflows.
Write-back supports planning and operational use cases that extend beyond passive reporting.
Cons
Sigma's core experience still centers on workbooks and spreadsheet-style interaction, so teams should test whether AI materially expands adoption beyond existing power users.
As users move from an initial AI question into deeper exploration or building, the workflow can still depend on workbook and formula concepts.
Sigma's AI capabilities span multiple surfaces, so teams should understand how context and governance remain consistent across them.
Usage and feedback reporting provide visibility into AI activity, but teams should pressure-test how they identify the context behind weak answers, make improvements, and validate those changes over time.
Pricing
Sigma publishes no per-user prices; its pricing process routes to a contact form, and the four-tier licensing model launched without published rates: View, Act, Analyze, and Build.
Who is Sigma best for?
Sigma is a strong fit for Snowflake-centric teams that want live warehouse access and spreadsheet-style self-service. If company-wide AI self-service is the goal, test how far non-spreadsheet users can get without being forced back into traditional BI workbook workflows.
Tableau
Tableau is enterprise BI with visualization and governance tooling and published per-user pricing. Its Snowflake Semantic Views path is an export workflow rather than a native read. You call SYSTEM$EXPORT_TDS_FROM_SEMANTIC_VIEW('schema.view_name') in Snowflake, get a .tds file, and open it in Tableau Desktop, which then connects live to the semantic view through the Tableau Data Source (TDS) export workflow. In public preview, the export produces a point-in-time file, so you re-import when the view's structure changes.
Key features
Tableau Agent and Tableau Pulse ground answers in Tableau Semantics, Tableau's own metric layer, which is generally available only within the Tableau+ package or Data 360. Once a TDS import lands, Tableau manages those metrics as its own data sources. Snowflake's Semantic View Autopilot runs the other direction, ingesting a Tableau .twb file and generating a semantic view from its calculated fields and relationships through Snowflake's Autopilot creation workflow.
Tableau's newer AI experiences increasingly rely on Tableau Semantics and Data 360 for the context behind conversational and AI-assisted workflows.
Pros
Mature enterprise reporting, visualization, and dashboarding workflows.
Existing Tableau teams have a path to reuse Snowflake Semantic Views in familiar reporting experiences.
Live Snowflake connectivity and enterprise identity controls are well established.
Existing Tableau metadata can help bootstrap Snowflake Semantic Views.
Cons
The bigger trade-offs sit above the export mechanics, in how much of the Tableau ecosystem the AI story requires.
Getting AI grounded at all means buying into Tableau+ or Data 360 for Tableau Semantics — the metric layer Agent and Pulse actually use — on top of the TDS export itself, so the Snowflake object gets you a data source, not an AI-ready one, until you've added that package.
Tableau Agent and Pulse extend Tableau's existing authoring model rather than building a dashboard or app from a prompt; someone still opens Desktop and assembles the workbook by hand.
AI capability is scattered across that same package boundary — Agent, Pulse, and Tableau Semantics live in Tableau+/Data 360, while the semantic view export, connections, and core authoring stay in base Tableau — so a team has to license and stitch together two products to get one continuous ask-to-build workflow.
If a virtual connection's data policy uses User Functions, an extract holds only the rows matching that policy at extraction time, so live connections are preferable for those cases, and the client credentials OAuth flow uses one shared identity, so row access policies don't apply per viewer.
The export path remains practical for existing Tableau estates, but teams should price the Data 360/Tableau+ dependency as part of the AI decision, not as a footnote to it, and understand that most modern analytics work extends
beyond dashboards
.
Pricing
Tableau Standard starts at $15 per user per month, Enterprise at $35, and Tableau Next at $40, all on annual contracts. Viewers are paid seats on standard tiers, though capacity-based Viewer Blocks carry no per-user charge.
Who is Tableau best for?
Tableau fits organizations already standardized on Tableau that want Snowflake Semantic Views to feed existing reporting workflows. If Semantic Views are intended to become a broader context layer for AI, test how much of that investment carries into Tableau's AI experiences without creating another semantic layer to maintain.
Power BI
Power BI
is a familiar and cost-effective BI option for organizations standardized on Microsoft, with deep integration across Power BI, Entra ID, and Fabric.
Power BI gives business users a reporting experience integrated with Entra ID and Fabric. For organizations already using Microsoft tools, that integration simplifies setup and provides a low published entry price among the tools here. Power BI's own semantic model is the center of gravity, so you re-express a Snowflake-defined metric as DAX measures. One workaround is an open-source community connector that wraps metrics in AGG() for DirectQuery.
Key features
Copilot answers from your Power BI semantic model, so it only knows the DAX measures you rebuilt there, not the ones you defined in Snowflake. Fabric data agents can route across up to five sources, including warehouses and semantic models. Snowflake's Autopilot ingests .pbix and .pbit files and converts a Power BI model into a semantic view. That capability is now GA, though the flow runs one way into Snowflake.
Pros
Strong integration with Microsoft 365, Entra ID, and Fabric.
Familiar reporting and dashboard workflows with a large installed user base.
Attractive economics for organizations already standardized on Microsoft's data stack.
Existing Power BI metadata can help teams bootstrap Snowflake Semantic Views.
Cons
Power BI's AI experiences are grounded in Power BI's own semantic model, so Snowflake-defined metrics may still need an equivalent representation in Microsoft's layer.
Teams can therefore end up maintaining business logic across Snowflake and Power BI rather than using the Snowflake Semantic View as the single context source.
Copilot, Fabric agents, reporting, and deeper analytical workflows span multiple Microsoft surfaces rather than one continuous question-to-analysis-to-build experience.
Teams investing in Snowflake Semantic Views specifically for portable AI context should test how much additional DAX modeling and Microsoft-specific context is still required.
Pricing
Pro costs $14 per user per month and Premium Per User costs $24, both raised on April 1, 2025. Microsoft bills Fabric capacity separately.
Who is Power BI best for?
Power BI is a strong fit for organizations already standardized on Microsoft that primarily need cost-effective traditional BI. If Snowflake Semantic Views are intended to become the shared context layer for AI, test how much duplication remains between Snowflake and Power BI's own semantic model.
Looker
Looker
is Google's governed BI platform built around LookML, with version-controlled semantic modeling at the center of the product.
Key features
Looker can work with Snowflake Semantic Views and can also publish LookML-defined semantics into Snowflake. LookML, however, remains central to how Looker's own BI and conversational analytics experiences understand the data.
For teams with significant existing LookML investments, that creates a path to extend those definitions into Snowflake while retaining established modeling and review workflows.
Pros
Mature governed modeling and version control through LookML.
Per-user Snowflake OAuth supports user-level governance.
Existing LookML investments can be extended into Snowflake Semantic Views.
Mature enterprise reporting and dashboarding workflows.
Cons
LookML remains the center of gravity for Looker's BI and AI workflows, so teams investing in Snowflake as a shared semantic layer may end up maintaining context in both places.
Looker's conversational agents are constrained by the Explores, relationships, and context modeled in advance. As users ask broader questions, the data team may need to keep extending LookML to maintain coverage.
More advanced or exploratory analysis generally moves outside Looker's core BI workflow into a separate technical environment.
Teams should pressure-test how weak answers are identified from real-world usage and how context improvements are validated over time.
Pricing
Standard, Enterprise, and Embed editions use annual commitments with no published dollar figures; you call sales.
Who is Looker best for?
Looker is a strong fit for teams already deeply invested in LookML and comfortable keeping it as their primary analytics model. Teams adopting Snowflake Semantic Views to make context portable across AI and analytics tools should evaluate whether they're actually reducing modeling duplication or adding another semantic representation.
ThoughtSpot
ThoughtSpot
is a conversational BI platform centered around Spotter. Its Snowflake Semantic Views integration can bring Snowflake-defined semantics into ThoughtSpot Models for use across its search and conversational experiences.
Key features
When a Snowflake Semantic View is brought into ThoughtSpot, its definitions can seed a ThoughtSpot Model used by Spotter, Liveboards, and other ThoughtSpot experiences.
ThoughtSpot can then enrich that model with additional metadata and context for its own agents. Snowflake identity passthrough provides a path for maintaining user-level warehouse permissions.
Pros
Conversational analytics experience for business users.
Snowflake Semantic Views can provide a starting point for ThoughtSpot's modeled and conversational experiences.
Snowflake OAuth can preserve user-level permissions.
ThoughtSpot can reuse the resulting model across Spotter, Liveboards, and embedded analytics.
Cons
Importing a Semantic View creates a ThoughtSpot-side model that can accumulate additional context, so teams should understand which system remains authoritative as both evolve.
Changes and enrichments made inside ThoughtSpot may not automatically become reusable by other agents consuming the Snowflake Semantic View.
Spotter is primarily grounded in ThoughtSpot's modeled context, so teams should test how well it handles questions outside relationships and definitions modeled in advance.
Conversation and reusable dashboard building remain distinct workflows rather than one continuous natural-language path.
Teams should pressure-test how they identify weak answers from production usage and systematically improve context over time.
Pricing
Essentials costs $25 per user per month, Pro costs $50 per user per month with 25 Spotter queries per user per month and SSO, and Enterprise pricing is custom.
Who is ThoughtSpot best for?
ThoughtSpot is a good fit for teams prioritizing just conversational BI on top of governed warehouse data. If Snowflake Semantic Views are intended to be a portable context layer across many AI and analytics tools, test how much additional context accumulates specifically inside ThoughtSpot and how that stays aligned with Snowflake.
Choose a BI tool that maximizes your Snowflake Semantic Views investment.
Snowflake Semantic Views give teams a way to define governed business context close to the data at exactly the moment AI agents are becoming much more capable of analyzing it.
Choosing a BI platform therefore isn't just about checking whether a Semantic Views integration exists. It's about how much leverage the platform lets you get from the context you've built.
Start with the integration. Does the platform actually use your Snowflake definitions, preserve governance, and avoid unnecessary duplication?
Then look at what happens after the connection is made. Can the context ground self-service questions, dashboards and apps, deeper analysis, and external agents? Can it sit alongside trusted context that doesn't belong in the semantic model? And does real-world usage give your data team a scalable way to identify gaps and improve answer quality?
The best integration shouldn't just consume your Snowflake Semantic Views. It should make them more useful as your AI analytics strategy expands.
That makes Hex a strong fit for teams that want Snowflake Semantic Views to power more than a single BI surface: business users can ask questions in
Threads
, teams can turn answers into dashboards and apps, analysts can go deeper in the same environment, and
Context Studio
helps data teams see where context is holding up and where it needs improvement. See how it works in a
demo
.
Frequently Asked Questions
Do I need a finished Snowflake Semantic View before a BI tool's AI can be trusted?
No. A Snowflake Semantic View can provide important governed metrics, relationships, and definitions, but it doesn’t need to contain every piece of context an AI agent relies on.
Teams can start with trusted warehouse tables, metadata, documentation, and existing analytical assets, then deepen semantic modeling where consistent metric definitions matter most. In Hex, for example,
Semantic Model Sync
can bring in Snowflake Semantic Views, while
Guides
,
Endorsements
, and
Context Studio
help supplement and improve the context around them over time.
The important thing is choosing a platform that lets semantic models work alongside other trusted context rather than treating a fully modeled semantic layer as a prerequisite for every AI workflow.
What's the difference between syncing a semantic view and importing it?
A sync keeps the Snowflake object as the source and refreshes the BI tool's representation from it. An import converts the definition into the tool's own model, as ThoughtSpot does with ThoughtSpot Models, after which changes in Snowflake wait for an admin resync. That gap matters most for metrics that change often — pricing tiers, discount rules, anything Finance revisits every quarter. Treat an imported copy as a snapshot, not a live mirror, and pair it with
data quality monitoring
to catch drift before a stakeholder does.
How do I keep Snowflake's row access policies working in a BI tool?
Use per-user OAuth or SSO with live queries, so each viewer's session carries their own role and Snowflake evaluates the policy per person. Avoid extracts and Import mode for governed data, because those run once under a service account and bake that account's view of the data into a file. Test it directly: have two users with different Snowflake roles ask the same question through the tool's AI or dashboard, and confirm each gets results filtered to their own access rather than a shared service account's view. That per-viewer check matters as much for
security and compliance
audits as it does for day-to-day correctness. Watch the tool-specific edges: Looker uses each user's default role under OAuth and can't switch, and ThoughtSpot builds its search index on the connection creator's identity.
Share:
twitter
linkedin
Get "The Data Leader’s Guide to Agentic Analytics"  — a practical roadmap for understanding and implementing AI to accelerate your data team.
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
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
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
Request a demo
Technical support
Contact us
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
