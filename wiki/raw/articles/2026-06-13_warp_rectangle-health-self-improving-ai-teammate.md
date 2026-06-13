---
title: "How Rectangle Health Built an AI Teammate That Writes Its Own Code"
source: "Warp Blog"
url: "https://www.warp.dev/blog/rectangle-health-self-improving-ai-teammate"
scraped: "2026-06-13T06:01:01.432714+00:00"
lastmod: "2026-06-12T19:36:06.000Z"
type: "sitemap"
---

# How Rectangle Health Built an AI Teammate That Writes Its Own Code

**Source**: [https://www.warp.dev/blog/rectangle-health-self-improving-ai-teammate](https://www.warp.dev/blog/rectangle-health-self-improving-ai-teammate)

Company
How Rectangle Health Built an AI Teammate That Writes Its Own Code
Olivia Johnston
June 12, 2026
Oz powers a custom AI Teammate, Rex, that wrote
54% of its own code
Rex currently writes
35,000 lines of code
per week to production
Problem: Scaling productivity gains from agents
Rectangle Health is a healthcare payment technology company with a 30-person engineering team building and maintaining software that touches some of the most sensitive data in any industry — patient records, credit card transactions, PCI compliance, HIPAA.
Like many engineering teams at growth-stage companies, Rectangle Health's developers were spread across a fragmented AI tooling landscape. Different engineers had adopted different tools — GitHub Copilot, Cursor, JetBrains Junie — and the team had no unified way to leverage AI across projects or share the productivity gains one developer found with another.
Especially during busy sprints, the Rectangle Health team was accumulating small bits of tech debt: low-priority bugs like misaligned buttons, or slow SQL queries that sat untouched for months, not because the team couldn't fix them, but because there was never a dedicated resource available when the backlog shuffled them to the bottom.
Rectangle Health needed a way to actually scale agentic workflows across their team to reduce tech debt and increase velocity.
Solution: Rex, the self-improving ticket to PR agent that lives in Slack
A VP of Development introduced Matthew Chastain, a Senior Software Engineer at Rectangle Health, to Warp. What immediately appealed to him was simple: Warp wasn't another IDE extension. It lived on a second monitor as a standalone application, letting him seamlessly work across projects with different tech stacks.
When Warp released Oz, the cloud orchestration platform, Matthew started experimenting during a busy period at work. He began building with Oz for fun, wiring agents into Rectangle Health's existing Jira workflow so that when a development ticket was created, an agent could take it all the way through to a pull request. Then, he built a Slack bot as a conversational front-end to kick off agents. Quickly, Matthew realized that spending time building specialized agents with Oz would allow him to increase his throughput more than writing code by hand.
Rex's agent architecture triages tasks and orchestrates them across one of 4 core agents or 6 subagents
Just a few weeks in, Matthew demoed his work to Rectangle Health's CTO and SVP of Engineering. The CTO had a test ready: a set of slow SQL queries that had been sitting at the bottom of the tech debt backlog for months. Matthew described the issue and let the agents run. They came back with two pull requests across two different repositories, showcasing cross-repo context the team hadn't seen from any other tool.
Today, Matthew's side project has evolved into Rex: an agentic solution where Slack messages kick off a triage agent to interpret intent, route requests, and orchestrate specialized agents for research, development, code review, and QA. Rex even has a self-improvement loop: it reviews its own runs, generates improvement proposals, and opens pull requests against its own codebase. 54% of Rex's code has been written by Rex itself.
Rex is available to engineers at Rectangle Health in public Slack channels and via DM, complete with a mascot, brand, and Slack emojis.
"It has been the most fun I've had developing in years," Matthew said.
Impact: From Side Project to Company-wide Infrastructure
What started as a personal experiment became something Rectangle Health couldn't ignore. In just 60 active development days, Rex contributed 139 commits across 11 Rectangle Health repositories, added 97,000 lines of code, and shipped 31 fixes directly to the company's flagship payment platform. The system now runs approximately 100 cloud agent runs per week, with a typical turnaround of 3 to 10 minutes from Slack @mention to a clickable pull request.
Today, Rectangle Health's entire engineering org is on the Enterprise plan, with Rex rolled out across the team. There are even separate initiatives from the Engineering, QA, and Product teams to build similar agents for a variety of Rectangle Health workflows on top of Oz — a sign that the idea of building with Oz has taken on a life of its own. The team is also actively integrating Warp with AWS Bedrock to manage inference costs more efficiently, and exploring self-hosted Oz infrastructure.
Matthew's pitch to other engineers is direct: "The flexibility of Warp and Oz Cloud is superior to anything else I've tried." For junior developers, he emphasizes something different — that Warp teaches as it works, making its reasoning visible and explorable, so engineers can ask it to walk them through a solution rather than just hand one over.
For Rectangle Health, Warp is now a central part of how they ship faster, more autonomously, and with more excitement as they build out lasting agent infrastructure.
Curious to see how it would work for your team?
Book a demo
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
