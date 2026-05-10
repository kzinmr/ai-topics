---
title: "Introducing Warp 2.0: the Agentic Development Environment"
source: "Warp Blog"
url: "https://www.warp.dev/blog/reimagining-coding-agentic-development-environment"
scraped: "2026-05-10T01:28:03.572436+00:00"
lastmod: "2026-04-07T02:49:39.000Z"
type: "sitemap"
---

# Introducing Warp 2.0: the Agentic Development Environment

**Source**: [https://www.warp.dev/blog/reimagining-coding-agentic-development-environment](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment)

Company
Introducing Warp 2.0: Reimagining coding with the Agentic Development Environment
Zach Lloyd
June 24, 2025
Today, we’re excited to launch Warp 2.0, the first Agentic Development Environment.
In Warp 2.0 you get:
The top overall coding agent: #1 on Terminal-Bench (52%) and top-5 on SWE-bench Verified (71%). It features a fundamentally new and superior user interface compared to IDE and terminal coding agents.
Agent multi-threading and management with the ability to run and monitor multiple agents – all under your control.
The best interface for running agentic workflows across the entire software development life cycle, from setup and coding to shipping and production.
Founder and CEO Zach Lloyd introduces the Agentic Development Environment
Download Warp
Why build an Agentic Development Environment (ADE)?
Software development is rapidly evolving from a world where developers code by hand to one where they code by prompt. In the next year, it will be rarer and rarer to type code, even with autocomplete, or manually enter commands. Instead, every task will start with a prompt and be done in collaboration with agents. This could be coding, setup, deployment, debugging, incident management, whatever. It’s all going to be agentic.
The products on the market today, from AI IDEs to CLI coding agents, all miss the mark supporting this workflow. They bolt agents onto code editors through chat panels and bury them in CLI apps. What’s needed is a product native to the agentic workflow; one primarily designed for prompting, multi-threading, agent management, and human-agent collaboration across real-world codebases and infrastructure.
Warp 1.0, the terminal, was a first step to support this workflow. It had the right overall architecture: a modern input editor for writing prompts, block-based output for managing agent interactions. Being the terminal meant it had the right context to work across projects and development tasks. Through Warp Drive and MCP, it had built in knowledge sharing and team context, for both humans and agents.
However, even Warp 1.0 missed the mark. It lacked primitives for managing multiple agents, controlling their permissions, giving them maximal context, and, most importantly, first-class support for coding. It was a terminal, not an agent platform.
With Warp 2.0, the ADE, this is all fixed: it’s amazing at coding and really any development task you can think of. You tell it what to build, how to build it, and it gets to work, looping you in when needed.
We kept what’s best about Warp but re-oriented it around the agentic workflow in a way that feels totally natural and gives developers all the power, which has always been our mission.
In the weeks leading up to launch, we invited a small group of developers to try Warp 2.0. The results were remarkable:
Multithreading:
Heavy AI developers save 6–7 hours a week by running multiple agents in parallel
Coding:
Generated over 75 million lines of code with a 95% acceptance rate in the first couple weeks
Production quality:
We’ve been using Warp to build Warp, which is a 1M+ line Rust codebase. In fact, the universal input we launched in Warp 2.0 was built almost entirely by Warp’s agents.
What you get in Warp 2.0
Warp 2.0 has four capabilities in a single app: Code, Agents, Terminal, and Drive. The main interface is our universal input which accepts prompts and terminal commands and lets you kick off any agentic task.
Code: State of the art coding platform
Warp is now a state of the art coding platform scoring 71% on
SWE-bench Verified
and #1 on
Terminal-Bench
, making it the highest quality coding agent on the market.  Warp, however, has a superior user experience compared to other AI coding tools.
Anyone familiar with Claude Code will appreciate Warp’s coding workflow: type a prompt, attach context, and watch Warp work. Warp finds the relevant files using a range of tools, from grep, glob, etc to codebase embeddings (which we and our Preview users find especially useful on large repos). In addition, Warp supports a dedicated planning mode using state of the art reasoning models like o3 that help make sure humans and agents are aligned at the task at hand.
Agent generated code diff
Because of Warp’s low level in the stack, our agents can code across multiple repos at once, e.g. for coding client-server applications within a single conversation. Our coding agent also works on large codebases and large files (including allowing us to
build Warp using Warp
). Real users saw similar benefits: early testers have generated a total of 75M lines of code with Warp.
And because Warp is the platform and not a CLI-app running within the terminal, Warp has much richer UX capabilities than any CLI agent possibly can. For instance, unlike in CLI coding agents you can edit diffs directly in Warp’s native code editor; no context switching to an IDE required.
Finally, compared to IDE-coding agents, Warp is a much more natural interface. In a world where developers write less and less code by hand, there’s no reason to spend your day in an interface built for hand-editing code. As workflows fully adjust to accommodate agents, unified agent interfaces that support every part of your development workflow will feel more natural, and you’ll miss seeing code on ¾ of your screen less and less.
Agents: Multithread yourself
The primary way of working in Warp 2.0 is launching an agent by typing a prompt. We use the term “agent” broadly here – an agent is really just an intelligent task. These tasks can be anything – fix this bug, build this feature, resolve this git issue, tell me why this server is crashing – and they can range from very short-lived to tasks that run for minutes or even hours.
The flexibility of Warp’s agents gives developers tremendous power. They gather context using CLI commands, MCP, Warp Drive, and Codebase Context. They use the best models available and (optionally) present users plans before acting. Developers have complete control over agent autonomy – whether agents run on their own to completion, or check in more frequently.
Warp's agent management UI
As agents perform longer, more complex tasks, it’s natural to want to run more than one at a time. To handle this, we’ve built a management UI where you can see the status of all your running agents as well as in-app and system notifications when a running agent completes or needs your help.  This multitasking will become core to the agentic development workflow.
One global consulting firm reported a 240% increase in developer productivity after adopting Warp’s agentic workflows, highlighting the power of enabling engineers to multitask.
Terminal: Still a great command-line
If you are one of Warp’s half-million plus active users who use us as a terminal, that’s great – you’ll find that Warp still has the best terminal UX on the market. If you are new to Warp coming from a traditional terminal, you’ll love the productivity gains of working in a modern command-line.
Unlike other terminals, Warp has a rich, IDE-like experience for editing commands (and now prompts). The mouse works, you get completions and syntax highlighting out of the box, and we predict your next command.
Warp's input panel has rich interactions
In Warp 2.0, our input is even better. You can lock it into either command- or agent-mode, or let Warp detect. You get a host of AI controls directly available with no mode switching: pick your model, continue a conversation, attach an image or reference a file using the “@” key. It’s the most powerful way to run commands or prompt an agent.
Drive: Context for your teammates and your agents
The final capability is Warp Drive, a shared knowledge store for your team and your agents. It ensures that everyone on your team – human or agent – always has the right context for every task.
More specifically, Drive allows you to configure MCP and rules in a central location, so agents have all your organization’s context and understand your coding conventions.
Teams can store and share commands, notebooks, env variables, and prompts in Drive. Drive objects are available to teammates – especially useful during onboarding and firefighting – as well as agents doing long running tasks. This is highly useful for standardizing your team’s knowledge, workflows and conventions so that agents understand them and perform tasks in the same way a teammate would.
Warp 2.0 in action
Here are real examples of how we are using Warp to build Warp today.
Help me get oriented in a new codebase
In this video, I use Warp to help me understand how a feature is implemented in Warp. Warp explains how the Agent Management UI is rendered and how to add a new button.
Build a feature in an existing codebase
Warp replaces an icon within Warp. We have a custom UI framework built in Rust, which Warp navigates to make the change.
Multithreading myself in Warp
Here I made UI changes based on a linear issue, did some code review work, and reviewed logs at the same time in Warp.
And this is just the beginning. Warp is improving rapidly, and what is remarkable today will be table-stakes tomorrow.
Stepping back – our product philosophy
As we evolve Warp, I want to share a bit about how we think about building products in the age of agents.
Empower developers don’t replace them
Our first principle stems directly from Warp’s mission of empowering developers to ship better software more quickly and reliably: we are building an app to empower developers, not to replace them.
We believe that software development is going to evolve, but that the fundamentals of what it takes to build great software will remain the same. Professional developers are best positioned to make sure the world doesn’t end up with a lot of shitty, unusable products and unstable systems over the next few years. The basics of problem solving that make a great developer great are going to be as valuable, if not more, in the world of agents.
Warp has transformed how our technical teams work. As very technical people who are constantly context switching, Warp helps us solve problems with great speed and efficiency.
Development will happen at a higher level of abstraction; this is not a new trend, and in many ways is similar to the move from assembler to C to Java to Typescript. Every increase in abstraction has caused disruption, but ultimately developers will enjoy using agents to automate away the less interesting parts of their jobs.
Meet pro developers where they are
Our second principle is meeting pro developers where they already are, which in Warp’s case is in the terminal. Working with agents is a totally new workflow for most developers, and the best way to accustom them to it is by showing them the value of agents in the tool they are already using.
We designed Warp to work how professionals work. Warp is built to do extremely well on large, existing codebases and not just 0-1 apps, and our collaboration features mean you can grow with your team with Warp. Software production is a huge economic lever, and it’s the professionals who drive it forward. Plus, if it’s good enough for the pros, it will be good enough for everyone.
“Warp is a powerful example of how AI is reshaping the developer experience. By evolving from a modern terminal into a full Agent Development Environment, they’re unlocking new ways for developers to code, collaborate, and orchestrate agents. We’re excited to support Warp as they help redefine what building with agentic tools looks like.”
Lastly, we get that not everyone is ready to embrace agentic workflows. The technology is new, and while it’s getting better at a truly staggering pace, it’s not perfect yet. That’s why with Warp 2.0, developers can keep using Warp as just a great terminal. You can even turn all AI features off with a single toggle (I don’t recommend it, but it’s easy to do). Our goal is to show developers the value of agents rather than force them to adopt; we believe at some point all developers will realize the value, but it will take time.
Help developers improve
A lot has been made of agentic development making developers lazier, making it impossible to train junior engineers, or filling the world with crappy code. These are, without question, risks.
But we also think there’s an opportunity to help developers improve their skills with agents. Agents can explain code with infinite patience and always-on availability. They can suggest different approaches to problems, and walk you through in detail how systems are put together. Used properly, they can empower developers. I’ve seen this first hand within the Warp team. Developers jumping into new parts of the codebase are ramping faster, more independently than they used to, and as a leader I’m able to more quickly move engineers to the most important projects.
"Warp helped us onboard engineers a full week faster. That’s a week of engineering time we get back on every hire. By saving information all within Warp, we’ve reduced context switching and increased productivity"
From a product perspective, we are looking for ways to use agents to help developers improve. Can we make the agent really good at explaining, at challenging thinking, at making sure developers comprehend the work they are doing and consider options? Can we make sure developers understand their systems better? That’s our goal.
Control, transparency and privacy
We believe that the best experiences with agents are ones where humans are fully in control and in-the-loop. Agents need to earn our trust, and right now, for a lot of use cases, trusting them would be a mistake.
We approached this problem by giving developers granular control over how they work with agents.. In Warp, agent permissions are highly configurable and developers can:
Decide whether agents should auto-accept their code diffs
Decide whether agents can read files on your machine without human permission
Decide whether agents can run commands on their own
Create an allowlist and denylist of commands agents can or cannot run autonomously
Define which MCP servers can be used without asking for human permission
Pause agents at any point to course-correct
Different situations call for different levels of autonomy, so for any given task you can dispatch it to completion even if you start with approvals. And we intentionally started locally rather than having agents running around in the cloud, as cloud-based agents remove the human from the loop too early relative to the state of today’s technology and disempower developers.
On the privacy side, we have zero-data retention (ZDR) in place with our LLM providers and give all developers the ability to control what telemetry and crash reporting is sent. You can see exactly what data is leaving your computer using our Network Log. And if you don’t want any AI at all (again, not recommended) you can turn it off entirely.
Multi-threading as a force multiplier
Not only is the future agentic, it’s one where developers are coordinating multiple agents at once.  We are investing in supporting this workflow natively in a way no other app has. That means native support for multiple agent statuses, notifications, autonomy settings and more.
Warp agents can send in-app and system notifications
We have a real head start here compared to the competition, as the terminal is natively set up for running multiple-log running processes, managing permissions, showing linear updates and so on. I’m very excited to keep pushing this capability.
More AI, on us
To celebrate Warp 2.0, we're increasing AI request limits for all paid users:
Pro
: 1,000 → 2,500/month
Turbo
: 3,000 → 10,000/month (+ unlimited Lite requests)
Pay-as-you-go available after you use your monthly quota
What comes next
Warp 2.0 is just the beginning of the next chapter of Warp. We remain committed to our existing user-base, many of whom just want a better terminal. We also remain committed to empowering software developers to ship better, faster, and more reliably.
We’re building for a future where Warp is the primary—and only—tool developers need to ship software, but there’s work to be done to get us there. In the coming months, look forward to product updates including:
The ability to schedule or trigger tasks, for example summarizing user-logs every 3 hours
A revamped file-editing experience, allowing you to more comprehensively view and edit directly within Warp
File tree support natively in Warp, making it easier to track agent-changes across your codebase
And much, much more.
To those who have been using Warp already, thank you for your role in our journey. For those joining with this launch, welcome to the community.
Give Warp 2.0 a try, and let us know what you think.
Related articles
Apr 28, 2026  ·  4 min
The virtuous loop of open, automated development
With today’s open-sourcing of Warp, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
Mar 16, 2026  ·  8 min
What happens when you give the company 4 hours to automate everything
The Warp team held a company-wide hackathon to build with Oz, our cloud agent platform. Here's every project, from docs migrations to churn detection, that shipped in just 4 hours.
Feb 10, 2026  ·  12 min
Introducing Oz: the orchestration platform for cloud agents
Run hundreds of coding agents in parallel with full visibility and full control
