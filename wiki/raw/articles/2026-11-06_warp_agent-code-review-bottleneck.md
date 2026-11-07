---
title: "Addressing the code review bottleneck"
source: "Warp Blog"
url: "https://www.warp.dev/blog/agent-code-review-bottleneck"
scraped: "2026-11-06T06:00:22.613500+00:00"
lastmod: "2026-11-05T18:38:45.000Z"
type: "sitemap"
---

# Addressing the code review bottleneck

**Source**: [https://www.warp.dev/blog/agent-code-review-bottleneck](https://www.warp.dev/blog/agent-code-review-bottleneck)

Engineering
Addressing the code review bottleneck
Ben Holmes
|
November 5, 2026
How many agent PRs are awaiting your review right now? 10? 100? 1000?
“Too many” or “I’m tired” are valid answers too. That said, I’m not going to suggest that we let the bots win and merge without human review; that’s for a post-AGI world. Today, the goal is to cut the time spent on each code review, and reduce the barrier for shipping agent PRs to production.
There are three levers you can pull today to cut review times significantly:
Run rounds of adversarial code review
with your own review agent before a human looks.
Verify user flows end-to-end
with simulated environments, computer use, and automated checks.
Score and mitigate merge risk
on every PR so reviewers know what to focus on,
with a /merge-risk skill
you can use.
Let’s drill into each of these.
Build your own code review agent
Agents should run through their own internal code review process before a PR ever reaches a teammate. Think of this like doing a “make it work” pass (the code addresses the task) followed by a “make it good” pass (the code is well-architected for the next person).
It’s tempting to use an off-the-shelf code review agent for this. But it’s quite easy, and valuable, to build a code review agent yourself. It lets you define the grading criteria based on what
your
team cares about. Plus, owning the agent also lets you fine-tune its accuracy based on your own data. As
Addy Osmani calls out in Anthropic's code review process
, production incidents and reverts are high-signal feedback that something slipped through review. These can be turned into eval cases to improve the quality of code review over time.
It’s also common to have code review agents comment on the GitHub PR for the human to see. This works, but it creates noise that, in a majority of cases, doesn’t require human attention. It’s better to have your implementation and code review agents work together outside the GitHub thread, and only surface comments on the PR that require human input.
Here is the default loop that Warp Factories ships with:
The implementation agent hands off work to a code review agent.
The code review agent reviews the code and collects its findings as a list, noting the severity, impact, and the suggested change if applicable. If there’s ambiguity behind a change (i.e. code that goes beyond product decisions documented in context or in code), it hands back to the human for input. In the case of Warp Factories, this would be on the Slack thread of taskboard ticket where implementation began.
The implementation agent reviews these findings and addresses anything it can fix.
The code review agent flags more findings, and the cycle repeats until everything is settled or N max turns are reached.
Because multiple rounds of adversarial review can get expensive, we have also been experimenting with a gate in front of the reviewer to decide whether review is needed. In our early benchmarks on cost-to-quality against our own full-stack systems, we found that restricting multi-round review to larger features
is a viable option
. We’ll share more findings here soon.
Eval your code review agent
Once you set up a code review agent, you'll also want to evaluate the quality of those code reviews over time. This includes both the quality of the reviews themselves and downstream metrics like cost-per-PR, cycle time, and incident rollbacks.
In Warp Factories, we have dashboards for tracking those metrics, along with qualitative scoring for code quality, efficiency, test quality, and other failure modes.
These qualitative scores are driven by an LLM-as-a-judge using scoring rubrics across each metric. You can have this LLM-as-a-judge eval the full agent conversation, or eval the code review subagent specifically. From there, a self-improvement agent reviews the scores given by this LLM-as-a-judge to propose improvements automatically.
/skill-doctor
is a simple way to try this pattern yourself.
Give agents a computer to verify their work
Would you trust a PR written by a coworker that they didn’t verify on a local build? Hopefully not, and the same should go for agents.
You should give the agent tools to test the application as if it's a user. For backend systems, this means simulating the environment realistically: standing up a staging database, injecting test credentials for the agent to use, and capturing access logs to understand what the agent is doing.
For clientside changes, you’ll need commands for the agent to navigate around the application like a user.
The Chrome DevTools MCP
and
WebMCP
are model-agnostic options for web apps, but
computer use
is becoming more common across harnesses to test any kind of client application.
A computer-use-enabled model has its own virtual desktop to open the application and click around the application it built. In Warp Factories, computer use runs as a tool call that delegates to a computer-use subagent, which drives the computer and reports back screenshots and screen recordings as artifacts.
Once an agent verifies its work this way, these artifacts should be available to the human reviewer. Verification should also include both a before
and
after state to confirm what was changed. We suggest making test artifacts a required field on your PR description so an agent does this by default. Matt Pocock’s
/pr skill
is a good template.
It’s also important to prevent
over-
verification. If multiple screenshots are needed, they should be for distinct user flows rather than overlapping ones. Plus, recordings should be edited to remove dead space and jump to the part that’s worth human review. We added FFmpeg post-processing to Warp Factory agents to automatically slice out dead zones between agent actions. This can cut clips from minutes to 10-15 seconds in our experience.
Demonstration of the computer use tool built into Warp Factories
Have agents score and mitigate risk
Once the agent has reviewed and verified its own work, the human reviewer needs to understand the scope of the change, and which parts are worth the closest review. These are five criteria worth assessing:
Verification:
Is the code well verified, both with test coverage and end-to-end computer use artifacts?
Alignment:
Does the code follow the issue and PR description, or are there drive-by fixes and unintended side effects?
Impact:
What is the blast radius of the change, and is it touching sensitive code paths like auth, permissions, or billing? For sensitive systems, this is where you should
route reviews by code owner
so the right person is tagged into the PR.
Rollback cost:
How easily can this be rolled back, and what is the rollback procedure in the case of an incident?
Matt Pocock frames this
as a one-way door versus a two-way door, where a one-way door (like a destructive schema migration) is harder to reverse.
Error detection:
If something goes wrong in production, how much visibility will we have? Are errors swallowed, logged, or reported to an error monitoring service? That last option is ideal for agent visibility to fix their own mistakes. For example, we added a webhook to monitor for Sentry alerts and relay reports to our software factory agents for investigation.
These five categories help you decide how much human oversight a PR actually needs. If you want to spot-check your own PRs against these criteria, we created a
/merge-risk skill
to score the risk and highlight what needs the most attention.
It’s also worth bringing some of these criteria into the PR description, namely testing procedure, rollback cost, and impact.
Matt Pocock's PR template
and
Anthropic's internal code review template
both follow similar lines.
You can also have your agent run the
merge-risk skill
as a last-mile step to catch risky changes early:
Strip out unaligned changes to avoid drive-by fixes
Add error monitoring on new paths for better tracking
Break up high-impact changes into stacked PRs for simpler review
Avoid code sensitive paths if it can achieve the same outcome
And of course, verify work end-to-end with screenshots and recordings
Reduced risk doesn’t mean zero risk
None of these remove the human bottleneck on code review; engineers should continue to stay involved in how a codebase evolves. All of these are meant to a) increase trust in the work an agent delivers, and b) reduce the human attention needed to get work to the finish line.
To start, try adding fields like “impact” and “rollback cost” to your PR descriptions to pick out the low-hanging fruit. Then, layer on a code review step, and add computer use for deeper verification than e2e tests can provide. Focus engineering on the systems driving your agents, instead of reviewing every PR line-by-line.
We’ll be hosting a live session on November 10th to dive deeper into implementing these ideas.
RSVP
so you don’t miss it!
Resources
Merge risk skill
: A five-category rubric for scoring alignment, impact, verification, rollback cost, and error detection.
Computer use in Warp
: How Warp agents launch applications, verify user flows end-to-end, and capture screenshot and video artifacts.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Nov 4, 2026
|
Engineering
11
min
Don’t vibe code your software factory
11
min
Oct 29, 2026
|
Engineering
9
min
7 core components for building a software factory
9
min
Oct 15, 2026
|
Engineering
10
min
Tactics for rolling out software factories: human and organizational changes
10
min
Oct 15, 2026
|
Engineering
7
min
The road to self-improving software
7
min
Sep 15, 2026
|
Engineering
12
min
Adopting the software factory model: crawl, walk, run
12
min
View all articles
