---
source_url: https://stripe.dev/blog/meet-stripes-knowledge-ai-platform
ingested: 2026-09-25
sha256: 4f5bd6cf01c646323647c8dcca305b2c1c81142de51858725013c32e12c46970
---

# Meet Stripe's Knowledge AI Platform

Date: 2026.7.30 | Authors: Anna Mason, Sharadh Krishnamurthy, Anupam Upadhyay

Stripe's Knowledge AI Platform is our versatile AI agent platform built to handle diverse non-coding knowledge work, from quick queries to complex, multi-day projects. By connecting employees to over 1,000 internal tools and skills, it enables secure, enterprise-scale productivity across the organization.


Coding agents transformed engineering at Stripe, but non-engineers like sales reps, finance analysts, technical account managers, and others felt left behind by the AI wave of Claude Code and Codex. No existing tool could handle the data security requirements and specific workflows Stripe needed: querying data warehouses, researching accounts before sales calls, triaging incidents, modeling revenue scenarios, or preparing compliance reviews. That all changed when we shipped Stripe’s knowledge AI platform.

![](/images/meet-stripes-knowledge-ai-platform/image5.gif)

Within two weeks of our April launch, most of Stripe was using Stripe's Knowledge AI Platform, also known as Kai. Today, 83% are weekly active users, including nearly all of GTM (marketing, sales, customer success managers, and technical account managers). Most Kai sessions require many turns, with users doing deep research, creating specific artifacts, or refining assets before sharing internally or externally.  With Kai, everyone at Stripe has an agent built specifically to help them with their day-to-day work.

## Why we built a Knowledge AI Platform

For coding tasks, the specific change varies, but the workflow and tools needed to perform the task stay about the same. You edit files, run tests, commit. The programming languages vary, but the shape of the work is rather uniform, which is why a single agent architecture works well. Knowledge work is the opposite side of that spectrum. Tasks like researching an account or preparing a compliance review require different tools, different data, different outputs, and different definitions of "done".

Before Kai, we had two AI options for knowledge work:

-   **NoCode Agent Builder**: Anyone could build and deploy workflow-specific agents that could use tools. Over 4,000 agents were built using this system. However, we quickly noticed that teams were writing conceptually similar prompts but with varying levels of quality, and found the proliferation of these micro-agents increasingly hard to monitor and maintain.
-   **Coding agents**: Coding agents were powerful, but they introduced a different set of risks. Since our goal is to enable improved productivity for all of Stripe, some users altered their workflows and chose coding agents.  However, security concerns quickly emerged, along with a new support burden for code quality teams that had never supported non-engineers before.

From these experiences, we realized that building a knowledge AI platform required getting three things right: scaling expertise without centralizing it, meeting users wherever they work, and enforcing guardrails that don't exist in code.

### Scaling expertise without centralizing it

The range of expertise required to serve Stripe’s users is staggering. The people who know how to triage a billing escalation or model a revenue scenario are not centralized and certainly aren't on the team building the agent infrastructure. They're distributed across dozens of specialized domains – GTM, Finance, Marketing, Legal, Data Science, and more – each with its own tools, data sources, workflows, and judgment about what "good" looks like. Multiply this across all the products and countries Stripe operates in, and the result is astonishingly complex. Kai has to model that complexity in a way that makes it invisible, so that the task just works.

### The agent has to roam

Where the agent surfaces matters as much as what it knows. Not everyone works in a browser tab, and fewer still in a terminal. So a knowledge agent can't just be a single product; it has to be a platform, flexible enough to embed itself wherever work happens.

For example, consider an internal application our Finance team uses to model complex changes in Stripe's operating budget: the agent needs to read the context, research related documents, propose valid changes, and summarize the differences, all without pulling them out of the app.

Building a standalone agent product wouldn't work.  Instead, it would force users out of their natural workflows and into a new app. Building a separate agent product for each surface wouldn’t work either; it’d be hard to maintain, and users who span multiple tools would have a fractured experience. The platform has to meet the user where they are.

### Building guardrails from scratch

Coding agents operate in an environment with decades of fast, verifiable guardrails: compilers reject invalid syntax, tests catch regressions, and git makes every mistake reversible. Knowledge work has very little support for these constructs.

Consider a core invariant at Stripe: _“you shouldn't combine data from two unrelated customer contexts in a single analysis.”_ A user may have legitimate access to both contexts independently, but they can never appear in the same session. The isolation boundary isn't _"what can this person access based on their authorization token?"_, but instead _"what should this task be allowed to view given this context?"_  The platform has to enforce these implicit guardrails that users rely upon.

## How we built Kai

A single monolithic agent simply cannot encode all of these constraints effectively. And, asking every domain team to independently build secure, hosted, performant agent infrastructure doesn't scale either. To manage this challenge, we built Kai in three layers:

-   **Surface-agnostic APIs** that give multiple interfaces into the same agent
-   **Agent Studio** where domain owners build and govern their own Kai agents, and
-   **Execution environments** to deliver security in seconds without anyone thinking about infrastructure.

### Surface-agnostic APIs

Kai ships with an opinionated web application and a Slack integration, but the main primitive is the underlying API that powers them both. The agent is a service, not an application, and surfaces are simply customized views into it.

