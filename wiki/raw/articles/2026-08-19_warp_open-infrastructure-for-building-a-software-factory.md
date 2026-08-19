---
title: "Introducing Warp Factories - open, flexible infrastructure for building your software factory"
source: "Warp Blog"
url: "https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory"
scraped: "2026-08-19T06:00:02.414656+00:00"
lastmod: "2026-08-18T22:46:17.000Z"
type: "sitemap"
---

# Introducing Warp Factories - open, flexible infrastructure for building your software factory

**Source**: [https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory](https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory)

Product
Introducing Warp Factories - open, flexible infrastructure for building your software factory
Zach Lloyd
|
August 18, 2026
Tl; dr
Warp Factories allow engineering organizations to deploy their own cloud software factories on open, flexible infrastructure
Built to increase coding agent ROI over time: use any model and any harness, measure effectiveness with evals and benchmarks on your own data, built-in self-improvement and memory.
Easy to start: set up a factory to triage, spec, implement, review and verify on your codebase in less than five minutes.
AI sovereignty: you own your data, inference and compute. We provide the infrastructure and control plane; you own and customize the rest.
Flexible infrastructure: factories are defined as code and built to integrate with the tools you already use.
Available in closed beta today: apply here and qualified orgs get $10k of factory use on us to get started.
Full walkthrough of Warp Factories
Introducing Warp Factories
Warp Factories provide flexible, open infrastructure to accelerate companies building internal cloud software factories.
For engineering leaders, this infrastructure helps measure and improve coding agent ROI over time. It provides agent governance and controls. It allows your team to focus more on building your product, rather than building infrastructure.
For developers automating workflows, Warp Factories gives you the building blocks for making your own scalable, secure factories that improve over time. It’s factory infrastructure you could build yourself, but built for scale, and with the annoying bits taken care of so you can focus on optimizing your factory for your product.
Problems with interactive agents
Over the past year, pretty much every engineering organization has made the transition from writing code by hand to writing code with agents. These agents are viewed as developer tools – every developer installs, configures, and operates them to produce PRs at an increasing rate. Developers interactively prompt these tools on their laptops.
While interactive agents do increase productivity, they also have issues and aren’t the correct end state given the rate of improvement of models. I hear again and again from eng leaders that interactive agents have created two major problems that Warp Factories solve.
The first problem is measuring and improving coding agent ROI over time. When I speak with customers there’s  consensus that coding agents add productivity, but it’s unclear if they are worth the cost. This is especially true as usage increases. It’s evident that you don’t always need to be at the frontier, and that open weight models should be in the mix. Engineers and eng leaders want systems that improve coding agent throughput, cost and quality over time.
The second problem is governance and control. The current setup where every user installs a bespoke coding agent that runs on their laptop is a governance nightmare. Engineers install a variety of agents, each having access to all of the systems they are logged into, creating security holes when agents go off the rails. There’s no standardization of skills or MCPs, all data exhaust the agents produce is lost, making it hard to create standards and measure improvement.
Cloud software factories are the solution
The solution to both of these problems is cloud software factories.
In case you aren’t familiar, a cloud software factory is an automation loop around the SDLC, where cloud agents triage, spec, implement, review, verify and monitor work. Humans stay in the loop at key decision points. Over time a good software factory implementation helps increase software throughput, manages costs and reduces defect rate. I predict software factories will be as ubiquitous as CI/CD in the next few years.
The goal of deploying factories is to start automating some percentage of your easier work as soon as possible. At Warp we are currently automating about 30% of our tasks through our factories and expect this number to rise quickly in the next few months.
This idea probably isn’t new to you. Most organizations I chat with have at least a few engineers building the components of cloud factories, even though they might not think in factory terms. It’s very easy to get started, by putting a coding agent SDK in a Docker container and vibe coding a web app to trigger runs or a slack app to chat with your code.
The problem with the build-it-yourself approach is that getting to a scalable, solid system that improves over time and solves all the problems of interactive agents is actually a big endeavor. I wrote a whole
guide
on this that’s worth reading for more context.
Instead, most companies should be adopting infrastructure to help them build their factories. That doesn’t mean outsourcing responsibility for your factories. It means building them on a platform that accelerates their development and makes them more reliable, scalable and cost-efficient over time. Every engineer on your team will eventually be responsible for improving your factories. Our vision is providing you all with the core components to get to this point as quickly as possible. In an age where time to ship is arguably your most important competitive advantage, you should be standing up and operating a factory today, not six months from now.
That’s why we’ve decided to approach the software factory category as
infrastructure
rather than as a
factory product
or
AI teammate
. Infrastructure implies you build on top of it and that you own what you build. It implies flexibility, programmability and customization. We believe firmly this is what agent-forward development teams are looking for as they automate more of their internal workflows.
Factory definitions as code
In Warp, factories are defined as version-controlled code. This has the same benefits as other infrastructure-as-code platforms like Terraform: the factory is completely specified at any point in time. You can roll back or forward to factory versions, canary them, test them, and so on.
In an agent-first world it also enables agentic changes to the factory, which is a huge driver of factory self-improvement, discussed below.
Every factory encompasses:
One or more repos, roughly corresponding to a single product to automate work on
Definitions for distinct agents for different parts of the assembly line (e.g. for Triage, Implementation, Verification, etc).
Skills, MCPs, permissions
Our default factory has agents specifically for:
Triage:
deciding what to do with work items (implement, spec, or wait)
Spec:
interact with a human to spec out a complex or ambiguous change
Implement:
write the code
Review:
review the code
All of these agents have access to computer use on Linux and Mac to reproduce issues and prove correctness of changes.
An implementation agent uses computer use to click through a dropdown it built to verify the change works end-to-end. This video is saved to PR descriptions for human review.
You also can add custom agents with their own automations, skills, etc. (More on this below).
The factory workflow
Work enters your factories from the tools your team already uses:
Communication tools like Slack or Teams
Task trackers like Linear or Jira
Source code forges like Github or Gitlab
Terminals, IDEs and other local coding agents via the Factory MCP
Message your factory agents directly from Slack. Your foreman agent will route requests from triage to spec writing to implementation and review
Warp provides integrations into your common tools out of the box and provides a complete API, SDK and CLI for programmatically building more integrations.
A work item enters the factory by triggering the factory’s
foreman
agent. This triggering can be explicit (e.g. sending a slack message to the foreman), or implicit (e.g. adding a tag to a JIRA issue).
Mention your factory agents from taskboards like Linear, Jira, or GitHub issues
The foreman is an orchestrator agent that takes the initial context from its trigger and splits off subagents to tackle whatever is needed to get the work item to the next agent in the assembly line. It chooses the best model, harness and context for these subagents to optimize cost and quality. Each of these subagents has specific skills, MCPs, and memories it has access to, and can be optimized over time.
For example, say there’s a server crash you want to automatically fix.
A monitoring agent that integrates with Sentry might detect this and create a Linear ticket for it.
That would trigger the factory triage agent to examine the crash and decide if it was simple enough to fix.
If so, it would move on to the implementation agent to write the code.
The implementation agent might use computer-use to verify the fix, and then open a PR for the code review agent to review.
If it looks good the fix could simply be merged directly, or, depending on your policies, a human could review and iterate on it.
At any point in this flow, a human can step in and steer the process or bring the in-process work into a local setup to iterate on using the Factory MCP.
As mentioned, everything that defines this flow lives in code. That allows for it to be versioned and for you to customize endlessly. It also – crucially – allows for agents to improve how the factory works.
Note that this flow can also be adopted piecemeal – if you want to start your factory just by adding a triage agent or a computer use verification agent, that’s possible too.
Natively multi-model and multi-harness
Our factory agents are built to support whatever model or harness is
best for your workflow
. You can use Warp’s SOTA agent for multi-model access, including open-weight models, or you can directly run Claude Code or Codex as the harness.
Our goal here is to give you all the options, measure them against your own workflows, and land on what’s best.
Metrics, evals and self-improvement
The point of setting up a factory is not just to automate some percent of work today, it’s to increase that automation percentage over time, while optimizing also for cost and quality.
Get a birds-eye view of cost and velocity to monitor the ROI of your factory overtime
Warp Factories provides the building blocks for long-term measurement and improvement.
On the measurement side we provide a rich set of queryable metrics on agent throughput, cost, quality and ROI. These are visible in every Factory’s control room view and also available via API and Factory MCP for agents to do analysis on.
We also provide built-in eval capabilities, so that you can measure and improve factory performance on
your own workflows
. Full details are here, but at a high level, we provide scorers that evaluate how well work items are flowing through the factory. How many tokens were spent, how good was the code, did it cause defects, etc. You can also define your own custom scorers.
These scorers drive two features for optimizing your factory: Self-improvement loops and Benchmarks.
With
self-improvement
enabled, we create “observer” agents that score some percent of agent runs and look for ways to improve the score. The available knobs are what model or harness was used, what context was provided, the contents of skills and so on. Since all factory definitions live in code, the observer agents are able to make PRs that improve the underlying factory functionality automatically.
Benchmarks support explicit, repeatable comparisons for fixed tasks across different factory configurations. For example, say you want to figure out the best model to use for frontend tasks within your factory. You can accomplish this by curating a set of benchmark tasks and then scoring those tasks across different model and harness configurations. Since Warp is both multi-model and multi-harness, you can create benchmarks that compare things like “GLM 5.2 in Warp’s harness vs. Claude Code running Opus.”
The factory app
While most work going into the factory originates in the tools your team already works in, we also provide a “control room” web app that shows everything happening.
That means you can easily see:
All factory agent runs, live and historic
The status of all work items, kanban-style (e.g. triaged, planned, etc)
All automations
All other configurations
And for any live factory run, you have the ability to open it up on the web (local or mobile), and view or interact with the running agent.
Warp Factory MCP – interact with the factory from any coding agent
We realize that your factories need to integrate with all the agentic tools you’re using, so we are also launching a Factory MCP that gives full interoperability for any coding agent or MCP client. Via MCP, you can put work into a factory, pull status, guide sessions, and so on.
This allows engineers across the team to use the local coding agent of their choice – Claude Code, Codex, Cursor, etc – to start work and push it into a factory for review and verification. Likewise any coding agent can pull work down from the factory to iterate locally in a tight loop.
Custom agents and automations
Warp provides the default factory agents to help teams get started immediately, but our infrastructure also allows for the definition of arbitrary agentic workflows.
You can define custom agents with their own prompts, MCPs, etc, that respond to arbitrary triggers and take actions across all your integrations.
A good use case here is if you wanted to build a periodic dead-code removal agent – it’s easy to set this up using all the same infrastructure used in the main factory loop (all the same skills, mcps, etc), but have it do a specific task that isn’t part of the normal SDLC flow.
Integration with Warp Terminal and Warp Agent CLI
Warp Factories are decoupled from Warp’s other products, but they interoperate well. The CLI and Terminal both ship with native MCP support for Warp Factories, which makes it very easy to iterate locally on changes with Warp’s agent and then move the work into the factory when it makes sense.
AI Sovereignty
Warp Factories provide a solution that is inherently AI sovereign. When you deploy a factory through Warp, you have the ability to
Bring your own inference (or we can provide it)
Bring your own hosting (or we can provide it)
Host all data exhaust from the factory, including agent conversations, evals, memories (or we can host for you)
Prohibit any kind of training or use of your data through ZDR
Our strong belief is that your software factory is a key competitive advantage of your business, and you should own everything associated with it.
Try Warp Factories today
We are currently onboarding a limited number of companies onto Warp Factories before opening the gates to the world. For select folks, we are offering $10k of factory usage to help get you started.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Aug 4, 2026
|
Product
6
min
Introducing the Warp Agent CLI: a CLI coding agent that does what others can't
6
min
Aug 3, 2026
|
Product
7
min
How to build a cloud software factory - computer use verification
7
min
Jul 18, 2026
|
Product
4
min
Get agents off your machine
4
min
May 20, 2026
|
Product
6
min
Bring your own inference to Warp
6
min
May 19, 2026
|
Product
6
min
A single pane of glass for managing all of your cloud agents
6
min
View all articles
