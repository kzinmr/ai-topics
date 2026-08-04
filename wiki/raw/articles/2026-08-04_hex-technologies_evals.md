---
title: "Introducing Evals"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/evals/"
scraped: "2026-08-04T06:00:11.008237+00:00"
lastmod: "2026-08-04"
type: "sitemap"
---

# Introducing Evals

**Source**: [https://hex.tech/blog/evals/](https://hex.tech/blog/evals/)

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
Introducing Evals
Measure how the Hex Agent performs and test context changes safely before they ship, all from the CLI.
Andrew Lee
Data teams
Product
August 4, 2026
Share:
twitter
linkedin
Every few years the data teams’ job seems to get upended, at least
we’re used to it at this point
. The latest shift in our role: maintaining and managing analytics agents. As people demand conversational analytics, the data teams’ new job is keeping agents accurate and consistent. This starts with the context agents’ use.
Agents are non-deterministic
and
you can’t control how users interact with them the way you could with a dashboard. This makes it hard to know how agents are actually going to use context, and whether answers get better as you make context changes.
Today, we're introducing Evals in Hex: the way to test the Hex Agent and your context. Hex’s Evals are inspired by
the same testing workflow
we use internally to ship our own agent features, now yours to build on.
knowledge
We've been using Evals ourselves to compare model performance.
Join us August 13
for a live conversation on what we learned building a new way to test whether AI can be trusted with data analysis.
How it works: grade the
work
, not just the answers
Data analytics is a uniquely hard domain for an agent to work in: easy questions can look hard, hard questions can look easy, and a correct number can still mislead you.
Evals let you define tests against the agent. Generally, it’s easiest to start with just checking that the agent gets the correct answer. But Evals empower much more advanced testing as well:
Checking valid answers
You can specify a numeric result as a specific number or reference SQL query, alongside your tolerance level. But not all correct answers are numbers. Say your test question is “which segment and region churned the most revenue in 2025?” Set the correct answer to the
west region
and
mid-market.
Checking how it arrives at an answer
Evals have an LLM-as-judge that reads the entire conversation and sees the specific tools and resources the agent uses. This lets you grade the agent’s work:
Did the agent use the correct tools, like a specific semantic model or guide?
For an open-ended question did the agent propose multiple approaches back to the user or ask for clarification?
But the funny thing about analytics is that getting the answer right isn’t always the point. Sometimes what matters is the reasoning and behavior how you got there:
Did the agent find and call out the data discrepancy that you know exists in the data?
Did the agent appropriately refuse to answer a question where there is insufficient context?
Built for your existing workflow
Your eval test cases are defined in files that you can version control, and you run them from
the Hex CLI
. Eval suites can live alongside the rest of your context, so you can use the same code review workflow you already use for guides and semantic models.
You can also fork your context and run evals against the fork. In Hex, you fork your context to get a
Context Preview
: a sandboxed version of your agent with an alternate version of your workspace context. You can run your Evals on the Context Preview to validate changes to your context.
Because each run is scoped to a specific fork and configuration, you can compare results side by side. Agents aren't deterministic, so you can run each test case up to three times and see how much the answer moves before you commit to a default.
See
the docs
for more details on how to define and run evals.
What you can do with Evals
Evals turn agent quality and cost into something that you can measure and improve, so you're not just going on vibes.
Specifically, they help you:
Test context changes before publishing:
Start by staging a guide or semantic model change from the CLI. You can run your eval suite against a preview of this change, and publish only if it passes.
Catch drift before your users do:
Data changes over time, and context can too. External context, data and tables can change upstream of the agent. You can run your eval suite on a schedule and catch unexpected regressions to the agent’s performance.
Run configuration sweeps:
Run a suite of evals against different language models and effort levels: you can evaluate a cheaper open-source model like Kimi with frontier models. Compare the cost and quality of responses in the agent. This lets you choose the default LLM that fits your organization’s needs.
The full context lifecycle
Evaluating agent performance isn’t a one-off exercise, building maintaining, and improving context is ongoing work. Here’s how you manage the full context lifecycle to give your organization confidence in the answer you get from the agent:
Unify context
Bring in context and build on what you already have in dbt, git repos, docs, or external apps. We never lock you in with proprietary specifications and all context defined in Hex is portable and can be taken out of Hex.
Observe the agent
Get one view of every question and answer, wherever it happened: Hex, Slack, MCP, or the CLI. The Review Agent flags warnings where context is missing and classifies what each answer actually used.
Improve with use
The Review Agent clusters context gaps into
Suggestions
, so you can quickly review and apply. Once you make context changes, use Evals to verify if there change worked. Want to apply a suggestion? Add the suggestion with an eval to make sure your change doesn’t regress in the future.
Getting started
Here are some tips for getting started with Evals:
Install the Hex CLI
Check Suggestions,
the Review Agent already has some changes you should probably make.
Start with simple questions
your team already asks, the ones you'd want the agent to get right every single time.
Run it again next week
, even ad hoc runs every week will start surfacing interesting opportunities.
As part of onboarding, we’ve included a bootstrap prompt for Claude Code, Cursor, or your coding agent of choice. It scans your recent Threads, clusters them into your team's most common question topics, and drafts a starter suite from real usage instead of a blank file.
Give Evals a try, we'd love to hear what you find!
Evals is available to Editors, Managers, and Admins on Team and Enterprise plans.
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
