---
title: "Introducing the Knowledge Engine"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/knowledge-engine/"
scraped: "2026-11-20T06:00:37.208017+00:00"
lastmod: "2026-11-19"
type: "sitemap"
---

# Introducing the Knowledge Engine

**Source**: [https://hex.tech/blog/knowledge-engine/](https://hex.tech/blog/knowledge-engine/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
Introducing the Knowledge Engine
A new self-learning, graph-based context system for Hex 4.0.
Katherine Harrison
Product
November 19, 2026
Share:
twitter
linkedin
In this article
The Hex Knowledge Engine: a new agent-facing context layer
This all sounds great, so what do I do?
Building for an agent-native world
Get started for free
Today, we’re introducing the Hex Knowledge Engine:
a graph-based, self-learning system that re-imagines the context lifecycle for agents and humans
.
With the Hex Knowledge Engine, agents are able to re-use their own findings along with the context you’ve set up in your Hex workspace. This
makes agents faster, lowers your AI token costs, and gives you more consistent, accurate answers.
knowledge
The Knowledge Engine is now available in
beta
and rolling out alongside Hex 4.0. We look forward to your feedback!
Every time an analytics agent is asked a question,
it makes dozens of small decisions
about which context and data should be prioritized and how to interpret a user’s intent.
For simple questions, it’s simple: just hit a semantic model and pull a metric. But for most work – especially the work that
really matters
– it’s more complex. And organizations evolve quickly, meaning
you can’t rely on having everything perfectly modeled at every moment.
For data teams managing self-service analytics, this presents three challenges:
It’s inefficient.
Every new thread re-searches and re-reasons from scratch, spending time and credits on something another thread may have already learned.
It opens the door for inconsistencies.
Because it’s starting from scratch, there is a decent chance it will come up with a different answer than before. You can try to document every business rule up front (and some teams try), but it’s tough to keep up.
It’s invisible.
You can’t easily get a handle on what judgment calls agents are making without digging into individual conversations one at a time, and that doesn’t scale.
But all of those conversations result in
findings
– knowledge that the agent discovers along the way – that’s
immediately thrown away
.
But… what if it wasn’t? What if that “
context exhaust
” was retained, curated, and compounded?
What if you could observe that work and make use of all of it?
Now, Hex does exactly that, with our graph-based
Knowledge Engine powering Hex 4.0.
The Hex Knowledge Engine: a new agent-facing context layer
The Knowledge Engine is a self-learning system –
picking up knowledge from all your context and agent conversations to form an agent-facing graph
.
This graph then serves as
the primary search interface for all context retrieval and analytics work in Hex
.
Think of the graph as a map of all of the facts Hex knows about how data is defined in your organization, and where they originated:
When you ask a question in a thread with the Hex agent, the agent can reference all of these facts to get to an answer faster.
Agentic knowledge curation
Every night, a background Curator Agent reviews your workspace and adds any new learnings into your graph
. It builds from two sources:
What you’ve defined:
It translates new or changed guides, semantic models, and published projects directly into individual units of knowledge.
What Hex’s agent has learned:
It documents the judgment calls agents made and the context discovery paths they followed while answering questions in your workspace that day.
It then reconciles what it learns.
Duplicates are automatically resolved (e.g., so ten threads that each defined “active customer” all back one unit of knowledge). When you change some documentation in your workspace, like a guide or a semantic model, any associated knowledge is automatically updated.
The agent keeps working in the background to verify and validate knowledge units,
ultimately assigning each a status – from “Verified” to “Debunked” – in order of trustworthiness.
Many teams have inconsistent or conflicting context and don’t even realize it: so when the agent encounters this,
it creates a unit of “contested knowledge,”
so agents proactively know about alignment gaps rather than silently choosing whichever guidance they happen to encounter first.
More efficient knowledge retrieval
The Knowledge Engine is Hex 4.0’s new interface to workspace context. Instead of searching through all of your raw context (like guides, semantic models, repos, and endorsed projects)
the agent now searches the graph to find and reuse existing knowledge
, returning to the raw context or warehouse only when it needs to discover or validate something no agent in your workspace has done before.
You’ll see references to this show up in your agent thinking when you run a Hex thread, like this:
Faster, more consistent answers
Because the Knowledge Engine synthesizes each day’s open-ended agent discovery into distilled learnings, the resulting graph lets agents skip context and data discovery and routes them directly to the table, definition, method, or other source they should use – since earlier agents already did the research to find them. This means
not only fewer tool calls, but also fewer opportunities for agents to make conflicting analytical choices
.
In our own workspace, we’ve observed significant efficiency improvements –
the Knowledge Graph has cut response time by 22% and cost by 25%.
Visibility and steerability
So far so good, but there’s an obvious objection: some people are ignorant and agents aren’t perfect, so
a self-learning system
could
propagate incorrect beliefs
– which means you could get faster
wrong
answers.
And yes – we thought of this!
By codifying the decisions agents in your workspace are
already
making,
the graph functions as an observability surface
into how agents are leveraging your existing context, what they’re learning from it, and what they’re having to come up with in the absence of clear guidance. The Knowledge Engine does the review your data team would otherwise have to, and finds those hidden gaps and inconsistent or incorrect agent behaviors.
And as your agents retrieve and materially rely on knowledge,
Hex tracks when and how often each unit is used
. Commonly held beliefs (and incorrect ones) now come with a signal your data team can act on.
See a learning that doesn’t feel right? That's a signal that the agent couldn't find what it needed.
Update your context
(e.g., a guide, semantic model, or endorsed project) and the Knowledge Engine will embed the change in your graph and reconcile it.
The evolution of context management with Hex
We believe the future is going to be defined around agentic systems that can self-learn, while still providing governance, observability – and ultimately trust.
The Knowledge Engine works
with
your existing governed assets like Semantic Models
– in fact, it makes them work even better. Earlier this year, we launched
Suggestions
– a first step toward “self-learning” that makes gaps in context visible so humans can improve the system. The Knowledge Graph builds on this, taking a more automated approach to self-learning while still keeping your data team in control.
We have much more coming on this front soon!
This all sounds great, so what do I do?
Nothing!
Seriously. If you’re using Hex 4.0,
the Hex Knowledge Engine will run every night, and it will start powering your threads automatically
. You’ll see knowledge powering agent thinking, and your threads will be faster.
If you want to take a peek, you can review contested knowledge, which might indicate inconsistencies in your context layer or places where agents aren’t agreeing.
As graph usage builds up, use the newfound visibility to guide your decisions on where to invest in context management.
Building for an agent-native world
We just rebuilt the backend of our platform to be
truly
agent native,
with the mission to make analytical work faster, cheaper, and more accurate— while reducing the amount of grunt work and overload that data teams and context admins have to contend with.
Agents are already being used to make all kinds of decisions, and we want to help you see them and steer them.
The Knowledge Engine is being rolled out as a preview to workspaces included in the Hex 4.0 public beta starting November 19.
Self-service workspaces are expected to follow in early December.
For a deeper look, you can check out Izzy Miller’s walkthrough from the
Prompt product keynote
.
Note: in the initial beta, the Knowledge Engine only builds from sources that are accessible to everyone in your workspace. As we expand the beta, we'll evolve our authentication controls so as to safely expand its learning opportunities.
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
