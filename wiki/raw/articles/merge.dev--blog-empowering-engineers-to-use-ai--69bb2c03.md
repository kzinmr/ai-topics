---
title: "How Merge empowers its engineers to leverage AI effectively"
url: "https://www.merge.dev/blog/empowering-engineers-to-use-ai"
fetched_at: 2026-11-19T10:03:57.597942+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# How Merge empowers its engineers to leverage AI effectively

Source: https://www.merge.dev/blog/empowering-engineers-to-use-ai

Our guiding philosophy for using AI in engineering is to give our team greater leverage.
As an engineering manager, it’s my job to turn this into reality through a combination of AI tools, structured workflows, and hands-on learning opportunities.
To that end, here are some of the most successful initiatives we’ve run so far.
Give engineers the autonomy to choose their tools
We want our engineers to choose the tools that work best for them, and that extends to AI.
Each engineer has a monthly budget that they can allocate on AI tool(s), including Windsurf, and Claude Code, and they can decide to spend that budget on one tool or on a combination of tools.
Our thinking is that if you force a certain tool on an engineer and they don’t like it for whatever reason, they just won’t use it.
That said, we’ve deliberately limited the choices to a few tools. Offering too many can make it harder for engineers to learn from each other.
Promote knowledge sharing through consistent demos
We have clear visibility on how much individual team members use AI tools, whether that’s the volume of prompts a user submits or the credits they’ve consumed.
We can use this data to proactively select individuals to showcase how they use AI during our team’s recurring all-hands meetings.
This not only helps colleagues uncover impactful use cases but also implicitly rewards the presenter for discovering valuable ways to use AI. And it encourages the rest of the team to do the same.
We also took this to the next level recently during our inaugural “Chainathon,” which was a hackathon-style event dedicated to exploring chained LLM workflows and agentic systems.
We trained our engineers (and everyone else at Merge) on using certain platforms, like Claude, n8n, Devin, and our new product,
Merge Agent Handler
(an MCP gateway), and gave participants an entire day to experiment.
Setting aside a space and time for our engineers to explore AI has helped unlock their curiosity and creativity. This has led to new automations that save our engineers countless time.
Implement specialized Claude sub-agents for repetitive backend tasks
In addition to resolving bugs, we use custom Claude subagents to automate repetitive backend work.
For instance, we often need to add new fields or query parameters to our APIs, which is straightforward but time-consuming.
To streamline this, we designed a Claude subagent with detailed prompt instructions on where to look in the codebase, how to model new changes, and what tests to include.
How we configured a Django API filter subagent in Claude
We’ve now built several of these subagents, allowing our team to lean on these agents across their day-to-day tasks.
{{this-blog-only-cta}}
Automate PR reviews with Windsurf
Code reviews are one of the most time-consuming parts of our engineering workflow, especially for small, repetitive changes.
To help my team move faster without sacrificing quality, we use Windsurf to automate PR reviews.
When a pull request is opened, Windsurf automatically analyzes the diff, checks for missing tests, inconsistent implementations, or inefficient queries, and leaves inline comments summarizing its findings. Our engineers can then review Windsurf’s feedback, choose which feedback to accept, and request another engineer to review it.
This workflow helps in a few important ways.
Now, every PR gets a baseline review for consistency and best practices, even during busy cycles. We’re also able to reduce the cognitive load on our engineers.
Taken together, reviews move faster, code quality is consistently higher, and our engineers focus on higher-level architecture or product implications across PRs.
Outsource bug fixes to an AI agent
AI agents can perform the tedious, repetitive tasks so that our team can focus on the more thoughtful, critical projects they’re uniquely equipped to handle.
Case in point: We use
Devin
, an AI agent for software engineers, to handle nit issues.
Here’s how it works: We have a Slack channel where anyone, whether they work in product or a go-to-market team, can flag minor bugs. I can then tag Devin and provide it with high level context on the issue and the expected behavior.
From there, Devin kicks off a predefined, asynchronous workflow:
1. Pulls the relevant GitHub repo
2. Sets up the developer environment
3. Makes the appropriate code change
4. Puts up a PR that tags the relevant engineers to review it
Devin can tackle nit bugs in a matter of seconds
Final thoughts
AI shouldn’t replace engineers; it should make them more productive.
We’re still learning how to embed AI naturally into our day-to-day workflows, but the results so far are undeniable: faster iteration, fewer repetitive tasks, and higher engagement across the team.
I also wouldn’t be doing my job if I didn’t mention that our engineering team is growing aggressively. You can check out all of our open roles and apply to any by visiting
our careers page
!
