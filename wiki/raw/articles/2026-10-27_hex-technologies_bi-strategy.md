---
title: "How to build a BI strategy for the AI era"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/bi-strategy/"
scraped: "2026-10-27T06:00:13.366861+00:00"
lastmod: "2026-10-22"
type: "sitemap"
---

# How to build a BI strategy for the AI era

**Source**: [https://hex.tech/blog/bi-strategy/](https://hex.tech/blog/bi-strategy/)

Skip to main content
📊
Buyer's Guide:
Should you replace your BI tool with an agent?
📖
eBook:
How to make build context for AI analytics
🔍
Research:
Using evals to cut AI errors by 7x
📊
Buyer's Guide:
Should you replace your BI tool with an agent?
📖
eBook:
How to make build context for AI analytics
🔍
Research:
Using evals to cut AI errors by 7x
📊
Buyer's Guide:
Should you replace your BI tool with an agent?
📖
eBook:
How to make build context for AI analytics
🔍
Research:
Using evals to cut AI errors by 7x
📊
Buyer's Guide:
Should you replace your BI tool with an agent?
📖
eBook:
How to make build context for AI analytics
🔍
Research:
Using evals to cut AI errors by 7x
📊
Buyer's Guide:
Should you replace your BI tool with an agent?
📖
eBook:
How to make build context for AI analytics
🔍
Research:
Using evals to cut AI errors by 7x
📊
Buyer's Guide:
Should you replace your BI tool with an agent?
📖
eBook:
How to make build context for AI analytics
🔍
Research:
Using evals to cut AI errors by 7x
Blog
How to build a BI strategy for the AI era
Build a business intelligence strategy for the AI era, covering self-service, AI-powered building, governance, and cost.
The Hex Team
Data
October 22, 2026
Share:
twitter
linkedin
In this article
What is a business intelligence strategy?
What changed and why the traditional approach needs to evolve
Start with the decisions that matter
The four questions a BI strategy has to answer
Where governance fits
Sequencing it without a two-year program
How you know the strategy is working
Make the governed path the fastest one
Frequently Asked Questions
Get started for free
For years, the playbook for
business intelligence
was pretty straightforward: centralize your data, define trusted metrics, build dashboards, and give people a way to explore them.
But AI is upending that approach. People are exporting data into ChatGPT and Claude, asking questions in plain language, and increasingly building their own dashboards and analytical tools, often without involving the data team at all.
That's creating a new challenge for data leaders: how do you give people the flexibility they now expect without losing the trust, governance, and consistency you've worked to establish?
What is a business intelligence strategy?
A business intelligence (BI) strategy defines how an organization uses data, technology, and people to make better decisions. It connects business priorities to the tools, processes, and governance needed to make data accessible, trustworthy, and useful across the organization.
A good BI strategy addresses everything from how data is collected and modeled to how employees access insights, perform analysis, and put those insights to work. Increasingly, that also means determining how AI agents fit into these workflows and how to maintain trust as more people work with data independently.
What changed and why the traditional approach needs to evolve
Traditional BI strategies assumed that most analytical work happened inside a controlled environment, whether through dashboards, self-service interfaces, or requests to the data team. AI is fundamentally changing that assumption.
A Gartner survey of 302 cybersecurity leaders found that 69% of organizations suspect or have evidence that employees are using prohibited public generative AI tools. The CSV someone exported last Tuesday is exactly the kind of data that can end up outside the governed path.
The appeal is understandable. ChatGPT, Claude, and Cursor make it easy to ask questions, explore data, and increasingly build analytical experiences without waiting on the data team. But an exported dataset doesn't necessarily include the context that revenue excludes refunds, or that a table was deprecated last quarter. And as people generate their own dashboards and analyses, useful work can become scattered across chat threads and local files with little visibility into how it was produced.
A ban alone doesn't solve the problem, because these workarounds often exist to address something the official workflow can't deliver. Your BI strategy needs to make trusted analytics just as accessible as the alternatives, rather than forcing people to choose between flexibility and governance.
That's the idea behind
AI-native business intelligence
: letting people ask questions, explore data, and build what they need in natural language, while giving the data team visibility and control over the underlying context and logic.
Start with the decisions that matter
Identify the decisions your BI strategy needs to support before auditing every table or evaluating tools. Start with the decisions you want to improve, then determine the information and workflows needed to support them.
List the recurring decisions your company makes, such as weekly pricing changes, monthly campaign budgets, or quarterly headcount planning. For each, answer a few questions:
Who owns the decision, and what will they do without new information?
Which metrics and business context inform that decision?
Where does the current workflow break down? Are people waiting on analysts, searching dashboards, or exporting data?
What would they do differently with a faster answer or a more flexible analytical tool?
Then rank the opportunities by business impact and the effort required to support them. Otherwise, the loudest requests can determine what gets built while more valuable work stays in the backlog.
You don't need to make every dataset available to every AI agent on day one. Start with the domains where better self-service would have a meaningful impact.
The four questions a BI strategy has to answer
Ask, Build, Trust, and Cost each need a clear plan and named owner. Together, they determine how widely analytics can scale without losing the consistency and governance your organization depends on.
1. Ask: Who can ask questions, and from where?
Decide which questions business users should be able to answer directly and which still need an analyst. Define what data people can access, what the data team governs centrally, and what happens when a question falls outside the available context. You don't need one policy for the entire company. Finance might be ready to self-serve on endorsed revenue data while another domain still has disputed definitions that need resolving.
But AI introduces another important question:
where should people be able to ask?
Traditionally, BI strategies assumed people would come to a dashboard or reporting interface. Today, many questions arise in Slack, Claude, ChatGPT, and other applications where employees already work.
With the
Model Context Protocol (MCP)
, AI agents can connect to analytical systems and work with company data without people needing to open a separate BI application. Hex supports this approach through
Threads
, Slack, and
MCP
integrations, allowing people to investigate questions using shared business context and permissions.
Your strategy should account for analytics happening across these tools, not just inside your BI platform. The goal is to make trusted answers available wherever people work, without fragmenting the underlying context or governance.
2. Build: What can people create with data?
Decide what people should be able to build themselves, what the data team needs to maintain, and which analytical assets should become shared resources.
Traditional BI strategies focused on dashboard authorship and report maintenance. AI changes that equation. People can increasingly describe a dashboard, report, or interactive application in natural language and have an agent build it, rather than learning a drag-and-drop interface or waiting on an analyst.
With
Hex Generative Apps
, a prompt can become an interactive, code-backed application using the endorsements, semantic models, and Guides the data team already maintains. The resulting work remains inspectable and can be refined or reused.
That capability also introduces a new risk. Without a plan for ownership and reuse, AI-generated dashboards and apps can proliferate across disconnected files, chat conversations, and tools. Instead of dashboard sprawl, you end up with
AI data sprawl
.
Establish when an analysis should become a durable asset. For example, promote it when someone has asked the same question repeatedly, when it supports an important business decision, or when other teams would benefit from reusing it. Name an owner for every asset you promote.
The goal is to let more people build without creating more work for the data team to maintain afterward.
3. Trust: What makes an answer defensible?
Decide what trustworthy AI analytics means before people start using generated answers to make important decisions.
Hex's
State of Data Teams
research found that 31% of data leaders cite trust and data accuracy as their top AI concern. And research on enterprise text-to-SQL benchmarks demonstrates why: an AI agent can generate syntactically correct queries while misunderstanding complicated schemas or business logic.
The challenge isn't just the underlying AI model. It's whether the agent understands your business.
Define which sources the data team endorses, which metric definitions must be consistent, who can inspect generated queries, and what should happen when context is missing or ambiguous. This context can come from warehouse metadata, documentation, existing SQL, Guides, and semantic models rather than needing everything to be recreated inside one BI tool.
And governance doesn't stop when an agent produces a correct answer. As your business changes, context becomes outdated, new questions emerge, and the quality of answers can degrade.
Hex Context Studio
helps data teams observe how agents use context, identify missing or ambiguous information, and evaluate improvements. Instead of manually reviewing every query, the team can prioritize the areas where better context will have the most impact.
Decide who reviews those signals, how often, and who's responsible for making improvements.
Maintaining answer quality needs to be an ongoing process, not a one-time implementation project.
4. Cost: What does broader access actually cost?
Cost per seat tells you little on its own about what an AI-driven analytics deployment will cost. As more people ask questions, build applications, and run agents, usage can increase significantly.
The
State of FinOps 2026
found that AI spend management has become a major focus for FinOps teams, reflecting how quickly these costs have become part of enterprise technology planning.
Your strategy should account for BI licenses, AI usage, warehouse compute, and the ongoing work required to maintain context and governance. Identify who owns each budget and how usage will be monitored as adoption grows.
But rising usage isn't inherently a problem. If employees are answering questions that previously required hours of an analyst's time, that's part of the value you're trying to create.
Consider how your data team's work changes as well. Less time should go toward fulfilling repetitive requests, and more toward maintaining trusted data foundations, improving agent context, and tackling sophisticated analysis.
Where governance fits
All four questions already involve governance decisions, so don't treat governance as something you'll add in a later phase. The access boundaries in Ask, ownership rules in Build, and quality standards in Trust are all parts of the same strategy.
The additional consideration is that analytical work increasingly extends beyond your BI platform, introducing new requirements for identity, permissions, and observability.
For example, when an employee connects Claude to an analytical system through MCP, your strategy should establish which resources the agent can access, whose credentials it uses, and whether its activity can be audited.
The same principles apply to AI-generated dashboards, automated analysis, and shared analytical assets. Define who can publish and modify them, how sensitive data is protected, and how the data team can investigate problems when they arise.
Governance needs to cover the entire analytical workflow, not just the reports and dashboards published inside your BI tool.
Sequencing it without a two-year program
Start with the datasets behind your most consequential decisions and add context in the order it creates value. You don't need to model every possible question before allowing people to use AI analytics.
A practical sequence looks like this:
Endorse trusted tables and improve warehouse metadata.
Start with the sources behind your priority decisions. Clear table and column descriptions provide useful context for agents without needing a major modeling project.
Add business documentation and Guides.
Capture the logic that doesn't live in your schemas, such as how teams interpret their funnel, apply exclusions, or evaluate performance. Existing documentation can often be reused.
Build or sync semantic models where they add value.
Important metrics like revenue, ARR, churn, and pipeline benefit from consistent definitions. If you already maintain them in dbt MetricFlow, Cube, or Snowflake, reuse that work rather than duplicating it.
Enable self-service and reusable building.
Let business users ask questions, investigate results, and create analytical assets within the domains you've prepared.
Use observability to improve context.
Monitor which topics people explore, where agents struggle, and what information is missing. Let real usage guide your next investment.
Semantic models are valuable, but they represent one layer of context among several. As we explore in
Are Semantic Layers the Cornerstone for AI Analytics?
, not every question or business rule needs to be encoded in a semantic model before an agent can be useful.
The important shift is to treat context as something that evolves with usage. Start with what you have, learn from the questions people ask, and improve the foundations as adoption grows.
How you know the strategy is working
Measure the strategy by how quickly people get trustworthy answers and how effectively they can use those answers. Dashboard output and adoption still matter, but they shouldn't be your only measures of success.
For each priority business domain, establish a baseline and track:
Time to answer:
How long does it take someone to get a reliable answer, including necessary follow-up questions?
Self-service adoption:
What percentage of questions can people answer without submitting a request to the data team?
Analytical reuse:
How often are dashboards, apps, and other shared analytical assets used by multiple people or teams?
Answer quality:
Where are agents encountering missing context, ambiguous definitions, or incorrect results, and how quickly are those issues addressed?
Business impact:
Which workflows are reducing manual effort or contributing to measurable business outcomes?
Include context quality and usage trends in your regular reviews. A growing number of questions about a domain with little trusted context is a signal for where the data team should invest next.
The goal is to measure how effectively the organization works with data, not simply how much reporting the data team produces.
Make the governed path the fastest one
The BI strategy that survives AI is the one where the governed path is also the easiest way to get an answer.
People shouldn't have to choose between the flexibility of Claude or ChatGPT and the trusted definitions maintained by their data team. Nor should they have to wait on an analyst every time they need a new dashboard or want to investigate something unexpected.
A modern BI strategy brings those capabilities together: conversational self-service, AI-powered building, reusable analytical work, and shared context that extends into the tools people already use.
That's what Hex is built to enable, giving business users the freedom to ask, explore, and build while data teams maintain the governance and visibility needed to keep everything trustworthy.
Request a demo
to see how Hex can help put your BI strategy into practice, or start with our
BI buying guide
.
Frequently Asked Questions
How should a small team without a dedicated BI function scope this?
Start with a short list of important business decisions before evaluating tools. Pick two or three high-impact workflows, identify the trusted datasets behind them, and establish who owns access, context, and costs. Focus on reducing repetitive analytical requests without introducing an infrastructure project your team can't maintain. Expand into additional domains as you learn what people actually need.
How often should you revisit a business intelligence strategy?
Review the roadmap quarterly and revisit overall priorities at least annually. Some parts of the strategy need more frequent attention, particularly AI usage patterns, metric definitions, and context quality. Assign clear owners and use adoption, accuracy, and business impact metrics to determine what needs to change rather than reviewing the strategy document in isolation.
What do you do with teams that have already built their own shadow reporting?
Inventory it before trying to replace it. Shadow reporting often exists because the official workflow couldn't meet a real need. Identify the questions people are answering, the data they're using, and which analyses are worth preserving. Bring important metrics into governed definitions and offer a faster, trusted way to perform the same work, ideally from the tools people already prefer. Treat employees who built useful shadow workflows as potential champions rather than assuming every workaround needs to be eliminated.
Share:
twitter
linkedin
Exploring what BI should look like in the AI era? Get the BI Buying Guide for a breakdown of what’s changing and what to look for in the next generation of analytics.
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
