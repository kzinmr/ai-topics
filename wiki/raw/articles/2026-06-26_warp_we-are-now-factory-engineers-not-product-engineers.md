---
title: "We are now factory engineers, not product engineers"
source: "Warp Blog"
url: "https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers"
scraped: "2026-06-26T06:00:30.609069+00:00"
lastmod: "2026-06-25T20:44:21.000Z"
type: "sitemap"
---

# We are now factory engineers, not product engineers

**Source**: [https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers](https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers)

Company
We are now factory engineers, not product engineers
Zach Lloyd
June 18, 2026
This is the memo I shared with the Warp team about what building Warp needs to look like. It’s a combo of context on what I’m hearing from customers, what I think the future of development looks like, and how the Warp team needs to adjust to be cutting edge.
Over the past year we have moved from AI Autocomplete to Interactive Coding Agents. Over the next six months the paradigm is going to evolve again to Automated Development.
In the world of Automated Development, the job of engineers is no longer to write code. It’s not even to build products. It’s to build an internal machine – a cloud software factory – that builds the products for them. The goal of this factory is to ship an incredible product, but the day-to-day job of the engineer is not to build that product directly – it’s to build the thing that builds that product.
Success is measured not by how many features an engineer ships; that’s a failure metric. It’s measured by the percentage of all changes that are shipped automatically, and at what cost. “Automatically” means an agent has done
all
the work: from triaging to spec’ing to implementing and reviewing and verifying and monitoring. If a change can’t yet be shipped automatically (and many currently can’t) then the goal is semi-automation, with an agent doing triage or verification, even if a human needs to step in at review. Have agents do as much as possible.
The job of every engineer is to improve the efficiency of their team’s product factory. Factory efficiency is roughly measured by shipped product / (inference cost + human time cost).
Companies are going to assess the efficacy of their factories in terms of ROI: if they spend a dollar on automation, does their business get more than a dollar of value? (Shipping product is an imperfect measure of value, but it’s fine for right now).
The days of giving all engineers unlimited token budgets to spend on interactive coding agents are ending. Instead, companies are going to treat software production as a variable cost, not an R&D expense. It’s going to show up as COGS on the P&L, because they are going to want to see the marginal gain of investing more and more in their software factories.
I'm writing this because this is the mentality we need to embrace at Warp. Every engineer must stop thinking that they are making changes to our codebase and our product directly and instead view everything through the lens of improving our factory.
Yes, while we are building and improving the factory, you are still responsible for improving the product directly – after all the product we ship is what creates value for customers and users; but whenever our factory fails, we need to learn from the failure and try next time to get further into the automation. Over time, the percentage of automation will go up and up until our job is purely improving efficiency, not pulling cars off the line to build them ourselves.
This is extra important for Warp because our company is now in the factory business. We are running a factory for improving our open-source Warp terminal that has almost a million devs relying on it improving. And we are shipping a
platform called Oz
to help other companies replicate this workflow on their most important products. The factory business is the only software productivity business that’s going to matter – if we are selling that, we better embrace its ethos ourselves.
What needs to change: the automation mandate
First, we must measure our throughput and efficiency. We must religiously look at how much product we are shipping autonomously, and how much it cost us to ship it. We are not yet doing that. The most important metrics to track right now are the
percentage of fully automated tasks
we are completing and the
cost of completing them
.
Second, we must force ourselves to approach everything
automation-first
. That means every time we use an interactive agent (aka human-in-the-loop) to write code, we view it as a failure to learn from. For every task, we should follow the factory workflow and only pull stuff off the factory floor where we need to. Right now we will need to do this often, and that’s fine. But the goal is to do it less and less.
The factory workflow is simple:
Triage agent runs and tries to understand and repro issue
If it determines the task is automatable → hand it to the implementation agent
If it needs specs because of ambiguity or scope → have the spec agent spec it
If it’s ambiguous → get human input and re-run, or just decide to park the issue for now
If necessary, the spec agent runs
Human reviews specs and then passes to implementation agent
Implementation agent writes code
Code review agent reviews code
Verification agent does computer-use or other verification
Human reviews code and verification output
If necessary, go back to step 2, 3, 4 or 5
CI / CD
Ship it
Monitor agent runs and creates issues if need be completing the loop
This workflow should already look familiar – it’s what we have built for our 60k star
open source repo
. You can see how that’s working at
build.warp.dev
. My view is that it’s half-working, but that we haven’t fully embraced it yet. I look at build.warp.dev and see 1300 issues in the ready-to-implement state and wonder “well, what are we waiting for? Let’s have an agent implement them.” We need to make it fully work.
Every time we need to bring a human into the loop, our platform Oz needs to record that and have
our self-improvement agents
try to improve the flow to make it less likely a human has to intervene again. Likewise, we need our self-improvement agents running over factory conversations looking for patterns of token waste and suggesting efficiency gains. We should be eval’ing different harnesses and prompts and noting which work best for the next execution.
Our primary job as engineers at Warp is to make sure this workflow is running smoothly and that Oz provides the best experience possible for supporting it. If we get this right, the factory will eventually reach a state of recursive self-improvement. This is the golden path.
This may sound like an embrace of drudgery, or maybe an idealistic but unrealistic vision of the world; like we are no longer getting to tinker with code or that we are going to spend all of our time reviewing agent-generated slop.
I view it differently. I view it as solving the last, most-important problem there is in software engineering – call it
meta-engineering
– which is engineering the system in which coding agents can most effectively build and ship useful stuff.
Yes, there is going to be a ton of pain in the short term where agents fail or we have to review their slop. But we must make ourselves experience this pain so that we can figure out how to automate it away. If we don’t, someone else will.
Our mission has always been to empower developers to ship better software more quickly. Letting them all build, manage and tune cloud software factories is the final product for this.
Related articles
Jun 12, 2026  ·  5 min
How Rectangle Health Built an AI Teammate That Writes Its Own Code
Rectangle Health used Oz to build a self-improving AI teammate that takes issues from triage through merged PR. The teammate, named Rex, currently ships 35K+ lines of code per week and has written over 50% of it's own code.
Apr 28, 2026  ·  4 min
The virtuous loop of open, automated development
With today’s open-sourcing of Warp, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
Mar 16, 2026  ·  8 min
What happens when you give the company 4 hours to automate everything
The Warp team held a company-wide hackathon to build with Oz, our cloud agent platform. Here's every project, from docs migrations to churn detection, that shipped in just 4 hours.
