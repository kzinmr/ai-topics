---
title: "How to build a cloud software factory - self-improving code review"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-self-improving-code-review"
scraped: "2026-07-17T06:00:49.843524+00:00"
lastmod: "2026-07-15T16:15:18.000Z"
type: "sitemap"
---

# How to build a cloud software factory - self-improving code review

**Source**: [https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-self-improving-code-review](https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-self-improving-code-review)

Engineering
How to build a cloud software factory - self-improving code review
Zach Lloyd
July 15, 2026
This is the third post in my series on how to build a
cloud software factory
:
Build an issue triage agent
Build a spec writing agent
[This post] Build a self-improving code review agent
I’ll describe how to build a code review agent, and how to have the quality of reviews it produces automatically improve over time. This is a follow on to prior posts where I described how to set up triage, spec and implementation agents as the first part of the factory.
Note that you could use an out-of-the-box platform for code review, but the nice thing about hooking it into a cloud factory workflow is that all of the factory agents follow a similar pattern and can share context (e.g. your code review agent can be aware of how your spec’ing agent writes specs, and can ask your verification agent to verify suggestions made in review comments). You also get complete control over the code review skill, freedom to select the model, and the ability to control how that skill improves over time. It is better to set yourself to automate the entire SDLC in my opinion, rather than just one piece.
To follow along and implement code review on your own repo, you can check out the demo code
here
.
Diving in, to implement the code review agent, we will create the following:
A code review skill that a cloud agent can apply to a PR
A Github action that invokes the skill
A second “outer-loop” agent that observes the code reviewer and improves it over time
Let’s start with the code review
skill, which I’ll base on the
skill
Warp uses for code review on its
popular OSS repo
.
The skill takes three inputs:
The PR description
The PR diff
The specs from the spec agent, if any
It returns a structured output called
review.json
.
Since the skill is run by a cloud coding agent like Claude Code, Codex or Warp, it can also leverage all the standard things a coding agent can do, like reading files, searching the codebase, building the code, writing tests, and so on. Having a fully fledged agent do code review lets it test hypotheses before it suggests any changes, make sure suggested changes build, and so on. It’s key to the workflow.
The body of the skill instructs the agent to review the code for security, correctness, style, etc. It provides detailed instructions on how to leave feedback inline, what counts as severe, important, or just a nit, what style to leave comments in, and so on. It instructs the agent to compare the code against the specs if they were provided, and to validate any changes it suggests. Finally, it provides a schema for structured output via the
review.json
so that the result can be transformed into a set of comments in Github.
The skill isn’t just a text file, it’s also a set of supporting python scripts that make it more deterministic and cost-efficient. I recommend shipping scripts as skill resources to avoid making the agent write them on-the-fly, which consumes extra tokens and introduces non-determinism.
What’s missing in the skill is any specific context around the coding conventions of a particular team or repo. Rather than adding these up front, we will create a second agent that learns those conventions as the review agent runs over time (more on this later).
The code review skill
In order to invoke the code review skill, we need:
A Github action to trigger it
A place for it to run in the cloud
The Github action is fairly straightforward and is mostly plumbing that’s not worth going deep on. At a high level, it runs on different PR state changes, gathers context about the PR, and then launches the cloud agent with the review skill.
For running in the cloud, we use a combination of Github actions + the Warp agent, as we have in the other demos in this repo, but there are many options you can use here. The nice thing about Warp though is that it’s multi-model and multi-harness, which is great for managing costs (and can run open-weight models). It also can be configured to run on any infra.
The Github action
Note that the agent is given read-only permissions for pull requests, and the GitHub action programmatically turns the agent’s
review.json
into GitHub comments
. We could give the agent
write
access to post GitHub comments directly, but this would introduce a prompt injection risk (like commenting on other PRs or even deleting the PR).
Here is an example
of a high-quality review agent output, with detailed inline comments and suggested fixes:
A PR level summary
An inline comment
If you respond to one of these comments and re-push code, the review agent is automatically set to run again. It will understand the prior context and threads and re-review as appropriate. It really is that simple.
You could leave things here and have a functional-yet-basic PR reviewer, but I want to show how you can set up this reviewer to improve over time using a self-improvement loop.
The loop looks like:
Over the course of a day, the code review agent runs on every PR
Human authors and reviewers interact with the comments left by the review agent, sometimes correcting them or validating what it suggested
Once a day, an “outer agent” runs, and reviews all of the PRs the code review agent did that day, synthesizing the human feedback
If the outer agent finds any knowledge that is worth remembering for future runs, it makes a PR to update the code review agent skill
The next time the code review agent runs, it incorporates that learning
This system isn’t perfect, but it does improve the quality of review over time as more relevant information about the team’s preferences makes it into the skill. This could be info around code style, or particular gotchas in the codebase, or info on how the review agent should validate suggestions, etc.
For this to work really well, you should couple it with metrics and evals to see how much you are spending on code review, how many cycles it takes, and how often the reviewer has to be corrected.  I’ll show how to create evals for these loops in a future post.
The outer loop improver skill
For my sample PR, I added both positive and negative feedback to agent comments and then observed how the outer agent adjusted the code reviewer to take this into account in the future.
Here’s some negative feedback, where I ask the agent to favor making structural code changes over adding comments.
And some positive feedback on it suggesting adding a timeout to http requests.
And this is the adjustment to the code review skill that our “outer loop” agent proposed in a PR. takes those two pieces of feedback into account, so future runs of the reviewer will be better:
I hope folks find this useful. To try it out, ask your agent to add the PR Review and Improve PR Review Skills + GitHub workflows from
the cloud factory demo repository
.
As I do more of these posts, we will get closer and closer to building an entire factory, one agent at a time. In the next post I’ll show how to add a verification agent that does computer use to check if a change is correct from the user perspective.
We are working at Warp on making this more turnkey, but I think there is actually a lot of value in learning how to set the agents up yourself to start.
Please let me know if you have any feedback or questions!
Related articles
Jul 7, 2026  ·  17 min
A guide to cloud software factories for engineering leaders
Software development is shifting from interactive coding agents to cloud software factories — systems that automate major parts of the SDLC while improving security, compliance, and measurable ROI.
Jun 29, 2026  ·  5 min
How to build a cloud software factory - add spec-driven development skills
This is my second post in a series on how to build out a fully automated cloud software factory. In this post, I’ll show how you can add spec-driven development for issues that are too complex or ambiguous to one-shot. The goal of these posts is to build a fully working...
Jun 25, 2026  ·  7 min
How to build a cloud software factory - the automatic triage skill
This post is the first in a series I’m doing on how to set up your own cloud software factory using skills and loops. It’s easier than it sounds to get something simple and effective running so you can start to automate significant parts of your team’s development flow.
