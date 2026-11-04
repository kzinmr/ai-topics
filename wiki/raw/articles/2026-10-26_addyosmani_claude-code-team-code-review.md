---
title: "How the Claude Code team does code review"
author: Addy Osmani (@addyosmani)
date: 2026-10-26
type: x_article
source: "https://x.com/addyosmani/status/2114604912520921136"
url: "https://x.com/i/article/2114604912520921136"
engagement:
  bookmarks: 34753
  likes: 13482
  retweets: 1569
  impressions: 2570989
tags:
  - agentic-engineering
  - coding-agents
---

# How the Claude Code team does code review

**Author:** Addy Osmani ([@addyosmani](https://x.com/addyosmani))
**Published:** 2026-10-26 (X Article)
**Source tweet:** https://x.com/addyosmani/status/2114604912520921136

We previously mentioned that Claude writes about 90 percent of the code for Claude Code. So how do we do code review at this scale? Who reads code anyway? What happens if code goes wrong?
This post describes our team's code review process at Claude Code and how we have improved it. Between June and September, we saw more than double the number of pull requests that were merged to the codebase for Claude Code, while the share of pull requests that had to be reverted fell by more than 40 percent.
We didn't stop doing code review. Instead, we've automated the majority of reading and tuned it to optimize for human time and effort. We've also made significant investments into improving the speed and ease of reverting mistakes.
Rethinking the goal of code review
With agents writing code, the volume of changes increases rapidly. In our monorepo, we went from approximately 2,500 changes merging each day in May to over 30,000 in September of this year.
While Claude Code is not in our monorepo, it has a lot of pressure on it as well. When you're moving fast like that, it becomes increasingly hard, if not impossible, to do code review manually, line by line.
Code review serves two purposes:
Detect and correct bugs before they ship
Develop a shared understanding of the codebase 
While this article focuses primarily on the first goal, we'll discuss the second goal toward the end of the post.
We view "did someone read the code?" as an imprecise measure of "what could go wrong with this change, and what check - automated or human - is the right one to catch it?"
This question also changed the timing of code review. Traditionally, code review was a check performed after the fact, when the code was written, the PR was filed, and someone waited for someone else to take a look. Instead, we've integrated code review into the workflow. It's more like a spellcheck that you continuously do while writing. 
The majority of changes have already been reviewed and corrected by Claude, at least once, before a human is asked to take a look. In this way, we catch most of the routine bugs and reserve human attention for more high-level considerations.
Human time and attention 
We want to reserve human time and attention for things only humans can handle, while making sure we have enough automation to cover the rest. Even at our current pace, there is still an incredible amount of work for humans to do, and our team is encountering new and novel challenges almost every day.
For this reason, human time is a dual-sided cost. Not only do we count the time people spend doing code review, but also the time that they spend fixing bugs that are introduced by bad code. If we reduce the first without reducing the second, we're not really saving human time.
So, our goal is that the majority of pull requests in our Claude Code repos (the CLI, the desktop and web apps, and the mobile apps) should merge with a maximum of one person in the loop (who could be the author) without an increase in reverts or incidents. 
We track our human time in terms of median human approvals per PR (along with the 95th percentile), the number of human comments, and how long a PR waits on a person. We use the revert and incident rates as a guardrail: if these metrics increase, we haven't reduced human time, just relocated it.
What's the journey of a change?
A typical change, whether it's from an engineer's laptop or a Claude session in Slack, goes through multiple layers of review. 
 
Above is the typical Claude Code change, from the author's environment to production. Most of this process is automated, with human attention focused on the risky part. 
We have six layers of checks with a rollback mechanism to handle any issues that get through.
 
Each layer catches some bugs while missing others. Few bugs get through all of the layers, and if some do, we have a rollback mechanism in place.
1.Pre-PR verification:
Most of our review is done before we create a PR. We ask Claude to do something runnable, such as running tests, the build, or comparing a screenshot to the design. Instead of saying the task is done, we ask it to show us the result. Then, a subagent reviews the diff with fresh context. Both these strategies are part of our guide to best practices.
Before opening a PR, many of us also run a handful of internal skills -- bug hunting, diff reduction, end-to-end validation, and checking our UI changes against our design guidelines.
According to Boris Cherny, who created Claude Code, equipping Claude with a verification process is probably the biggest key to higher quality outcomes.
He estimates that a verification process improves the quality of Claude's output by a factor of two to three.
The verification process for any given domain can be very different:
Sometimes it's as simple as running a bash command. Sometimes it's running a test suite. Sometimes it's testing the app in a browser or phone simulator.
If the automated reviewer is consistently flagging the same issue, we fix it at the source -- via the skill itself, a lint rule, or updating documentation files like:
CLAUDE.md -- The project description file that you can use to give Claude context about the project (technology stack, conventions, goals, non-goals). Claude Code pulls this file in for every single review, so we keep it brief for large codebases and reference the rest of the documentation here. When code breaks a convention in this file, or an update makes something in it out of date, the reviewer flags it.
REVIEW.md -- The file where code owners tell the reviewer what matters in their part of the code. We separately verify whether the reviewer is actually following these guidelines. Good ones are brief and focus on:
Defining project failure (the docs should not lie; the config should not misroute) Limiting nitpicking Defining ignored paths Requiring file + line reference, not guessing filenames Requiring top-level summary including count and clear statement of "no issues"
2. AI review on every pull request
Every PR receives a Claude review before a human review. 
The diff is analyzed against the entire codebase and the intent of the PR as stated by the PR author. It checks that: the change actually addresses the issue the change fits into the larger system the change does not break other parts of the codebase
When reviewing a bug fix, the bot tries to find the root cause.
Our public product, Code Review for Claude Code, is now available to all Team and Enterprise customers. There is a lighter version for local use as well -- /code-review.
Since we released the research preview, the share of our internal PRs getting substantive review comments has gone from 16% to 54%. Code Review detects issues on the majority of PRs with more than 1,000 lines and returns clean results on most smaller PRs. Repos can be configured by admins to use Quick, Standard, or Deep modes. Deep is useful in cases where the cost of missing a single bug is higher than the time spent reviewing code.
Findings are vetted by multiple other agents before human review:
Multiple agents run in parallel to hunt for bugs 
A separate vote decides if a finding is valid or a false positive, only confirming the findings that have enough votes 
Findings that are only style/diagnostics/cleanup related are filtered out (we A/B tested these filters on our own PRs before rolling them out)
The remaining findings are presented as inline comments, ordered by severity level and marked as:
Important Nit Pre-existing (so we don't unfairly penalize the author for bugs that were not introduced by the PR)
All findings must be addressed -- fixed or the thread is resolved with a reason. In many cases, an agent will fix the problem overnight so the author returns to a PR that's already been through another review pass.
3. Security review that can block
We also run an automated security review. No PR can be merged while there is still an open finding (either from the code review or the security review). The author can either fix the issue or close the thread with a short reason (how we deal with a false positive).
A finding will be auto-closed if a subsequent commit addresses the problem. You can set up the same thing with the open-source security review GitHub Action, or the /security-review command. See automated security reviews in Claude Code for a guide on how to set this up.
4. Automated checks that block
Standard checks: lint, type checks, tests on all platforms, build. (We wrote about how we scaled CI here.) A typical CLI PR can have dozens of checks run before anyone looks at it. The PR template has questions about how the change was tested and how to revert it. Claude can answer those for you, but the author is responsible for reviewing them.
5. Human approval, scaled by risk
Some changes are more risky than others (e.g. a docs fix vs. an auto-updater change), so they require different levels of review.
 
The tier is determined by the change, not the author. A classifier determines the risk level based on the change. Another classifier determines if a particular change actually requires another approval, even if the tier does not say it does. Some paths always require another approval -- anything marked as sensitive by owners, and any CI workflow file.
Only authors on the repo's trusted list receive relaxed review requirements, and that's generally the team that owns the repo. All others require a second person to approve. Agent approvals don't count as human approvals. Automated review can clear a low-risk change, but it can't stand in for a human when one is required.
The author of the change is responsible for it, so if an agent authors a PR the operator of the agent is always counted as one of the required reviewers. A PR approval is only good for one commit. If a new commit lands that can't be trusted (e.g. an agent pushed something, or someone resolved a merge by hand), the PR must be reapproved.
6. Merge queue, feature flags and staged rollouts 
The merge queue ensures that all the checks run on main with the change applied. This prevents merging two successful PRs into a broken main. Typically, new features are rolled out behind a feature flag, with Anthropic employees getting access first. Because we use the product extensively, we often notice regressions before our users do.
When we roll out publicly, changes go to the latest channel first, and the stable channel trails behind. 
7. Fast feedback and rollback 
Some bad merges will inevitably make it through. This is our last line of defense, focused on identifying these as quickly as possible. Changes behind feature flags can be disabled without deploying.
Claude Code runs a weekly on-call rotation and any incident reviews involve looking back to see what layer should have caught the problem. It's still up to the author and on-call to notice bad merges, in addition to monitoring the revert and incident dashboards. We don't yet have circuit breaker mechanisms that adjust approval requirements based on these, but it's something we're looking into as we're making progress toward less human intervention in merging. 
One team member noted that slowing down and reducing output can actually improve accuracy, but that's mostly because the amount of work being done decreases overall. Our priority is really on improving our ability to identify and correct issues quickly.
How we make the reviewer better
Our code review process is an ongoing cycle of improvement:
We use incidents as an evaluation metric. The team collected incident-causing PRs, their fix-forwards and reverts, and had the engineers who understand the codebase verify the location and correctness of each bug. The review system is evaluated daily against this collection.
 
Every incident adds to the collection and every change to the review system is evaluated against the entire collection.
To measure noise, we observe how humans react to the review comments. It's easy to improve our bug-finding rate if we're okay with reporting lots of non-bugs, so this needs to be regulated. We categorize each review comment into how the person on the PR handled it: fixed the issue, rejected it, clarified it as intentional, or decided it didn't matter. Additionally, we run the review system on PRs we know to be clean and observe how often the system reports something that would have resulted in a harmful change.
Our stated priorities are first, detecting real bugs, and second, reducing the number of review cycles.
It's more costly for an author to have to deal with a review comment when they're an agent. It only takes a second for a human to dismiss a nit, but when an agent has to address it, this results in another commit, and another cycle of review.
The review process must converge. It's possible for an agent author and an agent reviewer to cycle forever. We observed one PR in our CLI project cycle more than fifty times overnight, due to the back-and-forth between the agent author and the agent reviewer. This cycle was stopped manually, but it could have gone on indefinitely.
When we ran git blame on what the review system kept flagging, ~59% of it was code that had been there since its first pass. Essentially, the review system was rarely finding new bugs, but finding a few more old ones on each cycle.
We made this worse because we had gotten into the habit of running several review cycles by default, because each cycle can find a different bug. While it can be useful to iterate through several review cycles for a high-risk change, it's not needed for every PR. Our team started tracking the number of cycles-to-pass in addition to recall, and updated re-review to:
Limit the number of cycles. The review system asks the author to re-evaluate the approach after three cycles. Limit re-review to just diff after the initial cycles. Specify the class of bugs, so the author can correct all of them, not just one line. Avoid re-reporting issues already observed. The review agents are also run on the current codebase overnight, helping us identify historical bugs before they propagate.
 
Reduction in the average number of review rounds per internal pull request after Convergence.
Humans in the loop
Having a senior engineer stop working to review a common error is an expensive process compared to automating that process. Human reviewers are still essential for some tasks:
Should we even build this? Deciding whether or not to build something, setting the vision, taste, and goals for the product.
One team that claims they have solved the bottleneck of code review still performs human review for changes from outside the team to ensure that it is the right thing to build.
Auditing dangerous code (billing, auto-updater, CI workflows).
Architecture review, because those choices set the conventions others follow.
Verifying proofs (test output, commands run, screenshots, reviewer comments). If you can't describe what the checks would miss, don't ask for a 👍, you need a real review!
Taking responsibility. A person answers for every change that ships, whoever typed it.
Team context
Code review has always served the dual purpose of communicating codebase changes. Reading the diff of a colleague's change is how people usually understand what has changed, and how the codebase works. If the bulk of the reading is done by machines, what becomes the way to learn the codebase?
We don't have any formal mechanism for this. No member of the team has a full mental model of Claude Code in their head, nor do we think anyone needs to. Rather, when anyone wants to learn about a piece of the codebase, they ask Claude to generate an explainer about that exact slice. It only takes a few minutes and the explainer is always up to date.
 
For some of us, we go the extra step and have Claude generate a mini artifact that visualizes this area and teaches it in our preferred style.
This is a better way to focus our human attention than reading trivial diffs line by line, which teaches you very little (e.g. a one-line copy change). Creating an explainer about the module you're going to change teaches you a lot.
Plus, we're generally open by default, working in open Slack channels, and seeing what others are building as they build it.
"You land it, you own it"
If you merge a small or medium change, and something still goes wrong, the general expectation is that you usually fix it yourself. There are a few reasons why this doesn't spiral out of control:
Small changes that are easy to review, debug, and revert.
Everything can be reverted. Feature flags, reverts, and staged rollouts can reverse most mistakes in minutes.
Blast radius sets the bar. More expensive code gets more eyes and validation.
Regressions are surfaced quickly by telemetry and internal usage.
It's not a blame game. The person who fixes the issue owns it because they have the most context. Incident reviews consider the system.
Plus, much of the team shares responsibilities by working in open channels. Anyone can see what others are building, join in on the conversation, or have Claude look for gaps. Feedback also comes from non-code owners. That openness is a big part of why quality stays high without a gate on every line.
Changing course
With agents, it is cheap to start new work, but sometimes you shouldn't. This typically arises when someone in the channel calls out the proposed change as an invalid path (citing previous decisions or suggesting a better path), and the author either closes the PR or changes the implementation.
Because it was easy to write the code in the first place, it doesn't feel like a loss to close the PR. The key is to pivot early in the thread, instead of waiting until the end to make a blocking comment on a finalized PR.
How to implement
Most of the components of this approach are already available to your team.
Before the pull request
Give the agent a checklist of checks it can run. List these checks in a short CLAUDE.md file
Set up the agent to call formatters and linters via hooks
Run /code-review and /security-review locally or have a new-context subagent review the changes
Create a REVIEW.md, and use it to track recurring review issues
On every pull request
Enforce CI
Update your PR template with "Testing", "Risk" and "How to revert"
On one repo, add an AI reviewer (Code Review for Claude Code, or the Claude Code GitHub Action), and iterate on your REVIEW.md for a few weeks before rolling it out to more repos.
Add an automated security review
Require that all review threads be resolved before merging
Apply review rigor according to risk: a quick pass for routine changes, and a thorough review for high-risk areas (where bugs are expensive). Code Review has Quick, Standard and Deep levels.
Limit the number of review rounds, and after a few rounds, just review the new diff.
Approval
Define risk levels, which are set based on the change, not the author. Start strict, and progressively relax as you see evidence.
Reserve lenient approval paths for trusted authors.
Bot approvals cannot be used to satisfy a required approval. Dismiss any approvals when new commits are pushed.
Designate humans as the approvers for code and policies controlling auth, billing, CI, and release workflows, as well as installers. Use CODEOWNERS and branch protection for this.
Merging and post-merge
Set up a merge queue
Experiment with feature flags
Launch to internal users first
Roll out in stages
Create a one-step revert mechanism
Build a set of evals by logging incidents and reverts
Rescore the reviewer any time you change its prompts, tools or model
Track human effort, using reverts and incident rates as guardrails
Where this is headed
Code Review was announced with the intention that the final approval decision would still be made by a human. All the product does is post its findings. But in our own repos, we are going further: Owners are deciding which low-risk changes can be merged automatically when the automated checks pass. And this boundary will continue to evolve.
So whenever our reviewers miss something, we ask ourselves what wasn't in the model's context, and turn that into a CLAUDE.md file, a skill or a new check. And we haven't changed our goal: To reduce the amount of human effort per change while keeping our revert rate no higher than it is now.
So if you also allow agents to create pull requests, please let us know what checks you've automated, what requires a human, and what we're getting wrong.
A rewrite of our original article and checked with Pangram.
