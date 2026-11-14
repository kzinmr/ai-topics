---
title: "AI-native analytics vs. bolt-on AI"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/ai-native-analytics/"
scraped: "2026-11-14T06:00:27.585550+00:00"
lastmod: "2026-11-04"
type: "sitemap"
---

# AI-native analytics vs. bolt-on AI

**Source**: [https://hex.tech/blog/ai-native-analytics/](https://hex.tech/blog/ai-native-analytics/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
AI-native analytics vs. traditional BI: What's actually different?
Every BI tool has AI now. But there's a big difference between adding a copilot to traditional BI and rebuilding the experience around agents. Here's why it matters.
The Hex Team
Data
November 4, 2026
Share:
twitter
linkedin
In this article
TL;DR
Traditional BI vs. AI-native analytics
1. Agent functionality: From navigating BI to doing the work
2. Architecture and interoperability: BI shouldn't stop at the browser tab
3. Trust and context: BI governance needs to evolve for agents
The cost of BI falling behind: AI data sprawl
What this looks like in practice: LangChain
When adding AI to traditional BI is enough
The future of BI is AI-native
Frequently asked questions
Get started for free
TL;DR
AI-native analytics is the next evolution of BI.
Instead of navigating dashboards or learning drag-and-drop interfaces, users can ask questions, investigate data, build apps, and automate analysis in natural language.
The difference goes beyond a chatbot.
AI-native platforms like Hex bring end-to-end agent workflows, interoperability with external agents, and shared context and governance together.
Traditional BI risks falling behind user expectations.
When people can't do what they need in legacy BI tools like Tableau or Looker, they'll turn to Claude or ChatGPT, creating disconnected analyses and governance gaps. AI-native BI gives them that flexibility without sacrificing trust.
Every BI vendor has an AI copilot now. But people's expectations have moved well beyond asking questions about existing dashboards. They want to investigate data, build applications, and get answers in plain language, without learning another interface or waiting on an analyst.
And if their BI tool can't deliver that experience, they'll increasingly turn to external agents like Claude or ChatGPT instead. That leaves data teams dealing with disconnected analyses, inconsistent definitions, and little visibility into how answers are generated.
That's why the distinction between traditional BI with AI added-on and AI-native analytics matters.
AI-native analytics isn't a departure from business intelligence. It's a more modern way to deliver it.
Companies still need dashboards, reporting, trusted metrics, and governance. What's changing is how people create, interact with, and build on that work.
And as frontier models get better at increasingly sophisticated analytical tasks, the gap will only become more apparent. Hex's
DataBench
benchmark tracks how quickly models are improving at real-world analytical work, including complex investigations that go well beyond writing SQL.
The question isn't whether your BI tool has AI. It's whether it can keep up with what people now expect AI to do.
Traditional BI vs. AI-native analytics
Traditional BI was designed around a familiar workflow: data teams prepare models and dashboards, and business users navigate what's been published.
That approach works well for recurring reporting. But it has struggled to deliver on BI's broader promise of making data accessible to everyone. Most people still don't know how to build dashboards, and answering an unexpected follow-up often means going back to the data team.
Adding AI can improve those workflows. A copilot might summarize a report, generate a visualization, or help someone write a calculation.
AI-native analytics changes the starting point. Instead of asking people to navigate and construct analytical interfaces themselves, agents do much of that work for them. This has prompted many data teams to wonder whether they could even
replace their BI tool with an agent
.
These aren't absolute categories. Traditional BI products like Sigma and Omni have added on AI features to their existing BI capabilities.
But the more meaningful distinction is whether AI features help users operate the same BI workflows faster, or enable more sophisticated analytical work through one connected experience.
That difference shows up in three areas.
1. Agent functionality: From navigating BI to doing the work
The promise of self-service BI was always straightforward: people should be able to answer their own questions without waiting for an analyst.
But traditional self-service largely meant giving people more intuitive ways to navigate data. Dashboards, filters, and drag-and-drop builders helped, but they still required users to understand the interface and anticipate what they wanted to investigate.
AI changes that.
Imagine a sales leader asking: "Why did enterprise expansion revenue slow last quarter?"
An AI agent can investigate the question, break down the drivers, and follow up on unexpected results. If the user wants to join another source, introduce a new calculation, or build an interactive dashboard, the agent can continue the work.
And once that analysis is useful, it doesn't have to end in a chat. The user can publish it as an app, share it with colleagues, or schedule an agent to investigate the same question every week.
Hex supports these workflows through the
Hex Agent
, Generative
Apps
, and
Agent Tasks
.
Dashboards don't disappear. They become something anyone can create, change, and investigate, rather than something they have to find or wait for someone else to build.
Why code-native architecture matters
There's also an architectural shift happening underneath this experience.
Traditional BI platforms were largely built around predefined visual components. Even when AI generates a dashboard, it may still be assembling the same charts, tables, and workbook elements that users previously created by hand.
That's useful, but it can limit what an agent builds to the components the BI system supports.
A code-native architecture offers a different approach. Agents can generate custom application interfaces backed by analytical code, with greater flexibility over layout, interaction, and functionality. That means users aren't limited to whatever charts, filters, and layouts their BI vendor has predefined. They can describe the experience they actually need and let the agent build it.
This is the direction Hex is taking with
Hex 4.0
. Projects are backed by code files, allowing agents to build custom applications while keeping the analytical logic and dependencies behind individual elements inspectable.
That matters as AI takes on more of the building. A polished dashboard is only useful if someone can understand and trust the numbers behind it.
2. Architecture and interoperability: BI shouldn't stop at the browser tab
People are already using agents like Claude, ChatGPT, and Cursor to work with data. And as those agents get more capable, they're increasingly competing with traditional BI interfaces for where analytical work begins.
That's not necessarily a problem. The issue is what happens when people leave their governed analytics environment to do the work.
A sales leader might export pipeline data into Claude. An engineer might connect directly to the warehouse from Cursor. Someone else might generate an interactive dashboard in ChatGPT.
Each workflow can be useful on its own. But if everyone is rebuilding business logic independently, the data team loses the consistency and control it worked to establish through BI.
The answer isn't forcing people back into one interface. It's making governed analytics available through the agents they already want to use.
That's why interoperability is becoming a fundamental part of modern BI. Through MCP, APIs, and CLI, external agents can access analytical capabilities without requiring everyone to use the same application. But an integration logo doesn't tell you how much an external agent can actually do.
Can Claude answer questions using the same business definitions as the native analytics experience? Can Cursor create or modify an analytical project? Can the resulting work be published and shared without rebuilding everything from scratch?
Hex supports these workflows through MCP and the
Hex CLI
, letting external agents access governed analytics and work with analytical projects.
Code-native architecture makes this more powerful. When analytical work is represented as inspectable code, agents have greater flexibility to create and modify it across different environments.
The goal is to give people the freedom to use their preferred agents without fragmenting the company's analytical knowledge.
3. Trust and context: BI governance needs to evolve for agents
Traditional BI has invested heavily in governance: managing data access, defining metrics, and ensuring people use certified reports.
Those capabilities remain essential. But AI introduces another challenge.
An agent can access the right data and still produce the wrong answer. It might choose an outdated table, misunderstand a business definition, make an incorrect join, or draw a conclusion the evidence doesn't support.
And unlike a conventional dashboard, an agent can generate a completely new analytical path every time someone asks a question. That means governing AI analytics requires more than restricting which data an agent can access.
Shared context, not just semantic models
Semantic models remain valuable for defining metrics, dimensions, and relationships. But agents also benefit from warehouse metadata, business documentation, reference queries, and instructions about how a company operates.
Not every question can be anticipated and modeled in advance.
A flexible context architecture lets agents draw on those sources without requiring every piece of business knowledge to be rebuilt inside a proprietary semantic layer.
Hex can sync existing semantic models from dbt, Snowflake, and Cube. Through
Context Sync
and repository connections, teams can also bring in Markdown Guides and knowledge from existing code repositories.
That means the context your data team builds can support analytical work across different interfaces, rather than being useful only to one vendor's chatbot.
From governing data to improving answers
Context isn't a one-time setup.
Business definitions change. New tables appear. Users ask questions nobody anticipated. And manually reviewing thousands of agent conversations isn't a realistic way to maintain accuracy.
Data teams need visibility into what agents are doing, where they're getting answers wrong, and which context needs improvement.
Context Studio
helps teams inspect supported agent conversations, evaluate answer quality, identify recurring failures, and improve shared context.
This becomes particularly important as more employees rely on AI for their everyday analytical work. A wrong answer in a single chat is one problem. A misunderstood business definition repeated across hundreds of conversations is another.
The goal isn't just to make sure people access the right data. It's to make sure agents use that data correctly, and keep getting better as the business changes.
The cost of BI falling behind: AI data sprawl
When a BI tool can't support the questions people want to answer or the experiences they want to build, they don't necessarily stop working with data.
They find another way. That might mean exporting CSVs into ChatGPT, generating dashboards with Claude, or writing SQL through a coding agent.
The problem isn't that these tools are incapable. Quite the opposite. Their growing capabilities are what make them attractive alternatives to traditional BI.
The problem is that analytical work can end up scattered across chat histories, local files, and disconnected applications. Metric definitions get duplicated, numbers don't match, and the data team has limited visibility into how conclusions were reached.
We've described this as
AI data sprawl
.
There's a potential cost dimension, too. When different agents repeatedly reconstruct the same context or run overlapping investigations, teams can accumulate unnecessary model and compute usage.
This is why AI-native BI needs to deliver on both sides of the equation: the flexibility and ease of use people expect from modern AI, and the shared context, governance, and collaboration that made BI valuable in the first place.
Otherwise, companies risk building a governed BI environment that fewer and fewer people actually use.
What this looks like in practice: LangChain
LangChain
offers a useful example of how an AI-native approach can change the work of BI.
The company wanted to move away from its legacy BI environment and give more employees access to data.
Instead of manually rebuilding every dashboard, its analytics team provided existing YAML definitions to Hex's agent and asked it to recreate the reports.
On the initial pass, the agent reconstructed roughly 90% of the dashboards, including queries, charts, and structure. After review and consolidation, the team completed its migration in six weeks.
But the bigger change was what happened afterward.
Employees gained broader self-service access to data, while analytics engineering shifted more attention toward maintaining the business context and infrastructure behind trustworthy answers.
LangChain didn't stop needing dashboards or business intelligence. It adopted a more flexible way to build and deliver them.
That's the opportunity of AI-native BI: give people the analytical capabilities they're increasingly finding in general-purpose agents, while keeping the resulting work connected to a trusted, shared environment.
When adding AI to traditional BI is enough
Not every organization needs to rethink its BI stack immediately.
If your existing dashboards serve most users well, you have established semantic models, and your main goal is making reports easier to navigate, the AI capabilities in your current BI tool may be a reasonable fit.
Traditional BI platforms also offer mature reporting, governance, and distribution features that remain valuable. The question is whether those workflows will continue to meet people's expectations.
If employees increasingly want to investigate unfamiliar questions, build their own applications, automate analysis, and work with data through external agents, a chatbot attached to an existing BI experience may not be enough.
And if your BI environment can't support those workflows, it's worth asking where that analytical work is going instead.
The future of BI is AI-native
Business intelligence has always promised to make data accessible to more people.
For years, the industry tried to deliver on that promise with easier interfaces, more dashboards, and increasingly sophisticated visual builders.
AI changes the equation. People no longer need to learn how to navigate or construct every analytical experience themselves. They can describe what they want to know or build, and agents can do much of the work.
And increasingly, they'll expect that experience whether their BI tool supports it or not.
That's why the next generation of BI needs to bring together two things: the power and flexibility of modern AI agents, and the trusted business context, governance, and collaboration companies have spent years building.
That's the direction Hex is taking with conversational self-service, Generative Apps, external agent interoperability, code-native architecture, and tools to continuously improve answer quality.
The future of BI isn't another dashboard builder with a chatbot. It's an analytics experience built around what AI can now do, without giving up the trust that makes BI useful.
Frequently asked questions
What's the difference between AI-native analytics and traditional BI?
Both support the core jobs of business intelligence, including exploration, reporting, dashboards, and decision-making. Traditional BI generally relies on people navigating and authoring analytical interfaces, while AI-native analytics puts agents at the center of those workflows, letting users ask questions, investigate, and build in natural language.
Can traditional BI platforms become AI-native?
Yes. The distinction isn't determined by when a platform was founded. Traditional BI vendors can evolve their architectures and workflows to support more sophisticated agents. The important question is how much of the analytical process AI can complete, and whether those capabilities work together.
Does AI-native analytics replace dashboards?
No. Dashboards remain useful for reporting, monitoring, and sharing metrics. AI-native analytics changes how they're created and used, making it easier to generate dashboards from prompts, investigate results, and build interactive applications when a static report isn't enough.
Why does code-native architecture matter for BI?
Code-native architecture allows agents to generate and modify analytical applications with fewer constraints from predefined visual components. It also makes underlying code easier to inspect and review, which becomes increasingly important as AI generates more analytical work.
Can AI-native analytics work alongside existing BI tools?
Yes. Teams can adopt AI-native workflows alongside existing dashboards and reporting systems. Reusing semantic models and business definitions from systems like dbt or Snowflake can help maintain consistency during a transition.
Share:
twitter
linkedin
Choosing your next BI tool? Get the BI buyers guide for what to look for when evaluating the next generation of AI analytics platforms.
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