Most Stripes interact with Kai through the internally hosted web application. There's no infrastructure to set up – it's available to every employee on Day 0.

Any internal tool can also embed Kai, and many have chosen to do so. For example an employee working in our business intelligence platform can ask Kai a question from within their existing application because our Chrome extensions surface Kai capabilities inside web-based third-party tools.

![](/images/meet-stripes-knowledge-ai-platform/image3.png)
> Custom applications embed Kai via APIs to bring agentic experiences to all workflows

### Agent Studio

Agent Studio is the control plane for domain owners. Teams use it to build, test, and monitor their skills, custom Kai agents, and tool selections. A GTM team, for example, owns a Kai agent tuned to their workflows. It loads their skills by default, connects to their data sources, and presents outputs in the format their users expect. Agent Studio surfaces usage data and quality signals alongside each asset, so domain owners can see what's working without asking the platform team.

![](/images/meet-stripes-knowledge-ai-platform/image4.png)
> Assets are organized into areas across Stripe that are managed by domain experts

### The execution environment

![](/images/meet-stripes-knowledge-ai-platform/image1.png)

This is the layer that makes the platform's promises real. The core primitives, including the agent harness, sandbox, workflow orchestration, and access control framework, are deliberately shared with Stripe's product-facing agents. Internal knowledge work operates on the same sensitive data and serves the same users as our external products, so it requires the same security and compliance bar. Sharing the substrate forces discipline and creates a flywheel: improvements to the execution environment benefit both internal and product agents simultaneously.

The agent harness, built using [LangChain’s deepagents](https://github.com/langchain-ai/deepagents), runs on Kubernetes with a secure per-session sandbox and a multi-tenant virtual filesystem. Within a session, the agent works with a virtual filesystem where it creates and iterates on artifacts, while a secure code execution sandbox is used for analytics and data processing.

It's built to hold state across long, complex sessions — one recently reached 932 turns. With Kai’s deep task management capabilities, a single conversation can consist of hundreds of turns, and hundreds of tool and LLM calls without timing out or overloading the context window. This matters because knowledge work is rarely a single question. It's iterative reasoning that builds on itself, and the session has to hold that state without degrading.

![](/images/meet-stripes-knowledge-ai-platform/image2.png)
> User behaviors are changing, and sessions are increasingly used for deep multi-turn collaboration

One of the most interesting parts of the harness is how it chooses the correct skill to use. Kai is connected to 1,000+ skills and tools spanning various internal systems – from business intelligence dashboards that track key metrics, to project management tools that organize internal execution, and third-party services like Zoom and Google Workspace. Anyone can ask it a question and trust it will load the right context and use the right tools to get the job done. Coding agents have a natural advantage here: the folders they work provide a natural organization for skills and context. In a follow-up post, we’ll go into how we solved this without that pre-existing structure by utilizing a hybrid RAG/LLM approach, among other techniques.

## Impact

The results have been striking. New hires on GTM are Kai-native: they use it 2.7x more, and power users close 80% more value than low users within the same cohort. When Account Executives use Kai, they produce 2x the sales activity, create 17% more opportunities, generate 26% more revenue opportunities, and close 39% more deals when compared to the same sellers in weeks they don't use it. In aggregate, Kai has helped shift 25,000 hours per year from administrative work, to revenue generating work.

In finance and operations, Kai is helping Stripes analyze messy data, generate recurring digests, and turn fragmented context into usable artifacts.

In engineering, Kai is now a natural place to ask system questions, research for run requests, analyze logs, draft plans, and invoke more specialized agents and skills.

And across Stripe, more than 5,000 sessions everyday center on data analysis. This makes Kai a unique leverage point: by plugging in the right context about data quality and our analytics layer, we can ensure correct responses by default for most questions.

Stripes’ direct feedback backs up these aggregates: they report feeling “empowered to embrace AI” and “astounded at what Kai just does precisely correct”. But our favorite anecdote is a non-engineer who left a Kai intro session and immediately collaborated on a digest that pulls together Asana, Slack, and Jira into a single automated process.

## We haven’t won yet

At Stripe, one of our favorite catchphrases is “we haven’t won yet”, and that’s apt for Kai. We’re in the earliest stages of this journey, and have a lot more we want to do:

-   **Better state management:** General-purpose agents like Kai generate a lot of state as they iteratively make tool calls, pull down large documents, and more. We are continuously tuning both the “active” context being sent to the LLM and the “extended” context sitting in state stores like S3 or the virtual file system.
-   **Reflection and self-improvement:** We are working on a quality improvement loop that lets Kai reflect on traces involving a skill, propose improvements, test them, and submit changes for the skill owner to review.
-   **Better collaboration primitives:** Users generate a lot of context in their Kai sessions that is currently “locked in”, but that’s not how work gets done. We want to let people share what Kai surfaces across sessions, and let multiple people (and agents!) collaborate on the same artifacts.

Coding agents made AI feel concrete for software engineers first. Kai has helped bring that same sense of leverage to knowledge workers across Stripe. It’s interesting because while we have improved productivity considerably, we don't know the ceiling yet - and we’re excited to keep pushing the envelope here. If building agentic systems that power internal productivity and external agents sounds like your kind of challenge, [we’re hiring](https://grnh.se/b5wzjpge1us).
