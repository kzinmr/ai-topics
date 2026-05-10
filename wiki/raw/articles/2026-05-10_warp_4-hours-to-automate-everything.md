---
title: "What happens when you give the company 4 hours to automate everything"
source: "Warp Blog"
url: "https://www.warp.dev/blog/4-hours-to-automate-everything"
scraped: "2026-05-10T01:27:05.391356+00:00"
lastmod: "2026-04-24T15:40:02.000Z"
type: "sitemap"
---

# What happens when you give the company 4 hours to automate everything

**Source**: [https://www.warp.dev/blog/4-hours-to-automate-everything](https://www.warp.dev/blog/4-hours-to-automate-everything)

Company
What happens when you give the company 4 hours to automate everything
Ben Holmes
March 16, 2026
This past week, the Warp team met in Tahoe for our semi-annual offsite. It's a time for the team to meet in person as a fully-remote company, to bond over ideas, and above all: to build together.
This year, we held a single-day hackathon to build something with our
Oz cloud agent platform
. We had full participation across the whole company: engineering, sales, marketing, and DevEx, and every team walked away with a working prototype.
We're pretty proud of the results. Here's everything we built.
Docs Migration: From GitBook to Astro Starlight
Team: Ben Holmes, Hong Yi Chen, Petra Donka
Our docs team works best in Markdown with GitHub PR reviews, and our existing hosted docs platform wasn't offering the flow they wanted. Plus, self-hosting could save $10k+ a year.
So, Ben, Hong Yi, and Petra used this hackathon to migrate the whole site from an external CMS to
Astro Starlight
, a Markdown-first framework with self-hosting on Vercel.
In just a four hour span, they:
Migrated all 266 pages, including video embeds, tab components, callouts, and image formatting
Built a custom Ask AI widget backed by Kapa that also improves the experience
Exposed all docs content as plain Markdown for agent and LLM accessibility
Set up hosting on Vercel, including proper preview deployments and better analytics
The next step before shipping to production is validation: using Oz's
computer use capabilities
to visit each page, capture screenshots, and compare against the GitBook source to catch anything that didn't transfer cleanly.
Grafana Oncall Analyzer
Team: Kevin, Maggie, Leon
A Grafana alert at 2am tells you something is broken. Kevin, Maggie, and Leon wanted to know what kind and how urgent before anyone starts investigating.
They built an agent that analyzes Grafana oncall alerts automatically, pulling relevant metrics, correlating them with recent changes, and generating a triage summary before anyone opens a dashboard. MVP is done and working locally. The team is migrating it off a personal server and tuning prompts for production.
Warp Offer Model
Team: Mac, Rosie, Erin, Pei
The talent team's offer process lived in a Google Sheet. It worked, until it didn't.
Mac, Rosie, Erin, and Pei built a custom offer model app: designed in Figma Make, wired up to Greenhouse for live candidate data, and built out as a proper web app. Candidates get a real interface to explore their offer. Recruiters get a consistent, maintainable tool. V1 is running. The next step is adding an auth layer and deploying it with infrastructure support.
PLG → Sales Pipeline Agent
Team: Emily, Olivia, Ian K, Ryan, Trevor
Emily's team built an agent that ingests product usage signals, scores users against a PQL model, and surfaces the highest-conversion-probability accounts to the BDR team in Slack each day. By the end of the hackathon, all the backend data flows were wired up and the agent was posting.
What's left: dialing in the scoring model, scheduling it into production, and building a richer UI beyond Slack. The core loop is running.
Oz Webapp Playwright Tester
Team: Ben Steidel
Ben wired Oz directly into Playwright so agents can spin up the Warp webapp against a
Mock Service Worker
environment and take actual screenshots. Those screenshots attach directly to the PR, so reviewers can see what the agent's changes look like in the browser alongside the diff.
V1 shipped at the hackathon and is already being used by Oz cloud agents on staging.
Stripe Churn Agent
Team: Tyler, Varoon, Advait
Tyler's team built an agent that queries the Stripe API daily, identifies top self-serve spenders who've churned or show risk signals, cross-references their AI and Warp Drive usage, and surfaces the results to the sales team.
MVP is working. Secrets handling in Oz was a friction point during the hackathon (they used a temp key to get unstuck). Next step is production data and tightening the analysis.
Vulnerability Bot
Team: Jeff, Andy
If Dependabot is a steady workhorse, Jeff wanted to build the version that drank a C4, a Celsius, and a white Monster and was "locked tf in."
The Vulnerability Bot goes beyond dependency bumps. It scans GitHub issues, Docker containers, and (stretch goal) Semgrep output for reported vulnerabilities, then actually tries to fix them, especially the ones that require real code changes rather than a version bump in a lockfile.
PR QA Engineer Agent
Team: Edward, John
Code review catches logic issues. Manual QA catches regressions. Neither reliably catches "did this PR accidentally break the login flow?"
Edward and John built an agent that triggers on new pull requests, reads the diff and description to infer which user flows are affected, spins up the app in a cloud environment, calls on
computer use
to walk through those flows before a human reviewer ever opens the PR. A mini bug bash, automated, on every PR.
Moma: Institutional Knowledge Search
Team: John R, David Stern, Matthew
How many times a week does someone ask in Slack "where's the doc on X?" and get five different answers, or none?
Moma is an agent-powered institutional knowledge search across GitHub, Slack, and Warp Drive. It's designed as a composable skill that any Oz agent can call, not a standalone chatbot, so the institutional knowledge becomes reachable from anywhere in the platform. The team hit some Slack auth token scope friction during the hackathon, but the core plumbing is largely in place.
Cherrypicker
Team: Aloke, Moira, Kevin C
Client release engineering at Warp involves a steady stream of cherrypick PRs from main to release candidates. It's necessary and it's a chore.
Cherrypicker is a Slack bot that tracks all outstanding cherrypicks, pings the right people when an RC is cut, and reports status throughout the client oncall rotation. A few core skills and flows were tested at the hackathon. The team is polishing and integrating it into the real oncall workflow.
And Many More
We had many more submissions from the week worth mentioning:
Anomaly Monitoring Agent
(Ian W, Chris, Erik): Flags sudden changes in growth marketing data that could indicate broken tracking or attribution pipelines, distinguishing "our numbers dropped" from "our tracking broke."
Fraud Finder
(Danny, Isaiah, Katarina): Automated fraud detection in Stripe, building a graph of connected accounts and spend to help make the case for account-level action.
PR Buddy Agents
(Safia, Erica): A suite of agents to improve PR velocity: smarter reviewer assignment, stale PR cleanup, and merge queue triage.
Keyboard Navigation Audit Agent
(Lili, Daniel): Audits Warp for keyboard navigability gaps, benchmarks against competitor keybinding conventions, and proposes improvements.
dbt Pipeline Fixer
(Wian): Receives webhooks on dbt job failures and opens a PR with a proposed fix.
Database Query Monitoring Agent
(Harry, Abhi, Lucie): Flags changes in database query load time across releases and analyzes possible root causes.
A/B Test Cron Agent
(Ben S): Reads previous test results and automatically sets up the next experiment.
AI UGC
(Eric): An agent trained on our internal thought leadership content to generate short-form video content. Yes, really.
Shipping It
The projects that moved fastest shared a pattern: the person who built it was also the person who'd use it every day. That's what made the difference between something that got to MVP and something that stayed on a slide.
Several are already in flight: the docs site is going through production validation, the PLG agent is close to fully scheduled, and the Playwright tester is already running on staging. The rest have owners and are on the roadmap.
If you want to help us build products and automations to ship faster,
we're hiring
. Come join us!
Related articles
Apr 28, 2026  ·  4 min
The virtuous loop of open, automated development
With today’s open-sourcing of Warp, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
Feb 10, 2026  ·  12 min
Introducing Oz: the orchestration platform for cloud agents
Run hundreds of coding agents in parallel with full visibility and full control
Dec 30, 2025  ·  8 min
Warp Wrapped: 2025 in Review
2025 was the year Warp became an Agentic Development Environment. Here’s a look at the numbers, launches, and ideas that defined it.
