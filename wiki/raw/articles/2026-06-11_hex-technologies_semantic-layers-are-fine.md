---
title: "Are Semantic Layers the Cornerstone for AI Analytics?"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/semantic-layers-are-fine/"
scraped: "2026-06-11T06:00:23.152829+00:00"
lastmod: "2026-06-10"
type: "sitemap"
---

# Are Semantic Layers the Cornerstone for AI Analytics?

**Source**: [https://hex.tech/blog/semantic-layers-are-fine/](https://hex.tech/blog/semantic-layers-are-fine/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
Are Semantic Layers the Cornerstone for AI Analytics?
Are they the secret to trusted, accurate answers from data? The people selling them would certainly say so
Charles Schaefer
Data
Data teams
June 10, 2026
Share:
twitter
linkedin
The timeless question in the analytics world is: how do you balance freedom with control? To whom do you give the freedom to ask any question? And how do you control analysis, so when people base their decisions on data, everyone is confident what they used is the truth?
AI models have breathed new life into this conundrum. Now, anyone can ask any analytics question, but not everyone has the technical understanding to fully understand what they’re being told. What rights do you give people? How do you verify the answers are right?
The data industry is coalescing around the idea of
context
as the solution. You give your AI agents some documentation as guardrails so they give you more accurate answers.
That sounds right - but how does it work? If you look at most of the discourse around this, it’s primarily in the form of a Semantic Layer. The workflow is:
First, define your metric calculations, relationships between your tables, and dimension definitions in a semantic model.
Enforce your semantic model(s) as a “layer” that agents must go through (i.e. only allow your AI agents to answer questions where the data has been modeled this way).
That way, the agent can never be wrong!
Brilliant, right? Well, we believe there are some flaws in this approach. It’s not that semantic models are
bad
, per se (in fact, you can use them in Hex!), we just think they aren’t the
whole
solution. And we think we have a better way.
Where semantics fall short
Building agents around a semantic layer
is
a brilliant business strategy (as long as you’re selling the semantic layer). Once someone has invested the time to load all of that documentation into your system, they’re locked in to your platform. They’re never getting out without a painful re-platforming project that will probably cost them more than they’ll ever save retiring your software contract.
But is it a brilliant strategy for a customer? If I were buying a data product right now, and the product reps were selling me hard on their semantic layer, I’d be worried.
Here’s what I’d ask in this hypothetical situation:
What happens when someone has a question that wasn’t pre-built into my semantic model?
What happens when we add a new data source that wasn’t defined in the semantic model?
What happens when the LLMs improve? How will I rebuild my semantic models to optimize them for the updated LLM capability?
Will I even need a semantic model? Or is the natural language context, code repo, and warehouse metadata enough to answer a question?
In a lot of ways, semantic models fall into the same trap dashboards have fallen into. They’re pre-defined information. They fail the simple test of self-service:
what happens when someone has a new question?
Wait a minute…isn’t a semantic layer necessary for governance?
Ok
,
the semantic layer evangelist might say,
but AI is also capable of making huge errors!
It can hallucinate, it can pull the wrong data, it lacks some of the human judgement that cause people to question unusual-looking answers.
And because we’re talking about giving AI tools to non-technical people who don’t know how to debug a SQL query, it’s
dangerous
for them to have ungoverned, unregulated answers. Semantic model proponents argue that a semantic model, where the metrics and queries are defined before business stakeholders can misinterpret them, is a necessity to protect the business against wrong answers.
There’s the timeless question - how do you balance the freedom to ask any question with the need for control?
The answer is also timeless: if you restrict users too much, if you only provide them answers that you have first defined, you won’t scale to meet all of their demands.
There is an infinite demand for insight
.
There is simply no way for a data team to anticipate every business question. And when you limit stakeholders, their natural response is not to follow your rules. Their response is to work around them.
Business users taking spreadsheets they pulled from your BI tool and loading them into ChatGPT. Gut decisions made because the most senior person in the room said “I said so.” Rogue analytics tools that are implemented without the data team’s consent. That’s the inevitable conclusion of strict, semantic-layer-only governance. Not stakeholders who patiently file a ticket and wait in line for you to define the next answer.
They’re more like guidelines
It’s common to have a question that is only
partially
resolved by the semantic model.
Take this as an example:
What is the median refund request amount by support channel (chat vs email) over the last 30 days? Return channel and median_amount_dollars
.
This is part of an internal eval we use to test the Hex agent. The trick is that there
is
a semantic model, but it doesn’t fully answer the question. The semantic model doesn’t aggregate data in the way the user asks, so a bit of raw data transformation is required. But the model has information about ways to segment and filter the data.
This is a good example because it’s something that our agent wasn’t getting right with previous models, but
as LLMs have gotten more sophisticated
, the Hex agent is able to pull what’s needed from both raw SQL and the model.
A sample from Hex’s internal agent benchmark. As the models have evolved, the way we use semantic models has changed as well.
We don’t know exactly what the next generation of LLMs will be capable of. But as they get more sophisticated, the guidance they need will evolve as well. Enforcing a semantic model for AI analytics doesn’t only lock you into a vendor, it locks your capabilities into a previous generation of AI capabilities.
Partnerships in context
Analytics can only work as a partnership. Data teams must work to understand the business’ priorities and needs, enabling them to self-serve on insights without feeling too restricted. This creates the potential for error, yes, but if someone is going to go rogue, they should do it under your watch. When you can see what questions people are asking and how AI is responding, you make your stakeholders into partners with you as you build out context for AI.
Every question, every query, every dashboard, every model - is context that can make the next answer better. The more people interrogate data, the more context you get. You then take that all of that context and put it to work. The context compounds, answers get faster and more trusted, and your analytics system gets smarter the more you use it. Crucially, your stakeholders are accountable
with
you, because they’re helping curate all of this context, they aren’t just waiting for it to happen.
The business team has context, too - strategy documents, customer interactions, and conversations - that AI can incorporate into its reasoning. This isn’t the type of information that naturally lives in a semantic layer, but it can serve as powerful rules for AI agents, telling it what to prioritize, what answers matter the most, and how to judge its results.
If you’re trying to build a future-proof data practice, take a broad approach to context. The more you embrace the power and flexibility that AI models provide, the more trusted, accurate system you’ll be able to support.
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
Your code knows things your warehouse doesn't
Andrew Lee
·
May 15, 2026
BLOG
Introducing Context Suggestions
Andrew Lee
·
April 23, 2026
Hex's new Context Suggestions automatically learn from every Thread, turning user conversations and agent analyses into smarter, compounding data context.
BLOG
Dashboards aren't dead, they're just demoted
Charles Schaefer
·
February 18, 2026
Dashboards have become the standard for communicating data insights, but as AI companies have started to enter the data space, they have attacked dashboards as "dead" or "outdated." We think it's time to rightsize their role.
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
