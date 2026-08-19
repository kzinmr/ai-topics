---
title: "How Vercel used Cursor to build Queues · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/vercel"
scraped: "2026-08-18T06:00:27.967806+00:00"
lastmod: "2026-08-18T06:00:26.830Z"
type: "sitemap"
---

# How Vercel used Cursor to build Queues · Cursor

**Source**: [https://cursor.com/blog/vercel](https://cursor.com/blog/vercel)

Blog
/
customers
Jul 28, 2026
·
customers
How Vercel used Cursor to build Queues
Vercel Queues was built entirely with Cursor. Power users saw a 54% increase in PR throughput, an 89% decrease in PR cycle time, and 104 hours saved per developer annually.
5 min read
Contact sales
Table of Contents
↑
Cursor offers the best harness and developer experience
Access to all the best models
Intelligent context management
A unified workspace for the entire software lifecycle
Building Vercel Queues with Cursor
Measuring impact
Expanding beyond engineering and turning PMs into builders
Vercel is a Cloud Infrastructure company in North America.
54%
Increase in PR throughput
89%
Decrease in PR cycle time
27%
Decrease in resources allocated per feature
104 hrs
Saved per developer annually
Vercel Queues
Product built entirely with Cursor
Vercel is a Cloud Infrastructure company in North America.
54%
Increase in PR throughput
89%
Decrease in PR cycle time
27%
Decrease in resources allocated per feature
104 hrs
Saved per developer annually
Vercel Queues
Product built entirely with Cursor
Vercel Queues, one of Vercel's most important new infrastructure products, was built entirely with Cursor, with agents writing code and testing it end-to-end against real AWS environments. Engineers at Vercel turned to Cursor for intelligent context management across long agent sessions, integrated code review for PR stacking, and seamless model switching.
Vercel has seen an inflection in PR throughput (54% increase), cycle times (89% decrease), and productivity for its heaviest Cursor users. The company has also expanded coding agent adoption beyond engineering, with product managers using Cursor to ship features, fix bugs, and run data analyses without relying on scarce engineering resources.
#
Cursor offers the best harness and developer experience
Joe Haddad is one of Vercel's longest-tenured engineers. He has spent the last seven years building Vercel's core infrastructure and now works primarily on critical backend systems.
He prefers Cursor over other coding agents because he believes the harness matters more than the model: "Cursor offers the best harness, and the platform has the smoothest developer experience of anything I've tried."
I didn't feel the AGI moment with Opus or GPT until I used it in Cursor. After that, my expectations for coding agents were raised so high that using those models in other coding harnesses became untenable.
Joe Haddad
Distinguished Engineer, Vercel
#
Access to all the best models
Haddad's preferred model has continuously changed as the labs keep releasing new models: "I was a steady Claude user through Opus 4.5, but when GPT-5.4 came out I started shifting more of my work over." In Cursor, Haddad can easily switch between providers, allowing him to pick the right model for the task at hand.
Whenever he starts on a new problem space, Haddad uses Cursor to compare which model performs best. He'll fire off parallel planning agents, review each plan, and then commit to the strongest one for that leg of work.
#
Intelligent context management
The other dimension where Cursor's harness stands out for Haddad is context management, specifically how it handles compaction. When agents run for extended sessions, they periodically compress their context to stay within the window. In other coding agent harnesses Haddad tried, models would lose critical details during compaction, forgetting how to run tests or failing to reference resources they had created earlier in the session.
In Cursor, those details were retained, allowing agents to handle complex, long-running tasks from end-to-end. "I could actually let Cursor run and compact itself six times over without any issues," says Haddad.
Without Cursor, even the best models struggle with context management. That causes them to stop prematurely or forget key details during their work.
Joe Haddad
Distinguished Engineer, Vercel
#
A unified workspace for the entire software lifecycle
Because Haddad works on critical backend infrastructure, every change goes through deep review. Cursor's integrated review experience lets him review agent-generated code inline, iterate with the agent, and then break work into stacked PRs that his team can review incrementally.
Haddad often works across many projects and tasks at once. While he works closely with a local agent on one focused task, Cursor's Cloud Agents let him delegate other work to run asynchronously in the background. He frequently kicks off agents directly in Slack conversations so they have context on an issue he's already been discussing with coworkers. Cloud agents handle everything from routine docs upgrades to more involved feature work.
Cursor's cloud agents are dependable and strongly sandboxed. This makes the cloud experience much more useful because agents can accomplish real work without constantly escalating to the user.
Joe Haddad
Distinguished Engineer, Vercel
#
Building Vercel Queues with Cursor
Vercel Queues is a durable event streaming system and one of Vercel's most important new infrastructure products. Haddad and his team built the product entirely with Cursor across three separate rewrites, each one refining the architecture based on what the team learned from internal dogfooding.
Cursor's ability to go beyond writing code to testing and verifying its work end-to-end against real infrastructure was essential for the ambitious scope of this project. Engineers would instruct agents to work on the Queues API, connect to AWS, read side effects from DynamoDB and Kinesis, inject faults, simulate bugs, and verify results. Haddad would repeat this pattern across each leg of work and hundreds of stacked PRs.
Cursor's harness allowed agents to ground themselves in production AWS environments with real resources. Agent-led testing was a significant part of meeting our quality bar with Vercel Queues.
Joe Haddad
Distinguished Engineer, Vercel
Cursor's intelligent context management allowed agents to remember every resource created, side effects observed, and test run across long sessions with multiple compaction events.
#
Measuring impact
Vercel tracks engineering velocity and quality through a few key metrics: PR velocity, time to first review, time to merge, and number of review cycles before merge.
The philosophy behind focusing on these metrics comes from Vercel's CTO, Malte Ubl, who coined the phrase internally: "Iteration velocity solves all known software problems."
Among Vercel's Cursor power users, PR throughput is up 54%, PR cycle time is down 89%, and resources allocated per feature dropped 27%. That works out to 104 hours saved per developer annually.
We have seen meaningful inflection in speed of PR velocity, time to review, and cycle times for our heaviest Cursor users. That's what we care about most.
Joe Haddad
Distinguished Engineer, Vercel
#
Expanding beyond engineering and turning PMs into builders
Vercel's adoption of Cursor extends beyond engineering. Product managers like Marcos Grappeggia use Cursor daily for work that would otherwise require pulling engineers out of their flow.
Common use cases for PMs at Vercel include:
Understanding the product.
Grappeggia loads multiple repositories into a multi-root workspace and queries across all of them. When a customer asks whether Vercel supports a specific feature, he can get an answer in the same meeting, along with an estimate of how much lift a change would require, without interrupting an engineer.
Product analytics.
PMs use Cursor with data warehouse CLIs and MCPs to dig into product usage patterns. Cloud agents can run for long durations to develop complex analyses that Vercel's data team doesn't have bandwidth for.
Shipping quick changes.
PMs use Cursor to one-shot small bugs and improvements that would otherwise sit in P2 backlogs indefinitely. A polling bug in the Vercel CLI's project linking flow was a quick fix implemented with Cursor that engineering wouldn't have gotten to for weeks.
PMs are using Cursor to ship features and fix bugs without requiring resources from other parts of the business.
Marcos Grappeggia
Product Manager, Vercel
Vercel is now focused on bringing coding agents into more workflows across the company, building on the patterns its engineers and PMs have already established.
If you're interested in bringing agents to every team that touches your SDLC, please
reach out to our team
to start a free Cursor trial.
Filed under:
customers
Author
:
Cursor Team
Vercel is a Cloud Infrastructure company in North America.
54%
Increase in PR throughput
89%
Decrease in PR cycle time
27%
Decrease in resources allocated per feature
104 hrs
Saved per developer annually
Vercel Queues
Product built entirely with Cursor
Vercel is a Cloud Infrastructure company in North America.
54%
Increase in PR throughput
89%
Decrease in PR cycle time
27%
Decrease in resources allocated per feature
104 hrs
Saved per developer annually
Vercel Queues
Product built entirely with Cursor
