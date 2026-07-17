---
title: "Building semantic models in Hex"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/semantic-models-in-hex/"
scraped: "2026-07-17T06:00:50.368536+00:00"
lastmod: "2026-07-15"
type: "sitemap"
---

# Building semantic models in Hex

**Source**: [https://hex.tech/blog/semantic-models-in-hex/](https://hex.tech/blog/semantic-models-in-hex/)

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
Building semantic models in Hex: A playbook for governed & trustworthy metrics
A practical build recipe for Hex admins and data leads
Rafa Carrasco
Data
July 15, 2026
Share:
twitter
linkedin
In this article
Important assumptions
Act I: Prepare the resources for the model build
Act 2: Build the model
Create supporting files for the agent
Maintain it over time
Get started for free
Picture a single KPI; ie. active customers, and three people who need it. A sales lead asks the agent, "how many customers are active right now?" Finance asks, "what's our current active account count?" A PM types "count of users with activity this month" into a notebook. Same metric, three phrasings. The agent
might
answer all three questions exactly the same, but without an anchor for governance, it’s likely to compile three different SQL queries to each user’s prompt.
This is the worst of all worlds: extra lag while the agent re-derives the logic, three different numbers, and crucial edge cases (churned accounts, refunds) quietly dropped by one path but not another.
A governed semantic model fixes that: one question, one agreed-upon answer, for everyone who asks.
It's the single place where your clean tables, their descriptions (metadata), and the plain-English questions people actually ask all line up behind one set of definitions. The agent stops guessing, and every phrasing of "active customers" resolves to the same verified logic.
The goal is trust that holds where it matters most: the moment someone actually
uses
an answer. And you earn that trust the unglamorous way - by checking answers against queries you've already verified, not by hoping the AI behaves. Here's the exact recipe I walk admins through when they're ready to codify their highest-stakes KPIs in Hex.
knowledge
A quick check: you probably don't need a semantic model to get started. Hex's agents can already work from your table and column descriptions, your endorsed (trusted) tables, and your workspace context.
A semantic model is the
most structured
kind of context you can add - so save it for your high-stakes KPIs, the ones where "close enough" isn't good enough
.
It's great at "how much / how many" questions, less so at "why" questions.
Important assumptions
Data warehouse quality
A semantic model adds business meaning on top of your data, so it can only ever be as good as the data underneath it. This playbook assumes the warehouse you're modeling on already holds
gold-standard, highly governed data
. Without that foundation, a model won't save you - it will just make wrong numbers sound more convincing.
knowledge
⚠️  If the underlying data isn't already clean, trusted, and governed, stop here and fix that first. A semantic model is only ever as trustworthy as the warehouse beneath it.
Specifically, this assumes:
Clean, well-modeled tables
- transformed, deduplicated, and tested (e.g., dbt staging/marts), not raw dumps.
Endorsed, production data
- you're pointing the model at trusted tables marked as such, with dev, scratch, and staging excluded.
Reliable joins and table grain
- your tables connect on trustworthy keys and each row means one clear thing, so totals don't quietly double-count.
Existing metadata
- meaningful table and column descriptions already flow through from the warehouse or dbt.
Act I: Prepare the resources for the model build
Curate 5-10 business questions (10 is ideal)
Scope to
one
team, domain, or KPI set. Don't boil the ocean - go after the 20% of your data that answers 80% of the questions, and start with your most
contentious
metrics (the ones where Finance and Sales show up to the same meeting with different numbers).
Write them as real questions a stakeholder would ask:
What was net revenue last month?
How many active customers do we have right now?
What's our average deal size by segment this quarter?
If you can't list 5 questions a domain genuinely argues about, that domain probably isn't ready for a model yet.
Pair each question with a Verified SQL Query (VSQ)
This is critical to get an accurately scoped Semantic Model. For every question, write the
single query your team agrees is correct
- edge cases and all (refunds, cancellations, nulls, currency, what counts as "active"). Put your questions and SQL queries in a
Hex Project
to validate and test.
These VSQs become your ground truth: the answers everything else gets checked against.
Drop them into a single markdown file to use as the foundation of the build.
📓 Hex notebook: Sales KPIs as your ground truth (VSQs)
Cell 1 — Markdown
Copy
**Goal** capture the stakeholder question + the agreed definition (edge cases included).
Cell 2 — SQL
Q1: What was net revenue last month?
Definition: completed order amounts − refunds − discounts.
-- Q1: What was net revenue last month?
-- Definition: completed order amounts − refunds − discounts.
SELECT
SUM(amount - refund_amount - discount_amount) AS net_revenue
FROM orders
WHERE status = 'completed'
AND order_date >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
AND order_date <  DATE_TRUNC('month', CURRENT_DATE);
Cell 3 — SQL
Q2: How many active customers do we have?
Definition: distinct customers with ≥1 completed order in the trailing 30 days.
Copy
-- Q2: How many active customers do we have?
-- Definition: distinct customers with ≥1 completed order in the trailing 30 days.
SELECT
COUNT(DISTINCT customer_id) AS active_customers
FROM orders
WHERE status = 'completed'
AND order_date >= CURRENT_DATE - INTERVAL '30 days';
The discipline of writing these forces the cross-functional agreement that the model is supposed to encode. The conversation
is
the work.
Act 2: Build the model
Hand the project to Hex's semantic modeling agent
In the
Modeling Workbench
, reference your Hex project to the Modeling Agent, using this prompt:
Build a governed semantic model for [Domain KPI] from this Hex Project:
**@<project name>**
The Hex Project contains 5–10 stakeholder questions, each paired with a
Verified SQL Query (VSQ) that my team agrees is correct.
Treat those VSQs as the ground truth / spec for this model — the model's
answers must match them exactly, edge cases included.
**Writing Instructions:**
For every entity, measure, and dimension, write the level of detail you'd
give a sharp new hire on day one: spell out abbreviations, enumerate the
allowed values of categorical fields, note how nulls are handled, and add
synonyms for the words your business actually uses.
**Scope:**
Only model what's needed to answer these questions for the [Sales]
domain. Only use the tables referenced in the Project SQL cells.
Point at our endorsed/production tables only — exclude dev,
scratch, and staging.
The agent will scaffold the model: the entities, measures, and dimensions (your business objects, the numbers, and the ways you slice them) plus the joins between tables. You're not starting from scratch; you're handing the agent a spec it can build against. You can make the prompt as detailed and enriched as needed.
Example prompt for the semantic modeling agent: tailor the prompt with any context the agent needs that are specific to the model, your business and your data warehouse.
knowledge
💬 Build a governed semantic model for [Sales KPIs] from this Hex Project - @Project-Name
This Hex Project that contains [N] stakeholder questions, each paired with a Verified SQL Query (VSQ) that my team agrees is correct. Treat those VSQs as the ground truth / spec for this model — the model's answers must match them exactly, edge cases included.
Scope:
Only model what's needed to answer these questions for the [Sales] domain. Point at our endorsed/production tables only — exclude dev, scratch, and staging.
Check for detailed and accurate descriptions
Descriptions are what give an agent context. After the agent writes the model, check every entity, measure, and dimension to ensure the descriptions match the Business Context. The agent leans on this context when a question doesn’t map cleanly.
Test your ground-truth queries against the model
Test your model
in the workbench by running your original questions
through the model
and compare the answer to your VSQ. Think of these as a checklist you re-run every time the model changes — the answers should never move unexpectedly. As you check results, verify:
Definitions
- does "net revenue" match your canonical SQL?
Measures
- are aggregations (SUM, COUNT DISTINCT) doing what you intended?
Joins
- is the agent using the right relationships between tables?
Dimensions
- can you group and filter the way stakeholders will ask?
Keep this question set around. Every time you change the model, re-run them.
Create supporting files for the agent
Write a guide
to inform the AI of your model
A model tells the agent
how
to calculate. A guide tells it
when to reach for the model at all,
and when not to. Keep guides small and tightly scoped, with a clear title and description at the top so the agent knows when to reach for them:
---
title: Sales KPIs Semantic Model — Usage Guide
description: Use for revenue, bookings, and active-customer questions for the
Sales org. Governs when to rely on the Sales KPIs semantic model.
---
## When to use this model
- "How much / how many" questions about revenue, bookings, active customers.
## When NOT to use it
- "Why" questions (root cause, drivers) — query the warehouse directly.
- Anything outside Sales (product usage, support, etc.).
## If the data isn't in the model
- Don't guess or swap in a look-alike metric.
- Say it isn't covered, and point to the closest endorsed table.
That last section, what to do when the answer
isn't
in the model, is what separates a model that says "I don't know" from one that confidently makes something up.
Reference it in workspace context file
Hex.md
- one line
Your workspace context is appended to every agent prompt, so keep it short. You're not re-explaining the model here, just pointing to it:
Copy
For Sales revenue, bookings, and active-customer questions, use the
Sales KPIs semantic model and follow the Sales KPIs Usage Guide.
One line is enough to make the model and its guide discoverable across the workspace.
Maintain it over time
A semantic model isn't just a one-time build. As the business evolves it should take in new metrics and answer new questions. Use
Context Studio
as your observability loop: watch where agents hit ambiguity or throw warnings, review the suggested patches, and feed what you learn back into the model, descriptions, and guide. Assign a clear owner for each domain's model. The teams that win here are the ones who keep closing the loop.
The short version:
scope to one domain, anchor on 5-10 questions with verified queries, let the Modeling Agent build, test against your ground truth, describe everything richly, wrap it in a guide, surface it in workspace context, then keep tending it. Do that, and the same question returns the same verified answer for everyone, whether it's an analyst writing SQL, a business user asking in plain English, or a stakeholder reading a dashboard. That's what makes self-serve analytics trustworthy enough to actually use.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
More on Data
BLOG
Supporting the Open Semantic Interchange
Barry McCardel
·
September 23, 2025
Hex joins the Open Semantic Interchange consortium
BLOG
Semantic modeling: how to build a single source of truth for your data
The Hex Team
·
February 13, 2026
A semantic model translates raw database schemas into consistent, governed business metrics. Learn how to build and scale one for your analytics and AI.
BLOG
Introducing Semantic Authoring
Andrew Lee
·
August 20, 2025
Data teams can author semantic models right inside of Hex using the Modeling Workbench to build context and trust for humans and AI agents.
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
