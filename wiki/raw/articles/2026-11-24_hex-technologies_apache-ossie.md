---
title: "What is Apache Ossie?"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/apache-ossie/"
scraped: "2026-11-24T06:00:34.224874+00:00"
lastmod: "2026-11-23"
type: "sitemap"
---

# What is Apache Ossie?

**Source**: [https://hex.tech/blog/apache-ossie/](https://hex.tech/blog/apache-ossie/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
What is Apache Ossie?
Apache Ossie gives business definitions a shared format, so adopting another analytics tool doesn't have to mean rebuilding your semantic models.
The Hex Team
Data
November 23, 2026
Share:
twitter
linkedin
In this article
Where Apache Ossie came from
Why semantic model portability matters
What Apache Ossie standardizes
An Apache Ossie YAML example
How Apache Ossie works
How ready is Apache Ossie?
Do you need a semantic model for AI analytics?
Getting started with Apache Ossie
Definitions that can move with you
Frequently asked questions
Get started for free
Data teams often maintain versions of the same metric across a BI tool, a semantic layer, and the context supplied to AI agents. Each version takes work to build and update. When definitions diverge, teams spend time reconciling numbers instead of using them.
Apache Ossie
, formerly Open Semantic Interchange (OSI), is an open, vendor-neutral specification for exchanging semantic metadata across analytics tools, BI platforms, and AI applications. Its core model describes datasets, fields, relationships, and metrics in a shared format.
The goal is to make business definitions reusable across tools, so changing a BI product or adding an agent doesn't require recreating that work. For data teams, that means less duplicated modeling and more flexibility over where business logic is maintained and used.
This guide explains where Ossie came from, what it standardizes, how conversion works, and what to check before using it with your own stack.
Where Apache Ossie came from
Ossie began as Open Semantic Interchange, an initiative supported by companies across the data ecosystem. Hex
joined Open Semantic Interchange in September 2025
, supporting the idea that customers should be able to take semantic definitions between tools rather than keep them tied to a proprietary format.
The project subsequently entered the Apache Incubator. A
July 2026 announcement
introduced the name Apache Ossie (Incubating), chosen to avoid confusion with other projects using the OSI acronym. The rename itself didn't replace the specification; development continued under the new name and governance home.
The
Apache Incubator
provides a community-governance setting for the project as it works toward becoming an established Apache project. Participation by a vendor and support in a particular product are separate questions, so evaluate the integrations your team actually needs.
Why semantic model portability matters
A semantic model records business definitions such as metrics, dimensions, and relationships. Those definitions become more useful when multiple applications can use them.
Without interchange, adopting another tool may mean translating an existing model into that tool's native format. Teams then have another copy to maintain, and changes can be applied inconsistently.
A common format gives tools a shared target for import and export. The intended benefits include:
Less duplicated modeling:
Reuse definitions instead of recreating every metric in each application.
More choice:
Evaluate analytics tools without assuming a change requires abandoning the modeling work you've already done.
Reviewable changes:
Keep exchanged definitions in version control and inspect what changed.
Shared context for agents:
Make modeled business meaning and associated guidance available to supported AI applications.
A shared format helps make those outcomes possible. Actual portability still depends on what each importer and exporter supports, how expressions are interpreted, and how updates reach consuming tools.
What Apache Ossie standardizes
The core specification defines a machine-readable representation of a semantic model. YAML is the format readers will commonly encounter.
The current development schema places a single model directly at the document root. Check the
core specification
and the version your converter supports before preparing a file; earlier snapshots can use different structures.
AI context and extensions
Ossie also supports an
ai_context
field. It can contain text or structured guidance such as instructions, synonyms, and example questions. This lets a definition travel with information that helps an AI application interpret it.
For example, a monthly recurring revenue metric might include “MRR” as a synonym. A consuming application can use that guidance when interpreting a question, provided its integration preserves and uses the field.
Vendor-specific extensions provide a place for attributes outside the shared core. Treat those attributes as potentially nonportable: preserving them in a file doesn't establish that another application understands or implements them.
An Apache Ossie YAML example
The following example illustrates the structure of the
0.3.0.dev0
development schema checked for this article. It defines a dataset and a simple aggregate, rather than a complete finance-approved MRR model.
Here,
source
identifies the warehouse relation. The fields expose attributes from it, and the model-level metric refers to a field using its qualified
dataset.field
name.
Validate your document against the matching
JSON Schema
, then test it with the intended converter. Schema validation checks document structure; it doesn't establish that a metric matches your business definition or that every consumer supports it.
How Apache Ossie works
Ossie provides a shared representation for semantic definitions. Query execution and access to the underlying data remain responsibilities of consuming tools and engines.
A typical exchange has three steps:
Export or author the model.
A tool or converter produces an Ossie document from existing definitions, or a team authors one directly.
Validate and version it.
The document is checked against the intended schema and stored with a clear owner and change process.
Import and test it.
Another application reads the document or converts it into its native semantic model. The team checks both the imported structure and representative query results.
The
converter ecosystem
connects vendor formats to the shared representation. This reduces the need to maintain a separate direct translation for every possible pair of tools.
Conversions can still lose information. One system may support a metric type, relationship behavior, or expression dialect that another doesn't. Review warnings and test a round trip where supported: export a model, import it back, and inspect what survives.
For important calculations, compare results on the same data, filters, and time periods. A successful import isn't enough to establish equivalent behavior.
How ready is Apache Ossie?
Readiness has several parts: the specification version, converter implementation, and support in the products you use. Treating them as one maturity label hides useful detail.
The specification is evolving
As of November 20, 2026, Apache's main core specification identifies itself as
0.3.0.dev0
, an unreleased development version. Its version history warns that the schema is mutable and should not be relied on in production.
Pin the revision you're testing. A development branch can change independently of a converter or integration, and a project announcement doesn't establish compatibility with every subsequent schema revision.
Converter coverage varies
The existence of a converter doesn't establish complete import and export support. Check its direction, accepted input, supported version, warnings, and known gaps.
Start with a representative slice of your model, including the calculations and relationships most important to your business. Include less common features rather than testing only a simple sum.
Product support is version-specific
For example,
Hex's Ossie support
is alpha and uses the Hex CLI to convert files into Hex semantic project files, then sync them through Context Sync. The guide currently documents
0.2.0.dev0
input, distinct from Apache's current development schema.
Check the receiving tool's documented version before using the example above or upgrading a model. Keep the source file and review conversion output before publishing changes.
Do you need a semantic model for AI analytics?
Semantic models are useful for giving agents consistent business definitions, but they’re only part of the context needed for accurate AI analytics.
For a question like “What was net revenue retention last quarter?”, a maintained semantic model can provide the agreed calculation and customer population. Making that definition portable through Ossie helps more tools use the same business logic.
“Why did retention decline, and what should we investigate next?” requires more. An agent may need documentation about a pricing change, details about how a product event is recorded, and findings from an earlier customer analysis. It may also need to develop and test hypotheses that nobody anticipated when the model was built.
Trying to encode every possible investigation upfront creates more work for the data team and limits what people can explore before someone updates the model. Shared metric definitions remain useful throughout that investigation; they just aren't the full set of knowledge the agent needs.
AI analytics should draw on context across the stack: semantic models, warehouse metadata, documentation, repositories, and relevant analytical work. And that context needs to improve as people ask new questions and agents discover useful information.
Ossie supports this approach by making semantic definitions and associated instructions easier to reuse. You can value that portability without requiring all business knowledge to live inside a semantic model.
How this works in Hex
Hex builds on semantic models alongside documentation, metadata, and existing analytical work. Its
Knowledge Engine
brings that context together with knowledge agents discover during analysis, so each new question can build on what’s already been learned.
Ossie makes semantic definitions portable. The Knowledge Engine makes them useful alongside broader business knowledge that grows and improves as agents work.
Getting started with Apache Ossie
You don't need to migrate every definition to assess whether Ossie is useful for your team.
Identify a real exchange.
Choose a source model and a tool where you want to reuse it.
Check both sides.
Confirm supported versions, conversion direction, and feature coverage.
Test a small but representative model.
Include important calculations, joins, types, and AI instructions.
Inspect the output.
Review warnings and identify information that was dropped or changed.
Compare behavior.
Test the same questions and filters against the source and imported definitions.
Decide who maintains it.
Establish a source of truth, update process, and checks for future changes.
Keep improving the definitions and documentation you already use while evaluating interchange. Portability is most useful when the underlying business meaning is clear and maintained.
Definitions that can move with you
Apache Ossie is an effort to make semantic metadata easier to exchange across the data stack. Its value is straightforward: the work of defining your business shouldn't have to be repeated every time you adopt another analytical tool.
The practical next step is to test a real model against the integrations you need. Use the
project documentation
and converter guidance to understand current support, and keep the distinction between intended portability and verified behavior clear.
Frequently asked questions
Who maintains Apache Ossie?
Apache Ossie is a community project undergoing incubation at the Apache Software Foundation. Development happens through public project resources, including repositories and discussion channels. Apache incubation concerns community and project development; it isn't a certification that every integration is production-ready.
Is Apache Ossie the same as Open Semantic Interchange?
Apache Ossie is the current project name for the initiative previously known as Open Semantic Interchange, or OSI. The rename accompanied its move into Apache incubation. Historical OSI materials remain relevant background, but check current Ossie documentation for supported schemas and tooling.
Does dbt support Apache Ossie?
The Ossie converter ecosystem includes a
dbt integration
. Check its current documentation for supported artifacts, conversion directions, versions, and limitations. A converter's availability shouldn't be read as universal native support across every dbt workflow or every semantic feature.
Is Apache Ossie a semantic layer or a query engine?
It is a specification for representing and exchanging semantic metadata. Tools can use that representation to build or consume semantic models, while query planning and execution depend on the implementation. Exchanging a model doesn't by itself provide a running analytics service.
Should you wait for Apache Ossie before investing in semantic models?
No. Maintain useful business definitions in the tools that fit your stack today, and evaluate how you could reuse them elsewhere. Reviewable definitions, clear ownership, and representative tests are valuable now and make future conversion easier to assess. You don't need to model every domain before using AI for a scoped analytical workflow.
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
