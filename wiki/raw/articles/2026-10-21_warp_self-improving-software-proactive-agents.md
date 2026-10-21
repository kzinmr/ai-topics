---
title: "Self-improving software"
source: "Warp Blog"
url: "https://www.warp.dev/blog/self-improving-software-proactive-agents"
scraped: "2026-10-21T06:01:02.818420+00:00"
lastmod: "2026-10-15T22:28:58.000Z"
type: "sitemap"
---

# Self-improving software

**Source**: [https://www.warp.dev/blog/self-improving-software-proactive-agents](https://www.warp.dev/blog/self-improving-software-proactive-agents)

Engineering
The road to self-improving software
Ben Holmes
|
October 15, 2026
We’re all starting to think in systems to get better code out of agents. Maybe you’ve started adding loops for
computer use verification
, auto-fixing CI failures, and
adversarial code review
to get something worthy of review on the first pass.
These are huge steps forward in agentic development.
@poteto
calls this “building trust” with agents, which I really like.
But something feels unfinished about this. The ultimate goal when people talk about automating development (as in
a software factory
) isn’t to pump out PRs faster with
small
automation loops; it’s to create one
large
loop for software development itself. That loop starts with the task, and ends with the shipped product. How do we get agents to
proactively decide what to build next?
I think this will be the next challenge engineers face, and there are easy wins to do this today. Let’s walk through a few use cases we’ve started deploying that you can try:
Proactive bug fixes:
have agents monitor for errors and propose the next fix.
Proactive agent self-improvement:
have agents review their own conversations for failures, then propose improvements to their own agent skills and factory configuration.
Proactive product work:
have agents review user feedback on the product, from feature analytics to user interview recordings, to propose what features to build next.
1. Proactive bug fixes
The first idea, and maybe the most obvious one, is having agents fix their own bugs. And no, I don't mean proactively looking at a backlog. I mean figuring out what should be in the backlog in the first place.
There are a number of ways to detect bugs in systems, the lowest hanging fruit being server errors. Sentry and Grafana are common examples here: When errors are thrown from full stack systems, have an alert
tag in an agent to investigate
.
A simple version of this is having an agent read your codebase and report findings on that alert to Slack. A
better
version, though, is to give an agent the tools it needs to fix the issue and send the PR. This means computer use verification, adversarial code review… all of the small-loop automations I noted at the start of this article.
In a factory context, all it takes is a
webhook that can trigger an agent
on an always-on computer. In Warp, we configure this using an
automations file
, which binds a trigger referencing a webhook and sets an agent prompt and model to go address that alert.
Markdown
---
triggers:
  - provider: webhook
    event: received
    filter:
      webhook_ids:
        - 01a04b2e-4738-7d88-9004-6cc6d5b1540a
      payload:
        action:
          - triggered
---
You are the factory foreman handling a fatal Sentry alert delivered to the `sentry-fatal` webhook source.
…
This is a case of fully closing the feedback loop. Yes, we still have the human code review bottleneck before fixes are merged; It’s an act of risk mitigation
that’s worth improving
. But for the classes of bugs that you're alerted to, the friction of filing bug fixes no longer needs a human in the equation. The agent should fix its own bugs.
2. Proactive agent self-improvement
Now let’s talk about the system driving those agents. There’s a growing meta-skill in engineering to optimize your system of skills, code architecture, and agent automations to improve software quality down the line. You may hear this called gardening, meta-engineering, or
factory engineering
(my personal favorite).
Agents can help with this type of engineering by reviewing their own past conversations to find failure points. You might think of RSI (recursive self improvement) when you hear this, but we’ll be talking about a simpler idea:
skill self-improvement
.
The system works something like this:
Aggregate  all of the past agent sessions across your team. This includes the conversation traces, the tool calls, and the artifacts produced.
For each session, have an agent “score” the quality using
rubrics that you define
. We use an
LLM-as-a-judge
approach, but it could involve static analysis as well.
Once you have enough sessions scored, have an agent review all of the low-scoring conversations and look for common causes behind those failures.
Finally, let the agent propose changes to the codebase, the skills, or the AGENTS.md to prevent those failures moving forward.
Here's an in-depth diagram that shows what a complete
self-improvement loop
might look like. This uses an “efficiency” scorer as an example, meaning “did the agent reach a solution in the fewest steps?”
In the example, you can see the agent spins its wheels to work around bugs in its test harness, which the scoring agent flags as a common failure worth fixing in the skill definition.
See the full diagram breakdown on X
This isn't an example of improving the software itself, but it is an example of improving the process
behind
the software. This has indirect gains on the velocity that features can ship, the quality of those features, and the cost to deliver them. If you can make changes cheaper and quicker to add, you’ll start addressing issues you would’ve buried in the backlog. This goes back to building trust in your agents to confidently hit “merge” with less line-by-line scrutiny.
3. Proactive product work
The final example, and the most direct one, is having agents inform the product roadmap itself. This is the most sensitive area for agents to get involved in; product development is where human “taste” comes from, right?
I agree a human will always be in the loop for product work. But when deciding priorities on a product roadmap, there’s a lot that agents can do to reduce friction.
It starts by tapping into the customer data. You’re probably collecting information today on:
Which features are most highly used, and which are ignored
How every marketing page is performing on SEO and (maybe) AEO
What customers are saying about the product, both in user-experience interviews and candidly online
This data becomes much more valuable with agents, particularly agents that have access to the product’s source code.
We’ve started leveraging this today with our user experience calls. We use a service called Grain to record transcripts on customer discovery calls, which are compiled into a folder that's
accessible to agents via MCP
.
We’ve been using interactive agents to pull out insights and suggest roadmap items, which has been invaluable building an early-access product with first adopters. Here, an agent goes through prior customer interviews
on a regular cadence
and looks for commonalities in where customers get stuck.
At first, these insights have landed in Slack for the sales team to review, which is quite useful on its own. Now we’ve gone a bit further to turn these into usable tasks on our Notion board for
engineering
to review. We still require humans to review and accept these ideas. But in its completed state, agents could look through our existing roadmap, see if features are either underprioritized or missing, and fill in the gaps for us. This closes barriers in our org chart by putting the information where it matters: in front of engineers.
Closing the loop
I hope this gets your brain turning on how agents can close the development loop across all aspects of software: bug fixes, agent setup, and the product itself. If you're curious how to set up these automations, check out
Warp Factories
.
You can get
early access
or
book a demo
for a tailored walk-through of the platform.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Oct 15, 2026
|
Engineering
10
min
Tactics for rolling out software factories: human and organizational changes
10
min
Sep 15, 2026
|
Engineering
12
min
Adopting the software factory model: crawl, walk, run
12
min
Sep 2, 2026
|
Engineering
6
min
WarpBench: How we reduced our cost-per-PR 75%
6
min
Aug 27, 2026
|
Engineering
12
min
Closing the loop with self-improving cloud software factories
12
min
Aug 26, 2026
|
Engineering
8
min
The missing feedback loop for software factories
8
min
View all articles
