---
title: "How Underdog powers 10,000+ data conversations with dbt and Hex"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/how-underdog-powers-conversational-analytics-with-dbt-and-hex/"
scraped: "2026-11-19T06:00:52.434507+00:00"
lastmod: "2026-11-18"
type: "sitemap"
---

# How Underdog powers 10,000+ data conversations with dbt and Hex

**Source**: [https://hex.tech/blog/how-underdog-powers-conversational-analytics-with-dbt-and-hex/](https://hex.tech/blog/how-underdog-powers-conversational-analytics-with-dbt-and-hex/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
How Underdog powers 10,000+ data conversations with dbt and Hex
Making conversational analytics smarter with every question.
Camden Willeford
Friends of data
November 18, 2026
Share:
twitter
linkedin
In this article
1 / The stack
2 / Four files, not two
3 / What this looks like in practice
4 / Turn conversations into dbt improvements
5 / Treat context like production infrastructure
Where to start? The context you already have.
Get started for free
knowledge
This is a guest post by
Camden Willeford
from Underdog, explaining how his team has built out conversational analytics with Hex + dbt.
Traditional BI has always revolved around data teams attempting to anticipate the questions the business will ask, whether by modeling an intricate semantic layer or building a bunch of dashboards. And then hoping everybody finds the answer they need.
We’ve mostly stopped doing that at Underdog.
More than 200 people have had over 10,000 analytics conversations with the
Hex agent
in Hex,
Slack
, and
Claude
. Instead of requesting a dashboard, people ask the question they actually have, follow it wherever it goes, and move on.
That might sound like it makes our dbt work less important. But it’s actually the opposite.
Once people can ask basically anything, the hard part is no longer giving them an interface for querying data. It’s making sure the agent that’s answering actually understands our data.
What does
registered user
mean?
Which table should it use?
Should employee accounts be excluded?
Is this table current state or historical?
Which metric do we trust?
Can these two models actually be joined?
That knowledge already existed in bits and pieces across our dbt project. So instead of creating a new AI-specific knowledge base, we started treating the project itself as our foundational context layer.
And we've found that the relationship goes both ways. Our dbt project helps the Hex agent answer questions, while those conversations show us where our dbt project needs work. Here's how.
1 / The stack
For our purposes, there are three main pieces to this loop.
dbt = transformation + semantic layer
It builds the data, defines how it relates, tests it, and increasingly carries the context necessary to understand it.
Hex = conversational analytics + observation layer
Where most of our users ask questions, explore data, and build through conversation. And Hex uses those conversations to actively identify gaps in context and suggest improvements.
Claude = code + implementation agent
We use it heavily for development and for taking those suggestions, tracing them back to the right part of the dbt project, making the change, and opening a PR.
There are more pieces around the edges, but that separation is useful.
The important bit is that I do not want to teach all three systems what
registered user
means independently. That sounds miserable.
If the definition changes, I want to update it once. If we discover a caveat about a table, I want every agent to learn it. If someone flags a bad answer, I want the fix to improve the system rather than disappear into a Slack thread.
So we keep as much of that knowledge as possible in version-controlled files that all three can reach. Our dbt project is a pretty natural home for a lot of it because the repo already knows things the warehouse itself doesn’t.
It knows why the table exists, how it was transformed, what the columns mean, which relationships are valid, what we tested. And increasingly, it also knows how an agent should use it.
2 / Four files, not two
A delivered dbt model used to mean two things for us:
users.sql
schemas/users.yml
Now it usually means four:
The first two probably look familiar. The last two are where things start getting particularly useful for an agent.
Take a simplified
users
model. The SQL might define what makes it into the table in the first place. The schema YAML tells Hex that
user_id
is unique, that
account_id
connects a user to an account, and that
country
represents the current address rather than the address at registration. The semantic model says
user_count
is the trusted measure for registrations and defines which other models a user can be joined to. Then the
guide
carries all of the annoying stuff that doesn't fit neatly into any of those.
Something like:
knowledge
## Employees: always exclude
Internal accounts live in this table alongside real users.
Unless the question explicitly asks otherwise, exclude employees from customer analysis.
## Known data gaps
This model represents current state.
For questions about what a user's attributes were at a historical point in time, use the daily snapshot instead.
That last category has turned out to be incredibly important. A useful agent needs to know what
not
to do just as much as what to do. A column description can tell it what
country
means. A guide can tell it that using today's
country
to analyze an experiment from six months ago would be dumb. Very different jobs.
This is essentially what we mean when we talk about the context layer. I don’t think the answer is one giant semantic model with every possible thing encoded inside it.
Sure, semantic models are great for precise relationships and definitions. But agents also need judgment, caveats, negative knowledge, and context that doesn’t fit neatly into a metric or dimension.
Together, they form a collection of increasingly precise information that an agent can flexibly navigate when it needs it. Your dbt repo is already a pretty good skeleton for that.
3 / What this looks like in practice
Say someone asks the Hex agent:
“Can you segment accounts by registered user attributes to help me come up with an A/B test for marketing?”
They haven’t specified a table, population, timezone, or even exactly what they mean by registered user. But they shouldn’t have to.
Hex can pull those decisions from the context we’ve already built. The dbt model establishes the population. The semantic layer defines the trusted measures and relationships. The guides carry the edge cases and analytical conventions. Global instructions handle things that should be true basically everywhere.
The user just gets to ask the question. And they don’t even have to be sitting in Hex to do it.
They can ask from
Slack
or
Claude
too. The analysis still runs through Hex, which means they can work from whatever surface is convenient without us losing the context, visualizations, provenance, or conversation history behind the answer.
That matters more than it might sound.
If people start asking analytics questions everywhere, but every surface becomes its own silo, you’ve basically recreated the age-old fragmentation problem in analytics (BI tools, notebooks, spreadsheets), but with a nicer interface.
We wanted the opposite. One analytics layer underneath multiple surfaces. One set of context. One place where we can still see what’s being asked and how the system is behaving. That’s the part that feels meaningfully different from dashboard-era self-service.
We used to encode enough business logic into a predefined interface that somebody could click their way to the right answer. Now we’re trying to give the agent enough context that somebody can just describe the question they need help understanding.
4 / Turn conversations into dbt improvements
The convenient part is that this relationship runs both ways. dbt makes our conversations in Hex better. Hex then looks across those conversations to find where documentation in dbt is missing or breaking down.
Say people across the company keep asking some version of:
“How many active users did we have this week?”
The agent can answer those questions, but across enough conversations Hex starts to see the same ambiguities coming up. Should “active” mean a login or any non-bot activity? What time window should we use? Are we counting users or accounts?
A single instance might feel anecdotal. Across ten thousand conversations, it becomes a dataset. Hex looks across those interactions, surfaces warnings and recurring patterns, and
groups them into suggestions
.
Not every suggestion means “add another metric to the semantic layer.” Sometimes the fix belongs in a column description or a guide. Other times we need to endorse a different table. The important part is figuring out where the context belongs, not forcing every problem into the same abstraction.
Then Claude can pick those suggestions up through the Hex CLI, figure out where the relevant context lives in the dbt repo, make the change, and open a PR.
Our users are basically pressure-testing the context layer all day. The same questions our dbt models help answer become signals for where those models and docs need work.
5 / Treat context like production infrastructure
None of this context stays correct forever. Products change, metrics change, tables get deprecated, and new edge cases show up. At 10,000 conversations, manually reviewing all of that isn’t a governance strategy.
So we’ve started treating context more like production infrastructure. We use
evals
to test how well the agent is actually using that context across three dimensions:
Correctness:
is the answer right when the question is well-defined?
Consistency:
when the question is ambiguous, does the agent handle that ambiguity consistently and clarify when it should?
Path:
did it use the right context to get there? The right semantic model, tables, and guides, without wandering into stale or irrelevant data.
That last one matters because an agent can occasionally land on the right answer through the wrong path. We care about whether the behavior is repeatable, not just whether one answer happened to work.
We test those dimensions across different kinds of questions, from basic metric definitions and lookups through segmentation and more open-ended analysis.
Today, that eval suite is something we run more ad hoc. The next step is scheduling it and hooking it into CI, so changing context starts to look a lot like changing a production model: make the change, run the tests, see what got better or worse, review the diff, ship it.
Where to start? The context you already have.
If you already run dbt, you probably don’t need to go build a separate AI knowledge base from scratch.
My advice is to start small. Start with one heavily used model and ask what an agent would still need to know beyond the SQL. Maybe there are employee accounts that should always be excluded. Maybe there’s a snapshot table people should use for historical questions. Maybe three teams still mean slightly different things when they say “active.”
Write that down in a guide where the agent can reach it, then watch what people ask. That’s the loop we’re building at Underdog: dbt gives the agent better context, Hex shows us where that context falls short, and Claude helps push the improvements back into the repo.
Instead of trying to anticipate every question our business needs to answer, we’re building a system that makes agents capable of answering whatever gets asked next.
For a more detailed walkthrough of our setup, including the agent harness and how we run evals, see my original post:
Deploying Conversational Analytics v1.0
.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
More on Friends of data
BLOG
Introducing Hex 4.0
Olivia Koshy
·
October 27, 2026
BLOG
Before you build that data agent, I have notes.
Nick Pasquinzo
·
October 15, 2026
BLOG
The AI data sprawl
Barry McCardel
·
September 9, 2026
Nobody can trace it. The data team still owns the mess.
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
