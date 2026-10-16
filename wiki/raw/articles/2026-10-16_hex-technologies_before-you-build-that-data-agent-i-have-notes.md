---
title: "Before you build that data agent, I have notes."
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/before-you-build-that-data-agent-i-have-notes/"
scraped: "2026-10-16T06:00:53.660467+00:00"
lastmod: "2026-10-15"
type: "sitemap"
---

# Before you build that data agent, I have notes.

**Source**: [https://hex.tech/blog/before-you-build-that-data-agent-i-have-notes/](https://hex.tech/blog/before-you-build-that-data-agent-i-have-notes/)

Skip to main content
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
Before you build that data agent, I have notes.
Build vs. buy in data has never been hotter. But do you know what you’re signing up for?
Nick Pasquinzo
Data teams
October 15, 2026
Share:
twitter
linkedin
In this article
So what are you actually signing up to own?
What is worth building yourself?
What does the math look like for you?
Get started for free
The last year has been a wild ride for data teams. We went from wondering whether AI was coming for our jobs, to suddenly all becoming “context engineers”, to now policing an endless stream of vibe-coded dashboards and queries.
It’s chaotic. And it’s pushed a lot of teams toward a similar idea:
why not just build a data agent ourselves?
The appeal makes sense. It’s easier than ever to spin up an agent harness, connect it to your data, put an interface in front of it, and have something answering real questions surprisingly quickly.
But the ease of building that prototype is something of a well-disguised trap. It’s cheap to build, but expensive to own. And I say that from experience.
Before joining Hex this summer, I spent close to a decade on data teams at Vercel, Miro, and Google. I built data apps, worked on ML and analytics systems, and helped deploy and maintain an internal analytics agent. I’ve been the person getting tagged when someone asks, “Is this number the agent spit out actually right?” and then digging through the agent’s trail to figure out what happened.
From my own trial and error, the question isn’t whether you can build an agent. That’s a weekend project now. It’s how much owning one will change the day-to-day of your data team.
Once a prototype is out the door, your attention quickly shifts to debugging bad answers, keeping definitions and logic from going stale, building new capabilities, and maintaining the infrastructure for something the whole company now relies on. That stops looking like a side project pretty quickly.
knowledge
Thinking about building?
Estimate the cost →
So what are you actually signing up to own?
The harness is probably the least intimidating part now. There’s no shortage of open-source tooling and agent frameworks. The real work surfaces once it’s out in production and everyone starts asking questions.
In particular, there are three areas that are easy to underestimate and I’d think hardest about before deciding whether your team wants to own this.
1. “Is this right?” becomes a product requirement.
Once you’ve deployed an agent out in the wild, it’s not enough for it to just generate a single SQL query and return a number. People are going to follow up, change the scope, ask about data from different tables, and push into more open-ended questions.
And as the answers get more nuanced, users will inevitably start to ask, “Wait, is this right?”
This is where auditability gets real. You need to know which tables or models it queried, the SQL it wrote, the assumptions it made, and how it arrived at the answer.
If you have to piece that information together across logs and agent-generated code, reviewing an answer becomes a project in itself. Ideally, you should be able to open an answer, see the shape of the analysis, inspect the queries and logic, and quickly understand what happened.
I’ve done this the hard way before: getting tagged in Slack, tracking down SQL in a text snippet, copy-pasting it out, and working backwards to figure out what happened. It’s doable, but if every questionable answer turns into 15 minutes of detective work, that adds up fast. Just a few dozen questions can eat up a meaningful chunk of an analyst’s week.
And it’s not just whether the answer is right. You also need to know whether the person asking should have had access to it in the first place. Finance, HR, customer, and sensitive product data all come with different access rules that need to hold when questions are asked and when answers get shared.
In a perfect world, reviewing an agent’s work should feel a lot like reviewing the work of an analyst on your team. The logic should be easy to follow, permissions should hold automatically, and anything questionable should be easy to dig into.
Those aren’t nice-to-haves, they’re product requirements. At scale, that traceability and governance have to be first-class experiences in their own right, or every questionable answer risks turning into a security issue or debugging project for the data team.
knowledge
Say 500 questions hit your agent each week, and just 10% get flagged for a closer look. At 15 minutes each to find the SQL, reconstruct the steps, and figure out what happened, that’s
12.5 hours a week
investigating answers.
Get to 2,000 questions a week and that becomes
50 hours
, just diagnosing what went wrong.
2. Context isn’t a one-time setup. It’s constant upkeep.
Being able to inspect one-off answers is one thing. Keeping them consistently accurate across your organization is a separate challenge entirely.
At this point, it’s table stakes to give an agent context on your business. But managing that context and keeping it current as your company changes is far less straightforward.
The agent needs more than a map of your schema. It needs to know which models are trusted, how metrics are defined, how tables should be joined, what dimensions are safe to slice by, and all the weird business logic your team normally just knows.
And none of that context remains still.
Products launch, metrics change, and new parts of the business make their way into the warehouse before anyone’s had a chance to model them.
This was one of the more painful parts of maintaining an internal agent for me. A lot of the work was reactive. New questions would expose missing definitions, stale metrics, or unmodeled tables, and we’d scramble to patch those gaps as users surfaced them.
You can’t scale this by waiting for users to tell you what broke. You need tooling around it: a way to see what people are asking, where the agent is struggling, which domains are missing coverage, and whether the changes you make are actually improving things. That means investing in observability, evals, and automation to continuously improve the agent over time.
At a small scale, you can keep tabs on some of this manually with basic logs. Once hundreds of people are asking questions every day, that falls apart quickly. Suddenly, you’re trying to make sense of thousands of interactions to figure out where the agent is struggling and how to fix it.
knowledge
Say you have 200 users chatting with the agent just 3 times a week. At 600 conversations, manually reviewing logs for stale definitions or context gaps stops being realistic.
A lightweight Claude Code + Git + evals setup could alone take
4–6 engineer-weeks
to wire together. Build a real UI for reviewing conversations, triaging context issues, and tracking evals over time, and you’re probably pushing
9–12+ weeks.
3. People need more than chat.
This is the one I think I underestimated most. At first, the goal is simple: let people ask questions in plain language and get an answer.
Then someone wants a chart of the answer. They want to save it. Share it. Monitor it. Build on it. Turn it into a recurring report. Set up an alert. Access it from Claude.
And those are all pretty reasonable asks. But now you’re owning dashboards with live data connections, permission-backed sharing, MCP connections, and more.
We ran into this pretty quickly. Our agent lived in Slack, so it could spit back an answer, some SQL, maybe even a visualization. But once someone wanted to dig deeper, keep the analysis around, or bring it into another agent workflow, we needed to go build the functionality to support it.
The scope starts to expand really fast. Those are real product capabilities to build, and you’re starting to pull in engineering work well beyond just the data team.
At some point, you have to reckon with the fact that you’re no longer just building a data agent. You’re building an end-to-end platform for analytics.
knowledge
Charts, saved analyses, alerts, sharing, integrations. Even if some of those take only a few days and others take a few weeks, you can easily end up with
10+ engineer-weeks of product work
before ongoing maintenance.
What is worth building yourself?
If all of this sounds like a lot, that’s kind of the point. It’s easier than ever for data teams to build software, but you have to set a high bar for deciding whether you actually should.
Is the workflow genuinely unique to your business? Is owning the agent itself strategically important? Do you need behavior or integrations existing platforms simply can’t support? Do you have the engineering capacity to keep investing after the prototype? Are you comfortable turning part of the data team into the team that owns this system long-term?
There are a few companies where the answer to all of that is probably yes. OpenAI may have good reasons and resources to build a lot of this infrastructure themselves.
But let’s be honest, most of us are not OpenAI. And if the answer to most of those questions is no, that’s a pretty good signal you’re signing up to rebuild a lot of infrastructure that isn’t meaningfully differentiated for your business.
So what is actually worth owning?
The stuff that’s uniquely yours: your metric definitions, business logic, trusted models, analytical standards, and all the institutional knowledge that makes an agent useful in the first place. None of that becomes less valuable just because you decide you don’t want your team maintaining every piece of infrastructure around it. And increasingly, it doesn’t have to be locked to the agent you originally built it for. You can
sync it into platforms like Hex
without having to rebuild from scratch.
For me, the promise of AI analytics is the opposite of building all of that infrastructure ourselves. I want it to give data teams the time to dig into the weird, nuanced questions that actually need our expertise, while making it easier for everyone else to answer their own day-to-day questions.
I’d be careful not to confuse “we can build this now” with “we should own this forever.”
What does the math look like for you?
The numbers above are intentionally rough. So we built a calculator that lets you plug in your own assumptions around usage, human review, context management, and the product capabilities you’d need to build.
Estimate the cost of your analytics agent →
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
Introducing DataBench
Izzy Miller
·
August 13, 2026
A frontier benchmark for complex data work and analytical reasoning
BLOG
You don't need to migrate those 300 dashboards
Rachel Herrera
·
September 10, 2026
AI is changing BI migrations. Learn which dashboards are worth migrating and why moving the logic—not the UI—unlocks real self-service.
BLOG
The life and times of data teams in the AI era
Katie Bauer
·
July 17, 2026
How data teams have changed, and remained the same, in the age of AI.
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
