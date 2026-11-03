---
title: "Snowflake semantic layer: 7 options compared for BI and AI"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowflake-semantic-layer/"
scraped: "2026-11-03T06:00:56.226446+00:00"
lastmod: "2026-10-29"
type: "sitemap"
---

# Snowflake semantic layer: 7 options compared for BI and AI

**Source**: [https://hex.tech/blog/snowflake-semantic-layer/](https://hex.tech/blog/snowflake-semantic-layer/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
Snowflake semantic layer: 7 options compared for BI and AI
Where you define business metrics in Snowflake determines which BI tools and AI agents can reuse them, and what you may need to rebuild later.
The Hex Team
Data
October 29, 2026
Share:
twitter
linkedin
In this article
Semantic model vs. semantic layer: what's the difference?
What to look for in a semantic layer for Snowflake
The best Snowflake semantic layer options compared
How Snowflake AI and external agents use semantic definitions
What Apache Ossie means for semantic layer portability
How to choose a Snowflake semantic layer
Frequently asked questions
Get started for free
Snowflake gives data teams several ways to define what terms like “revenue,” “active customer,” or “net retention” mean. You can build those definitions natively in Snowflake, maintain them upstream in dbt or Cube, or create them inside a BI tool. But as more AI agents and analytics tools depend on those definitions,
where they live matters as much as what they contain
.
Not all semantic layers are equally portable. Some live within a particular BI platform, while others sit upstream and can serve multiple BI tools and AI agents. Where your semantic layer lives affects how easily you can reuse business definitions as your analytics stack evolves. And consistent metrics are only part of the context AI needs to understand your business.
This guide compares seven semantic layer options for Snowflake:
Snowflake Semantic Views, dbt MetricFlow, Cube, Looker, Omni, Hex, and Lightdash
. We'll cover how they work, their modeling and governance capabilities, and two questions that are especially important for AI: how portable are your definitions, and where does the rest of your business context live?
Semantic model vs. semantic layer: what's the difference?
A
semantic model
defines business concepts on top of data: metrics, dimensions, joins, relationships, and the rules needed to calculate them consistently. For example, a revenue model might define which transactions count as revenue, how customer accounts join to transactions, and which date field to use for reporting.
A
semantic layer
is the broader system that organizes and exposes those definitions so BI tools, applications, and AI agents can query data using the same business meaning. Put simply, a model defines what data means; a layer makes those definitions usable. Vendors sometimes use the terms interchangeably, and a semantic layer can contain multiple models.
On Snowflake, native
Semantic Views
live in the warehouse; dbt and Cube expose models through separate services; BI products can combine modeling with authoring.
What to look for in a semantic layer for Snowflake
Basic modeling functionality is important: can you define reusable metrics, dimensions, joins, time calculations, and access rules? Does it run queries against Snowflake, and can your BI and AI tools use the result?
Two additional tests deserve equal attention.
1. Portability: what happens when your tools change?
It's helpful to distinguish an
accessible
model from a
portable
one. An MCP server or API may let Claude or another agent ask questions through a vendor, without making the underlying definitions available for another system to own. Check who can consume the model directly, whether you can export or convert it, and how much logic would need rebuilding if you switched vendors.
2. Context beyond the model: where does everything else go?
An agent may need more than metric definitions to answer “Why did enterprise expansion slow last quarter?” It might need product documentation, sales-process changes, trusted past analyses, or instructions about which datasets are appropriate. Some products attach that information to semantic objects; others let teams maintain additional instructions, documentation, and other context independently. Neither approach is automatically wrong, but it affects maintenance and reuse.
Seven Snowflake semantic layer options at a glance
The best Snowflake semantic layer options compared
1. Snowflake Semantic Views
Snowflake Semantic Views
bring business metrics and relationships directly into the warehouse. Instead of maintaining a second modeling service, data teams define a semantic view as a native schema object, using SQL, YAML, or Snowflake's assisted authoring tools.
Modeling and governance.
Semantic Views describe logical tables, relationships, dimensions, facts, and metrics. Snowflake permissions continue to apply, and views can include synonyms, descriptions,
verified queries and AI instructions
. Teams can manage changes as code. Contrary to older guidance, CREATE OR ALTER SEMANTIC VIEW can now modify model definitions without the blanket need to replace the view and re-grant privileges.
BI and AI support.
Snowflake's Cortex Analyst and Cortex Agents can use semantic views for natural-language analysis.
Other tools can query supported views
through SQL or Snowflake interfaces, and some BI products import them.
Portability.
Definitions can be exported as YAML, and Snowflake has introduced support for importing models using the Open Semantic Interchange format, now developed as
Apache Ossie
. But exportability isn't universal compatibility: downstream products must understand the format or translate its behavior. A second warehouse will not automatically inherit Snowflake-specific models and policies.
Beyond the model.
Semantic Views can hold SQL-generation instructions, question-classification instructions, and verified query examples. These improve how Cortex interprets questions, but broader documents and business processes generally involve other context sources or agent services. Snowflake's overall AI ecosystem is broader than any one semantic view.
Best fit:
Teams standardized on Snowflake that want governed definitions close to the data and expect to use Snowflake's own analytics and AI services alongside
compatible third-party tools
.
2. dbt Semantic Layer and MetricFlow
dbt MetricFlow
defines metrics and semantic models in the dbt project and generates SQL to query them. With Snowflake as the underlying data platform, teams can maintain metric logic as code alongside the transformations they already build and review.
Modeling and governance.
MetricFlow supports simple, ratio, cumulative, and derived metrics, plus dimensions and relationships, with definitions reviewed in version control.
dbt Core vs. dbt Cloud:
MetricFlow is open source, so teams using dbt Core can define semantic models, generate SQL, and query metrics locally. However, dynamically serving those metrics to downstream BI tools and AI applications through dbt's hosted Semantic Layer APIs requires a paid dbt platform plan (Starter or higher). This means your metric definitions remain portable, but accessing them across tools through dbt's managed service introduces a separate dependency.
BI and AI support.
dbt's Semantic Layer exposes defined metrics through supported BI integrations and APIs; its MCP integrations can make relevant metric and metadata information available to agents. For teams using multiple BI products, this can prevent each tool from having to redefine the same basic calculation.
Portability.
Definitions live in version-controlled YAML, and MetricFlow is open source. dbt also supports
Apache Ossie
interoperability. This makes the definitions relatively portable, although consuming them through another semantic layer may require conversion, and not every modeling feature translates automatically.
Beyond the model.
dbt projects provide descriptions, metadata, lineage, and code-level context. Other documentation can live in repositories alongside the project, though a given AI agent still needs an integration that can read and use it. External documentation still needs an agent integration.
Best fit:
Analytics engineering teams already invested in dbt, particularly those trying to keep metric definitions independent of whichever BI interface business users adopt next.
3. Cube
Cube
is an independent semantic layer that connects to Snowflake and serves governed analytical definitions to different tools. Teams author cubes and views in YAML or JavaScript, then query them through supported interfaces. Cube can also use pre-aggregations to accelerate repeated workloads.
Modeling and governance.
Cube models define measures, dimensions, joins, segments, and views. Access policies and security context can govern which data a user or application may query.
BI and AI support.
Cube exposes APIs including SQL, REST, and GraphQL, with additional protocols or integrations for specific BI tools. This makes it useful when the organization needs one metric service supporting several applications, dashboards, and agents rather than a model attached to one frontend.
Portability.
The model lives independently of the BI tools that consume it, which can make those consumers easier to replace. However, Cube's own modeling format and deployment still represent a dependency; moving away from Cube may require translating measures and security rules. Export support varies by integration.
Beyond the model.
Cube's semantic definitions and access context give agents useful grounding. Separate policy documents, guides, prior analytical work, and business instructions generally need to be supplied through other connected systems; Cube is primarily the semantic service rather than a complete context-management workflow.
Best fit:
Teams serving multiple BI or application frontends that are willing to operate a dedicated semantic service and manage its performance, access controls, and integrations.
4. Looker and LookML
Looker
uses LookML to define metrics, joins, dimensions, and reusable Explores. Those definitions typically live in Git-managed LookML projects, while Looker acts as the service through which users and other tools access them.
Modeling and governance.
LookML has a mature framework for governed metric definitions, relationship logic, access filters, and code review.
BI and AI support.
Looker's Conversational Analytics and other Gemini-enabled experiences can work with its modeled data, while APIs and integrations expose Looker content to additional workflows. But being able to query Looker is not the same as being able to take its modeling logic and run it in another semantic layer.
Portability.
Git makes LookML versioned, inspectable, and recoverable, but the language itself remains tied to Looker's architecture. A move to Snowflake Semantic Views, Cube, or another model system can require translating logic, joins, permissions, and calculations.
Beyond the model.
Descriptions, modeled definitions, examples, and other Looker metadata help ground its AI experiences. Extra context can also be supplied through broader tooling, but teams should check which instructions each agent actually uses and how much of that knowledge remains tied to Looker.
Best fit:
Organizations with substantial LookML investments and Google Cloud workflows that value centralized modeling and are comfortable with Looker as the long-term modeling authority.
5. Omni
Omni
combines semantic modeling, dashboards, workbooks, and AI analytics. Its modeling architecture can draw on existing dbt work while letting teams define reusable views, joins, calculations, and Topics directly in Omni.
Modeling and governance.
Omni provides structured modeling for business metrics and relationships, along with access controls and Snowflake integration. Topics can curate the fields and joins available for particular experiences.
BI and AI support.
Omni agents are restricted to answering questions through its semantic modeling architecture. Its MCP and related interfaces also allow supported external agents to access Omni’s semantic model to answer questions.
Portability.
Omni can build on dbt and other upstream definitions, so not every piece of logic must originate there. However, definitions added in Omni's modeling layer are not automatically portable to another BI vendor. Buyers should ask which portions of a Topic or model can be exported, synchronized, or recreated elsewhere.
Beyond the model.
Omni's ai_context fields let teams add instructions at different levels of its modeling architecture. This keeps guidance close to the relevant data, but also places more agent-specific business knowledge inside Omni-managed model definitions. Compare that with maintaining instructions in independent documents or repositories that multiple tools can reuse.
Best fit:
Teams looking for integrated AI-enabled BI and semantic modeling, particularly when they want curated self-service and are comfortable maintaining a substantial share of agent context within Omni.
6. Hex
Hex
combines semantic modeling with conversational analytics, and interactive dashboards and apps. Rather than requiring every agent question to fit a prebuilt semantic model, Hex can use those definitions alongside other endorsed data and business context.
Modeling and governance.
Teams can author semantic models in Hex or sync supported definitions maintained upstream in tools such as dbt MetricFlow, Cube, and Snowflake Semantic Views. Those models establish reusable metrics, dimensions, and relationships. Endorsements and warehouse metadata help agents identify trusted starting points, while permissions and workspace controls govern access.
BI and AI support.
The same context helps power Threads for conversational self-service, deeper SQL and Python analysis, and published apps or dashboards. Business users can ask follow-up questions while technical users inspect and extend underlying analytical work. A semantic model is valuable for recurring metric questions, but the agent can also investigate appropriate warehouse data when a question wasn't anticipated in advance.
Portability.
When metrics are
synced
from an upstream source, the source definitions remain there instead of becoming dependent on Hex. That reduces the work involved if the organization later introduces a different BI tool that can also consume those definitions. Portability still depends on the upstream format and integration coverage; analytics created natively in Hex are not automatically interchangeable with another vendor's projects.
Beyond the model.
This is where Hex takes a different architectural approach.
Guides
can provide business instructions independently of semantic models, alongside Endorsements, repository content, table metadata, and previous analytical projects. Guides can be maintained outside Hex and synchronized through code-based workflows.
Context Studio
gives data teams visibility into agent behavior and a way to evaluate answers, identify gaps, and improve context over time.
For example, a metric definition might specify
expansion revenue
, while a Guide explains which accounts should be excluded from an investigation or how a changing sales process should be interpreted. Those instructions don't all need to be turned into joins or embedded in a vendor-specific metric field.
At
PandaDoc
, teams combined Cube semantic definitions with Hex conversational exploration to make business questions more consistent and easier to investigate. This is a useful example of consuming an existing model while extending what business users can do with it.
Best fit:
Teams that want to preserve semantic definitions across their stack while giving AI agents access to broader context, from trusted metadata and documentation to existing analytical work, and then use that context in conversational and advanced analytics.
7. Lightdash
Lightdash
is particularly relevant to dbt-first teams. It uses dbt models and associated YAML to define and expose metrics, dimensions, and relationships, while also supporting Lightdash-specific modeling features.
Modeling and governance.
Teams can maintain metric definitions close to dbt transformations, with code review and versioning as part of the workflow. Lightdash supports table and field configuration, joins, filters, and permissions.
BI and AI support.
Lightdash offers dashboards, self-service exploration, and AI functionality that can answer questions and create analytical content. Its integrations include conversational access through supported external tools. Teams should verify which Lightdash and dbt features are understood by a particular AI surface rather than assuming every YAML field is consumed.
Portability.
Reusing dbt definitions helps avoid putting every metric exclusively inside a BI platform. However, Lightdash-specific YAML and dashboard configuration may still need work to migrate.
Beyond the model.
Lightdash documents knowledge documents and verified answers that can guide AI responses beyond basic metric descriptions. These provide important additional context; evaluate where the knowledge is stored, how it is maintained, and whether the same material can be reused in other agents.
Best fit:
dbt-oriented teams that want analytics tightly connected to their transformation project, with an open-source BI option and a manageable path to conversational self-service.
How Snowflake AI and external agents use semantic definitions
The choice of semantic layer is increasingly visible outside traditional BI.
Cortex Analyst
uses modeled business definitions to interpret natural-language questions. Cortex Agents can combine analytical tools with other retrieval capabilities. Snowflake's own AI experiences and managed integrations can expose governed semantics to additional consumers.
There are several ways an outside tool may work with Snowflake definitions: query a Semantic View directly, use an API or MCP service that interprets the model, or import definitions into another tool's own modeling architecture. Semantic Views support verified queries and AI instructions. Test which definitions the agent used and whether the data team can inspect its reasoning.
What Apache Ossie means for semantic layer portability
One promising development is
Apache Ossie
, previously called
Open Semantic Interchange (OSI)
. The project is developing a vendor-neutral specification for expressing semantic concepts—including metrics, dimensions, datasets, and relationships—so products can exchange definitions more easily. It was accepted into the Apache Incubator in 2026.
But the distinction between
standard support
and
actual compatibility
still matters. Converters and integrations exist, including work involving dbt and Snowflake, yet feature coverage differs. Advanced calculations, access rules, or vendor-specific metadata may not translate one-to-one. For now, treat Ossie as a meaningful interoperability effort and ask vendors which imports, exports, and converters are available today, not just whether they support the initiative.
How to choose a Snowflake semantic layer
Start with your existing source of truth. If almost all analytics run in Snowflake, native Semantic Views may simplify ownership and governance. If dbt already defines your metrics, extending MetricFlow may be more natural. If many applications need a common semantic query service, Cube deserves attention. If your company has invested heavily in LookML or an integrated BI model, the cost of moving those definitions should be part of the decision.
Test two scenarios:
First, change the consumer.
Define revenue once, use it in your main BI tool, then ask an external agent the same question. Check whether both tools use the same definition. Ask the vendor to demonstrate how the model would move or be reused if you replaced the BI tool.
Second, change the business context.
Introduce a new sales territory rule, product naming convention, or trusted source recommendation that isn't itself a metric. Where would your team maintain that instruction? Which agents pick it up? Can you inspect their behavior and improve the guidance without rebuilding semantic models for every new question?
Semantic models are an important foundation for trustworthy analytics, but they shouldn't become a place to cram every piece of business knowledge. The best choice is the one that keeps
critical metrics consistent, context maintainable, and future analytical tools flexible
.
Hex can help teams take that approach by building on existing Snowflake, dbt, and Cube definitions while maintaining additional context through Guides, Endorsements, metadata, and projects. Explore
BI in Hex
to see how that foundation supports everything from natural-language questions to sophisticated analysis and reusable apps.
Frequently asked questions
Does Snowflake have a native semantic layer?
Yes.
Snowflake Semantic Views
are native schema objects that define logical tables, relationships, dimensions, facts, and metrics. Snowflake's Cortex tools and supported integrations can consume them. Teams can author Semantic Views in SQL or YAML and use Snowflake's governance controls, while considering which external tools can query or import their definitions.
What's the difference between a semantic model and a semantic layer?
A
semantic model
defines business concepts like metrics, dimensions, and relationships over underlying data. A
semantic layer
is the broader system that organizes and exposes those definitions so BI tools, applications, and AI agents can query data consistently. Put simply, models define what the data means; the layer makes that meaning usable. The terms are sometimes used interchangeably, and a semantic layer can contain multiple models.
What is Apache Ossie, and how does it improve semantic layer portability?
Apache Ossie
(formerly Open Semantic Interchange) is an open-source effort to standardize how tools describe and exchange semantic definitions. It aims to reduce the need to recreate metrics, dimensions, and relationships whenever a company changes BI tools or adds an AI agent. The project entered the Apache Incubator in 2026. Support is still evolving, and feature differences mean a conversion isn't guaranteed to preserve every rule or calculation.
Is a Snowflake Semantic View the same as a universal semantic layer?
Not exactly. A Semantic View is maintained inside Snowflake and is naturally suited to Snowflake workloads and supported consumers. An independent service like Cube or dbt's Semantic Layer can serve definitions through its own interfaces to different applications and, depending on the product, more than one warehouse. Neither architecture guarantees universal compatibility; check each integration and the portability of the underlying definitions.
Does an AI agent need a semantic model to answer questions about Snowflake data?
Not always. A model is valuable for consistent metrics, joins, and recurring business questions, but some agents can also investigate trusted warehouse tables using descriptions, documentation, and other context. The appropriate approach depends on the question, governance needs, and how the agent's output is inspected and evaluated. A semantic model is one important source of context, not a substitute for every other kind of business knowledge.
Share:
twitter
linkedin
Choosing your next BI tool? Get the BI buyers guide for what to look for when evaluating the next generation of AI analytics platforms.
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
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
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
