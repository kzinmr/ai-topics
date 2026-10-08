---
title: "Best BI Tools for Databricks Metric Views (2026)"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/best-bi-tools-for-databricks-metric-views/"
scraped: "2026-10-07T06:00:31.859106+00:00"
lastmod: "2026-10-01"
type: "sitemap"
---

# Best BI Tools for Databricks Metric Views (2026)

**Source**: [https://hex.tech/blog/best-bi-tools-for-databricks-metric-views/](https://hex.tech/blog/best-bi-tools-for-databricks-metric-views/)

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
Best BI tools for Databricks metric views
Compare Hex, Sigma, Tableau, Power BI, and more on live metric view support, per-user OAuth, and governed MEASURE() queries for Databricks Unity Catalog.
The Hex Team
Data
October 1, 2026
Share:
twitter
linkedin
In this article
What Unity Catalog metric views are
Four ways a BI tool can consume a metric view
What to evaluate before you connect a tool
How eight tools handle Databricks metric views
Choosing the best BI tools for Databricks metric views: start with one view and a live connection
Frequently Asked Questions
Get started for free
Databricks is evolving from a lakehouse into a broader analytics platform, and
Unity Catalog metric views
are an important part of that shift. They let teams define governed measures, dimensions, and relationships centrally so the same business definitions can be reused across the tools and agents that consume Databricks data.
That matters more as
frontier models get better at real-world data analysis
. If agents can increasingly answer open-ended business questions, the quality and portability of the context underneath them becomes just as important as the model itself.
For teams investing in metric views, that changes how to evaluate a BI tool. Connecting to Databricks is table stakes. The more important questions are whether the tool actually preserves your metric views as the source of truth, how broadly those definitions can be used across self-service and dashboard workflows, whether they can work alongside other forms of business context, and how the data team maintains answer quality as usage grows.
The goal should be to get more leverage from the semantic work you've already done in Databricks, not recreate it in another proprietary modeling layer.
What Unity Catalog metric views are
Metric views provide a
centralized way to manage business metrics
by separating measure definitions from the fields (also called dimensions) used to group, filter, and aggregate them, so you can define metrics once and query them at runtime. Each one registers in Unity Catalog as a securable object with lineage, and the feature reached
general availability (GA) on April 2, 2026
.
Most BI query generators were not originally designed for MEASURE() semantics. Unlike SUM or AVG, the MEASURE function "does not specify the aggregation. It inherits the definition of the aggregation from the metric view definition." A measure column isn't a raw numeric column. Without native metric-view support or compatibility rewriting, a tool that sends SUM() against a measure can fail or return the wrong result. You also
can't SELECT * from a metric view
.
Four ways a BI tool can consume a metric view
Databricks documents several ways BI tools can consume metric views. The implementation matters because each approach creates a different tradeoff between governance, maintenance, and portability.
Custom SQL with MEASURE().
The BI tool passes SQL to Databricks and the analyst explicitly calls MEASURE() for each governed measure.
SELECT
Order Month
, MEASURE
Total Revenue
)
FROM main.sales.orders_metric_view
GROUP BY ALL;
This preserves the definition in Databricks, but analysts still need to maintain metric-view-specific SQL inside the BI tool.
Wrapper views.
Teams can create a standard Unity Catalog view that embeds the MEASURE() calls and exposes the result like an ordinary table. This can make metric views usable by tools without native support, but the wrapper becomes another governed object that needs to stay aligned with the underlying metric view.
BI compatibility mode.
Databricks can rewrite BI-tool aggregations into metric-view semantics for supported integrations. Compatibility support varies by product and has changed over time, so teams relying on it should verify the current connector behavior rather than assume it is permanent.
Built-in integrations.
Some partners expose metric views, dimensions, and measures directly inside the product. Databricks has announced integrations with platforms including Hex, Sigma, Omni, Tableau, Power BI, and ThoughtSpot, but "support" can range from a shipped native workflow to compatibility paths or roadmap functionality.
Those differences become important once metric views move from an experiment to a production foundation for analytics.
What to evaluate before you connect a tool
1. Does the tool preserve Databricks as the source of truth?
Start with the basic architectural question: when a metric is defined in a metric view, does the BI tool query that definition directly, sync it, translate it, or recreate it in another semantic model?
Live queries against the current definition minimize drift. Extracts, copied models, wrapper layers, and translated metrics can all be valid architectural choices, but each adds another place where the business definition can diverge.
Identity matters too. Row filters and column masks evaluate against the credential that runs the query. Per-user OAuth can preserve user-level Databricks permissions, while service principals or shared credentials can require teams to rebuild more access control inside the BI layer.
The important thing is knowing exactly which system owns the metric, which identity executes the query, and what needs to stay synchronized over time.
2. How broadly can metric views power analytics?
A metric view becomes more valuable when the same governed definition can power more than one dashboard.
Can a business user ask a question in natural language against it? Can someone build a dashboard or interactive app from the same context? Can that governed definition also be used by agents working outside the core BI interface?
If every consumption surface requires its own copy of the metric logic, the value of centralizing it in Unity Catalog starts to erode.
3. Can metric views sit alongside other business context?
Metric views are useful context, but they aren't the entirety of what an AI agent needs to answer every business question.
Agents may also need warehouse metadata, documentation, definitions, endorsed assets, code, dbt projects, or instructions about how the business operates. Semantic models provide strong structure for metrics and relationships, but open-ended questions often require context that wasn't encoded into the model in advance.
Look for platforms that can use metric views as an important governed foundation without forcing every piece of context into another proprietary semantic layer.
4. Can you see where your metric views need to improve?
Metric views aren't a one-time modeling project. Once people start asking real questions, you'll discover missing measures, relationships, descriptions, synonyms, and areas where the model doesn't cover what users actually need.
Look for a platform that shows you which questions are being asked, where answers struggle, and whether the issue traces back to gaps in the metric view or other business context. Ideally, that usage becomes a feedback loop for improving the governed layer itself, so you're extending metric views based on real demand rather than trying to model every possible question upfront.
How eight tools handle Databricks metric views
Hex
Hex
is a
BI platform
built for the AI era: spanning natural-language self-service, dashboards and
data apps
, and governed AI workflows. Hex added Databricks Unity Catalog Metric Views as a semantic view sync in its
October 15, 2025 changelog
, alongside dbt MetricFlow, Cube, and Snowflake Semantic Views.
Key features
By bringing Databricks metric views inside Hex, teams can use their governed measures and dimensions without recreating those definitions in a separate Hex-only model.
Those definitions can then support
Threads
for natural-language self-service and dashboards or apps built from the same governed context. A business user can start with a question, follow up in plain language, and turn useful work into something reusable without rebuilding the metric logic elsewhere.
Metric views can also sit alongside other forms of context.
Context Management
lets teams combine semantic models with Guides, Endorsements, warehouse metadata, existing analytical assets, and other business context rather than requiring every instruction to be represented inside the semantic model.
Context Studio
then gives the data team visibility into what users are asking and where answers are struggling, helping surface gaps that may require new or improved metric definitions, descriptions, relationships, or other context. That creates a feedback loop where real-world usage can inform how the governed context in Databricks evolves.
Enterprise customers can also use per-user OAuth for Databricks so queries run under each user's own credentials rather than one shared service identity.
Pros
Unity Catalog metric views can remain the governed source of metric definitions rather than being rebuilt solely for Hex.
The same definitions can support natural-language self-service, dashboards, and apps.
Other forms of context can sit alongside metric views instead of forcing every business rule into the semantic model.
Context Studio helps teams use real-world questions and answer quality to identify where metric views and supporting context need to be extended or improved.
Per-user OAuth on Enterprise can preserve Databricks user identity and permissions.
Metric views can coexist with other semantic-model sources such as dbt MetricFlow, Cube, and Snowflake Semantic Views.
Cons
Semantic Model Sync coverage should be validated against the specific Databricks metric-view features your team uses.
Per-user OAuth and Explorer access are Enterprise features.
Teams with very large deployments should model both Hex seat economics and Databricks compute.
Pricing
Hex pricing
lists Community as free, Professional at $36 per Editor per month, Team at $75 per Editor per month, and custom Enterprise pricing.
Who is Hex best for?
Hex is a strong fit for teams that want Unity Catalog metric views to become a broader foundation for AI analytics: business users asking questions in plain language, dashboards and apps built on the same governed definitions, and real-world usage helping the data team understand where those metric views should be improved or extended.
Sigma
Sigma is warehouse-native BI built around a spreadsheet-style interface. It added support for browsing and querying Databricks metric views in workbooks and data models in 2026, allowing users to work with governed measures while queries continue to execute against Databricks.
Key features
Connection-level OAuth for Databricks became GA in
May 2026
. Sigma queries Databricks live, so changes to metric definitions can flow into subsequent workbook interactions without an extract refresh.
Its spreadsheet-style interface gives a familiar way to work with warehouse data. Sigma also supports Databricks OAuth, including configurations that preserve user identity.
Pros
Live warehouse queries can reflect current metric-view definitions without moving the data.
Spreadsheet-style exploration is familiar to finance and operations users.
Native metric-view browsing reduces the need for hand-written MEASURE() SQL.
OAuth can preserve Databricks governance when configured for individual users.
Cons
Metric-view support is relatively new, so teams should validate exactly how measures are grounded across Ask Sigma and workbook workflows.
The broader experience still centers on Sigma workbooks, so users may eventually fall back into spreadsheet and workbook concepts despite AI functionality.
Deployment patterns that use shared or group service identities can weaken the per-user governance benefits of Unity Catalog.
Usage and feedback reporting can be manually set up to show how people interact with AI, but teams should test whether that functionality is sufficient to identify specific gaps in the underlying metric views and feed improvements back into Databricks.
Pricing
Sigma doesn't publish pricing; sales quotes every tier. In the quote, ask whether viewer seats are licensed separately and confirm that Databricks compute is billed by Databricks rather than bundled into the Sigma number.
Who is Sigma best for?
Sigma is a good fit for teams that want to prioritize spreadsheet-style exploration directly against Databricks and are comfortable making workbooks the primary interface for business users.
Omni
Omni
is a semantic-model-first BI platform. Its Databricks integration imports metric views into Omni Topics, where fields, relationships, metrics, and additional AI context can be maintained inside Omni.
Key features
Metric-view definitions can be brought into Omni through schema refreshes, giving teams a starting point for exploration and AI inside Omni's model.
Omni also supports the reverse path: teams can publish Omni-authored definitions back into Databricks, creating a two-way modeling workflow between Omni and Unity Catalog.
That flexibility can be useful if Omni is intended to remain an active semantic-modeling surface. But it also means teams need to be explicit about which system owns each definition and how changes stay synchronized.
Pros
Metric views can seed Omni Topics rather than requiring every definition to be created from scratch.
Two-way modeling gives teams flexibility to publish Omni-authored definitions back to Databricks.
AI agents and dashboards operate against the same Omni semantic rules.
Omni's eval tooling lets teams test representative questions against the modeled context.
Cons
Imported metric views are represented inside Omni rather than acting as a perfect live mirror of the Databricks object.
Not every Databricks metric-view construct maps directly into Omni.
Bidirectional modeling can create ambiguity about which system is authoritative if definitions evolve independently in Omni and Databricks.
Omni's AI is constrained to the Topics, relationships, and context defined in its semantic model. As users ask broader questions, the data team may need to keep expanding model coverage.
Existing business context may need to be recreated inside Omni's modeling layer, and context built there is less portable to other analytics or agent workflows.
Omni's evals are useful for testing defined question sets, but teams should also evaluate how easily real-world questions expose gaps that should be addressed in the underlying Databricks metric views rather than only in Omni.
Service-principal deployments can require permissions to be recreated in Omni rather than inheriting each user's Unity Catalog identity.
Pricing
Omni doesn't publish pricing, so you can't line it up against the published seat prices elsewhere in this list without a call. Ask for the seat model, whether viewer access is priced separately, and confirmation that Databricks compute bills through Databricks.
Who is Omni best for?
Omni fits teams that want its semantic model to remain a primary modeling surface and are comfortable investing in and maintaining that model alongside Unity Catalog.
Tableau
Tableau is enterprise visualization and dashboarding software with several documented ways to consume Databricks metric views, including custom SQL, wrapper views, and compatibility-mode approaches.
Key features
Databricks
enforces OAuth authentication
when publishing to Tableau Cloud, with 90-day token expiry by default, so row filters and masks can apply according to the authenticated user's privileges on live connections. Tableau Semantics and the Semantic Model Builder are available to Tableau Next / Tableau+ and Data 360 customers. Tableau Semantics does not have a documented metric-view ingestion path today.
Pros
Multiple compatibility paths let existing Tableau estates adopt metric views incrementally.
Mature dashboarding and visualization workflows.
Per-user OAuth can preserve Databricks permissions on live connections.
Databricks migration tooling can help teams move existing Tableau assets into Databricks-native experiences if needed.
Cons
Current metric-view support still relies on compatibility paths rather than a fully native semantic experience.
Compatibility behavior can have limitations around certain metric-view operations.
Extracts introduce another copy of the data and logic that can drift between refreshes.
Tableau's AI capabilities extend its existing authoring model rather than providing one continuous natural-language workflow from question to generated dashboard or app.
Tableau Agent grounding directly in Unity Catalog metric views is not currently documented.
Teams should test whether real-world AI usage provides actionable signals about gaps in Databricks metric views or primarily informs Tableau's own semantic and authoring layers.
Pricing
Tableau pricing
lists Cloud Standard at $15/user/month, Cloud Enterprise at $35/user/month, and Cloud+ by contact. Tableau Next starts at $40/user/month, and sales quotes Viewer Blocks for viewer-only access.
Who is Tableau best for?
Tableau is strongest for teams with a substantial existing Tableau estate that want to adopt Databricks metric views incrementally while prioritizing established dashboard workflows.
Power BI
Power BI is a familiar reporting environment for business users and offers the lowest published entry seat price among the tools with public pricing. That combination suits Microsoft-standardized organizations already using Entra ID and Fabric. It can list metric views through its Databricks connector but cannot query them directly because Power BI does not automatically generate the needed MEASURE() and GROUP BY logic. Compatibility mode was removed in the
April 2026 release notes
: "Reports that use this connector option no longer function." That leaves native query with MEASURE() in DirectQuery (Desktop only), wrapper views, or Tabular Editor's Semantic Bridge. For a broader workflow view, teams can
compare analytics platforms
.
Key features
DirectQuery with Entra ID SSO can pass user identity through to Databricks, allowing Unity Catalog permissions to apply to dashboard queries.
Copilot adds natural-language assistance, but it grounds answers primarily in the Power BI semantic model rather than directly in Unity Catalog metric-view definitions.
Pros
Low published entry pricing relative to many enterprise BI tools.
Familiar experience for organizations already standardized on Microsoft.
DirectQuery with correctly configured SSO can preserve Databricks user identity.
Mature reporting and semantic-modeling capabilities.
Cons
Native metric-view consumption still requires workarounds or translation rather than being the default Power BI modeling path.
Recreating governed definitions in DAX or the Power BI semantic model introduces another semantic layer to maintain.
Import mode creates another copy of data, permissions, and logic that needs to remain synchronized.
Copilot requires Fabric capacity and grounds against Power BI's own semantic model.
Reporting, AI, agents, and semantic modeling span multiple Power BI and Fabric surfaces.
Because AI grounding lives primarily in Power BI's semantic layer, usage feedback may point teams toward improving that layer rather than revealing where Unity Catalog metric views themselves need to evolve.
Pricing
Microsoft Power BI pricing lists Pro at $14.00/user/month and Premium Per User at $24.00/user/month, paid yearly, with Fabric capacity priced separately. Free viewer consumption needs an F64 or larger capacity, and Microsoft is retiring P-SKUs in favor of Fabric.
Who is Power BI best for?
Power BI is a good fit for Microsoft-standardized organizations that prioritize familiar, cost-effective reporting. Teams that want Unity Catalog metric views to remain the semantic source of truth should carefully evaluate how much logic and ongoing improvement work moves into Power BI instead.
ThoughtSpot
ThoughtSpot is a search- and conversational analytics platform centered on Spotter. It has announced support for Unity Catalog metrics, while native metric-view integration has been rolling out separately from existing custom-SQL approaches.
Key features
ThoughtSpot can query Databricks live, and per-user OAuth can allow Unity Catalog policies to apply to the authenticated user's queries.
Spotter makes conversational access central to the product, making ThoughtSpot particularly relevant for teams evaluating natural-language self-service on top of Databricks.
Pros
Conversational analytics is a core product experience.
Live Databricks querying avoids moving data into extracts.
Per-user OAuth can preserve Unity Catalog permissions.
Answer lineage gives users more visibility into how results were produced.
Cons
Teams should confirm the current availability and scope of native metric-view support rather than relying on roadmap announcements.
Where native support isn't available, teams may need to maintain custom MEASURE() SQL or wrapper views.
Conversational exploration and reusable artifact building remain more distinct workflows.
ThoughtSpot maintains its own semantic and object-permission layers alongside Unity Catalog.
Teams should evaluate whether usage and answer-quality signals can identify gaps in Databricks metric views themselves or primarily inform ThoughtSpot's own semantic layer.
Pricing
ThoughtSpot pricing lists Essentials at $25/user/month for 5–50 users with no Spotter, and Pro at $50/user/month with Spotter capped at 25 queries per user per month. A usage-based option runs $0.10 per credit, with Enterprise custom.
Who is ThoughtSpot best for?
ThoughtSpot is a good fit for teams that want conversational analytics over live Databricks data and are comfortable validating how metric-view grounding, improvement workflows, and broader artifact building fit together.
Looker
Looker has no documented integration with metric views. Its
Databricks connection documentation
covers catalog configuration with no mention of metric views or MEASURE(), and Looker is absent from the Databricks BI guidance. Based on the documented integration options, LookML has to re-model any logic you already defined in Unity Catalog. Teams deciding between a dedicated modeling layer and a workflow that combines conversational answers, generative building, and observability on the same governed layer can review
Looker vs Hex
.
Key features
Looker has no documented integration with metric views. Its
Databricks connection documentation
covers catalog configuration with no mention of metric views or MEASURE(), and Looker is absent from the Databricks BI guidance. Based on the documented integration options, LookML has to re-model any logic you already defined in Unity Catalog.
LookML provides mature version-controlled definitions for metrics, dimensions, joins, and permissions. But Looker's Conversational Analytics is grounded in that LookML semantic model.
That creates a straightforward architectural decision for teams investing in Unity Catalog metric views: either LookML remains the semantic source of truth, or teams maintain overlapping definitions across Looker and Databricks.
Pros
Mature semantic modeling and governance for organizations already invested in LookML.
Strong version-control and development workflows.
Per-user OAuth can preserve Databricks identity when configured.
Conversational Analytics can operate against established LookML models.
Cons
Metric definitions maintained in Unity Catalog need to be recreated in LookML.
There is no documented synchronization path between the two semantic layers.
Looker's AI remains grounded in predefined LookML Explores and relationships, which can increase modeling work as users ask broader questions.
Context built in LookML is closely tied to Looker and less portable across the wider AI ecosystem.
Because AI questions and modeling feedback resolve against LookML, teams don't get a natural feedback loop from real-world usage into improving Unity Catalog metric views.
Teams using default service-account configurations may need to recreate more user-level governance inside Looker.
Pricing
Looker pricing reads "Call sales" for every edition, with annual commitment. Conversational Analytics is free through September 30, 2026; from October 1, Standard includes 60M input and 1.2M output tokens per month, with overage at $3 per million input and $20 per million output tokens.
Who is Looker best for?
Looker is strongest for teams already committed to LookML as the primary governance layer. If Unity Catalog metric views are intended to become the semantic source of truth, maintaining and improving both layers creates additional work.
Choosing the best BI tools for Databricks metric views: start with one view and a live connection
The value of metric views comes from defining important business logic once, letting more consumers use it consistently, and improving that governed layer as you learn what people actually need.
So don't stop an evaluation at "can the connector see my metric view?"
Start with one important governed metric and test the full workflow. Ask a real business question in natural language. Check whether the generated query actually uses the current Databricks definition. Change the metric and see how quickly the BI layer reflects it. Verify that user-level permissions still behave correctly.
Then go further.
Can the same governed definition power a dashboard or app without being recreated? Can other business context sit alongside it when a question extends beyond modeled measures and dimensions? And when users start asking questions the metric view doesn't handle well, can the data team actually see that pattern and determine what needs to change?
That's the feedback loop to look for:
define governed context in Databricks, put it in front of real users and agents, observe where it falls short, and use those signals to improve the metric views themselves.
That's ultimately what determines whether the BI tool is amplifying your investment in Unity Catalog metric views or simply consuming a static version of it.
Frequently Asked Questions
How do I test a tool's metric view support in a trial?
Create one metric view with a measure and two dimensions, then connect using the identity model you plan to deploy in production.
Ask a question against the measure and inspect the generated query. Does the tool preserve the metric-view definition or generate its own aggregation? Then change the underlying definition and check whether the next interaction reflects it immediately or waits for a refresh or sync.
Finally, ask several questions the metric view doesn't handle cleanly. See whether the platform makes those failures visible enough that the data team can identify whether a missing measure, relationship, description, synonym, or other context should be added back to the governed layer.
Do I still need a separate semantic layer if I have Unity Catalog metric views?
Not necessarily.
If metric views contain the governed definitions your BI and AI consumers need, recreating those definitions in another semantic layer adds maintenance and another potential source of drift.
A separate layer can still make sense when you need capabilities Unity Catalog metric views don't provide, such as serving metrics consistently across multiple warehouses or specialized downstream applications. The important thing is being explicit about which layer owns each definition and where improvements should be made when real-world usage exposes a gap.
How do I keep Unity Catalog row filters and column masks intact through a BI tool?
Use per-user OAuth (U2M) for live queries. Shared service principals and personal access tokens shift user-level permission management into the tool, while Import mode, extracts, and external caches like Cube Store serve data read under one identity. Check the defaults: Looker uses a service account, and Hex's per-user OAuth connections are an Enterprise feature.
What should I look for beyond basic metric-view compatibility?
Our
BI Buying Guide
goes deeper on how the evaluation criteria for BI are changing in the AI era.
For metric views specifically, focus on whether the platform keeps Databricks as the source of truth, lets the same governed context power self-service and reusable BI workflows, works alongside other forms of business context, and turns real-world questions into useful signals about where your metric views need to improve.
See how Hex works against your own Databricks metric views with a
demo
.
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
