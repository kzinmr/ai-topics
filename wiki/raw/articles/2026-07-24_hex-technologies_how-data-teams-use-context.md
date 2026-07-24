---
title: "How the best data teams obsess over context"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/how-data-teams-use-context/"
scraped: "2026-07-24T06:00:47.182561+00:00"
lastmod: "2026-07-23"
type: "sitemap"
---

# How the best data teams obsess over context

**Source**: [https://hex.tech/blog/how-data-teams-use-context/](https://hex.tech/blog/how-data-teams-use-context/)

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
Accuracy and AI analytics: How the best data teams obsess over context
AI analytics depends on context for trusted answers. Here's how data teams at Ramp, Underdog, and Hover build and manage that context with Hex.
James Rajasingh
Data teams
July 23, 2026
Share:
twitter
linkedin
In this article
Ramp: One source of truth, kept in sync
Underdog: Start from what you have, build from there
Hover: Context gets better with every question
Get started for free
Thousands of companies use Hex to ask and answer questions with their data. But how do they trust those answers to be accurate and consistent? It starts with context.
Just as you’d train a new analyst on the definitions, metrics, business terminology, and table relationships that your business runs on, analytics agents rely on that same context to return answers people can trust.
While teams using Hex come from different levels of context maturity, their approach is largely the same: activate the latent context that already exists across dbt, docs, tables, and more so users can actually start asking questions. Then let the agent's answers guide what to sharpen next and where.
Here's a glimpse into how a few of these customers — Ramp, Underdog, and Hover — have approached building and managing context at their organizations.
Ramp: One source of truth, kept in sync
At
Ramp
, data scientists like Ricky Meyers build the data foundations that the rest of the company relies on to explore data with AI, and trust the answers.
Building that trust starts with context, and for Ricky and team, that begins in dbt. It's where their data models already live, and it’s where the data team maintains what they call domain docs: plain-language markdown files that spell out core concepts, key metric definitions, and which tables are relevant for a given part of the business.
Ramp doesn't have to rebuild any of this in Hex. Using
the dbt integration
, Hex is able to read the model descriptions directly, while Hex's
GitHub Action for context guides
syncs Ramp's domain docs on every merge. When something changes in dbt, it changes in Hex too.
dbt is our single source of truth, and Hex stays in lockstep with it.
Ricky M.
— Product Data Scientist, Ramp
Beyond helping the agent make sense of their models and domains, the Ramp team also steers it towards the tables that matter most. They tag their most trusted models as endorsed in dbt, whether that's a canonical transactions table, a users model, or something similar, and
sync those endorsements into Hex
via the API. It’s a low-effort, high-reward signal that keeps the agent focused on the models the team has invested in instead of raw or less-vetted tables nearby.
Importantly, none of this is set-and-forget. In Context Studio, Ricky can observe what's being asked of the agent and where answers run into trouble. When the agent hits a gap in context,
a warning and suggested fix is automatically raised
, which Ricky can programmatically apply back in dbt and sync to Hex.
I like the warning and suggestions. They show me where our docs have gaps, when people are running into them, and how to fix.
Ricky M.
— Product Data Scientist, Ramp
The payoff is what’s possible for everyone else at Ramp. Less-technical users can now self-serve data questions from anywhere, whether that's a product marketer working with the agent to build a launch reporting
dashboard
or a risk underwriter @-mentioning the Hex agent
in Slack
to get answers to a quick question raised in the channel.
Underdog: Start from what you have, build from there
When Camden Willeford joined
Underdog
to lead analytics engineering, his first task was to stand up conversational analytics. Unlike his previous experiences evaluating traditional BI tools for what was the best dashboard builder, he was now looking for a platform that could absorb the context already scattered across Underdog's stack and turn it into leverage for AI analytics.
His first move wasn't to start building out context. It was to take inventory of what Underdog already had: the queries analysts had written, the questions stakeholders kept asking in Slack, the documentation living in Notion, and the models already in the warehouse. Underdog didn't need to invent context. They just needed to activate what was already there.
My advice: Don’t try to model and document everything up front. Find leverage from the context you already have.
Camden W.
— Engineering Manager, Analytics, Underdog
Camden's team pulled and organized that existing context into markdown files in Underdog's dbt repo: business logic, table documentation, FAQs, the concepts scattered across Slack and Notion. Hex's
GitHub Action for context guides
then pushed those files into Hex as guides on every merge. For Camden, this meant no two sets of books, no maintaining context in two places. The repo was the source of truth, and the Hex agent absorbed it.
Some of Underdog's context lives directly in code. Instead of Camden translating data models and transformation logic into markdown files, Hex reads it directly via
reference repos
, letting the code itself be context for the agent.
While aggregating existing context, the Underdog team also worked on defining core metrics of the business. This is where they turned to semantic models: pre-defined metrics, documented joins, and column descriptions that travel from dbt into Hex, so the agent wasn't guessing how a metric was calculated or how to join two tables. Over time, the Underdog team has built these out in dbt as questions come up and the business makes clear which definitions need to be locked down.
For Camden, the biggest shift with conversational analytics is how tight the feedback loop gets. Every question from a user is either a hit or a signal about what's missing, and the team acts on those signals weekly.
Context Studio
groups the week's conversations into topics and flags
warnings
where the agent hit a gap. A GitHub Action then pulls the subsequent
suggestions down through the Hex CLI
, hands them to Claude with access to Underdog's repo, and opens a pull request proposing specific changes. Camden reviews it like any other PR and the wheel keeps turning.
Every Thursday I have a PR waiting that says: update these models based on the real conversations that happened in Hex. You'd never have that in a traditional BI world.
Camden W.
— Engineering Manager, Analytics, Underdog
Hover: Context gets better with every question
At
Hover
, conversational analytics is now the primary way people work with data. For Brian Nguyen, Director of Analytics Engineering, and his team, getting there hasn't meant modeling out every measure, dimension, and join across their business. Instead, they focused on low lift, high impact steps like documenting all their key tables and columns with clear and robust descriptions and relationships. This simple foundation made the Hex agent noticeably more precise across their data, giving the team confidence to immediately start pilots across a few teams.
With table descriptions and column definitions alone, the moment we turned on the Hex agent, it was just way better. Just like out of nowhere.
Brian N.
— Director of Analytics Engineering, Hover
From there, adoption spread quickly, and their context grew alongside it. Brian's team prioritized where to start by talking to leaders across the org, figuring out where daily reporting usage was the highest, and layering in deeper context for those domains first. This meant they had to understand how PMs, sales leaders, and finance teams thought about the business and asked questions.
Rather than making the analytics team a bottleneck for documenting that knowledge, the team anchored the process on simple markdown files that subject matter experts across the business could directly contribute to from accessible tools like Google Docs. Once reviewed, they became
guides
in Hex via a
GitHub Action
. This way, domain knowledge came from the domain owners; and the analytics team could focus on keeping the standards.
For Brian, keeping context sharp is a continuous process, especially at a fast-moving company where the business is always changing. To keep up, his team is starting to lean on the
Context Studio
to surface
suggestions
where the agent's running into gaps. They then pull those suggestions down
via the CLI
, aggregate them, and identify the patterns that appear most often. That lets them prioritize the highest-lift updates and get ahead of gaps before people run into bad answers, rather than waiting for stakeholders to flag them.
Context engineering is a constant state of maintenance. It's never really a one-and-done situation.
Brian N.
— Director of Analytics Engineering, Hover
Conveniently, building context at Hover isn't always deliberate. Because projects in Hex are
referenceable by the agent
, every data app and dashboard they build and endorse becomes reusable context. Business users can
ask questions against vetted analytical work
that's already been built, allowing the agent to reuse proven logic instead of starting from scratch.
Getting a data answer at Hover used to mean waiting on someone else. Now anyone, from product to sales to finance, can ask questions and build data products in plain language. And instead of spending their time answering one-off requests, Brian's team can now invest in the context foundations that makes trustworthy self-service possible.
Every team starts from a different state of context maturity for agentic analytics. There will always be nuances in the state of your documentation, dbt projects, warehouse maintenance, and more.
That said, what’s consistent among the most successful data teams is they don't wait on a perfect setup to get going. They start from what they already have, learn where to focus from real usage, and continuously sharpen context as they go.
At Hex, we're making that workflow feel effortless, so curating context for agents feels a bit like magic.
Explore Context Studio
to learn more.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
More on Data teams
BLOG
How we built a lab to evaluate data agents
Izzy Miller
·
May 22, 2026
We built a synthetic $129M business just to test our data agent. Here's the eval architecture, what it catches, and what still doesn't work.
BLOG
Your code knows things your warehouse doesn't
Andrew Lee
·
May 15, 2026
BLOG
Are Semantic Layers the Cornerstone for AI Analytics?
Charles Schaefer
·
June 10, 2026
Semantic layers are useful. They're just not sufficient for AI analytics — and vendors won't say so. Here's what Context Studio does differently.
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
