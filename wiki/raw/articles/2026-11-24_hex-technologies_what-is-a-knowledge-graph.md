---
title: "What is a knowledge graph?"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/what-is-a-knowledge-graph/"
scraped: "2026-11-24T06:00:34.507676+00:00"
lastmod: "2026-11-23"
type: "sitemap"
---

# What is a knowledge graph?

**Source**: [https://hex.tech/blog/what-is-a-knowledge-graph/](https://hex.tech/blog/what-is-a-knowledge-graph/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
What is a knowledge graph?
A knowledge graph connects information with explicit meaning, helping people and software understand how entities, concepts, and facts relate.
The Hex Team
Data
November 23, 2026
Share:
twitter
linkedin
In this article
What a knowledge graph is made of
How a knowledge graph gets built
Knowledge graph vs. graph database
Knowledge graph examples and use cases
Knowledge graphs and LLMs
Knowledge graph vs. semantic layer for analytics
Do you need a knowledge graph?
Agents that know what your data means
Frequently Asked Questions
Get started for free
An AI agent can answer a business question incorrectly when it misreads a metric or can't follow a relationship. Agents need to know what your data means, which has brought "knowledge graph" back into vendor discussions about understanding your business. A knowledge graph stores facts as entities and the relationships between them, with a schema or ontology defining which kinds of things and relationships you can record so people and machines can follow the connections.
With Hex, you ask what's happening now in Threads, act on the answer through
generative data apps
built with App Builder, and check where a number came from in Context Studio. Hex's agent gets business meaning from semantic models (metric and dimension definitions), endorsed tables, warehouse descriptions, and
workspace guides
. For analytics questions about metrics and tables, that context can be enough; a graph helps when you need to trace relationships across systems.
You'll learn what a knowledge graph is, how to build one, where knowledge graphs are used, and how they compare with semantic models and semantic layers for analytics.
What a knowledge graph is made of
You can break a knowledge graph into three basic parts. Entities are the nodes: customers, accounts, products, places, people. Relationships are the edges that connect two entities, and each edge has a type, such as "owns" or "located in." Properties give details about an entity, like a name or a signup date.
Here's a tiny example written out as facts:
Acme Corp owns Account 4471.
Contract 2024-118 governs Account 4471.
Contract 2024-118 covers the EMEA region.
Acme Corp has the name "Acme Corporation."
Each line follows the same subject, predicate, object shape, so we call these facts triples. The first three link two entities. The last attaches a plain value, so it works like a property. Because Account 4471 appears as the object of the first two facts, you can walk from Acme Corp to the EMEA region in three hops without anyone writing that connection down directly.
The ontology is the rulebook for the graph. It declares which entity types exist (Customer, Account, Contract, Region) and which relationships can connect them, so "covers" can only point from a Contract to a Region. The W3C standard for writing ontologies is
OWL 2
, which describes domains in terms of classes, properties, individuals, and data values.
How a knowledge graph gets built
You typically build a knowledge graph in four stages. Expect most of the hard work in the middle two.
Pull from sources by mapping structured data, such as database tables, to entities and relationships with rules. For documents, use extraction software to find entity names in text and the relationships between them.
Resolve duplicates through entity resolution, merging records such as "Acme Corp" in your CRM, "ACME Corporation" in billing, and the domain on a support ticket into a single entity when they describe one company. Comparing every record against every other gets expensive fast, so teams group likely matches first and compare within each group.
Store the facts in a graph database or a triple store; many teams use RDF, the W3C data model in which every fact is a subject, predicate, object triple. RDF 1.1 has been a
W3C Recommendation since 2014
, and RDF 1.2 is still working through the standards process.
Query the graph with a graph query language. For RDF data, that's
SPARQL
, which matches patterns across connected facts ("find every account whose contract covers EMEA").
Keeping the graph current takes ongoing work and people to own it. As new records arrive and the business adds a product line, the team maintaining the ontology has to decide whether it needs a new entity type. Then the cycle starts again.
Knowledge graph vs. graph database
You use a graph database to store and query data. A knowledge graph supplies the content inside it. The database holds nodes and edges and can run traversals (follow connections) quickly, whether it uses a property graph model (nodes, edges, and properties) or stores triples. In a knowledge graph, you connect and type facts, using the ontology to give them meaning. Random edges alone don't make a graph database a knowledge graph. A knowledge graph's data can also stay in a relational database, exposed as a graph through mappings. That's often called a virtual knowledge graph.
Knowledge graph examples and use cases
You'll find knowledge graphs wherever you ask how things connect rather than how much of something there is.
Web search. Google launched its Knowledge Graph in
May 2012
with the line "things, not strings." A search for the Taj Mahal could resolve to the monument or the musician, and the panel beside the results showed facts about that specific entity.
Recommendations. By linking items through shared attributes (same director, same ingredient, same brand), you let a recommender suggest things a user never interacted with directly.
Fraud rings and entity resolution. Accounts that share a device, an address, or an intermediary can look unrelated in a table. In a graph, you can spot the ring by following the shared node.
Biomedical research. Researchers use graphs connecting compounds, genes, diseases, and pathways to trace whether an existing drug reaches a disease through a chain of biological relationships. That's one route to drug repurposing.
Supply chains. Many companies only see their direct suppliers. With a supplier graph, you can see who supplies the supplier and trace a disruption three tiers away to a product.
You can also use these connected facts as context for a language model.
Knowledge graphs and LLMs
You can use a knowledge graph to ground a large language model (LLM) in facts and relationships it wouldn't otherwise have. GraphRAG is one name for this pattern. An LLM reads a document collection, extracts entities and relationships into a graph, and groups closely related entities into summarized clusters. At question time, the system pulls the relevant facts and summaries from the graph and adds them to the model's prompt, which helps with questions that span many documents or need several hops of reasoning.
Business users also need ways to supply context as their questions change. In Hex's
Threads
, they can ask follow-up questions in plain language and reference published apps as context. Context Studio helps the data team find context gaps, a practical part of
trusting AI analytics
.
Knowledge graph vs. semantic layer for analytics
Knowledge graphs record entities and relationships, semantic models define metrics and dimensions, and the
semantic layer
turns metric requests into consistent SQL. Practitioners don't use these words consistently, so treat this table as a working distinction rather than a standard.
You can answer most analytics questions by querying warehouse tables, a starting point for
AI analytics
. "What was net revenue retention last quarter?" and "Which regions grew fastest?" are aggregates over facts you already store. To answer them well, an agent needs the meaning of those tables: which table is the trusted one, how ARR is calculated, when your fiscal year starts, and that "active customer" means a transaction in the last 90 days. Trusted tables and projects, metric definitions in semantic models, warehouse metadata such as table and column descriptions, and written rules and guides carry that meaning. Many teams get there without building a graph.
Start with endorsed tables and warehouse descriptions, then add workspace guides. Hex's agent can use that context before you add semantic models through Semantic Authoring in Hex or Semantic Model Sync from existing models. Hex's
Context Studio
closes the loop by showing the data team which context sources shaped an answer and raising warnings where context was missing or the user doubted the result. That shows you where to invest in deeper definitions next. PandaDoc uses Semantic Model Sync with Cube to share context. In Hex,
PandaDoc's team
gets answers 75% faster with Threads.
Use a graph when you need to follow relationships. You might link a payment record, a support ticket, and a CRM contact to one person, find every subsidiary under a parent company, or trace which products depend on a supplier you've never contracted with. For formula disputes, define the metric instead. If your dashboards disagree on churn, a graph of thousands of connected concepts won't settle the formula, but a metric definition will.
Do you need a knowledge graph?
If your hardest questions concern metrics and tables, start with trusted tables, descriptions, and definitions. If they concern relationships and identity, a graph may be worth the build. Assess that choice against your own data:
Do your hardest questions ask how records connect across systems, or how numbers add up inside your warehouse?
Do several systems describe the same real-world customer, product, or supplier in ways you can't reconcile with keys and joins?
When an agent gets an answer wrong, is it because it misread a metric, or because it couldn't follow a relationship?
Do you have people who can own an ontology and keep it current as the business changes?
Balance the need to trace relationships against whether your team can keep the ontology current.
Agents that know what your data means
Clear context gives business users
self-service analytics
without waiting in a queue and keeps your team pulling the same trusted number. Whether that context lives in a graph, a semantic model, or a well-described table, the goal is agents that know what your data means.
To plan that context step by step, get
The Data Leader’s Guide to Agentic Analytics
.
Frequently Asked Questions
Is a knowledge graph the same as a semantic layer?
A knowledge graph and a semantic layer do different jobs, though some vendors use the terms loosely. You use a knowledge graph to record entities and how they relate, typed by an ontology, across documents, systems, and domains. A semantic layer usually sits on top of warehouse tables and turns requests for governed metrics into consistent SQL. Some teams connect the two. You get identity and relationships from the graph and calculations from the semantic layer.
Do you need a knowledge graph for AI analytics?
You usually don't need a knowledge graph to start with AI analytics. Start with trusted tables, column and table descriptions, and metric definitions. A graph helps when the relationships are the question, such as resolving one customer across several systems or tracing dependencies through a supplier network.
What's the difference between a knowledge graph and an ontology?
You use an ontology as the schema and a knowledge graph for the facts that follow it. In the ontology, you define classes like Customer and Contract, the relationship types between them, and constraints on those relationships. In the graph, you store actual instances, such as a specific company and the specific contract it signed. Description logic research calls these the TBox for the schema and the ABox for the facts. In practice, the line between them can blur.
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
