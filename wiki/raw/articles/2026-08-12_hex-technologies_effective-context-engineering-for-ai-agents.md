---
title: "How to Improve Agent Efficiency Through Context Engineering"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/effective-context-engineering-for-ai-agents/"
scraped: "2026-08-12T06:00:22.205435+00:00"
lastmod: "2026-07-17"
type: "sitemap"
---

# How to Improve Agent Efficiency Through Context Engineering

**Source**: [https://hex.tech/blog/effective-context-engineering-for-ai-agents/](https://hex.tech/blog/effective-context-engineering-for-ai-agents/)

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
How to improve agent efficiency through context engineering
Your analytics agent returned a clean, confident, completely wrong number. The fix isn't a better model.
The Hex Team
Data
July 17, 2026
Share:
twitter
linkedin
In this article
What context engineering is (and why it beats model choice)
Four techniques for structuring what your agent sees
Context rot: how agent performance degrades and how to catch it
The token economics of context at scale
What separates production agents from prototypes
Where to start with the governed context
Frequently Asked Questions
Get started for free
You point an analytics agent at your warehouse, ask a revenue question, and get a confident, cleanly formatted, completely wrong answer. The agent queried a deprecated table, and nothing in the output flagged it. Understanding
why analytics agents break
starts here: the failure mode is almost always missing context, not missing capability.
Most context engineering guides focus on token budgets and retrieval-augmented generation (RAG) pipelines. For analytics agents, the bigger constraint is
data governance
. An agent with no governed metric definitions gives confidently wrong answers no matter the model. This is the core of Hex's approach to
AI-native analytics
: governed context moves accuracy more than model choice. In Hex's
State of Data Teams
research, 77% of data professionals were excited about AI, yet only 3% were prioritizing it, largely because teams lacked the governance foundation to move past prototypes.
What context engineering is (and why it beats model choice)
Context engineering is the discipline of curating and maintaining the information a model sees during inference. Andrej Karpathy
described it
as filling context windows with "just the right information for the next step." The goal is to give the model the smallest, highest-signal set of information that maximizes the likelihood of the desired outcome.
If that sounds like prompt engineering, the difference is scope. Prompt engineering refines the instructions you write. Context engineering governs everything the model sees, across every turn: tools, retrieved data, message history, and business definitions. Once a system runs for many turns, the instructions become a small fraction of the total context, and curating the rest becomes the actual engineering work.
A paired benchmark
ran 100 questions against a retail dataset with three frontier models, once with schema access only and once with a 4 KB context-layer document added. With schema only, the models scored 45.5–50.5%, too close to distinguish statistically. With the context layer, all three converged at 67.7–68.7%, again indistinguishable.
The context layer accounted for essentially all significant performance differences. The same pattern shows up beyond that one benchmark: moving from raw schema access to governed metric definitions improves results without changing the underlying model.
On
Spider 2.0
, which tests enterprise-level text-to-SQL complexity, GPT-4o drops from 86.6% on the original Spider benchmark to 10.1%. Upgrading the model alone is unlikely to close that gap. Writing down what your metrics mean can move accuracy more than swapping in a more expensive model, which is why
evaluating AI tools
by model benchmarks alone misses the point.
Four techniques for structuring what your agent sees
Context engineering work falls into four practical patterns. Teams write context outside the window, select what to pull in, compress what's there, and isolate contexts from each other. In analytics work, each pattern maps to something your team probably already has, though making it machine-readable takes deliberate effort.
1. Retrieval: warehouse metadata and endorsed tables
Analytics agents need schema metadata, table descriptions, and column-level context to generate accurate SQL. That means documentation for your warehouse architecture doubles as retrieval infrastructure. But retrieval quality cuts both ways: research on text-to-SQL shows that schema retrieval noise degrades accuracy. A smaller, curated set of high-relevance tables produces less noise than a large, undifferentiated catalog.
In Hex, the lightest form of this curation is endorsing tables: marking which sources are trusted so agents search those first, or exclusively. As we put it, endorsing your most-queried tables and adding column descriptions prevents the most common class of wrong-table errors before you've written a single semantic model.
A guide file plays the knowledge role (more on that below) by encoding institutional knowledge that doesn't fit neatly into a schema, including which tables to prefer for which questions, what filters to always apply, and how to handle the edge cases that trip up even experienced analysts. Setting up your
data connections
so agents can reach trusted sources is the first step.
2. Memory: previous analyses and published notebooks
General-purpose agents often build memory by writing files or otherwise storing reusable state outside the context window. Data teams have an advantage here because the highest-signal memory already exists as shipped work. Published agentic notebooks in the
notebook environment
, prior analyses, and existing dashboards contain joins, filters, and metric logic that someone already vetted, tested, and reviewed. An agent that can reference that prior work inherits the reasoning instead of re-deriving it from raw tables, which is both faster and less likely to drift from how the team actually defines things.
3. Institutional knowledge: workspace guides
For chat agents, knowledge means summarizing long conversations. For analytics agents, the more valuable move is documenting institutional knowledge up front: the fiscal calendar quirk, the "always exclude test accounts" filter, the convention that pipeline questions use the CRM-synced tables. The Hex workspace guide constraint keeps it tight: keep it under 300 lines, 800 words maximum. That limit reflects a high-signal approach to
governance best practices
applied to the business context. If a rule doesn't change agent behavior, it's noise competing for attention with the guides that do.
4. Codified metrics: semantic models
Semantic models give agents a deeper form of truth: they hold the business logic constant across sessions so the agent doesn't have to reconstruct it from scratch. In MetricFlow terms, a definition encodes not just what to compute, but how: the entity, the measure, the filters, the grain.
Teams can author semantic models natively through
semantic authoring
in Hex or sync them from existing sources through
semantic model sync
with dbt MetricFlow, Cube, or Snowflake Semantic Views. Define the metric once, and queries use the same governed definition across users and sessions. Without that, each conversation may re-derive joins and metric logic from scratch, and the same question can return different answers on different days.
Context rot: how agent performance degrades and how to catch it
Context rot describes the finding that model performance degrades as input context grows, even well within advertised limits. Long-context research shows degradation can happen even when relevant evidence is present and placed favorably. Position matters too.
The Stanford
"lost-in-the-middle" research
showed models handle information at the start or end of a context far better than information buried in the middle. The effective context window, where quality actually holds, is often much smaller than the number on the spec sheet. (For more on how
vanity evals
can obscure real-world performance, here are what benchmarks actually measure.)
Analytics context also ages in ways benchmarks don't capture. Tables get deprecated, metric definitions change, and last quarter's workspace guides quietly become wrong.
Data trust
erodes when context drifts, and nobody catches it. Analytics context can also fail through direct conflict: information accumulating in the same context can contradict other information already there. The analytics version is an agent holding two revenue definitions, one net of refunds and one gross, and producing internally contradictory analysis without flagging it.
Teams usually catch context rot through a few recurring signals.
Ground truth and snapshot testing.
Keep a set of questions with known-correct answers and rerun them whenever context changes. Compare outputs to stored snapshots to catch drift before users do.
Trajectory evaluation.
For multi-step agents, inspect the path, not just the answer: did it query the endorsed table or a lookalike? Aggregate accuracy metrics can miss reasoning failures that a trajectory review would catch immediately.
Conversation-length trends.
If success drops as sessions grow, context management is the suspect, not the model.
Token efficiency tracking.
Sudden spikes in token usage often signal a context problem upstream: duplicated retrieval, runaway history, or conflicting guides forcing the agent into longer reasoning chains.
Ongoing evaluation.
Treat evaluating data agents as a continuous practice, because context and model versions shift over time, and a passing benchmark today can fail next quarter.
You can only write guides for questions you know people are asking, which leaves the gaps you can't see. That's the job
Context Studio
does inside Hex: it surfaces what questions users actually ask agents, where quality issues cluster, and which topics are leaning on unstructured data. Then it recommends specific context improvements. Instead of guessing which semantic model to build next, the data team invests governance effort where observed agent behavior says it's needed.
The token economics of context at scale
Once an agent runs hundreds of sessions a day, prompt caching is often one of the biggest cost levers. A
prompt caching evaluation
across 500+ agent sessions found that caching cut API costs 41–80% and improved time-to-first-token 13–31%. For repeated 50K-token prompts, the cost difference can be material when cache reads are discounted relative to standard input.
Combine caching with just-in-time retrieval and model routing, and the savings compound when the implementation is careful. Because prompt caching depends on keeping stable prefixes intact, append-only context design is a cost decision as much as an architectural one.
At scale, context engineering becomes recurring infrastructure unless the
AI analytics platform
handles the plumbing. A DIY context pipeline means owning ingestion, embeddings, vector search, permissions, and evaluation. That creates maintenance overhead, operational risk, and engineering time that could go to actual analysis. None of that maintenance is analytics work.
When the platform handles context engineering, that plumbing comes built in, and the data team's job narrows to what no vendor can do for them: curating the business context. Which tables are trustworthy, what "active customer" means, and which filters always apply. That curation is analytics engineering work pointed at a new consumer.
What separates production agents from prototypes
Production analytics agents differ from prototypes because teams evaluate them continuously, govern their context, and watch real usage after launch. That discipline matters because
Gartner predicts
over 40% of agentic AI projects will be canceled by the end of 2027 due to escalating costs, unclear business value, or inadequate risk controls. That forecast illustrates the gap between experimentation and production scale, and most of the gap comes down to
preparing for AI agents
with the right
governance framework
.
Production maturity is a spectrum you climb, not a wall you build first.
Endorse tables and write column descriptions.
The lightest intervention, doable this week, eliminates the most common wrong-table errors on its own.
Add workspace guides.
Short markdown files that capture conventions and edge cases every experienced analyst knows, like which fiscal calendar to use or which customer segments require special filters.
Build or sync semantic models.
Author them natively or sync from dbt MetricFlow, Cube, or Snowflake Semantic Views, giving teams shared metric definitions and deterministic SQL generation across supported Hex workflows.
Close the loop with observability.
Watch real agent interactions to see where context is thin, then deepen governance exactly there.
The list deliberately omits "complete your semantic layer before anyone touches an agent." Semantic models are the heaviest level of the spectrum, and they're a destination you grow into, guided by what observability shows.
Syncing semantic models into Hex from dbt MetricFlow, Cube, or Snowflake gives every user the same SQL-backed logic, so Threads returns
self-serve answers
against definitions analysts can audit rather than against whichever table the agent guessed. When analysts can audit governed SQL-backed logic, users can act on answers without chasing definitions.
This played out at
PandaDoc's team
, where Hex's Semantic Model Sync with Cube helped Threads answer questions 75% faster. The governed model made the faster path auditable, which matters more than speed by itself.
That is the production pattern worth copying: make the governed path faster than the ungoverned one.
Where to start with the governed context
Context engineering for analytics agents is mostly governance work: deciding which tables and metric definitions the agent can trust. Model choice often matters less once those definitions exist. Pilots fail from missing evaluation rather than missing capability. And the real cost of a wrong answer is everything that happens after it ships.
The order matters less than the loop: start where context is already clear, then deepen governance where observed agent behavior shows ambiguity. Hex's context tools let the people who know the data best encode and inspect that governance so business users get answers grounded in context that support
trusting AI analytics
at scale. If a data team's hard-won knowledge of the business is the highest-signal context an agent can have, the platform's job is to make that knowledge easy to encode and easy to inspect.
Ready to see what governed context does for your agents?
Request a demo
or
start a free trial
.
Frequently Asked Questions
Do We Need a Semantic Layer Before Deploying an Analytics Agent?
No, because the first production risk is usually ambiguous source selection, not the absence of a complete metric catalog. Endorse your most-queried tables and add column descriptions so the agent starts from trusted sources on day one. Build semantic models when repeated usage reveals ambiguity around specific metrics. Tools like Context Studio show where deeper governance will pay off, and a team practicing
agentic analytics
can start generating value before the semantic layer is complete.
How Is Context Engineering for Analytics Agents Different from Standard RAG?
RAG retrieves text that looks similar to the question, which works for documents but breaks on metrics. Analytics questions need deterministic answers: "revenue" must compute the same way every time, not whichever way the most similar retrieved passage suggests. Governed definitions, which encode the entity, measure, filters, and grain of each metric, outperform document retrieval for warehouse questions. RAG can still help with unstructured context, like documentation, but it can't substitute for a governed definition of what your numbers mean.
How Much Context Should Go into an Agent Guide File?
Keep it under 300 lines and 800 words maximum, per Hex's documented constraint. Don't duplicate table endorsements or metric formulas there, since those belong in endorsements and semantic models respectively. Guides files are for conventions a schema can't express: preferred tables for common question types, filters that should always apply, and fiscal calendar quirks. If a rule wouldn't change how an agent answers a real question, cut it, because every low-signal line competes for attention with the lines that matter.
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
You have opted out of data tracking
