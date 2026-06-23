---
title: "How to build a self-improvement loop for your Skills"
source: "Warp Blog"
url: "https://www.warp.dev/blog/self-improvement-loop-for-skills"
scraped: "2026-06-23T06:00:29.645487+00:00"
lastmod: "2026-06-23T01:40:23.000Z"
type: "sitemap"
---

# How to build a self-improvement loop for your Skills

**Source**: [https://www.warp.dev/blog/self-improvement-loop-for-skills](https://www.warp.dev/blog/self-improvement-loop-for-skills)

Engineering
How to build a self-improvement loop for your Skills
Zach Lloyd
June 16, 2026
There’s been a lot of chatter about using “loops” lately to drive agents, and I think this has been accompanied by a bit of “what actually is a loop”?
I can’t speak for everyone else using the term, but I wanted to show a practical approach using Skills and cloud agents for a particularly powerful kind of loop: a self-improvement loop.
This is the idea that an agent can improve the quality of its own Skills over time from external feedback. My example is a loop that involves a human feedback step, but if you have a clear goal that doesn’t require a human, you can use the same method with an automated grader.
To make matters concrete, say this Skill does issue triage, separating incoming issues into a few buckets: ready-to-implement, duplicate, needs-info. This would also work for a code review Skill, a bug fixing Skill, an incident response Skill, and so on.
Here’s what a first draft of the Skill might look like:
Full triage-issue
Skill
What you need to do is set up the following loops:
An inner agent loop
: this is where you actually apply the Skill. For issue triage, you could be running it manually, or, more likely, you have an integration with your task tracker that runs the Skill whenever a new issue is filed. Interactions with the Skill are recorded somewhere: in a file, an agent trace, or an interaction in an external system like Slack or Github.
with the Skill are recorded somewhere: in a file, an agent trace, or an interaction in an external system like Slack or Github.
An outer agent loop
: this is an agent that runs on a schedule and observes the inner loop use of the Skill. For the issue triager, this will likely be a cloud agent that pulls records of every time the Triage agent ran. Its job is to look at all the runs of the inner agent and adjust its Skill based on the performance of those runs. Since Skills are just files, this means it should make a diff to improve Skill based on user feedback from past runs.
I’ll show you how to do this in practice using Warp and
Oz
, our cloud agent platform, but there are lots of ways you can accomplish it. We will use Github Issues as the issue tracker.
Here is a sample repo
with the Skills and GitHub workflows to follow along.
Step 1: set up the inner agent loop
The inner agent loop uses a Github action that runs on every new issue created.
Full GitHub Action
The Github action invokes a cloud agent through Oz, Warp’s cloud agent platform. This cloud agent syncs the repo, pulls in the issue contents from github, and tries to classify it. The code on how to set this up is in the repo linked below.
Now when a new issue comes in, a cloud agent runs the inner loop triaging skill, and applies a label indicating that a new feature request is ready to implement.
Step 2: set up the outer loop for self-improvement
Let’s say though that a human reviewer doesn’t agree with the agent assignment. As a person looking at the agent’s assigned labels, I switch the issue from “ready to implement” to “needs info” and add a comment on the thread as to why it was miscategorized, e.g. because there is ambiguity on whether we should add a setting for the new feature.
Here’s where the outer loop becomes interesting. The outer loop agent runs once a day and looks at all issues that have been triaged, and when it runs, it will find that I manually adjusted the label and gave a reason why.
Full improve-triage-issue Skill
Since the outer loop agent Skill is run through a coding agent, it will take the feedback I provided and make a diff to update the triage Skill.
Once that diff merges, it feeds back into Skill that drives the inner loop agent, and the next time the agent runs the Skill should work better.
Would love to know if this is useful for folks. We use self improvement loops to manage the Warp open-source repository, and we extracted the framework behind it for others to adopt.
Early version here
.
Related articles
Jun 18, 2026  ·  1 min
Generate interactive PR Walkthroughs with a single Skill
While we’re waiting for someone to re-invent Github I put together a useful skill that can help folks better understand agent (or human) generated PRs.
Jun 11, 2026  ·  2 min
Three skills you need for spec-driven development
Use Skills to guide agents through product specs, technical specs, implementation, and validation so spec-driven development is repeatable and reviewable.
Jun 2, 2026  ·  6 min
Why we tore down our no-code site and went back to code
Our marketing site sees over 10 million visitors a year. This past week, we launched a brand-new version — rebuilt from scratch so agents can work on it as fluidly as humans do.
