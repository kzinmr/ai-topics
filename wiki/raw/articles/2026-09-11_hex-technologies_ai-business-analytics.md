---
title: "AI in business analytics: tools, strategies & case studies"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/ai-business-analytics/"
scraped: "2026-09-11T06:00:17.903909+00:00"
lastmod: "2026-08-28"
type: "sitemap"
---

# AI in business analytics: tools, strategies & case studies

**Source**: [https://hex.tech/blog/ai-business-analytics/](https://hex.tech/blog/ai-business-analytics/)

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
AI in business analytics: tools, strategies & case studies
Most organizations have adopted AI in some form, but only a fraction have scaled past pilot projects. Here's how to close the gap.
The Hex Team
Data
August 28, 2026
Share:
twitter
linkedin
In this article
How teams are actually using AI for analytics
How to evaluate AI analytics
Where AI analytics projects go wrong
Shipping your first AI analytics use case
What teams that shipped real results did differently
Start with context, scale with observability
Frequently Asked Questions
Get started for free
Your CEO just asked when AI analytics will start delivering real return on investment (ROI). You're not sure what to tell her, because you're still figuring that out yourself.
AI's biggest impact on analytics is deceptively simple: anyone can ask a question in natural language and get an answer. That's a fundamentally more accessible way to work with data than traditional business intelligence (BI), where getting an answer meant either building a dashboard or filing a request with the data team. But that accessibility creates real challenges.
Can you
trust the answers
? Are they governed by the same metric definitions your data team would use? And what does it cost when every question burns tokens against an LLM?
AI also makes it possible to meet people where they already work (asking data questions in Slack, through MCP integrations, or from the command line), which compounds both the opportunity and the governance stakes.
You're not alone in wrestling with this. While
88% of organizations
now use AI in at least one business function, only about a third have started scaling their AI programs (McKinsey's State of AI 2025). And according to Hex's
State of Data Teams
2026 report, 31% of data leaders cite trust as their top concern with AI adoption, nearly twice as much as any other concern.
The gap between adoption and impact is where most teams stall. This guide covers what actually closes it: which workflows matter most, how to evaluate your platform, how to avoid the most common failure modes, and what teams that shipped real results did differently.
How teams are actually using AI for analytics
A few common workflows are emerging as AI reshapes how organizations work with data. They overlap, but each solves a different problem, and understanding where each one fits helps you invest in the right capabilities.
Conversational analytics: anyone can ask a question
This is the workflow reshaping analytics fastest. Business users ask questions in plain language (in a dedicated interface, in Slack, or through MCP integrations) and get charts, tables, and explanations back. Tools like ChatGPT and Claude have made this interaction pattern feel natural, but applying it to your organization's data introduces hard problems that general-purpose chatbots don't solve.
The central one is trust. When a conversational interface returns a number for "churn rate" or "customer acquisition cost," it's using
someone's
definition. If that definition isn't governed, the answer might be technically correct for one team and completely wrong for another. Accuracy depends on the context available to the AI: endorsed tables, business rules, and metric definitions that tell it what those terms mean in your organization.
A common assumption is that you need a complete semantic model before conversational analytics works. That's one vendor's worldview, not the full picture. Lighter-weight context (endorsed tables, warehouse descriptions, workspace rules) can get you started. The latest models generate accurate queries from well-described schemas paired with clear business rules, without a fully formalized context layer. Paired with observability into agent behavior, this gives you a faster path to identifying where formal semantic models are truly necessary rather than building them speculatively.
One question matters more than the rest: can you inspect what the AI did? If your analysts can't verify the generated SQL, trust erodes fast. Hex
conversational analytics
takes this approach, showing the underlying queries and connecting answers to governed context at every step.
Coding agents for exploratory and advanced analysis
Tools like Cursor, Claude Code, and Codex have shown what coding agents can do for software engineering. The same pattern is hitting analytics: AI agents that write SQL, generate Python, build visualizations, and run multi-step analyses. For data teams, this is the 10x productivity story. The kinds of deep exploration that used to take days can collapse into hours.
The governance question here is different from conversational analytics. A business user asking a question in plain language needs guardrails they can't see. An analyst working in a notebook needs guardrails they can. The agent should write queries against governed definitions and endorsed tables, but the analyst should be able to inspect, modify, and validate every step. The best pattern is an
agentic notebook
where the AI does the heavy lifting while the human retains full control over the logic.
The risk to watch for: coding agents are powerful enough that analysts can build production-quality outputs fast, but if those outputs aren't connected to governed context, you've just accelerated the creation of ungoverned artifacts. The agent's speed is only valuable if it's grounded in the same definitions the rest of the organization trusts.
There's a second gap that matters just as much: what happens after the analysis is done. In a local coding environment, the output lives on one person's machine. Sharing it means copy-pasting into a slide deck or scheduling a screen share. In a platform like Hex, the same agentic notebook that produced the analysis can be shared with collaborators, reviewed in context, and published as an interactive data app that stakeholders explore on their own. That path from exploration to collaboration to publishing is what turns individual analysis into organizational knowledge.
Vibe-coded dashboards and data apps
The third workflow is the most surprising to traditional BI teams: using AI to build interactive dashboards and data apps from natural language descriptions. Instead of dragging and dropping in a BI tool, a user describes what they want (a churn dashboard filtered by segment, an inventory tracker with scenario modeling), and the AI generates a working application.
This collapses the gap between "analysis exists" and "stakeholders can use it." An analyst or business user doesn't need to spend hours clicking around in a BI tool's dashboard builder to configure a visualization. Instead, it becomes a fully customizable and interactive
data app
that business users can filter, explore, and act on, without filing a request or waiting for an engineering sprint.
The governance stakes here mirror conversational analytics: does the generated app use the same metric definitions and data sources as the rest of your stack? If it pulls from ungoverned tables or invents its own calculations, you've created a polished-looking source of unreliable answers. The app needs to inherit its context from the same governed layer that powers your conversational and exploratory workflows.
How the pieces fit together
These three workflows aren't siloed tools. In the strongest implementations, they share the same governed context. Data flows from source systems into a cloud warehouse, passes through transformation tools like dbt, and reaches a governed context layer where metrics and definitions are standardized. Conversational analytics, coding agents, and vibe-coded apps all sit on top of that context layer, drawing from the same endorsed tables, workspace rules, and semantic models.
The outputs feed into operational workflows: Slack, customer-facing portals, MCP integrations, or published interactive data apps. The specifics vary, but the principle holds: AI workflows produce trustworthy answers when they operate on governed context, and the strongest pattern is starting with what you have and deepening governance where observability shows it's needed.
How to evaluate AI analytics
The workflows above are emerging fast, but not every platform handles them equally. When you're evaluating AI analytics, whether you're choosing a new tool or pressure-testing the one you have, three questions cut through the noise.
AI analytics experience
Can people actually ask real questions, follow up, go deeper, and turn their work into something reusable? A lot of tools stop at the first answer: you ask a question, get a chart, and that's it. The experience that matters is the full arc: asking a question, getting an answer, asking a follow-up that refines it, exploring an unexpected result, and then turning the whole thing into a dashboard or data app that others can use without starting over.
The gap between "you can ask a question" and "you can do real analytical work" is where most conversational analytics tools fall short. If the tool can't support follow-up questions that build on previous context, or if every answer is a dead end that can't be extended into deeper analysis, you'll end up back in the request queue.
Trust and accuracy
What context does the system use to generate answers, and can you inspect how it got there? This is the question that separates tools that demo well from tools that work in production.
According to Hex's State of Data Teams 2026 report, 31% of data leaders cite trust as their top concern with AI adoption. That concern is justified when AI answers are opaque. The evaluation checklist here is short: Can you see the generated SQL or code? Does the system use your governed metric definitions, or does it infer its own? Can accuracy improve over time as you add context (endorsed tables, workspace rules, semantic models) rather than requiring everything upfront? And does the platform give you observability into where answers are falling short, so you know where to invest governance effort next?
Context Studio
is Hex's answer to this: it shows you which questions produce unreliable answers, so you can tighten context in the specific areas that matter rather than trying to govern everything before you start.
Ecosystem integration
Can your analytics work across Slack, Claude, ChatGPT, coding agents, and internal tools without fragmenting context and governance? This is increasingly the deciding factor as AI analytics moves from a single interface to something embedded across the organization.
The risk is real: if your conversational analytics tool uses one set of definitions, your coding agent uses another, and the dashboard someone vibe-coded pulls from a third source, you've multiplied the metric chaos problem rather than solving it. The platform you choose needs to be the governed layer underneath all of those surfaces, not just one more surface alongside them.
According to IBM,
60% of CEOs
are looking into mandating additional AI policies to mitigate risk. That mandate gets harder to enforce when every AI touchpoint operates independently. The strongest approach is a single context layer that governs answers regardless of where the question is asked: in the app, in Slack, through MCP, or from a coding agent.
Where AI analytics projects go wrong
Most AI analytics failures share a handful of root causes. Recognizing them early is cheaper than discovering them six months into a deployment.
Metric chaos.
Different teams define "churn," "customer acquisition cost," or "active user" differently, and AI tools amplify the inconsistency. When a natural language interface returns a number, it's using
someone's
definition, and if that definition isn't governed, the answer might be technically correct for one team and completely wrong for another. The fix: start by endorsing your most critical tables and adding clear descriptions. Add workspace rules for the terms that cause the most confusion. Formalize semantic models for your highest-stakes metrics as adoption grows.
Shadow AI
.
When the data team's request queue is three months deep, business users turn to ChatGPT or build their own spreadsheets. The answers they get are fast, plausible, and frequently wrong. General-purpose AI tools don't have your data context, your metric definitions, or your business logic. The governed alternative is
self-serve analytics
that gives business users speed
and
accuracy. But that only works if the governed path is fast enough that people actually choose it over the ungoverned one.
Analysis stuck in local environments.
A data analyst builds a predictive model in Cursor or Claude Code that performs well in testing. It shows up in one presentation, maybe two. Then it sits in a local coding environment nobody else can access or put into production. The gap between "analysis works" and "analysis drives decisions" means giving non-technical stakeholders a way to interact with the outputs: adjusting parameters, filtering to their segment, exploring what-if scenarios.
Governance theater
.
Policies exist on paper, but tooling doesn't enforce them. Analysts route around the governed path because it's slower than the ungoverned one. The only governance that actually sticks is governance built into the workflow, where following the rules is the path of least resistance, not a detour.
Shipping your first AI analytics use case
If your foundations are reasonably solid, with clean data pipelines, access to the data you need, and at least basic endorsed tables and descriptions, here's a practical path to shipping something real within about 90 days.
Weeks 1–3: Pick your use case and confirm the data.
Start with a problem that's both high-value and bounded: churn prediction for a specific segment, demand forecasting for one product line, or automating a recurring ad hoc report that eats a full day every week. Confirm that the data sources exist, are accessible, and have reasonable quality. Endorse the key tables and add the workspace rules you'll need.
Weeks 4–8: Build the minimum viable product (MVP).
Stand up the model, natural language interface, or automated report. Run it in parallel with the existing process so you can compare outputs. This is where you'll discover whether your data quality is actually good enough and whether your context holds up under real-world queries. In Hex, this often looks like building the analysis in an agentic notebook with Notebook Agent, then publishing it as a data app that stakeholders can explore without touching code. Context Studio shows you where answers are falling short, so you can tighten context in the specific areas that matter.
Weeks 9–12: Embed it in the workflow.
Move the output from "interesting analysis" to "thing people actually use." That might mean embedding a dashboard in Slack, building an interactive data app that stakeholders check weekly, or setting up automated alerts when a metric crosses a threshold. Define what success looks like: reduction in ad hoc requests, faster time-to-decision, forecast accuracy improvement. Set up monitoring so you know if the model drifts.
The goal at 90 days is a working proof point that demonstrates value and teaches your organization how to ship AI analytics iteratively.
What teams that shipped real results did differently
Statistics about AI potential are everywhere. Concrete stories about teams that automated recurring workflows, migrated from legacy BI, and delivered AI analytics where people already work are harder to find. Here are three worth studying.
Automating recurring workflows at EliseAI
EliseAI
, an AI company transforming healthcare and housing operations, doubled in size every year for four years running. That growth turned the data team's ticket queue into a bottleneck: existing BI tools were either too rigid for the business or too technical for non-analysts, and every new customer-facing workflow meant more custom work.
Rather than staff up to keep pace with requests, the team rebuilt their approach around Snowflake and Hex, letting Notebook Agent do the heavy lifting on the workflows that ate the most analyst time.
The clearest example: quarterly business review (QBR) prep. A rep used to spend two days building a customer deck by hand. An analytics engineer used Notebook Agent to package the whole workflow into a data app that merges data from Snowflake, Salesforce, and product databases; reps now generate a fully customized deck in three clicks. A separate audit-prep app scans a customer account, flags unused features, quantifies the performance lift each one would deliver, and links directly into product settings so reps can make changes on the call. Threads handles the one-off questions that used to fall through the cracks — a rep can ask "who hasn't had a QBR in the last 90 days?" in plain language and get an answer without writing SQL.
The data team stopped being a request queue and became the team building the workflows the rest of the company relies on.
Migrating from legacy BI at LangChain
LangChain's analytics engineering team
had data spread across Segment, BigQuery, dbt, and Salesforce, but no easy way to access insights outside of a few dashboards in their legacy BI tool. Creating anything new required their sole data person to build abstractions and YAML files before analysis could begin. Non-technical users waited in the queue; technical users stitched together workarounds with Claude Code and Python scripts.
The team migrated everything to Hex in six weeks. Notebook Agent handled roughly 90% of the dashboard rebuilds. The team copied YAML files from the legacy platform, pasted them into the agent, and got production-ready dashboards on the first pass. They consolidated 60% of active dashboards and deprecated the rest. Today, 100% of the company accesses data through Hex, and the analytics engineering team has shifted from fielding requests to curating context in Context Studio so the agent gets more accurate over time.
The migration wasn't just a platform swap. It was the moment LangChain went from a data request queue to a data-fluent organization.
Delivering AI analytics in Slack at Neo Financial
Neo Financial
, Canada's fastest-growing fintech, needed to scale data access across a rapidly growing organization without compromising governance. They'd tried point-and-click analytics tools before, but those required everyone to understand complex data models, and they were separate from the data team's own tools, creating fragmentation.
After turning on Hex's Slack integration, adoption went viral. Active users grew from 12 to 139 — including the CEO, VP of Ops, and CTO — and the team generated over 4,000 Threads messages, with 35% of questions originating in Slack. Trust came from two things: every query runs under the individual user's OAuth credentials (critical for a regulated fintech), and Threads displays the logic and analysis alongside every answer so anyone can verify the results.
For the data team, the shift was transformational. Instead of fielding ad hoc questions, they now monitor quality and focus on ingesting new datasets and building better context, a much better use of their time.
The shared pattern
These stories share something worth noting: the technology worked because it met people where they already were. EliseAI didn't ask reps to become analysts; the data team packaged the highest-effort workflows into apps that put the answers right in the rep's flow of work. LangChain's team didn't ask everyone to learn a new tool; the agent rebuilt what they already knew. Neo Financial didn't ask executives to open an analytics platform; the answers showed up in Slack. In all three cases, governed context traveled with the answer regardless of where the question was asked. That's the pattern that scales.
Start with context, scale with observability
AI in business analytics has moved from experimental technology to something teams depend on daily. The organizations seeing real results share a pattern: they start with the context they have (endorsed tables, warehouse descriptions, workspace rules), use observability to see where AI answers fall short, and invest in deeper governance (semantic models, formalized definitions) where it matters most.
Tools have matured. The bottleneck is context, not capability. And the path to
trusted AI analytics
is faster than it used to be, because you don't need to govern everything before you start. You need to start, observe, and govern where it counts.
For teams looking to close the gap between AI adoption and real impact, Hex lets anyone explore data using natural language, with or without code, on trusted context in one AI-native workspace. Data teams get deep analytical power with
Notebook Agent
; business users get governed self-serve answers through Threads. Context Studio shows you where to invest governance effort next, so context improves continuously rather than all at once.
Try Hex free
or
request a demo
to see how it works with your data.
Frequently Asked Questions
Do we need a complete context layer before AI analytics can deliver value?
No, and treating it as a prerequisite is one of the most common reasons teams stall. The latest AI models can generate accurate queries from well-described warehouse schemas paired with endorsed tables and clear business rules, without a fully formalized context layer. Start there, then use observability (Context Studio shows which questions produce unreliable answers) to identify where formal semantic models are truly necessary. Build governance incrementally based on what you learn, not speculatively based on what might go wrong.
How do we prevent AI analytics from amplifying inconsistent metric definitions?
Start by endorsing your most-used tables and adding descriptions so AI agents know which data to trust. Add workspace rules for the terms that cause the most cross-team confusion ("active user," "churn," "customer acquisition cost"). Formalize semantic models for the highest-stakes metrics as adoption grows. The key is treating this as a spectrum: each layer of context you add makes every AI-generated answer more consistent, and you can start seeing value from the lightest layers immediately.
What's the fastest way to show ROI from AI analytics?
Pick one high-frequency, low-complexity use case: a recurring ad hoc report that eats analyst time every week, a question that hits your queue repeatedly, or a metric stakeholders constantly ask about. Build it as a governed self-serve experience (a Threads workflow or an interactive data app) and measure the reduction in ad hoc requests. The EliseAI and Neo Financial stories both followed this pattern: the data and tools already existed; the value came from making governed answers accessible to the people who needed them. A single proof point that saves measurable time builds the case for broader investment.
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
